---
title: "Cloakcoin Promises the Holy Grail of Cryptocurrency: Trustless Anonymity"
---

Posted by: DeepDotWeb

<span>July 17, 2014</span>

<p>Cryptocurrency enables users to wrest control of their money away from banks and governments, but without privacy features governments will often use their power to punish people who use currencies they do not approve of. Unfortunately, the crypto-community has thus far been unable to produce a viable system to give users complete privacy—until now. Cloakcoin, a new currency, has burst onto the scene with a promise to achieve the Holy Grail of cryptocurrency: complete trustless anonymity. To avoid the mishaps of its predecessors, Cloakcoin will implement a comprehensive privacy system consisting of anonymous transactions, stealth addresses, a secure multi-currency wallet with a built-in currency exchange, and a decentralized marketplace.</p>
<p>Satoshi Nakamoto created a monetary revolution when he launched Bitcoin in 2009. Bitcoin was the first digital currency to offer trustless peer-to-peer transactions. This increased privacy by eliminating the need to know the identity of the person you were transacting with. However, Bitcoin and most other cryptocurrencies operate on a public ledger, which means that although wallet address are not connected to specific identities, a careful observer can follow the money trail and figure out who the addresses belong to.</p>
<p><strong>The Problem with Deep Web Markets</strong></p>
<p>While Bitcoin’s pseudonymity satisfies many ordinary users, privacy advocates continued searching for a system that would facilitate completely anonymous transactions. For a time, deep web marketplaces like <a href="http://en.wikipedia.org/wiki/Silk_Road_(marketplace)" rel="nofollow">Silk Road</a> appeared to offer a secure, anonymous marketplace. However, the Silk Road, like other current deep web marketplaces, used centralized servers to store website data and user Bitcoins, which gave hackers a viable target for their attacks. Thus, the United States FBI was able to shut down Silk Road and seize over $3.6 million in user-owned Bitcoins as well as $28 million in Bitcoins believed to be owned by Silk Road operator Dread Pirate Roberts.</p>
<p><strong>The Problem with CoinJoin</strong></p>
<p>Centralized deep web markets are risky at best, but even if they presented no security risks they only offer anonymity for purchases made in their marketplace. Thus, they are not a viable option for the majority of people who want to send or receive money anonymously. To meet this remaining demand, several cryptocurrency developers have attempted to design wallets and coins that offer completely anonymous transactions. Darkcoin, SharedCoin, and DarkWallet are several prominent examples.</p>
<p>Darkcoin, etc. attempt to achieve anonymity by implementing <a href="https://bitcointalk.org/index.php?topic=279249.0" rel="nofollow">CoinJoin</a>, a coin-mixing protocol. Unfortunately, CoinJoin is not as secure as most people believed. For one thing, CoinJoin centralizes the anonymization process by using nodes to mix transactions. As the Cloakcoin <a href="https://bitcointalk.org/index.php?topic=637704.0">whitepaper</a> explains, this system contains inherent flaws.</p>
<blockquote><p>Those nodes may be altruistic or evil, they may log and capture de-anonymizing information, they may be controlled by adversarial entities, or they may simply be poorly maintained by inexperienced operators.</p></blockquote>
<p>Thus, CoinJoin kills the trustless nature of cryptocurrency by forcing you to trust the node operators tasked with mixing your coins.</p>
<p>However, the problems with CoinJoin do not stop there. Recently, security expert and <a href="http://anonymousbitcoinbook.com/" rel="nofollow"><em>Anonymous Bitcoin</em></a> author Kristov Atlas conducted a comprehensive <a href="http://www.coinjoinsudoku.com/advisory/" rel="nofollow">study of the CoinJoin-based SharedCoin</a>. Using CoinJoinSudoku, an analysis tool he designed, Atlas was able to identify relationships between transaction participants. Atlas’ research demonstrates that anyone with the proper tools and expertise can spy on Bitcoin transactions made through the SharedCoin wallet.</p>
<p>Atlas concluded that SharedCoin offered “only limited privacy to users due to weaknesses in its design.” Following Atlas’ study, SharedCoin conceded in a <a href="https://blog.blockchain.com/2014/06/10/sharedcoin-and-other-coinjoin-implementations-uses-and-limitations/" rel="nofollow">blog post</a> that their service was not designed for complete anonymity.</p>
<blockquote><p>If you want to truly hide transactions, SharedCoin and other implementations of CoinJoin are not for you – they are neither sufficient nor convenient. SharedCoin provides a basic level of enhanced privacy transaction but doesn’t guarantee anonymity nor was it intended to.</p></blockquote>
<p>Atlas plans to release the <a href="https://github.com/kristovatlas/coinjoin-sudoku" rel="nofollow">source code</a> for CoinJoinSudoku so others can adapt it to test the security of other CoinJoin-based applications such as DarkWallet and Darkcoin. If SharedCoin is correct, then these CoinJoin-based systems will fail the anonymity test as well.</p>
<p><strong>How is Cloakcoin Different?</strong></p>
<p>Cloakcoin is a new coin ecosystem designed to replace deep web marketplaces and CoinJoin applications. Cloakcoin is superior to previous attempts at anonymity because it offers comprehensive, trustless decentralized anonymity to cryptocurrency users. The three-pronged Cloakcoin ecosystem includes anonymous transactions using Proof of Stake Anonymity (CloakSend 2.0), a secure wallet with a built-in currency exchange, and a decentralized marketplace.</p>
<p>

