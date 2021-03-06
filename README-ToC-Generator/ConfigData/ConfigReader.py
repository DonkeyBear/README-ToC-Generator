from chardet import detect as chardetDetect
from os import path as osPath

dirHere = osPath.dirname(__file__)
dirParent = "\\".join(dirHere.split('\\')[:-1])

# 判斷 Config.txt 編碼
f_config = open(dirParent + '\\Config.txt', 'rb')
configChardet = chardetDetect(f_config.read())
configCodec = configChardet['encoding']
f_config.close()

# 讀取 Config.txt 並寫入 Config.py
f_config2 = open(dirParent + '\\Config.txt', 'r', encoding = configCodec)
f_configpy = open(dirHere + '\\ConfigPY.py', 'w', encoding = configCodec)
f_configpy.write(f_config2.read())
f_config2.close()
f_configpy.close()