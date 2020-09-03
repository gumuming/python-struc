import os


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for fileName in os.listdir(path):
            childPath = os.path.join(path,fileName)
            total += disk_usage(childPath)

    print('0:<7'.format(total),path)
    return total