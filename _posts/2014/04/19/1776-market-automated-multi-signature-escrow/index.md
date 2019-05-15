---
title: "1776 Market: Automated Multi-Signature Escrow"
---

Posted by: DeepDotWeb

<span>April 19, 2014</span>
    

<p class="post-box-title"><strong><span style="text-decoration: underline;">Update</span>: 1776 market redesigned its payment system: <a title="Permalink to Introducing The Grail: The 1776 Equal Trust Multisig System" href="2014/05/12/introducing-grail-1776-equal-trust-escrow-system/" rel="bookmark">Introducing The Grail: The 1776 Equal Trust Multisig System</a></strong></p>
<p>1776 is a marketplace offering a bit more friendly implementation of 3-multisig transactions, we have been chatting with the developer &#8220;Tom&#8221;, for quite a few months as we worked on this marketplace, ans we are happy to be the first to introduce it now, we have asked the developer to provide us with and overview along with a usage guide of the sites multisig, and here it is exactly as he presents it, so you can be the judge:</p>
<div class="box  info"><div class="box-inner-block"><i class="tieicon-boxicon"></i>
<strong>1776 Marketplace url: <span style="color: #ff0000;">http://n6tzonxy7sod7eqt.onion/Register?refid=AGGEHU</span></strong>
</div></div>
<p><span style="text-decoration: underline;"><strong>Video Tutorial:</strong></span></p>
<p><iframe src="//www.youtube.com/embed/uzUFJZe0TkE" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe></p>
<p><span style="text-decoration: underline;"><strong>What is 1776?</strong> </span></p>
<p>1776 is the answer to the Darknet Markets&#8217; most difficult business problem: theft and fraud.</p>
<p>Many multisig escrow sites have popped up attempting to address this problem. Some require the buyer to get involved in the escrow process. All involve large amounts of fiddly, complicated work for the vendor.<br />
    None of them is designed in such a way that they could be a major marketplace in the Silk Road vein. They just expect too much from the vendor and the buyer.</p>
<p>Yours Truly (the author of the 1776 system) was a vendor late in 2013. I lost about $3000 when Sheep Marketplace got hacked/whatever happened.</p>
<p>I headed over to Silk Road&#8217;s message board, and posted about a feature that at the time, almost nobody knew about: Multi-Signature Escrow. As recently as last November, almost nobody had ever heard of it.</p>
<p>Within two minutes, my post was deleted. I declined to start using SilkRoad 2, and resolved to write my own system. I probably don&#8217;t have totell you that I&#8217;m glad I did.</p>
<p><span style="text-decoration: underline;"><strong>How does it work?</strong></span></p>
<p>The central design goal for 1776 was to completely secure the escrowed funds from fraud and theft in the most automated, simple-to-use way that could be accomplished. From an interface standpoint, Silk Road is the model.</p>
<p>Buyers never have to understand the escrow, or even know that it exists. When a buyer places an order, they are automatically taken to their orders page, which will show a deposit address unique to that order, and  amount to pay. It also features a QR code to make payment from a smart phone easy.</p>
<p><a href="/imgs/2014/04/userorderpage.jpg"/>
<p>Within ten seconds of payment being received, the order is marked paid. Buyers need only refresh the page to see that it is awaiting approval from the vendor.</p>
<p>Consider how much more convenient this is than what we&#8217;re used to. There is no tedious process of making a deposit, hoping it&#8217;s the right amount (due to BTC price fluctuations) two hours from now, waiting however many confirmations the site requires, often made worse by overload-induced lag, then finally placing the order. Making a purchase takes planning ahead to be around your computer for up to several hours. It is a huge hassle. But with 1776, if you know what you want, you can choose the item, enter the quantity and shipping information (which is automatically encrypted for you with the vendor&#8217;s public key when you submit it), copy and paste the payment address into your wallet, make the payment, wait ten seconds, refresh the orders page to confirm, and you&#8217;re done. There&#8217;s not one more thing you have to do until you finalize. If the vendor can&#8217;t fulfill the order, your money will be sent to a refund address that you specified in your account settings.</p>
<p>So, unlike other multisig systems, not only is the user experience not more complex than usual, it is actually far more convenient than any other marketplace operating today. The minor amount of added complexity is handled by the vendor. And it is quite minor!</p>
<p><span style="text-decoration: underline;"><strong>Understanding Multisig</strong></span></p>
<p>The essence of multisig transactions is pretty simple. An ordinary transaction is conducted by specifying an amount of bitcoins to send to a wallet address, what address to send it to, and then signing the<br />
    transaction with the private key of the wallet from which you are sending them. Multisig is simply a wallet which requires 2 or more signatures to do the same thing.</p>
