from pathlib import Path

C1 = bytes.fromhex("22 02 0f 1c 0b 1a 1e 0f 1d 08 18 16")
C2 = bytes.fromhex("2c 11 1c 06 14 1b 07 00 00 12 1a 00")

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

def is_alpha_word(s: str) -> bool:
    return len(s) == 12 and s.isalpha()



words = []
with open("dic.txt", "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        w = line.strip()
        if is_alpha_word(w):
            words.append(w)
word_set = set(words)
print("C1 XOR C2 =", xor_bytes(C1, C2).hex(" "))
solution = None

for m1 in words:
    key_bytes = xor_bytes(C1, m1.encode("ascii", errors="ignore"))
    m2_bytes = xor_bytes(C2, key_bytes)
    try:
        m2 = m2_bytes.decode("ascii")
    except UnicodeDecodeError:
        continue
    if not is_alpha_word(m2):
        continue
    if m2 not in word_set:
        continue
    try:
        key_word = key_bytes.decode("ascii")
    except UnicodeDecodeError:
        continue
    if not is_alpha_word(key_word):
        continue
    if key_word not in word_set:
        continue
    solution = (m1, m2, key_word)
    break

if solution is None:
    print("No solution found.")
else:
    m1, m2, key_word = solution
    print("M1 =", m1)
    print("M2 =", m2)
    print("K  =", key_word)
    print("Verify M2 XOR K =", xor_bytes(m2.encode("ascii"), key_word.encode("ascii")).hex(" "))
    print("Verify M1 XOR K =", xor_bytes(m1.encode("ascii"), key_word.encode("ascii")).hex(" "))