from chardet import detect as chardetDetect
from os import path as osPath
from ConfigData import ConfigReader
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

# 定義 eraseChar() 函數，用以去除文字
def eraseChar(stringTarget):
    eraseResult = stringTarget
    # 以 eraseTarget 函數記錄要去除的「字」
    eraseTarget = '.`[]()'
    eraseList = [] 
    eraseList[:0] = eraseTarget
    for j in range(0, len(eraseList)):
        eraseResult = ''.join(eraseResult.split(eraseList[j]))
    return eraseResult

# 定義 deLink() 函數，用以去除超連結
# TODO
#def deLink(titleLevel, stringTitle):
    #delinkTitle = stringTitle[titleLevel + 1:]

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
                reading = reading[2:-1]
            readingAnchor = '-'.join(eraseChar(reading.lower()).split(' '))
            f[i] = v_BQ + '* [' + v_style1 + reading + v_style1 + '](#' + readingAnchor + ')\n'
            continue

    # 偵測二級標題
    if ToC_master <= 2:
        if reading[:3] == '## ':
            if reading[-1:] == '\n':
                reading = reading[3:-1]
            readingAnchor = '-'.join(eraseChar(reading.lower()).split(' '))
            f[i] = v_BQ + (2 - ToC_master) * '    ' + '* [' + v_style2 + reading + v_style2 + '](#' + readingAnchor + ')\n'
            continue

    # 偵測三級標題
    if ToC_master <= 3:
        if reading[:4] == '### ':
            if reading[-1:] == '\n':
                reading = reading[4:-1]
            readingAnchor = '-'.join(eraseChar(reading.lower()).split(' '))
            f[i] = v_BQ + (3 - ToC_master) * '    ' + '* [' + v_style3 + reading + v_style3 + '](#' + readingAnchor + ')\n'
            continue

    # 偵測四級標題
    if ToC_master <= 4:
        if reading[:5] == '#### ':
            if reading[-1:] == '\n':
                reading = reading[5:-1]
            readingAnchor = '-'.join(eraseChar(reading.lower()).split(' '))
            f[i] = v_BQ + (4 - ToC_master) * '    ' + '* [' + v_style4 + reading + v_style4 + '](#' + readingAnchor + ')\n'
            continue

    # 偵測五級標題
    if ToC_master <= 5:
        if reading[:6] == '##### ':
            if reading[-1:] == '\n':
                reading = reading[6:-1]
            readingAnchor = '-'.join(eraseChar(reading.lower()).split(' '))
            f[i] = v_BQ + (5 - ToC_master) * '    ' + '* [' + v_style5 + reading + v_style5 + '](#' + readingAnchor + ')\n'
            continue

    # 偵測六級標題
    if ToC_master <= 6:
        if reading[:7] == '###### ':
            if reading[-1:] == '\n':
                reading = reading[7:-1]
            readingAnchor = '-'.join(eraseChar(reading.lower()).split(' '))
            f[i] = v_BQ + (6 - ToC_master) * '    ' + '* [' + v_style6 + reading + v_style6 + '](#' + readingAnchor + ')\n'
            continue

    # 判定為內文後清空
    f[i] = ''

# 以原 README.md 的編碼，將目錄寫入 ToC.md
theToC = open(dirHere + '\\ToC.md','w', encoding = readmeCodec)
theToC.writelines(f)