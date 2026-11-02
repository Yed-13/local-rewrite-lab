# 从安装到全文输出

[English](QUICKSTART.md) · [项目首页](README.zh-CN.md) · [固定版本](model_versions.json)

## 环境与权重

需要 Git、Python 3.11 以上及 Xcode 命令行工具（macOS 使用 `xcode-select --install`）。两套配置及环境建议预留约 25GB 磁盘，内存有限时，同一时间只启动一个模型。

Ataraxy 使用 Gemma-2-Ataraxy-9B Q5_K_M，文件约 6.65GB。HIP 使用 Qwen3-4B-Base Q6_K（3.31GB）与匹配的 HIP f16 adapter（0.53GB）；转换前还会缓存约 1.06GB 的已发布 adapter。无需训练。模型、转换器和运行时分别固定版本，见 `model_versions.json`。

## 最低与推荐配置

| 运行方案 | 最低内存估算 | 推荐内存 | 建议 SSD 可用空间 |
|---|---:|---:|---:|
| HIP · Qwen3-4B Q6_K + f16 adapter | 8GB | 16GB 以上 | 12GB 以上 |
| Ataraxy · 9B Q5_K_M | 16GB | 24GB 以上 | 15GB 以上 |
| 两套依次运行，不同时加载 | 16GB | 24–32GB 以上 | 25GB 以上 |

以上按当前单并发上下文配置（HIP 2,048、Ataraxy 8,192 tokens），结合权重、缓存、运行时和操作系统余量估算，用于选择设备，并非逐档实测的硬件下限。内存指系统 RAM 或统一内存，不是独立显存；增加上下文、并发或同时运行其他应用会提高需求。

处理器建议采用现代 64 位 ARM64 或 x86-64，4 核以上可作为入门配置，纯 CPU 推理推荐 8 核以上。不强制要求独立显卡。全量 GPU 加速建议 HIP 预留约 8GB 显存，Ataraxy 预留约 12–16GB 显存；较小显存可配合充足系统内存进行部分卸载。Apple Silicon 使用统一内存，不将表中的内存与显存建议相加。设置 `GPU_LAYERS=0` 可仅用 CPU，运行速度会较低。

