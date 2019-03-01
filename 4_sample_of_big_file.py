import os
import csv
import gzip
import zipfile


def write_csv(filename, data):
    f = open(filename, 'a', newline='', encoding='utf-8')
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()
    return


def sample_big_csv(srcfile, dirfile):
    if os.path.exists(srcfile):
        with open(srcfile, 'r') as file:
            i = 0
            for row in file:
                if i == 0:
                    i = i + 1
                    continue
                print(row)
                print(type(row))
                if i <= 300000:
                    i = i + 1
                    write_csv(dirfile, row)
                else:
                    break
    else:
        print('the path [{}] is not exist!'.format(srcfile))


def sample_big_tar_gz(srcfile, dirfile):
    if os.path.exists(srcfile):
        gz = gzip.GzipFile(srcfile)
        with gzip.open(gz.name, 'r') as file:
            i = 0
            for row in file:
                if i == 0:
                    i = i + 1
                    continue
                # print(gzip.decompress(row).decode())
                print(row)
                print(type(row))
                print(row.decode())
                if i < 30:
                    i = i + 1
                    write_csv(dirfile, [row.decode()])
                else:
                    break
    else:
        print('the path [{}] is not exist!'.format(srcfile))


# sample_big_tar_gz('ad_feature.csv.tar.gz', "sample_tar_gz.csv")
# sample_big_tar_gz('H:\\数据\\阿里店铺——关键词\\ijcai_qui_1.tar.gz', "sample_tar_gz.csv")


def sample_big_zip(srcfile, dirfile):
    if os.path.exists(srcfile):
        zf = zipfile.ZipFile(srcfile)
        with zf.open(zf.namelist()[0], mode='r') as file:
            i = 0
            for row in file:
                i = i + 1
                if i < 30:
                    print(row)
                    write_csv(dirfile, [row.decode()])
                else:
                    break

    else:
        print('the path [{}] is not exist!'.format(srcfile))

# sample_big_zip('H:\\数据\\阿里手机端推荐算法\\tianchi_mobile_recommend_train_user.zip', "sample_zip.csv")