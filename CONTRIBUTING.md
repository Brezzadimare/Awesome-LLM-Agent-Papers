# Contributing Guide / 贡献指南

Thank you for your interest in contributing to **Awesome LLM Agent Papers**!  
感谢您对本项目的贡献兴趣！

---

## How to Submit a New Paper / 如何提交新论文

### 1. Check for Duplicates / 检查重复

Before adding a paper, search the repository to ensure it is not already listed:

```bash
grep -r "arxiv.org/abs/XXXX.XXXXX" papers/
```

### 2. Paper Format Specification / 论文格式规范

All papers must be added to the appropriate venue + year Markdown file  
(e.g., `papers/ICLR/2024.md`) **and** any relevant topic file under `topics/`.

Each paper entry is a row in a Markdown table with the following columns:

| Column | Description | Required |
|--------|-------------|----------|
| **Title** | Linked paper title | ✅ |
| **Authors** | First author et al. (for ≥3 authors) or full list | ✅ |
| **Tags** | Backtick-quoted topic tags (see approved tags below) | ✅ |
| **Paper** | Link to arXiv / ACL Anthology / OpenReview | ✅ |
| **Code** | Link to official GitHub repo, or `-` if unavailable | ✅ |

**Table header template:**

```markdown
| Title | Authors | Tags | Paper | Code |
|-------|---------|------|-------|------|
```

**Row template:**

```markdown
| [Paper Title](PAPER_URL) | Author et al. | \`tag1\` \`tag2\` | [arXiv](ARXIV_URL) | [GitHub](GITHUB_URL) |
```

#### Approved Topic Tags / 已批准的主题标签

| Tag | Meaning |
|-----|---------|
| `reasoning` | General reasoning |
| `math` | Mathematical reasoning |
| `long-CoT` | Long chain-of-thought / extended thinking |
| `planning` | Task planning and decomposition |
| `agent` | Single-agent systems |
| `multi-agent` | Multi-agent systems |
| `tool-use` | Tool / API / function calling |
| `RAG` | Retrieval-Augmented Generation |
| `code` | Code generation / software engineering |
| `alignment` | RLHF, DPO, Constitutional AI |
| `RLHF` | Reinforcement Learning from Human Feedback |
| `DPO` | Direct Preference Optimization |
| `safety` | Safety and robustness |
| `benchmark` | Evaluation benchmarks |
| `foundation-model` | Foundation / base model reports |
| `efficiency` | Model efficiency, compression, distillation |
| `architecture` | Novel neural architectures |
| `scaling` | Scaling laws |
| `multimodal` | Vision-language, multimodal agents |
| `survey` | Survey / position papers |
| `data` | Data curation, synthetic data |
| `interpretability` | Model interpretability and analysis |
| `in-context-learning` | In-context and few-shot learning |
| `reinforcement-learning` | Reinforcement learning for LLMs |
| `self-improvement` | Self-play, self-training |
| `fine-tuning` | Instruction tuning, SFT |

If your paper does not fit any existing tag, propose a new one in your PR description.

### 3. PR Submission Workflow / PR 提交流程

1. **Fork** the repository.
2. **Create a branch** with a descriptive name:
   ```bash
   git checkout -b add-paper/neurips2024-swe-agent
   ```
3. **Add your paper** to the appropriate venue file and relevant topic file(s).
4. **Commit** your changes with a clear message:
   ```bash
   git commit -m "Add SWE-agent (NeurIPS 2024) to agent/code papers"
   ```
5. **Open a Pull Request** against the `main` branch.
6. Fill in the PR template — include the paper title, venue, year, and arXiv link.

### 4. PR Review Criteria / PR 审核标准

PRs will be reviewed for:
- ✅ Correct Markdown table formatting
- ✅ Valid arXiv / official paper links
- ✅ Appropriate topic tags
- ✅ Paper relevance to LLM agents / reasoning / alignment
- ✅ No duplicate entries

---

## Reporting Issues / 报告问题

If you find a broken link, incorrect information, or a missing important paper,  
please [open an issue](https://github.com/Brezzadimare/Awesome-LLM-Agent-Papers/issues).

---

Thank you for helping make this resource better! 🙏
