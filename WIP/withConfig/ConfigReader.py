from chardet import detect as chardetDetect
from os import path as osPath

dirHere = osPath.dirname(__file__)

f_config = open(dirHere + '\\Config.txt', 'rb')
configChardet = chardetDetect(f_config.read())
configCodec = configChardet['encoding']
f_config.close()

f_config = open(dirHere + '\\Config.txt', 'r', encoding = configCodec)
f_configpy = open(dirHere + '\\Config.py', 'w')
f_configpy.write(f_config.read())