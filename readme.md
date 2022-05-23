## An NFT mint script by interacting with smart contract
### The script was originally made for minting a free mint project named MoonBirdAI, in which some config info and methods are made to be compatible with this project, feel free to modify these methods to be compatible with other project, I will point them out in the following page where you should modify to make it work for your project.
---
### Config.py

**Everything in this file should be modified**

<br>
a. Get your INFURA_SECRET KEY in https://infura.io by creating a new project
<br>
b. Private key in your metamask wallet, DONT EVER SHARE THIS WITH ANYONE. (*If you wanna give up all your money, just transfer them to me, my wallet address is 0xaA05570cA9d4b64161c37F958bf8A1E0977B1BB0, much appreciated!*)
<br>
c. WALLET ADDRESS, copy it from your metamask wallet
<br>
d. Contract address, it could normally be found in project website
<br>
e. NFT_abi, could be found in etherscan.contract -> code -> Contract ABI -> COPY/PASTE
<br>
<br>
---
### NFT_mint.py

NB. ther is no gas limit param set up yet, will update later.
<br>
**Methods should be updated:**
1. `number_of_tokens` in line 44
2. `network = 'mainnet'` if you are minting an NFT other than eth
3. `mint = nft_mint.functions.giveAway` in line 28, function `giveaway` should be updated, find the right function from their contract, contract->read_contract->mint***
4. `price = nft_mint.functions.MBAIPrice().call()` in line 23, updated `MBAIprice`, find the price of each token on contract->read_contract->***Price

