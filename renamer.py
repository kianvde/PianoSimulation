__author__ = 'kian'
import os
# This file is needed to loop over the different keys and produce their .wav file
# NB This uses the bash command 'sed' !
letters = ['A','B','C','D','E','F','G']
nums = ['3','4','5']
moduleNext = None
par = "Parameters.parameters"
for j, num in enumerate(nums):
    for i, letter in enumerate(letters[:-1]):
        bashPythoncommand = "python main.py"
        # os.system(bashPythoncommand)
        if moduleNext == par+letters[-1]+nums[j-1]:
            modulePrev = moduleNext
            tonePrev = toneNext
            toneNext = letters[i]+num
            moduleNext = par+toneNext
        else:
            tonePrev = letter+num
            toneNext = letters[i+1]+num
            modulePrev = par+letter+num
            moduleNext = par+letters[i+1]+num
        print modulePrev, moduleNext
        bashCommand_module = "sed -i -e 's/" + modulePrev +"/"+ moduleNext+"/g' "+ "./*.py"
        bashCommand_filename = "sed -i -e 's/" + "piano"+tonePrev +"/"+ "piano"+toneNext+"/g' "+ "./*.py"
        # os.system(bashCommand_module)
        # os.system(bashCommand_filename)
