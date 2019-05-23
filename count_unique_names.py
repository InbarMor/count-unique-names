from stringdist import levenshtein

def indexes_of(list, item):
    """
    Get:
    list, item in the list.

    Returns:
    list of the indexes of the item in the list.
    if the item doesn't exist in the list the function will return empty list.
    """

    indexes = []
    for i in xrange(len(list)):
        if list[i].lower() == item:
            indexes.append(i)
    return indexes

def is_nickname(name0, name1, names, nicknames):
    """
    Get:
    name0 - string of name,
    name1 - string of name,
    names - list of names,
    nicknames - list of nicknames.

    *item in the nicknames list in some index is the nickname of the item exist in the names list in the same index.

    Returns:
    True if name0 is a nickname of name1 and vice versa or in case the names are equal,
    otherwise the function will return False.
    """

    indexes0 = indexes_of(nicknames, name0)
    indexes1 = indexes_of(nicknames, name1)

    name0_nickname_of_name1 = False
    name1_nickname_of_name0 = False

    for index in indexes0:
        if names[index].lower() == name1:
            name0_nickname_of_name1 = True
            break

    if not name0_nickname_of_name1:
        for index in indexes1:
            if names[index].lower() == name0:
                name0_nickname_of_name1 = True
                break

    if name0 == name1:
        return True
    elif name0_nickname_of_name1:
        return True
    elif name1_nickname_of_name0:
        return True
    return False

def is_typo(name0, name1):
    """
    Get:
    name0 - string of name,
    name1 - string of name.

    Returns:
    True if the Levenshtein-distance between the names is <= 1,
    otherwise the function will return False.
    """

    return levenshtein(name0, name1) <= 1

def is_same_name(name0, name1, names, nicknames):
    """
    Get:
    name0 - "first_name (optional middle name) last_name",
    name1 - "first_name (optional middle name) last_name".

    Returns:
    True if the names are the same and False otherwise.
    """

    #get first and last name of each full name.
    name0 = name0.split()
    first_name0, last_name0 = name0[0], name0[-1]
    name1 = name1.split()
    first_name1, last_name1 = name1[0], name1[-1]

    #compare names
    if is_typo(first_name0, first_name1) or is_nickname(first_name0, first_name1, names, nicknames):
        if is_typo(last_name0, last_name1):
            return True
    return False

def read_csv(csv_file):
    """
    Get:
    csv_file - path to csv file.

    Returns:
    names - list of names,
    nicknames - list of nicknames.

    *item in the nicknames list in some index is the nickname of the item exist in the names list in the same index.
    """

    with open(csv_file) as nicknames_file:
        names = []
        nicknames = []
        for line in nicknames_file:
            _, name, nickname = line.split(", ")
            names.append(name)
            nicknames.append(nickname[:-1])
    return names, nicknames


def count_unique_names(bill_first_name, bill_last_name, ship_first_name, ship_last_name, bill_name_on_card):
    """
    Get:
    bill_first_name - the first name in the billing address form (could include middle names),
    bill_last_name - the last name in the billing address form,
    ship_first_name - the first name in the shipping address form (could include middle names),
    ship_last_name - the last name in the shipping address form,
    bill_name_on_card - the full name as it appears on the credit card.

    Returns:
    number of unique names in the transaction.
    """

    #read nicknames csv file
    names, nicknames = read_csv("nicknames.csv")

    #build names
    build_name = lambda first_name, last_name: first_name + " " + last_name

    bill_name = build_name(bill_first_name, bill_last_name).lower()
    ship_name = build_name(ship_first_name, ship_last_name).lower()

    first, second = bill_name_on_card.split()
    bill_name_on_card1 = build_name(second, first).lower()
    bill_name_on_card = bill_name_on_card.lower()

    #compare names
    if is_same_name(bill_name, ship_name, names, nicknames):
        if is_same_name(bill_name, bill_name_on_card, names, nicknames) or \
                is_same_name(bill_name, bill_name_on_card1, names, nicknames):
            return 1
        else:
            return 2
    elif is_same_name(ship_name, bill_name_on_card, names, nicknames) or \
            is_same_name(ship_name, bill_name_on_card1, names, nicknames):
        return 2
    elif is_same_name(bill_name, bill_name_on_card, names, nicknames) or \
            is_same_name(bill_name, bill_name_on_card1, names, nicknames):
        return 2
    return 3