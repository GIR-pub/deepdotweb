---
title: "Silk Goxed: How DPR used Mtgox for Hedging &#038; Lost Big"
---

Posted by: DeepDotWeb 

<span>January 25, 2015</span>
    

<p><strong>As always, another amazing work researched by <a href="http://www.reddit.com/u/impost_r">/u/impost_r</a> (<a href="https://twitter.com/1mp0ster" target="_blank">@1mp0ster</a>) and written by <a href="http://www.reddit.com/u/gwern">/u/gwern</a> (<a href="http://www.gwern.net/" target="_blank">Gwern.net</a>) all Credit and tips goes to them. Was originally posted <a href="http://www.reddit.com/r/DarkNetMarkets/comments/2tgymg/silk_goxed_how_dpr_used_mtgox_for_hedging_lost_big/" target="_blank">on Reddit</a> and reposted here for more publicity:</strong></p>
<p>Summary:</p>
<blockquote><p>Using recent filings in the trial of Ross Ulbricht, the 2014 leak by hackers of the Mtgox database, and a Mtgox insider, we identify Ulbricht&#8217;s Mtgox account, the accessing IP, and trades made by it. The account information indicates that SR1 implemented its currency hedging system (intended to prevent vendor losses due to BTC fluctuations) by, starting in July 2011, connecting to Mtgox over the clearnet and trading through a Mtgox account. Surprisingly, it seems that this IP information was <em>not</em> used by the US government investigation to de-anonymize SR1. The bulk of the account seems to have been stolen by a Mtgox or SR1 insider.</p></blockquote>
<p>(This was primarily researched by <a href="http://www.reddit.com/u/impost_r">/u/impost_r</a>, and written by <a href="http://www.reddit.com/u/gwern">/u/gwern</a> .)</p>
<p>Silk Road 1 launched in January 2011. During 2011, the exchange rate for Bitcoin experienced extreme volatility, moving by orders of magnitude, which made it difficult to transact using Bitcoin because payment for an order could easily become less than the order cost. In response to this, Dread Pirate Roberts 1 introduced in <a href="https://www.dropbox.com/s/58v7x0nh794tr0b/index.php%3Ftopic%3D819.0">9 July 2011 a “hedging” system</a>:</p>

<img src="https://info-gir.github.io/deepdotweb/imgs/2015/01/hedge.png">

