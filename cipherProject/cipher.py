import argparse

from algorithms.caesar import caesar_encrypt, caesar_decrypt
from algorithms.vigenere import vigenere_encrypt, vigenere_decrypt
from utils.brute_force import brute_force_caesar, brute_force_vigenere


def main():

    parser = argparse.ArgumentParser(description="Cipher Tool")

    parser.add_argument("--algo", choices=["caesar", "vigenere"], required=True)

    parser.add_argument("--mode", choices=["encrypt", "decrypt", "bruteforce"], required=True)

    parser.add_argument("--text", required=True)

    parser.add_argument("--key")

    args = parser.parse_args()

    if args.algo == "caesar":

        if args.mode in ("encrypt", "decrypt") and args.key is None:
            print("Error: --key is required for caesar encrypt/decrypt.")
            return

        if args.mode == "encrypt":
            result = caesar_encrypt(args.text, int(args.key))
            print(result)

        elif args.mode == "decrypt":
            result = caesar_decrypt(args.text, int(args.key))
            print(result)

        elif args.mode == "bruteforce":
            brute_force_caesar(args.text)

    elif args.algo == "vigenere":

        if args.mode in ("encrypt", "decrypt") and args.key is None:
            print("Error: --key is required for vigenere encrypt/decrypt.")
            return

        if args.mode == "encrypt":
            result = vigenere_encrypt(args.text, args.key)
            print(result)

        elif args.mode == "decrypt":
            result = vigenere_decrypt(args.text, args.key)
            print(result)

        elif args.mode == "bruteforce":
            brute_force_vigenere(args.text)


if __name__ == "__main__":
    main()