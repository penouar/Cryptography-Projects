def encryption(text, k):
    k= k%26
    result=""
    for ch in text:
        if ch>='A' and ch<='Z':
            m= ord(ch)-ord('A')
            c=(m+k)%26
            result+=chr(c+ord('A'))
    return result

def decryption(text,k):
    k= k%26
    result=""
    for ch in text:
        if ch>='A' and ch<='Z':
            m= ord(ch)-ord('A')
            c=(m-k)%26
            result+=chr(c+ord('A'))
    return result

choice= int(input("Enter 1 for encryption and 2 for decryption: "))
text= input("Enter plaintext: ").upper().replace(" ", "")
k= int(input("Enter the key: "))
if choice==1:
    result=encryption(text, k)
else:
    result=decryption(text, k)

print(result)









