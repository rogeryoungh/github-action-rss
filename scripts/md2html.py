# -*- coding: utf-8

import markdown
import os
import sys
import shutil

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
</style>
<link href="https://lf3-cdn-tos.bytecdntp.com/cdn/expire-1-M/github-markdown-css/5.1.0/github-markdown.min.css" rel="stylesheet">
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
    ret = markdown.markdown(content)
    ret = html % ret
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
