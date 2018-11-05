# -*- coding:utf-8- -*-
'''
环缀模型：实现对
'''


class Circumfix:
    '词形还原中的环缀模型'

    def _get_middle_str(self, content, startStr, endStr):  # 定义一个模板函数(私有方法）, 返回去掉环缀后的词语
        startIndex = content.find(startStr)
        endIndex = content.find(endStr)
        if startIndex == 0:
            startIndex += len(startStr)
            if endIndex == len(content) - len(endStr):
                return content[startIndex:endIndex]
            else:
                return content
        else:
            return content

    def _get_middle_str2(self, content, startStr, endStr):  # 定义一个模板函数(私有方法）, 返回去掉环缀后去掉重复缀的词语
        s = self._get_middle_str(content, startStr, endStr)
        if s != content:
            str = '-'
            if (s.find(str) != -1):
                wordlist = s.split(str)
                if (wordlist[0] == wordlist[1]):
                    finalstr = wordlist[0]
                    return finalstr
                else:
                    return content
            else:
                return content
        else:
            return content

    # 基于_get_middle_str（）的规则
    def remove_ber_kan(self, string):
        s = self._get_middle_str(string, 'ber', 'kan')
        return s

    def remove_ber_an(self, string):
        s = self._get_middle_str(string, 'ber', 'an')
        return s

    def remove_ter_kan(self, string):
        s = self._get_middle_str(string, 'ter', 'kan')
        return s

    # 基于_get_middle_str2（）的规则
    def remove_se_nya(self, string):
        s = self._get_middle_str2(string, 'se', 'nya')
        return s

    # 对词语进行所有的环缀处理
    def remove_circumfix(self, string):
        s = self.remove_ber_kan(string)
        if s != string:
            return s
        s = self.remove_ber_an(string)
        if s != string:
            return s
        s = self.remove_ter_kan(string)
        if s != string:
            return s
        s = self.remove_se_nya(string)
        if s != string:
            return s

        # 如果以上方法都失败就返回原型
        return string


# a = Circumfix()
# print  a.remove_circumfix('terperian')
