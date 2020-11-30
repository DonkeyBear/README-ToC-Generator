from chardet import detect as chardetDetect
from os import path as osPath
from ConfigData import ConfigPY as Conf

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

# 匯入 ConfigPY.py 為 Conf 後，設置好變數及其意義 
ToC_master = Conf.ToC_master
v_style1 = Conf.ToC_h1_style * '*'
v_style2 = Conf.ToC_h2_style * '*'
v_style3 = Conf.ToC_h3_style * '*'
v_style4 = Conf.ToC_h4_style * '*'
v_style5 = Conf.ToC_h5_style * '*'
v_style6 = Conf.ToC_h6_style * '*'

v_BQ = ''
if Conf.ToC_in_blockquote == 1:
    v_BQ = '> '

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
            f[i] = v_BQ + '* [' + v_style1 + reading[2:] + v_style1 + '](#' + readingAncher + ')\n'
            continue

    # 偵測二級標題
    if ToC_master <= 2:
        if reading[:3] == '## ':
            if reading[-1:] == '\n':
                reading = reading[:-1]
            readingAncher = '-'.join((''.join(reading[3:].lower().split('.'))).split(' '))
            f[i] = v_BQ + (2 - ToC_master) * '    ' + '* [' + v_style2 + reading[3:] + v_style2 + '](#' + readingAncher + ')\n'
            continue

    # 偵測三級標題
    if ToC_master <= 3:
        if reading[:4] == '### ':
            if reading[-1:] == '\n':
                reading = reading[:-1]
            readingAncher = '-'.join((''.join(reading[4:].lower().split('.'))).split(' '))
            f[i] = v_BQ + (3 - ToC_master) * '    ' + '* [' + v_style3 + reading[4:] + v_style3 + '](#' + readingAncher + ')\n'
            continue

    # 偵測四級標題
    if ToC_master <= 4:
        if reading[:5] == '#### ':
            if reading[-1:] == '\n':
                reading = reading[:-1]
            readingAncher = '-'.join((''.join(reading[5:].lower().split('.'))).split(' '))
            f[i] = v_BQ + (4 - ToC_master) * '    ' + '* [' + v_style4 + reading[5:] + v_style4 + '](#' + readingAncher + ')\n'
            continue

    # 偵測五級標題
    if ToC_master <= 5:
        if reading[:6] == '##### ':
            if reading[-1:] == '\n':
                reading = reading[:-1]
            readingAncher = '-'.join((''.join(reading[6:].lower().split('.'))).split(' '))
            f[i] = v_BQ + (5 - ToC_master) * '    ' + '* [' + v_style5 + reading[6:] + v_style5 + '](#' + readingAncher + ')\n'
            continue

    # 偵測六級標題
    if ToC_master <= 6:
        if reading[:7] == '###### ':
            if reading[-1:] == '\n':
                reading = reading[:-1]
            readingAncher = '-'.join((''.join(reading[7:].lower().split('.'))).split(' '))
            f[i] = v_BQ + (6 - ToC_master) * '    ' + '* [' + v_style6 + reading[7:] + v_style6 + '](#' + readingAncher + ')\n'
            continue

    # 判定為內文後清空
    f[i] = ''

# 以原 README.md 的編碼，將目錄寫入 ToC.md
theToC = open(dirHere + '\\ToC.md','w', encoding = readmeCodec)
theToC.writelines(f)