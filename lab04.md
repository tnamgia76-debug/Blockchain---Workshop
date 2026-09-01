# Lab 04 — Real Bitcoin Blocks: PoW, Fees & Merkle Root

## Q1. Proof-of-Work Target

The target has roughly **19 leading zero hexadecimal digits**, which corresponds to about **76 leading zero bits** because each hexadecimal digit represents 4 bits. Therefore, finding one valid block header requires roughly **2^76 hash attempts on average**.

## Q2. Why is PoW verification much faster than finding a valid block?

SHA-256 produces an unpredictable and effectively random-looking output, so miners cannot directly predict which nonce will produce a hash below the target. They must try many different inputs until they find a valid hash. In contrast, verification only requires hashing the block header and comparing the resulting hash with the target.

## Q3. Why did this transaction have such a high fee rate?

The transaction was included on the 2024 Bitcoin halving day, when the launch of Runes caused unusually high demand for block space. Users competed for limited block space by offering extremely high transaction fees, demonstrating that Bitcoin fees are primarily determined by supply and demand for block space.

## Q4. Where does the difference in the coinbase output come from?

The difference comes from the **transaction fees** collected from the transactions included in the block. Therefore, the miner's total reward consists of the **block subsidy plus transaction fees**.

For block #840,000:

* Coinbase outputs: **4,075,061,499 sat**
* Block subsidy: **312,500,000 sat**
* Transaction fees: **3,762,561,499 sat**

Therefore:

`4,075,061,499 − 312,500,000 = 3,762,561,499 sat`

## Q5. What does the matching Merkle root prove?

The matching Merkle root shows that the transaction list produces exactly the same cryptographic commitment stored in the block header. Because cryptographic hashes are highly sensitive to changes and designed to resist collisions, changing a transaction would normally produce a different Merkle root.
