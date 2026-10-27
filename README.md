# side-handoff

**在侧聊调用一次，得到一段可复制上下文，贴给主对话就能继续。**

不需要审阅确认，不需要主对话调用 Merge，不要求文件权限。

## 怎么用

侧聊讨论告一段落后，发送：

```text
$side-handoff
蒸馏当前侧聊，给我可直接贴到主对话的接续上下文。
```

它只输出一个可复制文本块。复制**块内全文**到主对话，作为补充上下文继续原任务；主对话不用调用 Skill。

![在侧聊调用一次](docs/images/01-extract.png)

输出覆盖会影响继续工作的目标、当前方案、关键理由、硬约束、重要细节、进度/未验证项和下一步；只在相关时出现，不填冗长模板。

![一次输出可复制上下文](docs/images/02-merge.png)

![贴给主对话继续](docs/images/03-confirm.png)

演示图是合成示例页的浏览器截图，非 Codex 原生界面，不证明真实任务已完成。

## 为什么比“总结一下”更具体

- **以接续为目标**：保留会改变主线程判断或行动的信息，而非按聊天时间线复述。
- **压缩时保住条件**：数值、单位、范围、兼容性和关键反例不被泛化成“注意边界”。
- **避免重复踩坑**：保留关键理由及容易重新提出的否决方案，但不逐条复述所有试探。
- **事实不升格**：模型建议不写成用户决定；未执行不写已完成；声称通过不写实际验证。
- **一次出成品**：内部检查遗漏和冗余后，只输出最终文本，不展示草稿或要求确认。

默认目标约 **400–800 个中文字符**，简单则更短；这不是 token 数，也不是保证。复杂话题优先保关键约束，用户可指定预算：

```text
$side-handoff 约300字，重点保留最终方案、兼容约束和下一步。
```

压缩有损，验收看关键条件是否保留、主线程能否继续，不声称无损或保证“保住绝大部分聊天”。

## 安装

本机用户级位置：`~/.codex/skills/side-handoff`。

其他机器：克隆本仓库后，复制核心 Skill。PowerShell 示例遇到已有安装会停止：

```powershell
git clone https://github.com/tianxiangliu-ds/side-handoff.git
$target = Join-Path $HOME '.codex/skills/side-handoff'
if (Test-Path -LiteralPath $target) { throw '已有安装，请先比较与备份，停止覆盖。' }
New-Item -ItemType Directory -Path $target -ErrorAction Stop | Out-Null
Copy-Item -LiteralPath './side-handoff/SKILL.md' -Destination $target
Copy-Item -LiteralPath './side-handoff/references' -Destination $target -Recurse
```

核心流程自包含于 SKILL.md；正常提炼无需读取示例文件，不调用外部工具。

## v0.3.0 的变化

旧版把交接做成了确认、包文件和合并归档流程。实际使用反馈表明操作过重。新版仅负责侧聊蒸馏，移除默认确认、Merge、版本回执、文件保存、INDEX 和 AGENTS.md 管理。旧 `Extract` 仍是提炼别名，旧主线程归档流程不再执行。

升级前备份本地修改，替换 SKILL.md 与本版本 references；过时 package.md / merge.md 不再是新版入口。仓库历史与旧 Release 保留原流程文档，已有项目交接文件不会被删除或迁移。

- [中文教程与输出示例](docs/tutorial.zh-CN.md)
- [开源策略调研及取舍](docs/research.md)
- [测试场景](references/examples.md) / [验证范围](docs/validation.md)
- [维护说明](CONTRIBUTING.md) / [版本记录](CHANGELOG.md)
