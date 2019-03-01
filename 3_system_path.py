'''
利用 sys 模块 和 os 模块 获取系统路径
'''


def sys_path():
    import sys
    print(sys.argv)
    print(sys.argv[0])          # 获取本程序路径
    print(sys.path)
    print(sys.path[0])          # 当前文件路径

def os_path():
    import os
    # 11，13，16 的结果相同，结果均为当前路径
    # 14 是在当前路径后追加文件（非本程序名）
    print(11, os.getcwd())                      #获取当前工作目录路径
    print(12, os.path)
    print(13, os.path.abspath('.'))             #获取当前工作目录路径
    print(14, os.path.abspath('test.txt'))      #获取当前目录文件下的工作目录路径
    print(15, os.path.abspath('..'))            #获取当前工作的父目录 ！注意是父目录路径
    print(16, os.path.abspath(os.curdir))       #获取当前工作目录路径

sys_path()
os_path()