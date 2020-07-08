import sys
import xml2xlsx
import traceback


def main():
    if sys.argv.__len__() < 3:
        print("格式错误，格式：<命令> <XML源文件> <XLSX目标文件>")
        return

    c = xml2xlsx.xml2xlsx()
    try:
        c.convert(sys.argv[1], sys.argv[2])
        print("处理文件%s成功" % sys.argv[1])
    except Exception as e:
        print("处理文件%s失败, 异常:%s" % (sys.argv[1], e))
        print(traceback.format_exc())


if __name__ == '__main__':
    main()