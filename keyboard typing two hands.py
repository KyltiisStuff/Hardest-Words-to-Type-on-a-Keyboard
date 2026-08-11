# if you are going to import another word list, ensure that it only contains letters (no numbers or special symbols), and that the words are all lowercase, or it will not work
import math
with open("scrabble.txt") as f:
    all_words = [line.strip() for line in f]
length = 0 # edit this to be the length of words you want it to check; ensure that it isn’t set to 1, because you will get a division-by-zero error
words = []
for word in all_words:
    if len(word) == length:
        words.append(word)
distance = 0
letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
xs = [0.5, 2.5, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5, 16.5, 18.5, 1, 3, 5, 7, 9, 11, 13, 15, 17, 2, 4, 6, 8, 10, 12, 14]
ys = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0]
lefthand = [0, 0]
righthand = [0, 0]
ranked_pairs = []
for word in words:
    distance = 0
    lefthand = [0, 0]
    righthand = [0, 0]
    for letter in range(len(word)):
        if word[letter] in "qwertasdfgzxcv":
            if lefthand[0] != 0:
                distance += math.dist((xs[letters.index(word[letter])], ys[letters.index(word[letter])]), (lefthand[0], lefthand[1]))
            lefthand[0] = xs[letters.index(word[letter])]
            lefthand[1] = ys[letters.index(word[letter])]
        else:
            if righthand[0] != 0:
                distance += math.dist((xs[letters.index(word[letter])], ys[letters.index(word[letter])]), (righthand[0], righthand[1]))
            righthand[0] = xs[letters.index(word[letter])]
            righthand[1] = ys[letters.index(word[letter])]
    score = (distance / (len(word) - 1)) * 100 / math.sqrt(76.25)
    ranked_pairs.append((score, word))
    print("", math.floor((words.index(word)) * 100 / len(words)), "%", end="\r", flush=True) # this line is just so you can see how much progress it’s making
ranked_pairs.sort(reverse=True)
for score, word in ranked_pairs:
    print(word, score, sep = "\t")
