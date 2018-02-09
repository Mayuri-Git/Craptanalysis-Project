from Book import *
from Caesar import *
from RSA import *

'''
This class implements the attack on BCR crypto-system
It calls relevant methods from Book, Caesar and RSA cipher for cryptanalysis 
It also verifies crypto-system design implementation by encrypting broken message back to retrieve original book text
'''
class BCR:

    book = None;
    caesar = None;
    rsa = None;

    bookText = "SIERRA-ZERO-JULIET-SIX-YANKEE-ONE-ROMEO-PAPPA-EIGHT-KILO-FIVE-UNIFORM-XRAY-XXX-BRAVO-VICTOR-TWO-FOUR-TANGO-MIKE-OSCAR-HOTEL-DELTA-QUEBECK-FOXTROT-ALPHA-YYY-LIMA-INDIA-THREE-WHISKEY-NOVEMBER-ECHO-CHARLIE-GOLF-ZULU"

    finalNumber = "02192404240811270719140602241104010404040" \
                  "83018141904071807141212241907191709120624" \
                  "06270107062704143004080918170602120819140" \
                  "40614080908171814042718180830060408090714" \
                  "17061727170924302409091208191709142701240" \
                  "4113007060419062409011109180619111802270619"
    finalNum = []

    def __init__(self):
        self.book = Book()
        self.caesar = Caesar()
        self.rsa = RSA()

    def convertHex(self,hexInput):
        input = ''.join(hexInput)
        Decimaloutput = str(int(input,16))
        return Decimaloutput

    def processFinalNumber(self):
        i = 0
        while (i < len(self.finalNumber)):
            self.finalNum.append(self.finalNumber[i:i + 2])
            i = i + 2
        return self.finalNum

    def findSubstitutedFinalNum(self,txt, finNumber):
        substitutedFinalNum = []
        for i in range(0,len(finNumber)):
            index = int(finNumber[i])-1
            substitutedFinalNum.append(txt[index])
        return substitutedFinalNum

