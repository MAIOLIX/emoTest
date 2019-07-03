'''
Created on 3 lug 2019

@author: maiola_st
'''
from vokaturi.batch.VokaturiHelper import  VokaturiHelper

if __name__ == '__main__':
    v=VokaturiHelper()
    print(v.analyzeEmotion("cliente1.wav"))