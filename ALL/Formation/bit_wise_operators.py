print('{:08b}'.format(197,'b'))
x = bin(197>>1)[2:]
print(bin(197>>0)[2:],197>>0)
print(x,type(x),197>>1)
print('197>>2',bin(197>>2)[2:],197>>2)
print(bin(197>>3)[3:],197>>3)
print('197>>4',197>>4,197>>4==0b1110)
print('197>>5',bin(197>>5)[2:],197>>5,197>>5==0b110)
print('197>>6',bin(197>>6)[2:],197>>6,197>>6==0b110)
print('197>>7',bin(197>>7)[2:],197>>7,197>>7==0b1110)

result = 0 
idx = 0 
for _ in range(len(x)-1,-1,-1):
    if x[idx] == '1':
        result+= 2 ** _ 
    idx += 1
print(result)
# >> bit shifted to the right 
# << bit shifted to the left 