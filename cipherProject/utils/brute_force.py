from algorithms.caesar import caesar_decrypt
from algorithms.vigenere import vigenere_decrypt


def brute_force_caesar(text):

    print("\nPossible decryptions:\n")

    for key in range(1, 26):

        decrypted = caesar_decrypt(text, key)

        print(f"Key {key}: {decrypted}")


def brute_force_vigenere(text, max_key_length=6):

    english_freq = [
        8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.15,
        0.77, 4.0, 2.4, 6.7, 7.5, 1.9, 0.10, 6.0, 6.3, 9.1,
        2.8, 0.98, 2.4, 0.15, 2.0, 0.074,
    ]

    letters_only = [c.lower() for c in text if c.isalpha()]

    if not letters_only:
        print("No alphabetic characters found in the text.")
        return

    def score(chars):
        total = len(chars)
        freq = [chars.count(chr(97 + i)) / total * 100 for i in range(26)]
        return sum(freq[i] * english_freq[i] for i in range(26))

    print("\nAttempting to break Vigenere cipher (frequency analysis):\n")

    for key_len in range(1, max_key_length + 1):

        if key_len > len(letters_only):
            break

        key = ""

        for i in range(key_len):
            nth_chars = letters_only[i::key_len]
            if not nth_chars:
                key += "a"
                continue
            best_shift = max(
                range(26),
                key=lambda s: score([chr((ord(c) - 97 - s) % 26 + 97) for c in nth_chars]),
            )
            key += chr(best_shift + 97)

        decrypted = vigenere_decrypt(text, key)
        print(f"Key length {key_len}, Key: '{key}' => {decrypted}")