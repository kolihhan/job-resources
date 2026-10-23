# Next-chat execution prompt

Copy the block below into the next chat:

```text
继续执行并维护我的 job search repo `kolihhan/job-resources`。

先读取默认分支的 `README.md`、`PROFILE.md`、`RULES.md`、`DISCOVERY_STATE.md`，再读取当前需要处理的 Issues。以 repo 当前内容为唯一 operating contract；不要从旧 memory / 旧 prompt 重建 market scope、YOE、employment type、role direction、freshness、dedupe 或 source rotation。

按 `RULES.md` 实际执行当前应该做的 maintenance / discovery 工作；需要 Gmail 证据时检查两套 Gmail。只加载规则要求的 relevant Issue context，历史 WAIT / closed 记录按需查询，不要每轮全部重读。

如果某个 Issue 已经记录了我对 exact application/action 的明确授权，继续执行即可，不要重复问我一次 `go`。没有已记录授权的 employer-facing action 仍然必须先取得明确授权。

任何 GitHub/automation 写入都要读回验证。网站表单如果当前工具不能真正提交，就准确记录 blocker；没有 receipt / confirmation 时不要把它说成已申请，也不要移到 WAIT。

不要创建第二个 tracker/dashboard/framework。不要虚构 sponsor、薪资、WLB、application state 或岗位 liveness。
```