<p>The first question that comes to mind, considering that the signatures are going to come from two different people, is &#8220;So where is the escrow wallet then? Is it in the bitcoin network somewhere? If the money isn&#8217;t in my wallet and isn&#8217;t in yours, where is it?&#8221;</p>
<p>The way we create an escrow/multisig wallet is by creating a new wallet address which is in essence the mathematical product of one wallet owned by me, and one wallet owned by you. We give the Bitcoin Core client (which vendors must install) a couple of simple commands to get a &#8220;public key.&#8221; That public key is put together with the 1776 public key (my key) to create an escrow address. Unlike usual addresses that start with a 1, escrow addresses start with a 3. Here&#8217;s an example:</p>
<p>3Cfg5g9f5CVY1MpMigUb6xr322e882NFBN</p>
<p>So, once you&#8217;ve got a public key from Bitcoin Core, you enter it on the web site, along with a payout address. When funds are released from escrow, this is where they will be sent. It should not be an address in Bitcoin Core; I strongly recommend creating a blockchain.info wallet (and doing all of the recommended backup procedures!) and sending your bitcoins out from there via the &#8220;shared coin&#8221; option, which will mix them and make them maximally untraceable.</p>
<p><a href="/imgs/2014/04/escrowwalletinput.jpg"/>
<p>The back-end engine will see there is a new request for an escrow wallet, and calculate it. This can take up to a minute. Just refresh the page to see the address.</p>
<p>You can also click the &#8220;View&#8221; button to show you the command you can cut-and-paste into Bitcoin Core to confirm that your public key and my public key do indeed create the specified escrow address.</p>
<p>I mentioned earlier that the buyers send their funds to a unique deposit address for each order. When that deposit receives a single confirmation, the funds are immediately transferred out to the vendor&#8217;s escrow wallet. Then (and only then) are you notified that you have received a new order: when the safety of your funds is for all intents and purposes a mathematical certainty. You can verify the existence of the funds by searching on your escrow wallet on blockchain.info.</p>
<p>So, at this point, you accept the orders, decrypt the addresses, ship the product, and await finalization.</p>
<p>I&#8217;ll mention here that there are two different methods of creating a multisig address in Bitcoin Core. One is older and simpler, one is newer and more robust. My original development centered around thenewer and more robust command. But in the process of experimenting, I realized that the older implementation was exactly as secure as the new one, did everything I would ever need it to do, and was way simpler to use for everyone concerned. The simple part made the choice a no-brainer.</p>
<p>The other multisig systems require you to modify commands that you&#8217;ll paste into Bitcoin Core, or similar. You have to pull your private key out and paste it in to the transaction. Given the state of the art in client software, the newer method is just too darned complicated.</p>
<p>With 1776, all you need to do is this: Your Bitcoin Core software (unlike with the newer multisig) has to actually know the escrow wallet exists. It needs to do the math itself and &#8220;realize&#8221; that it has one of the keys for this wallet, so it knows what to do when you go to sign the transaction.</p>
<p><a href="/imgs/2014/04/transactionpage.jpg"/>
<p>The addmultisigaddress command only has to be done once per escrow wallet. Bitcoin Core will remember it after that.</p>
<p>Here we see a finalized transaction ready to be redeemed. It takes the exact transaction that was forwarded to your escrow, and sends 95% of it to you, and 5% to me. Note that I only EVER get paid when you do. Figure I&#8217;m honest?</p>
<p>(You can verify what the transaction does by typing &#8220;decoderawtransaction &#8221; followed by the hexidecimal string in the box. It will show you where the outputs of the transaction go).</p>
<p>You highlight and copy the contents of the box, then you paste it into the Bitcoin Core console window. It will return another long hexidecimal string. That is the signed transaction.</p>
<p><a href="/imgs/2014/04/complete-true.jpg"/>
<p>The quickest way to grab that is to double-click it; it highlights exactly the right text. Hit Control-C or right-click and copy, then type &#8220;sendrawtransaction &#8221; with a space and paste the signed transaction in.</p>
<p>Boom &#8211; if you have your payout wallet software open you&#8217;ll see the funds hit immediately, not when some batch process happens on the server as with other systems but *right now.*</p>
<p>When there is a refund the site creates a signed transaction giving the refund and the vendor signs it and sends it.  Each user has a refund address they must specify in order to be able to place an order, so it is all set up automatically.</p>
<p>Once you are in practice, it should be easy to redeem one transaction every ten seconds or so. Seems a small price to pay for perfect assurance of the security of your funds to me. How about you? :)</p>
<p>Vendors who can establish that they are established vendors on an existing site will be able to get a free vendor account for one week from launch. During that week, vendors who are not established sellers will be able to purchase an account for $200USD. (All prices on the site are given in dollars and converted to bitcoins at a market price not more than ten minutes old, via Coinbase).</p>
<p>After that week, vendor accounts will probably go up, possibly quite a bit.</p>
<p>I figure I&#8217;ll either see you guys this week, or after the next time someone steals all your bitcoins. ;)</p>
<p><span style="text-decoration: underline;"><strong>Resolution / Support</strong></span></p>
<p>For now, the buyers don&#8217;t have a signature on the escrow accounts.  I&#8217;m going to add that functionality soon.  For now, what happens is they send a message to support/dispute resolution, and whatever the resolution is, the vendor and I will sign a transaction that reflects the decision.  Buyers who want to be on the escrow in the future will be able to purchase an account that has that functionality, which will be much less expensive than a vendor account.</p>
<p><span style="text-decoration: underline;"><strong>XMPP Address</strong></span></p>
<p>You will notice that there is an XMPP address for your account at the top of the main page. Click the address for instructions on how to use it with Tor. It is a tor-only XMPP system with no connection to the Internet, so it is inherently secure. Users may create any number of rooms for discussion. I offered this because I think it is superior to a message board and because I think the Darknet needs it. I don&#8217;t know of another.</p>
<p><span style="text-decoration: underline;"><strong>The Future</strong></span></p>
<p>In the near future, I intend to introduce multisigs that include buyers, but they will be special buyer accounts. They won&#8217;t be free, but they won&#8217;t be nearly as expensive as vendor accounts. I anticipate these being used by people buying very large amounts of product from abroad, for example.</p>
<p>How would you like to be able to export all your orders to a .csv file you could import into any shipping label software you liked? Automatically decrypt all the addresses and get your labels done in five minutes, even if there&#8217;s a hundred of them. How big could you grow your operation then? How much less would shipping suck? The capability is already there. I&#8217;ll be announcing how to take advantage of it soon.</p>
<p><span style="text-decoration: underline;"><strong>SECURITY</strong></span></p>
<p>I&#8217;ll give the final word to the security question. First and foremost: there&#8217;s nothing to steal. The amount of money in the system is exactly what has come in since the last confirmation. Once any funds coming in get that one confirmation, they immediately go out to escrow wallets. The only sensitive information in the system that is theoretically stealable is the site&#8217;s private key. All that would do is allow you to get your funds out of escrow without my help. And by the way, if the site gets taken down, that&#8217;s exactly what I&#8217;ll do: give you the private key so you can get your money out yourself. That&#8217;s dead simple too. Then I&#8217;ll set the system back up somewhere else, in some other country, with no real names attached to it, and never connecting to it via any method but Tor. With 1776 credibility intact, we just get back on track as fast as we can, and probably from a very recent database backup. My interests are aligned with yours: I set it up that way deliberately.</p>
<p>The front-end application connects to a back end API. It is the API that talks to the database. There is no SQL code in the front-end so there is no chance of SQL injection attacks. All sensitive operations<br />
    are carried out by a completely separate process that doesn&#8217;t even know the front-end exists.</p>
