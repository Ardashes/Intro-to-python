import argparse
parser = argparse.ArgumentParser()
parser.add_argument("Value", help= "What is your value ?", type=int)
set2 = {0,"hi",2,300}
args = parser.parse_args()
print (set2)
set2.remove(args.Value)
print ("New set is", set2 )