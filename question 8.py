def print_receipt(item_1_name, item_1_price, item_2_name, item_2_price, item_3_name, item_3_price):
    total = item_1_price + item_2_price + item_3_price
    print("{} - £{} \n{} - £{} \n{} - £{} \nTOTAL: £{}".format(item_1_name, item_1_price, item_2_name, item_2_price, item_3_name, item_3_price, total))


print_receipt('Shoes', 5, 'Dress', 10, 'Tshirt', 20)

