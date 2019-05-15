---
title: "Tutorial: Multi-signature Transactions with Electrum 2.0"
---

Posted by: DeepDotWeb 

<span>March 21, 2015</span>

<p><strong><em>A great tutorial posted originally <a href="http://www.reddit.com/r/DarkNetMarkets/comments/2znvmi/guide_multisignature_transactions_with_electrum_20/">on Reddit</a> by /r/darknetmarkets mod <a href="http://www.reddit.com/user/galaxyandspace">galaxyandspace</a>, Edited with the images for your convenience:</em></strong></p>
<p>Greetings Ya&#8217;ll! It&#8217;s time to learn how to multisig!!!!</p>
<p>Recently, Electrum 2.0 came out, along with the ability to create 2 of 3 multisig wallets. We will be walking through how to complete this process, both from the buyers end and vendors end, both covering the mechanics and whats happening. The market admins can figure it out for themselves what to do. We will cover what goes down in the events of a normal transaction, and in the events of a dispute.</p>
<p><strong>If you don&#8217;t get this guide the first time through, give it time. Come back in a day later, look it over again. It&#8217;s a fairly complex process, give it time to sink in.</strong></p>
<p><strong>Buyers End first. You are in charge of making the wallet, and providing funds to it.</strong></p>
<ol>
<li>Get Electrum 2.0 <a href="http://www.electrum.org/#download">www.electrum.org/#download</a></li>
<li>Run Electrum.</li>
<li>Select Create New Wallet and multi-signature wallet, then proceed. If you already have a default wallet, File&gt;New/Restore. 

<img src="/imgs/2015/03/rY1ld7W1.png">

<li>Select 2 of 3 on next screen, then proceed. 

<img src="/imgs/2015/03/07fuv1S1.png">

<li>You will find your seed generated. Copy it to your clipboard and a text file then #fuckingwriteitdown. 

<img src="/imgs/2015/03/JBtMEuC1.png">

<li>click next, then paste that same seed onto the next screen. Hit next. 

<img src="/imgs/2015/03/P4vtfDy1.png">

<li>Create a password. Don&#8217;t skip this step, the password is required to keep your end secure and release funds. Click next. 

<img src="/imgs/2015/03/uagOa7k1.png">

<li>Copy your master public key, and share it with the market and vendor. <strong>Take care not to share your seed or password.</strong></li>
<li>Gather the two master public keys, one from the market, one from the vendor. Paste them each, order doesn&#8217;t matter. Next. 

<img src="/imgs/2015/03/9.png">

<li>&#8220;Select Server Manually&#8221;, then config to route through Tor. Tor Browser Bundle must be running for this to work. 

<img src="/imgs/2015/03/LLlq6l31.png">

<li>SSL, SOCKS5, localhost, port 9050</li>
<li>Light in bottom right corner will turn from red to green when connected. 

<img src="/imgs/2015/03/icGh48S1.png">

<li>On the receive tab, note that all the addresses start with 3, instead of one. This signifies they are indeed multisig addresses. 

<img src="/imgs/2015/03/XSi87T61.png">

<li>You are responsible for funding the correct amount of bitcoins to an address on this wallet. <strong>Remember, any funds transfered there can&#8217;t be transfered back without without 2 of 3 consensus.</strong> Be careful to send the correct amount. After this is done, your work is done until it&#8217;s time to finalize the transaction (which you will do in a timely manner, as you are not a little bitch).</li>
</ol>
<p><strong>Vendors it&#8217;s your turn!</strong></p>
<p>Generate your Master Public Key</p>
<ol>
<li>Get Electrum 2.0 <a href="http://www.electrum.org/#download">www.electrum.org/#download</a></li>
<li>Run Electrum.</li>
<li>Select Create New Wallet and multi-signature wallet, then proceed. If you already have a default wallet, File&gt;New/Restore.</li>
<li>Select 2 of 3 on next screen, then proceed.</li>
<li>You will find your seed generated. Copy it to your clipboard and a text file then #fuckingwriteitdown.</li>
<li>click next, then paste that same seed onto the next screen. Hit next.</li>
<li>Create a password. Don&#8217;t skip this step, it is for your security. Click next.</li>
<li>Copy your master public key, and share it on your market profile. <strong>Take care not to share your seed or password.</strong></li>
<li>end the creation, you will not be making a wallet at this time. This is done by deleting the wallet file.</li>
</ol>
<p>To open your end of a wallet created by a customer/buyer (this is for each order).</p>
<ol>
<li>File&gt;New/Restore, name the file.</li>
<li>Select &#8220;Restore a wallet or import keys&#8221; and &#8220;multi-signature wallet&#8221;. next screen, 2 of 3. next.</li>
<li>Paste your previous generated master public key.</li>
<li>Gather the two master public keys, one from the market, one from the buyer. Paste them each, order doesn&#8217;t matter. Next.</li>
<li>Verify the correct funds are present.</li>
<li>You are responsible for creating two transactions. One is to pay the market their previously agreed upon share. The other is to pay yourself the rest to the correct bitcoin address. You won&#8217;t be able to complete these, but you will generate the text needed for the customer or market to sign off on these transactions. These will be exported as .txn text files, which you can then copy and share the contents to the market message system, for the buyer or market to fully sign the transaction.</li>
<li>Click the send tab</li>
<li>enter correct address, and amount, then click send. 

<img src="/imgs/2015/03/tF6Q5UU1.png">

<li>Agree to the fee. 

<img src="/imgs/2015/03/SYpij6f1.png">

<li>Provide your password. 

<img src="/imgs/2015/03/ThOmmBj1.png">

<li>save the file. repeat for each transaction, ideally the markets small share first. 

<img src="/imgs/2015/03/tly8Pn31.png">

<li>Open the files in a text editor, and share on the markets message system.</li>
<li>Wait to get paid once the buyer receives their package.</li>
</ol>
<p><strong>Finalizing</strong></p>
<ol>
<li>Open the correct multisig wallet. Nothing will work unless you are in the right wallet.</li>
<li>Tools&gt;Load Transaction&gt;From Text 

<img src="/imgs/2015/03/tCisnTX1.png">

<li>Copy paste each transaction (one at a time), starting with paying the market first. 

<img src="/imgs/2015/03/ev3g9ml1.png">

<li>It should load up a small window, giving signing as an option. <strong>Make sure all the details look correct before you sign!!!!!!!!</strong> 

<img src="/imgs/2015/03/DnbCZLN1.png">

<li>Repeat for vendors transaction.</li>
<li>Congratulations! The transaction is complete!</li>
</ol>
<p><strong>Disputing</strong></p>
<p>Weather it&#8217;s the vendor or buyer disputing, they are responsible for providing a return address. The market is responsible for generating the transaction text. The winner of the dispute is responsible for signing/finalizing the transactions and making sure the the coins are going to the right address.</p>

Updated: 2015-03-21