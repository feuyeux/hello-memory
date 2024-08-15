# Papers

[A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/pdf/2308.11432)

## 记忆的来源

- 内部任务信息（Inside-trial Information）对话的上下文信息
- 跨任务信息（ Cross-trial Information ）利用跨任务的信息来优化和改进当前任务的执行策略
- 外部知识（External Knowledge）

### ExpeL

- [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/pdf/2308.10144)
- <https://github.com/LeapLabTHU/ExpeL>

Experiential Learning (ExpeL) agent

`https://github.com/LeapLabTHU/ExpeL/blob/main/memory/episode.py`

**Memory Mechanisms** Agents with persistent long-term memory have demonstrated exciting results in multi-agent settings (Park et al. 2023; Maas et al. 2023; Qian et al. 2023). These works usually have multiple instantiations of generative agents that interact with each other and simulate human societies or fictional settings. In generative agents (Park et al. 2023), agents have a memory mechanism where they can retrieve information based on recency, relevance, and importance, much like how humans sometimes refer to and associate with different memories during their day. These lines of work usually are open-ended, while ExpeL agents are task-solving. Like generative agents, our work also uses memory: successful in-context examples and extracted insights as condensed memory which were both gathered from the agent’s own experience.

## 记忆的形式

记忆可以是**文本形式(Textual Form)**的。[MemGPT](https://memgpt.ai/)的短期记忆和召回记忆；至于完整的交互记忆，通常用于ReAct(reasoning and acting)，在Qwen-Agent中，通过chatml特有的多轮的格式<im_start> <im_end>进行分割历史的会话，最后一轮才加上ReAct的prompt。

[MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/pdf/2310.08560)

MemGPT: Unlimited Memory without Token Constraints for Generative AI Platforms, like GPT-4, LaMDA, PaLM, LLAMA, CLAUDE, and others <https://medium.com/@lawrenceteixeira/memgpt-unlimited-memory-without-token-constraints-for-generative-ai-platforms-like-gpt-4-lamda-0c755ece7d05>

记忆也可以是**参数形式(Parametric Form)**的，这种方式更高级一些。它不是直接存储文字，而是把记忆转换成模型参数，就像是把知识压缩成精华。这样做的好处是不会受到文本长度的限制，而且存储效率更高。但是，这种形式的记忆在写入时可能需要更多的计算，而且解释起来也不如文本形式直观。

参数形式的记忆则涉及到一些更复杂的技术，比如fine-tuning和editing。微调可以帮助模型快速学习特定领域的知识，而知识编辑则可以精确地更新或删除某些记忆，避免影响其他无关的知识。经典的**Character-LLM**: A Trainable Agent for Role-Playing，就是使用的微调的方式。

[Character-LLM: A Trainable Agent for Role-Playing](https://arxiv.org/pdf/2310.10158)

## 记忆的操作

记忆操作就像是LLM的大脑，它由三个部分组成：

- 记忆写入
- 记忆管理
- 记忆读取

### 记忆写入

这就像是LLM的短期记忆。当LLM接收到新的信息时，比如我们在聊天中提到的内容，它就会把这些信息存入它的“大脑”。这个过程就像是我们在记事本上写东西，但LLM用的是一种特殊的编码方式，比如转换成一系列的数字参数。这样，当信息需要被用到时，它们就能够更快速地被调取出来。

在MemGPT中，它的记忆写入完全是自我指导的。智能体可以根据上下文自己决定更新记忆，就像是我们根据当前的情况来决定记住什么一样。

MemoChat研究中，这个模型的智能体在聊天时会做总结，它会提取每个对话片段的主要讨论话题，然后像给书本加索引一样，把这些话题作为记忆片段的关键词存起来，这样以后查找记忆就方便多了。

[MemoChat: Tuning LLMs to Use Memos for Consistent Long-Range Open-Domain Conversation](https://arxiv.org/pdf/2308.08239)

### 记忆管理

这个环节就像是LLM的长期记忆。LLM会在这里处理和整理之前写入的信息，把它们变得更有用。比如，如果LLM接收到了很多信息，它可能会把这些信息进行分类，或者找出最重要的部分，然后把不那么重要的信息“忘掉”，以保持大脑的清晰和高效。

来看看几个具有代表性的研究，它们是咋让智能体搞记忆管理的。

- [MemoryBank](https://github.com/zhongwanjun/MemoryBank-SiliconFriend/blob/main/README_cn.md) 把对话内容提炼成每天的大事记，有点像我们人类回忆一天中的关键点一样。通过长期的互动，智能体还能不断地评估和提炼它们的知识，生成对个性特征的日常洞察。
- [Voyager](https://github.com/MineDojo/Voyager) 可以根据环境的反馈来优化它们的记忆。就像我们根据别人的反应来调整自己的记忆一样。
- Generative Agents就更高级了，智能体能进行反思，获取更高层次的信息。它们能从积累的事件中产生抽象的想法。当有足够的事件需要处理时，这个反思过程就会被激活。
- GITM，这个智能体为了建立各种情况下的共同参考计划，会进一步在记忆模块中总结多个计划中的关键行动。这就像是我们根据不同情境制定计划，并从中提取出最重要的行动步骤。见下图。

[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/pdf/2305.10250)

[VOYAGER: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/pdf/2305.16291)

[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/pdf/2304.03442)

GITM [Ghost in the Minecraft: Generally Capable Agents for Open-World Environments via Large Language Models with Text-based Knowledge and Memory](https://arxiv.org/pdf/2305.17144)

Voyager - An LLM-based curriculum generator, actor and critic, with skill reuse in Minecraft! <https://www.youtube.com/watch?v=Y-pgbjTlYgk>

### 记忆读取

这是LLM使用记忆中的信息来帮助解决问题的时刻。就像我们在准备考试时，会从笔记中找到重要的知识点一样。LLM会根据当前的情况，从记忆中找到最相关的信息，然后用这些信息来帮助我们做出决策或回答问题。

同样，咱们看看几个有代表性的研究。

- [ChatDB](https://www.chatdb.ai/)里，记忆阅读操作是通过SQL语句来执行的。这些SQL语句是智能体提前生成的，就像是提前准备好的一连串记忆链。这样，当需要记忆的时候，智能体就能快速找到需要的信息。
- MPC(Modular Prompted Chatbot)中，智能体能从记忆池里检索出相关的记忆。这个方法还提出了一种提供思维链示例的方式，帮助智能体忽略某些不重要的记忆。这样智能体就能集中注意力在那些对当前任务更有帮助的记忆上。
- ExpeL这个模型就更厉害了，它使用Faiss向量库作为记忆池，然后找出与当前任务相似度最高的前K个成功轨迹。这就像是智能体有一个超级记忆库，能快速匹配并找出最相似的成功经验来指导当前的任务。

MPC [Prompted LLMs as Chatbot Modules for Long Open-domain Conversation](https://arxiv.org/pdf/2305.04533)

## 记忆模块的评估

### 主观评估

主要有两个关键点：连贯性和合理性。这就像是在看一部电视剧，如果剧情突然跳到了完全不相关的地方，你可能会觉得很突兀，对吧？同样的道理，智能体的记忆也需要和当前的情境保持连贯。

- **连贯性**：这是指智能体回忆起的内容是否自然、是否适合当前的上下文。比如，如果智能体正在给小明做旅游计划，那么它的记忆就应该和小明对旅游的偏好有关，而不是工作相关的事情。以前的研究中，比如
  - RET-LLM（RET-LLM: Towards a General Read-Write Memory for Large Language Models）的工作中，就研究了记忆模块是否能在不断变化的知识中提供恰当的参考。
  - MemoryBank（MemoryBank: Enhancing Large Language Models with Long-Term Memory）中提到通过评分标签来评估那些结合了上下文和检索记忆的回应的连贯性。
  - MPC （Prompted LLMs as Chatbot Modules for Long Open-domain Conversatio）中提到了考虑回忆记忆和上下文之间的矛盾。
- **合理性**：这个方面的目标是评估智能体回忆的内容是否合理。比如，如果智能体被问到“颐和园在哪里”，它应该回答“颐和园在北京”，而不是“颐和园在月亮上”。在以前的研究中，上面MPC中提到过让众包直接对检索到的记忆的合理性进行评分。MemoryBank中提到了让人类评估者来检查记忆是否包含了对当前问题合理的答案。

### 客观评估

这种方式更加量化，我们用数字来说话。我们可以看看智能体是否能够准确地回答问题，或者它们是否能够找到正确的参考信息。这种方式的优点是它提供了一个清晰的标准，让我们可以比较不同的记忆模块。但问题是，它可能无法完全捕捉到记忆模块的所有细微差别。

- **结果正确性**，衡量智能体是否能够基于记忆模块成功回答预定义的问题。例如，如果用户询问是 “小明今天去了哪里？”，智能体需要从记忆中选择正确的答案，如 "A: 东湖" 或 "B: 西湖"，并与正确答案进行匹配比较。通过准确率就可以计算。
- **参考准确性**，与结果正确性不同，参考准确性更关注智能体在做出最终决定时所依赖的中间信息。将检索到的记忆与预先准备好的标准答案进行比较，通常使用F1分数来评估检索过程的准确性。
- **时间和硬件成本**，关注记忆模块操作的总时间成本，包括记忆管理和推理的时间。记忆管理指的是记忆写入和管理所需的时间，而推理时间则是记忆读取的时间延迟。并且，计算开销可以通过评估过程中使用的峰值GPU内存分配来衡量。

- <https://github.com/AIoT-MLSys-Lab/Efficient-LLMs-Survey>
