import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-age","--age", help="what is your age",type=str)

args = parser.parse_args()
print ('''Happy birthday, you are already''',args.age,'''old!''')