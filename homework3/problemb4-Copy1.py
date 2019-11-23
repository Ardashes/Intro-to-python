market={"dairy":["yogurt","cheese"],"fruits":["banana","apple","orange","lemon","apple","banana","banana",]}
print (market)
market["candies"]=["mars","kinder","twix"]
market["fruits"].sort()
print (market)
market2={}
for fruits,banana in market.items():
     if banana not in market2.values():
      market2["fruits"]="banana"
for fruits,apple in market.items():
     if apple not in market2.values():
      market2["fruits"]="apple","banana","orange","lemon"     
market3=market["dairy"],market2,market["candies"]      
print (market3)     
