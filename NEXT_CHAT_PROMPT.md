# Next-chat execution prompt

Copy the block below into the next chat:

```text
继续执行并维护我的 job search repo `kolihhan/job-resources`。

先读取默认分支的 `README.md`、`PROFILE.md`、`RULES.md`、`DISCOVERY_STATE.md`，再读取当前需要处理的 Issues。以 repo 当前内容为唯一 operating contract；不要从这段 prompt 重建 freshness、dedupe、source rotation、Web3 或状态规则。

按 `RULES.md` 实际执行一次当前应该做的 maintenance / discovery 工作；需要 Gmail 证据时检查两套 Gmail。只加载规则要求的 relevant Issue context，历史 WAIT / closed 记录按需查询，不要每轮全部重读。

任何 GitHub/automation 写入都要读回验证。访问或验证失败时报告具体未完成步骤，不要猜。

不要创建第二个 tracker/dashboard/framework。不要虚构 sponsor、薪资、WLB、application state 或岗位 liveness。

提交申请或联系任何人之前，仍必须得到我对那个 exact action 的明确授权。
```
