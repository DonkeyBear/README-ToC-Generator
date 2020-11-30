from os import path as osPath

dirHere = osPath.dirname(__file__)

print('\n　　　'+dirHere+'\n')

dirHere = "\\".join(dirHere.split('\\')[:-1])

print('\n　　　'+dirHere+'\n')