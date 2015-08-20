from random import choice

def createDict(source, size): #size specifies the number of words in each state
    splitSource = source.split(" ")
    words = {}
    for index, word in enumerate(splitSource):
        try:
            tempList = splitSource[index: index+size+1]
        except IndexError: #case of it not dividing evenly
            break
        if tempList[0:size] not in words:
            words[tempList[0:size]] = [tempList[size]]
        else:
            words[tempList[0:size]].append(tempList[size])
    return words

def generateText(words, size, length): #size specifies the number of words in each state, length is max characters
    upper = [key for key in words.keys() if key[0][0].isupper()]
    if len(upper) > 0:
        start = choice(upper)
    else: #if no words uppercase, pick entirely by random
        start = choice(words.keys())
    text = start
    currentLength = sum([len(word) for word in text]) + (size-1)
    while currentLength < length:
        current = text[-size:]
        selected = choice(words[current])
        text.append(selected)
        currentLength = currentLength + len(selected) + 1 # +1 is to account for spaces later
    return " ".join(text)
