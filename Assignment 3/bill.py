import csv
from random import choices


global price_of_each_item
price_of_each_item = []


def calculate_bill(menu_card, ordered_items):
    
    """caluclating bill by using details
    from the menu_card .Also storing the price
    of each qnatity in price_of_each_item with
    item_id as key"""

    total_amount = 0.0
    for items in ordered_items.items():

        price = 0.0
        item_id = items[0].split()[0]
        amount = items[0].split()[1]
        quantity = items[1]

        if amount == "half":
            price = menu_card[item_id][0]
        elif amount == "full":
            price = menu_card[item_id][1]

        amount = amount[0].upper() + amount[1:]
        price = price * quantity
        price_of_each_item.append([item_id, amount, quantity, price])
        total_amount = total_amount + price

    return total_amount


def calculate_percent(bill, tip_percentage):
    tip_percentage = int(tip_percentage[:-1])
    final_bill = bill + (tip_percentage * bill) / 100
    return final_bill


def game(total_bill):

    # print("You will have these possibilities")
    # print("5% chance to get a 50% discount off the total bill")
    # print("10% chance to get a 25% discount off the total bill")
    # print("15% chance to get a 10% discount off the total bill")
    # print("5% chance to get a 50% discount off the total bill")
    # print("20% chance to get no discount")
    # print("50% chance that the total amount increases by 20%")

    discount = [1, 2, 3, 4, 5, 6]
    probabilities = [0.05, 0.1, 0.15, 0.05, 0.2, 0.5]
    choice = choices(discount, probabilities)
    possibilities = {1: -50, 2: -25, 3: -10, 4: -50, 5: 0, 6: 20}
    percentage = possibilities[choice[0]]
    discount_value = (percentage * total_bill) / 100
    return discount_value


def print_pattern_happy():
    print(" ****            ****")
    print("|    |          |    |")
    print("|    |          |    |")
    print("|    |          |    |")
    print(" ****            ****")
    print()
    print("          {}")
    print("    ______________")


def print_pattern_sad():
    print(" ****")
    print("*    *")
    print("*    *")
    print("*    *")
    print("*    *")
    print(" ****")


menu_card = {}  # to store menu items
# reading the CSV file
with open("Menu.csv", mode="r") as file:
    csvFile = csv.reader(file)

    """coverting string to integer format and 
    creating the dictionary with key as item_id 
    and values as price of half and full items"""

    for lines in csvFile:
        if lines[0] == "Item no":
            continue
        else:
            lines[1] = float(lines[1])
            lines[2] = float(lines[2])
        menu_card[lines[0]] = [lines[1], lines[2]]

# Displaying menu items
print("{0: <15}".format("Item no"), end="")
print("{0: <15}".format("Half Plate"), end="")
print("{0: <15}".format("Full Plate"))
for item in menu_card.keys():
    print("{0: <15}".format(item), end="")
    print("{0: <15.2f}".format(menu_card[item][0]), end="")
    print("{0: <15.2f}".format(menu_card[item][1]), end="")
    print()

print("Enter number of items you want to order: ", end="")
no_of_items = int(input())
ordered_items = {}
print("Please enter items you want to order in the below format")
print("item_id    [half/full]   quantity")


# taking input from user
for i in range(no_of_items):

    item_details = input().split()
    item_details[1] = item_details[1].lower()
    item_details[2] = int(item_details[2])

    key = []
    key = item_details[0] + " " + item_details[1]
    if key in ordered_items.keys():
        ordered_items[key] = ordered_items[key] + item_details[2]
    else:
        ordered_items[key] = item_details[2]

print("Tips percentage you can give are: 0% 10% 20%")
print("Please specify your tip percentage:")
tip_percentage = input()


bill = calculate_bill(menu_card, ordered_items)
total_bill = calculate_percent(bill, tip_percentage)
print("Total bill:", "{0:.2f}".format(total_bill))

print("How many people want to split the bill: ")
no_of_people = int(input())
share = total_bill / no_of_people
print("Share of each person:", "{0:.2f}".format(share))

print("Do you want to play TEST YOU LUCK GAME (yes/no)")
decision = input()
flag_discount = False
result = 0.0
if decision.lower() == "yes":
    result = game(total_bill)
    if result < 0:
        print("Discount:", "{0:.2f}".format(result))
        print_pattern_happy()
        flag_discount = True
    else:
        print("Increase:", "{0:.2f}".format(result))
        print_pattern_sad()

print("BREAKDOWN OF BILL")
for item in price_of_each_item:
    print("Item ", item[0], end=" ")
    print("[" + item[1] + "]", end=" ")
    print("[" + str(item[2]) + "]:", end=" ")
    print("{0:.2f}".format(item[3]))

print("Total:", "{0:.2f}".format(bill))
print("Tip percentage:", tip_percentage)


final_bill = abs(result + total_bill)
if flag_discount:
    print("Discount:", "{0:.2f}".format(result))
else:
    print("Increase:", "{0:.2f}".format(result))

print("Final Bill:", "{0:.2f}".format(final_bill))
share = final_bill / no_of_people
print("Updated share of each person:", "{0:.2f}".format(share))
