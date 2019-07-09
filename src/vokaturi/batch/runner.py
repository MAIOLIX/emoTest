'''
Created on 3 lug 2019

@author: maiola_st
'''
from vokaturi.batch.VokaturiHelper import  VokaturiHelper
import os

if __name__ == '__main__':
    v=VokaturiHelper()
    basePath='C:/progetti/rabbia'
    print(v.analyzeEmotion("1001_DFA_ANG_XX.wav"))
    listaFile=os.listdir(basePath)
    fileOutput=open('c:/progetti/vokaturi.txt','a')
    fileOutput.write('File;neutro;felice;triste;rabbia;paura\n')
    result=v.analyzeEmotionFromDirectory(basePath)
    fileOutput.write(result+'\n')
    fileOutput.close()