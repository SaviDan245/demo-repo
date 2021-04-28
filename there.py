from argparse import ArgumentParser


argparser = ArgumentParser('Add to integers')
argparser.add_argument('a', help='first integer', type=int)
argparser.add_argument('b', help='second integer', type=int)
argparser.parse_args()

print('This code needs to be checked...')
