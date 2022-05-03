def solution(N):
    number_list = list(str(N))
    list_index = 0
    while int(number_list[list_index]) > 5:
        pass
    else:
        number_list.insert(number_list[list_index], "5")
    # for i in number_list:
    #     if 5 > int(i):
    #         number_list.insert(number_list.index(i), "5")
    print(number_list)


solution(268)


# print(5406)