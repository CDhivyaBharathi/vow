def isVowel(x):
    vow = 0
    for i in x:
        if i in 'aeiouAEIOU':
            vow = 1
            break
    
    if vow == 1:
        return True
    else:
        return False

def removeVowel(x):
    str_n = ''
    for i in x:
        if i not in 'aeiouAEIOU':
            str_n += i
    
    if len(str_n) == len(x):
        return "No Vowel"
    else:
        return str_n
    
def countVowel(x):
    vow = ''
    for i in x:
        if i in 'aeiouAEIOU':
            vow+=i
        
    if len(vow) == 0:
        return "No vowel"
    else:
        return len(vow)
    
