import argparse
parser=argparse.ArgumentParser()
parser.add_argument("value" , help="What is the value?", type=int)
set3= {1,2,3,4}
args=parser.parse_args()
if min(set3)<args.value>max(set3):
    print(" It is")
else:
    print ("It is not")
