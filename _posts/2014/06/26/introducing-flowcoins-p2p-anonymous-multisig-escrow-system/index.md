---
title: "Introducing Flowcoins: P2P &#038; Anonymous Multisig Escrow System"
---

<article class="post-listing post-6228 post type-post status-publish format-standard has-post-thumbnail hentry  tag-anonymous tag-escrow tag-flowcoins tag-introducing tag-multisig tag-p2p tag-system">
<<span>Posted by: <a href="https://www.deepdotweb.com/author/admin/" title="">DeepDotWeb </a></span>
    <span>June 26, 2014</span>
    
    <span><a href="https://www.deepdotweb.com/2014/06/26/introducing-flowcoins-p2p-anonymous-multisig-escrow-system/#comments">2 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>We are happy to introduce Flowcoins, an interesting new service providing P2P &amp; Multisig Escrow System operating both on the clearnet and in Tor. Which includes some new and innovative features:</p>
    <div class="box  info"><div class="box-inner-block"><i class="tieicon-boxicon"></i>
    <strong>Tor Version: </strong>k5wsvjf3m54cfl44.onion<br />
    <strong>Clearnet Version</strong>: https://flowcoins.li/
    </div></div>
    <p>As The admin told us:</p>
    <blockquote><p>flowcoins started as an idea that the internet needed better ways to handle P2P transactions with Bitcoin that weren&#8217;t attached to a storefront site.  We offer both our clearnet site and TOR site, depending on the sensitivity and need for privacy and anonymity that the transaction requires.  Any buyer and seller can now do business one-on-one with confidence that they are both protected by the escrow system.</p>
    <p>The best part about the site is the way the transactions actually work.  We didn&#8217;t want usernames, passwords, or permanent wallets, because those are places people can attack.  If everything is temporary, the opportunity for hacks iss minimized.</p>
    <p>Buyers receive a one-time URL from the seller that expires after being loaded.  It gives all necessary details for the transaction, including the Bitcoin address of the temporary wallet.  The buyer is then directed to their own status page, which can only be accessed initially from the one-time link.  So the seller can&#8217;t get access to the status page without expiring the link.  This allows the buyer and seller to update the status of the order (from funded to shipped to confirmed) without needing to login.  The URLs themselves are the login.</p>
    <p>If the buyer neglects to mark it complete, the transaction will autocomplete after a certain period of time that is initially set by the seller (from 10 to 30 days).  If the buyer disputes it, it enters arbitration and we work with both the buyer and seller to a reasonable resolution.</p>
    <p>After the transactions are fully complete, they are deleted, and no records are kept.</p></blockquote>
    <p>More details about the service:</p>
    <p><span style="text-decoration: underline;"><strong>In terms of Privacy and anonymity:</strong></span></p>
    <p>While BitCoin and similar currencies use a public ledger system, there are ways to remain anonymous when doing the transactions. FlowCoins attempts to increase anonymity through a few methods:</p>
    <ol>
    <li>The site loads with SSL encryption as the only option, and redirects any site URLs without SSL encryption (http) to our encrypted site (https).</li>
    <li>They offer a TOR-based option <strong>k5wsvjf3m54cfl44.onion</strong>, so the connection between your computer and theirs is obscured (<a href="https://flowcoins.li/faq.php#6">read more about TOR here</a>). Our TOR site also uses no javascript, preventing any potential security issues in JS from affecting your privacy or anonymity.</li>
    <li>The servers are located outside the US, and they have separate servers in different locations for the open web site and the TOR site, to prevent bottlenecking and reduce potential attack options (whether technological or legal).</li>
    <li>The service encourage users to communicate using PGP-encrypted information sent, and can block any plaintext communication from being sent. Emails sent from FlowCoins can be encrypted using public PGP keys that are input during transactions.</li>
    <li>Using email to approve transactions and receive a receipt of the transaction is optional, allowing for all fund releases and shipping updates to be made through single-use URLs that expire after the transaction is finished.</li>
    <li>After transactions are completed, they&#8217;re removed from the system and any transaction logs are deleted. This assures that even the site owners won&#8217;t have access to the transactional info after the funds are released.</li>
    </ol>
    <p><span style="text-decoration: underline;"><strong>Stability &amp; Security</strong></span></p>
    <p>The most common problem with cryptocurrency transaction websites is that they are vulnerable to DDoS attacks, locking users out of their accounts and preventing transactions from completing. as the site mentions:</p>
    <blockquote><p>We find this unacceptable. While DDoS attacks can happen and cause havoc, they can be mitigated through the use of network management techniques. But even if they are successful at taking down the site, all transactions done through FlowCoins don&#8217;t require our site to be operational to function.</p>
    <p>Our site uses multi-signature transactions, which hold the coins in a temporary wallet that needs two of three private keys to unlock (the buyer and seller, or the seller and flowcoins) (more on how multi-signature transactions work).</p></blockquote>
    <p>Finally, multi-signature transactions are more secure in general. They require 2 of 3 keys to release the funds from the escrow (so either you and the vendor, the vendor and the site, or you and the site), so an unscrupulous 3rd party would need to know at least two of the private keys to release the funds.</p>
    <p>I asked for some explanation about the multisig process about who generates the keys and if the site actually holds the multisig keys?</p>
    <div>
    <blockquote>
    <div>It does, but the way the system operates is assigning the keys to the status pages (each key is on a different server, one of which isn&#8217;t even known outside the internal system), so the system itself can&#8217;t access it, only the buyer can (unless we manually release it with our key, since the seller&#8217;s key releases it with the confirmation of shipping and that means two keys). Also, transactions can&#8217;t be altered unless the buyer disputes it anyway, even from the admin panel.  We can&#8217;t make any changes in admin to the transaction unless the buyer disputes it. Even I, one of the owners of the site, can&#8217;t change transactions unless there&#8217;s a dispute.  We set it up this way to minimize potential problems with the very remote possibility of the admin section being compromised.Oh and, if it wasn&#8217;t clear, each transaction has its own new keys created, so there are never repeats.</div>
    </blockquote>
    </div>
    <p><span style="text-decoration: underline;"><strong>What Are the plans for future developments of this service?</strong></span></p>
    <p>Right now our service is simple and currently limited to individual P2P transactions. But we have plans to help this grow and serve the cryptocurrency community even better.</p>
    <blockquote><p>Some desires for the future:</p>
    <ul>
    <li>We&#8217;ll soon be adding tumbling to flowcoins in order to add additional security and privacy to your transactions. Tumbling obscures the origin amount before being sent to the seller, allowing an additional layer of obfuscation to the transaction.</li>
    <li>API system that will allow open-web and TOR-based sites to use our service to process BitCoin (and other currency) transactions, while maintaining the same type of anonymity, privacy, and security that we demand.</li>
    <li>Reducing our fees. Yes, that&#8217;s right, our aim is to make these types of transactions more commonplace and accessible, and we also want you to keep more of your money. We will continue to analyze our revenue and see when we are able to lower our fees. Unfortunately there&#8217;s no timetable on this kind of thing, as it depends on many different factors, but rest assured that we will be keeping it in our minds.</li>
    <li>Mobile is a big potential area for coin transactions. But the vast majority of the mobile market – Android, iPhone, and Windows Phones – is locked from proper security vetting. This makes assuring PASS on mobile a difficult proposition, but one we believe is necessary for growth of this market. We will continue to work on it, and consider it an ongoing goal.</li>
    <li>Batch transactions for easy organization by the seller, while maintaining the same level of privacy and anonymity, is one of our top priorities, and we&#8217;ll be announcing something about that soon.</li>
    </ul>
    </blockquote>
    <p>Overall this sounds like a very promising service and we will be following and hoping to see how it grows. Check out for yourself:</p>
    <div class="box  info"><div class="box-inner-block"><i class="tieicon-boxicon"></i>
    <strong>Tor Version: </strong>k5wsvjf3m54cfl44.onion<br />
    <strong>Clearnet Version</strong>: https://flowcoins.li/
    </div></div>
    </div>
    <a href="https://www.deepdotweb.com/tag/anonymous/" rel="tag">anonymous</a> <a href="https://www.deepdotweb.com/tag/escrow/" rel="tag">escrow</a> <a href="https://www.deepdotweb.com/tag/flowcoins/" rel="tag">flowcoins</a> <a href="https://www.deepdotweb.com/tag/introducing/" rel="tag">introducing</a> <a href="https://www.deepdotweb.com/tag/multisig/" rel="tag">multisig</a> <a href="https://www.deepdotweb.com/tag/p2p/" rel="tag">p2p</a> <a href="https://www.deepdotweb.com/tag/system/" rel="tag">system</a></span> <span style="display:none" class="updated">2014-06-26</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name">
    
