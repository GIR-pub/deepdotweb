---
title: "Introducing Bitrated: Bitcoin Arbitration Marketplace"
---

<article class="post-listing post-4254 post type-post status-publish format-standard has-post-thumbnail hentry  tag-arbitration tag-bitcoin tag-bitrated tag-introducing tag-marketplace">
Posted by: DeepDotWeb
<span>February 17, 2014</span>
    
<a href="/2014/02/17/bitrated-bitcoin-arbitration-marketplace/#comments">1 Comment</a></span>
</p>
<p>One of the most needed things in the DarkNetMarket Scene, is without a doubt, more Multisig based services, few days ago we were introduced to some <strong>open source and 100% free solution</strong> for arbitration services in bitcoin transactions using multisigs, the service is called <strong>Bitrated </strong>and it can be accessed here:</p>
<div class="box  info"><div class="box-inner-block"><i class="tieicon-boxicon"></i>
    Service Name:  <strong>Bitrated </strong><br />
    Service Url: <a href="https://www.bitrated.com/" target="_blank">https://www.bitrated.com/</a>
</div></div>
<p>It turned out that we are more or less familiar with the creator of this service and we pretty much know that they are reliable, so we decided doing a short interview with them and try to cover most of the frequently asked questions about this type of services with the hope it can be used to help reduced scamming, enjoy:</p>
<p><strong>How does it work? (2 way &#8211; 3 way)</strong></p>
<p>Basically, multi-signature, when used for arbitration, works by creating a 2-of-3 multisig that the payment is deposited to. There are three parties involved &#8211; the buyer, the seller and the arbitrator. Two of those three have to cooperate in order to release the payment.</p>
<p>To give a more tangible example, lets say Bob wants to buy something from Alice, and they both trust Trent as an arbitrator that can mediate disputes. Bob deposits his payment to a 2-of-3 multisig address with the<br />
    public keys of Bob, Alice and Trent. Alice can verify the payment was made and that the payment is &#8220;locked&#8221; in the multisig deposit, and ships the goods to Bob.</p>
<p>If Bob got the goods and he&#8217;s satisfied, he and Alice can be the 2-of-3 and release the payment from the multisig to Alice&#8217;s bitcoin address. In case of dispute, they both contact Trent and explain what happened. Then, either Bob+Trent can sign a transaction that issues a refund to Bob, or Alice+Trent can sign a transaction that moves the funds to Alice.</p>
<p><span style="text-decoration: underline;">The process on the website itself looks like that:</span></p>
<p>1. Bob goes to the &#8220;New transaction&#8221; page, enters the arbitrator (either a username of a registered arbitrator, or any public key) and the terms of the transaction (those are signed digitally by Bob and Alice, which later proves to Trent they both agreed to it)</p>
<p>2. Bob starts the transaction, and gets a link to share with Alice. When Alice enters, she confirms the arbitrator/terms by clicking &#8220;I agree&#8221;</p>
<p>3. Bob and Alice now see the transaction page with the multisig address, and Bob makes the payment.</p>
<p>4. Alice see the payment was received (by checking the multisig balance) and ships the product.</p>
<p>5. At this point, Bob or Alice can create a transaction that releases the funds, and ask the other party to approve it. If they get into a dispute, they have a link they can share with Trent, where he can be the 2nd party that approves transactions.</p>
<p><strong>How it can be used anonymously?</strong></p>
<p>Bitrated does not require an account or even an email address from buyer/sellers. The only details users provide are the terms of the transaction, which aren&#8217;t uploaded to the server and only shared via the URL the parties send to eachother.</p>
<p>Arbitrators can optionally sign up to have a public profile listed on the website, but they don&#8217;t have to. They can simply provide their public key to the buyer/seller and have them use it.</p>
<p><strong>I saw you mentioned in one of our previous mails it based *mostly* on client side, can you elaborate on this?</strong></p>
<p>Bitrated was built with a very strong security/privacy model. Almost everything happens client-side, with the server not being involved unless its 100% necessary. Private keys are created and used client side, transactions are constructed and signed client-side and the transaction data, including the terms, is only saved as part of the URL each party has and isn&#8217;t stored on the server at all.</p>
<div>The server is only involved in order to enable communication between clients. Its impossible to communicate between browsers directly, so a WebSocket server is used to send information between connected clients. The data that is sent via the server isn&#8217;t considered sensitive &#8211; just the the public key of the party joining the transaction and the partially-signed transaction request. Both of those are sent immediately to the other clients and discarded, with no permanent copy being saved. (in the future, we plan to <a href="http://github.com/shesek/bitrated/issues/1" target="_blank">encrypt that</a> end-to-end too)</div>
<p><strong>Elaborate on how you don&#8217;t touch the private keys and how it can be verified?</strong></p>
<p>Private keys are created and used client-side, and are never transmitted to the server. Each party gets a URL with his own private key embedded in the hash portion of the URL (after the &#8220;#&#8221;, which is not part of the http<br />
    request).</p>
<p>Bitrated is an open-source software that can be audited by anyone. It can be independently verified that the client-side code never sends sensitive information to the server, and it can be verified that the source served by<br />
    the webserver matches the code on Github.</p>
<p>In the future, we plan to provide a browser extension that does this automatically and ensures that the code coming from bitrated.com matches the code published on Github.</p>
<p><strong>Is there a possibility for the arbitrator to collect some fee? </strong></p>
<p>Fees are possible, but not currently handled specifically in Bitrated. There are basically two fees structures that I see people using:</p>
<ol>
<li>Fees for every transaction, which is the common model today. In this case, it should be paid as a separate transaction, before starting the multisig. The arbitrator should simply refuse to handle disputes where the fee wasn&#8217;t paid in advance.</li>
<li>Fees for disputed transactions only. Because the arbitrator doesn&#8217;t have to do anything when there&#8217;s no dispute, some of them choose to only charge for disputes. In this case, it can be paid from the multisig balance, where the arbitrator will simply refuse to sign transactions without his fees. Bitrated&#8217;s interface can be used to create a transaction sending some percentage of the balance as fees to the arbitrator, and the rest to the winning party.</li>
</ol>
<p><strong>Most people using Tor markets trying to avoid using JS, and your service is based on JS, how can this work together?</strong></p>
<p>I would be very careful about running Java and Flash, but I think JS is relatively safe to execute. Most of the web doesn&#8217;t function properly without JavaScript, and its necessary for a service like Bitrated that<br />
    relies heavily on client-side technology. Also, its open source and can be verified to not contain malicious code.</p>
<p><b>Who provides the arbitration?</b></p>
<p>Bitrated doesn&#8217;t provide the arbitration services themselves &#8211; the goal is to create a marketplace for arbitration services. We allow arbitrators to signup and offer their services for a fee, and let users choose which arbitrator they want to use.</p>
<p><strong>Why not make a n .onion domain for this service?</strong></p>
<p>.onion is good for websites that wants to conceal their identity. Bitrated is operated in the open and has a known owner (my name and my company&#8217;s name is listed in the About page), so I don&#8217;t think it&#8217;ll achieve much.</p>
<div class="box  info"><div class="box-inner-block"><i class="tieicon-boxicon"></i>
    Service Name:  <strong>Bitrated </strong><br />
    Service Url: <a href="https://www.bitrated.com/" target="_blank">https://www.bitrated.com/</a>
</div></div>
<p>Feel free to try it out and contact the service admin directly at <a href="/cdn-cgi/l/email-protection#630d0207021523010a1711021706074d000c0e" target="_blank"><span class="__cf_email__" data-cfemail="81efe0e5e0f7c1e3e8f5f3e0f5e4e5afe2eeec">[email&#160;protected]</span></a> if you have any issues, questions or suggestions for improvements.</p>
<p>We have also added this solution to the <a href="/2013/10/28/updated-llist-of-hidden-marketplaces-tor-i2p/">List of hidden marketplaces</a> as a related service</p>
</div>
<a href="https://www.deepdotweb.com/tag/arbitration/" rel="tag">arbitration</a> <a href="https://www.deepdotweb.com/tag/bitcoin/" rel="tag">bitcoin</a> <a href="https://www.deepdotweb.com/tag/bitrated/" rel="tag">bitrated</a> <a href="https://www.deepdotweb.com/tag/introducing/" rel="tag">introducing</a> <a href="https://www.deepdotweb.com/tag/marketplace/" rel="tag">marketplace</a></span> 
Updated: 2014-02-17
    
