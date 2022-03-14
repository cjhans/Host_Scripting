#Caleb Hansen Host Scripting Final Exam 4/27/2021

#Demonstration of loading the Regex module, the nslookup, and the logging module in order to use them later in the script
import re,logging as log

#Line that sets up the format for otu debug information that is used later in the script
log.basicConfig(level=log.DEBUG, format=' %(asctime)s -%(levelname)s -  %(message)s')

#Demonstrating the use of a variable.
#I put the output of the open function into 'openLog' and used it in the 'for' loop below.
openLog=open('/home/cjh127/Documents/secure-error-log.txt')

#Demonstration of proper debugging
#This prints what is held in the 'openLog' variable
log.debug(openLog)

#Demonstration of a for loop
#The for loop creates a variable on the fly called 'line'
#for each line in the text file, the loop prints the line variable
#This cerates a sort of reader loop
for line in openLog:
    print(line)

#Demonstration of a funciton
#Acomplishes the same task as above
#Although, this function accepts the path as a parameter and then opens that path and uses a loop to iterate and read whatever was at the end of the path
def txtReader(path):
    functionOpen=open(path)
    for line in functionOpen:
        print(line)

#Demonstration of opening and parsing log file
#Demonstration of a list
#Inputs the paths for the file I will write to and the file that is being read in order to save on screen space
writtenFilePath= '/home/cjh127/Documents/RegExLog.csv'
filenamePath= '/home/cjh127/Documents/secure-error-log.txt'
rePattern = '(Failed password for invalid user) (\w+)'
new_file=[]

#I open the log file and input a readline function in the 'lines' variable
with open(filenamePath, 'r') as s:
    lines = s.readlines()

#using a for loop I iterate through the lines variable setting up a match variable that holds my regex pattern
#using a conditional 'if' I say if the regex matches any lines I display it to the screen
#It also appends the empty list with the matching lines
for line in lines:
    match = re.search(rePattern, line)
    if match:
        new_line=match.group() + '\n'
        print(new_line)
        new_file.append(new_line)

#Finally I open the file I'll write the matchs to. Go to the start of the file and write the lines that are stored in the list.
with open(writtenFilePath, 'w') as w:
     w.seek(0)
     w.writelines(new_file)


#Demonstration of a dictionary
#I initialize the dictionary 'demoDict'
demoDict={"fruit": "Apple","color": "Red","shape" : "Round"}
#Then printign the specific item form that dictionary
print(demoDict["fruit"],demoDict["color"])


