import argparse
parser = argparse.ArgumentParser()
parser.add_argument("Value", help= "What is your value ?", type=str)
set1 = {0,"hi",2,300,100,2}
args = parser.parse_args()
print (set1)
set1.add(args.Value)
print ("New set is", set1 )