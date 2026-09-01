# Lab 03 — Hash, Merkle tree & Digital Signatures
## Q1: 
Each extra leading zero multiplies the expected work by around 16 times, because each hexadecimal character has 16 possible values (0-f) so the probability of getting a zero is 1/16. Therefore requiring one more leading zero make the probability 16 times smaller.

## Q2: 
Verifying the nonce takes only one hash call. This shows that PoW is hard to find but easy to verify.

## Q3: 
A merkle proof contains approximately log2(n) hashes, so for 1000000 transactions, it contains about 20 hashes.

## Q4: 
Bitcoin SPV uses merkle proofs to verify that a transaction is included in a block without downloading the entire block.
