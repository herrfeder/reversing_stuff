import pdb

bomb_explode = 0
ecx = 0

inp_str = raw_input("Give input:")
eax = inp_str.lower()
str_inp_P0x8 = eax # eax = inp_str
eax = len(inp_str)
str_len_M0x10 = eax
ebpM0x14 = 0
ebpM0xc = 0


if (eax < 4):
    print "String is smaller 4 bytes"
    bomb_explode = 1 # when string smaller than 4 bomb will explode


ebpM0x14 = 0
while bomb_explode != 1:
    eax = ebpM0x14
    print("STR_LEN_M0x10: %d"%(str_len_M0x10))
    print("EAX: %d"%(eax))
    print("ECX: %d"%(ecx))
    print("ebpM0x14: %d"%(ebpM0x14))
    if (eax < str_len_M0x10): # if eax smaller than str_len

        edx = ebpM0x14
        eax = str_inp_P0x8
        eax = eax[edx]
        ebpM0xc = eax #taking first char of input

        if (ebpM0x14 == 0):
        
            ebpM0x14 += 1
            eax = ebpM0x14
        else:
            eax = ebpM0x14
            edx = eax + 1
            eax = str_inp_P0x8
            try:
                eax = eax[edx]
            except:
                pass
            if (eax != ebpM0xc):
                ebpM0x14 += 1
                eax = ebpM0x14
            else:
                print("EAX: %s"%(eax))
                print("ebpM0xc: %s"%(ebpM0xc))
                print "Bomb explode"
                bomb_explode = 1

    else:
        if (str_len_M0x10 > 1):
            eax = str_inp_P0x8
            edx = eax[0]
            eax = str_len_M0x10
            ecx = eax - 1 
            eax = str_inp_P0x8
            eax = eax[ecx]
            
            print("EDX: %s"%(edx[0]))
            print("EAX: %s"%(eax[0]))

            if (edx[0]==eax[0]):
                str_inp_P0x8 = str_inp_P0x8[1::]#str_inp_P0x8 +=1
                str_len_M0x10 -=2
            else:
                print "Bomb explode"
                bomb_explode = 1
