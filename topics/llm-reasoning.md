# LLM Reasoning Papers / 大语言模型推理论文

> Cross-venue compilation of key papers on LLM reasoning.  
> Back to [README](../README.md)

---

## 📖 Chain-of-Thought Prompting

Foundational works on prompting LLMs to reason step-by-step.

| Title | Authors | Venue | Tags | Paper |
|-------|---------|-------|------|-------|
| Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | Wei et al. | NeurIPS 2022 | `reasoning` | [arXiv](https://arxiv.org/abs/2201.11903) |
| Self-Consistency Improves Chain of Thought Reasoning in Language Models | Wang et al. | ICLR 2023 | `reasoning` | [arXiv](https://arxiv.org/abs/2203.11171) |
| Tree of Thoughts: Deliberate Problem Solving with Large Language Models | Yao et al. | NeurIPS 2023 | `reasoning` `planning` | [arXiv](https://arxiv.org/abs/2305.10601) |
| Graph of Thoughts: Solving Elaborate Problems with Large Language Models | Besta et al. | AAAI 2024 | `reasoning` | [arXiv](https://arxiv.org/abs/2308.09687) |

---

## 🔢 Mathematical Reasoning

See also: [ICLR 2024](../papers/ICLR/2024.md#-reasoning)

| Title | Authors | Venue | Tags | Paper | Code |
|-------|---------|-------|------|-------|------|
| [MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models](https://arxiv.org/abs/2309.12284) | Yu et al. | ICLR 2024 | `reasoning` `math` | [arXiv](https://arxiv.org/abs/2309.12284) | [GitHub](https://github.com/meta-math/MetaMath) |
| [WizardMath: Empowering Mathematical Reasoning via Reinforced Evol-Instruct](https://arxiv.org/abs/2308.09583) | Luo et al. | ICLR 2024 | `reasoning` `math` | [arXiv](https://arxiv.org/abs/2308.09583) | [GitHub](https://github.com/nlpxucan/WizardLM) |
| [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://arxiv.org/abs/2309.17452) | Gou et al. | ICLR 2024 | `reasoning` `tool-use` | [arXiv](https://arxiv.org/abs/2309.17452) | [GitHub](https://github.com/microsoft/ToRA) |
| [Scaling Relationship on Learning Mathematical Reasoning with LLMs](https://arxiv.org/abs/2308.01825) | Yuan et al. | ICLR 2024 | `reasoning` `scaling` | [arXiv](https://arxiv.org/abs/2308.01825) | — |

---

## 🔧 Tool-Augmented Reasoning

| Title | Authors | Venue | Tags | Paper | Code |
|-------|---------|-------|------|-------|------|
| [ToolLLM: Facilitating LLMs to Master 16000+ Real-world APIs](https://arxiv.org/abs/2307.16789) | Qin et al. | ICLR 2024 | `tool-use` `reasoning` | [arXiv](https://arxiv.org/abs/2307.16789) | [GitHub](https://github.com/OpenBMB/ToolBench) |
| [ToRA: A Tool-Integrated Reasoning Agent](https://arxiv.org/abs/2309.17452) | Gou et al. | ICLR 2024 | `reasoning` `tool-use` | [arXiv](https://arxiv.org/abs/2309.17452) | [GitHub](https://github.com/microsoft/ToRA) |
| [SELF-RAG: Learning to Retrieve, Generate, and Critique](https://arxiv.org/abs/2310.11511) | Asai et al. | ICLR 2024 / NeurIPS 2024 | `RAG` `reasoning` | [arXiv](https://arxiv.org/abs/2310.11511) | [GitHub](https://github.com/AkariAsai/self-rag) |

---

## 🌲 Tree & Graph Search for Reasoning

| Title | Authors | Venue | Tags | Paper | Code |
|-------|---------|-------|------|-------|------|
| [Language Agent Tree Search (LATS)](https://arxiv.org/abs/2310.04406) | Zhou et al. | ICLR 2024 | `reasoning` `planning` | [arXiv](https://arxiv.org/abs/2310.04406) | [GitHub](https://github.com/lapisrocks/LanguageAgentTreeSearch) |
| [Toward Self-Improvement of LLMs via Imagination, Searching, and Criticizing](https://arxiv.org/abs/2404.12253) | — | ICLR 2025 | `reasoning` `self-improvement` | [arXiv](https://arxiv.org/abs/2404.12253) | — |
| [ReasonFlux: Hierarchical LLM Reasoning via Scaling Thought Templates](https://arxiv.org/abs/2502.06772) | Yang et al. | ICLR 2025 | `reasoning` `planning` | [arXiv](https://arxiv.org/abs/2502.06772) | [GitHub](https://github.com/Gen-Verse/ReasonFlux) |

---

## ⏱️ Test-Time Scaling

| Title | Authors | Venue | Tags | Paper | Code |
|-------|---------|-------|------|-------|------|
| [Scaling LLM Test-Time Compute Optimally Improves Reasoning](https://arxiv.org/abs/2408.03314) | Snell et al. | ICLR 2025 | `reasoning` `scaling` | [arXiv](https://arxiv.org/abs/2408.03314) | — |
| [s1: Simple Test-Time Scaling](https://arxiv.org/abs/2501.19393) | Muennighoff et al. | ICLR 2025 | `reasoning` `scaling` | [arXiv](https://arxiv.org/abs/2501.19393) | [GitHub](https://github.com/simplescaling/s1) |
| [STILL-2: Enhancing Long Thought Reasoning in LLMs](https://arxiv.org/abs/2412.09413) | He et al. | ICLR 2025 | `reasoning` `long-CoT` | [arXiv](https://arxiv.org/abs/2412.09413) | — |
| [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | DeepSeek-AI | NeurIPS 2025 | `reasoning` `reinforcement-learning` | [arXiv](https://arxiv.org/abs/2501.12948) | [GitHub](https://github.com/deepseek-ai/DeepSeek-R1) |
| [OpenAI o1 System Card](https://arxiv.org/abs/2412.16720) | OpenAI | NeurIPS 2025 | `reasoning` | [arXiv](https://arxiv.org/abs/2412.16720) | — |

---

## 🏆 Process Reward Models

| Title | Authors | Venue | Tags | Paper |
|-------|---------|-------|------|-------|
| Let's Verify Step by Step | Lightman et al. | ICLR 2024 | `reasoning` `RLHF` | [arXiv](https://arxiv.org/abs/2305.20050) |
| Math-Shepherd: Verify and Reinforce LLMs Step-by-step | Wang et al. | ACL 2024 | `reasoning` `math` | [arXiv](https://arxiv.org/abs/2312.08935) |

---

*See venue files for full paper details: [ICLR 2024](../papers/ICLR/2024.md) · [ICLR 2025](../papers/ICLR/2025.md) · [NeurIPS 2024](../papers/NeurIPS/2024.md)*
