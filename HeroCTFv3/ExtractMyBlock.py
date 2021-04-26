from pwn import *
from string import printable
context.log_level = "error"

def get_block(token):
    new = []
    for i in range (0, len(token), block_size):
        new.append(token[i:i+block_size])
    return new

#The block size in hex
block_size = 32
auth_length = 129

#Here we get the "sould be block"


line = ['z','a','o','u','r',' ','p','a','s','s','w','o','r','d',' ',':',' ']
flag = []

def get_the_flag() :
    offset = 13
    while line[-1] != "}":

        #Getting the sould be block
        r = remote("chall0.heroctf.fr",10000)
        t = r.recv().decode()
        r.sendline("A"*(offset))
        t = r.recv().decode()
        block_sould_be = get_block(t)[2]

        for c in printable:
            r = remote("chall0.heroctf.fr",10000)
            t = r.recv().decode()
            r.sendline("".join(line)+c)
            t = r.recv().decode()
            block = get_block(t)
            if block_sould_be == block[1]:
                line.append(c)
                flag.append(c)
                line.pop(0)
                offset -= 1
                print("".join(flag))
get_the_flag()