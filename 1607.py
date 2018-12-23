times = int(input())
alphabet = list("abcdefghijklmnopqrstuvwxyz")
total = 0
for i in range(times):
    string = str(input()).split(" ")
    str1, str2 = string
    lis1 = list(str1)
    lis2 = list(str2)

    j = 0 
    while j < len(str1):
        posit1 = alphabet.index(lis1[j])
        posit2 = alphabet.index(lis2[j])
        if (posit1 > posit2):
            size = len(alphabet) - posit1 + posit2
        else: 
            size = posit2 - posit1
        total += size
        j+=1
    print(total)
    total = 0
        
