# -*- coding: utf-8

import markdown
import os
import sys
import shutil
import requests

base_url = 'https://rogeryoungh.github.io/github-action-rss'

gh_rss = requests.get(
    'https://lf3-cdn-tos.bytecdntp.com/cdn/expire-1-M/github-markdown-css/5.1.0/github-markdown.min.css')

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

def md2html(content):
    ret = markdown.markdown(content)
    ret = html % (gh_rss.text, ret)
    return ret


if __name__ == '__main__':
    if os.path.exists('./build'):
        shutil.rmtree('./build')
    os.mkdir('./build')

    md = markdown.Markdown()

    index = ['# 您的今日资讯', f'- [年度汇总]({base_url}/this-year.html)']
    this_year = ''
    for dirpath, dirnames, filenames in os.walk('./test/'):
        for name in filenames:
            if name.endswith('.md'):
                tname = name[:-3]
                content = ''
                with open(f'./test/{tname}.md') as f:
                    content = f.read()
                if tname == 'this-year':
                    this_year = content
                with open(f'./build/{tname}.html', 'w') as f:
                    f.write(md2html(content))
                index.append(f'- [{tname}]({base_url}/{tname})')
    
    index.append('- [github-action-rss](https://github.com/rogeryoungh/github-action-rss)')

    index.append(this_year)

    with open('./build/index.html', 'w') as f:
        f.write(md2html('\n\n'.join(index)))
