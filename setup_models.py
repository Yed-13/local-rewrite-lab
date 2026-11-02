#!/usr/bin/env python3
# SPDX-License-Identifier: CC-BY-SA-4.0
"""Fetch pinned public weights, reuse the HF cache, and prepare a HIP GGUF adapter."""
import argparse
import json
import shlex
import subprocess
import sys
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--profile', choices=['ataraxy', 'hip', 'all'], default='all')
    p.add_argument('--directory', type=Path, default=Path('models'))
    p.add_argument('--llama-cpp', type=Path, help='Checkout containing convert_lora_to_gguf.py')
    p.add_argument('--offline', action='store_true')
    for name in ['ataraxy', 'hip-base', 'hip-adapter']:
        p.add_argument('--reuse-' + name, type=Path)
    a = p.parse_args()
    from huggingface_hub import hf_hub_download, snapshot_download
    versions = json.loads(Path(__file__).with_name('model_versions.json').read_text())
    a.directory.mkdir(parents=True, exist_ok=True)
    paths = {}

    def link(source, filename):
        source = Path(source).resolve()
        if not source.is_file():
            raise FileNotFoundError(source)
        with source.open('rb') as f:
            if f.read(4) != b'GGUF':
                raise ValueError(f'Expected GGUF: {source}')
        target = a.directory.resolve() / filename
        if target.exists() or target.is_symlink():
            if target.resolve() != source:
                raise FileExistsError(f'Use a different model directory: {target}')
        elif target != source:
            target.symlink_to(source)
        return str(target)

    def weight(key, reuse):
        spec = versions[key]
        source = reuse or hf_hub_download(spec['repo'], spec['file'], revision=spec['revision'], local_files_only=a.offline)
        return link(source, spec['file'])

    if a.profile in ['all', 'ataraxy']:
        paths['MODEL_GGUF'] = weight('ataraxy', a.reuse_ataraxy)
    if a.profile in ['all', 'hip']:
        paths['HIP_BASE_GGUF'] = weight('hip_base', a.reuse_hip_base)
        if a.reuse_hip_adapter:
            adapter = a.reuse_hip_adapter
        else:
            spec = versions['hip_adapter']
            folder = Path(snapshot_download(spec['repo'], revision=spec['revision'], allow_patterns=['adapter_config.json', 'adapter_model.safetensors'], local_files_only=a.offline))
            config = json.loads((folder / 'adapter_config.json').read_text())
            if config['base_model_name_or_path'] != 'Qwen/Qwen3-4B-Base':
                raise ValueError('Adapter and Base model do not match')
            spec = versions['hip_config']
            base = snapshot_download(spec['repo'], revision=spec['revision'], allow_patterns=['*.json', '*.txt'], ignore_patterns=['model.safetensors.index.json'], local_files_only=a.offline)
            adapter = a.directory.resolve() / 'hip-adapter-f16.gguf'
            if not adapter.exists():
                if not a.llama_cpp:
                    p.error('--llama-cpp is required to convert the released adapter')
                subprocess.run([sys.executable, str(a.llama_cpp.resolve() / 'convert_lora_to_gguf.py'), '--base', base, '--outtype', 'f16', '--outfile', str(adapter), str(folder)], check=True)
        paths['HIP_ADAPTER_GGUF'] = link(adapter, 'hip-adapter-f16.gguf')
    (a.directory / 'paths.json').write_text(json.dumps(paths, indent=2) + '\n')
    for key, value in paths.items():
        print(f'export {key}={shlex.quote(value)}')


if __name__ == '__main__':
    main()
