# LLM Efficiency Papers / 大语言模型效率论文

> Papers on efficient architectures, inference, compression, and distillation.  
> Back to [README](../README.md)

---

## 🏗️ Efficient Architectures

| Title | Authors | Venue | Tags | Paper | Code |
|-------|---------|-------|------|-------|------|
| [Transformers are SSMs: Mamba-2 via Structured State Space Duality](https://arxiv.org/abs/2405.21060) | Dao et al. | NeurIPS 2024 | `architecture` `efficiency` | [arXiv](https://arxiv.org/abs/2405.21060) | [GitHub](https://github.com/state-spaces/mamba) |
| [Mixture of Depths: Dynamically Allocating Compute in Transformers](https://arxiv.org/abs/2404.02258) | Raposo et al. | ICLR 2025 | `efficiency` `architecture` | [arXiv](https://arxiv.org/abs/2404.02258) | — |
| Mixtral of Experts | Jiang et al. | 2024 | `architecture` `efficiency` | [arXiv](https://arxiv.org/abs/2401.04088) | — |
| MegaByte: Predicting Million-byte Sequences with Multiscale Transformers | Yu et al. | NeurIPS 2023 | `architecture` `efficiency` | [arXiv](https://arxiv.org/abs/2305.07185) | — |

---

## 💡 Efficient Inference & KV Cache

| Title | Authors | Venue | Tags | Paper | Code |
|-------|---------|-------|------|-------|------|
| FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning | Dao | ICLR 2024 | `efficiency` `architecture` | [arXiv](https://arxiv.org/abs/2307.08691) | — |
| GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints | Ainslie et al. | EMNLP 2023 | `efficiency` | [arXiv](https://arxiv.org/abs/2305.13245) | — |
| SnapKV: LLM Knows What You Are Looking for Before Generation | Li et al. | NeurIPS 2024 | `efficiency` | [arXiv](https://arxiv.org/abs/2404.14469) | — |

---

## 🗜️ Quantization & Compression

| Title | Authors | Venue | Tags | Paper | Code |
|-------|---------|-------|------|-------|------|
| GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers | Frantar et al. | ICLR 2023 | `efficiency` | [arXiv](https://arxiv.org/abs/2210.17323) | — |
| AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration | Lin et al. | MLSys 2024 | `efficiency` | [arXiv](https://arxiv.org/abs/2306.00978) | — |
| LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale | Dettmers et al. | NeurIPS 2022 | `efficiency` | [arXiv](https://arxiv.org/abs/2208.07339) | — |

---

## 📚 Knowledge Distillation

| Title | Authors | Venue | Tags | Paper | Code |
|-------|---------|-------|------|-------|------|
| [Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone](https://arxiv.org/abs/2404.14219) | Abdin et al. | NeurIPS 2024 | `foundation-model` `efficiency` | [arXiv](https://arxiv.org/abs/2404.14219) | — |
| [Gemma 2: Improving Open Language Models at a Practical Size](https://arxiv.org/abs/2408.00118) | Google DeepMind | NeurIPS 2024 | `foundation-model` `efficiency` | [arXiv](https://arxiv.org/abs/2408.00118) | — |
| Distillspec: Improving Speculative Decoding via Knowledge Distillation | Zhou et al. | ICLR 2024 | `efficiency` | [arXiv](https://arxiv.org/abs/2310.08461) | — |

---

## ⚡ Parameter-Efficient Fine-Tuning (PEFT)

| Title | Authors | Venue | Tags | Paper | Code |
|-------|---------|-------|------|-------|------|
| LoRA: Low-Rank Adaptation of Large Language Models | Hu et al. | ICLR 2022 | `efficiency` `fine-tuning` | [arXiv](https://arxiv.org/abs/2106.09685) | — |
| QLoRA: Efficient Finetuning of Quantized LLMs | Dettmers et al. | NeurIPS 2023 | `efficiency` `fine-tuning` | [arXiv](https://arxiv.org/abs/2305.14314) | — |

---

*See venue files: [ICLR 2025](../papers/ICLR/2025.md) · [NeurIPS 2024](../papers/NeurIPS/2024.md)*
