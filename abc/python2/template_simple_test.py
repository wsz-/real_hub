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
data ={'title':'���Ա���',
       'text':'��������'}
print template % data
