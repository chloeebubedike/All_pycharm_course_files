import random


def decide_lottery_number():
    lottery_number = []
    for num in range(7):
        lottery_number.append(random.randint(0, 9))
    return lottery_number


def calculate_lottery_number_matches(lottery_ticket, lottery_number):
    count = 0
    for i in lottery_ticket:
        if int(i) in lottery_number:
            count += 1
        else:
            count += 0
    return count


def calculate_lottery_prize(match_count):
    if match_count >= 7:
        print('You have won £1000000')
    elif match_count >= 6:
        print('You have won £1000')
    elif match_count >= 5:
        print('You have won £100')
    elif match_count >= 4:
        print('You have won £40')
    elif match_count >= 3:
        print('You have won £20')
    else:
        print('You have won nothing')


user_lottery_ticket = list(input('What is the 7 digit number on your lottery ticket?'))

count_of_matches = calculate_lottery_number_matches(user_lottery_ticket, decide_lottery_number())

calculate_lottery_prize(count_of_matches)

