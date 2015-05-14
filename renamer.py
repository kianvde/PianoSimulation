__author__ = 'kian'
import os
import time
from subprocess import Popen
# This file is needed to loop over the different keys and produce their .wav file
# NB This uses the bash command 'sed' !
letters = ['A','Ab','Ad','B','C','Cd','D','Dd','E','F','Fd','G']
nums = ['3','4']
moduleNext = None
par = "Parameters.parameters"
names = ['main', 'plot_and_save','update']
for j, num in enumerate(nums):
    for i, letter in enumerate(letters):
        bashPythoncommand = "/home/kian/anaconda/bin/python"
        p = Popen([bashPythoncommand, 'main.py'])
        if num == nums[0]:
            try:
                tonePrev = letter+num
                toneNext = letters[i+1]+num
            except:
                break
            modulePrev = par+tonePrev
            moduleNext = par+toneNext
        else:
            modulePrev = moduleNext
            tonePrev = toneNext
            toneNext = letters[i]+num
            moduleNext = par+toneNext

        print modulePrev, moduleNext
        for name in names:
            bashCommand_module = "sed -i -e 's/" + modulePrev +"/"+ moduleNext+"/g' "+ "./"+name+".py"
            os.system(bashCommand_module)
            time.sleep(0.2)
            bashCommand_filename = "sed -i -e 's/" + "piano"+tonePrev +"/"+ "piano"+toneNext+"/g' "+ "./"+name+".py"
            os.system(bashCommand_filename)
            time.sleep(0.2)

# print moduleNext,modulePrev
# moduleNext == par+letters[-1]+nums[j-1]: