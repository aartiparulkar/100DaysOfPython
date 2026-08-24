logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids = {}

continue_bid = True
while continue_bid:
    name = input("What is your name? ")
    bid = int(input("How much will you bid? Rs. "))
    bids[name] = bid
    
    more_bid = input("Are there more people who bid? Enter 'yes' or 'no'. ")
    if more_bid == 'no':
        continue_bid = False
        break

    print("\n" * 20)

max_bid = -1
winner = ""
for user_bid in bids:
    if bids[user_bid] > max_bid:
        max_bid = bids[user_bid]
        winner = user_bid

print(f"Product going for Rs. {max_bid}.  1...2...3 and sold to {winner}!")
