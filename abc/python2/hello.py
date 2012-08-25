import sys
argvs=sys.argv
#print(len(argvs))
base="Hello"
err='''用法:
hello
hello -p
hello -p $str
大小写无关'''
arg_len=len(argvs)
if arg_len==1 :
    print(base,'word!')
elif arg_len==2:
    if argvs[1].lower()=='-p':
        print(base,'word!')
    else:
        print(err);
elif arg_len==3:
    if argvs[1].lower()=='-p':
        print(base,argvs[2])
    else:
        print(err)
else:
    print(err)
