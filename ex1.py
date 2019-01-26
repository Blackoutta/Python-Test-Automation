def who_do_you_know():
    users_known = input("tell me some people you know: ")
    people_without_spaces = [person.strip().title() for person in users_known.split(",")]
    return people_without_spaces


def ask_user():
    a_name = input("tell me a name: ")
    if a_name in who_do_you_know():
        print("You know {}!".format(a_name))
    else:
        print("You don't know {}!".format(a_name))


while True:
    ask_user()
