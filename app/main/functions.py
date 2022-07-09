# Global Variables

wordlist = []
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
with open("wordlist.txt", "r", encoding="utf8") as file:
    wordlist = ((file.read()).strip()).split()


def combine_letters(words_list):
    word = ""
    for _, values in words_list.items():
        word += values[0]
    return word.lower()


def check_word(word):
    return word in wordlist


# Finds grey letters in the guess
def greyLetters(result, guess):
    return [guess[i] for i in range(5) if result[i] == "w"]


# Finds yellow letters in the guess
def yellowLetters(result, guess):
    return [[guess[i], i] for i in range(5) if result[i] == "y"]


# Finds green letters in the guess
def greenLetters(result, guess):
    return [[guess[i], i] for i in range(5) if result[i] == "g"]


def removeWord(result, guess, possibleWords):
    greyLettersArray = greyLetters(result, guess)
    yellowLettersArray = yellowLetters(result, guess)
    greenLettersArray = greenLetters(result, guess)
    goodLetters = [g[0] for g in greenLettersArray]

    goodLetters.extend(y[0] for y in yellowLettersArray)
    acceptableWords1 = []
    for w in possibleWords:
        check = next(
            (1 for b in greyLettersArray if b in w and b not in goodLetters), 0
        )

        if check == 0:
            acceptableWords1.append(w)

    acceptableWords2 = []
    for w in acceptableWords1:
        check = next((1 for g in greenLettersArray if w[g[1]] != g[0]), 0)
        if check == 0:
            acceptableWords2.append(w)

    acceptableWords3 = []
    for w in acceptableWords2:
        check = next((1 for p in yellowLettersArray if w[p[1]] == p[0]), 0)
        if check == 0:
            acceptableWords3.append(w)

    acceptableWords4 = []
    for w in acceptableWords3:
        check = next((1 for g in goodLetters if g not in w), 0)
        if check == 0:
            acceptableWords4.append(w)

    acceptableWords5 = []
    for w in acceptableWords4:
        check = next(
            (
                1
                for b in greyLettersArray
                if b in greenLettersArray and w.count(b) != greenLettersArray.count(b)
            ),
            0,
        )

        if check == 0:
            acceptableWords5.append(w)

    return acceptableWords5


# Finds frequencies of letters in each position
def letterFreq(possibleWords):
    arr = {}
    for c in alphabet:
        freq = [0, 0, 0, 0, 0]
        for i, w in itertools.product(range(5), possibleWords):
            if w[i] == c:
                freq[i] += 1
        arr[c] = freq

    return arr


# Gives score based on frequency of letters


def wordScore(possibleWords, frequencies):
    words = {}
    maxFreq = [0, 0, 0, 0, 0]
    for c, i in itertools.product(frequencies, range(5)):
        if maxFreq[i] < frequencies[c][i]:
            maxFreq[i] = frequencies[c][i]
    for w in possibleWords:
        score = 1
        for i in range(5):
            c = w[i]
            score *= 1 + (frequencies[c][i] - maxFreq[i]) ** 2
        words[w] = score

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
