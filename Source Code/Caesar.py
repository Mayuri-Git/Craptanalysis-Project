class Caesar:
    digitsOffset = None
    lettersOffset = None
    caesarKey = 0

    def __init__(self):
        self.digitsOffset = 0
        self.lettersOffset = 0
        self.dictRight = {
            '0': '3',
            '1': '4',
            '2': '5',
            '3': '6',
            '4': '7',
            '5': '8',
            '6': '9',
            '7': '0',
            '8': '1',
            '9': '2',
        }
        self.dictLeft = {
            '0': '7',
            '1': '8',
            '2': '9',
            '3': '0',
            '4': '1',
            '5': '2',
            '6': '3',
            '7': '4',
            '8': '5',
            '9': '6',
        }
        self.dictLeftLetter = {
            'P': 'A',
            'Q': 'B',
            'R': 'C',
            'S': 'D',
            'T': 'E',
            'U': 'F'
        }
        self.dictRightLetter = {
            'A': 'P',
            'B': 'Q',
            'C': 'R',
            'D': 'S',
            'E': 'T',
            'F': 'U'
        }

    def getDigitsOffset(self):
        return self.digitsOffset

    def getLettersOffset(self):
        return self.lettersOffset

    def setLettersOffset(self, letterOffset):
        self.lettersOffset = letterOffset

    def shift(self,stage1Output,digitDirection):

        caesarInput = []
        for i in range(0,len(stage1Output)):
            caesarInput.append(stage1Output[i])
        if digitDirection == "right":
            for i in range(0,len(caesarInput)):
                if caesarInput[i] in self.dictRight.keys():
                    caesarInput[i] = self.dictRight[caesarInput[i]]
        elif digitDirection == "left":
            for i in range(0, len(caesarInput)):
                if caesarInput[i] in self.dictLeft.keys():
                    caesarInput[i] = self.dictLeft[caesarInput[i]]
        for i in range(0, len(caesarInput)):
            if caesarInput[i] in self.dictLeftLetter.keys():
                caesarInput[i] = self.dictLeftLetter[caesarInput[i]]
        return caesarInput

    def encrypt(self, input):
        ciphertext = []
        for member in input:
            if member.isdigit() :
                ciphertext.append(self.dictLeft[member])
            else:
                ciphertext.append(self.dictRightLetter[member])
        print '\nCaesar cipher ciphertext:\t\n'+str(ciphertext)
        return ciphertext