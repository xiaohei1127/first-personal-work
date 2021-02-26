import re
import requests
import json

comments = []
comment = []
x = 1614254331760
cursor = '0'
flag = 0

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}

for i in range(0,2000):
    url = 'https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + cursor + '&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=' + str(x)
    source = requests.get(url, headers=headers).content.decode()
    comment = re.findall('content":"(.*?),"', source, re.S)
    comments.append(comment)
    cursor = re.findall('"last":"(.*?)"', source, re.S)[0].replace("\n","").replace(" ","")
    if (flag == 0):
        x = x + 3
    else :
        x = x + 1
    flag = flag + 1
a = open("comments.json", "w", encoding='utf-8')
for elements in comments:
    for element in elements:
        a.write(element)
        a.write('\n')
a.close()
print(comments)