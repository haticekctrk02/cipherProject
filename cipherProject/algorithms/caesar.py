def caesar_encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            shift = key % 26

            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)
