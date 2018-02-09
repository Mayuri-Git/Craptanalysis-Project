import BCR
'''
Book text:
SIERRA-ZERO-JULIET-SIX-YANKEE-ONE-ROMEO-PAPPAEIGHT-KILO-FIVE-UNIFORM-XRAY-XXX-BRAVO-VICTORTWO-FOUR-TANGO-MIKE-OSCAR-HOTEL-DELTA-QUEBECKFOXTROT-ALPHA-YYY-LIMA-INDIA-THREE-WHISKEYNOVEMBER-ECHO-CHARLIE-GOLF-ZULU
Alice and Bob could not read some parts of the text. The two
words are marked as XXX and YYY. You have to gure out the
correct substitutions.
'''

class Book:

    text = ""
    XXX = ""
    YYY = ""
    decodedText = []

    digits = {
        "ZERO":0,
        "ONE":1,
        "TWO":2,
        "THREE":3,
        "FOUR":4,
        "FIVE":5,
        "SIX":6,
        "SEVEN":7,
        "EIGHT":8,
        "NINE":9
    }

    def getText(self):
        return self.text

    def getDecodedText(self,text):
        self.decodedText = text.strip().split("-")
        #print str(decodedText)
        for i in range(0,len(self.decodedText)):
            if self.decodedText[i] in self.digits.keys():
                self.decodedText[i] = str(self.digits[self.decodedText[i]])
            elif self.decodedText[i] == 'XXX':
                pass
            elif self.decodedText[i] == 'YYY':
                pass
            else:
                self.decodedText[i] = self.decodedText[i][0]
        return self.decodedText

    def decrypt(self):
        decodedText1 = []
        for i in range(0, len(self.decodedText)):
            decodedText1.append(self.decodedText[i])
            if self.decodedText[i] == 'XXX':
                decodedText1[i] = self.XXX
            elif self.decodedText[i] == 'YYY':
                decodedText1[i] = self.YYY
        return decodedText1

    def encrypt(self,input,finalNum):
        output = []
        for i in range(36):
            output.append('')
        for j in range(len(finalNum)):
            output[int(finalNum[j])-1] = input[j]
        return output




