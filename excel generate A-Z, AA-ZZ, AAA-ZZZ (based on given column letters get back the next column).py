# By: Abdulrahman Alamoudi
# Created Date: May 11, 2017
# status : works well

def NextColumn(string):

    # ['A', 'B', 'C', .. etc]
    alphaB = [chr(asciiNum) for asciiNum in range(65, 91)]

    # extract alphabet from string
    onlyAlpha = ""
    for char in string:
        if char.isalpha():
            onlyAlpha += char

    # if last character in 'onlyAlpha' is  n o t  'Z'
    if alphaB.index(onlyAlpha[-1]) + 1 <= alphaB.index('Z'):
        # go to next letter e.g. 'A' to 'B'
        onlyAlpha = onlyAlpha[:-1] + alphaB[alphaB.index(onlyAlpha[-1]) + 1]

    # if 'Z'
    else:

        # change last character from 'Z' to 'A'
        onlyAlpha = onlyAlpha[:-1] + 'A'

        # assume all onlyAlpha characters from first character to previous last character [:-1]
        # are 'Z'(s) >> if so, they will be change to 'A'(s) and a new 'A' will be added to the end
        isZs = True

        # loop through from from first character to previous last character [:-1]
        for pos in range(len(onlyAlpha) - 2, -1, -1):
            # if 'Z'
            if alphaB.index(onlyAlpha[pos]) + 1 > alphaB.index('Z') and isZs == True:
                onlyAlpha = onlyAlpha[:pos] + 'A' + onlyAlpha[pos+1:]

            # if not 'Z'
            else:
                if isZs == True:
                    # go to next letter e.g. 'A' to 'B' >> only once can happened >> if it happened, no more flips
                    onlyAlpha = onlyAlpha[:pos] + alphaB[alphaB.index(onlyAlpha[pos]) + 1] + onlyAlpha[pos+1:]
                isZs = False

        # only in case all characters in onlyAlpha is/are 'Z'(s)
        if isZs == True:
            onlyAlpha = onlyAlpha + 'A'

    print(onlyAlpha)
            
    
NextColumn("ABCZ")
