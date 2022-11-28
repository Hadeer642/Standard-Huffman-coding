fileout = open("output.txt", 'w')
com = {"C": "0", "A": "11", "D": "101", "B": "100"}
d_swap = {v: k for k, v in com.items()}

# print(d_swap)
result = ""
dec = "0111011000"

p = ""
fileout.write("sequence :" + '\n')
for char in range(len(dec)):
    p += dec[char]
    if p in d_swap.keys():
        result += d_swap[p]
        p = ""
        fileout.write(result)
