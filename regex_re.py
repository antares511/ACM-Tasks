import re

pattern = '^[aeiou]\w*[^aeiou]$' #pattern starts with vowel, any alphanumeric in between and ends with cons

def isGoodWord(inStr):
    res = inStr.split() #splits the string using any delimiter. default is space
    
    for i in range(0,len(res)):
    	if(re.match(pattern, res[i].lower())): #matches the pattern
    		print(res[i])

# Main Code 
strx = str(input(Input: ))
isGoodWord(strx) 