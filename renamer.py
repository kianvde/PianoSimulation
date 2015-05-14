__author__ = 'kian'
import os
import time
from subprocess import Popen
# This file is needed to loop over the different keys and produce their .wav file
# NB This uses the bash command 'sed' !
letters = ['A', 'Ab', 'Ad', 'B', 'C', 'Cd', 'D', 'Dd', 'E', 'F', 'Fd', 'G']
nums = ['2', '3', '4', '5']
moduleNext = None
par = "Parameters.parameters"
names = ['main', 'plot_and_save','update']
present = os.listdir("./Notes")
tonePrev = letters[0]+nums[0]
threadCount = 0
for j, num in enumerate(nums):
    for i, letter in enumerate(letters):

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
        if "piano"+tonePrev+".wav" not in present:
            print "python thread processing "+tonePrev
            bashPythoncommand = "/home/kian/anaconda/bin/python"
            threadCount += 1
            p = Popen([bashPythoncommand, 'main.py'])
        # print modulePrev, moduleNext
        for name in names:
            bashCommand_module = "sed -i -e 's/" + modulePrev +"/"+ moduleNext+"/g' "+ "./"+name+".py"
            os.system(bashCommand_module)
            time.sleep(1)
            bashCommand_filename = "sed -i -e 's/" + "piano"+tonePrev +"/"+ "piano"+toneNext+"/g' "+ "./"+name+".py"
            os.system(bashCommand_filename)
            time.sleep(1)
if "piano"+letters[-1]+nums[-1]+".wav" not in present:
    print "python thread processing "+letters[-1]+nums[-1]
    bashPythoncommand = "/home/kian/anaconda/bin/python"
    p = Popen([bashPythoncommand, 'main.py'])
    threadCount += 1
print "Thread starter complete - Total number of threads running: " + str(threadCount)