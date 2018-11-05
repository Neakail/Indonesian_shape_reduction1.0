#encoding:utf-8

class passive_words:

    #普通表示法
    def passive(self,word,startStr,endStr):
        startIndex = word.find(startStr)
        endIndex = word.find(endStr)
        if (startIndex != 0):
            return word
        else:
            if (word[len(word) - len(endStr):] == endStr):
                return word[len(startStr):len(endStr)*-1]
            if (endIndex < 0):
                return word[len(startStr):]
            return word

    #被动(删增表示法)
    def passive_add(self,word,startStr,reStr):
        startIndex = word.find(startStr)
        if(startIndex == 0):
            word_final = reStr + word[len(startStr):]
            return word_final
        return word

    # di-被动-i
    def di_passive_i(self,word):
        w = self.passive(word,'di','i')
        return w

    #diper-被动
    def diper_passive(self,word):
        w = self.passive(word,'diper',' ')
        return w

    # di-被动
    def di_passive(self, word):
        w = self.passive(word, 'di', ' ')
        return w

    #ter-被动
    def ter_passive(self,word):
        w = self.passive(word,'ter',' ')
        return w

    #删menge增di
    def menge_di_passive(self, word):
        w = self.passive_add(word, 'di','menge' )
        return w

    #删meng增dik
    def meng_dik_passive(self, word):
        w = self.passive_add(word,'dik' ,'meng' )
        return w

    #删meng增di
    def meng_di_passive(self, word):
        w = self.passive_add(word, 'di', 'meng')
        return w

    # 删meny增dis
    def meny_dis_passive(self, word):
        w = self.passive_add(word,'dis' ,'meny' )
        return w

    # 删men增dit
    def men_dit_passive(self, word):
        w = self.passive_add(word, 'dit', 'men')
        return w

    # 删mem增dip
    def mem_dip_passive(self, word):
        w = self.passive_add(word, 'dip','mem' )
        return w

    #删me增di
    def me_di_passive(self,word):
        w = self.passive_add(word,'di','me')
        return w

    def passive_final(self,word):
        word = word.lower()
        w = self.di_passive_i(word)
        if (w != word):
            return w
        w = self.diper_passive(word)
        if (w != word):
            return w
        w = self.di_passive(word)
        if (w != word):
            return w
        w = self.ter_passive(word)
        if (w != word):
            return w
        return word

    def passive_final_add(self,word):
        word = word.lower()
        w = self.menge_di_passive(word)
        if (w != word):
            return w
        w = self.meng_dik_passive(word)
        if (w != word):
            return w
        w = self.meng_di_passive(word)
        if (w != word):
            return w
        w = self.meny_dis_passive(word)
        if (w != word):
            return w
        w = self.men_dit_passive(word)
        if (w != word):
            return w
        w = self.mem_dip_passive(word)
        if (w != word):
            return w
        w = self.me_di_passive(word)
        if (w != word):
            return w
        return word