from Crypto.Util.number import *

# def iroot(x, n):
#     """Return (y, b) where y is the integer nth root of x and b is True if y is exact."""
#     if x == 0:
#         return x, True
#     k = (x.bit_length() - 1) // n
#     y = 1 << k
#     for i in range(k - 1, -1, -1):
#         z = y | 1 << i
#         if z ** n <= x:
#             y = z
#     return y, x == y ** n

flag = b'<redacted>'
flag = bytes_to_long(flag)

p = getPrime(64) # returns a random 64 bit prime number
q = getPrime(256) # returns a random 256 bit prime number
n = p * q

assert n > flag

phi = (p-1) * (q-1)

e = 65535 # 2^16 - 1
#d = pow(e, -1, phi) # n^e % -1 = 0
d = pow(n,e,-1)
#print("d:", d) # 0

ct = pow(flag, e, n) # ct = flag^e % n = flag ^ 65535 % (p*q)


#print("n:", n) # 1611913360955528663054324169736689343135929083519085238380892808738256415602840059371434432090673
# BASE64 - PDUrwqrDtHbDqwoBw7TDuQ==
#print("ct:", ct) # 958641319547732447747427478465970976236954956070767518975162742968210412550503669031432234762485
# bASE 64 - w6xGwqLDkh/Dqg==

n = 1611913360955528663054324169736689343135929083519085238380892808738256415602840059371434432090673
ct = 958641319547732447747427478465970976236954956070767518975162742968210412550503669031432234762485

q = 106264993776059623933915696845839220369367557810234839837653411075124338073471

p = 15168808689270122063

#print(n == p*q)

# 1611913360955528662948059175960629719202013386673246018011525250928021575765171479487620823895140
phi = (p-1) * (q-1)

print("phi:", phi)

d = inverse(e, phi)

#d = pow(e, -1, phi)

print("d:", d)

flag = pow(ct, d, n)

print("flag:", flag)

print(long_to_bytes(flag))

print(long_to_bytes(flag).decode('ascii'))

# convert to ASCII to get the flag

