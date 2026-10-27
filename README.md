# side-handoff

把侧聊反复打磨的理解交给主线程，让它知道**做什么、为什么、边界在哪里，以及下一步怎么做**。

**侧聊蒸馏 → 展示整包 → 你确认 → 交接确认版本 → 主线程说明理解与计划 → 继续原任务**

适用于代码、研究、写作、课程设计等任务。交接包由**行动摘要＋完整专题**组成；完整度以“能复现判断与执行”为标准，不按固定字数删减关键细节。

## 最短使用流程

### 1. 在侧聊准备审阅包

讨论完成后发送：

```text
$side-handoff Extract
把我们打磨的成果蒸馏成行动摘要＋完整专题包。
保留足以复现判断和执行的理由、边界、关键推导、反例、否决方案与具体行动。
先展示完整包让我确认，别只给摘要。
```

![侧聊整包审阅示例](docs/images/01-extract.png)

### 2. 在侧聊确认并取得交接指令

看过完整包后，例如回复：

```text
确认这份 course@v1 整包，明确标为待议的建议仍保持待议。
```

Skill 固定确认版本，准备一句交接指令：

- 可共享文件：用户指定目录优先，否则已确认项目根目录的 `docs/agent-handoffs/inbox/`；保存并回读后给真实路径。
- 无共享文件权限：给完整可复制确认包，你把指令和包正文一起带回主线程。
- 线程链接可附为追溯信息；不依赖跨线程工具一定能读到完整记录。

![确认版本与交接载体示例](docs/images/02-merge.png)

### 3. 主线程接收并继续

复制侧聊实际生成的指令，例如：

```text
$side-handoff Merge：接收并合并 course@v1；包文件：[替换为实际共享路径]。
说明理解、对主任务的影响和调整后的计划，然后在原任务授权内继续。
```

“接收并合并”同时授权保存相关交接文档，**不重复审批已确认且无冲突的包**。只说“看看、评估”或要求先展示候选时，仍是只读。

主线程核对相关专题与项目现状，保存完整经验及 INDEX，说明理解与计划后继续原任务。只在目标、硬约束或已确认决策矛盾时集中问你，只暂停受影响的工作。旧代码尚未实现方案，属于实现差距，不为此重审方案。

![主线程接收并推进示例](docs/images/03-confirm.png)

截图为合成教程页的真实浏览器截图，非 Codex 原生界面，不代表真实项目已执行。

## 让新聊天找回经验

首次使用时，Skill 可展示拟加入项目 AGENTS.md 的简短读取规则；你确认具体规则后才添加。后续聊天先查 INDEX，再按任务加载相关专题。尚未设置入口也不阻塞这次接收。

## 安装与升级

本机用户级位置为 `~/.codex/skills/side-handoff`。如果聊天已列出它，可直接使用。

其他机器可克隆后复制核心文件；下面命令遇到已有安装会停止：

```powershell
git clone https://github.com/tianxiangliu-ds/side-handoff.git
$target = Join-Path $HOME '.codex/skills/side-handoff'
if (Test-Path -LiteralPath $target) { throw '已有安装，请先比较并备份；停止覆盖。' }
New-Item -ItemType Directory -Path $target -ErrorAction Stop | Out-Null
Copy-Item -LiteralPath './side-handoff/SKILL.md' -Destination $target
Copy-Item -LiteralPath './side-handoff/references' -Destination $target -Recurse
```

升级先备份并比较本地修改，仅同步 SKILL.md 和 references；保留其他自定义文件。v0.2.0 调整了确认流程，旧包的兼容方式见教程。发现机制参见 [OpenAI 官方 Skills 文档](https://developers.openai.com/codex/skills/)；没有被发现时，可提供实际 SKILL.md 路径要求读取，不因此扩大权限。

## 深入使用

- [完整中文教程](docs/tutorial.zh-CN.md)：多侧聊、增量、冲突、无权限、新聊天。
- [包格式与侧聊确认](references/package.md)、[主线程接收流程](references/merge.md)。
- [可测试场景](references/examples.md)、[实际验证范围](docs/validation.md)。
- [维护说明](CONTRIBUTING.md)、[版本记录](CHANGELOG.md)。

当前版本 **v0.2.0**。CONFIRMED 表示接受方案，VERIFIED 表示限定范围的事实证据；二者相互独立。包确认也不把待议建议或假设变成已采纳、已验证结论。
