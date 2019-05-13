---
title: "BTC Transaction Malleability Theory: What Happened to SR 2.0 and Mt.Gox---

<article class="post-listing post-6769 post type-post status-publish format-standard has-post-thumbnail hentry tag-bitcoin tag-happened tag-malleability tag-mtgox  tag-theory tag-transaction">
<<span>Posted by: <a href="https://www.deepdotweb.com/author/iburnez/" title="">iBurnEZ </a></span>
    <span>August 21, 2014</span>
    
    <span><a href="https://www.deepdotweb.com/2014/08/21/bitcoin-transaction-malleability-theory-behind-happened-silkroad-2-0-mt-gox/#comments">2 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Before we get started I’d like to address the people who are about to flame the hell out of me for including Mt. Gox in the list of those affected by Bitcoin transaction malleability. The role this vulnerability played in the Mt. Gox shenanigans is debatable, but Trustwave researchers Ben Hayak and Daniel Chechik included Mt. Gox in their <a href="https://www.blackhat.com/us-14/briefings.html#bitcoin-transaction-malleability-theory-in-practice">Black Hat presentation “Bitcoin Transaction Malleability Theory in Practice</a>,” so I will also include it here.</p>
    <p>Bitcoin transaction malleability is the bug responsible for the theft of 4,500 Bitcoins (approx. $2.6 million) from the SilkRoad2.0. Mt. Gox will go down as one of the largest robberies in history, someone relieved the Bitcoin exchange of 850,000 Bitcoins ($465 million+). Investigators were able to recover about 200,000 Bitcoins but 650,000 ($355 million+) remain unaccounted for.</p>
    <p>The Bitcoin transaction malleability works in favor of the recipient of the transaction. As far as I’m aware this vulnerability has not been used in transaction between two private parties. The obvious targets were vulnerable Bitcoin exchanges and darkmarkets who store users Bitcoins in a central location. Attackers used Bitcoin transaction malleability to endlessly request Bitcoins from their accounts, eventually draining all of the Bitcoins from these targets.</p>
    <p>To understand how hackers were able to exploit the Bitcoin transaction malleability you need to have a basic understanding of how Bitcoin transactions work.</p>
    <p><strong>A laymen’s overview of Bitcoin transactions: </strong></p>
    <p>Bitcoin transactions require the same basic information you would expect in any other transaction. The following information is considered critical, once a transaction has been initiated making a change to any of this information will invalidate the transaction.</p>
    <ul>
    <li>Information identifying the sender (senders BTC wallet address)</li>
    <li>Sender’s signature to verify consent (sender’s private key)</li>
    <li>Amount of the transaction</li>
    <li>Information identifying the recipient (recipients Bitcoin wallet address)</li>
    <li>Recipient’s signature to verify their identity (recipient’s public key)</li>
    </ul>
    <p>The above information is combined with other “peripheral” information and hashed to generate a unique transaction ID which is used to track the transaction in the block chain. This is a key point about the Bitcoin transaction process, when you input the exact same information into a hashing algorithm you will always receive the exact same output (transaction ID). Changing the input information even slightly will generate an entirely new transaction ID.</p>
    <p>The critical information and transaction ID are then sent to the block chain (a historical ledger of all Bitcoin transactions) to be verified by Bitcoin miners. If all information is correct the transaction ID is verified and the funds are transferred. If any information is invalid the transaction ID will be rejected.</p>
    <p><strong>Bitcoin transaction malleability:</strong></p>
    <p>The theory behind Bitcoin transaction malleability is to intercept the transaction information before it reaches the block chain and make minor changes to the peripheral information that will generate a new transaction ID but not invalidate the transaction.</p>
    <p>Peripheral information includes the byte length of the transaction which can be changed while still maintaining the integrity of the data. For example if the byte length of the transaction is 2 bytes, it could also be written 002 bytes. When the new information is hashed this slight change generates an entirely new transaction ID.</p>
    <p><a href="/imgs/2014/08/standard-mutated-BTC.png"><img class="aligncenter  wp-image-6770" src="/imgs/2014/08/standard-mutated-BTC.png" alt="standard-mutated BTC" width="767" height="393" srcset="/imgs/2014/08/standard-mutated-BTC.png 933w, /imgs/2014/08/standard-mutated-BTC-300x154.png 300w" sizes="(max-width: 767px) 100vw, 767px"/></a></p>
    <p>This creates a race condition between the two transaction IDs, the mutated transaction ID must arrive to the block chain first to invalidate the original transaction ID. The block chain treats these transactions as duplicates and validates the first transaction ID and rejects the second transaction ID. When the mutated transaction ID is verified the funds are transferred to the recipient.</p>
    <p>The sender tracks the original transaction ID and has no idea a mutated transaction ID exists or it has been verified. The funds have been transferred from but there is no record of this activity from the senders account. Since original transaction ID has failed there is no reason to deduct anything from the balance of the senders account.</p>
    <p>Hopefully you can see where this is going, using the Bitcoin transaction malleability someone can, and did, endlessly withdraw funds from their exchange or darkmarket accounts and the balance will never change.</p>
    <p>The storage of Bitcoins in a central location is a fundamental flaw of Bitcoin exchanges and darkmarkets. Individual account balances are funded from the central Bitcoin cache, this allowed the attackers to drain the entire combined balance from a vulnerable target.</p>
    <p><strong>The fallout: </strong></p>
    <p>We must give credit where credit is due, Silk Road 2.0 made efforts to repay all users for the stolen Bitcoins by invoking a tax on all transactions. Essentially the community paid themselves back but the accounts affected by the theft were made whole.</p>
    <p>As for the Mt. Gox the investigation continues, we may never know what really happened or the exact numbers involved with the theft.</p>
    <p>Fortunatley, this particular bitcoin transaction malleability has been addressed and is no longer exploitable. But if there is one thing I learned at Black Hat this year is it is only a matter of time, nothing is secure, everything will be hacked, eventually.</p>
    <p>The tools used by Ben Hayak and Daniel Chechik to demonstrate this vulnerability can be found in the <a href="http://blackhat.com/us-14/archives.html">Black Hat USA 2014 archives</a>, or downloaded directly <a href="http://blackhat.com/docs/us-14/materials/us-14-Chechik-Malleability-Tool-Tool.zip">here</a>.</p>
    <p><a href="https://www.blackhat.com/us-14/briefings.html#bitcoin-transaction-malleability-theory-in-practice">https://www.blackhat.com/us-14/briefings.html#Bitcoin-transaction-malleability-theory-in-practice</a></p>
    <p><a href="http://blackhat.com/us-14/archives.html">http://blackhat.com/us-14/archives.html</a></p>
    <p><a href="http://blackhat.com/docs/us-14/materials/us-14-Chechik-Malleability-Tool-Tool.zip">http://blackhat.com/docs/us-14/materials/us-14-Chechik-Malleability-Tool-Tool.zip</a></p>
    </div>
     <a href="https://www.deepdotweb.com/tag/bitcoin/" rel="tag">bitcoin</a> <a href="https://www.deepdotweb.com/tag/happened/" rel="tag">happened</a> <a href="https://www.deepdotweb.com/tag/malleability/" rel="tag">malleability</a> <a href="https://www.deepdotweb.com/tag/mtgox/" rel="tag">mtgox</a> <a href="https://www.deepdotweb.com/tag/silkroad/" rel="tag">silkroad</a> <a href="https://www.deepdotweb.com/tag/theory/" rel="tag">theory</a> <a href="https://www.deepdotweb.com/tag/transaction/" rel="tag">transaction</a></span> <span style="display:none" class="updated">2014-08-21</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/iburnez/" title="Posts by iBurnEZ" rel="author">iBurnEZ</a></strong></div>
    
