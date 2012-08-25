# -*- coding: cp936 -*-
template='''
<html>
    <head>
        <title>%(title)s</title>
    </head>
    <body>
        <h1>%(title)s</h1>
        <p>%(text)s</p>
    </body>
</html>'''
data ={'title':'测试标题',
       'text':'测试内容'}
print template % data
