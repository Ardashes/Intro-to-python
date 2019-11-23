import argparse
parser = argparse.ArgumentParser()
parser.add_argument("text", help="The text", type=str)
args = parser.parse_args()
print("The old string:", args.text)
print("middle 3 characters:" , args.text[4:7])

print ("The new string:", args.text[0:4] + args.text[4:7].upper() +  args.text[7:])