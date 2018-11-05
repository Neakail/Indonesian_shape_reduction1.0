# -*- coding:utf-8- -*-
'''
前缀模型：实现对词语进行前缀还原
'''


class Prefix:
    '词形还原中的前缀模型，以下是四个基本规则'

    def _get_back_str(self, content, startStr):  # 定义一个模板函数(私有方法）, 返回去掉前缀后的字符串
        startIndex = content.find(startStr)
        if startIndex == 0:
            startIndex += len(startStr)
            return content[startIndex:]
        return content

    def _get_back_str2(self, content, startStr, charList):  # 定义一个模板函数(私有方法）, 假如前缀后一个字母在字母列表中，返回去掉前缀后的字符串
        startIndex = content.find(startStr)
        if startIndex == 0:
            startIndex += len(startStr)
            if content[startIndex] in charList:
                return content[startIndex:]
        return content

    def _get_back_str3(self, content, startStr, monosyllableList):  # 定义一个模板函数(私有方法）,判断如果后面为单音节词语，则返回去掉前缀的词语
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

    def _get_back_str4(self, content, startStr, stringList):  # 定义一个模板函数(私有方法）, 假如前缀后面的部分在列表中，返回去掉前缀后的字符串
        startIndex = content.find(startStr)
        if startIndex == 0:
            startIndex += len(startStr)
            if content[startIndex:] in stringList:  # 这一步与_get_back_str2不同
                return content[startIndex:]
        return content

    # 基于_get_back_str的规则构建的去前缀的函数：
    def remove_se(self, string):
        s = self._get_back_str(string, 'se')  # 基于模板创建去前缀的特定函数
        return s

    def remove_a(self, string):
        s = self._get_back_str(string, 'a')
        return s

    def remove_anti(self, string):
        s = self._get_back_str(string, 'anti')
        return s

    def remove_bi(self, string):
        s = self._get_back_str(string, 'bi')
        return s

    def remove_de(self, string):
        s = self._get_back_str(string, 'de')
        return s

    def remove_ekstra(self, string):
        s = self._get_back_str(string, 'ekstra')
        return s

    def remove_eks(self, string):
        s = self._get_back_str(string, 'eks')
        return s

    def remove_hiper(self, string):
        s = self._get_back_str(string, 'hiper')
        return s

    def remove_infra(self, string):
        s = self._get_back_str(string, 'infra')
        return s

    def remove_intra(self, string):
        s = self._get_back_str(string, 'intra')
        return s

    def remove_inter(self, string):
        s = self._get_back_str(string, 'inter')
        return s

    def remove_in(self, string):
        s = self._get_back_str(string, 'in')
        return s

    def remove_kontra(self, string):
        s = self._get_back_str(string, 'kontra')
        return s

    def remove_ko(self, string):
        s = self._get_back_str(string, 'ko')
        return s

    def remove_makro(self, string):
        s = self._get_back_str(string, 'makro')
        return s

    def remove_mikro(self, string):
        s = self._get_back_str(string, 'mikro')
        return s

    def remove_multi(self, string):
        s = self._get_back_str(string, 'multi')
        return s

    def remove_neo(self, string):
        s = self._get_back_str(string, 'neo')
        return s

    def remove_non(self, string):
        s = self._get_back_str(string, 'non')
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

    # 基于_get_back_str4的规则构建的去前缀的函数：
    def remove_se_num(self, string):
        s = self._get_back_str4(string, 'ke',
                                ['dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh',
                                 'sebelas', 'duabelas', 'tigabelas', 'empatbelas', 'limabelas', 'enambelas',
                                 'tujuhbelas', 'delapan belas', 'sembilanbelas', 'duapuluh'])
        return s

    def remove_ber_num(self, string):
        s = self._get_back_str4(string, 'ber',
                                ['dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh',
                                 'sebelas', 'duabelas', 'tigabelas', 'empatbelas', 'limabelas', 'enambelas',
                                 'tujuhbelas', 'delapan belas', 'sembilanbelas', 'duapuluh', 'ratus', 'seribu', 'juta'])
        return s

    # 对词语进行所有的前缀处理
    def remove_prefix(self, string):
        # 基于_get_back_str4的规则构建的去前缀的函数：
        s = self.remove_se_num(string)
        if s != string:
            return s
        s = self.remove_ber_num(string)
        if s != string:
            return s
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
        s = self.remove_se(string)
        if s != string:
            return s
        s = self.remove_anti(string)
        if s != string:
            return s
        # s = self.remove_a(string)
        # if s != string:
        #     return s
        s = self.remove_bi(string)
        if s != string:
            return s
        # s = self.remove_de(string)
        # if s != string:
        #     return s
        s = self.remove_ekstra(string)
        if s != string:
            return s
        s = self.remove_eks(string)
        if s != string:
            return s
        s = self.remove_hiper(string)
        if s != string:
            return s
        s = self.remove_infra(string)
        if s != string:
            return s
        s = self.remove_intra(string)
        if s != string:
            return s
        s = self.remove_inter(string)
        if s != string:
            return s
        s = self.remove_in(string)
        if s != string:
            return s
        s = self.remove_kontra(string)
        if s != string:
            return s
        s = self.remove_ko(string)
        if s != string:
            return s
        s = self.remove_makro(string)
        if s != string:
            return s
        s = self.remove_mikro(string)
        if s != string:
            return s
        s = self.remove_multi(string)
        if s != string:
            return s
        s = self.remove_neo(string)
        if s != string:
            return s
        s = self.remove_non(string)
        if s != string:
            return s
        # 如果以上方法都失败就返回原型
        return string
        #
        # c = Prefix()
        # print c.remove_prefix('mengena')
