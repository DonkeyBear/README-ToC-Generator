from chardet import detect as chardetDetect
from os import path as osPath

dirHere = osPath.dirname(__file__) #<-- absolute dir the script is in

# 透過 chardet 套件判斷 README.md 文件編碼
f_temp = open(dirHere + '\\README.md', 'rb')
readmeChardet = chardetDetect(f_temp.read())
readmeCodec = readmeChardet['encoding']
f_temp.close()

# 以適當編碼逐行讀取 README.md 的內容到串列 f 裡面
f_readme = open(dirHere + '\\README.md', 'r', encoding = readmeCodec)
f = f_readme.readlines()

for i in range(0, len(f)):

    reading = f[i]

    # 偵測一級標題
    if reading[:2] == '# ':
        if reading[-1:] == '\n':
            reading = reading[:-1]
        readingAncher = '-'.join((''.join(reading[2:].lower().split('.'))).split(' '))
        f[i] = '* [**' + reading[2:] + '**](#' + readingAncher + ')\n'
        continue

    # 偵測二級標題
    if reading[:3] == '## ':
        if reading[-1:] == '\n':
            reading = reading[:-1]
        readingAncher = '-'.join((''.join(reading[3:].lower().split('.'))).split(' '))
        f[i] = '    * [' + reading[3:] + '](#' + readingAncher + ')\n'
        continue

    # 偵測三級標題
    if reading[:4] == '### ':
        if reading[-1:] == '\n':
            reading = reading[:-1]
        readingAncher = '-'.join((''.join(reading[4:].lower().split('.'))).split(' '))
        f[i] = '        * [' + reading[4:] + '](#' + readingAncher + ')\n'
        continue

    # 偵測四級標題
    if reading[:5] == '#### ':
        if reading[-1:] == '\n':
            reading = reading[:-1]
        readingAncher = '-'.join((''.join(reading[5:].lower().split('.'))).split(' '))
        f[i] = '            * [' + reading[5:] + '](#' + readingAncher + ')\n'
        continue

    # 偵測五級標題
    if reading[:6] == '##### ':
        if reading[-1:] == '\n':
            reading = reading[:-1]
        readingAncher = '-'.join((''.join(reading[6:].lower().split('.'))).split(' '))
        f[i] = '                * [' + reading[6:] + '](#' + readingAncher + ')\n'
        continue

    # 偵測六級標題
    if reading[:7] == '###### ':
        if reading[-1:] == '\n':
            reading = reading[:-1]
        readingAncher = '-'.join((''.join(reading[7:].lower().split('.'))).split(' '))
        f[i] = '                    * [' + reading[7:] + '](#' + readingAncher + ')\n'
        continue

    # 判定為內文後清空
    f[i] = ''

# 以原 README.md 的編碼，將目錄寫入 ToC.md
theToC = open(dirHere + '\\ToC.md','w', encoding = readmeCodec)
theToC.writelines(f)