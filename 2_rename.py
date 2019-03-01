'''
对某一文件夹下的所有文件实现批量重命名
    此程序功能为同一修改后缀
'''

import os


def rename():
    i = 0
    path = "D:\\test"
    filelist = os.listdir(path)                       #该文件夹下所有的文件（包括文件夹）
    for files in filelist:                            #遍历所有文件
        i = i + 1
        old_dir = os.path.join(path, files)            #原来的文件路径
        # print(Olddir)
        if os.path.isdir(old_dir):                     #如果是文件夹则跳过
            continue
        filename = os.path.splitext(files)[0]         #文件名
        filetype = os.path.splitext(files)[1]         #文件扩展名

        new_dir = os.path.join(path, filename + '.sql')  #新的文件路径
        os.rename(old_dir, new_dir)                     #重命名


rename()
