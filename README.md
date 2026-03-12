# Awesome LLM Agent Papers / 大语言模型智能体论文精选

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/Brezzadimare/Awesome-LLM-Agent-Papers?style=social)](https://github.com/Brezzadimare/Awesome-LLM-Agent-Papers/stargazers)
[![Forks](https://img.shields.io/github/forks/Brezzadimare/Awesome-LLM-Agent-Papers?style=social)](https://github.com/Brezzadimare/Awesome-LLM-Agent-Papers/network/members)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A curated list of must-read papers on **Large Language Model (LLM) Agents**, organized by venue, year, and topic.  
> 精心整理的**大语言模型智能体**领域必读论文列表，按会议、年份和主题分类。

English | [贡献指南](CONTRIBUTING.md)

---

## Table of Contents / 目录

- [🚀 Usage / 使用方法](#usage)
- [📄 Papers by Venue / 按会议分类](#papers-by-venue)
  - [ICLR](#iclr)
  - [NeurIPS](#neurips)
- [🏷️ Papers by Topic / 按主题分类](#papers-by-topic)
  - [LLM Reasoning](#llm-reasoning)
  - [LLM Alignment](#llm-alignment)
  - [LLM Efficiency](#llm-efficiency)
  - [Agent Planning](#agent-planning)
  - [Agent Tool Use](#agent-tool-use)
  - [Multi-Agent Systems](#multi-agent-systems)
- [📊 Statistics / 统计](#statistics)
- [🤝 Contributing / 贡献](#contributing)
- [🔗 Related Resources / 相关资源](#related-resources)

---

## Usage / 使用方法 <a name="usage"></a>

### 1. Browse the paper list / 浏览论文列表

No installation is needed to read the lists.  
无需安装任何依赖，直接在 GitHub 上浏览 Markdown 文件即可。

- **By venue / 按会议浏览:** Open any file under [`papers/`](papers/) (e.g. [`papers/ICLR/2024.md`](papers/ICLR/2024.md)).
- **By topic / 按主题浏览:** Open any file under [`topics/`](topics/) (e.g. [`topics/llm-reasoning.md`](topics/llm-reasoning.md)).

---

### 2. Fetch new papers automatically / 自动抓取新论文

The [`scripts/fetch_papers.py`](scripts/fetch_papers.py) script queries **OpenReview** and **Semantic Scholar** to collect relevant papers for a given venue and year, and writes the results as a Markdown table.

该脚本通过查询 OpenReview 和 Semantic Scholar，自动抓取指定会议和年份的相关论文，并输出为 Markdown 表格。

#### Prerequisites / 环境准备

Requires **Python 3.10+**.  需要 **Python 3.10+**。

```bash
# Install dependencies / 安装依赖
pip install -r scripts/requirements.txt
```

#### Optional: API key / 可选：配置 API 密钥

Create a `.env` file in the repository root to avoid Semantic Scholar rate limits:  
在项目根目录创建 `.env` 文件可提升 Semantic Scholar 的请求频率上限：

```
SEMANTIC_SCHOLAR_API_KEY=<your-key>
```

> Get a free key at <https://www.semanticscholar.org/product/api>

#### Run the script / 运行脚本

```bash
# Fetch ICLR 2024 papers / 抓取 ICLR 2024 论文
python scripts/fetch_papers.py --venue ICLR --year 2024 --output papers/ICLR/2024_fetched.md

# Fetch NeurIPS 2025 papers / 抓取 NeurIPS 2025 论文
python scripts/fetch_papers.py --venue NeurIPS --year 2025 --output papers/NeurIPS/2025_fetched.md

# Also save raw JSON output / 同时保存原始 JSON 数据
python scripts/fetch_papers.py --venue ICLR --year 2024 \
    --output papers/ICLR/2024_fetched.md \
    --json papers/ICLR/2024_fetched.json

# Skip Semantic Scholar enrichment (faster) / 跳过 Semantic Scholar 补全（速度更快）
python scripts/fetch_papers.py --venue ICLR --year 2024 \
    --output papers/ICLR/2024_fetched.md \
    --skip-semantic-scholar
```

#### CLI options / 命令行参数

| Flag | Description |
|------|-------------|
| `--venue` | Conference name: `ICLR` or `NeurIPS` / 会议名称 |
| `--year` | Conference year, e.g. `2024` / 会议年份 |
| `--output` | Path for the output Markdown file / 输出 Markdown 文件路径 |
| `--json` | *(optional)* Path for a raw JSON dump / （可选）原始 JSON 输出路径 |
| `--skip-semantic-scholar` | Skip Semantic Scholar enrichment step / 跳过 Semantic Scholar 补全步骤 |

---

## Papers by Venue / 按会议分类 <a name="papers-by-venue"></a>

### ICLR

| Year | File | # Papers |
|------|------|----------|
| 2024 | [papers/ICLR/2024.md](papers/ICLR/2024.md) | 21 |
| 2025 | [papers/ICLR/2025.md](papers/ICLR/2025.md) | 21 |
| 2026 | [papers/ICLR/2026.md](papers/ICLR/2026.md) | TBD |

### NeurIPS

| Year | File | # Papers |
|------|------|----------|
| 2024 | [papers/NeurIPS/2024.md](papers/NeurIPS/2024.md) | 20 |
| 2025 | [papers/NeurIPS/2025.md](papers/NeurIPS/2025.md) | 23 |
| 2026 | [papers/NeurIPS/2026.md](papers/NeurIPS/2026.md) | TBD |

---

## Papers by Topic / 按主题分类 <a name="papers-by-topic"></a>

| Topic | File | Description |
|-------|------|-------------|
| 🧠 LLM Reasoning | [topics/llm-reasoning.md](topics/llm-reasoning.md) | CoT, math reasoning, test-time scaling |
| ⚖️ LLM Alignment | [topics/llm-alignment.md](topics/llm-alignment.md) | RLHF, DPO, safety, Constitutional AI |
| ⚡ LLM Efficiency | [topics/llm-efficiency.md](topics/llm-efficiency.md) | MoE, quantization, distillation, SSM |
| 🗺️ Agent Planning | [topics/agent-planning.md](topics/agent-planning.md) | MCTS, tree search, PDDL planning |
| 🔧 Agent Tool Use | [topics/agent-tool-use.md](topics/agent-tool-use.md) | APIs, RAG, code execution |
| 👥 Multi-Agent | [topics/multi-agent.md](topics/multi-agent.md) | AutoGen, ChatDev, MoA, role-playing |

---

## Statistics / 统计 <a name="statistics"></a>

| Venue | 2023 | 2024 | 2025 | Total |
|-------|------|------|------|-------|
| ICLR  | —    | 21   | 21   | 42    |
| NeurIPS | —  | 20   | 23   | 43    |
| **Total** | — | **41** | **44** | **85** |

### Topic Distribution

| Topic | Count |
|-------|-------|
| 🧠 Reasoning | 20+ |
| 🤖 Agents | 18+ |
| 👥 Multi-Agent | 8+ |
| ⚖️ Alignment | 8+ |
| 🔧 Tool Use | 6+ |
| ⚡ Efficiency | 5+ |

---

## Paper Format Example / 论文格式示例

Each paper file uses the following table format:

```markdown
| Title | Authors | Tags | Paper | Code |
|-------|---------|------|-------|------|
| [Paper Title](https://arxiv.org/abs/XXXX.XXXXX) | Author et al. | \`tag1\` \`tag2\` | [arXiv](https://arxiv.org/abs/XXXX.XXXXX) | [GitHub](https://github.com/...) |
```

---

## Contributing / 贡献 <a name="contributing"></a>

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on:
- How to add new papers / 如何添加新论文
- Paper format specification / 论文格式规范
- PR submission workflow / PR提交流程

---

## Related Resources / 相关资源 <a name="related-resources"></a>

- [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) — Large language model papers
- [Awesome-LLM-Reasoning](https://github.com/atfortes/Awesome-LLM-Reasoning) — LLM reasoning papers  
- [LLM-Agent-Survey](https://github.com/Paitesanshi/LLM-Agent-Survey) — Agent survey resources
- [Awesome-AI-Agents](https://github.com/e2b-dev/awesome-ai-agents) — AI agent frameworks
- [Papers with Code](https://paperswithcode.com/) — Find code for ML papers

---

<div align="center">
  <sub>⭐ Star this repo if you find it helpful! / 如果对您有帮助，请点个星！</sub>
</div>
