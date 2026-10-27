# 经验包格式

下面是输出契约；按实际数据填充，模板符号不代表真实证据。每个决策用独立小节，避免把不同接受程度的结论合成一条。

```markdown
# Handoff: {主题}
- package_id: {稳定 ID}
- version: {整数，首次为 1}
- previous_version: {版本或无；未知则写原因}
- scope: {主任务、模块、适用条件}
- sources: {当前可见对话 / 粘贴记录的局部编号 / 用户提供的可访问文件}
- source_coverage: {可见范围与缺失部分}
- created_at: {实际可知时间，或未知}

## 最终决策
### {稳定决策 ID}: {决策}
- acceptance: CONFIRMED | PROPOSED
- evidence: VERIFIED | UNVERIFIED
- lifecycle: active | SUPERSEDED
- source: {出处及简短引文，标明用户或模型}
- acceptance_basis: {用户明确接受的依据；无则未知}
- rationale: {设计理由及出处}
- constraints: {明确约束及出处}
- code_locations: {路径、符号、版本及存在性核对情况；否则未知}
- verification: {实际检查、结果、范围、版本、证据出处；否则未知}
- acceptance_criteria: {可观察、可执行的验收条件；建议项标 PROPOSED}
- supersedes / superseded_by: {决策 ID 或无}
- replacement_reason: {替代原因及确认依据，或不适用}

## 否决方案
- {方案、否决者、理由、出处；未被用户否决的模型取舍标为模型建议}

## 待验证假设与开放问题
- {假设、验证方法、责任人如已知；未知项说明原因}

## 版本记录
- v{版本}: {新增/变更/替代的 ID、原因、来源；首次提炼也记录}
```

对同一决策的证据补充沿用 ID。决策语义发生改变时创建新 ID，旧项在明确替代后标 SUPERSEDED；不覆盖历史理由。包版本和 Skill 文件版本无关。
