# CipherProject

A command-line tool for classical cipher encryption, decryption, and cryptanalysis (brute-force) — built in Python.

Supported ciphers:
- **Caesar Cipher** — shift-based substitution cipher
- **Vigenère Cipher** — polyalphabetic substitution cipher with frequency-analysis attack

---

## Features

| Feature | Caesar | Vigenère |
|---|---|---|
| Encrypt | ✅ | ✅ |
| Decrypt | ✅ | ✅ |
| Brute-force / Cryptanalysis | ✅ (all 25 keys) | ✅ (frequency analysis, key length 1–6) |

---

## Project Structure

```
cipherProject/
├── cipher.py               # CLI entry point
├── algorithms/
│   ├── __init__.py
│   ├── caesar.py           # Caesar encrypt / decrypt
│   └── vigenere.py         # Vigenère encrypt / decrypt
├── utils/
│   ├── __init__.py
│   └── brute_force.py      # Brute-force & frequency analysis
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Requirements

- Python **3.8+**
- No third-party dependencies — standard library only

---

## Installation

```bash
git clone https://github.com/your-username/cipherProject.git
cd cipherProject
```

---

## Usage

```
python cipher.py --algo <caesar|vigenere> --mode <encrypt|decrypt|bruteforce> --text <TEXT> [--key <KEY>]
```

### Arguments

| Argument | Required | Description |
|---|---|---|
| `--algo` | ✅ | Cipher algorithm: `caesar` or `vigenere` |
| `--mode` | ✅ | Operation mode: `encrypt`, `decrypt`, or `bruteforce` |
| `--text` | ✅ | Input text |
| `--key` | For encrypt/decrypt | Integer key for Caesar; string key for Vigenère |

---

## Examples

### Caesar Cipher

**Encrypt:**
```bash
python cipher.py --algo caesar --mode encrypt --text "Hello World" --key 3
# Output: Khoor Zruog
```

**Decrypt:**
```bash
python cipher.py --algo caesar --mode decrypt --text "Khoor Zruog" --key 3
# Output: Hello World
```

**Brute-force (try all 25 keys):**
```bash
python cipher.py --algo caesar --mode bruteforce --text "Khoor"
# Key 3: Hello
```

---

### Vigenère Cipher

**Encrypt:**
```bash
python cipher.py --algo vigenere --mode encrypt --text "Hello World" --key "key"
# Output: Rijvs Uyvjn
```

**Decrypt:**
```bash
python cipher.py --algo vigenere --mode decrypt --text "Rijvs Uyvjn" --key "key"
# Output: Hello World
```

**Frequency analysis attack (guess key length 1–6):**
```bash
python cipher.py --algo vigenere --mode bruteforce --text "Rijvs Uyvjn"
```

---

## How It Works

### Caesar Cipher
Each letter in the plaintext is shifted by a fixed integer key along the alphabet. Non-alphabetic characters are preserved unchanged.

$$C = (P + k) \mod 26$$

### Vigenère Cipher
A polyalphabetic cipher where each letter is shifted by the corresponding letter of a repeating keyword.

$$C_i = (P_i + K_{i \mod |key|}) \mod 26$$

### Vigenère Brute-Force
Uses the **Index of Coincidence / frequency analysis** method: for each candidate key length, each nth column of ciphertext is treated as a Caesar cipher and the most likely shift is determined by comparing character frequencies to standard English letter frequencies.

---

## License

This project is licensed under the [MIT License](LICENSE).
