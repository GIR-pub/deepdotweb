---
A Novel System for Secure Offline Bitcoin Payments
---
<article class="post-listing post-19401 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news category-news-updates tag-bitcoin tag-offline tag-payments tag-secure tag-system">
    
    <div class="post-inner">
    
    
    <p class="post-meta">
    
    <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    
    
    <span>April 26, 2017</span>
    <span>in <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://www.deepdotweb.com/category/news-updates/" rel="category tag">News Updates</a></span>
    
    <span><a href="https://www.deepdotweb.com/2017/04/26/novel-system-secure-offline-bitcoin-payments/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    
    <div class="entry">
    
    <p>Bitcoin is inarguably the most successful cryptocurrency so far, when market capital and growing popularization are considered. Users have to have online access to be able to initiate transactions to spend their bitcoins. A certain amount of time is required for the transaction to be successfully confirmed and validated (20-30 minutes in most cases). However, a large number of real world scenarios require immediate payments that are initiated offline, but offline bitcoin payments raise a number of serious security challenges, as the receiver of the coins can never verify that the payment has actually been received without accessing the bitcoin network via the internet. Furthermore, even immediate forms of online payments have been proven to be vulnerable to <a href="https://www.deepdotweb.com/2016/12/31/two-new-models-double-spending-attacks-bitcoins-blockchain/">double spending scenarios</a>.</p>
    <p>A <a href="http://dl.acm.org/citation.cfm?id=3052980">recently published paper</a> presented the first ever solution that can facilitate secure offline bitcoin payments throughout instances when immediate payments have to be immediately accepted (e.g. vending machines, mobile ticketing&#8230;.etc). The proposed approach is based on using an offline wallet and implementing a number of new security mechanisms that can shield transactions against double spending attacks and verify their validity within an offline setting. These new mechanisms aim at probabilistic security that ensures that the probability of launching an attack is lower than the required threshold for success. The developers of the solution provided a risk and security analysis, in addition to security parameters for various forms of adversaries. They also eliminated remaining risks via excluding misbehaving wallets.</p>
    <p>The solution was implemented on Android mobile clients to instantiate an offline bitcoin wallet via a microSD security card. The implementation showed that using a popular platform, such as Android, to smoothly integrate this solution is possible and that online and offline bitcoin transactions can coexist in secure settings. An alternative implementation approach is also proposed for the offline wallet that does not rely on secure hardware; instead, it is based on a deposit framework that is managed by the bitcoin network.</p>
    <p><strong>The Offline Payment Scenario:</strong></p>
    <p>The new solution is comprised of three phases as shown on the below figure;</p>
    <p>i. Online bitcoin preloading</p>
    <p>ii. Offline bitcoin payment</p>
    <p>iii. Online redemption of coins and revocation of double spending attacks</p>
    <p><img class="wp-image-19415 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/04/word-image-104.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/04/word-image-104.png 630w, https://www.deepdotweb.com/wp-content/uploads/2017/04/word-image-104-300x247.png 300w" sizes="(max-width: 630px) 100vw, 630px" /></p>
    <p>Throughout the first phase, the sender of the coins <strong><em>X</em></strong> creates a pre-loading bitcoin transaction <strong><em>T<sub>1</sub></em></strong> (step 1) which leads to transfer of some coins from his/her main bitcoin account <strong><em>x</em></strong> to the account of the offline wallet<strong><em> w</em></strong>, so <strong><em>w</em></strong>&#8216;s balance became positive. This is achieved via an online bitcoin transaction, for which the nodes of the network will create <strong><em>n</em></strong>-transaction confirmation <strong><em>n-T<sub>l</sub> </em></strong>. Throughout the second phase, the sender of the coins <strong><em>X</em></strong> communicates with <strong><em>W</em></strong> requesting it to create an offline bitcoin transaction <strong><em>T<sub>0</sub></em></strong> with the amount destined to be sent to the account <strong><em> y</em></strong> (step 3). Throughout the third phase, the receiver of the coins <strong><em>Y</em></strong> will redeem the coins he/she received offline via publishing <strong><em>T<sub>0</sub></em></strong> to the blockchain (step 4) and occasionally obtaining transaction&#8217;s confirmation (step 5). The confirmation(s) of transactions will be issued, only when no double spending attack attempts have been detected against <strong><em>T<sub>0</sub>. </em></strong>If not, the receiver of the payment <strong><em>Y</em></strong> will initiate a double spending revocation bitcoin procedure, which includes initiating a double spending revocation transaction <strong><em>T<sub>r </sub></em></strong> (step 6), broadcasting it to the blockchain and obtaining its confirmations <strong><em>n-T<sub>r</sub></em></strong> (step 7).</p>
    <p><strong>The New Solution, CoinBlesk and Green Addresses:</strong></p>
    <p>The new solution is somehow similar to CoinBlesk, which is a mobile payment platform that facilitates fast bitcoin payments. Similarly to this solution, CoinBlesk facilitates direct payments from the sender to the receiver (via NFC). Nevertheless, CoinBlesk requires at least one party has to have an online connection, so it does not address the problem this new solution solves. Another solution, which is known as Green Addresses, solves the problem of &#8220;confirmation delay&#8221; via the introduction of a trusted intermediary, or third party, that aids in the guarantee of zero confirmation transactions. Generally speaking, Green Addresses present a striking evidence that third parties can be accepted within Bitcoin&#8217;s ecosystem, yet it cannot solve the problem of offline payments.</p>
    <p>By far, this new solution is the first ever payment system to promote offline bitcoin payments; thus, opening the door for the implementation of bitcoin payments in a myriad of sectors including ticketing for public transportation, events, and concerts.</p>
    
    
    </div><!-- .entry /-->
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/bitcoin/" rel="tag">bitcoin</a> <a href="https://www.deepdotweb.com/tag/offline/" rel="tag">offline</a> <a href="https://www.deepdotweb.com/tag/payments/" rel="tag">payments</a> <a href="https://www.deepdotweb.com/tag/secure/" rel="tag">secure</a> <a href="https://www.deepdotweb.com/tag/system/" rel="tag">system</a></span>				<span style="display:none" class="updated">2017-04-26</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    
    
    </div><!-- .post-inner -->
</article><!-- .post-listing -->

