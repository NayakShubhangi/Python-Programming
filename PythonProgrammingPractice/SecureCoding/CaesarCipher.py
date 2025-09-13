# Example: "Shubhangi", key = 5 (meaning that the letter should be incremented 5)
# In Caesar Cipher, the plain text is incremented by the key in order to encrypt it,
# and that cipher text is decremented by the same key to decrypt it and put it into a readable format.

def encrypt_text(plainText, key):
    cipherText = ""
    for letter in plainText:
        cipherText += letters[(letters.index(letter) + key) % 26]
    return cipherText

def decrypt_text(cipherText, key):
    plainText = ""
    for letter in cipherText:
        plainText += letters[(letters.index(letter) - key) % 26]
    return plainText

plainText = input("Enter text: ")
key = int(input("Enter a number: "))
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(encrypt_text(plainText, key))
print(decrypt_text("xmzgmfsln", key))