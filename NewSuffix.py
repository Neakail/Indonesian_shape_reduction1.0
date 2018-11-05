#encoding:utf-8

class suffix_words:

    #去后缀
    def suffix(self,word,endStr):
        if (word[len(word) - len(endStr):] == endStr):
            return word[:len(endStr)*-1]
        return word

    #-kah
    def suffix_kah(self,word):
        w = self.suffix(word,'kah')
        return w

    #-lah
    def suffix_lah(self,word):
        w = self.suffix(word,'lah')
        return w

    #-tah
    def suffix_tah(self,word):
        w = self.suffix(word,'tah')
        return w

    #-ku
    def suffix_ku(self,word):
        w = self.suffix(word,'ku')
        return w

    #-mu
    def suffix_mu(self,word):
        w = self.suffix(word,'mu')
        return w

    #-nya
    def suffix_nya(self,word):
        w = self.suffix(word,'nya')
        return w

    #-an
    def suffix_an(self,word):
        w = self.suffix(word,'an')
        numword = ['dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan',
                   'sepuluh','sebelas', 'duabelas', 'tigabelas', 'empatbelas', 'limabelas',
                   'enambelas','tujuhbelas', 'delapan belas', 'sembilanbelas', 'duapuluh']
        if w in numword:
            return w
        else:
            return word

    def suffix_final(self,word):
        word=word.lower()
        w = self.suffix_kah(word)
        if(w != word):
            return w
        w = self.suffix_lah(word)
        if(w != word):
            return w
        w = self.suffix_tah(word)
        if(w != word):
            return w
        w = self.suffix_ku(word)
        if(w != word):
            return w
        w = self.suffix_mu(word)
        if(w != word):
            return w
        w = self.suffix_nya(word)
        if(w != word):
            return w
        w = self.suffix_an(word)
        if(w != word):
            return w
        return word