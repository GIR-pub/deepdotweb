---
ChaosVPN: The Hackers’ VPN!
---
<article class="post-listing post-16415 post type-post status-publish format-standard has-post-thumbnail hentry  tag-chaosvpn tag-hackers tag-vpn">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/ciphas/" title="">Ciphas </a></span>
    <span>November 14, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/11/14/chaosvpn-hackers-vpn/#comments">5 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    <p>You have to admit it – even the name sounds intriguing, doesn’t it? ChaosVPN is a VPN intended to connect hackers and hackerspaces. The Chaos Computer Club, based in Hamburg, Germany, designed it.</p>
    <p>I discovered ChaosVPN in a very unusual way. I’m a member of several dark web-related social networks (on the clearnet, that is) and one of the group members asked how to connect to it. Thus, I was directed to the <a href="https://wiki.hamburg.ccc.de/ChaosVPN">ChaosVPN wiki</a>, which, of course, explains how to connect and all the basics.</p>
    <p>The part that really made me laugh, of course, was this “warning” emblazoned on the front page:</p>
    <p><img class="wp-image-16416 aligncenter" src="/imgs/2016/11/word-image-24.png" width="928" height="561" srcset="/imgs/2016/11/word-image-24.png 1282w, /imgs/2016/11/word-image-24-300x181.png 300w, /imgs/2016/11/word-image-24-1024x619.png 1024w" sizes="(max-width: 928px) 100vw, 928px" /></p>
    <p>Can anyone say “Shadow Web”? Hopefully that made you giggle – but I digress.</p>
    <p><strong>Connecting to ChaosVPN</strong></p>
    <p><img class="wp-image-16417 aligncenter" src="/imgs/2016/11/word-image-25.png" width="810" height="618" srcset="/imgs/2016/11/word-image-25.png 1280w, /imgs/2016/11/word-image-25-300x229.png 300w, /imgs/2016/11/word-image-25-1024x782.png 1024w" sizes="(max-width: 810px) 100vw, 810px" /></p>
    <p>ChaosVPN uses <a href="https://www.tinc-vpn.org/">tinc</a>, a VPN daemon that creates a secure network between hosts on the internet via encryption and a tunneling protocol. In fact, ChaosVPN and tinc are really interdependent.</p>
    <p>If you’re unfamiliar with how to use tinc, I suggest you start with that first. When it comes to your anonymity, you may already have loyalty to a specific VPN, but ChaosVPN serves a different purpose. For those seeking out a VPN with strong anonymity, I direct you to our <a href="https://www.deepdotweb.com/vpn-comparison-chart/">VPN Comparison Chart</a>.</p>
    <p>Tinc consists of a single daemon known as <a href="https://www.tinc-vpn.org/documentation/tincd.8">tincd</a> that makes up both the sending and receiving end of the tunnel. Its user interface consists of a CLI, which is very similar to the Bash Unix shell (or if you use Windows, it’s quite a bit like the DOS command prompt.)</p>
    <p>Features of Tinc include:</p>
    <ul>
    <li><strong>Encryption, authentication, and compression: </strong>You have the option to compress traffic using <a href="http://www.zlib.net/">zlib</a> or <a href="http://www.oberhumer.com/opensource/lzo/">LZO</a>; <a href="https://www.libressl.org/">LibreSSL</a> or <a href="https://www.openssl.org/">OpenSSL</a> encrypt your traffic and defend it against modification using message authentication codes and sequence numbers.</li>
    <li><strong>Automatic full mesh routing:</strong> Despite the fact that there are multiple ways to set up the tinc daemon connections, VPN traffic is sent directly to its destination (as much as possible).</li>
    <li><strong>Ability to expand your VPN:</strong> In order to add new nodes to the VPN, you merely create a new config file; this eliminates the need for creating new daemons or configuring new network devices.</li>
    <li><strong>Bridge Ethernet segments:</strong> You can link Ethernet segments together to run as a single segment.</li>
    <li><strong>Runs on multiple operating systems:</strong> Linux, FreeBSD, OpenBSD, NetBSD, OS X, Solaris, Windows 2000, XP, Vista, and Windows 7 and 8 all support Tinc.</li>
    <li><strong>Supports IPV6:</strong> Provides the possibility of tunneling IPV6 traffic over its tunnels, and of creating tunnels over preexisting IPV6 networks.</li>
    </ul>
    <p>As for how to connect to ChaosVPN using Tinc, it depends on which OS you’re using. The ChaosVPN Wiki features a “Generic” tutorial, written by a Debian user. If you use a different OS, you can slightly adjust the instructions accordingly.</p>
    <p>Other than the Generic tutorial, they also feature these:</p>
    <p><a href="https://wiki.hamburg.ccc.de/ChaosVPN:DebianHowto">Debian how-to</a></p>
    <p><a href="https://wiki.hamburg.ccc.de/ChaosVPN:UbuntuHowto">Ubuntu how-to</a></p>
    <p><a href="https://wiki.hamburg.ccc.de/ChaosVPN:OpenWRTHowto">OpenWRT how-to</a></p>
    <p><a href="https://wiki.hamburg.ccc.de/ChaosVPN:FreeBSDHowto">FreeBSD how-to</a></p>
    <p><a href="https://wiki.hamburg.ccc.de/ChaosVPN:NetBSDHowto">NetBSD how-to</a></p>
    <p><a href="https://wiki.hamburg.ccc.de/ChaosVPN:Netbsd_NAT_VPN_router_using_chaosvpn_and_ipnat">NetBSD NAT VPN router using ChaosVPN and ipnat</a></p>
    <p><a href="https://wiki.hamburg.ccc.de/ChaosVPN:MacOSXHowto">Mac OSX how-to</a></p>
    <p>Does that cover just about all of them? I think so. While I was initially going to write out all the instructions here, I don’t want to plagiarize from the wiki too much…so I’ll just sum it up.</p>
    <p>1. Whichever operating system you’re using, go into the CLI and install LibreSSL and zlib (a.k.a. A Massively Spiffy Yet Delicately Unobtrusive Compression Library).</p>
    <p><img class="wp-image-16418 aligncenter" src="/imgs/2016/11/word-image-26.png" width="838" height="406" srcset="/imgs/2016/11/word-image-26.png 1587w, /imgs/2016/11/word-image-26-300x145.png 300w, /imgs/2016/11/word-image-26-1024x496.png 1024w" sizes="(max-width: 838px) 100vw, 838px" /></p>
    <p>2. Install tinc. There are a few ways to do this, but one way is to simply go to this repository, download the components, and compile them: <a href="http://debian.sdinet.de/lenny/sdinet/tinc/">Index of /lenny/sdinet/tinc</a>. The alternative is to go to <a href="http://tinc-vpn.org/download/">tinc: download</a>, where all the packages are available.</p>
    <p>3. Install the ChaosVPN software. You can find this at <a href="https://github.com/ryd/chaosvpn">GitHub: ChaosVPN</a>. There are several methods to install it, depending on how hardcore you are, but basically – you can create a git snapshot Debian package, create a Debian package, or compile and install the raw binary. (I’m suddenly having a vision of 1’s and 0’s…)</p>
    <p><img class="wp-image-16419 aligncenter" src="/imgs/2016/11/word-image-27.png" width="889" height="428" srcset="/imgs/2016/11/word-image-27.png 1595w, /imgs/2016/11/word-image-27-300x144.png 300w, /imgs/2016/11/word-image-27-1024x493.png 1024w" sizes="(max-width: 889px) 100vw, 889px" /></p>
    <p>4. Once you have a new node in ChaosVPN, you need to come up with a network nickname and an IPv4 or IPv6 range that you’ll be using (which the wiki also goes into detail about).</p>
    <p>5. You then need to generate your public and private RSA keys with tinc. In order to do this, you use the command “generate rsa-keys [bits].” The default number of bits is 2048. If you save keys to existing files, tinc won’t delete the old ones; you have to remove these manually.</p>
    <p>6. Email your info to the guys at Chaos Computer Club: <a href="/cdn-cgi/l/email-protection#1d7e757c726e6b6d7330777274735d757c707f686f7a337e7e7e337978"><span class="__cf_email__" data-cfemail="610209000e1217110f4c0b0e080f2109000c031413064f0202024f0504">[email&#160;protected]</span></a>. The wiki goes into more detail about what information they need.</p>
    <p><strong>What’s the Point of ChaosVPN?</strong></p>
    <p><strong><img class="wp-image-16420 aligncenter" src="/imgs/2016/11/word-image-5.jpeg" srcset="/imgs/2016/11/word-image-5.jpeg 656w, /imgs/2016/11/word-image-5-300x216.jpeg 300w" sizes="(max-width: 656px) 100vw, 656px" /></strong></p>
    <p>Credit: Matt Joyce 2011</p>
    <p>This is really just a very basic summary, and the wiki covers all the gritty details.</p>
    <p>And you may wonder – why join the network at all? Personally, I love the idea of a VPN that can bring hackers and coders together. Whether you’re a novice at hacking or a master, it’s a way that you can communicate with one another, share secrets, and all that good stuff.</p>
    <p>I confess that it took me <em>a little time</em> to get the hang of tinc, but if you’re already a command line wizard, then it should be almost second nature.</p>
    <p>That being said, I love the idea that I may have helped connect a few of you together.</p>
    <p>Oh…and for those of you who are disappointed that you can’t access .lll, .rdos, or .clos sites with ChaosVPN, guess what? You <em>can</em> access .hack sites!</p>
    <p>Is that good motivation?</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/chaosvpn/" rel="tag">chaosvpn</a> <a href="https://www.deepdotweb.com/tag/hackers/" rel="tag">hackers</a> <a href="https://www.deepdotweb.com/tag/vpn/" rel="tag">vpn</a></span> <span style="display:none" class="updated">2016-11-14</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/ciphas/" title="Posts by Ciphas" rel="author">Ciphas</a></strong></div>
    
