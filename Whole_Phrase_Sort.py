from nltk.corpus import words
from statistics import mode
import sqlite3
import random

import inflect

choice = ()
letter_guessing = False


def guessing_over(tweet, alpl, word_list):

    global choice

    for word in tweet.split():
        if word[0] == '_':
            if '#' in alpl:
                choice = '#'
                return choice
            elif '@' in alpl:
                choice = '@'
                return choice
            else:
                pass

            #### POssible might give this the authority to guess a @ or #


    remaining_letter_list = []
    for word in word_list:
        for l in word:
            if l in alpl:
                remaining_letter_list.append(l)

    # print(remaining_letter_list)

    if remaining_letter_list == []:
        choice = random.choice(alpl)
        # print('1',choice)
        return choice
    else:
        # print(alpl)
        choice = max(set(remaining_letter_list), key=remaining_letter_list.count)
        # print('Remaining in ALPL')
        # print(choice)
        return choice



def word_sort(tweet_words, tweet, alpl, word_processing_order):

    global choice

    # print(word_processing_order)

    conn = sqlite3.connect('HangmanSolverdb.db')
    c = conn.cursor()

    word_list = []
    c.execute('SELECT * FROM Word_Dict')
    for row in c.fetchall():
        # if l == row[1]:
        word = str(row[0])
        word_list.append(word)
    c.execute('SELECT * FROM Plural_Word_dict')
    for row in c.fetchall():
        # if l == row[1]:
        word = str(row[0])
        word_list.append(word)
    c.execute('SELECT * FROM New_Word_dict2')
    for row in c.fetchall():
        # if l == row[1]:
        word = str(row[0])
        word_list.append(word)


    #removes any duplicates
    word_list = list(set(word_list))
    # print('word list before emphasis',len(word_list))

    c.execute('SELECT * FROM Emphasis_List2')
    for row in c.fetchall():
        word = str(row[0])
        word_list.append(word)
    c.close()
    conn.close()
    # print('Word list after emphasis', len(word_list))


    # print('type', type(tweet))
    # print('a', len(word_processing_order))
    # print(word_processing_order)
    if len(word_processing_order) == 0:
        guessing_over(tweet, alpl, word_list)
        return choice

    # print('Word List Length',len(word_list))
    #Why was it so much faster to append to new list than remove from a current?
    new_list = []
    for i in word_list:
        if len(i) in word_processing_order:
            new_list.append(i)
    # print('new list',len(new_list))
    word_list = new_list
    # print(tweet_words)
    High_prob_letters = {}

    # print('word list length after length sorting', len(word_list))

    # print('6')
    # print('b',type(tweet))
    # # tweet_words = tweet.split()
    # print('type2', type(tweet))
    # print('Tweet Words', tweet_words)


    for l in tweet_words:
        p = list(l)


    # print('c',p)
    # print('d',tweet_words)

    # u = [list(word) for word in word_list]

    # w = [list(word) for word in word_list]
    # print(word_list)
    # u = map(list, word_list)

    possible_words = []

    word_list_remove = []
    # print(tweet_words)
    High_prob_letters = {}
    for l in tweet_words:
        possible_words = []
        let_list = []
        for char in l:
            let_list.append(char)
        for i in word_list:
            if len(l) == len(i):
                u = list(i)
                for n, t in enumerate(u):
                    if t not in let_list:
                        u[n] = '_'
                if u == let_list:
                    possible_words.append(i)
                else:
                    pass
        # print('tweet word',l)
        # print(possible_words)
        if l != ''.join(possible_words):
            letter_list = []
            if len(possible_words) > 0:
                for word in possible_words:
                    for char in word:
                        if char in alpl:
                            letter_list.append(char)
                # print('length of letter list',len(letter_list))
                if len(letter_list) > 0:
                    most_common_letter = max(set(letter_list), key=letter_list.count)
                    # print('Most common letter',most_common_letter)
                    usage =letter_list.count(most_common_letter)
                    usage = (usage / len(letter_list))
                    # print('usage',usage)
                    if most_common_letter in High_prob_letters:
                        if usage > High_prob_letters[most_common_letter]:
                            High_prob_letters.update({most_common_letter : usage})
                    if most_common_letter not in High_prob_letters:
                        High_prob_letters.update({most_common_letter: usage})

                else:
                    pass
        else:
            pass


            # print('High in ', High_prob_letters)

    print(High_prob_letters)

    # print('type5', type(tweet))

    #returns the choice that has the highest individual probability for each word length evaluated
    import operator
    # print('1', bool(High_prob_letters))
    if not bool(High_prob_letters):
        # print('in boolean')
        guessing_over(tweet, alpl, word_list)
    if bool(High_prob_letters):
        choice = max(High_prob_letters, key=High_prob_letters.get)
    return choice










