import os


absDir = 'E:\\api_auto_test'


def findAll(path, dirList=None, fileList=None):
    if fileList is None:
        fileList = []
    if dirList is None:
        dirList = []
    listData = os.listdir(path)
    for i in listData:
        subPath = os.path.join(path, i)
        if os.path.isdir(subPath):
            dirList.append(subPath)
            findAll(subPath, dirList, fileList)
        if os.path.isfile(subPath):
            if i.endswith('.py'):
                fileList.append(subPath)

    return fileList


if __name__ == '__main__':
    print(findAll(absDir))
