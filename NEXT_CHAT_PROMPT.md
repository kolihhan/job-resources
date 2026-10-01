# Next-chat execution prompt

Copy the block below into the next chat:

```text
继续执行我的 job search，并维护 GitHub 私有 repo `kolihhan/job-resources`。

先读取默认分支 `README.md`、`PROFILE.md`、`RULES.md`、当前 Issues 和相关新评论；以这些为准。`docs/market-facts-2026-10-01.md` 是背景证据，不要每轮重做市场报告。

目标：拿到适合我的 full-time onsite/hybrid 工程岗位面试和 offer。

**重点是 Singapore + Mainland China。Malaysia 只是 backup，不要变成第三条同等主线。**

先处理已有机会：
- 查两套 Gmail 的最近 recruiter / OA / interview / rejection / deadline；
- 按时间顺序更新现有 Issues；
- 尊重 `applied` / `skip`；
- 不要 broad-audit 整个邮箱，dedupe 只对 exact company/role/req 做 targeted search。

然后实际做一轮 SG + CN discovery。

使用两阶段方法：

1. **Broad discovery first**
   - 扩大新公司覆盖；
   - SWE / backend / full-stack / platform / ML systems / Applied AI 都找；
   - 先 cheap-screen 明显 senior、硬 5+ YOE、明显届别不符、硬 stack/domain mismatch、明确 no-sponsorship / citizenship blocker、明显 stale；
   - 不要为了每个 raw candidate 先查 salary/WLB、未知 sponsor、exact ATS、两套 Gmail；
   - 不要找到两三条就停。输出稀少就换公司、关键词或 source 继续找。

2. **Verify serious survivors**
   - 对真正值得考虑的 survivor 才核实 exact/full JD、毕业窗口、seniority、GitHub + targeted Gmail dedupe、实际 Apply 入口和 materially relevant blocker；
   - exact route 未验证只能 CHECK；MCF-only SG role blocked；
   - 只有 serious survivor 才写 GitHub Issue。

Malaysia：只有 SG/CN 本轮合理 broadening 后仍明显 sparse，或自然发现特别强的 MY role 时才补搜。MY 更偏 AI Engineer / Applied AI / AI SWE / LLM-RAG-Agent / AI backend-platform，但不要因为 AI title 放弃更好的正常 SWE/backend engineering role。

特别强的 verified role 可以找一个 relevant recruiter / alumnus / team contact，但不要每个岗位都做 networking。联系任何人或提交 application 前仍必须得到我对 exact action 的明确 `go`。

不要使用旧的 `clean cohort` / `main sample` / application experiment 概念。GitHub 只维护 ACTION / APPLY / CHECK / WAIT 和真实下一步。

写入 GitHub 后读回验证。最后只汇报：
- 本轮 SG/CN broad candidates 大概覆盖了什么；
- 真正新增的 APPLY / CHECK；
- 已推进的 ACTION / WAIT；
- duplicates / stale / hard mismatches 的主要原因；
- 最值得我看或给 `go` 的机会。

不要另建 tracker、dashboard、framework 或投递 quota。不要虚构 sponsor、薪资、WLB、可投数量或成功率。
```
