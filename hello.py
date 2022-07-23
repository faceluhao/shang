import os         #导入模块
path = r'C:\Users\luhao\Desktop\add2\motor' #设置创建后文件夹存放的位置，例如根目录\bike
for i in range(0,200): #这里创建10个文件夹
   # *定义一个变量判断文件是否存在,path指代路径,str(i)指代文件夹的名字*
    isExists = os.path.exists(os.path.join(path, str(i+1)))
    if not isExists:                  #判断如果文件不存在,则创建
    	#这里有五个视角，你需要匹配哪几个视角就使用哪两句，其余的注释掉
        os.makedirs(os.path.join(path, str(i+1), "front1"))
        os.makedirs(os.path.join(path, str(i+1), "back"))
        os.makedirs(os.path.join(path, str(i+1), "front2"))
       # os.makedirs(os.path.join(path, str(i+1), "fside"))
       # os.makedirs(os.path.join(path, str(i+1), "bside"))
        print("%s 目录创建成功"%i)
    else:
        print("%s 目录已经存在"%i)
        continue         #如果文件不存在,则继续上述操作,直到循环结束
