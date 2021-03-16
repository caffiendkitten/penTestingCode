# !/user/bin/python3
# This program will encrypt the input with a very basic Ceasar Cipher.
# It is not optomized, recommended, or tested for real use.
# This is just a test program.


def cipher1(inputz, shift):
    alphabetLower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alphabetUpper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    alphabetSpecial = [" ", "!", "#",  "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
    alphabetNum = [0,1,2,3,4,5,6,7,8,9]
    temp = ""
    


    for x in inputz:
        if x in alphabetLower:
            if ascii(x) == ascii(alphabetLower[alphabetLower.index(x)]):
                temp += alphabetLower[alphabetLower.index(x)+shift]
        elif x in alphabetUpper:
            if ascii(x) == ascii(alphabetUpper[alphabetUpper.index(x)]):
                temp += alphabetUpper[alphabetUpper.index(x)+shift]
        elif x in alphabetSpecial:
            if ascii(x) == ascii(alphabetSpecial[alphabetSpecial.index(x)]):
                temp += alphabetSpecial[alphabetSpecial.index(x)+shift]
        elif x in alphabetNum:
            if ascii(x) == ascii(alphabetNum[alphabetNum.index(x)]):
                temp += alphabetNum[alphabetNum.index(x)+shift]
    print(temp)





inputz = input("Please enter input to the ciper: ") 
inputz = inputz # Given number
shift = input("Please enter shift value: ") 
shift = int(shift) # Given shift value
cipher1(inputz, shift)