<p>vendors could ‘lock in’ the USD value of any purchase and receive, when the transaction settled, the USD value in Bitcoins back. The obvious way to implement a hedging system is to maintain an account on a large exchange (the largest then being Mtgox) and transfer bitcoins in and buy/sell to match each purchase; but this would incur fees for trading, counterparty risk (not just the exchange collapsing/being hacked but also the account being seized), complexity, and risking de-anonymization (Mtgox and other exchanges do not look kindly on Tor connections due to abuse). It was not clear how DPR had implemented hedging; he could have self-insured, betting on Bitcoin’s long-term upwards trend to profit on average.</p>
<p>The hedging system was a success, and was used from July 2011 to October 2013 when SR1 was raided, with perhaps occasional hiccups.</p>
<p>In January 2015, as part of the ongoing trial of DPR (Ross Ulbricht), the prosecutors released <a href="https://www.dropbox.com/s/csdfztq3mb9xawj/253100323-154-1United-States-v-Ross-William-Ulbricht-14-Cr-68-wexhibits.pdf">a letter with several exhibits</a> objecting to the defense strategy of painting the owner of Mtgox, Mark Karpeles, as the real DPR. It writes:</p>
<blockquote><p>Several days after the defendant’s arrest on October 1, 2013, which was publicly disclosed the following day, the U.S. Attorney’s Office for the Southern District of New York (“USAO-SDNY”) was contacted by Mr. Karpeles’ attorney. The attorney offered to forward records associated with a certain suspicious MtGox account that he stated he had previously sent to AUSA-2 in USAO-Baltimore. The attorney stated that MtGox had also found a different account, in the defendant’s own name, which the attorney said he could supply records for as well.</p>
<p>Mr. Karpeles’ attorney subsequently forwarded via email the information he had previously sent to AUSA-2 concerning the account MtGox deemed suspicious. (See Ex. E). As reflected in the email, the attorney explained that the forwarded information was “not information about the account in Ulbricht’s name, which MtGox only identified as of interest after the Ulbricht indictment [i.e., arrest].” (Id. (emphasis in original)). The forwarded information related instead to a MtGox account as to which “MtGox ha[d] suspicions may be associated with the largest bitcoin wallet that is perceived by some in the bitcoin community to be associated with Silk Road.” (Id.) (Bitcoin users had long speculated about Bitcoin “wallets” or “addresses” connected to the Silk Road website, based on analyses of the Blockchain. 5 Thus, it appeared the MtGox account in question had transactions involving these addresses.)</p>
<p>The email from Mr. Karpeles’ attorney further explained that there was other suspicious activity connected to the account. The account was initially opened by someone using the email address “<a href="#">
<p>After receiving the records for the account, investigators working with USAO-SDNY’s investigation of Silk Road were able to tie the “<a href="#">
<p>This may sound relatively innocuous: ‘AUSA-2 in USAO-Baltimore’ ignored the original email, and by the time USAO-SDNY took it seriously, Ulbricht had already been arrested, and then with all the information in hand and his IP, an account which did nothing was found. So what?</p>
<p>Well, as an exhibit (pg18), it quotes an email from Mt. Gox lawyer Scott was sent to USDOJ on 24 July 2013 and forwarded to Serrin Turner (U.S. attorney / cybercrime coordinator) on 15 October 2013 (emphasis added):</p>
<blockquote><p>“The user deposited a large number of bitcoins into the account. The user used the bitcoins to purchase U.S. dollars, but the account was never linked to a bank account to make a withdrawal. <em>The transactional records for the account are too voluminous to provide via e-mail.</em> I’m happy to discuss a method and format to provide the records to you.</p>
<p>In May 2013, the user contacted MtGox to report that the account was “hacked.” MtGox informed the user that the e-mail address associated with the account had been changed pursuant to a proper request to change the address. A copy of the exchange with the user regarding the hack is also attached to this e-mail. Following the exchange attached to this e-mail, the user did not communicate further with MtGox, and MtGox is not aware that the user made any report to law enforcement.</p>
<p>Prior to the user contacting MtGox regarding the “hack”, the approximately U.S. $1.9 million had been converted to bitcoins. The bitcoins (7393.49 BTC) were transferred to address 1AsUc3Lw1oDmwimWoGeCfBngzziS98FP5V (7393.49 BTC). MtGox is aware that some of these bitcoin were used, and the balance (6393.49 BTC) currently remain at address 1Mh58EcGSMMscgh5qE5u4BVSL9KRd8GzQK. MtGox believes 1000 BTC were sold on exchange btc-e.com.”</p></blockquote>
<p>Unlike in the main body, this says something interesting &#8211; “The transactional records for the account are too voluminous to provide via e-mail.” So if DPR was not using this account to cash out commissions from SR1, but it was heavily trading only to eventually withdraw a noticeably smaller sum of bitcoins, what on earth was this account doing? The obvious possibility is: the ‘davidmaisano’ Mtgox account implemented the SR1 hedging system.</p>
<p>We identified the 7393.49 BTC withdrawal using a blockchain search, using wallet identification based on multiple input transactions, and tracking back change addresses we could see that the same entity received 8630 BTC in another transaction origination from Mt. Gox. Ulbricht seems to have stopped using the Mtgox account around May 2013. All activity on the account stopped after the last withdrawal, leaving a negligible amount of funds in the account. Why? There are two possible reasons:</p>
<ol>
<li>The account hack. The hack appears to have been genuine and not some sort of attempt to scam Mtgox: <a href="https://www.scribd.com/doc/253456456/Silk-Road-exhibits-GX-241">a 05/29/13 journal entry presented in court</a> shows that Ulbricht thought the DEA stole 2mln usd from his Mt. Gox account, a loss confirmed in the <a href="https://www.dropbox.com/s/f94v4d4c8hs8vcw/253456480-Silk-Road-exhibits-GX-250.pdf">spreadsheet Ulbricht kept of SR1-related transactions</a> (exhibit GX-250).</li>
<li>In the 2013 journal, Ulbricht comments on 03/24/2013 that he had been “been slowly raising the cost of hedging”, suggesting he was trying to discourage use of it. On 04/10/2013, he writes “some vendors using the hedge in a falling market to profit off of me by buying from themselves. turned of access log pruning so I can investigate later. market crashed today.” This suggests he was no longer keen on the hedging system and was planning on scrapping it anyway when the vendors began abusing it, the market crashed (increasing losses), and then on top of that, the account was drained by what he believed was the DEA (see the journal &amp; spreadsheet entries) a month later.</li>
</ol>
<p><strong>MtGox2014Leak.zip</strong></p>
<p>In early 2014, Russian hackers gained access to Mtgox backend servers (possibly with the help of insiders) and released [<a href="magnet:?xt=urn:btih:b6545ecc7db8d44c8cbc4e93989edf8221af75f5&amp;dn=2014+Mt.+Gox+Leak&amp;tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&amp;tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&amp;tr=udp%3A%2F%2Ftracker.istole.it%3A6969&amp;tr=udp%3A%2F%2Ftracker.ccc.de%3A80&amp;tr=udp%%203A%2F%2Fopen.demonii.com%3A1337" target="_blank">a public torrent</a>] containing dumps of Mtgox databases up to December 2013 and held the rest back for sale. This is the leak which was used to produce <a href="https://willyreport.wordpress.com/">The Willy Report</a> and <a href="http://bitcoin.stamen.com/">The MtGox 500</a> Fortunately, that period covers the full lifetime of SR1.</p>
<p>The email specifies that ‘The bitcoins (7393.49 BTC) were transferred to address AsUc3Lw1oDmwimWoGeCfBngzziS98FP5V (7393.49 BTC).’, which is an unusual number of BTC. We can search the torrent for that and find entry y, entry x is included as it served as direct confirmation of the account:</p>
<p>x:</p>
3fcf63cc-c7d9-4cd8-b630-9a7ac9ee4ff0,0f97bfa3-b1ad-404a-afb1-8ead63c8250b,"2013-05-06 11:09:31",withdraw,-8630
</textarea></div>

