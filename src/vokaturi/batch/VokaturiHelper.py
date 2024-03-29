'''
Created on 3 lug 2019

@author: maiola_st
'''
import sys
from scipy.io import wavfile
sys.path.append("../api")
import Vokaturi
import scipy.io.wavfile
import os

class VokaturiHelper(object):
    
    
    def __init__(self):
        self.__checkOS()
        if self.__osSystem=='win32':
            print ("Loading library...")
            Vokaturi.load("../lib/open/win/OpenVokaturi-3-3-win64.dll")
    
    def __checkOS(self):
        self.__osSystem=sys.platform
    
    def getOS(self):
        print ("Analyzed by: %s" % Vokaturi.versionAndLicense())
    
   
    def analyzeEmotion(self,filePath):
        
        try:
            (sample_rate,samples)=wavfile.read(filePath)
            print ("   sample rate %.3f Hz" % sample_rate)
            #print ("   samples %.3f Hz" % len(samples))
        
            buffer_length = len(samples)
            c_buffer = Vokaturi.SampleArrayC(buffer_length)
            if samples.ndim == 1:  # mono
                c_buffer[:] = samples[:] / 32768.0
            else:  # stereo
                c_buffer[:] = 0.5*(samples[:,0]+0.0+samples[:,1]) / 32768.0
            voice = Vokaturi.Voice (sample_rate, buffer_length)
            voice.fill(buffer_length, c_buffer)
            quality = Vokaturi.Quality()
            emotionProbabilities = Vokaturi.EmotionProbabilities()
            voice.extract(quality, emotionProbabilities)
            result=filePath
            if quality.valid:
            #print ("Neutral: %.3f" % emotionProbabilities.neutrality)
            #print ("Happy: %.3f" % emotionProbabilities.happiness)
            #print ("Sad: %.3f" % emotionProbabilities.sadness)
            #print ("Angry: %.3f" % emotionProbabilities.anger)
            #print ("Fear: %.3f" % emotionProbabilities.fear)
                result=result+";%.3f"%emotionProbabilities.neutrality+";%.3f"%emotionProbabilities.happiness+";%.3f"%emotionProbabilities.sadness+";%.3f"%emotionProbabilities.anger+";%.3f"%emotionProbabilities.fear
            else:
                print ("Not enough sonorancy to determine emotions")
            voice.destroy()
            return result
        except :
            print(filePath)


    def analyzeEmotionFromDirectory(self,filePath):
        listaFile=os.listdir(filePath)
        result=''
        for file in listaFile:
            pathOfFile=filePath+'/'+file
            app=self.analyzeEmotion(pathOfFile)
            if app is not None:
                result=result+'\n'+app
        return result