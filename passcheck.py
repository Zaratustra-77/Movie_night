import re

max_val = 16
min_val = 8

def char_count(password):

    ranking = {'count_upper': 0, 'count_lower': 0, 'count_num': 0, 'count_special': 0}
    for i in password:
        # print(ranking)
        if i.islower():
            ranking.update({'count_lower' : int(1)})
        if i.isupper():
            ranking.update({'count_upper': int(1)})
        if i.isdigit():
            ranking.update({'count_num': int(1)})
        if not (i.isalnum()):
            ranking.update({'count_special': int(1)})

    new_score = sum(ranking.values())
    return new_score


def tooshort(password):
    return len(password) < min_val


def toolong(password):
    return len(password) > max_val


def password_input():
    user_password = input(f"""
    Please input a password.
    it should be at least {min_val} characters long and less than {max_val}.
    A strong password contains 4 different character types.
    A weak password contains between 1 and 3 different character types.
    You will be indicated if the password is weak or strong before completing your choice.
    Please input your selected password: """)
    return user_password


def create_password():
    flag = True
    while flag:
        user_password = password_input()
        if tooshort(user_password):
            print(f"you only entered {len(user_password)} characters, please input a password longer than {min_val} ")
        elif toolong(user_password):
            print(f"you entered {len(user_password)} characters, please input a password shorter than {max_val} ")
        elif char_count(user_password) >1 and char_count(user_password) < 4:
                create = input("You entered a weak password, do you wish to create password or quit?y to create, n to choose nother password or q to quit?:  ").casefold()
                if create == 'y':
                    print(f"New Password **{user_password[2]}{'*' * (len(user_password) -3)} was created")
                    flag = False
                elif create == 'q':
                    flag = False
        elif char_count(user_password) == 4:
                create = input("You entered a strong password, do you wish to create password quit?y to create, n to choose nother password or q to quit?:  ").casefold()
                if create == 'y':
                    print(f"New Password **{user_password[2]}{'*' * (len(user_password) -3)} was created")
                    flag = False
                elif create == 'q':
                    flag = False

        else:
            print("You have entered only one char type please try again")


create_password()
