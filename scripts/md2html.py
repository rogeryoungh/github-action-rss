# -*- coding: utf-8

import markdown
import os
import sys
import shutil
import requests

base_url = "https://rogeryoungh.github.io/github-action-rss"

gh_rss = requests.get("https://unpkg.com/heti/umd/heti.min.css")

htmls = [
    """
<html lang="zh-cn">
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.container {
    box-sizing: border-box;
    padding-block-start: 12px;
    padding-block-end: 72px;
    padding-inline-start: 12px;
    padding-inline-end: 12px;
  }
  @media screen and (min-width: 640px) {
  body {
    min-width: 640px;
    background-color: hsl(0deg, 0%, 93%);
  }
  .container {
    box-sizing: border-box;
    width: 80%;
    min-width: 640px;
    max-width: 768px;
    margin-block-start: 48px;
    margin-block-end: 72px;
    margin-inline-start: auto;
    margin-inline-end: auto;
    padding-block-start: 48px;
    padding-block-end: 48px;
    padding-inline-start: 48px;
    padding-inline-end: 48px;
    border-radius: 2px;
    box-shadow: 0 8px 32px hsla(0deg, 0%, 0%, 0.32);
    background-color: hsl(0deg, 0%, 100%);
  }
  .section {
    max-height: none;
    overflow: visible;
  }
}""",
    """
</style>
</head>
<body>
<main class="container">
<article class="article heti heti--classic">
""",
    """
</article>
</main>
</body>
</html>
""",
]


def md2html(content):
    ret = markdown.markdown(content)
    ret = htmls[0] + gh_rss.text + htmls[1] + ret + htmls[2]
    return ret


if __name__ == "__main__":
    if os.path.exists("./build"):
        shutil.rmtree("./build")
    os.mkdir("./build")

    md = markdown.Markdown()

    index = ["# 您的今日资讯", f"- [年度汇总]({base_url}/this-year.html)"]
    this_year = ""
    for dirpath, dirnames, filenames in os.walk("./test/"):
        for name in filenames:
            if name.endswith(".md"):
                tname = name[:-3]
                content = ""
                with open(f"./test/{tname}.md") as f:
                    content = f.read()
                if tname == "this-year":
                    this_year = content
                with open(f"./build/{tname}.html", "w") as f:
                    f.write(md2html(content))
                index.append(f"- [{tname}]({base_url}/{tname})")

    index.append(
        "- [github-action-rss](https://github.com/rogeryoungh/github-action-rss)"
    )

    index.append(this_year)

    with open("./build/index.html", "w") as f:
        f.write(md2html("\n\n".join(index)))
