from sys import exit
from nltk.corpus import words
import inflect
from datetime import datetime

import sqlite3


from flask import Flask
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hangman_dict.db'
# db = SQLAlchemy(app)



conn = sqlite3.connect('HangmanSolverdb.db')
c = conn.cursor()


def create_table_order():
    # c.execute('CREATE TABLE IF NOT EXISTS orders(game_win INTEGER, game_lose INTEGER, counter INTEGER, order VARCHAR)')
    c.execute('CREATE TABLE IF NOT EXISTS orders(game_win INTEGER, game_lose INTEGER, counter INTEGER, choice_order VARCHAR)')


def create_table_Word_Dict():
    c.execute('CREATE TABLE IF NOT EXISTS Word_dict(Word String, Word_length INTEGER)')

def create_table_Plural_Word_Dict():
    c.execute('CREATE TABLE IF NOT EXISTS Plural_Word_dict(Word String, Word_length INTEGER)')


def create_table_New_Word_Dict():
    c.execute('CREATE TABLE IF NOT EXISTS New_Word_dict2(Word String, Word_length INTEGER, Date_added NUMERIC, Date_last_used DATE, Usage INTEGER)')


def create_table_Tests():
    c.execute('CREATE TABLE IF NOT EXISTS Tests2(Games_Won Integer, Games_Lost INTEGER,  Description STRING)')

def create_table_Games_lost():
    c.execute('CREATE TABLE IF NOT EXISTS Games_Lost2(Tweet_Original String, Tweet_Guessed String, Letters_Remaining String, Test_Description String)')


def create_table_Emphasis_List():
    c.execute('CREATE TABLE IF NOT EXISTS Emphasis_List2(word String)')



# create_table_order()
# create_table_Word_Dict()
create_table_New_Word_Dict()
create_table_Games_lost()
# create_table_Plural_Word_Dict()
create_table_Emphasis_List()
create_table_Tests()
# c.close()
# conn.close()

tweets_list = []
number = (0)

description = 'First run through. No New words learned'


#

def learn_from_tweet():


    new_words = []
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

    c.close()
    conn.close()

    for word in tweet_learning.split():
        if word not in word_list:
            new_words.append(word)
    print(new_words)

    conn = sqlite3.connect('HangmanSolverdb.db')
    c = conn.cursor()
    new_words_db = []
    c.execute('SELECT * FROM New_Word_Dict2')
    for row in c.fetchall():
        n_word = (row[0])
        new_words_db.append(n_word)


    for word in new_words:
        time = (datetime.now())
        word = word.lower()
        c.execute('INSERT INTO New_Word_Dict2(Word, Word_length, Date_added) VALUES(?,?,?)',(word,len(word), time))
        conn.commit()
    c.close()
    conn.close()

def read_from_db():
    global tweets_list
    global number
    c.execute("SELECT * FROM Tweets")
    counter = 0
    for row in c.fetchall():
        if counter == 300:
            break
        else:
            counter += 1
            tweets = (row[1])
            tweets_list.append(tweets)



read_from_db()
c.close()
conn.close()


Most_success = [0,0,0]
counter = (0)
game_engine = True


