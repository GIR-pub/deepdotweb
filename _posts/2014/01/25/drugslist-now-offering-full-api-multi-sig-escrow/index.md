---
title: "Drugslist Now Offering FULL API multi-sig escrow---

<article class="post-listing post-3644 post type-post status-publish format-standard has-post-thumbnail hentry  tag-api tag-drugslist tag-escrow tag-full tag-multisig tag-offering">
Posted by: DeepDotWeb
<span>January 25, 2014</span>
<span>in <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://www.deepdotweb.com/category/news-updates/" rel="category tag">News Updates</a></span>
<a href="/2014/01/25/drugslist-now-offering-full-api-multi-sig-escrow/#respond">Leave a comment</a></span>
</p>
<div class="clear"></div>
<div class="entry">
<p>It seems that some marketplaces are headed in the right direction, as we previously reported &#8211; the Drugslist marketplace, started <a href="/2014/01/19/drugslist-marketplace-now-offering-multisig-escrow/">offering a Multisig</a> escrow that is meant to help buyers and sellers protect themselves from the option of losing all their funds in case the marketplace gets shut down or the owner is deciding to scam everyone, but the problem with &#8220;regular&#8221; multisig (i.e Multi-sig Lite) escrow is that the marketplace still being the one who holds the private keys for the transaction &#8211; which means he can still &#8220;finalize&#8221; them and steal the funds.</p>
<p>In the new Multisig version that was launched by the marketplace owners, the marketplace does not hold the private keys &#8211; hence, cannot collect all the escrow funds and shut down the market, running away with everyone&#8217;s BTC, druglist currently being only the second market (out of about 30 marketplaces) to offer such functionality while the first one is  <a href="/2013/12/30/full-guide-how-to-access-i2p-sites-use-themarketplace-i2p/" target="_blank">themarketplace.i2p</a> (not exactly the same, but with the same bottom line), and this is how this works on the technical side, quoted from the Reddit post mad by the Admins:</p>
<p><strong>Visit Drugslist at this url</strong>: http://drugslisvdknitqd.onion/</p>
<p>===Quote===<br/>
    Hi everyone:</p>
