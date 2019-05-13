---
Coinspermia : Unchaining Cryptocurrency
---
<article class="post-listing post-18256 post type-post status-publish format-standard has-post-thumbnail hentry  tag-coinspermia tag-cryptocurrency tag-unchaining">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>February 21, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/02/21/coinspermia-unchaining-cryptocurrency/#comments">1 Comment</a></span>
    </p>
    <div class="clear"></div>
    
    <p>Even though the <a href="https://www.deepdotweb.com/2015/10/12/we-love-the-blockchain-not-the-bitcoin-the-currency/">blockchain technology</a> has introduced the world to a revolutionary concept of digital currencies that can entirely transform the global financial system, the scalability of bitcoin, and many other cryptocurrencies, is hindering mass adoption of the world&#8217;s first decentralized currencies. Bitcoin&#8217;s proof-of-work (PoW) scheme promotes immutability and consensus formulation; however, it represents a process that consumes enormous time and energy.</p>
    <p><a href="https://www.researchgate.net/publication/312579108_Coinspermia_a_cryptocurrency_unchained">Coinspermia</a> represents a fairly different cryptocurrency approach as transactions are simultaneously seeded through a network, formed by peer nodes, in a manner that bolsters reliably secure financial operations, high speed of transfer of coins from the sender to the recipient and prevention of <a href="https://www.deepdotweb.com/2016/12/31/two-new-models-double-spending-attacks-bitcoins-blockchain/">double spending attacks</a>. On the other hand, coinspermia retains some of bitcoin&#8217;s features including utilization of cryptographic addresses and transaction input/outputs, yet no proof-of-work (PoW) process is needed to validate transactions. Alternatively, confirmation of a transaction takes place when a sufficient portion of the nodes across the network validate the transaction, which occurs only when the transaction successfully propagates across the network.</p>
    <p><img class="wp-image-18260 aligncenter" src="/imgs/2017/02/coinspermia-3-png.png" alt="Coinspermia 3.PNG" srcset="/imgs/2017/02/coinspermia-3-png.png 471w, /imgs/2017/02/coinspermia-3-png-283x300.png 283w" sizes="(max-width: 471px) 100vw, 471px" /></p>
    <p><strong>An Overview of Coinspermia:</strong></p>
    <p>Coinspermia is comprised of a peer-to-peer (P2P) decentralized network of nodes. The connection among nodes is random which is a crucial factor in coinspermia&#8217;s protocol.</p>
    <p>The following represents the input and output of a coinspermia transaction:</p>
    <p>Input:</p>
    <p>a- ID of the proceeding transaction output</p>
    <p>b- Proceeding transaction output ID: signature of the payer</p>
    <p>Output:</p>
    <p>a- ID of transaction output</p>
    <p>b- Transaction destination address</p>
    <p>c- Amount of paid coins</p>
    <p>Transactions are recorded onto a public ledger that is stored onto all nodes across the network. To minimize memory usage and increase speed, only outputs of transactions that include unspent coins utilize fast memory. Full transaction data is added to an archive to promote future audit and restoral.</p>
    <p>For a transaction to be successfully executed, its inputs have to match the unspent outputs of the proceeding transaction which are found on the ledger via means of universally unique identifiers (UUIDs). Just like bitcoin, the proceeding output address must validate the input&#8217;s signature. Also, the quantities of the input and output coins have to be equal. In case the transaction is valid, the matching proceeding outputs are excluded from the unspent store and the new outputs are recorded. Whenever a matching proceeding output isn&#8217;t found, the transaction will be marked as &#8220;invalid&#8221;. This can occur if either a proceeding transaction never took place, or the coins have been already sent (double spending attempt).</p>
    <p><strong>Consensus:</strong></p>
    <p>A transaction is initially sent to a network node from the sender of the coins and then broadcast to the network, from the entry node, beginning with its near neighbors, with the expectation of finding out either proceeding transactions or the valid absence of them. For achieving a reliable performance, the probability of discovering such findings has to be high.</p>
    <p>The below figure illustrates the immediately connected network nodes for a &#8220;blue&#8221; transaction that needs to match one of the transactions within the nodes immediately updated by a proceeding &#8220;green&#8221; transaction. For instance, a blue user may want to spend the coins which were received from a green user. In such situation, the red node represents an immediate neighbor which would be involved in both the green and blue transactions. Once discovered, the immediate blue neighbors can be quickly synchronized with the proceeding green transaction to confirm the blue transaction. Whenever a double spend is attempted, the red node will exclude the proceeding transaction due to the fact that it only supports the double spending transaction attempt.</p>
    <p><img class="wp-image-18261 aligncenter" src="/imgs/2017/02/coinspermia-1-png.png" alt="Coinspermia 1.PNG" srcset="/imgs/2017/02/coinspermia-1-png.png 559w, /imgs/2017/02/coinspermia-1-png-300x177.png 300w" sizes="(max-width: 559px) 100vw, 559px" /></p>
    <p>Finally, the transaction propagates throughout the entire network. Nevertheless, to promote low latency, a user is notified of completion of a transaction when a sufficient percentage of the nodes across the network validate the transaction. According to Coinspermia&#8217;s protocol, the entry node, along with its immediate neighbors, comprise a sufficient percentage of the network&#8217;s nodes. For this to operate swiftly, the probability of discovering an intersecting node has to be relatively high. The following formula calculates the probability of finding one or more of <strong><em>K </em></strong>items in <strong><em>N </em></strong>nodes with <strong><em>S </em></strong>samples:</p>
    <p><img class="wp-image-18262 aligncenter" src="/imgs/2017/02/coinspermia-2-png.png" alt="Coinspermia 2.PNG" /></p>
    <p>Where <strong><em>N </em></strong>is the number of nodes, <strong><em>K</em></strong> is the number of nodes that contain search items (proceeding green transaction), <strong><em>S </em></strong> is the number of random samples (present blue transactions) and <strong><em>P</em></strong> is the probability of discovering an item.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/coinspermia/" rel="tag">coinspermia</a> <a href="https://www.deepdotweb.com/tag/cryptocurrency/" rel="tag">cryptocurrency</a> <a href="https://www.deepdotweb.com/tag/unchaining/" rel="tag">unchaining</a></span> <span style="display:none" class="updated">2017-02-21</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

