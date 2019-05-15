---
title: "STUNnion &#8211; Detecting IP Address Leaks During Tor .Onion Browsing"
---


Posted by: DeepDotWeb 

<span>March 4, 2015</span>





<p>The guys from <a href="https://cryptostorm.is">Cryptostorm.is</a> just released a new research regarding a security vulnerability that may affect and cause De-anonymization of Tor users browsing .onion sites <strong>without using the Tor Browser Bundle</strong> &#8211;  that includes the &#8220;expert&#8221; browser bundle via SOCKS proxy. The summary was shared with us and is brought to you here:</p>
<p>A few weeks back, as we were working on mitigating <a title="Major Windows Security Flaw Leaks VPN Users Real IP Address" href="/2015/02/01/major-windows-security-flaw-leaks-vpn-users-real-ip-address/">webRTC</a>-based IP disclosures, we <a href="https://twitter.com/cryptostorm_is/status/569072686523129856">asked a question</a> in twitter&#8230;</p>
<blockquote class="twitter-tweet" width="550">
<p>So what happens to out-of-channel &quot;NAT-busting&quot; webRTC parallel-universe funky-packets going across Tor? <a href="https://twitter.com/i2p">@i2p</a>? Hyperboria/cjdns?&#10;Any papers?</p>
<p>&mdash; cryptostorm〰cstørmˣˣ (@cryptostorm_is) <a href="https://twitter.com/cryptostorm_is/status/569072686523129856">February 21, 2015</a></p></blockquote>
<p><script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script></p>
<p>It appeared somewhat obvious to us that this information disclosure vector would work across Tor just as well a on the plaintext internet &#8211; but others in the community weren&#8217;t as sure. Since (conventional) STUN requests are sent via UDP rather than TCP, it almost looked as if Tor sessions might be ontologically protected. But of course the STUN queries don&#8217;t route across TOR; they go to a plaintext internet lookup (for the STUNnion tester, we&#8217;ve used <b>stun:stun.services.mozilla.com</b>). Then they come back across Tor to the initiating server, where they present as unwelcome information disclosure.</p>
<p>After a bit of testing, we confirmed our suspicions and had positive test results we could consistently replicate. Since it seemed likely that a mere published announcement of webRTC over Tor would would succeed in alerting as many potential targets of this leak as possible, we went ahead and built a testing site to confirm the viability of the vector firsthand. (note: we have adhered to what we consider responsible disclosure practices in this matter)</p>
<p>Since we&#8217;ve noted quite a few <a href="https://github.com/cryptostorm/browsercreeps.com">leak testing sites</a> that are surprisingly heavy with aggressive advertising scripts, we have chosen to publish all source code of the STUNnion test concurrently with its release; it can be <a href="https://cryptostorm.is/blog/github.com/cryptostorm/STUNnions">found here</a>, in full.</p>
<p>(╭☞ ͡° ᴥ ͡°)╭☞ &#8230;heere&#8217;s STUNnion!</p>
<p><b><a href="http://stunmbj4vvnuv5pr.onion/">stunmbj4vvnuv5pr.onion</a></b> (native .onion)</p>
<img src="imgs/2015/03/stun1.png">
<b><a href="https://stunmbj4vvnuv5pr.torstorm.org/">stunmbj4vvnuv5pr.torstorm.org</a></b> (torstorm.org gateway)</p>
<img src="imgs/2015/03/stun2.png">
<p>Unfortunately, it still leaves (a rough estimate of) 10% of folks visiting .onion sites via non-TBB browsers who are potentially vulnerable. There&#8217;s discussions &amp; resources of this issue in another <a href="https://cryptostorm.org/webrtc">series of forum threads</a> that may prove useful for those seeking additional protection strategies. Plus there&#8217;s a bunch more out there; too many to list in one place, really. tl;dr protect yourself if you&#8217;re not using TBB to access .onion resources!</p>
<p>We&#8217;d be remiss if we didn&#8217;t mention that the webRTC blocking heuristics in our <a href="https://cryptostorm.org/widget">client-side &#8216;widget&#8217;</a> have proved successful thus far in protecting against in-the-wild examples of these disclosure events. Further, we&#8217;ve implemented across-the-board denial of <b>all</b> STUN-based queries for .onion-directed sessions accessing Tor via our <a href="https://torstorm.org">torstorm.org</a> ,onion gateway service. Since torstorm operates as a true http/onion proxy, it&#8217;s able to do this kind of thing particularly effectively (source code <a href="https://github.com/cryptostorm/cstorm_torstorm">published here</a>). Torstorm&#8217;s about to be opened up to everyone, rather than only cryptostorm members, since we&#8217;ve recently implemented native .onion access across our entire network, via our <a href="http://deepdns.net">deepDNS</a> system of layered-security DNS resolver resources. Of course, there&#8217;s other ways to block webRTC than the methods we&#8217;ve implemented for our members &#8211; we generally recommended layering of such defences, to ensure maximum protection even in corner-state scenarios.<br/>
    Thanks to everyone in the community and on our team who pitched in to help get this test ready for deployment. Here&#8217;s to the memory of Aaron Schwartz, who inspired so many of us to think creatively about big challenges. We miss you, Aaron.</p>
<p>~ <a href="https://cryptostorm.is">ˣˣcstørm_teamˣˣ</a></p>

Updated: 2015-03-04