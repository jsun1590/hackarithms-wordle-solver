# Global Variables

wordlist = []
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
with open("wordlist.txt", "r", encoding="utf8") as file:
    wordlist = ((file.read()).strip()).split()


def check_word(word):
    return word in wordlist
