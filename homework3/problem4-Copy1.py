import argparse
parser = argparse.ArgumentParser()
parser.add_argument("Value", help= "What is your value ?", type=int)
list4 = [2,3,4,2,3,5]
args = parser.parse_args()
print (list4)
list4.remove(args.Value)
print ("New list is ",  list4)