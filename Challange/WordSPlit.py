def WordSplit(strArr):
    wordToCompare = strArr[0]
    secondString = list(strArr[1].split(','))
    for i in range(len(secondString)):
        for j in range(len(secondString)):
            if secondString[i] + secondString[j] == wordToCompare:
                return ','.join([secondString[i],secondString[j]])
    return 'NotPossible'

    # res = ""
    # print(stringDict)
    # i = 1
    # while i < len(wordToCompare)


strArr = ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]
print(WordSplit(strArr))