while game_engine == True:

    # global word_list

    # conn = sqlite3.connect('HangmanSolverdb.db')
    # c = conn.cursor()
    #
    # word_list = []
    # c.execute('SELECT * FROM Word_Dict')
    # for row in c.fetchall():
    #     # if l == row[1]:
    #     word = str(row[0])
    #     word_list.append(word)
    # c.execute('SELECT * FROM Plural_Word_dict')
    # for row in c.fetchall():
    #     # if l == row[1]:
    #     word = str(row[0])
    #     word_list.append(word)
    # c.execute('SELECT * FROM New_Word_dict2')
    # for row in c.fetchall():
    #     # if l == row[1]:
    #     word = str(row[0])
    #     word_list.append(word)
    #
    # #removes any duplicates
    # word_list = list(set(word_list))
    # print('word list before emphasis',len(word_list))

    game_win = (0)
    game_lose = (0)

    counter += 1


    for tweet in tweets_list:


        global game_over


        alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']


        word_guess = []
        turns = ()
        phrase = []
        guessed_not_in = []
        guessed_in = []




        for char in tweet:
            for l in alpl:
                if char == l:
                    word_guess.append('_')
                    phrase.append(l)

                    break

                if char == l.upper():
                    word_guess.append('_')
                    phrase.append(l.upper())
                    break

                if char == ' ':
                    word_guess.append(' ')
                    phrase.append(' ')
                    break



        phrase = ''.join(phrase)
        # print(word_guess)
        # print(phrase)

        tweet_learning = phrase
        tweet_learning = tweet_learning.lower()


        l = len(phrase)

        l = int(l / 10)

        if l >= 10:
            turns = 4
        if l <= 9 and l >= 7:
            turns = 5
        if l <= 6 and l >= 5:
            turns = 6
        if l <= 4 and l >= 3:
            turns = 7
        if l <= 2:
            turns = 8


        choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']


        letter_guessing = False


        turn_counter = 0
        turns_amount = turns
        word_processing_order = []
        # print(word_processing_order)

        t = tweet.split()
        for word in t:
            word_processing_order.append(len(word))

        word_processing_order = list(set(word_processing_order))
        # print(word_processing_order)

        conn = sqlite3.connect('HangmanSolverdb.db')
        c = conn.cursor()

        # print(len(word_list))
        # Emphasis list gets the word_list to place emphasis on words that it already knows but gets the word wrong.
        # c.execute('SELECT * FROM Emphasis_List2')
        # for row in c.fetchall():
        #     word = str(row[0])
        #     word_list.append(word)
        # c.close()
        # conn.close()
        # print('Word list after emphasis',len(word_list))

        let_list = list(set(choices) - set(alpl))
        # print(let_list)



        # Evaluates the current state of the tweet and removes lengths from word_processing_order that have been fully solved
        # tweet_words = tweet.split()
        # print(tweet_words)

        game_over = ()

        while game_over != True:

            # ###### METHOD ######

            tweet = ''.join(word_guess)
            tweet_words = tweet.split()
            # print('Before Guess:   ', tweet)
            # from Dict_wort import *
            # word_sort(letter_guessing, word_list, word_processing_order, tweet, alpl)
            # from Dict_wort import choice
            # print('Into func.')
            from Whole_Phrase_Sort import *
            word_sort(tweet_words, tweet, alpl, word_processing_order)
            from Whole_Phrase_Sort import choice
            # print('Out Func')



            i = choice

            if i == '@' or '#':
                for letter in range(len(phrase)):
                    if i == phrase[letter]:
                        word_guess[letter] = i

            if str.isnumeric(i):
                for letter in range(len(phrase)):
                    if i == phrase[letter]:
                        word_guess[letter] = i
                    elif ' ' == phrase[letter]:
                        word_guess[letter] = ' '

            if str.islower(i):
                for letter in range(len(phrase)):
                    if i == phrase[letter]:
                        word_guess[letter] = i
                    elif ' ' == phrase[letter]:
                        word_guess[letter] = ' '

            i = i.upper()

            if str.isupper(i):
                for letter in range(len(phrase)):
                    if i == phrase[letter]:
                        word_guess[letter] = i
                    elif ' ' == phrase[letter]:
                        word_guess[letter] = ' '


            phrase = phrase.lower()
            i = i.lower()
            if i in phrase:
                alpl.remove(i)

            if i not in phrase:
                alpl.remove(i)
                turns -= 1
                turn_counter += 1

            comp_word = ''.join(word_guess)

            print('Character Guess: ', choice)
            print('Hangman Phrase: ', comp_word)

            if turns == 0:
                game_lose += 1
                # print('false2')
                game_over = True
                conn = sqlite3.connect('HangmanSolverdb.db')
                c = conn.cursor()
                # print(type(phrase))
                # print(type(comp_word))
                # print(type(alpl))
                # print(type(description))

                alpl = ''.join(alpl)

                c.execute("INSERT INTO Games_Lost2(Tweet_Original,Tweet_Guessed, Letters_Remaining, Test_Description) VALUES (?,?,?,?)",
                          (phrase, comp_word, alpl, description))
                conn.commit()
                comp_word = comp_word.split()
                phrase = phrase.split()
                # print(comp_word)
                let_list = []
                for word in comp_word:
                    for char in word:
                        let_list.append(char)

                new_words = []
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

                word_list = list(set(word_list))

                for i in phrase:
                    print(i)
                    u = list(i)
                    for n, t in enumerate(u):
                        if t not in let_list:
                            u[n] = '_'
                        print(u)
                        if "_" in u:
                            print('_ in u')
                            print(i.lower())
                            if i.lower() in word_list:
                                print(i)
                                print(type(i))
                                c.execute('INSERT INTO Emphasis_list2(word) VALUES (?)',(i,))
                                conn.commit()
                                break
                c.close()
                conn.close()
                print('Game Over Win:', game_win)
                print('Games Lost:', game_lose)
                alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']
                learn_from_tweet()
                break


            print('Turns Remaining:', turns)
            phrase = phrase.lower()
            comp_word = comp_word.lower()
            if comp_word == phrase:
                # print(comp_word)
                game_win += 1
                print('Game Over Win:',game_win)
                print('Games Lost:',game_lose)
                game_over = True
                alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']
                learn_from_tweet()
                break

            order = word_processing_order
            remove_list = []
            tweet_words = comp_word.split()
            for l in order:
                o = []
                for word in tweet_words:
                    if len(word) == l:
                        o.append(word)
                o = ''.join(o)
                if "_" not in o:
                    remove_list.append(l)

            word_processing_order = list(set(word_processing_order) - set(remove_list))
            print(word_processing_order)


            # print(comp_word)
            # print('Turns Remaining',turns)

    conn = sqlite3.connect('HangmanSolverdb.db')
    c = conn.cursor()

    ###### get all data from wins colomn, create variable for greatest amount of wins for if loop below#####
    # c.execute("SELECT game_win FROM orders")
    # rows = c.fetchall()
    # for row in rows:
    #     max_wins = max(row)

    c.execute("INSERT INTO Tests2(Games_Won, Games_Lost, Description) VALUES (?,?,?)",(game_win, game_lose,description))
    conn.commit()
    c.close()
    conn.close()
    # print('false1')
    # game_engine = False