<img src="https://info-gir.github.io/deepdotweb/imgs/2014/07/CloakSend.jpg" alt="CloakSend" width="690" height="475" srcset="/imgs/2014/07/CloakSend.jpg 690w, /imgs/2014/07/CloakSend-300x207.jpg 300w" sizes="(max-width: 690px) 100vw, 690px" />

<p><strong>Anonymous Transactions</strong></p>
<p>To avoid CoinJoin’s security holes, Cloakcoin created CloakSend, a transaction system that uses <a href="https://mega.co.nz/#!1c9UnKBI!BdEaoBuYDAr5F4nwltpYjYNOrZt7Jretk07eGc-oPDc">Proof of Stake Anonymity (PoSA)</a> to enable trustless anonymous transactions. CloakSend uses a two-phase anonymization process. As the whitepaper explains it:</p>
<blockquote><p>At the time that transactions are created, the wallet will go through a process of “electing” an anonymization service providing node to start transaction processing. The election process is a process of random selection from the pool of available anonymizing wallets. The transaction output is paired with the encoded destination and the raw transaction package is passed to the elected node…</p>
<p>The node will earn a fee for this service, and then redeem the input by recursing back to the election process, to elect a node for Phase 2. The node then constructs an anonymizing transaction package and broadcasts it to the elected Phase 2 node. Again in the Phase 2 pass the originator and recipient are not recorded; instead, the transaction occurs between the Phase 1 and Phase 2 nodes.</p></blockquote>
<p>Although the PoSA process adds a minor amount of latency to the system, it succeeds in achieving trustless decentralized anonymization for CloakSend transactions. In addition, <a href="http://sx.dyne.org/stealth.html">Stealth addresses</a> will allow for increased anonymity on the blockchain.</p>
<p><strong>Secure Wallet With Built-In Currency Exchange</strong></p>
<p>To increase user convenience, Cloakcoin also offers a secure wallet with a built-in currency exchange. Using the CloakTrade tab in the official Cloakcoin wallet, users can easily buy and sell Cloakcoins through the Bittrex exchange via an API code. This greatly simplifies the trading process for both new and experienced users.</p>
<p>

<img src="https://info-gir.github.io/deepdotweb/imgs/2014/07/cloaktrade.png" alt="cloaktrade" width="558" height="384" srcset="/imgs/2014/07/cloaktrade.png 863w, /imgs/2014/07/cloaktrade-300x206.png 300w" sizes="(max-width: 558px) 100vw, 558px" />

<p>However, storing coins on centralized exchanges is risky, so the CloakTrade developers are actively working on updates that will greatly increase CloakTrade security. These updates will integrate a multi-currency wallet into CloakTrade (beginning with Cloakcoin and Bitcoin) and establish a decentralized trustless exchange where you can buy and sell Cloakcoins from within your wallet. This update will enhance the security of your investment because your Cloakcoins will never remain on a centralized exchange, where they would be vulnerable to attacks from nefarious individuals.</p>
<p><strong>Decentralized Marketplace</strong></p>
<p>CloakTrade and CloakSend already give Cloakcoin a leg up over competing cryptocurrencies; however, Cloakcoin is about to release a feature that will settle the anonymity debate forever once the beta opens in about two weeks. Cloakcoin’s anonymous ecosystem will soon culminate in <a href="http://www.cloakcoin.com/onemarket.pdf">OneMarket</a>, a self-regulated, trustless decentralized marketplace where users can buy and sell goods anonymously using Cloakcoins.</p>
<p>

<img src="https://info-gir.github.io/deepdotweb/imgs/2014/07/Onemarket.png" alt="Onemarket" width="275" height="320" srcset="/imgs/2014/07/Onemarket.png 275w, /imgs/2014/07/Onemarket-258x300.png 258w" sizes="(max-width: 275px) 100vw, 275px" />

