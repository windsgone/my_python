original = raw_input('Enter a word:')
word = original.lower()
first = word[0]
pyg = 'ay'
new_word = word + pyg

"""判断输入的单词是否可用，若可用按首字母类型进行处理
"""

if len(original) > 0 and original.isalpha():
    if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
        print new_word
    else:
        new_word = word[1:] + first + pyg
        print new_word
else:
    print 'empty'