# 上下文蒸馏：参考策略与取舍

查阅日期：2026-10-27。以下链接是会变动的上游 main/网页，记录的是本次查阅时观察，不代表永久规范。这里只概述思路，未复制第三方提示词正文。

## 直接参考的实现

### OpenAI Codex 的 compact prompt

[源码](https://github.com/openai/codex/blob/main/codex-rs/prompts/templates/compact/prompt.md)

它面向接续任务，要求压缩当前进度、关键决定、约束、剩余动作及关键数据/示例/引用。我们采用这种“恢复工作所需最小状态”的取向，不把交接变成档案。

### forest/agent-skills 的 session-handoff

[源码](https://github.com/forest/agent-skills/blob/main/plugins/session-handoff/skills/session-handoff/SKILL.md)

观察到它强调决定的理由、约束、否决项、当前状态和未决问题，要求省略空项及套话。我们采用这些选择标准，不采用其 AWS 专用字段、上下文百分比阈值、固定七节和文档管理流程。其“确定性”措辞不是本项目的质量保证。

### u-ichi/compact-plus 的 state-summary

[源码](https://github.com/u-ichi/compact-plus/blob/main/prompts/state-summary.md)

它将草拟、检查遗漏、修订放在内部，只输出最终状态，并保留准确标识和失败原因。我们借鉴内部自检和最终输出约束；不采用完整状态文件、工作者拓扑、强制空节及多份结构元数据，以降低贴回主对话的成本。

## 工程依据

[Anthropic 的 context engineering 文章](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) 指出应筛选高信号上下文，压缩时保留关键决策、未解决问题及必要实现细节，清除冗余输出；并提醒过度压缩可能丢失关键细节。我们据此把“短”与“能继续工作”同时作为验收目标，不追求固定压缩率。

## 本项目自己的设计选择

以下是根据用户实测反馈做出的取舍，不是上游公认标准：

- 只在侧聊调用，一次输出一个可复制文本块；主线程无 Merge 阶段。
- 默认约400–800个中文字符作为可调目标，简单更短，复杂必要时超出；不声称是精确 token 限制。
- 用“删除这条会不会改变下一步行动/判断”筛选信息；保留条件、理由和反例，而非逐轮讨论。
- 自然语言区分已定/建议、已做/待做、已验证/未经核实，不输出重复状态表。
- 不要求确认、不默认写文件、不管理项目长期记忆。

## 怎样验证而不是凭感觉

先检查重要信息召回：方案、限制、精确细节、理由、否决路径、实际进度；再删冗余。让只收到蒸馏结果的接收方给出下一步与边界，对照原记录看是否走样；同时记录长度和操作次数。少字数不等于高质量，更不能从一次合成测试推断所有真实任务都可靠。
