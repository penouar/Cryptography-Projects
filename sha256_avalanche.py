import hashlib

def sha256_hash(text):
    return hashlib.sha256(text.encode()).digest()

def count_different_bits(hash1, hash2):
    diff = 0
    for b1, b2 in zip(hash1, hash2):
        xor = b1 ^ b2
        diff += bin(xor).count("1")
    return diff

p1 = "name123"
p2 = "name124"
p3 = "Name124"

h1 = sha256_hash(p1)
h2 = sha256_hash(p2)
h3 = sha256_hash(p3)

diff1 = count_different_bits(h1, h2)
diff2 = count_different_bits(h2, h3)

print("Different bits between name123 and name124:", diff1)
print("Different bits between name124 and Name124:", diff2)