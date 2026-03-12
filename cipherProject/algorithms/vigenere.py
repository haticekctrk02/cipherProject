def vigenere_encrypt(text, key):

    result = ""
    key = key.lower()
    key_index = 0

    for char in text:

        if char.isalpha():

            shift = ord(key[key_index % len(key)]) - 97

            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)

            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)

            key_index += 1

        else:
            result += char

    return result


def vigenere_decrypt(text, key):

    result = ""
    key = key.lower()
    key_index = 0

    for char in text:

        if char.isalpha():

            shift = ord(key[key_index % len(key)]) - 97

            if char.isupper():
                result += chr((ord(char) - 65 - shift) % 26 + 65)

            else:
                result += chr((ord(char) - 97 - shift) % 26 + 97)

            key_index += 1

        else:
            result += char

    return result