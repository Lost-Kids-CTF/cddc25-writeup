# Break The ECDSA

## Challenge (??? points, ??? solves)

As BH-2000 was cleaning the office, it lost Dex's key.
Now, without the key, Dex can't even open his cabinet for his combat suit.
Dex needs the suit to save whoever and whatever he needs to, so BH-2000 wants to recover Dex's key.

Dex says he used a combination of English words to create the key.
Unfortunately, he's forgotten some of the words he used.
Let's find the forgotten words and recover the key with whatever the information we have on hand!

```bash
words : BIP-39 SECP256k1 {word1} 5eed r4nd0m {word2} g00d 5olve c0ffe {word3} pe4nut 5mart
r = 81210355722750344493541519494641458710145722871994877785183554697310523407018
h1 = 45643200378651069483892104393394606812504455659831083323743202489147422538955
h2 = 74831345439009646272332597737070016777412939113737083148228963710487431876647
s1 = 110764343964105699917226529930289538481215574456544978805357332521308340464732
s2 = 90138993253633063487274662700800979929978777245182171200537527514756442604713
```

Oh, you thought it was a physical key?
Duh, what year do you think we're in? :P

FLAG Format : CDDC2025{word1_word2_word3_privatekey}
※ Private key value is written in hexadecimal
Ex) 0x1234567890abcdef

## Summary

We are given an ECDSA signature challenge involving reused `k` values across two signed messages. The challenge also provides partial information about a mnemonic used to derive the ECDSA key. Our task is to recover the private key and reconstruct the BIP-39 mnemonic that generated it using a custom dictionary.

## Analysis

From the problem statement, we're told that Dex used a mnemonic in the form:

```bash
BIP-39 SECP256k1 {word1} 5eed r4nd0m {word2} g00d 5olve c0ffe {word3} pe4nut 5mart
```

This phrase was then processed into a seed via PBKDF2-HMAC-SHA512 with the salt "mnemonic". The seed was used in the standard BIP-32 master key derivation, where the private key is taken from the left 32 bytes of:

```python
I = HMAC-SHA512(key="Bitcoin seed", msg=seed)
```

Separately, we are also given ECDSA signature parameters `r`, `s1`, `s2` along with their respective hashes `h1`, `h2`. This suggests a reused `k`, which allows us to recover the private key using:

```bash
k = (h1 - h2) / (s1 - s2) mod n  
priv = (s1 * k - h1) / r mod n
```

Where `n` is the order of the SECP256k1 curve.

## Approach

### Step 1: Recover the Private Key

Using the equations above, compute `k` and the private key `priv` from the given ECDSA values. This is possible due to the reused `k`, a classic cryptographic vulnerability.

### Step 2: Brute-force the Mnemonic Words

The format of the mnemonic is partially known and only three words are unknown. Using a custom dictionary (`Dex_dictionary.txt`), try all 3-word combinations (`word1`, `word2`, `word3`) and compute the derived private key for each combination. Match it against the recovered `priv`.

The correct combination is the one that reproduces the recovered private key exactly.

## Flag

`CDDC2025{p4d0c0in_b3_5tr0ng_0x9f9068a0cc25f39b9c5fba5bb88d75bc5e4503a8406101a3195dc395194ea690}`
