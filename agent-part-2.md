# The AI Engineering Skills Map — Part 2: AI Applications

**Source:** Andrew Ng and DeepLearning.AI, “The AI Engineering Skills Map Part 2 — AI Applications”

## Purpose

This part expands the first skill area from Part 1: building and deploying AI applications. Because AI systems produce uncertain outputs, their development is iterative. Skilled engineers examine intermediate results and use them to decide what to improve next, making unreliable AI components into more reliable software systems.

## Six skill areas for AI applications

1. **LLM foundations.** Understand tokenization and generation, model capabilities and failure modes, multimodal models, context-window tradeoffs, caching, knowledge cutoffs, reasoning effort, sampling settings, and tool calling. Use this knowledge to select models and decide when specialized approaches such as fine-tuning or self-hosting are appropriate.

2. **Ground models with data.** Supply useful, relevant context through suitable methods: prompt content, retrieval through tools, vector search, knowledge graphs, or semantic layers over structured data. Convert sources such as documents, PDFs, HTML, and images into model-ready inputs, and keep data pipelines clean and current.

3. **Build agentic systems.** Choose between fixed workflows and agent loops, and design the steps, parallel work, code/LLM split, and fallbacks. Select tools, memory, context-management approaches, and single- or multi-agent architectures. For production, address safety, security, guardrails, adversarial inputs, data-exfiltration risks, and governance. Stay aware of specialized approaches such as voice, computer-use, and generative-UI agents when relevant.

4. **Use evaluation-driven development.** Make evaluation and error analysis the feedback loop for development. Inspect traces and outputs, use exploratory data analysis and product or business insight to choose what to measure, and select among code-based checks, LLM-as-judge, and human review. Evaluate and refine the evaluations themselves so system improvements are guided by evidence rather than guesswork.

5. **Operate in production.** Account for AI-specific uncertainty, cost, and latency. Build observability for real-world performance, detect drift, and respond to model failures and security incidents such as prompt injection. Use regression testing and CI/CD with statistical evaluations calibrated to the risk of errors. Control cost and latency through model selection, distillation, fine-tuning, or simpler workflows as appropriate.

6. **Learn machine learning foundations.** Understand supervised learning, reinforcement learning, and deep learning, which underpin modern LLMs and many other applications. Know common model choices and tradeoffs in accuracy, training speed, and inference speed. Engineer data for training and evaluation, and use concepts such as bias/variance and error analysis to reason about uncertain systems.

## Main takeaway

Building useful AI applications takes technical depth and repeated, evidence-based iteration. The central practice is to measure system behavior, analyze errors, and use what you learn to choose the next development step. Software engineering fundamentals complement these application skills and are the subject of the next part.

## Scope note

This file summarizes **Part 2 only**, focused on building and deploying AI applications.
