from random import choice

def createDict(source, size): #size specifies the number of words in each state
    splitSource = source.split(" ")
    words = {}
    for index, word in enumerate(splitSource):
        if len(splitSource) < index + size + 1: #case of it not dividing evenly
            break
        tempList = splitSource[index: index+size+1]
        if tuple(tempList[0:size]) not in words:
            words[tuple(tempList[0:size])] = [tempList[size]]
        else:
            words[tuple(tempList[0:size])].append(tempList[size])
    return words

def generateText(words, size, length): #size specifies the number of words in each state, length is max characters
    upper = []
    for key in words.keys():
        try:
            if list(key)[0][0][0].isupper():
                upper.append(list(key))
        except IndexError:
            pass #empty strings
    if len(upper) > 0:
        start = choice(upper)
    else: #if no words uppercase, pick entirely by random
        start = list(choice(words.keys()))
    text = start
    currentLength = sum([len(word) for word in text]) + (size-1)
    while True:
        current = text[-size:]
        selected = choice(words[tuple(current)])
        text.append(selected)
        if len(selected) + currentLength + 1 <= length:
            currentLength = currentLength + len(selected) + 1 # +1 is to account for spaces later
        else:
            break
    return " ".join(text)
