# Global Variables


alphabet = "abcdefghijklmnopqrstuvwxyz"
file = open("wordlist.txt", "r")
wordlist = ((file.read()).strip()).split()


def check_word(word):
    return word in wordlist