<p>We are pleased to announced the launch of our new fully featured API escrow system as well as our new login page, which was updated due to user request.</p>
<p>Our site now offers, a fully featured API escrow, auto withdraw for vendors, 1% commission payments on any money spent by anyone whom you refer, a fully integrated forum and email system, client side pgp encryption and decryption as well as a very active customer support and development team.</p>
<p>Please understand that we know it is confusing and we will be creating an easier user interface this weekend. This is now the only fully featured API escrow available on any darknet TOR market. At the request of our users, we created this 2nd version multi-sig whereby drugslist only holds only one key (our own).</p>
<p><strong>**Please also be aware that you are still free to use the old multi-sig escrow system, which we&#8217;re calling it &#8220;multi-sig lite&#8221; if you prefer (which requires you to do nothing differently than normal- think Ebay). If you trust your vendor and wish to use FE, that is also an option. **</strong></p>
<p>The API is built on top of JSON-RPC (http://json-rpc.org) and can developed in pretty much any language. Anyone who’s interested can access it by using your drugslist username and password credentials and the URL http://drugslisvdknitqd.onion/api.</p>
<p>PHP Example with jsonRPCClient.php:</p>
<p>$user = ‘username’;<br/>
    $pass = ‘password’;<br/>
    $host = &#8221;drugslisvdknitqd.onion”;<br/>
    $port = 80;</p>
<p>$dl = new jsonRPCClient(&#8220;http://{$user}:{$pass}@{$host}:{$port}/api/&#8221;);</p>
<p>The system is very robust and offers developers the ability to a wide variety of operations on the site:</p>
<p>getInfo() — gets your profile information and balance and returns it in an array<br/>
    getBalance() — gets your balance and returns it as a string<br/>
    searchDrugs(search) — searches active drugslist listings and returns an<br/>
    array of drugs available for purchase<br/>
    getListing(id) — gets one particular listing by drugslist ID and returns<br/>
    an array of listing information<br/>
    getDrugsByVendor(vendor) &#8212; gets drugs by a vendor returned in an array<br/>
    getVendor(vendor) &#8212; gets information about vendor returned in an array<br/>
    listRegions() &#8211; lists available regions that drugslist uses for shipping destinations and origination<br/>
    getDrugsByOrigin(region) &#8212; get drugs by region returned in an array<br/>
    getDrugsByDestination(destination) &#8212; get drugs by destination returned in an array<br/>
    getDrugsByName(drug) &#8212; gets drugs by name returned in an array</p>
<p>We’re calling our old multi-sig escrow “Multi-sig Lite” and today we&#8217;re releasing our &#8220;full version&#8221; multi-sig escrow system that will enable buyers and vendors to have full control of their private keys with out drugslist intervention.</p>
<p>It works like this:</p>
<p>1. Buyer finds a vendor selling drugs that he wants to buy through searchDrugs(search).</p>
<p>2. Buyer sends a request to our API using requestForDrugs(array) with a JSON array built as:</p>
<p>&#8220;drugslistID&#8221; =&gt; drugslistID#<br/>
    &#8220;shippingID&#8221; =&gt; shippingMethodID#<br/>
    &#8220;quantity&#8221; =&gt; amount#,<br/>
    &#8220;delivery&#8221; =&gt; “[PGP ENCODED DELIVERY INSTRUCTIONS]”,<br/>
    “btc&#8221; =&gt; “[bitcoin address that the buyer controls and has the private key],</p>
<p>requestForDrugs(array) returns a string containing a drugslist transaction request number. At this point, it&#8217;s only a &#8220;request for drugs&#8221; as the buyer hasn&#8217;t sent money to anyone nor has the vendor approved the request (which will turn into an order).</p>
<p>3. Vendor sees request with getRequests() or via an email alert, and can do either of the following actions:</p>
<p>&#8211; Reject -&gt; cancels request with rejectRequest(id)</p>
<p>&#8211; Accept -&gt; approveRequest(id, “[bitcoin address that the vendor provides”])</p>
<p>4. Now, we have the buyer’s BTC and vendor’s BTC, so drugslist creates a multi-sig address using the three accounts. The buyer and vendor are given the instructions to re-create the multi-sig address on their end with our</p>
<p>multisigHelp() function.</p>
<p>Now drugslist gives the buyer:<br/>
    &#8211; the multi-sig address created with the three addresses<br/>
    &#8211; the three address so he can re-create it on his end<br/>
    &#8211; and asks to send money to it.</p>
<p>The buyer is given those in a returned array from getOrderStatus().</p>
<p>The funding window will close in 6 hours (and this variable will able to be chosen by the vendor) to prevent wide swings in market fluctuation.</p>
<p>5. Buyer sends money to BTC address and updates his transaction with: updateOrderStatus(id,txid) and drugslist creates the a raw transaction with 95%/5% split to the vendor and marketplace.</p>
<p>6. Vendor ships out package and the raw transaction using his favorite bitcoin client. The vendor then submits the signed transaction to drugslist with:</p>
<p>updateOrder(id, “[HEX]”)</p>
<p>7. When buyer receives package, he can do any of the following:</p>
<p>&#8211; send a command to the drugslist API asking drugslist to sign the transaction using our 1/3 vote<br/>
    -, log into drugslist and click “Received” package and again, drugslist signs the transaction using our 1/3 vote<br/>
    &#8211; or he can issue payment by getting the last signed transaction with getOrderStatus() and signing the transaction and submitting the transaction himself.</p>
<p>For users who want full documentation of our API, please visit our forum.</p>
<p>**** Please note that this is not required by any measure, and we still offer the easier, Multi-sig Lite and traditional escrow services. ******</p>
<p>**** The first implementation, Multi-sig Lite, is more than adequate for the majority of our users and is seamless and easy to use.******</p>
<p>As always, we are available to answer any questions/comments/concerns.</p>
<p>===Quote===</p>
<p>We support any market that will use these features to protect their buyers / vendors fund and show honest intents in these confusing times for the Dar knet markets. You can access Drugslist market at this url: http://drugslisvdknitqd.onion/</p>
<p>Or check out out <a href="/2013/10/28/updated-llist-of-hidden-marketplaces-tor-i2p/" target="_blank">hidden marketplace list</a> &#8211; for other marketplaces and updates.</p>
</div>
<a href="https://www.deepdotweb.com/tag/api/" rel="tag">api</a> <a href="https://www.deepdotweb.com/tag/drugslist/" rel="tag">drugslist</a> <a href="https://www.deepdotweb.com/tag/escrow/" rel="tag">escrow</a> <a href="https://www.deepdotweb.com/tag/full/" rel="tag">full</a> <a href="https://www.deepdotweb.com/tag/multisig/" rel="tag">multisig</a> <a href="https://www.deepdotweb.com/tag/offering/" rel="tag">offering</a></span> 
Updated: 2014-01-25
    
