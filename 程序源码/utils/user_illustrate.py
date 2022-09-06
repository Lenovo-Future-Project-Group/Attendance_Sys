import os


# import re

def ini_read(path):
    """读取数据，验证数据状态"""
    try:
        with open(path, 'r+', encoding='utf-8', errors='ignore') as f:
            f.read()
    except ValueError:
        raise Exception('您的配置文件中可能没有数据，请您核验一下。')


# todo 需要完善

def ini_path():
    """读取数据，判断文件路径"""
    try:
        ini_read(os.path.abspath('.') + r'/0-说明文档和配置文档/说明文档.txt')
        return os.path.abspath('.') + r'/0-说明文档和配置文档/说明文档.txt'
    except FileNotFoundError:
        ini_read(os.path.abspath('../..') + r'/0-说明文档和配置文档/说明文档.txt')
        return os.path.abspath('../..') + r'/0-说明文档和配置文档/说明文档.txt'


# todo 需要完善

def ini():
    with open(ini_path(), 'r+', encoding='utf-8', errors='ignore') as f:
        content = f.readlines()

    if not content:
        raise Exception('说明文件丢失，需要您在【说明文件.txt】中进行编写。')

    # def ini_info(data=None):
    #     data_in = re.findall(data, content, re.S)
    #     dict_to_str = ' '.join(data_in)
    #
    #     dict_info = {}
    #     for x in dict_to_str.strip('\n').split('\n'):
    #         if not x.strip():
    #             continue
    #         j = x.split('、')
    #         dict_info[j[0]] = j[1]
    #     return dict_to_str, dict_info

    # todo 需要完善

    data = [content][0]

    return data


# todo 需要完善


if __name__ == '__main__':
    test = ini()
    print(test)
