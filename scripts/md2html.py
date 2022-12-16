# -*- coding: utf-8

import markdown
import os
import sys
import shutil
import requests

gh_rss = requests.get('https://lf3-cdn-tos.bytecdntp.com/cdn/expire-1-M/github-markdown-css/5.1.0/github-markdown.min.css')

html = '''
<html lang="zh-cn">
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
}

@media (max-width: 767px) {
    .markdown-body {
        padding: 15px;
    }
}
%s
</style>
</head>
<body>
<article class="markdown-body">
%s
</article>
</body>
</html>
'''


def md2html(name):
    content = ''
    with open(f'./test/{name}.md') as f:
        content = f.read()
    content = '# 这是您的今日资讯\n\n' + content
    ret = markdown.markdown(content)
    ret = html % (gh_rss.text, ret)
    with open(f'./build/{name}.html', 'w') as f:
        f.write(ret)


if __name__ == '__main__':
    if os.path.exists('./build'):
        shutil.rmtree('./build')
    os.mkdir('./build')

    md = markdown.Markdown()

    for dirpath, dirnames, filenames in os.walk('./test/'):
        for name in filenames:
            if name.endswith('.md'):
                md2html(name[:-3])
