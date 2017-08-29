

inp_str = raw_input("Give input:")

inp_str = inp_str.lower()

str_inp_P0x8 = eax # eax = inp_str

eax = len(inp_str)

str_len_M0x10 = eax

if (eax < 4):

    bomb_explode()

    ebpM0x14 = 0
    eax = ebpM0x14

if (eax < str_len_M0x10):

    edx = 0
    eax = str_inp_P0x8

    eax = eax[edx]

    ebpM0xc = eax

    if (ebpM0x14 == 0):
    
        ebpM0x14 += 1
        eax = ebpM0x14
    else:
        eax = ebpM0x14
        edx = eax + 1

        eax = str_inp_P0x8

        eax = eax[edx]

        if (eax != str_len_M0x10):
            ebpM0x14 += 1
            eax = ebpM0x14
        else:
            bomb_explode()

else:
    if (str_len_M0x10 > 1):

        eax = str_inp_P0x8
        edx = eax[0]

        eax = str_len_M0x10
        ecx = eax - 1 

        eax = str_inp_P0x8

        eax = eax
        
        eax = eax[ecx]

        if (edx(byte)==eax(byte)):

            str_inp_P0x8 +=1
            str_len_M0x10 -=2
