import json


# 从json文件读取数据的函数
def read_from_json(file_name):
    # 打开文件的模式: 常用的有’r’（读取模式，缺省值）、‘w’（写入模式）、‘a’（追加模式）等
    # 这里encoding是定义打开文件时使用的编码方式，这里使用的是utf-8
    with open('./{}'.format(file_name), 'r', encoding='utf-8') as f:
        # 使用json.load()函数加载JSON文件，该函数可以从文件中读取JSON格式的数据并将其解析为Python对象
        data1 = json.load(f)

    return data1


if __name__ == '__main__':
    # 调用read_from_json()函数读取data.json的数据
    # 输出读取到的数据
    print(read_from_json('data.json'))
