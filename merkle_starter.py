#!/usr/bin/env python3
"""Lab 3.2 — Merkle tree (starter).


Hoàn thành 3 TODO rồi chạy:  python3 merkle_starter.py
Mọi dòng CHECK phải in OK.   All CHECK lines must print OK.


Quy ước (theo Bitcoin) / Convention (Bitcoin rule):
 - Lá = sha256(dữ liệu giao dịch).            Leaf = sha256(tx bytes).
 - Cha = sha256(trái + phải) trên byte digest. Parent = sha256(left + right) over raw digests.
 - Tầng lẻ: nhân đôi phần tử cuối.             Odd level: duplicate the last element.
"""
import hashlib

def H(b: bytes) -> bytes:
    return hashlib.sha256(b).digest()




def merkle_root(leaves: list[bytes]) -> bytes:
    level = leaves[:]
    while len(level) > 1:
        if len(level) % 2 == 1:
            level.append(level[-1])
        next_level = []

        for i in range(0, len(level), 2):
            parent = H(level[i] + level[i + 1])
            next_level.append(parent)

        level = next_level

    return level[0]

def merkle_proof(leaves: list[bytes], index: int) -> list[tuple[bytes, bool]]:
    proof = []
    level = leaves[:]

    while len(level) > 1:
        if len(level) % 2 == 1:
            level.append(level[-1])

        sibling_index = index - 1 if index % 2 == 1 else index + 1
        sibling_is_left = sibling_index < index

        proof.append((level[sibling_index], sibling_is_left))

        next_level = []

        for i in range(0, len(level), 2):
            next_level.append(H(level[i] + level[i + 1]))

        level = next_level
        index //= 2

    return proof

def verify_proof(leaf_hash: bytes, proof: list[tuple[bytes, bool]], root: bytes) -> bool:
    current = leaf_hash

    for sibling, sibling_is_left in proof:
        if sibling_is_left:
            current = H(sibling + current)
        else:
            current = H(current + sibling)

    return current == root


# ------------------------------------------------------------------ checks
if __name__ == "__main__":
    txs = [f"tx{i}: A->B {i} coin".encode() for i in range(8)]
    leaves = [H(t) for t in txs]
    root = merkle_root(leaves)


    print("root:", root.hex())


   # CHECK 1: proof đúng cho mọi lá / valid proof for every leaf
    ok = all(verify_proof(leaves[i], merkle_proof(leaves, i), root) for i in range(8))
    print("CHECK 1 (all 8 proofs valid):", "OK" if ok else "FAIL")


   # CHECK 2: proof có đúng log2(8)=3 phần tử / proof has exactly 3 elements
    print("CHECK 2 (proof length == 3):", "OK" if len(merkle_proof(leaves, 4)) == 3 else "FAIL")


   # CHECK 3: lá bị sửa phải trượt / a tampered leaf must fail
    fake = H(b"tx4: A->B 999999 coin")
    print("CHECK 3 (tampered leaf fails):",
        "OK" if not verify_proof(fake, merkle_proof(leaves, 4), root) else "FAIL")


   # CHECK 4: số lá lẻ (7) vẫn chạy / odd leaf count (7) still works
    l7 = leaves[:7]
    r7 = merkle_root(l7)
    print("CHECK 4 (odd count works):",
        "OK" if all(verify_proof(l7[i], merkle_proof(l7, i), r7) for i in range(7)) else "FAIL")


