# _*_ coding:utf-8- -*-
'''
前缀模型：实现对词语进行前缀还原
'''


class Prefix:
    '词形还原中的前缀模型，以下是四个基本规则'

    # 定义一个模板函数(私有方法）, 返回去掉前缀后的字符串
    def _get_back_str(self, content, startStr):
        startIndex = content.find(startStr)
        if startIndex == 0:
            startIndex += len(startStr)
            return content[startIndex:]
        return content

    # 定义一个模板函数(私有方法）, 假如前缀后一个字母在字母列表中，返回去掉前缀后的字符串
    def _get_back_str2(self, content, startStr, charList):
        startIndex = content.find(startStr)
        if startIndex == 0:
            startIndex += len(startStr)
            if content[startIndex] in charList:
                return content[startIndex:]
        return content

    # 定义一个模板函数(私有方法）,判断如果后面为单音节词语，则返回去掉前缀的词语
    def _get_back_str3(self, content, startStr, monosyllableList):
        startIndex = content.find(startStr)
        if startIndex == 0:
            startIndex += len(startStr)
            num = 0
            if len(content[startIndex:]) >= 2:
                for each in monosyllableList:
                    num += content[startIndex:].count(each)
                if num == 1:
                    return content[startIndex:]
        return content


    # 基于_get_back_str的规则构建的去前缀的函数：
    def remove_se(self, string):
        s = self._get_back_str(string, 'se')  # 基于模板创建去前缀的特定函数
        return s

    def remove_bi(self, string):
        s = self._get_back_str(string, 'bi')
        return s

    def remove_hiper(self, string):
        s = self._get_back_str(string, 'hiper')
        return s

    # 基于_get_back_str2的规则构建的去前缀的函数：
    def remove_meng(self, string):
        s = self._get_back_str2(string, 'meng', ['a', 'e', 'g', 'h', 'i', 'u', 'o'])
        return s

    def remove_men(self, string):
        s = self._get_back_str2(string, 'men', ['c', 'd', 'j'])
        return s

    # 基于_get_back_str3的规则构建的去前缀的函数：
    def remove_menge(self, string):
        s = self._get_back_str3(string, 'menge', ['a', 'e', 'i', 'u', 'o'])
        return s

    # 对词语进行所有的前缀处理
    def remove_prefix(self, string):
        # 基于_get_back_str3的规则构建的去前缀的函数：
        s = self.remove_menge(string)
        if s != string:
            return s
        # 基于_get_back_str2的规则构建的去前缀的函数：
        s = self.remove_meng(string)
        if s != string:
            return s
        s = self.remove_men(string)
        if s != string:
            return s
        # 基于_get_back_str的规则构建的去前缀的函数：
        # s = self.remove_se(string)
        # if s != string:
        #     return s
        s = self.remove_bi(string)
        if s != string:
            return s
        s = self.remove_hiper(string)
        if s != string:
            return s
        # 如果以上方法都失败就返回原型
        return string

c = Prefix()
print c.remove_prefix('mengena')