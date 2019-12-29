#===[ Import Additional Modules ]===#
import math     #for rounting

#===[ Initialise Variables ]===#
weights = ''        #our textfile input                  
weightList = []         #this will be the list we put our weights in
result = 0      #we do math here
outList = []        #ditto, for output

#===[ Read In Weights ]===#
"""We're going to pull the weights of all modules from a text file. Because I
wanted to play with pulling info from a text file, no other reason.
"""
f=open("weights.txt", "r")      #open the text file
if f.mode == 'r':       #inport the text file
    weights = f.read()
f.close         #close the text file

weightList = weights.split("\n")        #split the text file input into a list

#===[ The Magic ]===#
for mass in weightList:
    """Take each weight from the list, perform the calculation, and then add the
    result to the 'output' variable.
    """
    output += (math.floor(int(mass)/3)-2)
print(output)
