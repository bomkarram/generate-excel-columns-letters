# By: Abdulrahman Alamoudi
# Created Date: Nov 21, 2016
# status : works but not polished

def WhichPosition(num):
    position = 0
    for x in range(1, num+1):
        if x != num:
            position += (26 ** x)
    return position


def main():
    AZLetters = []

    for letter in range(65, 91): #A - Z (65 - 90)
        AZLetters.append(chr(letter))

    excelLetterList = AZLetters

    letterDigits = 4 # enter maximum of letter 
    totalLength = 26**(letterDigits) # digit number needed

    pos = WhichPosition(letterDigits)
                            # ex : A is from A to Z (26)
                            #           it should starts at position 1
                            #      AA is from AA to ZZ (26 ** 2 = 676) ***without including the first A(26))
                            #           it should starts at position 26
                            #      AAA is from AAA to ZZZ (26 ** 3 = 17576) ***without including the first A(26)) + AA(676)
                            #           it should starts at position 702
    while True:
        for x in excelLetterList:
            for letter in range(0, 26):
                excelLetterList.append(x + AZLetters[letter])
                print(x + AZLetters[letter])
            if len(excelLetterList[pos:]) == totalLength:
                break
        if len(excelLetterList[pos:]) == totalLength:
            break
    #print(excelLetterList, "\n",len(excelLetterList), "\n",pos)

main()
