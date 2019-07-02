import re

def printPercentage(woord, woordpercentage):
    wordLengte = len(woord);
    print(woord + (int(15 - wordLengte) * " ") + ":" + "[" + ("=" * round(woordpercentage / 10)) + (" " * (10 - round(woordpercentage / 10))) + "]" + "\t" + str(round(woordpercentage, 1)) + "%")

def printSpaces(aantalSpaties):
    print(aantalSpaties*"\n")

def checkOccurences(checkwords, txtwords, appearencewords):
    for word in checkwords:
        if word in txtwords:
            if word not in appearencewords:
                #give word 1 appereance
                appearencewords[word] = 1
            else:
                #if it already had an appearence add 1 to the count
                appearencewords[word] = appearencewords[word] + 1

def checkHighestkeyNumber(appearencewords):
    #check for the highest key value
    mostTimes = max(appearencewords.items(), key=lambda k: k[1])[1]
    return mostTimes

def stripSpaces(txt):
    textwords = {}
    for line in txt:
        #strip txt with spaces
        textwords[line.strip("\n")] = line.strip("\n")
    return textwords

def addMostOccurredWordsToWinners(appearencewords):
    potentialWinners = {}
    for word in appearencewords:
        if appearencewords[word] == checkHighestkeyNumber(appearencewords):
            #adding the highest occuring words to the potentialWinners dictionary
            potentialWinners[word] = checkHighestkeyNumber(appearencewords)

    return potentialWinners

def addPercentageBarToWords(potentialWinners):
    #loop thru potentialWinners
    for word in potentialWinners:
        #calculate the percentage and print the percentage bar
        wordPercentage = 100 / len(potentialWinners)
        printPercentage(word, wordPercentage)

def main():
    txt = open('Zelfstandignaamwoorden.txt', encoding='utf-8')
    txtwords = {}
    checktxt = input("Checktxt : ")
    checkwords = re.findall(r'\S+', checktxt)
    appearencewords = {}
    potentialWinners = {}

    #run stripspaces
    txtwords = stripSpaces(txt)

    #run checkOccurences
    checkOccurences(checkwords, txtwords, appearencewords)

    #run addmostoccuredWordsToWinners
    potentialWinners = addMostOccurredWordsToWinners(appearencewords)


    #run printSpaces
    printSpaces(50)

    #run addPercentageBarToWords
    addPercentageBarToWords(potentialWinners)

main()