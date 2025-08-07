from textblob import TextBlob

# Step 1: Caesar Cipher Decryption
def caesar_decrypt(cipher_text, shift):
    decrypted = ""
    for char in cipher_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

# Step 2: Spell Correction
def correct_spelling(text):
    blob = TextBlob(text)
    return str(blob.correct())

# Example cipher input
cipher_text = "Uifsf jt b tfdsfu dpef"  # Encrypted with Caesar shift of 1
shift = 1

# Run the process
decrypted = caesar_decrypt(cipher_text, shift)
corrected = correct_spelling(decrypted)

print("Decrypted:", decrypted)
print("Corrected:", corrected)

