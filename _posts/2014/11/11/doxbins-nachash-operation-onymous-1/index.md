---
title: "Doxbin’s Nachash On Operation Onymous (P.1)"
---

Posted by: <a href="https://www.deepdotweb.com/author/nealrauhauser/" title="">Neal Rauhauser </a></span>
<span>November 11, 2014</span>

<p><strong>Second part avilable at &#8211; <a href="http://www.deepdotweb.com/tag/nashcashtag/">#Nashcash Tag</a> (After publishing) &#8211; Read the other posts related to <a href="http://www.deepdotweb.com/tag/silkroad2bust/" target="_blank">Operation Onymous Here</a></strong></p>
<p>Among of Friday night chatter regarding Operation Onymous I noticed that doxbin was among the sites that had gone missing. If doxbin is new to you, this was a site just for dox, but it’s closely associated with Encyclopedia Dramatica. After checking to make sure that wasn’t a troll I decided to track down the particulars, because nachash is basically the Richard B. Riddick of the internet. I figured if anyone had some insight into what actually happened, it would be him &#8211; a couple of years ago nachash shared that his motivation for taking the site over from the original operator was so he could hone his methods of protecting onions in the most difficult environment imaginable.</p>
<p><a href="http://twitter.com/loldoxbin">@loldoxbin</a> and <a href="http://twitter.com/ioerror">@ioerror</a>, Jacob Applebaum, were publicly talking about logs Friday night. This later popped up as a long post on the tor-dev list &#8211; a 1,300 word writeup with an onion address containing the logs, the source of the site, and the details on the work nachash did to secure the system.</p>
<p><a href="https://lists.torproject.org/pipermail/tor-dev/2014-November/007731.html">yes hello, internet super villain here</a></p>
<p>While he was writing that I caught up with him on IRC. He was pretty adamant that doxbin will not be coming back again. About a year ago nachash publicly retired and turned operation of the site over to another hacker named Intangir, but he got it back last July.</p>
<p>(11:38:13 PM) nachash: tl;dr I guess we&#8217;ll see if they can do anything @ me as a human<br />
    (11:38:23 PM) nachash: but I have no plans of reviving doxbin<br />
    (11:38:41 PM) nachash: I could move boxes and tighten it up some more<br />
    (11:38:51 PM) nachash: and publish the hidden service descriptors again<br />
    (11:38:54 PM) nachash: pull in some of the traffic<br />
    (11:38:57 PM) nachash: and rebuild that way<br />
    (11:38:58 PM) nachash: but honestly<br />
    (11:39:06 PM) nachash: it&#8217;s a fucking 12 year old skid shit show<br />
    (11:39:10 PM) nachash: not worth my time</p>
<p>After the tor-dev post went up there was a lot of chatter theorizing about how the takedown was accomplished. There was talk of SQL injection being how the markets were had, but that made no sense for doxbin, <strong>as the site didn’t even have a SQL database</strong> – its done with flat files. There are a lot of theories being floated but it seems that there is a stealth DoS that loads up Tor, and this is being used to trigger admin visits to servers and otherwise work at deanonymizing them. This tweet was fairly interesting for those who want the gritty details and there are many more like it in <a href="http://twitter.com/loldoxbin">@loldoxbin</a>’s timeline.</p>
<blockquote class="twitter-tweet" width="550">
<p>.<a href="https://twitter.com/puellavulnerata">@puellavulnerata</a> Want me to get some other log reports up, so you can get a baseline for comparison?</p>
<p>&mdash; nachash (@loldoxbin) <a href="https://twitter.com/loldoxbin/status/531272976512323584">November 9, 2014</a></p></blockquote>
<p><script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script></p>
<p>There were a couple of questions posed on tor-dev, and nachash returned with further clarifications in this post:</p>
<p><a href="https://lists.torproject.org/pipermail/tor-dev/2014-November/007734.html">yes hello, internet supervillain (follow up)</a></p>
<p>The Tor Project posted their <a href="https://blog.torproject.org/blog/thoughts-and-concerns-about-operation-onymous">Thoughts and Concerns about Operation Onymous</a> about thirty six hours later . The eye opening paragraph has to do with the seizure of relays:</p>
<p>“We are also interested in learning why the authorities seized Tor relays even though their operation was targeting hidden services. Were these two events related?”</p>
<p>Nothing is certain at this point, but the analysis contained speculation as to how these takedowns were accomplished. The theories include:</p>
<p>1.) OPSEC troubles, which were clearly the issue for Silk Road 2.0<br />
    2.) SQL injection, but this was clearly not how doxbin was taken<br />
    3.) Bitcoin de-anonymization, but again not an issue for doxbin<br />
    4.) Direct attacks on the Tor network itself</p>
<p>As far as doxbin itself, I think they missed one – it&#8217;s quite possible that the site merely had the bad luck to be quartered in a facility that had a serious player in it, and they were a target of opportunity.</p>
<p>The Tor Project blog post closed with advice to concerned hidden service operators. The attacks being used were based on resource exhaustion, with the implicit advice being more ram and more cores are a cheap insurance policy. The other notable suggestion was the manual selection of the guard node for your hidden service. This is another box to register and fund with the same stealth as a server hosting a hidden service.</p>
<p>Taking a step back from the technical details, Tor is not a cloak of invisibility, it’s a piece of software with network and cryptographic features. Both of these offer an attack surface for a motivated intruder. The lesson for site operators is simple: What happens when a fault in Tor exposes your server? If your answer is a deer in headlights look you need to leave this work to others.</p>
</div>


Updated: 2014-11-11    
