def decryption(text,k):
    k = k%26
    result=""
    for ch in text:
        if ch>='A' and ch<='Z':
            m= ord(ch)-ord('A')
            c=(m-k)%26
            result+=chr(c+ord('A'))
    return result

text= input("Enter plaintext: ").upper().replace(" ", "")
for i in range(26):
    result= decryption(text, i)
    print("For the key: ", i, "==>", result)
