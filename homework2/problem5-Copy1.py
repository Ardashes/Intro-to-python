import argparse
parser=argparse.ArgumentParser()
parser.add_argument("text", help="uppercase and lowercase",type=str)
args=parser.parse_args()

print("All lowercase: ",args.text.lower())

print("All uppercase: ",args.text.upper())