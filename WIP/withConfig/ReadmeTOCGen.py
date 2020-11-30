from chardet import detect as chardetDetect
from os import path as osPath
from ConfigData import ConfigReader as Conf

# dirHere 為當前目錄，dirParent 為當前的上一層目錄
dirHere = osPath.dirname(__file__) #<-- absolute dir the script is in
dirParent = "\\".join(dirHere.split('\\')[:-1])

# 透過 chardet 套件判斷 README.md 文件編碼
f_temp = open(dirHere + '\\README.md', 'rb')
readmeChardet = chardetDetect(f_temp.read())
readmeCodec = readmeChardet['encoding']
f_temp.close()

# 以適當編碼逐行讀取 README.md 的內容到串列 f 裡面
f_readme = open(dirHere + '\\README.md', 'r', encoding = readmeCodec)
f = f_readme.readlines()

ToC_master = Conf.master

# 偵測各級標題，並加上字體樣式與錨點
for i in range(0, len(f)):

    reading = f[i]

    if ToC_master not in [1, 2, 3, 4, 5, 6]:
        f = []
        break

    # 偵測一級標題
    if ToC_master == 1:
        if reading[:2] == '# ':
            if reading[-1:] == '\n':
                reading = reading[:-1]
            readingAncher = '-'.join((''.join(reading[2:].lower().split('.'))).split(' '))
            f[i] = '* [' + reading[2:] + '](#' + readingAncher + ')\n'
            continue

    # 偵測二級標題
    if ToC_master <= 2:
        if reading[:3] == '## ':
            if reading[-1:] == '\n':
                reading = reading[:-1]
            readingAncher = '-'.join((''.join(reading[3:].lower().split('.'))).split(' '))
            f[i] = (2 - ToC_master) * '    ' + '* [' + reading[3:] + '](#' + readingAncher + ')\n'
            continue

    # 偵測三級標題
    if ToC_master <= 3:
        if reading[:4] == '### ':
            if reading[-1:] == '\n':
                reading = reading[:-1]
            readingAncher = '-'.join((''.join(reading[4:].lower().split('.'))).split(' '))
            f[i] = (2 - ToC_master) * '    ' + '* [' + reading[4:] + '](#' + readingAncher + ')\n'
            continue

    # 偵測四級標題
    if ToC_master <= 4:
        if reading[:5] == '#### ':
            if reading[-1:] == '\n':
                reading = reading[:-1]
            readingAncher = '-'.join((''.join(reading[5:].lower().split('.'))).split(' '))
            f[i] = (2 - ToC_master) * '    ' + '* [' + reading[5:] + '](#' + readingAncher + ')\n'
            continue

    # 偵測五級標題
    if ToC_master <= 5:
        if reading[:6] == '##### ':
            if reading[-1:] == '\n':
                reading = reading[:-1]
            readingAncher = '-'.join((''.join(reading[6:].lower().split('.'))).split(' '))
            f[i] = (2 - ToC_master) * '    ' + '* [' + reading[6:] + '](#' + readingAncher + ')\n'
            continue

    # 偵測六級標題
    if ToC_master <= 6:
        if reading[:7] == '###### ':
            if reading[-1:] == '\n':
                reading = reading[:-1]
            readingAncher = '-'.join((''.join(reading[7:].lower().split('.'))).split(' '))
            f[i] = (2 - ToC_master) * '    ' + '* [' + reading[7:] + '](#' + readingAncher + ')\n'
            continue

    # 判定為內文後清空
    f[i] = ''

# 以原 README.md 的編碼，將目錄寫入 ToC.md
theToC = open(dirHere + '\\ToC.md','w', encoding = readmeCodec)
theToC.writelines(f)