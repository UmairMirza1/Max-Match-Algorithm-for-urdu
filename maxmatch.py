
def generateDictionary():
    dictionary = set()
    file = open("testlist.txt", "r", encoding="utf8")
    for line in file:
        print(line.strip())
        dictionary.add(line.strip())
    return dictionary



def maxMatch(sentence, dictionary):
    pass

def main():
    dictionary = generateDictionary()
    #print(dictionary)

main()