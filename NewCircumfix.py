#_*_ coding:utf-8- -*-
'''
环缀模型：实现对词语进行环缀还原
'''
class Circumfix:
    '词形还原中的环缀模型， 以下是环缀的两种形式'

    # 前缀-middle-后缀
    def _get_middle_str(self, content, startStr, endStr):  # 定义一个模板函数(私有方法）, 返回去掉环缀后的词语
        startIndex = content.find(startStr)
        endIndex = content.find(endStr)
        if startIndex == 0:
            startIndex += len(startStr)
            if endIndex == len(content) - len(endStr):
                return content[startIndex:endIndex]
        return content

    # 前缀-重叠词-后缀
    def _get_middle_str2(self, content, startStr, endStr):  # 定义一个模板函数(私有方法）, 返回去掉环缀后去掉重复缀的词语
        s = self._get_middle_str(content, startStr, endStr)
        if s != content:
            str = '-'
            if (s.find(str) != -1):
                wordlist = s.split(str)
                if (wordlist[0] == wordlist[1]):
                    finalstr = wordlist[0]
                    return finalstr
        return content

    # 基于_get_middle_str（）的规则
    def remove_ber_kan(self, string):
        s = self._get_middle_str(string, 'ber', 'kan')  # 基于模板创建去环缀的特定函数
        return s

    def remove_ber_an(self, string):
        s = self._get_middle_str(string, 'ber', 'an')
        return s

    def remove_ter_kan(self, string):
        s = self._get_middle_str(string, 'ter', 'kan')
        return s

    # 基于_get_middle_str2（）的规则
    def remove_se_nya(self,string):
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




# a = Circumfixcumfix()
# print  a.remove_cir('trperian')