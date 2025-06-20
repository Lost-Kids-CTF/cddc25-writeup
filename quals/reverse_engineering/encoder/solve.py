import base64

# Precompute a 256-entry bit-reversal table
bit_rev = [int(f"{i:08b}"[::-1], 2) for i in range(256)]

BASE_KEY = 66

def decode(ct_b64: str) -> str:
    data = base64.b64decode(ct_b64)
    out_bytes = []
    for idx, byte in enumerate(data):
        # 1) undo the bit-reversal
        rev = bit_rev[byte]
        # 2) undo the position-based XOR
        pos_key = (idx * 7 + 13) % 256
        xored = rev ^ pos_key
        # 3) undo the fixed BASE_KEY XOR
        orig = xored ^ BASE_KEY
        out_bytes.append(orig)
    return bytes(out_bytes).decode("utf-8")

if __name__ == "__main__":
    ct = "MEi4xJpC4pI+FiJuAn4i2o7hpfHVCavRpfkzp18rX99jwWdodAA0wHQAYtKO9noGdBJ2sg=="
    print(decode(ct))
