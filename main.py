import random


def main():
    # food is a list of dictionaries, that I would rather host in a db somewhere, but this will work for now
    # name is the main entry, and style/price are tag groupings
    wheel = [{'name': "The Works", 'style': "American", 'price': "$"},
             {'name': "Kentucky Bourbon", 'style': "American", 'price': "$"},
             {'name': "Taste of Seoul", 'style': "Asian", 'price': "$"},
             {'name': "Burrito Boyz", 'style': "Mexican", 'price': "$$$"}]
    number = 2
    exclude = [{'style': "Asian"}, {'price': "$$$"}]
    nodupe = [{'style': "American"}]
    filtered = filter(wheel, exclude, nodupe)
    choices = spinner(filtered, number)
    for i in range(len(choices)):
        print(choices[i])


def spinner(items, number): # items is list of dictionaries, number is integer
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


def filter(wheel, exclude, nodupe): # wheel is a list of dictionaries, exclude, is list of key-value pair dictionaries
    # Given a list of dictionaries, and a list of excluded key: value pairs, trim the list to items without
    # todo implement no duplicate functionality
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


if __name__ == main():
    main()
