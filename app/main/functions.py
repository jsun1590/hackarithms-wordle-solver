import itertools
# Global Variables

wordlist = []
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
counter = 1
with open("wordlist.txt", "r", encoding="utf8") as file:
    wordlist = ((file.read()).strip()).split()
possible_words = wordlist

def combine_letters(words_list):
    word = ""
    for _, values in words_list.items():
        word += values[0]
    return word.lower()

def combine_results(words_list):
    result = ""
    for _, values in words_list.items():
        result += values[1]
    return result


def check_word(word):
    return word in wordlist


# Finds grey letters in the guess
def grey_letters(result, guess):
    return [guess[i] for i in range(5) if result[i] == "2"]


# Finds yellow letters in the guess
def yellow_letters(result, guess):
    return [[guess[i], i] for i in range(5) if result[i] == "1"]


# Finds green letters in the guess
def green_letters(result, guess):
    return [[guess[i], i] for i in range(5) if result[i] == "0"]


def remove_word(result, guess, possible_words):
    grey_array = grey_letters(result, guess)
    yellow_array = yellow_letters(result, guess)
    green_array = green_letters(result, guess)
    good_letters = [g[0] for g in green_array]

    good_letters.extend(y[0] for y in yellow_array)
    acceptable_words1 = []
    for w in possible_words:
        check = next(
            (1 for b in grey_array if b in w and b not in good_letters), 0
        )

        if check == 0:
            acceptable_words1.append(w)

    acceptable_words2 = []
    for w in acceptable_words1:
        check = next((1 for g in green_array if w[g[1]] != g[0]), 0)
        if check == 0:
            acceptable_words2.append(w)

    acceptable_words3 = []
    for w in acceptable_words2:
        check = next((1 for p in yellow_array if w[p[1]] == p[0]), 0)
        if check == 0:
            acceptable_words3.append(w)

    acceptable_words4 = []
    for w in acceptable_words3:
        check = next((1 for g in good_letters if g not in w), 0)
        if check == 0:
            acceptable_words4.append(w)

    acceptable_words5 = []
    for w in acceptable_words4:
        check = next(
            (
                1
                for b in grey_array
                if b in green_array and w.count(b) != green_array.count(b)
            ),
            0,
        )

        if check == 0:
            acceptable_words5.append(w)

    return acceptable_words5


# Finds frequencies of letters in each position
def letter_freq(possible_words):
    arr = {}
    for c in ALPHABET:
        freq = [0, 0, 0, 0, 0]
        for i, w in itertools.product(range(5), possible_words):
            if w[i] == c:
                freq[i] += 1
        arr[c] = freq

    return arr


# Gives score based on frequency of letters


def word_score(possible_words, frequencies):
    words = {}
    max_freq = [0, 0, 0, 0, 0]
    for c, i in itertools.product(frequencies, range(5)):
        if max_freq[i] < frequencies[c][i]:
            max_freq[i] = frequencies[c][i]
    for w in possible_words:
        score = 1
        for i in range(5):
            c = w[i]
            score *= 1 + (frequencies[c][i] - max_freq[i]) ** 2
        words[w] = score

    return words


def best_word(possible_words, frequencies):
    max_score = 1000000000000000
    best_word_string = "words"
    scores = word_score(possible_words, frequencies)
    for i in possible_words:
        if scores[i] < max_score:
            max_score = scores[i]
            best_word_string = i

    return best_word_string

def wordle_solver(guess, result):
    #print(word_list)
    if result == "00000":
        return True
    global possible_words
    possible_words = remove_word(result, guess, possible_words)
    if len(possible_words) == 0:
        return False
    #print(possible_words)
    suggestion = best_word(possible_words, letter_freq(possible_words))
    #print("SUGGESTION:", suggestion)

    return possible_words