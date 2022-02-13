# extracting words from their respective .txt files and adding them to an array

def wordleGuessList():
    words = []
    with open("wordleGuess.txt", "r") as f:
        for line in f:
            words.append(line.strip())
    return words


def wordleAnswerList():
    words = []
    with open("wordleAnswers.txt", "r") as f:
        for line in f:
            words.append(line.strip())
    return words


def wordmasterGuessList():
    words = []
    with open("wordmasterGuess.txt", "r") as f:
        for line in f:
            words.append(line.strip())
    return words


def wordmasterAnswersList():
    words = []
    with open("wordmasterAnswers.txt", "r") as f:
        for line in f:
            words.append(line.strip())
    return words
