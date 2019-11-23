dict1 = {'key':'value'}
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("key", help= "What is your value ?", type=str)
parser.add_argument("value", help= "What is your value ?", type=str)
args = parser.parse_args()
print (dict1)
dict1[args.key]=args.value
print (dict1)