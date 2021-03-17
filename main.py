import argparse
from searcher import Searcher

if __name__ == '__main__':

    # initializing arguements
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--underscore', action='store_true',
                        help="adds '^' as underscore")
    parser.add_argument('-c', '--color', action='store_true',
                        help="colorful output")
    parser.add_argument('-m', '--machine', action='store_true',
                        help="machine readable format")
    args = parser.parse_args()
    searcher = Searcher()

    # retrieving flags from user
    if args.machine:
        searcher.IS_M = True
    if args.underscore:
        searcher.IS_U = True
    if args.color:
        searcher.IS_C = True
    userInptut = raw_input("Please enter a string, or file(s) full path to search in\n"
                       "(file(s) path must be prefixed with '-')):\n\n")
    data = searcher.validateUserInput(userInptut)

    reg = raw_input("Please Enter a regular expression to be searched:\n")

    searcher.validateUserRegex(reg)
    while not searcher.ISREGEX:
        print("Please enter a valid regular expression!\n")
        reg = input("Please Enter a regular expression to be searched:\n")
        searcher.validateUserRegex(reg)

    searcher.regex = reg
    if searcher.ISFILES:
        searcher.handlefiles(data, searcher.regex)
    else:
        searcher.handleString(data, searcher.regex)
