import argparse
from functions import delete, register, list

#pyhton main.py ...
parser = argparse.ArgumentParser()

parser.add_argument('-r', type=str, nargs="+", help="Register task")
parser.add_argument('-lt', help="List tasks")
parser.add_argument('-dl', type=str, nargs="+", help="Delete Tasks")

args = parser.parse_args()

if args.r :
    register(args.r) #[x,y]

if args.lt:
    list()

if args.dl:
    delete(args.dl)
