
bid_list = {}

def find_highest_bidder(list_of_bid):
    winner = ""
    highest_bid = 0
    for bidder in list_of_bid:
      bid = list_of_bid[bidder]
      if bid > highest_bid:
          highest_bid = bid
          winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

continue_bid = "yes"
while continue_bid == "yes":
    bidder_name = input("What is the bidder name?: ")
    bid_amount = int(input("What is your bid amount?: $"))
    bid_list[bidder_name] = bid_amount
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if continue_bid == "no":
        find_highest_bidder(bid_list)
