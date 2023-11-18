from art import logo
from replit import clear
print(logo)
print("Welcome to the secret auction model!")
bidding={}

def highest(records):
  highest_bid=0
  winner=""
  for bids in records:
    bid_amount=records[bids]
    if bid_amount>highest_bid:
      highest_bid=bid_amount
      winner=bids
  print(f"the winner is {winner} with amount ${highest_bid}")

bidding_finishes=False
while not bidding_finishes:
  name=input("What is your name?:")
  bid=int(input("What's your bid amount?:$"))
  bidding[name]=bid
  t=input("Are there any other bidders, 'Y' for \"YES\" and 'N' for \"NO\"").upper()
  if t=="N":
    bidding_finishes=True
    highest(bidding)
  elif t=="Y":
    clear()
  else:
    clear()
    
  



def ppl(name_given,bid_amt):
  bid_enter={}
  bid_enter[name]=name_given
  bid_enter[bid]=bid_amt
  bidding_list.append(bid_enter)