<p>OneMarket offers a decentralized alternative to popular online shopping websites like eBay and Amazon, as well as deep web marketplaces such as Silk Road and Agora. Like eBay and Amazon, you will be able to open your own storefront on OneMarket and sell your products to other OneMarket users. And as on deep web marketplaces, you will be able to buy and sell with complete anonymity.</p>
<p>However, OneMarket offers the added benefit of decentralization. OneMarket will not be stored on a third-party company server; it will utilize the Cloakcoin blockchain to host all the information necessary to operate the marketplace. Storing OneMarket on the blockchain makes it virtually unhackable because there is no single server for an attacker (including a government agency) to target. If the government managed to seize a computer running a node, it would not matter since every other computer with an open Cloakcoin wallet node would still be transmitting the OneMarket data through the Cloakcoin network. Moreover, payments will process through a trustless escrow system, ensuring that no third-party payment processor ever has full control of your coins.</p>
<p><a href="/imgs/2014/07/OneMarket2.png"/>
<p>You might be thinking OneMarket sounds a lot like <a href="http://openbazaar.org/">OpenBazaar</a>, the Bitcoin-based decentralized marketplace. Indeed, Cloakcoin’s OneMarket will operate quite similarly to OpenBazaar. OpenBazaar has the initial advantage of catering to the large Bitcoin community. However, OneMarket has the long-term advantage of existing in the Cloakcoin anonymous ecosystem. While OpenBazaar can offer a decentralized, anonymous marketplace, it cannot compensate for the lack of anonymity elsewhere in the Bitcoin ecosystem. People truly concerned about their privacy will gravitate to OneMarket.</p>
<p><strong>Get Started With Cloakcoin</strong></p>
<p>Cloakcoin is the clear monetary choice for the privacy conscious. No other currency can offer anything close to Cloakcoin’s comprehensive anonymization ecosystem. From its unique Proof of Stake Anonymity transaction system to its secure wallet that lets you buy Cloakcoins to OneMarket, Cloakcoin never ceases to protect your privacy. Cloakcoin truly has achieved the Holy Grail of anonymity.</p>
<p>To learn more about Cloakcoin or to get started today, check out the resources below.</p>
<p><strong>Cloakcoin Technical Details</strong></p>
<ul>
<li>Total coins: 4.5 million</li>
<li>PoW timespan: 7 days</li>
<li>Hashing Algorithm: x13</li>
<li>No pre-mine</li>
<li>PoS minimum stake age: 6 hours</li>
<li>Block time: 60 seconds</li>
<li>PoS 6%</li>
<li>Max age unlimited</li>
</ul>
<p><strong>Cloakcoin Resources</strong></p>
<ul>
<li><a href="http://www.cloakcoin.com" rel="nofollow">Official Website</a></li>
<li><a href="http://www.cloakcoin.com/#about" rel="nofollow">Whitepapers</a></li>
</ul>
<p>o   <a href="https://mega.co.nz/#!1c9UnKBI!BdEaoBuYDAr5F4nwltpYjYNOrZt7Jretk07eGc-oPDc" rel="nofollow">PoSA (CloakSend 2.0) Whitepaper</a></p>
<p>o   <a href="http://www.cloakcoin.com/onemarket.pdf" rel="nofollow">OneMarket Whitepaper</a></p>
<p>o   <a href="https://mega.co.nz/#!QE8BhBaZ!PbJF6DfYmcIPph8eN911XPiLZRzuTyCLDfJz2qi2kA4" rel="nofollow">Whitepaper FAQ</a></p>
<ul>
<li>Wallets: (<a href="http://www.cloakcoin.com/#wallets" rel="nofollow">Windows</a>, <a href="http://www.cloakcoin.com/#wallets">Mac</a>, <a href="http://www.cloakcoin.com/#wallets">Linux Source</a>)</li>
<li><a href="http://cloak.blockexplorer.cc/paperwallet/" rel="nofollow">Paper Wallets</a></li>
<li><a href="http://www.cloakcoin.com/#exchanges" rel="nofollow">Trade Cloak on These Exchanges</a></li>
<li><a href="http://www.cloak.blockexplorer.cc" rel="nofollow">Block Explorer</a></li>
<li><a href="http://coinmarketcap.com/currencies/cloakcoin/" rel="nofollow">Cloakcoin Market Cap</a></li>
<li><a href="http://cloaktalk.org" rel="nofollow">Cloaktalk Forums</a></li>
<li><a href="https://bitcointalk.org/index.php?topic=637704.0" rel="nofollow">Bitcointalk Thread</a></li>
<li><a href="https://twitter.com/CryptoPioneer" rel="nofollow">Official Twitter</a></li>
<li><a href="https://www.facebook.com/CloakCoin" rel="nofollow">Facebook</a></li>
<li><a href="http://reddit.com/r/CLOAK/" rel="nofollow">Reddit</a></li>
<li><a href="http://cloaked.eu/" rel="nofollow">Cloaked Proxy</a></li>
<li><a href="http://cloakfaucet.com/" rel="nofollow">CloakFaucet</a></li>
</ul>


Updated: 2014-07-17
    
