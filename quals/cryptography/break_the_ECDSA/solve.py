import hashlib, hmac
from itertools import product
from Crypto.Util.number import inverse

# Load word list from the Dex dictionary
with open("Dex_dictionary.txt", "r") as f:
    wordlist = [line.strip() for line in f.readlines()]

# ECDSA values from qn.txt
r = 81210355722750344493541519494641458710145722871994877785183554697310523407018
h1 = 45643200378651069483892104393394606812504455659831083323743202489147422538955
h2 = 74831345439009646272332597737070016777412939113737083148228963710487431876647
s1 = 110764343964105699917226529930289538481215574456544978805357332521308340464732
s2 = 90138993253633063487274662700800979929978777245182171200537527514756442604713

# secp256k1 order
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

# recover k and priv
k    = ((h1 - h2) * pow(s1 - s2, -1, n)) % n
priv = ((s1 * k - h1) * pow(r,     -1, n)) % n
priv_hex = hex(priv)

print(f"Recovered ECDSA private key: {priv_hex}")

# Known message template with placeholders
template = "BIP-39 SECP256k1 {} 5eed r4nd0m {} g00d 5olve c0ffe {} pe4nut 5mart"

# Try all word combinations
found = []
for word1, word2, word3 in product(wordlist, repeat=3):
    mnemonic = template.format(word1, word2, word3).encode()
    # print(f"Trying: {mnemonic.decode()}")
    seed = hashlib.pbkdf2_hmac('sha512',
                               mnemonic,
                               b'mnemonic',
                               2048,
                               dklen=64)
    I = hmac.new(b"Bitcoin seed", seed, hashlib.sha512).digest()
    cand_priv = int.from_bytes(I[:32], 'big')
    if cand_priv == priv:
        print("Found words:", word1, word2, word3)
        flag = f"CDDC2025{{{word1}_{word2}_{word3}_{priv_hex}}}"
        print("Flag:", flag)
        break
found
