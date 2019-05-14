---
title: "Security Alert: Six more bugs found in OpenSSl"
---

Posted by: DeepDotWeb
<span>June 6, 2014</span>

<p>As it was published earlier at <a href="http://www.theregister.co.uk/2014/06/05/openssl_bug_batch/">Theregister</a>: Users of anonymising network Tor should definitely update as the man-in-the-middle attack <a href="https://lists.torproject.org/pipermail/tor-talk/2014-June/033161.html" target="_blank">affects Tor clients and relays</a>. Readers may also recognize the name of the chap who, <a href="http://h30499.www3.hp.com/t5/HP-Security-Research-Blog/ZDI-14-173-CVE-2014-0195-OpenSSL-DTLS-Fragment-Out-of-Bounds/ba-p/6501002#.U5DId5RdV68" target="_blank">according to HP&#8217;s ZDI team</a>, wrote the buggy DTLS code.</p>
<p><strong>Quote</strong>:</p>
<blockquote><p>The OpenSSL team today pushed out fixes for <a href="https://www.openssl.org/news/secadv_20140605.txt" target="_blank">six security vulnerabilities</a> in the widely used crypto library.</p>
<p>These holes include a flaw that enables man-in-the-middle (MITM) eavesdropping on encrypted connections, and another that allows miscreants to drop malware on at-risk systems.</p>
<div class="article_side_content"></div>
<p>A DTLS invalid fragment bug (<a href="http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2014-0195" target="_blank">CVE-2014-0195</a>, affects versions 0.9.8, 1.0.0 and 1.0.1) can be used to inject malicious code into vulnerable software on apps or servers. DTLS is more or less TLS encryption <a href="http://security.stackexchange.com/questions/29172/what-changed-between-tls-and-dtls" target="_blank">over UDP</a> rather than TCP, and is used to secure live streams of video, voice chat and so on.</p>
<p>However, an SSL/TLS MITM vulnerability (<a href="http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2014-0224" target="_blank">CVE-2014-0224</a>, potentially affects all clients, and servers running 1.0.1 and 1.0.2-beta1) is arguably worse, as an advisory from OpenSSL explains:</p>
<p>An attacker using a carefully crafted handshake can force the use of weak keying material in OpenSSL SSL/TLS clients and servers. This can be exploited by a man-in-the-middle (MITM) attack where the attacker can decrypt and modify traffic from the attacked client and server.</p>
<p>The attack can only be performed between a vulnerable client *and* server. OpenSSL clients are vulnerable in all versions of OpenSSL. Servers are only known to be vulnerable in OpenSSL 1.0.1 and 1.0.2-beta1. Users of OpenSSL servers earlier than 1.0.1 are advised to upgrade as a precaution.</p>
<p>Users and administrators are advised to check their systems for updates; patched builds of OpenSSL are available from the major Linux distros, for instance.</p>
<div class="CaptionedImage Right Float">
<p>Kikuchi&#8217;s logo for the MITM bug</p>
</div>
<p>The CVE-2014-0224 MITM bug has existed since the very first release of OpenSSL, according to Masashi Kikuchi, the Japanese security researcher who <a href="http://ccsinjection.lepidum.co.jp/blog/2014-06-05/CCS-Injection-en/index.html" target="_blank">unearthed the flaw</a>.</p>
<p>&#8220;The good news is that attacks [exploiting CVE-2014-0224] need a man-in-the-middle position against the victim, and that non-OpenSSL clients (Internet Explorer, Firefox, Chrome on Desktop and iOS, Safari etc) aren&#8217;t affected,&#8221; Adam Langley, a senior software engineer at Google, <a href="https://www.imperialviolet.org/2014/06/05/earlyccs.html" target="_blank">published on his personal blog</a> today.</p>
<p>&#8220;None the less, all OpenSSL users should be updating.&#8221;</p>
<p>The DTLS flaw has also given security experts the fear. &#8220;The OpenSSL DTLS vulnerability dates from April, but was reported today. It may allow remote-code execution (<a href="http://en.wikipedia.org/wiki/Datagram_Transport_Layer_Security" target="_blank">OpenSSL DTLS</a> is still a nightmare),&#8221; noted computer-science professor Matthew Green in a <a href="https://twitter.com/matthew_d_green/status/474532779531595776" target="_blank">Twitter update</a>.</p>
<p>&#8220;This OpenSSL vuln is an example of the kind of subtle protocol bug that <a href="http://www.theregister.co.uk/2014/04/22/openssl_fork_libressl/" target="_blank">LibreSSL</a>&#8216;s (admirable) fork is not likely to fix.&#8221;</p>
<p>The OpenSSL.org advisory comes just weeks after the discovery of the infamous Heartbleed vulnerability.</p>
<p>Prof Green reckons none of the bugs would be easy to exploit – the direct opposite of the password-leaking Heartbleed hole.</p>
<p>The other four fixes in today&#8217;s batch deal with denial-of-service-style vulnerabilities.</p>
<p>Nicholas J. Percoco, veep of strategic services at vulnerability management firm Rapid7, said a wide variety of servers and other internet-connected systems will need to be updated to guard against attackers exploiting these now-fixed bugs.</p>
<p>&#8220;The newly disclosed man-in-the-middle vulnerability disclosed in OpenSSL affects all client applications and devices that run OpenSSL when communicating to vulnerable servers of specific versions, but includes the most recent,&#8221; Percoco explained.</p>
<p>&#8220;This likely contains the majority of systems on the internet given most rushed to upgrade OpenSSL after the Heartbleed disclosure in early April of this year. A man-in-the-middle attack is dangerous because it can allow an attacker to intercept data that was presumed encrypted between a client – for example, an end user – and a server – eg, an online bank.</p>
<p>&#8220;This attack is also passive in nature and will may not be detected by the client, server or network-based security controls.&#8221;</p>
<p>Prof Green added that unearthing multiple bugs in OpenSSL was essentially a welcome development, even though it may cause some unscheduled overtime for sysadmins in the short term.</p>
<p>&#8220;The sudden proliferation of OpenSSL bugs is to be expected and a good thing. Like finding dirty socks during spring cleaning,&#8221; he <a href="https://twitter.com/matthew_d_green/status/474532245869699072" target="_blank">said</a>. ®</p>
<h3>Bootnote</h3>
<p>Users of anonymising network Tor should definitely update as the man-in-the-middle attack <a href="https://lists.torproject.org/pipermail/tor-talk/2014-June/033161.html" target="_blank">affects Tor clients and relays</a>. Readers may also recognise the name of the chap who, <a href="http://h30499.www3.hp.com/t5/HP-Security-Research-Blog/ZDI-14-173-CVE-2014-0195-OpenSSL-DTLS-Fragment-Out-of-Bounds/ba-p/6501002#.U5DId5RdV68" target="_blank">according to HP&#8217;s ZDI team</a>, wrote the buggy DTLS code.</p></blockquote>
<p>This comes just couple of months after the original Heartbleed bug which required all users of openSSL to update their version and some owners of TOR hidden services to  change their private keys as a precaution. TOR users should follow up and update their browser bundle once such updated becomes available.</p>

Updated: 2014-06-06
    
