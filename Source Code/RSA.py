'''
The RSA key is not given.
Final number:
021924042408112707191406022411040104040408301814
190407180714121224190719170912062406270107062704
143004080918170602120819140406140809081718140427
181808300604080907141706172717092430240909120819
170914270124041130070604190624090111091806191118
02270619
'''
from Book import *
import math

class RSA:

    N = None
    exponent = None

    def modularInverse(self,a, m):
        g, x, y = self.part2(a, m)
        if g != 1:
            raise Exception('No modular inverse')
        return x % m

    def part2(self,a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = self.part2(b % a, a)
        return (g, x - (b // a) * y, y)

    def convertDecimalToHex(self,DecimalInput):
        Hexoutput = str(hex(DecimalInput))
        output=[]
        for char in Hexoutput:
            output.append(char.upper())
        output = output[2:-1]
        print '\nDecimal to HEX: '+str(output)
        return output

    def encrypt(self, plaintext):
        print str(plaintext)
        cipherText = (plaintext ** self.exponent) % self.N
        print "\nCiphertext discovered:\t"+str(cipherText)
        DecimalRSAInput = str(self.N)+str(self.exponent)+str(cipherText)
        print "\nDecimalRSAInput:\t"+str(DecimalRSAInput)
        return self.convertDecimalToHex(int(DecimalRSAInput))

    def decrypt(self,n,c,e):
        self.N = n
        self.exponent = e
        print '\nWe used an online tool to factorize n value..\nhttps://factordb.com/index.php'
        p = int('578455732137135466812346681323546443')
        q = int('866586465716584657165746753876546577')
        print "\nafter factorizing n we get,"
        print "p = " + str(p)
        print "q = " + str(q)
        print "\ninverting e to get d(=e^(-1) mod ((p-1)*(q-1)) ).."

        p_1 = p - 1
        q_1 = q - 1

        print "(p-1) = " + str(p_1)
        print "(q-1) = " + str(q_1)
        p_1mulq_1 = p_1 * q_1
        print "(p-1)*(q-1) = " + str(p_1mulq_1)
        print 'Finding d by multiplicative modular inverse..'
        d = self.modularInverse(e, p_1mulq_1)
        print "d = " + str(d)
        print "\nDecrypting c.... (m=c^d mod n)"
        print "Finding m i.e. Plaintext..."

        # we used Java BigInteger library to find out m
        m = 70082079077068071079078079082084072051055087069083084050051068073071053

        return m
