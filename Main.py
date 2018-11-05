# -*- coding:utf-8 -*-
from NewNewCircumfix import Circumfix
from NewNewPassive import passive_words
from NewNewPrefix import Prefix
from NewSuffix import suffix_words
from NewReduplication import reduplication_words
import xlwt

rule_file = open('rule.txt', 'r')
rule = {}
for i in rule_file.readlines():
    rule[i.strip().split('\t')[0]] = i.strip().split('\t')[1]
rule_file.close()


def main(string):
    if string in rule:
        return rule[string]

    flag = 1
    if '-' in string.strip():
        words = string.strip().split('-')
        for word in words:
            if len(word) < 4:
                flag = 0
    if flag == 0:
        return string

    circumfix = Circumfix()
    passive = passive_words()
    prefix = Prefix()
    suffix = suffix_words()
    reduplication = reduplication_words()

    # with open('indword.txt', 'r') as f:
    #     words = [i.strip() for i in f.readlines()]

    # flag为0表示还未还原成功,1表示还原成功
    #flag = 0

    # # 环缀
    # reduction_word = circumfix.remove_circumfix(string)
    # if reduction_word != string:
    #     if reduction_word not in words:
    #         flag = 0
    #     else:
    #         string = reduction_word
    #         flag = 1
    #
    # # 前缀
    # if flag == 0:
    #     reduction_word = prefix.remove_prefix(string)
    #     if reduction_word not in words:
    #         flag = 0
    #     else:
    #         string = reduction_word
    #         flag = 1
    #
    # # 被动第一种情况
    # if flag == 0:
    #     reduction_word = passive.passive_final(string)
    #     if reduction_word not in words:
    #         flag = 0
    #     else:
    #         string = reduction_word
    #         flag = 1
    #
    # # 被动第二种情况
    # if flag == 0:
    #     reduction_word = passive.passive_final_add(string)
    #     if reduction_word not in words:
    #         flag = 0
    #     else:
    #         string = reduction_word
    #         flag = 1
    #
    # # 后缀
    # if flag == 0:
    #     reduction_word = suffix.suffix_final(string)
    #     if reduction_word not in words:
    #         flag = 0
    #     else:
    #         string = reduction_word
    #         flag = 1

    # 重叠
    # if flag == 0:
    #     reduction_word = reduplication.reduplication_final(string)
    #     if reduction_word in words:
    #         string = reduction_word
    for i in xrange(2):
        string = reduplication.reduplication_final(string)
        string = circumfix.remove_circumfix(string)
        # string = suffix.suffix_final(string)
        try:
            string = prefix.remove_prefix(string)
        except:
            pass
        string = passive.passive_final(string)
        string = passive.passive_final_add(string)

    # if len(string) > 4:
    #     if string[-2:] == 'in':
    #         string = string[:-2]
    # if len(string) > 4:
    #     if string[-1] == 'i':
    #         string = string[:-1]


    # per-an、mem-、men-、memper-、me-还有pe-、ber-
    for i in xrange(2):

        # per-kan
        if len(string) > 7:
            if string[:3] == 'per' and string[-3:] == 'kan':
                string = string[3:-3]

        # pe-kan
        if len(string) > 6:
            if string[:2] == 'pe' and string[-3:] == 'kan':
                string = string[2:-3]

        # se-nya
        if len(string) > 6:
            if string[:2] == 'se' and string[-3:] == 'nya':
                string = string[2:-3]

        # per-kan
        if len(string) > 7:
            if string[:3] == 'per' and string[-2:] == 'kan':
                string = string[3:-2]

        # per-an
        if len(string) > 7:
            if string[:3] == 'per' and string[-2:] == 'an':
                string = string[3:-2]

        if len(string) > 7:
            if string[:3] == 'pem' and string[-2:] == 'an':
                string = string[3:-2]

        if len(string) > 6:
            if string[:2] == 'pe' and string[-2:] == 'an':
                string = string[2:-2]

        # ke-an
        if len(string) > 6:
            if string[:2] == 'ke' and string[-2:] == 'an' and string[-3] != 'kan':
                string = string[2:-2]

        string = reduplication.reduplication_final(string)

        if len(string) > 5:
            if string[-3:] == 'kan' and string[-4] != '-':
                string = string[:-3]
        string = reduplication.reduplication_final(string)

        if len(string) > 8:
            if string[:6] == 'memper':
                string = string[6:]

        if len(string) > 6:
            if string[:4] == 'meng':
                string = string[4:]

        if len(string) > 6:
            if string[:4] == 'peng':
                string = string[4:]

        if len(string) > 5:
            if string[:3] == 'men':
                string = string[3:]

        if len(string) > 5:
            if string[:3] == 'mem':
                string = string[3:]

        if len(string) > 5:
            if string[:3] == 'pen':
                string = string[3:]

        if len(string) > 5:
            if string[:3] == 'pem':
                string = string[3:]

        if len(string) > 5:
            if string[:3] == 'ber':
                string = string[3:]

        if len(string) > 4:
            if string[:2] == 'me':
                string = string[2:]

        if len(string) > 4:
            if string[:2] == 'pe':
                string = string[2:]

        # if len(string) > 8:
        #     if string[-6:] == 'kannya':
        #         string = string[:-6]
        # string = reduplication.reduplication_final(string)

        if len(string) > 5:
            if string[-3:] == 'nya' and string[-4] != '-':
                string = string[:-3]
        string = reduplication.reduplication_final(string)


        if len(string) > 4:
            if string[-2:] == 'an':
                string = string[:-2]
        string = reduplication.reduplication_final(string)

    return string


if __name__ == '__main__':
    # main('sebaiknya')
    f = open('/home/linnankai/PycharmProjects/difference_analysis 2/result/new_all_ind_word_sorted_processed_daxiaoxie_168048.txt', 'r')
    g = open('result6.txt', 'w')
    for i in f.readlines():
        word = i.strip().split(' ')[0].lower()
        if len(word) > 5:
            # print word
            reduction_word = main(word)
            # print reduction_word
            if word != reduction_word:
                if len(reduction_word) > 3:
                    g.write(word + ' ' + reduction_word)
                    g.write('\n')
                    if '-' in reduction_word:
                        print word,reduction_word
    f.close()
    g.close()
