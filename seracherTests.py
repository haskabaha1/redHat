from searcher import Searcher


class SearcherTests:

    def sanityFile(self, filepath, regex, expected):
        """test sanity that checks handlefile functionality
            given: filepath and regex
            expected: given output string"""
        print("=" * 30)
        print("Start Test Sanity 1 : File Input")
        print("=" * 30)
        se = Searcher()
        file = se.validateUserInput(filepath)
        se.IS_M = True
        seValue = se.handlefiles(file, regex, returnValue=True)

        assert (seValue == expected), "Test Sanity Failed"
        print("returnValue:{}\nexpected:{}".format(seValue, expected))


    def sanityString(self, word, regex, expected):
        """test sanity that checks handleString functionality
            given: string and regex
            expected: given output string"""
        print("=" * 30)
        print("Start Test Sanity 2 : String Input")
        print("=" * 30)
        se = Searcher()
        se.validateUserInput(word)
        se.IS_M = True
        seValue = se.handleString(word, regex, returnValue=True)

        assert (seValue == expected), "Test Sanity Failed"
        print("returnValue:{}\nexpected:{}".format(seValue, expected))

