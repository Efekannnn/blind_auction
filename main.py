from art import logo
biggest_bid = 0
biggest_offer_name = ""


def auction():
    print(logo)
    dic = {}
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    dic[name] = price
    over = input("Is there someone to make a offer? \n"
                 "for yes press y\n"
                 "for no press n")
    if over == "y":
        auction()

    return dic


def highest_bidder():
    global biggest_bid, biggest_offer_name
    for name, bid in auction_dic.items():
        if bid > biggest_bid:
            biggest_bid = bid
            biggest_offer_name = name

    print("The highest bid is $", biggest_bid, "by", biggest_offer_name)


auction_dic = auction()
highest_bidder()
