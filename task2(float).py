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

auction_bids = {}
is_other_bidders = "y"

while is_other_bidders == "y": 
  name = input("What is your name? :")
  price_str = input("What is your bid? (e.g., 10.50) $")
  
  price = float(price_str)
  auction_bids[name] = price # "name: price" is "Key: Value" pair
  
  is_other_bidders = input("Are there any other bidders? (y/n)")
  if is_other_bidders == "y":
    print("\n" * 20)

biggest_price = 0
biggest_bidder = None
for name, price in auction_bids.items():
  if price > biggest_price:
    biggest_price = price
    biggest_bidder = name

print(f"The winner is {biggest_bidder} with a bid of ${biggest_price}.")