<p>
    y:</p>
3fcf63cc-c7d9-4cd8-b630-9a7ac9ee4ff0,521960b9-8524-4737-93a0-2411aaa5e20f,"2013-05-06 12:38:33",withdraw,-7393.49
</textarea></div>

<p>
    That first part “3fcf63cc-c7d9-4cd8-b630-9a7ac9ee4ff0” is the UUID.</p>
<p>We asked an ex-employee for assistance in going further. The insider provided the following excerpt from official logs not part of the lea k(after showing him the relevant leak logs):</p>
"521960b9-8524-4737-93a0-2411aaa5e20f","3fcf63cc-c7d9-4cd8-b630-9a7ac9ee4ff0","22329","2013-05-06 12:38:33","withdraw","739349000000","806031","Bitcoin withdraw to
    1AsUc3Lw1oDmwimWoGeCfBngzziS98FP5V","(ip)","Money_Bitcoin_Block_Tx","ea309d42641b03ff0c41f1671a803db612d5c8c6f6ef183f197391ba969d2a78"
</textarea></div>

<p>
    This shows the same UUID, and some additional information such as blockchain data relating to the withdrawal.</p>
<p>Back to the 2 withdrawals mentioned above; we can see the 8360 BTC withdrawal 1.5 hours before the 7393.49 BTC one. So not only did this confirm that the same entity that received the 7393.49 BTC received the 8630 BTC as well, it shows that it’s a withdrawal from the same account.</p>
<p>These are not the only two entries for the account 3fcf63cc. Isolating the entries, we have almost all deposits and withdrawals to that account, ~100 in total. This is an odd amount of activity for an account portrayed as nearly inactive. Further, we can see a withdrawal of <a href="https://blockchain.info/fr/tx/ed62ab5009d218af8d6d16cba9e58842dcffa16d75401ccc4910263df9d5e7bb%20" target="_blank">40,000 BTC</a> then 2 months later, a deposit of 44,814.031337back into the <a href="https://blockchain.info/fr/tx/7269a8ebe71559e6337cab93fe75340dca91deeeed2af11be86affc9a23b50ab" target="_blank">same account</a>.</p>
<p>The agent Der-Yeghiayan testifies on 20 January 2015 that they were focusing on what seems to have been a different account (<a href="http://antilop.cc/sr/files/2015_01_20_Ulbricht_trial_transcript_W2_D1.pdf">pg102-107</a>), perhaps explaining the general lack of LE interest in the other activities.</p>
<p>The Mtgox insider, which is familiar with the legal side of things, commented on these transactions that the (bogus) identity information for 3fcf63cc had not drawn any notice and that 3fcf63cc was very active with <a href="https://mega.co.nz/#%212EAQSAyb%21N_YFfapZlJTRafvEIJI2OPI0naHGQ-qRK7csKmFgnPw">a number of transfers in/out</a>, a peak balance of 150k btc, and ~20,000 different trades of “(deposit, withdrawal, buy, sell, etc)” (consistent with the email’s description of the trading activity as ‘voluminous’). The 40,000 BTC withdrawal had caught our interest as this was the maximum amount of bitcoin that could be withdrawn within a day at the time, it also meant the user was verified as the limit for unverified users as the time was a mere 4000 BTC per day, the insider confirmed that the account had AML2 status (notarized verification).</p>
<p>An example order from the leaked files:</p>
1312614863842963,"2011-08-06 07:14:23",6534,NJP,sell,USD,29.70994053,292.03445,78.59413634758,22952.195381491,0.8761,78.59413634758,68.856322854115,0,0
</textarea></div>

