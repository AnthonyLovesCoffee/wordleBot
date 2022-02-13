import random
from getWords import wordleGuessList, wordleAnswerList
import time


def run():
    # get the word list
    words = wordleGuessList()
    downsizedWords = wordleAnswerList()

    # generate a random answer
    answer = random.choice(downsizedWords)

    for guessNumber in range(5):
        # guess five times in this loop but have sixth guess at the end
        # goal is to minimize the longest possible word list after guess & evaluation
        # start this metric at a million (we have under 100k words)
        minimiseWordcount = 1e6
        chosenWord = ""
        evalToWordsMap = {}

        if guessNumber != 0:
            possbleWords = words
        else:
            # first guess doesn't change, according to the below polygon aritcle, adieu is one of the best first guesses
            # best words: https://www.polygon.com/gaming/22884031/wordle-game-tips-best-first-guess-5-letter-words
            possbleWords = ["adieu"]

        # check every word in possbleWords to see which one gives us most information
        # (allows us to cancel out the most words)
        for guessWord in possbleWords:
            tempEvalToWordsMap = {}

            # evaluate with every possible answer
            for possibleAns in downsizedWords:
                evaluation = evaluate(possibleAns, guessWord)

                # store word by evaluation tuple in a list
                if tuple(evaluation) not in tempEvalToWordsMap:
                    tempEvalToWordsMap[tuple(evaluation)] = [possibleAns]
                else:
                    tempEvalToWordsMap[tuple(evaluation)].append(possibleAns)

            # metric we are trying to minimize, it finds the worst case in the downsized list of words
            worstCaseWordCount = max([len(val)
                                     for val in tempEvalToWordsMap.values()])

            # if we found a new minimum
            if worstCaseWordCount < minimiseWordcount:
                minimiseWordcount = worstCaseWordCount
                chosenWord = guessWord

                # save current best wordlist map
                evalToWordsMap = tempEvalToWordsMap

        # evaluate chosen word with answer
        downsizedWords = evalToWordsMap[evaluate(answer, chosenWord)]

        # once narrowed down to 1, we are done
        if len(downsizedWords) == 1:
            return True
    return False


def evaluate(answer, word):
    # 0 = nothing, 1 = yellow, 2 = green
    output = [0, 0, 0, 0, 0]

    # check for correct letter and placement
    for i in range(5):
        if word[i] == answer[i]:
            output[i] = 2
            answer = answer[:i] + ' ' + answer[i + 1:]

    # check for correct letter
    for i in range(5):
        char = word[i]
        if char in answer and output[i] == 0:
            output[i] = 1
            first_occurence = answer.find(char)
            answer = answer[:first_occurence] + \
                ' ' + answer[first_occurence + 1:]
    return tuple(output)


## these last two functions are only for testing ##

# returns success probability given n trials
def stats(n):
    successes = 0
    for i in range(n):
        print(i)
        successes += run()
    return successes / n

# returns worst case time elapsed


def runtime(n):
    t = 0
    for _ in range(n):
        start_time = time.time()
        run()
        t = max(t, time.time() - start_time)
    return t


if __name__ == '__main__':
    print(runtime(10))
    print(stats(100))
