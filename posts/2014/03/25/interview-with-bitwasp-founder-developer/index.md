---
Interview With Bitwasp Founder &#038; Developer &#8211; Security, DarkNetMarkets &#038; Future Development
---
<article class="post-listing post-4789 post type-post status-publish format-standard has-post-thumbnail hentry category-articles category-deepdot-news tag-bitwasp tag-founder">
    
    <div class="post-inner">
    
    
    <p class="post-meta">
    
    <span>Posted by: <a href="https://www.deepdotweb.com/author/admin/" title="">DeepDotWeb </a></span>
    
    
    <span>March 25, 2014</span>
    <span>in <a href="https://www.deepdotweb.com/category/articles/" rel="category tag">Articles</a>, <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a></span>
    
    <span><a href="https://www.deepdotweb.com/2014/03/25/interview-with-bitwasp-founder-developer/#comments">5 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    <div class="entry">
    
    <p>Following all the marketplaces that got hacked, and the fact that many of them were based on the Bitwasp software, we were very happy when the founder of Bitwasp contacted us and offered to answer some questions regarding Bitwasp, DarkNet uses, Security and the latest &amp; future developments of the Bitwasp market software, we have spoken to the Bitwasp team:</p>
    <p>Cameron Ruggles as Founder<br />
    Thomas Kerin as Developer<br />
    Harris Kalash as the UI designer</p>
    <p>If you feel like helping to the Bitwasp project and contribute for the future development of better marketplaces you can donate to this bitcoin address: 19EkDTAaGWySZv1QsWxyWwYMZpo7jpvPYe<br />
    The developer is working full time on this project, is unemployed and living off the donations so he would really appreciate donations!<br />
    You can find more information here: <a href="http://bitwasp.co/" target="_blank">http://bitwasp.co/</a></p>
    <div id="attachment_4801" style="width: 227px" class="wp-caption aligncenter"><a href="http://www.deepdotweb.com/wp-content/uploads/2014/03/bitwasp-new-design.png"><img class=" wp-image-4801 " alt="Bitwasp-new-design" src="https://www.deepdotweb.com/wp-content/uploads/2014/03/bitwasp-new-design.png" width="217" height="366" srcset="https://www.deepdotweb.com/wp-content/uploads/2014/03/bitwasp-new-design.png 478w, https://www.deepdotweb.com/wp-content/uploads/2014/03/bitwasp-new-design-177x300.png 177w" sizes="(max-width: 217px) 100vw, 217px" /></a><p class="wp-caption-text">Screenshot of the new design of the new Bitwasp Version</p></div>
    <p><b>So, What can you tell us about the new finished, but beta version of Bitwasp?</b></p>
    <p><span style="text-decoration: underline;">Thomas</span>: Our major milestone will be publishing a full version of the Bitwasp code running multisig. Multisig will remove the trust users need to have in the site operator, and at each step of making payment and signing, the user has all the information they need to make an informed decision before proceeding. Users will never pay to an address that one party has control over, meaning less exposure when operators setting up a site. No one wants to be responsible for losing coin, as there&#8217;s often little recourse. But with multisig, even if the site experiences downtime, once buyers and sellers can communicate on another channel they can recover the funds.</p>
    <p>Multisig, or P2SH addresses, have been supported since 2012, so it&#8217;s insane that there isn&#8217;t more support for it. Bitwasp will be one of the first few sites to implement multisig, let alone publish all the code behind it.</p>
    <p>The code itself has been effectively been implemented behind the scenes, however a lot of work remains before it&#8217;s finalized, and ready to be published. The software still needs a lot of work, but most of the ground work is done.</p>
    <p>But this release will see a huge change &#8211; no live wallet, or notion of &#8216;user balances&#8217;. An admin configures an electrum master public key to create public keys/addresses, vendors upload a list of them, buyers enter them on a per-order basis. The order process essentially guides users through steps of a multisiganture transaction.</p>
    <p>Once buyers pay to the multisig address, an unsigned transaction is created which pays the vendor, and the operators fee. In an up-front payment, the buyer must sign the transaction immediately after paying, and the vendor signs and broadcasts to indicate they&#8217;ve dispatched. In an escrow order, after payment is made, vendors would sign to indicate dispatch, and the buyer signs and broadcasts once they receive the goods. Otherwise a dispute is made, and the admin will talk it out with the buyer/seller. A new transaction is created by the admin when an acceptable solution is found. Recently a feedback system was built in, to further assist trustless transacting.</p>
    <p>The effort of creating public keys in advance is something that I&#8217;d love to change, but I don&#8217;t think it&#8217;s reasonable to ask everyone for an Electrum MPK.. Support for BIP32 extended public keys ( M/k&#8217; ) to automate this for all users is another milestone in the future &#8211; with this users could enter their extended key, allowing Bitwasp to generate public keys/addresses for multisig keys/receiving money, but ultimately means keys are all deterministically derived from one single seed.</p>
    <p><em><strong>Here is a gallery showing the process of placing an order using the new multisig:</strong></em></p>
    [nggallery id=3]
    <p><b>How large is the community around Bitwasp and how do you reach broader audience? (as we know with Opensource this is the most important factor when it comes to development)</b></p>
    <p><span style="text-decoration: underline;">Cameron</span>: It&#8217;s difficult to say. We only recently found out that over 10 Darknet Bitwasp marketplaces have been setup. I&#8217;d say it is pretty large considering we haven&#8217;t done much promotion, yet our Facebook page as over 400 likes &#8211; and considering what appears to be the main interest, most people wouldn&#8217;t like such a page with their Facebook account. Additionally 140 members are on our forum. That isn&#8217;t a lot but it is a decent number considering the incredibly small amounts of advertising we&#8217;ve done. I suspect it will easily grow orders of magnitude larger once we release a finished product, even if it is in alpha or beta and also have our Bitwasp.co site launched.</p>
    <p><span style="text-decoration: underline;">Thomas</span>: The forums usually sees new people coming and going, a few faces hanging around for longer.</p>
    <p><b>Is there some business plan behind it or it will stay completely free and open source?</b></p>
    <p><span style="text-decoration: underline;">Cameron</span>: We are planning on launching our own marketplace at Bitwasp.co and hope to see apps for Bitwasp being sold, along side various other legal items. We will also be selling items on our site as well. Hopefully it will become the next well known legal bitcoin marketplace.</p>
    <p><b>Do you consider the use of the current version as </b><b>Wreckless and disappointing behavior?</b></p>
    <p><span style="text-decoration: underline;">Thomas</span>: Bitwasp is highly experimental software, and it should be regarded that any Bitwasp implementation running a live wallet is taking unnecessary risks with user funds. We have never made an alpha release, and typically the only change to the software in site&#8217;s we&#8217;ve seen is they remove the &#8216;NOT IN PRODUCTION, USE ONLY ON TESTNET&#8217; notice. Until <a href="http://test.bit-wasp.org" target="_blank">http://test.bit-wasp.org</a> no longer has this banner, people shouldn&#8217;t trust them.</p>
    <p><b>Will you offer bounties for discovering exploits?</b></p>
    <p><span style="text-decoration: underline;">Cameron</span>: Since protecting security and privacy while facilitating transactions is our primary goal it is important that people are motivated audit our software and report these bugs and exploits to us so they can be fixed.</p>
    <p>The best way to motivate people is money. So we will be rewarding the person who finds the most exploits, and other issues with 3 bitcoins. The winner will be determined by a point system, whoever has the most points win. Exploits that can take bitcoins from the site or the users are worth 3 points, exploits that can access the database and read messages or other data provided by users are worth 2 points, and any other general bugs or exploits that don&#8217;t really jeopardize privacy, security or bitcoins are worth 1 point. This contest will be held after our first release and go for a month.</p>
    <p><b>Will You have all these SQL Injections issues sorted in the new version? How come they are not sorted till now?</b></p>
    <p><span style="text-decoration: underline;">Cameron</span>: Give us more info on this SQL injections&#8230; what have you heard about them? We&#8217;ve gotten little to no feedback in this area as far as I know.</p>
    <p><strong>I don&#8217;t know much about them, only that they exists, i have reached out to couple of the security guys who have experienced with Bitwasp Injections and offered that they will contact you. but here is one example taken from a <a href="http://www.deepdotweb.com/2014/03/23/security-sunday-fails-redsunexxtacy-unnamed-market/">previous published</a> post about security exploits:</strong></p>
    <p><a href="http://www.deepdotweb.com/wp-content/uploads/2014/03/VDMpbLU.png"><img class="aligncenter" alt="sql injection" src="https://www.deepdotweb.com/wp-content/uploads/2014/03/VDMpbLU.png" width="548" height="195" /></a></p>
    <p><span style="text-decoration: underline;">Thomas</span>: Hard to say without details. Most likely an error in the items by categories / locations pages. I&#8217;ve noticed that most of the &#8216;hacked&#8217; accusations take place on reddit, little technical detail is ever gven.</p>
    <p><b>Do you get the inputs from all the hacked markets (i mean on the technical level) about stuff that needs to be fixed?</b></p>
    <p><span style="text-decoration: underline;">Cameron</span>: No. I think the only one we even knew how it got hacked was FloMarket and it was an issue we had already known about.</p>
    <p><b>Can you elaborate on how Flomarket Got hacked technically? assuming its fixed now. (we are still happy to know it was hacked and not a scam and that the admin was telling the truth in the <a href="http://www.deepdotweb.com/2014/01/09/flomarket-admin-im-not-a-scammer-an-exculsive-interview/">interview</a> we have done with him)</b></p>
    <p><span style="text-decoration: underline;">Cameron</span>: This question needs to be answered by the developer. http://bit-wasp.org/index.php?topic=28.90) but in the next version It is fixed because we&#8217;ve entirely changed the way transactions are processed via 2/3 multisignature transactions. This way private keys or bitcoins are never held by the Bitwasp site admins or on the servers.</p>
    <p><span style="text-decoration: underline;">Thomas</span>: In the copy of Bitwasp that Flole used, there was an issue whereby when orders were being added to the database, if the bitcoin amount was out of range (say, 0.0001 satoshis), value like 99 would be entered. It was a subtle type error with disastrous consequences, as obviously if this order was cancelled, the buyer would be credited with 99BTC. Or that&#8217;s what we believe. This has been fixed now, since refactoring order system around multisig. Flomarket was really a sign of how the future would go if Bitwasp didn&#8217;t remove live wallets.</p>
    <p><b>Have you seen any markets nowadays that are based on Bitwasp that you can say are secured?</b></p>
    <p><span style="text-decoration: underline;">Cameron</span>: Nope, but we haven&#8217;t really looked. We didn&#8217;t even realize very many people were using our clearly unfinished software. The longest lasting seems to be Tor Bazaar but we&#8217;re not sure about that either.</p>
    <div id="magicdomid53">
    <div id="magicdomid67">
    <p><b>What do you think / feel About DarknetMarkets operators using your software?</b></p>
    <p><span style="text-decoration: underline;">Cameron</span>: It&#8217;s exciting and comical. It is also unfortunate that they used the unfinished software for live marketplaces and with real bitcoins. We clearly say that it is not finished, is still being developed and to use on testnet only. Unfortunately some have falsely claimed to have fixed issues which lead to people losing their money or privacy. While it doesn&#8217;t seem very profitable or logical to launch a darknet marketplace and we&#8217;re not at all condoning doing so, we are happy to see that there is interest in the software and that many people are enthusiastic about what we&#8217;re doing.</p>
    <p><b>Do you have any <b>general</b> a</b><b>dvice for Bitwasp operators?</b></p>
    <p><span style="text-decoration: underline;">Thomas</span>: Much of the barrier of entry to any company considering working with bitcoin is they simply can&#8217;t all afford to hire someone to code the system, but Bitwasp has lots of libraries, suited to make developing with it really easy, in Bitwasp or other projects. We&#8217;re really hoping it will inspire some inventive new businesses.</p>
    <p><span style="text-decoration: underline;">Cameron</span>: Consider getting creative with our software. Don&#8217;t forget that things such as Airbnb, cryptocurrency exchanges, freelance sites, and Lyft are all technically just marketplaces. why not make it into a freelance site or embrace the First-sale doctrine and have a site that sells incredibly cheap digital files? I feel like such things would get far more attention and</p>
    <p><b><b>Do you have any</b> a</b><b>dvice for DarkNet Marketplace operators Bitwasp operators? </b></p>
    <p><span style="text-decoration: underline;">Cameron</span>: Do not do it. It is not worth it. It isn&#8217;t going to be profitable to launch a dark net marketplace because the barrier to entry is incredibly low (the cost of hosting + setup time of the free software?) and the risk of going to prison if you slip up is just as high. It takes a lot to stay truly hidden in this networked world, and law enforcement only have to be lucky ones before you find yourself in serious trouble. Launching a unique clearnet marketplace would be far more profitable and less dangerous.</p>
    <p><strong>What kind of issues have you faced during development?</strong></p>
    <p><span style="text-decoration: underline;">Thomas</span>: This copy of Bitwasp has been in development since August 2013. We started before, but due to commitments like college, etc, it was hard for the project to proceed at a fast pace. Since August however, we have covered a lot of ground. Since then, the developer took a job elsewhere, before quitting to devote his full time to the project last February. It&#8217;s taken a lot of work to get this far, and we&#8217;re trying to do something great. We have received donations to date which the dev is currently living off, so if anyone is happy about what we&#8217;re doing, and can afford to give a little to keep us going, please donate! It&#8217;s not just Thomas, we have paid out bounties in the past (2.7BTC for someone who helped us fix low entropy private keys (guess we won&#8217;t need that now with multisig.. but glad he helped!), and 2BTC for Harris Kalash, who is working on a new layout for Bitwasp to work on all devices), as well as someone for finding an issue in our codes session management.</p>
    <p><b>Are there other announcements you want to make?<br />
    </b></p>
    <p><span style="text-decoration: underline;">Cameron</span>: Bitwasp.co &#8212; launching soon, submit your email for an update!</p>
    <p><span style="text-decoration: underline;">Thomas</span>: We&#8217;d ask everyone to weigh in on what we&#8217;re doing, and the features we&#8217;re offering. We&#8217;re hoping that Bitwasp can lower the barrier of entry to taking part in bitcoin ecommerce, as a buyer or seller, in a secure way. The unbanked population, and also those in countries with strict financial control face difficulties getting involved in ecommerce, and Bitwasp is making it possible to do it all with a webserver and the satoshi client. Any suggestions, feedback on what we&#8217;ve done, or features you&#8217;d like to see as a buyer/seller, please drop us a line on our forums: <a href="http://bit-wasp.org" target="_blank">http://bit-wasp.org</a></p>
    <p><b>If anyone wants to join the Bitwasp community / help / donate / develop how can he contact you?</b></p>
    <p><span style="text-decoration: underline;">Cameron</span>: To stay updated on the open source project join the Bitwasp forum ( The developers PGP key is here): <a href="http://bit-wasp.org" target="_blank">http://bit-wasp.org</a></p>
    <p>But if you&#8217;d just like to join our Clearnet site (Bitmit alternative) when we launch, submit your email here: <a href="http://Bitwasp.co" target="_blank">http://Bitwasp.co</a></p>
    <p>For donations go to: <a href="http://test.bit-wasp.org/" target="_blank">http://test.bit-wasp.org/</a></p>
    <p>Bitcoin address: 19EkDTAaGWySZv1QsWxyWwYMZpo7jpvPYe<br />
    Since the developer is working full time on this project, is unemployed and living off the donations we would really appreciate donations. We have been and intend to reward people who find exploits.</p>
    <p><em><strong>We want to thank the Bitwasp team for taking the time and answering our questions, and we wish them good luck with the future development! and at the same time we hope that the message from this interview will reach the people that are planning to start another marketplace using the current Bitwasp version.</strong></em></p>
    </div>
    </div>
    
    
    </div><!-- .entry /-->
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/bitwasp/" rel="tag">bitwasp</a> <a href="https://www.deepdotweb.com/tag/founder/" rel="tag">founder</a></span>				<span style="display:none" class="updated">2014-03-25</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/admin/" title="Posts by DeepDotWeb" rel="author">DeepDotWeb</a></strong></div>
    
    
    </div><!-- .post-inner -->
</article><!-- .post-listing -->

