def isVowel(ch): 
    return (ch == 'a' or ch == 'e' or
            ch == 'i' or ch == 'o' or
            ch == 'u') 
#check if isVowel
  
def isGoodWord(inStr):
    res = inStr.split() #splits the string using any delimiter. default is space
    
    outStr = []
    for i in range(0,len(res)):
        if isVowel(res[i][0].lower()) == True:
            if isVowel(res[i][len(res[i]) - 1].lower()) == False:
                outStr.append(res[i])
    
    print (outStr) 
        
# Main Code 
strx = str(input("Input: "))
isGoodWord(strx)
