def clean_text(text):
    text = text.upper().replace(" ", "")
    final_text = ""
    for ch in text:
        if 'A' <= ch <= 'Z':
            final_text += ch
    return final_text


def get_key(key):
    key=key.upper()
    sort = sorted(key)
    order = [0] * len(key)
    num = 1
    for ch in sort:
        for i in range(len(key)):
            if key[i] == ch and order[i] == 0:
                order[i] = num
                num += 1
                break
    return order


def columnar_encrypt(text, key):
    text = clean_text(text)
    columns = len(key)
    rows = (len(text) + columns - 1) // columns
    arr= [['X'] *columns for _ in range(rows)]
    k = 0
    for r in range(rows):
        for c in range(columns):
            if k < len(text):
                arr[r][c] = text[k]
                k += 1
    final_key=get_key(key)
    ciphertext = ""
    for num in range(1, columns + 1):
        col = final_key.index(num)
        for r in range(rows):
            ciphertext += arr[r][col]
    return ciphertext


def columnar_decrypt(cipher, key):
    columns = len(key)
    rows = (len(cipher) + columns - 1) // columns
    arr = [[''] * columns for _ in range(rows)]
    final_key = get_key(key)
    k = 0
    for num in range(1, columns + 1):
        col = final_key.index(num)
        for r in range(rows):
            if k < len(cipher):
                arr[r][col] = cipher[k]
                k += 1
    text = ""
    for r in range(rows):
        for c in range(columns):
            text += arr[r][c]
    return text


def row_encrypt(text, key):
    text = clean_text(text)
    columns = len(key)
    rows = (len(text) + columns - 1) // columns
    arr = [['X'] *columns for _ in range(rows)]
    k = 0
    for r in range(rows):
        for c in range(columns):
            if k < len(text):
                arr[r][c] = text[k]
                k += 1
    final_key = get_key(key)
    new_arr = [[''] * columns for _ in range(rows)]
    for i in range(columns):
        col = final_key.index(i + 1)
        for r in range(rows):
            new_arr[r][i] = arr[r][col]
    cipher = ""
    for r in range(rows):
        for c in range(columns):
            cipher += new_arr[r][c]
    return cipher


def row_decrypt(cipher, key):
    columns = len(key)
    rows = (len(cipher) + columns - 1) // columns
    arr = [[''] * columns for _ in range(rows)]
    k = 0
    for r in range(rows):
        for c in range(columns):
            arr[r][c] = cipher[k]
            k += 1
    order = get_key(key)
    original = [[''] * columns for _ in range(rows)]
    for i in range(columns):
        col = order.index(i + 1)
        for r in range(rows):
            original[r][col] = arr[r][i]
    text = ""
    for r in range(rows):
        for c in range(columns):
            text += original[r][c]
    return text

P = "THE NOSE IS POINTING DOWN AND THE HOUSES ARE GETTING BIGGER"
K = "ANALYST"

column_encrypt = columnar_encrypt(P,K)
print("Columinar Encryption: ", column_encrypt)
column_decrypt = columnar_decrypt(column_encrypt, K)
print("Columinar Decryption: ", column_decrypt)

row = row_encrypt(P,K)
print("Row Encryption: ", row)
row_plain = row_decrypt(row, K)
print("Row Decryption: ", row_plain)
