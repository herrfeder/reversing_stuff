import binascii
import string
import pdb
ascii_list = list(string.printable)

def rshift(valname,val, n):
    bef_val = val
    s = val & 0x80000000
    for i in range(0,n):
        val >>= 1
        val |= s
    print '{0} {1:08b} after RSHIFT is {2:08b}'.format(valname,bef_val,val)
    return val
    
def lshift(valname,val, n):
    s = val & 0x80000000
    for i in range(0,n):
        val <<= 1
        val |= s

    print '{0} {1:08b} after LSHIFT is {2:08b}'.format(valname,bef_val,val)
    return val


def rev_string(comp_str):

    res_list = []
    comp_str = list(comp_str)
    counter = 0
    constant_10 = 10
    while(counter<=7):
        for char in ascii_list:
            orig_char = char
            div = ord(char) / constant_10
            mod = ord(char) % constant_10

            char = ord(char) + mod
            if chr(char) == comp_str[counter]:
                res_list.append(orig_char)
                break
        counter +=1

    print "".join(res_list)
'''
str_input = raw_input("Give Input:")

counter = 0

while(counter < 7):

    eax = str_input + counter
    eax = eax(byte) # zero_extension
    ecx = eax(byte) # sign_extension

    eax = str_input + counter
    eax = eax(byte) # zero_extension
    eax = eax(byte) # sign_extension

    ebx = 0x10 # dword obj.modulus

    edx = eda
    edx = rshift("edx",edx,0x1f)
    edx = eax % ebx
    eax = eax / ebx
    eax = eax + edx
    eax = edx + ecx
    ecx = str_input
    edx = counter
    edx = edx + ecx
    edx(byte) = eax(byte) # al
    if eax(byte) < 0x7b:
        counter += 1
'''

if __name__ == '__main__':

    rev_string("H0Tf00D:")

