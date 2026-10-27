# 验证范围

## v0.1.0

- 官方 quick_validate.py 曾对安装版与原始发布核心文件通过。
- 独立只读演练：Extract 合成对话、Merge 无文件权限候选、显式调用与新闻总结的路由判断。
- 本仓库 scripts/validate_repo.py 检查元数据、相对链接、PNG 资源及 HTML 演示页，CI 在 push/PR 时重复执行。
- 浏览器截图来自合成 HTML 示例页；截图仅验证教程呈现。

尚未实测：客户端自动选择、真实无写权限错误、并发修改、多文件部分失败、实际 Merge 落盘及幂等更新。references/examples.md 提供这些场景的测试方法，不能把预期结果当成已通过。
