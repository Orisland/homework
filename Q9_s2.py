class AssrtionError(Exception):
    print("非字符串类型")
    pass


def findstr(string):
    if isinstance(string,str):
        print("正常")
    else:
        raise AssrtionError

try:
    findstr(123)
except AssrtionError:
    pass