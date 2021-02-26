import jieba

words = open("comments.json",encoding='utf-8').read()

wordslist = jieba.cut(words)
wordcount = {}

for word in wordslist:
    if len(word) == 1:
        continue
    else:
        wordcount[word] = wordcount.get(word, 0) + 1

value = list(wordcount.items())
value.sort(key=lambda x:x[1], reverse=True)

f = open("split.json","w",encoding='utf-8')
f.write(str(value))
f.close()