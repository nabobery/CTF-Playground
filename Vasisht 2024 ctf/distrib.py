from Crypto.Util.number import getPrime, bytes_to_long

def SUS(num1, num2):
    bin_num1 = bin(num1)[2:]
    bin_num2 = bin(num2)[2:]

    max_len = max(len(bin_num1), len(bin_num2))
    bin_num1 = bin_num1.zfill(max_len)
    bin_num2 = bin_num2.zfill(max_len)

    result = ''
    for bit1, bit2 in zip(bin_num1, bin_num2):
        result += bit1 + bit2

    return int(result, 2)

p = getPrime(256)
q = getPrime(256)

n = p * q
e = 65537

m_ = b'...'.strip()
m = bytes_to_long(m_)

assert n > m

ct = pow(m, e, n)

print(ct)
print(SUS(p, q))
