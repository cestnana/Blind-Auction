# main

# Get User Input: Name

# Get User Input: Bid Price

# Ask if there is another bid to add

# If yes: 
# 1. Clear the screen
# 2. Go back to the User Input part

# If no: 
# 1. compare the bids
# 2. show the {winner} with {price}

def find_highest_bid():
  biggest_price = 0
  for each_price in auction_bids["price"]:
    if int(each_price) > biggest_price:
      biggest_price = each_price
    else:
      break

auction_bids = {}
is_other_bidders = "yes"

while is_other_bidders == "yes": 
  auction_bids["name"] = input("What is your name? :")
  auction_bids["price"] = (input("What is your bid? $"))
  is_other_bidders = input("Are there any other bidders? (yes/no)")
  if is_other_bidders == "yes":
    print("\n" * 20)
  else:
    find_highest_bid()
    
print(f"The winner is {auction_bids["name"]} with a bid of ${auction_bids["price"]}.")