<p>
    Isolating all trade entries associated with the account, <a href="https://www.dropbox.com/s/j3bboteyufiudbo/mtgox_uuid_6534.csv">17,049 unique entries were found</a>. (Note that interpreting Mtgox trade records can be challenging; for example, the data is occasionally corrupt, and not all of these are separate orders since the exchange splits them into multiple orders in order to match them with various counter parties.) Looking at the entries, the easiest way to identify multiple trades as belonging to a single buy or sell order is to group them based on timestamps. Individual trades are visualized in this graph:</p>

<img src="https://info-gir.github.io/deepdotweb/imgs/2015/01/graph.png">

<p><a href="https://i.imgur.com/9SkDN5V.png">
aggregated by day</a>, <a href="https://i.imgur.com/mqxcI80.png">
aggregated by day, and log USD value</a>; the periods of inactivity can be clearly be seen.</p>
<p>The account was registered around April 2011 (logs from Jeb McCaleb’s Mtgox apparently were known to be incomplete), and began trading 5 May 2011 (2 months before the hedging went live).</p>
<p>This has two main implications:</p>
<ol>
<li>This activity is consistent with either hedging, or DPR1 being a trader who doesn’t care about cashing out and being so bad he could lose much of his money in a bull marketThis is an astonishingly large amount of bitcoins even at the time, would have represented a large fraction of Mtgox’s deposits, and substantial trading volume. It seems difficult to believe that Mtgox did not at least suspect the account of being linked with SR1. (The insider claims they had not realized what the account was for until we began asking about it.)</li>
<li>The exact rationale behind the switching between buying and selling doesn’t seem clear.Given that Ulbricht’s journal/memoirs describes him as barely being able to program when he began Silk Road in January 2011 and learning desperately on the fly, it may be that he implemented the simplest possible form of hedging: building up a cushion of USD early on by selling all hedging bitcoins, and then later buying back due to exchange rate decreases. It’d be worthwhile to analyze this further by looking at the Mtgox exchange rate movements.</li>
</ol>
<p><strong>IP addresses</strong></p>
<p>It gets even more interesting: The insider noted that the Mtgox IP logs indicate that before the hedging went live, the account connected over the clearnet from probably Ulbricht’s house, these IP addresses were identifiable as ‘unprotected’ because they weren’t registered to a server host (the IP addresses that were servers were most likely Tor exit nodes and/or VPNs). More recently (presumably in 2013), 3fcf63cc did not just connect over IPs ‘connected to Ulbricht’ (which could easily be himself logging in personally to do normal trading), but an IP, <code>207.106.6.28</code>, connected to the Mtgox API for trading.</p>
<p>The prefix <code>207.106.6.</code> should be familiar to those who have followed the SR1 case in detail, since it is the prefix of one of the server IPs listed in the <a href="https://info.publicintelligence.net/SilkRoadProtectiveOrder.pdf">civil asset forfeiture request filed in NY to seize SR1’s bitcoins</a> after the October 2013 raid. Specifically, the seizure lists the IP <code>207.106.6.32</code>. In other words, the SR1 backend server appears to have been connecting over the clearnet to Mtgox for its regular hedging transactions. (This is not unprecedented: Ulbricht did SR1 backups to his JTAN account over clearnet because he complained Tor was too slow, and also used a VPN.)</p>
<p>This is a serious anonymity leak: blockchain analysis has lead investigators to <a href="https://www.capa.net/case/2014-cr-00068/page/637">Mt. Gox deposit addresses as early as April 2012</a>, a subpoena or request for trading records would show a distinct pattern of large trades which screamed ‘hedging’ to anyone familiar with the operation of SR1. Was this how the Iceland server was identified?</p>
<p>Probably not. The server image in all filings has been described as having been obtained 23 July 2013, which is 1 day before the original Mtgox email was sent, and would have to have been located and then requested earlier, Further, this would have been a perfectly legitimate investigative strategy, indeed, it’s almost surprising that they <em>didn’t</em> ‘follow the money’ and de-anonymize SR1 in April 2012, or even 2011, when the FBI investigation began, and doubly surprising that they could be interested in Karpeles and Mtgox but not get the trading records. There was considerable pressure to take down SR1 as soon as possible (see Der-Yeghiayan’s testimony), and there was no reason to wait until July 2013 to image the SR1 server and use such a strange and cockamamie excuse like Agent Tarbell’s (undocumented) story of hacking SR1’s CAPTCHA. Interestingly, the Mt. Gox insider noted that it was unlikely investigators had any transactional logs of the Mt. Gox account(s) before their attorney sent investigators the full logs in July 2013.</p>
<p>This all also suggests that one could measure SR1 revenue over time by examining the hedging trades to estimate how much hedged volume there was, however it is uncertain to what extent hedging was done on the exchange, a possibility is that hedging was done both on and off-exchange as there are some significant gaps during which the account identified has no trade logs. Something that supports this is the previously quoted <a href="https://www.scribd.com/doc/253456456/Silk-Road-exhibits-GX-241">journal</a> entry:</p>
<blockquote><p>“&#8217;03/24/2013 / been slowly raising the cost of hedging; / orgainzed local files and notes&#8217;”</p></blockquote>
<p>We see that through 19-21 March 2013 a large amount of BTC is bought on the account, during this same time period roughly 40,000 BTC is withdrawn from the exchange in 3 separate transactions. this could indicate that funds were transferred off exchange for a more risky hedging method(risky in the sense that Ulbricht would take the loss if price collapsed).</p>
<p>(This all raises an interesting alternative history question: suppose SR1 had not been raided in October 2013; Mtgox collapsed not too long afterwards; what would have happened to SR1 when Mtgox vaporized? Did SR1 still have a significant amount of funds on Mt. Gox? Would SR1 have collapsed or DPR1 covered the loss of the hedging funds out of his own pocket? Would the trustees have figured out the DPR1 account and turned it and all the IPs over to law enforcement? Or would people have been motivated to examine the leak for possible DPR1 activity?)</p>
<p>An important note regarding the leaked files: the insider believes parts of them to have been altered by hackers, possibly the same ones that released the files. Further, we learned that the original files were altered too. Further, hackers had full read/write access to all Mt. Gox servers for 3 days, deleting server logs after they were finished. However, we can’t find any rumors or evidence that the Ulbricht account was known to anyone, much less the 2014 Mtgox hackers, so it is a priori likely that the Ulbricht transactions are not tampered with specifically.</p>
<p><strong>Who Stole Ulbricht’s Coins?</strong></p>
<p>We know from the original email that this was Ulbricht’s account, and we now know it was the hedging account rather than a way of cashing out or day-trading, due to its timing, activities, and lack of fiat withdrawals. But that doesn’t answer the question: where did the coins go and who took them?</p>
<p>Ulbricht claims, complaining to Mtgox support, that he was hacked. He might be lying, but the same claim appears in his personal records where he has no reason to continue the pretense. Specifically, he thinks his coins were seized by the DEA.</p>
<ol>
<li>The government did not take them. This is definitely wrong because the internal Mtgox records show purchases of Bitcoin and then a normal Bitcoin withdrawal rather than seizure of USD balance, there was no government announcement then, and still has been none.</li>
<li>A hacker did not take them based on the notorious Mtgox 2011 leak of usernames/password-MD5-hashes: we&#8217;ve checked but the &#8220;davidmaisano&#8221; account is simply not included in that dump (although interestingly, an account named &#8220;altoid&#8221; is), so as attractive and simple as this explanation would be, it&#8217;s impossible &#8211; the account could not have been exploited by cracking the password hash since no such hash was available.</li>
<li>A vendor probably did not take them. Our insider suggests a SR1 vendor may have figured the hedging system and somehow broken into the account and taken them. (Specifically, that they have some elements that could show vendors from Silk Road stealing and/or hacking Mt. Gox; further details were not given to us to protect his identity.) But it’s not clear how a vendor would even know SR1 genuinely used hedging, used it on Mtgox, which account it was on Mtgox, get the password or authentication token, and get in to drain it.</li>
<li>A Mtgox insider may have taken it. If they realized what the account was, it would be easy to log in, and withdraw the coins to sell on BTC-E. They would also know that Ulbricht would be unable to complain to LE, and easily verify the account to get higher withdraw limits. (Tampering with the records might also explain some anomalies and missing entries, but might not.)</li>
<li>A SR1 insider may have taken it. Ulbricht hired multiple people (“smedley”, “Variety Jones”/”cimon”, “utah”, etc) to work on coding and maintaining the site, and the hedging functionality was written in early 2011, when his coding was most amateurish and insecure. He showed a propensity for hardwiring values (the JTAN backup IP, the VPN login IP). If he hardwired the username/password or something of that ilk, any one who saw that part of the codebase could have easily engineered the theft; various employees had access to the codebase and sometimes the server itself (eg. &#8220;&#8230;04/21 &#8211; 04/30/2013: market and forums under sever DoS attack. Gave 10k btc ransom but attack continued. Gave smed server access&#8230;&#8221;). In which case, the question is not why the hedging account was burgled in 2013, but why it wasn’t burgled earlier.</li>
</ol>
<p><strong>Anomalies &amp; Missing entries</strong></p>
<p>EDIT: removed section about 3 missing rows. Appears to have been a glitch in downloading over HTTP or grepping the 2014 Mtgox leak, please disregard.</p>
<p>An additional anomaly is the account-verification status. Mtgox required identification for very large withdrawals like the 40k BTC withdrawal on 6-9-2012 or the final withdrawal of 4933 BTC made by the putative hacker, and this identity verification is attested to in the government email. But nevertheless, the transaction records mark each transaction with the Mtgox code of &#8220;!!&#8221; for an unverified or untrustworthy account, from the beginning to the end:</p>
1351795530115354,2012-11-01 18:45:30,6534,NJP,sell,USD,8.23742072,91.91536,79.874,7341.627,0.25736,79.874,20.556,0,0,!!,
    ...
    1367843632129978,"2013-05-06 12:33:52",6534,22fa9cb7-edfa-475e-a598-7b6b0d147ea5,45fe9a2df91b0b67779de6646a32fe42,NJP,buy,USD,134.13461537,16753.41346,98.063,
    1642892.307,0,98.063,0,0.40240385,4511.694,!!,
</textarea></div>

<p>
    It&#8217;s not 100% clear whether the &#8216;!!&#8217; notation refers to identify-verification or whether it might also here be referring to the account being accessed from multiple countries&#8217; IPs (which is certainly the case for SR1, which according to the <a href="https://t.co/8DZdRGIUYF">master server list document from Ulbricht&#8217;s laptop, exhibit GX-264</a>, bounced from country to country).</p>
<p><strong>TODO</strong></p>
<p>Open questions:</p>
<ol>
<li>How much did Mtgox really know and when did it know it?</li>
<li>Who were the Silk Road insiders and what information did they give, and to who?</li>
<li>Does this account, the account(s) the FBI investigation focused on, or any other Silk Road link to Mt. Gox have any connection to Mt. Gox’s massive losses?</li>
<li>Does the ‘hacking’ and big withdrawal account for most of DPR1’s missing bitcoins? The coins seized from the SR1 servers and Ulbricht’s laptop do not add up to the recorded SR1 commissions</li>
<li>How was Ulbricht’s Mtgox account hacked, exactly?The ‘davidmaisano’ account was not part of the 2011 Mtgox username/password leak, so the password hash could not have been cracked; ‘altoid’ was, but should have no connection. Or was it indeed SR1 vendors? And if so, how exactly did they go from suspecting that SR1 was hedging on Mtgox to being able to control the exact account and do withdrawals? Could they have hacked the SR1 backend and instead of settling for the hot wallet, stole the authentication for the Mtgo API and drained the account that way? Or, could it have been another Mtgox insider who, observing the trading, realized what the account was for and quietly drained it with some bitcoin withdrawals, knowing that Ulbricht would be unable to do anything but complain to Mtgox?</li>
<li>Did the trades stop in May 2013 because the account was hacked? Did activity switch to a different Mtgox account, a different exchange (such as BTC-E), or did DPR1 switch to self-insuring?</li>
<li>How much did Mtgox make off the hedging trades directly, or was its tolerance more strategic and about not interfering with SR1? There are BTC/USD fees for each transaction but it&#8217;s a bit difficult to convert that into a total.</li>
<li>Is hedging on exchange intrinsically unsafe for any large black-market due to the distinctive signature, increased counterparty risk, and high volume of trades?</li>
</ol>
<p><strong>Code</strong></p>
<p>The CSV file follows a schema like thus:</p>
Trade_Id,Date,User_Id,Japan,Type,Currency,Bitcoins,Money,Money_Rate,Money_JPY,Money_Fee,Money_Fee_Rate,Money_Fee_JPY,Bitcoin_Fee,Bitcoin_Fee_JPY
</textarea></div>

<p>
    Or by column-number:</p>
<ol>
<li>Trade_Id,</li>
<li>Date,</li>
<li>User_Id,</li>
<li>Japan,</li>
<li>Type,</li>
<li>Currency,</li>
<li>Bitcoins,</li>
<li>Money,</li>
<li>Money_Rate,</li>
<li>Money_JPY,</li>
<li>Money_Fee,</li>
<li>Money_Fee_Rate,</li>
<li>Money_Fee_JPY,</li>
<li>Bitcoin_Fee,</li>
<li>Bitcoin_Fee_JPY</li>
</ol>
<p>Halfway through, the format changes to include a hash. It can be deleted like this:</p>
sed -i -e 's/22fa9cb7-edfa-475e-a598-7b6b0d147ea5,45fe9a2df91b0b67779de6646a32fe42\,//' mtgox.csv
</textarea></div>

<p>
    The resulting file can be read into R and graphed:</p>
hedging &amp;lt;- read.csv("mtgox_uuid_6534.csv", header=FALSE)
    hedging$Date &amp;lt;- as.Date(hedging$V2)
    hedgingDaily &amp;lt;- aggregate(V8 ~ V5 + Date, hedging, `sum`)
    with(hedgingDaily, qplot(Date, V8, color=V5))
</textarea></div>


Updated: 2015-01-25

