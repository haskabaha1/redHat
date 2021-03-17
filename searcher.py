from __future__ import print_function
import re
import colorama

class Searcher:
    def __init__(self):
        colorama.init(autoreset=True)
        self.IS_M = False
        self.IS_U = False
        self.IS_C = False
        self.ISFILES = False
        self.ISREGEX = False
        self.fileName = "user_input"
        self.regex = None

    def getBareResult(self, res, reg, fno):
        # will return string in the following format
        # fileName:lineNumber:match
        rawResults = "{}:{}:{}".format(self.fileName, fno, reg)
        return rawResults

    def handlefiles(self, file, regx, returnValue=False):
        '''to handle inputs of type files
            takes a file and a regex to found a match for
            will procces the data and print results according to specified flags'''

        f = open(file, 'r')
        found = False
        # to keep count of line numbers
        lineNo = 1
        # iterating over file lines
        for line in f:
            # look for regex in given line
            match = re.search(regx, line)
            # if found, print according to user specified flags
            if match:
                self.regex = regx
                found = True
                result = self.getBareResult(match, regx, lineNo)
                # check if output should be in machine format
                if self.IS_M:
                    # to get the index of match in line
                    iterator = [(m.start(0), m.end(0)) for m in re.finditer(regx, line)]
                    result = self.addMachineFormat(match, lineNo, iterator[0])
                # check if output should be underscored
                if self.IS_U:
                    result = self.addUnderScore(result)
                if not returnValue:
                    # print results
                    self.printResults(result)
                else:
                    return result
            else:
                lineNo += 1
                continue
        if returnValue and not found:
            return None
        elif not found and not returnValue:
            print("No match was found!")

    def handleString(self, str, regx, returnValue=False):
        '''will hander userInput of type string
        will look for a matched regex in a given string
        will print the results according to specified flags'''

        # looking for a match in str
        match = re.search(regx, str)
        lineNo = 1
        if match:
            self.regex = regx
            result = self.getBareResult(match, regx, lineNo)
            if self.IS_M:
                iterator = [(m.start(0), m.end(0)) for m in re.finditer(regx, str)]
                result = self.addMachineFormat(match, lineNo, iterator[0])
            if self.IS_U:
                result = self.addUnderScore(result)
            if not returnValue:
                # print results
                self.printResults(result)
            else:
                return result
        if returnValue and not match:
            return None
        elif not match and not returnValue:
            print("No match was found!")


    def validateUserRegex(self, reg):
        # validate user regex
        try:
            re.compile(reg)
            self.ISREGEX = True
        except re.error:
            self.ISREGEX = False

    def validateUserInput(self, input):
        '''validate user input, determine weather it's a file
        or a raw input string'''
        list = []
        if len(input) == 0:
            assert ("no input was provided")
        if input.startswith('-'):
            self.ISFILES = True
            print("file input was detected..")
            list = input.split('-')
            self.fileName = input.split('\\')[-1].split('-')[-1]
            # for multiple files
            if len(list) > 2:
                return list
            else:
                return list[1]

        else:
            print("raw string input was detected")
            return input

    def addMachineFormat(self, res, fno, index):
        '''will manipulate given data into specified machine format'''
        res = "{}:{}:{}:{}".format(self.fileName, fno,
                                   index[0], res.string[index[0]:index[1]])
        return res

    def printResults(self, res):
        '''print results, but check if colored flag is provided first'''
        if self.IS_C:
            r = res.split(':')
            # _index = r.index(self.regex)
            # for i in range(len(res)):
            for w in r:
                if w == self.regex:
                    self.greenPrint(w)
                else:
                    print(w.strip()+':', end='')
        else:
            print(res)

    def addUnderScore(self, res):
        ''''adding underscore '^' under a given results'''
        res = res + ':\n' + '^' * len(res)
        return res

    def greenPrint(self, word):
        '''will add green color to a given word'''
        print(colorama.Fore.YELLOW + "{}".format(word))
