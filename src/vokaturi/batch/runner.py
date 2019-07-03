'''
Created on 3 lug 2019

@author: maiola_st
'''
from vokaturi.batch.VokaturiHelper import  VokaturiHelper
import os

if __name__ == '__main__':
    v=VokaturiHelper()
    basePath='c:/progetti/emovo/gioia'
    print(v.analyzeEmotion("cliente1.wav"))
    listaFile=os.listdir(basePath)
    fileOutput=open('c:/progetti/vokaturi.txt','a')
    for pippo in listaFile:
        filePath=basePath+'/'+pippo
        result=v.analyzeEmotion(filePath)
        fileOutput.write(result+'\n')
    fileOutput.close()