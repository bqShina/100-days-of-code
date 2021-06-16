from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")

auction_bid = {}
auction_going = True
while auction_going:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction_bid[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == "no":
        auction_going = False
    elif other_bidders == "yes":
        clear()
winner_bid = 0
winner = ""
for winner_name in auction_bid:
    if auction_bid[winner_name] > winner_bid:
        winner_bid = auction_bid[winner_name]
        winner = winner_name
# print(auction_bid)
print(f"The winner is {winner} with a bid of ${winner_bid}")