按设备选择 [llama.cpp 后端](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md)：Apple Silicon 使用 Metal，兼容 NVIDIA 显卡使用 CUDA，其他设备选择受支持后端。安装脚本不会自动启用 CUDA；可单独编译兼容服务并通过 `LLAMA_SERVER` 指定。权重体积见 [Ataraxy 模型页](https://huggingface.co/bartowski/Gemma-2-Ataraxy-9B-GGUF)及[固定模型配置](model_versions.json)。

```sh
git clone https://github.com/Yed-13/local-rewrite-lab.git
cd local-rewrite-lab
PYTHON=python3.11 sh bootstrap.sh all
```

将 `python3.11` 换成电脑上实际安装的 Python 3.11+。只安装一套时，将 `all` 换成 `ataraxy` 或 `hip`。脚本创建独立环境、复用 Hugging Face 缓存、准备权重并编译指定版本。完成后复制末尾打印的 export 命令，或执行：

```sh
export LLAMA_SERVER="$PWD/.tools/llama.cpp/build/bin/llama-server"
export MODEL_GGUF="$PWD/models/Gemma-2-Ataraxy-9B-Q5_K_M.gguf"
export HIP_BASE_GGUF="$PWD/models/Qwen3-4B-Base.Q6_K.gguf"
export HIP_ADAPTER_GGUF="$PWD/models/hip-adapter-f16.gguf"
```

已有同版本权重可复用，避免重复文件：

```sh
PYTHON=python3.11 sh bootstrap.sh all   --reuse-ataraxy /absolute/path/Gemma-2-Ataraxy-9B-Q5_K_M.gguf   --reuse-hip-base /absolute/path/Qwen3-4B-Base.Q6_K.gguf   --reuse-hip-adapter /absolute/path/hip-adapter-f16.gguf
```

最后一个参数可省略，由脚本转换官方 adapter。Linux CPU 可设置 `GPU_LAYERS=0`，Linux GPU 后端尚未通过这份安装脚本验证。依赖与权重准备好后，生成过程可离线运行；在线检测需要另外联网提交文本。

## 分段与生成

将正文另存 UTF-8 TXT，自然段之间留空行，保留原文件。此流程输出纯文本，不重建 DOCX 排版。

```sh
python3 workflow.py prepare examples/document.txt runs/demo/job
```

生成 `document.json` 回填计划和 `sections.jsonl` 输入。相邻正文合并为不超过 320 词的段落组，不切断自然段；单段超过上限时先在自然句界拆分。标题、Markdown 表格、引用块、代码块及 References 等文后内容保留。生成前查看计划，特别检查较短正文是否被识别为标题。特殊引文和文后标题需要调整文本布局或自行准备 JSONL。

终端 A 启动 HIP，等待模型显示 listening：

```sh
sh start_hip.sh
```

终端 B 在同一项目目录运行：

```sh
python3 hip_rewrite.py runs/demo/job/sections.jsonl runs/demo/hip
```

停止终端 A 后，比较 Ataraxy 单次改写：

```sh
sh start_server.sh
```

终端 B：

```sh
python3 rewrite.py runs/demo/job/sections.jsonl runs/demo/ataraxy
```

Ataraxy 可添加 `--style private/my_style.txt`，仅取前 2,800 字符；直接模式和 HIP 不需要个人语料。[个人语料准备](PERSONAL_CORPUS.md)。每个编号 JSON 保存输入、实际提示格式、参数、耗时和警告，TXT 保存候选。HIP 使用 source/target completion 格式；Ataraxy 使用服务端 Gemma 模板并检查分隔符。

## 核对与回填

```sh
python3 workflow.py review runs/demo/hip runs/demo/hip-reviewed
```

阅读 `comparison.md`，对照原文编辑编号 TXT。重点检查数字、单位、日期、术语、引文、因果与限定条件、遗漏和新增事实。数字检查会提示数字改成英文拼写，却可能发现不了 median 被改成 mean，因此需要阅读核对。

```sh
python3 workflow.py assemble runs/demo/job/document.json   runs/demo/hip-reviewed runs/demo/final-hip.txt
```

原有标题等保留块自动回填，已有输出不会覆盖。再次运行使用新目录。[公开运行样例](examples/expected/README.md) 提供真实候选、核对后输出及修改记录。样例是明确标记的虚构 AI 生成材料，与私有文稿检测成绩分开。

## 可选：末尾两组二次改写

固定组合规则：先核对 HIP 全文，只对最后两个正文组使用 Ataraxy，其余 HIP 内容保留。迁移效果见[选择性改写比较](SELECTIVE_REWRITE.md)。Ataraxy 服务运行时：

```sh
python3 workflow.py tail runs/demo/job/document.json   runs/demo/hip-reviewed runs/demo/tail.jsonl --groups 2
python3 rewrite.py runs/demo/tail.jsonl runs/demo/tail-ataraxy
python3 workflow.py review runs/demo/tail-ataraxy runs/demo/tail-reviewed   --original-plan runs/demo/job/document.json
```

再次对照原文核对后：

```sh
python3 workflow.py assemble runs/demo/job/document.json   runs/demo/hip-reviewed runs/demo/final-selective.txt   --overlay runs/demo/tail-reviewed
```

公开小样例总共只有两组，选两组等于处理全部正文；较长文章才体现局部替换。

## 真实检测与记录

在同一账号、扫描模式和相近时间内，分别提交完整原文与完整核对稿。GPTZero 使用 Advanced 扫描，记录实际分类、AI/Mixed/Human 三项概率，以及出现的 AI Paraphrased 标签。QuillBot、Originality 保留各自原生分数和分类。

复制 `examples/detector_results.csv` 到本地运行目录，每个服务、每版文本各写一行。记录检测时间、版本、字数、分数、分类和实际费用；未显示的字段留空，报错或额度不足单独标记。Human 分类数量与平均 Human probability 分开统计，不将其他平台的 AI 分数换算为 GPTZero Human 概率。检测平台接收你提交的文稿，不需要接收个人风格语料。

公开实现采用手动网页检测步骤，不包含绑定个人登录会话的浏览器自动化，也不要求购买 API。生成文本无需检测凭据。

## 常见问题

Python 报版本错误：通过 `PYTHON` 指定 3.11 以上版本。HTTP 503：模型仍在加载，等待 listening。端口占用：停止旧服务；Ataraxy 为 8085，HIP 为 8083。内存不足：只启动一个模型，关闭占内存应用，降低 `GPU_LAYERS`，或另选兼容量化并记录配置变化。模板错误：确认使用指定模型家族。HIP 输出异常：确认 Base、adapter 匹配，并使用专用入口。出现截断或生成上限警告：自然拆小段落，另存重跑并检查遗漏。下载中断：重跑复用缓存，不删除其他项目缓存。

实测验证：新建独立依赖环境、固定版本编译完成；两套模型均完成真实批量推理，HIP adapter 转换、核对副本和回填流程已运行。安装验证复用了已有权重，未重复下载数 GB 文件。
