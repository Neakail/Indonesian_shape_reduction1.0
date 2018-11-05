#encoding:utf-8

class reduplication_words:

    #单纯重叠
    def reduplication(self,word):
        str = '-'
        if(word.find(str)!=-1):
            wordlist = word.split(str)
            if(wordlist[0] == wordlist[1]):
                finalstr = wordlist[0]
                return finalstr
            else:
                return word
        else:
            return word

    #-an重叠
    def reduplication_an(self,word):
        str = 'an'
        if(word[-2:] == str):
            word_no_affix = word[:-2]
            finalstr = self.reduplication(word_no_affix)
            if(finalstr == word_no_affix):
                return word
            else:
                return finalstr
        else :
            return word

    #ber-重叠
    def ber_reduplication(self,word):
        str = 'ber'
        if (word[:3] == str):
            word_no_affix = word[3:]
            finalstr = self.reduplication(word_no_affix)
            if(finalstr == word_no_affix):
                return word
            else :
                return finalstr
        else:
            return word

    #me-重叠
    def me_reduplication(self,word):
        str = 'me'
        if (word[:2] == str):
            word_no_affix = word[2:]
            finalstr = self.reduplication(word_no_affix)
            if (finalstr == word_no_affix):
                return word
            else:
                return finalstr
        else:
            return word

    #di-重叠
    def di_reduplication(self,word):
        str = 'di'
        if (word[:2] == str):
            word_no_affix = word[2:]
            finalstr = self.reduplication(word_no_affix)
            if (finalstr == word_no_affix):
                return word
            else:
                return finalstr
        else:
            return word

    #ter-重叠
    def ter_reduplication(self,word):
        str = 'ter'
        if (word[:3] == str):
            word_no_affix = word[3:]
            finalstr = self.reduplication(word_no_affix)
            if (finalstr == word_no_affix):
                return word
            else:
                return finalstr
        else:
            return word

    #me-重叠-an
    def me_reduplication_an(self,word):
        str1 = 'me'
        str2 = 'an'
        if (word[:2] == str1 and word[-2:] == str2):
            word_no_affix = word[2:-2]
            finalstr = self.reduplication(word_no_affix)
            if (finalstr == word_no_affix):
                return word
            else:
                return finalstr
        else:
            return word

    #ber-重叠-an
    def ber_reduplication_an(self,word):
        str1 = 'ber'
        str2 = 'an'
        if (word[:3] == str1 and word[-2:] == str2):
            word_no_affix = word[3:-2]
            finalstr = self.reduplication(word_no_affix)
            if (finalstr == word_no_affix):
                return word
            else:
                return finalstr
        else:
            return word

    #重叠-me-重叠
    def reduplication_me_re(self,word):
        str = 'me'
        if (word.find(str) != -1):
            wordlist = word.split(str)
            if (wordlist[0] == wordlist[1]):
                finalstr = wordlist[0]
                return finalstr
            else:
                return word
        else:
            return word

    def reduplication_final(self,word):
        w = self.reduplication(word)
        if (w!=word):
            return w
        w = self.me_reduplication_an(word)
        if (w!=word):
            return w
        w = self.ber_reduplication_an(word)
        if (w!=word):
            return w
        w = self.reduplication_an(word)
        if (w!=word):
            return w
        w = self.ber_reduplication(word)
        if (w!=word):
            return w
        w = self.me_reduplication_an(word)
        if (w!=word):
            return w
        w = self.di_reduplication(word)
        if (w!=word):
            return w
        w = self.ter_reduplication(word)
        if (w!=word):
            return w
        w = self.reduplication_me_re(word)
        if (w!=word):
            return w
        return word
