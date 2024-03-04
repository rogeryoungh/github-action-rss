# -*- coding: utf-8

import markdown
import os
import sys
import shutil
import requests

base_url = sys.argv[1]


def read_file(file_name: str) -> str:
    with open(file_name, encoding="UTF-8") as f:
        return f.read()


def md2html(content):
    ret = markdown.markdown(content)
    template = read_file("./scripts/template.html")
    return template.replace("<!--  CONTENT -->", ret)


if __name__ == "__main__":
    md = markdown.Markdown()

    index = ["# 您的今日资讯", f"- [年度汇总]({base_url}/this-year.html)"]
    this_year = ""
    for dirpath, dirnames, filenames in os.walk("./build/"):
        for name in filenames:
            if name.endswith(".md"):
                tname = name[:-3]
                content = ""
                with open(f"./build/{tname}.md") as f:
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
