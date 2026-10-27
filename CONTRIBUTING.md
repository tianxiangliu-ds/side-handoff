# 维护与贡献

请用 Issue 描述问题，并附最小、脱敏的输入、预期行为与实际行为。不要提交私人聊天、密钥或未经授权的项目内容。

修改 Skill 时同步相关 references 与教程，运行 `python scripts/validate_repo.py`，并演练 references/examples.md 中受影响的用例。自动检查不替代模型行为验证。

通过 Pull Request 提交变更。影响来源追踪、侧聊整包确认、主线程授权或状态含义的修改，应附实际演练记录。截图有变化时更新 HTML 演示页并重新截取，不使用图片伪装测试通过。

当前处于 0.x 迭代期，工作流不兼容变化在 minor 发布中说明迁移方式；达到 1.0 后采用语义版本：修正文案为 patch，兼容能力为 minor，不兼容经验包格式或确认流程为 major。发布前更新 CHANGELOG.md、核对文档链接、生成版本标签和 Release。

仓库内文件是发布源；本机用户级安装是副本。升级前比较并备份已有 Skill，不直接覆盖用户修改。此仓库没有后台自动维护服务；后续维护通过 Issue、PR 和明确的后续任务进行。

重新截图：打开 docs/demos/ 下三张 HTML 页面，在 Chromium/Edge 中以 1280×940 视口截取整页，分别替换 docs/images/ 下同名 PNG。可使用 Playwright CLI 的 screenshot --channel msedge --viewport-size "1280,940" --full-page 命令；浏览器与 Playwright 需自行准备，不是 Skill 运行依赖。
