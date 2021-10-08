from flask import Flask, render_template
import sqlite3
import random

# Initializing flask
app = Flask(__name__)

# This function helps convert list of tuple output of sql query into list of dictionaries output
# Taken from https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
# Setting up SQLITE connection
connection = sqlite3.connect("picker.db")
connection.row_factory = dict_factory
db = connection.cursor()

@app.route("/")
def hello_world():
    return render_template('index.html')


def main():
    # food is a list of dictionaries, that I would rather host in a db somewhere, but this will work for now
    # name is the main entry, and style/price are tag groupings
    #wheel = [{'name': "The Works", 'style': "American", 'price': "$"},
             #{'name': "Kentucky Bourbon", 'style': "American", 'price': "$"},
             #{'name': "Taste of Seoul", 'style': "Asian", 'price': "$"},
             #{'name': "Burrito Boyz", 'style': "Mexican", 'price': "$$$"}]
    wheel = db.execute("SELECT * FROM restaurants")
    wheel = wheel.fetchall()
    number = 2
    exclude_params = [{'style': "Asian"}, {'price': "$$$"}]
    nodupe_params = [{'style': "American"}]
    # Note that filters will apply in this order: exlude -> nodupe and may throw a warning if there's not enough options to satisfy both
    filtered = exclude(wheel, exclude_params)
    filtered = nodupe(filtered, nodupe_params)
    choices = spinner(filtered, number)
    for i in range(len(choices)):
        print(choices[i])


def spinner(items, number):  # items is list of dictionaries, number is integer
    # Given a list of valid selections dictionaries, randomly select one of them, return list of names selected
    # todo investigate if random.sample() would work better
    choices = []
    while len(choices) < number:
        tmp = random.choice(range(len(items)))
        if items[tmp]['name'] not in choices:
            choices.append(items[tmp]['name'])
        # Make sure no infinite loop
        if len(choices) == len(items):
            break

    return choices


def exclude(wheel, exclude):  # wheel is a list of dictionaries, exclude, is list of key-value pair dictionaries
    # Given a list of dictionaries, and a list of excluded key: value pairs, trim the list to items without
    filtered = []
    check = 0
    for i in range(len(wheel)):
        for j in range(len(exclude)):
            [[key, value]] = exclude[j].items()
            if (key, value) in wheel[i].items():
                check = 1
        if check == 0:
            filtered.append(wheel[i])
        check = 0
    return filtered
    # return items


def nodupe(wheel, nodupe):
    # todo build this function to prevent duplicate tags if possible
    return wheel



if __name__ == main():
    main()