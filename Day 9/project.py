from replit import clear
from art import logo

print(logo)

bids = {}
bidding_finished = False

def high_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]  # Fix the indexing of the bidding_record dictionary
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and the Highest bidder is {highest_bid} $")

while not bidding_finished:
    name = input("What is your name? ")
    bid = int(input("What is your bid $"))
    bids[name] = bid
    should_continue = input("Are there other bidders? Type 'yes' or 'no'\n ")
    if should_continue.lower() == 'no':  # Use lower() to handle various input cases
        bidding_finished = True
        high_highest_bidder(bids)  # Pass the bids dictionary to the function
    elif should_continue.lower() == 'yes':  # Use lower() to handle various input cases
        clear()