<p>All mailing addresses are encrypted automatically when sent to the vendor, all messages sent to vendors are also encrypted automatically. The only messages not encrypted automatically are the ones from vendors to users. If the user specifies a PGP key, it is used. If they have not, it goes in the database as cleartext, for now. In the near-term, I expect to require encryption for users to receive a message even from vendors.</p>
<p>The server has never touched an IP address associated with me, it has been procured anonymously and is not within the jurisdiction of the US government. It contains precisely fuck-all with which a DEA agent could conceivably advance his career, or catch a single dealer. It has no money, no useful data, no connection to any real person. There just isn&#8217;t anything to hack&#8211; by design.</p>
<p>Hope to see you soon! &#8211; Tom</p>
<div class="box  info"><div class="box-inner-block"><i class="tieicon-boxicon"></i>
<strong>1776 Marketplace url: <span style="color: #ff0000;">http://n6tzonxy7sod7eqt.onion/Register?refid=AGGEHU</span></strong>
</div></div>
<p>&#8212;&#8212;</p>
<p>Marketplace url is also added to our <a href="/2013/10/28/updated-llist-of-hidden-marketplaces-tor-i2p/">hidden marketplace list</a></p>
<p>And this post is added to the <a href="multisig-guides/">Multisig Guides page</a>.</p>

Updated: 2014-04-19
    
