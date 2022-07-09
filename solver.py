# Global Variables


alphabet = "abcdefghijklmnopqrstuvwxyz"
file = open('wordlist.txt', 'r')
wordlist = ((file.read()).strip()).split()

# Finds grey letters in the guess


def greyLetters(result, guess):
    greyLettersArray = []
    for i in range(0, 5):
        if result[i] == 'w':
            greyLettersArray.append(guess[i])

    return greyLettersArray

# Finds yellow letters in the guess


def yellowLetters(result, guess):
    yellowLettersArray = []
    for i in range(0, 5):
        if result[i] == 'y':
            yellowLettersArray.append([guess[i], i])

    return yellowLettersArray

# Finds green letters in the guess


def greenLetters(result, guess):
    greenLettersArray = []
    for i in range(0, 5):
        if result[i] == "g":
            greenLettersArray.append([guess[i], i])

    return greenLettersArray


def removeWord(result, guess, possibleWords):
    greyLettersArray = greyLetters(result, guess)
    yellowLettersArray = yellowLetters(result, guess)
    greenLettersArray = greenLetters(result, guess)
    goodLetters = []

    for g in greenLettersArray:
        goodLetters.append(g[0])
    for y in yellowLettersArray:
        goodLetters.append(y[0])

    acceptableWords1 = []
    for w in possibleWords:
        check = 0
        for b in greyLettersArray:
            if b in w:
                if b in goodLetters:
                    pass
                else:
                    check = 1
                    break
        if check == 0:
            acceptableWords1.append(w)

    acceptableWords2 = []
    for w in acceptableWords1:
        check = 0
        for g in greenLettersArray:
            if w[g[1]] != g[0]:
                check = 1
                break
        if check == 0:
            acceptableWords2.append(w)

    acceptableWords3 = []
    for w in acceptableWords2:
        check = 0
        for p in yellowLettersArray:
            if w[p[1]] == p[0]:
                check = 1
                break
        if check == 0:
            acceptableWords3.append(w)

    acceptableWords4 = []
    for w in acceptableWords3:
        check = 0
        for g in goodLetters:
            if g not in w:
                check = 1
                break
        if check == 0:
            acceptableWords4.append(w)

    acceptableWords5 = []
    for w in acceptableWords4:
        check = 0
        for b in greyLettersArray:
            if b in greenLettersArray:
                if w.count(b) != greenLettersArray.count(b):
                    check = 1
                    break
        if check == 0:
            acceptableWords5.append(w)

    return acceptableWords5

# Finds frequencies of letters in each position


def letterFreq(possibleWords):
    arr = {}
    for c in alphabet:
        freq = [0, 0, 0, 0, 0]
        for i in range(0, 5):
            for w in possibleWords:
                if w[i] == c:
                    freq[i] += 1
        arr.update({c: freq})

    return arr

# Gives score based on frequency of letters


def wordScore(possibleWords, frequencies):
    words = {}
    maxFreq = [0, 0, 0, 0, 0]
    for c in frequencies:
        for i in range(0, 5):
            if maxFreq[i] < frequencies[c][i]:
                maxFreq[i] = frequencies[c][i]
    for w in possibleWords:
        score = 1
        for i in range(0, 5):
            c = w[i]
            score *= 1 + (frequencies[c][i] - maxFreq[i]) ** 2
        words.update({w: score})

    return words


def bestWord(possibleWords, frequencies):
    maxScore = 1000000000000000
    bestWord = "words"
    scores = wordScore(possibleWords, frequencies)
    for i in possibleWords:
        if scores[i] < maxScore:
            maxScore = scores[i]
            bestWord = i

    return bestWord

def checkWord(word):
  while(word not in wordlist):
    print("not in word list")
    word = input("Guess:")
  return word
  
def checkLength(guess):
  while(len(guess) != 5):
    print("incorrect length")
    guess = input("Result:")
  return guess

def wordleSolver(possibleWords):
    print("Suggested starting word is:", bestWord(possibleWords, letterFreq(possibleWords)))
    print("Guess and then result. Syntax for result is 'g' for green, 'y' for yellow and 'w' for wrong")
    guess = input("Guess:")
    guess = checkWord(guess)
    result = input("Result:")
    result = checkLength(result)
    counter = 1
    while result != "ggggg" and counter < 6:
        possibleWords = removeWord(result, guess, possibleWords)
        if len(possibleWords) == 0:
            break
        suggestion = bestWord(possibleWords, letterFreq(possibleWords))
        print("The suggested word is:", suggestion)
        guess = input("Guess:")
        guess = checkWord(guess)
        result = input("Enter your new result:")
        result = checkLength(result)
        counter += 1
    if len(possibleWords) == 0:
        print("Run again")
    elif counter == 6 and result != "ggggg":
        print("Fail")
    else:
        print(counter, "guesses.")


wordleSolver(wordlist)
