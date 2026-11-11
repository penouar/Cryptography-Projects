# 🔐 Cryptography Projects

Small Python projects that implement classic ciphers, **break** a reused-key XOR cipher, and measure why password hashing needs to be slow.

🌱 I built these on my own, for learning, to understand how cryptographic schemes work and how they fail. They are self-directed practice projects, not coursework.

> ⚠️ **Educational use only.** None of this code should be used to protect real data.

## 📦 What is inside

| # | Project | File | Topic |
|---|---------|------|-------|
| 1 | 🔤 Caesar cipher | `caesar.py` | Shift cipher, encryption and decryption |
| 2 | 🔨 Caesar brute force | `caesar_bruteforce.py` | Trying all 26 keys |
| 3 | 🧩 Transposition ciphers | `transposition_ciphers.py` | Columnar and row transposition with a keyword |
| 4 | 🕵️ XOR key-reuse attack | `xor_key_reuse_attack.py` | Breaking the two-time pad with a dictionary |
| 5 | 🔑 Password hashing benchmark | `hash_benchmark.py` | SHA-256 vs bcrypt vs Argon2 |
| 6 | 🌊 SHA-256 avalanche effect | `sha256_avalanche.py` | Bit differences between near-identical inputs |

## ⚙️ Requirements

- Python 3.8+
- Only project 5 needs extra packages:

```bash
pip install -r requirements.txt   # bcrypt, argon2-cffi
```

## 1. 🔤 Caesar cipher (`caesar.py`)

Shifts every letter of the alphabet by a key `k` (taken modulo 26). Input is upper-cased and spaces are removed.

```bash
python caesar.py
# Enter 1 for encryption and 2 for decryption: 1
# Enter plaintext: attack at dawn
# Enter the key: 7
```

Use letters only: digits and punctuation are not supported.

## 2. 🔨 Caesar brute force (`caesar_bruteforce.py`)

The Caesar key space is only 26 values, so the cipher is broken by trying all of them and reading the output for the one that makes sense.

```bash
python caesar_bruteforce.py
# Enter ciphertext: HAAHJRHAKHDU
# For the key:  0 ==> HAAHJRHAKHDU
# ...
# For the key:  7 ==> ATTACKATDAWN
```

## 3. 🧩 Transposition ciphers (`transposition_ciphers.py`)

Two keyed transposition ciphers. The key word (for example `ANALYST`) gives the column order, with repeated letters ordered left to right. The plaintext is written in rows, and short rows are padded with `X`.

- **Columnar transposition:** columns are read out in key order.
- **Row transposition:** columns are permuted by key order and the grid is read row by row.

Example with `P = "THE NOSE IS POINTING DOWN AND THE HOUSES ARE GETTING BIGGER"` and `K = "ANALYST"`:

```
Columnar : TIIAOEGEPGDSEINODTETGHSNNUGBSNWEAIEETNHRNROIOHSTG
Row      : TENHSEOIPOSNTIIGDNWNOADTNEHHOSEUARSEETGINTGIGBERG
```

Decryption returns the cleaned plaintext, possibly followed by the `X` padding.

## 4. 🕵️ XOR key-reuse attack (`xor_key_reuse_attack.py`)

Encrypting two messages with the **same** XOR key (a "two-time pad") is fatal:

```
C1 = M1 XOR K
C2 = M2 XOR K
C1 XOR C2 = M1 XOR M2      <- the key cancels out
```

🎯 **Attack.** Given two ciphertexts, where the plaintexts and the key are all 12-letter English words:

1. Load a word list and keep only the 12-letter alphabetic words.
2. For each candidate `M1`, compute `K = C1 XOR M1` and `M2 = C2 XOR K`.
3. Keep the candidate only if `K` **and** `M2` are also words in the list.

```bash
python xor_key_reuse_attack.py
```

Result for the ciphertexts in the script:

```
M1 = accumulative
M2 = opportunists
K  = Californians
```

The script also checks `M1 XOR K` and `M2 XOR K` against the original ciphertexts. It stops at the first valid match.

**Word list:** the script reads `dic.txt` from the current folder, one word per line. Provide your own word list, such as any `/usr/share/dict/words` file.

💡 **Lesson:** never reuse a one-time pad or stream-cipher key. Redundancy in natural language is enough to recover everything.

## 5. 🔑 Password hashing benchmark (`hash_benchmark.py`)

Hashes the same password repeatedly for 3 seconds with each algorithm and reports how many hashes were computed and the average time per hash.

```bash
python hash_benchmark.py
```

SHA-256 is designed to be fast, so an attacker can try an enormous number of guesses per second. bcrypt and Argon2 are deliberately slow and use salts, which makes brute force expensive. Absolute numbers depend on your machine, but SHA-256 is orders of magnitude faster than the other two.

## 6. 🌊 SHA-256 avalanche effect (`sha256_avalanche.py`)

Counts how many of the 256 output bits change when the input changes slightly.

```
Different bits between name123 and name124: 135
Different bits between name124 and Name124: 131
```

A one-character change flips about half of the output bits (around 128 of 256), which is the behavior expected of a good hash function.

## 📁 Repository structure

```
cryptography-projects/
├── README.md
├── requirements.txt
├── caesar.py
├── caesar_bruteforce.py
├── transposition_ciphers.py
├── xor_key_reuse_attack.py
├── hash_benchmark.py
└── sha256_avalanche.py
```

## 🛠️ Skills demonstrated

Python, classical cryptography, cryptanalysis, XOR and bitwise operations, hashing, password-storage security.

## 📄 License

MIT
