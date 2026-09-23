## Q1: chainId is included in the signed transaction to prevent replay attacks across different Ethereum-compatible chains. A transaction signed for one chain cannot normally be replayed on another chain with a different chainId.

## Q2: Under EIP-1559, the target is 15M gas while the block gas limit is 30M. Because the current gas usage is only around 2%, far below the target, the protocol keeps decreasing the base fee by up to 12.5% per block, so it remains near the minimum level.

## Q3: The extra baseFeePerGas value is the projected base fee for the next block. A wallet can use this predicted value together with the desired priority fee to choose an appropriate maxFeePerGas.

## Q4: Not necessarily. If maxFee - baseFee is already greater than maxPriorityFee, increasing maxFee does not change the effective gas price because the priority fee is still the limiting factor.

## Q5: A basic ETH transfer has an intrinsic transaction cost of 21,000 gas. A failed transaction still costs gas because validators have already spent computational resources executing it before the failure occurred.

## Q6: The contract dispatcher reads the first 4 bytes of calldata and compares the selector with known function selectors, then jumps to the corresponding function code. Etherscan needs the contract ABI to interpret the remaining encoded bytes and decode them into the correct argument types.