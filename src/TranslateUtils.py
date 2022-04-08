import re

from XsCore import XsFso
from googletrans import Translator

'''
这个方法暂时没用到，如果需要边搜索边翻译，可以调用这个方法
'''
def autoTran(path):
        # file = open(path, mode='w', encoding="utf8")
        # file_content = file.read()  # data 是读取到的结果
        # 设置Google翻译服务地址
        translator = Translator(service_urls=[
            'translate.google.cn'
        ])
        file_content =  XsFso.readFileAnyCode(path)
        # 提取字符串里的中文，返回数组
        pattern = "[\u4e00-\u9fa5]+"
        regex = re.compile(pattern)
        results = regex.findall(file_content)
        new_list = list(set(results))
        new_list.sort(key=lambda i: len(i), reverse=True)
        print(new_list)

        for kw in new_list:
            translation = translator.translate(kw, dest='en')  # dest='zh-CN'
            print(kw, ":", translation.text)
            file_content = file_content.replace(kw, translation.text)

        XsFso.writeFile(path,file_content)
        print("已保存:", path)


