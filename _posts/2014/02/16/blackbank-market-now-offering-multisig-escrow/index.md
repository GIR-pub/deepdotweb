---
title: "BlackBank Market Now Offering MultiSig Escrow"
---

Posted by: DeepDotWeb
<span>February 16, 2014</span>

<p>We have Just found out that BlackBank Market has implemented the use of Multisig transactions, once every market that does that in the correct way deserve our support, you can find the market at this address:  http://omo6o7akcampiryq.onion</p>
<p>Or at our <a href="/2013/10/28/updated-llist-of-hidden-marketplaces-tor-i2p/">list of marketplaces</a></p>
<p>We have pasted here the fully usage guide of their multisig, from the wiki page at this url: http://u5z75duioy7kpwun.onion/wiki/index.php/Multi-Sig_Escrow</p>
<p>You can discuss this new feature at their reddit thread here: www.reddit.com/r/DarkNetMarkets/comments/1y1twm/blackbank_market_small_updates_multisig_escrow/</p>
<h2>Introduction</h2>
<p>After researching several methods and implementations of Multi-Sig Escrow, there has been a compromise in terms of ease of use and security. In order to provide the best experience, Multi-Sig security applies only to Escrow, as this is the only time funds would be inaccessible. In every other case, BlackBank should not be used to store funds in the system.</p>
<p><a href="/imgs/2014/02/1.jpg"><img class="aligncenter size-full wp-image-4232" alt="1" src="/imgs/2014/02/1.jpg" width="400" height="232" srcset="/imgs/2014/02/1.jpg 400w, /imgs/2014/02/1-300x174.jpg 300w" sizes="(max-width: 400px) 100vw, 400px"/></a></p>
<ol>
<li>Buyer deposits BTC into BlackBank and after 6 confirmations can make purchases.</li>
<li>If the item has escrow, the Buyer enters a <b>public key</b>. At this point, the funds are not locked yet and can be cancelled and withdrawn at anytime.</li>
<li>If the Vendor accepts the escrow, the vendor enters his/her <b>public key</b>.</li>
<li>BlackBank automatically will generate it&#8217;s own <b>public key</b> and create a multisig BTC address to lock the funds.</li>
<li>In order to access and finalize the order, 2 of 3 keys are required:
<ol>
<li>Buyer + BlackBank <i>(ex. finalize order/dispute)</i></li>
<li>Vendor + BlackBank <i>(ex. dispute)</i></li>
<li>Buyer + Vendor <i>(ex. BlackBank unavailable)</i></li>
</ol>
</li>
<li>When an order is finalized, <b>the funds will not return to BlackBank</b>. <b>The funds will go directly to the address provided</b> during purchase or accepting an order.</li>
</ol>
<h2>Create a Public and Private Key Pair</h2>
<p>Before you make a purchase, you will need a public and private key pair. You will use the <b>public key</b> to &#8220;lock&#8221; the funds and a <b>private key</b> to &#8220;unlock&#8221; the funds later. The easiest way to create a public and private key is to go to <a href="http://brainwallet.org/" rel="nofollow">brainwallet.org</a> <i>(note: you will need to use Javascript here)</i>:</p>
<ul>
<li><a href="http://brainwallet.org/" rel="nofollow">brainwallet.org</a></li>
</ul>
<p><a href="/imgs/2014/02/2.jpg"><img class="aligncenter size-full wp-image-4233" alt="2" src="/imgs/2014/02/2.jpg" width="400" height="589" srcset="/imgs/2014/02/2.jpg 400w, /imgs/2014/02/2-204x300.jpg 204w" sizes="(max-width: 400px) 100vw, 400px"/></a></p>
<h2>Buyer&#8217;s Guide</h2>
<h3>Making a Multi-Sig Escrow Purchase</h3>
<h4>Purchasing an Item</h4>
<p>After you have your public and private key pair, you will use your public key to make a purchase. Store your private key someplace safe; keep it with your public key for cross-reference. After selecting the options, enter your <b>public key</b> and <b>refund address</b> to purchase:</p>
<p><a href="/imgs/2014/02/3.jpg"><img class="aligncenter size-full wp-image-4234" alt="3" src="/imgs/2014/02/3.jpg" width="529" height="448" srcset="/imgs/2014/02/3.jpg 529w, /imgs/2014/02/3-300x254.jpg 300w" sizes="(max-width: 529px) 100vw, 529px"/></a></p>
<h4>Cancel Purchase</h4>
<p>If a purchase has not been accept by the vendor yet, you can always cancel the purchase:</p>
<p><a href="/imgs/2014/02/4.png"><img class="aligncenter size-full wp-image-4235" alt="4" src="/imgs/2014/02/4.png" width="600" height="115" srcset="/imgs/2014/02/4.png 600w, /imgs/2014/02/4-300x58.png 300w" sizes="(max-width: 600px) 100vw, 600px"/></a></p>
<h4>Releasing Escrow</h4>
<p>After you are satisfied with your item or service, you release your escrow by entering your private key:</p>
<p><a href="/imgs/2014/02/5.jpg"><img class="aligncenter size-full wp-image-4236" alt="5" src="/imgs/2014/02/5.jpg" width="379" height="195" srcset="/imgs/2014/02/5.jpg 379w, /imgs/2014/02/5-300x154.jpg 300w" sizes="(max-width: 379px) 100vw, 379px"/></a></p>
<h2>Guide for Vendors</h2>
<h3>Handling Multi-Sig Purchases</h3>
<h4>How to Accept a Purchase</h4>
<p>When accepting a purchase, please enter your public key and a withdrawal address:</p>
<p><a href="/imgs/2014/02/6.jpg"><img class="aligncenter size-full wp-image-4237" alt="6" src="/imgs/2014/02/6.jpg" width="400" height="181" srcset="/imgs/2014/02/6.jpg 400w, /imgs/2014/02/6-300x136.jpg 300w" sizes="(max-width: 400px) 100vw, 400px"/></a></p>
<h4>Options after accepting a purchase</h4>
<p>After a purchase is made, there will be additional details provided:</p>
<ul>
<li><b>Public Key:</b> for reference on which private key to use</li>
<li><b>Manual FE Code:</b> for manually finalizing outside of BlackBank</li>
<li><b>Payment Address:</b> make sure this is correct as this is where the payment will go when the funds are released</li>
</ul>
<p><a href="/imgs/2014/02/7.jpg"><img class="aligncenter size-full wp-image-4238" alt="7" src="/imgs/2014/02/7.jpg" width="600" height="270" srcset="/imgs/2014/02/7.jpg 600w, /imgs/2014/02/7-300x135.jpg 300w" sizes="(max-width: 600px) 100vw, 600px"/></a></p>
<h2>Finalizing Outside of BlackBank</h2>
<p>In the event that BlackBank is unavailable to finalize an order, every step has been taken to make it easy for the buyer and vendor to finalize outside of the market. A finalize early code is provided to both the buyer and vendor. At this time, there is only a finalize to vendor code. If there is demand for a refund code, please let me know in the forum and I will implement it.</p>
<h3>How to use the Manual FE Code</h3>
<p><b>Step-by-Step Guide:</b></p>
<p>1. After you have copied the code, it will look like the below:</p>
<div>
<p><code>signrawtransaction '010000000125fbb54693f306f3b57a6e72772af2a55ea9f2dc8269ae67a08d9064d2abb6170100000000ffffffff01fb9a1000000000001976a9146f8eeafa1e979a730994c644dc8484c9493271f388ac00000000' '[{"txid":"17b6abd264908da067ae6982dcf2a95ea5f22a77726e7ab5f306f39346b5fb25","vout":1,"scriptPubKey":"a914069d1d7e42b361e76861b4782c2978d8b09b6c7a87","redeemScript":"5221024de3191645cc5d7d6bf1326fa3ae8e154cdc65544c9f012b491017b6c800824e21024de3191645cc5d7d6bf1326fa3ae8e154cdc65544c9f012b491017b6c800824e2102a96896a9c9bd5ee6e2adf8bcf6d7954c6b44b811f7fdd3a86f84b0cd632fdff153ae"}]' '["PRIVATE_KEY_A","PRIVATE_KEY_B"]'<br/>
</code></p>
</div>
<p>2. Replace PRIVATE_KEY_A and PRIVATE_KEY_B with the <b>Buyer</b> and <b>Vendor</b> private keys.</p>
<p>3. Using the official Bitcoin-QT Wallet Client, select <b>&#8220;Help&#8221;</b> followed by <b>&#8220;Debug window&#8221;</b>:</p>
<p><a href="/imgs/2014/02/8.jpg"><img class="aligncenter size-full wp-image-4239" alt="8" src="/imgs/2014/02/8.jpg" width="600" height="408" srcset="/imgs/2014/02/8.jpg 600w, /imgs/2014/02/8-300x204.jpg 300w" sizes="(max-width: 600px) 100vw, 600px"/></a></p>
<p>4. Select the &#8220;Console&#8221; tab and enter the code with the Private Keys from both Vendor and Buyer into the input box at the bottom and submit.</p>
<p>5. You will get the following result:</p>
<p><a href="/imgs/2014/02/9.jpg"><img class="aligncenter size-full wp-image-4240" alt="9" src="/imgs/2014/02/9.jpg" width="600" height="359" srcset="/imgs/2014/02/9.jpg 600w, /imgs/2014/02/9-300x180.jpg 300w" sizes="(max-width: 600px) 100vw, 600px"/></a></p>
<p>6. If &#8220;complete&#8221; is <b>false</b>, this means that one of the Private Keys is incorrect. If complete is <b>true</b>, copy the &#8220;hex&#8221; portion of the code.</p>
<div>
<p><b>Ex.</b><br/>
<code>{ "hex" : "01000000019cafae171c2d59ccc6dede75082ba20731d7f6892b7579559e5407b7117fe0d001000000fc00473044022053cb98f7502d78bf6fc23665c335697d69668f63afaf12f8ecf829a5ce7e8ae8022028322eb6df332fbd8f7c4e14b5f2c53f11a7962d7947be6bc0afab25c20fcaaf0147304402200ca1d96d927179d55e0877c0b650e73cc60c1bd61b046e0765ed2c1180551343022014b2dd9ba9c1aed8b62a3f52047dbc38c2063118f5d85306e2ebd08bbab665a6014c6952210229436df993475b592c7e5928e5f82e65f2549be4c78bece5c871122399e99a972103841bc1870615a9b8897335eabf4dbc63effa9d3f80913405bced7c12a5d88f7f2103c78ce13560f0c2fbaab36c9c9307250565013324ae8354b6d146ff65fc67f4da53aeffffffff0140420f00000000001976a914097e8a1b2ad02225c98750f463513b5966ba04c088ac00000000", "complete" : true }</code></p>
</div>
<p>7. After you copied the code, you will now finalize the transaction by sending it. Use the console again and enter the following command:</p>
<p>sendrawtransaction [<b>the hex code</b>]
<div>
<p><b>Ex.</b><br/>
<code>sendrawtransaction 01000000019cafae171c2d59ccc6dede75082ba20731d7f6892b7579559e5407b7117fe0d001000000fc00473044022053cb98f7502d78bf6fc23665c335697d69668f63afaf12f8ecf829a5ce7e8ae8022028322eb6df332fbd8f7c4e14b5f2c53f11a7962d7947be6bc0afab25c20fcaaf0147304402200ca1d96d927179d55e0877c0b650e73cc60c1bd61b046e0765ed2c1180551343022014b2dd9ba9c1aed8b62a3f52047dbc38c2063118f5d85306e2ebd08bbab665a6014c6952210229436df993475b592c7e5928e5f82e65f2549be4c78bece5c871122399e99a972103841bc1870615a9b8897335eabf4dbc63effa9d3f80913405bced7c12a5d88f7f2103c78ce13560f0c2fbaab36c9c9307250565013324ae8354b6d146ff65fc67f4da53aeffffffff0140420f00000000001976a914097e8a1b2ad02225c98750f463513b5966ba04c088ac00000000<br/>
</code></p>
</div>
<p>8. The transaction has now been manually finalized. This will provide you with a transaction ID; you can share it with the other party as reference.</p>
<p>You can find BlackBank Market on our list of <a href="/2013/10/28/updated-llist-of-hidden-marketplaces-tor-i2p/">hidden marketplace</a></p>

Updated: 2014-02-16
    
