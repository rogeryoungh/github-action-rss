# GitHub Action RSS

> 我对当前所有托管 RSS 服务的条数限制比较失望，并且邮件通知都需要付费功能，所以有了本项目。

本项目能够读取 OPML 格式的 RSS 订阅列表，按时间和目录进行排序，并实现邮件通知。

## 用法

使用本项目需要一定的脚本语言基础。

先 fork 本项目，opml 文件位于 `test/feed.opml`，并更新 `scripts/md2html.py` 中的 `base_url` 为你的地址，推送即可获得网页版。

如需获得邮件，请在项目设置中添加 Secrets: `MAIL_HOST`、`MAIL_USER`、`MAIL_PASS`、`RECEIVERS`。
