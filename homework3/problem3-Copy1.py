import argparse
parser = argparse.ArgumentParser()
parser.add_argument("Value", help= "What is your value ?", type=int)
list2 = [0,"hi",2,300,100,2]
args = parser.parse_args()
print (list2)
print ("Number of ", args.Value,"s"," ","=", list2.count(args.Value))