def main():

    bcr = BCR()

    print "\nCryptography Project Challenge:\t BCR Code (Book-Caesar-RSA)"
    print "\nChallenge Link:"
    print "\nhttps://www.mysterytwisterc3.org/images/challenges/mtc3-theofanidis-01-bcr-en.pdf"
    print "\nTeam:"
    print "\t\tMayuri Wadkar"
    print "\t\tPratik Surana"
    print "--------------------------------------------------------------------------------------"

    print "Introduction\r\n" +"Once upon a time, there have been three pirates: Alice, Bob and\r\n"\
    "Eve. They lived on the island Mallorca near a village called Porreres.\r\n"\
    "One day, while Alice and Bob were digging in their garden, they\r\n"\
    "found a treasure map. Because they could not gure out how to\r\n"\
    "use the instructions, they asked Eve who was an expert on\r\n"\
    "mysteries and riddles for help.\r\n"\
    "It turned out that Eve has made copies of the map and the\r\n"\
    "instructions for herself and is trying to nd the treasure on her own.\r\n"\
    "Can you help Alice and Bob to nd the treasure before Eve nds\r\n"\
    "the location?\r\n"

    print "The points A,B,C,D,E marked on the map are potential starting points of the treasure hunt.\n"

    print "Stage1-------------------------------------------------------------------------------------------"
    print "\nBook Text:\n"+str(bcr.bookText)
    stage1DecodedText = bcr.book.getDecodedText(bcr.bookText)
    print "\nDecoded Text:\n"+str(stage1DecodedText)
    print "\nCryptanalysis : Numbers 7 & 9 are missing.."
    print "\nTwo possible decoding:\n"
    bcr.book.XXX = "7"
    bcr.book.YYY = "9"
    stage1DecodedText1 = bcr.book.decrypt()
    bcr.book.XXX = "9"
    bcr.book.YYY = "7"
    stage1DecodedText2 = bcr.book.decrypt()
    print "1st possibility:\n"+str(stage1DecodedText1)
    print "2nd possibility:\n"+str(stage1DecodedText2)
    print "\nFinal Number :\n"+str(bcr.finalNumber)
    stage1FinalNum = bcr.processFinalNumber()
    print "\nFinal Number processed:\n"+str(stage1FinalNum)
    stage1SubstitutedFinalNum1 = bcr.findSubstitutedFinalNum(stage1DecodedText1, stage1FinalNum)
    stage1SubstitutedFinalNum2 = bcr.findSubstitutedFinalNum(stage1DecodedText2, stage1FinalNum)
    print "\nTwo possible final number decodings:\n"
    print "1st possibility:\n" + str(stage1SubstitutedFinalNum1)
    print "2nd possibility:\n" + str(stage1SubstitutedFinalNum2)
    print "\n\nStage2-------------------------------------------------------------------------------------------"
    bcr.caesar.lettersOffset = 15;
    bcr.caesar.digitsOffset = 7;
    print "\nShifting digits by 7 to left & shifting letters by 15 to right for 1st possibility from stage 1"
    stage2output1 = bcr.caesar.shift(stage1SubstitutedFinalNum1,"left")
    print str(stage2output1)
    print "\nShifting digits by 7 to right & shifting letters by 15 to right for 1st possibility from stage 1"
    stage2output2 = bcr.caesar.shift(stage1SubstitutedFinalNum1,"right")
    print str(stage2output2)
    print "\nShifting digits by 7 to left & shifting letters by 15 to right for 2nd possibility from stage 1"
    stage2output3 = bcr.caesar.shift(stage1SubstitutedFinalNum2,"left")
    print str(stage2output3)
    print "\nShifting digits by 7 to right & shifting letters by 15 to right for 2nd possibility from stage 1"
    stage2output4 = bcr.caesar.shift(stage1SubstitutedFinalNum2,"right")
    print str(stage2output4)
    print "\n\nStage3-------------------------------------------------------------------------------------------"
    print "\nCryptanalysis : Converting stage2 four HEX outputs to Decimal"
    stage3Decimal1 = bcr.convertHex(stage2output1)
    stage3Decimal2 = bcr.convertHex(stage2output2)
    stage3Decimal3 = bcr.convertHex(stage2output3)
    stage3Decimal4 = bcr.convertHex(stage2output4)
    print "Output1:\t",
    print str(stage3Decimal1)
    print "Output2:\t",
    print str(stage3Decimal2)
    print "Output3:\t",
    print str(stage3Decimal3)
    print "Output4:\t",
    print str(stage3Decimal4)

    print "\nCryptanalysis : 2nd decimal output contains a standard e value 65537"

    print "Splitting it to get n,e,c for RSA"

    n = long(stage3Decimal2[0:72])
    c = long(stage3Decimal2[77:149])
    e = long(stage3Decimal2[72:77])
    print "n = "+str(n)
    print "e = "+str(e)
    print "c = "+str(c)
    m = bcr.rsa.decrypt(n,c,e)
    print "m = "+str(m)

    j = 0
    mSplit = []
    while (j < len(str(m))):
        mSplit.append(str(m)[j:j + 3])
        j = j + 3
    print '\nSplitting into tuples of size 3'
    print str(mSplit)

    print "\nFinding ASCII values for each tuple in m.."
    print "\nMessage Broken:------------------------------------------------------------------->>"
    for token in mSplit:
        print str(chr(int(token[0:2]))),
    print "\n---------------------------------------------------------------------------------->>"
    print "\n\nLets go treasure hunting... :)"

    print "\n\nStage4 : Encrypting broken message back to get original book text--------------"

    print '\nRSA cipher encryption..'
    decimalInput = bcr.rsa.encrypt(m)
    print '\nCaesar cipher encryption..'
    finalNumDecoding = bcr.caesar.encrypt(decimalInput)
    print '\nBook cipher encryption..'
    initialBookText = bcr.book.encrypt(finalNumDecoding,bcr.finalNum)
    print '\nBook cipher ciphertext: ' + str(stage1DecodedText1)
    print '\nFrom above ciphertext we get our original boot text back...'
    print str(bcr.bookText)

if __name__ == '__main__':
    main()