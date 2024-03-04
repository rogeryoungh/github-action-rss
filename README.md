# GitHub Action RSS

> 我对当前所有托管 RSS 服务的条数限制比较失望，且邮件通知都是付费功能，所以有了本项目。

本项目能够读取 OPML 格式的 RSS 订阅列表，按时间和目录进行排序，并实现邮件通知。

This project is able to read a list of RSS feeds in OPML format, sort them by time and tag, and email notifications.

## Usage | 用法

您需要准备好您的 RSS 订阅文件 `feed.opml`，以及 Workflow 文件 [send.yml](https://github.com/rogeryoungh/github-action-rss/blob/main/.github/workflows/send.yml)，仓库如下图组织。

Please prepared your RSS subjects file `feed.opml` and [send.yml](https://github.com/rogeryoungh/github-action-rss/blob/main/.github/workflows/send.yml), organized as below:

```text
.
├─ .github
│  └─ workflows
│     └─ send.yml
└─ feed.opml
```

接下来您需要根据您的需求修改 `send.yml`：

1. 首先请您更改 `send.yml` 中的地址 `https://rogeryoungh.github.io/github-action-rss/` 为您的 GitHub Pages 服务的地址。
2. 若您不需要邮件服务，删掉 Send mail 块即可。
3. 若您需要邮件服务，请备好支持 SMTP 发信的邮箱：
   - 请在该仓库的 Setting > Actions secrets and variables 中添加变量：`MAIL_HOST`、`MAIL_USER`、`MAIL_PASS`、`RECEIVERS`。
   - 如您在填写 secrets 时遇到困难，也可以硬编码到 `send.yml`，注意隐私安全。

Next, you need to modify `send.yml` to suit your needs:

1. First, change the address `https://rogeryoungh.github.io/github-action-rss/` in `send.yml` to the address of your GitHub Pages.
2. If you dont need email notifications, delete the "send mail" block.
3. If you need email notifications, have a mailbox that support SMTP
   - Add variables `MAIL_HOST`、`MAIL_USER`、`MAIL_PASS`、`RECEIVERS` in your repo setting `Setting > Actions secrets and variables`.
   - If you have trouble with filling, you can also hardcode your information in `send.yml`. Please take care of your privacy and security.

四个变量的含义如下，以 `user@example.com` 发送到 `Q@Q.com` 为例

- `MAIL_HOST`：邮件服务器 `example.com`
- `MAIL_USER`：用户名 `user`
- `MAIL_PASS`：密码 `******`
- `RECEIVERS`：接收邮箱 `Q@Q.com`
- 请参考 [dawidd6/action-send-mail](https://github.com/dawidd6/action-send-mail)

The meanings of the four variables are as follows, using `user@example.com` sent to `Q@Q.com` as an example

- `MAIL_HOST`: the mail server `example.com`.
- `MAIL_USER`: the user name `user`.
- `MAIL_PASS`: password `******`
- `RECEIVERS`: receiving mailbox `Q@Q.com`
- refer to [dawidd6/action-send-mail](https://github.com/dawidd6/action-send-mail)
