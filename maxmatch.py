def generateDictionary():
    dictionary = set()
    file = open("wordlist.txt", "r", encoding="utf-8-sig")
    for line in file:
        dictionary.add(line.strip())
    return dictionary


def maxMatch(sentenceFile, dictionary):
    fileHandle = open(sentenceFile, "r", encoding="utf-8-sig")
    index = 0
    segmentSentences = []
    for line in fileHandle:
        print(line.strip())
        index += 1
        print("Line Number: " + str(index))
        snt = segmentSentence(line.strip(), dictionary)
        print(snt)
        segmentSentences.append(snt)
    return segmentSentences


def segmentSentence(sentence, dictionary):
    sentenceIndex = 0
    wordIndex = 0
    segmentedSentence = []
    #print(len(sentence))
    while sentenceIndex < len(sentence):
        tempMatchList = []
        for word in dictionary:
            wordIndex = 0
            currentSentenceIndex = sentenceIndex
            flag = True
            #print("word: " + word)
            while wordIndex < len(
                    word) and flag and currentSentenceIndex < len(sentence):

                if sentence[currentSentenceIndex] == word[wordIndex]:
                    wordIndex += 1
                    currentSentenceIndex += 1
                    if wordIndex == len(word):
                        tempMatchList.append(word)
                        #print("appended word: " + word)
                        currentSentenceIndex = 0
                        break
                else:
                    flag = False

        if (len(tempMatchList) > 0):
            segmentedSentence.append(max(tempMatchList, key=len))
            sentenceIndex = sentenceIndex + len(max(tempMatchList, key=len))
        else:
            segmentedSentence.append(sentence[sentenceIndex])
            sentenceIndex += 1
    return segmentedSentence


def countCharPerToken(filename):
    fileHandle = open(filename, "r", encoding="utf-8-sig")
    x = fileHandle.read().split()
    numberOfTokens = len(x)
    numberOfChars = 0
    for token in x:
        numberOfChars += len(token)
    avgCharsPerToken = numberOfChars / numberOfTokens
    return avgCharsPerToken


if __name__ == "__main__":
    dictionary = generateDictionary()
    parsedSentences = maxMatch("50_nospaces.txt", dictionary)
   # print(parsedSentences)
    file = open('Resultsentences.txt', 'w', encoding="utf-8-sig")
    for parsedSentence in parsedSentences:
       # print(' '.join(map(str,parsedSentence)))
        file.write(' '.join(map(str,parsedSentence)))
        file.write("\n")
    file.close()
# avg = countCharPerToken("urdu-test.txt")
# print(avg)
