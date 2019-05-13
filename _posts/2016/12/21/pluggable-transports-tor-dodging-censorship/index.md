---
Pluggable Transports for Tor: Dodging Censorship
---
<article class="post-listing post-17050 post type-post status-publish format-standard has-post-thumbnail hentry  tag-censorship tag-dodging tag-pluggable  tag-transports">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/ciphas/" title="">Ciphas </a></span>
    <span>December 21, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/12/21/pluggable-transports-tor-dodging-censorship/#comments">5 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    <p>Are you able to freely use Tor in your country? In that case, you’re one of the fortunate ones . If it’s merely a case where Tor is blocked by your ISP, there are easier solutions.</p>
    <p>You may already be familiar with Tor bridge relays, which the Tor project describes in detail at <a href="https://www.torproject.org/docs/bridges.html.en">Tor: bridges</a>. However, if you live in a country where the internet is heavily censored (e.g. North Korea or Burma), some of them use deep packet inspection (DPI) to filter internet traffic flows, even if they use alternate IP addresses.</p>
    <p>This is where pluggable transports (PTs) come in.</p>
    <p><strong>Previously, on Deepdotweb…</strong></p>
    <p>We at Deepdotweb did explain a bit about pluggable transports in our 2014 article <a href="https://www.deepdotweb.com/jolly-rogers-security-guide-for-beginners/hiding-tor-from-your-isp-part-1-bridges-and-pluggable-transports/">Hiding Tor From Your ISP &#8211; Part 1 &#8211; Bridges and Pluggable Transports</a>. Read it if you need a basic understanding of how they work.</p>
    <p>Currently, the most popular pluggable transports are obfuscated bridges. As their names suggest, they’re a method of obfuscating Tor traffic, making it appear to be “normal” (non-Tor) internet traffic.</p>
    <p>In the years since the aforementioned article, the Tor project has developed newer PTs. The currently deployed PTs are:</p>
    <ul>
    <li><a href="https://github.com/Yawning/obfs4/blob/master/doc/obfs4-spec.txt">obfs4</a></li>
    <li><a href="https://trac.torproject.org/projects/tor/wiki/doc/meek">meek</a></li>
    <li><a href="https://fteproxy.org/">Format-Transforming Encryption (FTE)</a></li>
    <li><a href="http://www.cs.kau.se/philwint/scramblesuit/">ScrambleSuit</a></li>
    </ul>
    <p>Though you can use any of these transports, the general consensus is that obfs4 (the latest version of obfsproxy) is the most effective PT at present.</p>
    <p>If you read more of its documentation, you’ll be able to get an understanding of how obfs4 works, but I’ll explain it as simply as I can.</p>
    <p>In the above article, Jolly Roger (a member of The Hub forums) explains how to use the older PTs obfs2 and obfs3. In his words:</p>
    <p><strong>…For the laymans [sic] out there, basically obfs2 uses a protocol that disguises your traffic to look like random data, whereas [Tor] has a more distinct structure to it. However, it should be noted in the case of obfs2, that if an attacker sniffs the initial handshake between your computer and the obfuscated bridge, they could get the encryption key used to disguise your traffic and use it to decrypt the disguised traffic, which would reveal it as Tor traffic.</strong></p>
    <p>Obfs4, on the other hand, is based on Philipp Winter’s ScrambleSuit, a transport protocol that’s difficult for DPI boxes to identify and block. ScrambleSuit protects against active probing attacks, a technique used by The Great Firewall of China (an ironic term that generally refers to internet censorship in China). For more information on that, see the Wikipedia article <a href="https://en.wikipedia.org/wiki/Golden_Shield_Project">Golden Shield Project</a>.</p>
    <p>Obfs4 is also known as “the obfourscator,” according to Yawning Angel (a member of the Tor Project). Obfs4 incorporates ideas from ScrambleSuit, despite its name being similar to older protocols obsf2 and obfs3. (Confused yet? I didn’t think so.)</p>
    <p>Just to clarify, Yawning Angel, on <a href="https://github.com/Yawning">his GitHub page</a>, briefly makes an effort to illustrate the differences between ScrambleSuit and Obfs4:</p>
    <ul>
    <li>When using obfs4, the handshake always does a full key exchange (i.e. there’s no <a href="https://www.ietf.org/rfc/rfc5077.txt">session ticket handshake</a>).</li>
    <li>The handshake uses the Tor project’s <a href="https://tor.stackexchange.com/questions/436/what-is-the-difference-between-ntor-and-tap">NTor handshake</a>, which obfuscates public keys with the Elligator 2 mapping.</li>
    <li>Link layer encryption uses <a href="https://nacl.cr.yp.to/secretbox.html">Networking and Cryptography library (NaCl)</a> secret boxes (Poly1305 and XSalsa20).</li>
    </ul>
    <p>I realize that these protocols are difficult to explain in a short article, but one of the main reasons that obfs4 is considered to be the best is that it’s faster than its protocol peers. Also, the main changes that have been made to obfs4 are in the key exchange process.</p>
    <p>If you still want more information, the Tor Project has an <a href="https://trac.torproject.org/projects/tor/wiki/doc/PluggableTransports/Obfs4Evaluation">obfs4 Transport Evaluation</a> on their main site, which is basically an FAQ, and tries to explain the transport in plain English.</p>
    <p>One of the more interesting questions posed on the FAQ is this: “How difficult or expensive will it be to block the design?”</p>
    <p>The answer, in essence, is that obfs4, as opposed to its predecessors, reduces the vulnerability against attackers who try to identify which type of protocol is running.</p>
    <p><strong>Give Me My Obfuscation!</strong></p>
    <p>To actually install obfs4, there are several methods. You can build it from its source code, install it directly, or just activate it when you start Tor. For the full list of instructions on building from the source code, visit Yawning Angel’s GitHub repository (which I linked to above).</p>
    <p><strong><img class="wp-image-17080 aligncenter" src="/imgs/2016/12/word-image-113.png" width="859" height="408" srcset="/imgs/2016/12/word-image-113.png 1579w, /imgs/2016/12/word-image-113-300x142.png 300w, /imgs/2016/12/word-image-113-1024x486.png 1024w" sizes="(max-width: 859px) 100vw, 859px" /></strong></p>
    <p>Setting it up from there is actually very simple. You merely need to install the components, using the following commands:</p>
    <p>In order to build it: go get git.torproject.org/pluggable-transports/obfs4.git/obfs4proxy</p>
    <p>After that, to install it: $GOPATH/bin/obfs4proxy – to a location on your hard drive.</p>
    <p>Finally, make a few small changes to your torrc file, which are described in detail at <a href="https://github.com/Yawning/obfs4">Yawning Angel: obfs4proxy</a> – under “Bridge side torrc configuration.” After that, it should be up and running!</p>
    <p>On the other hand, if you’re <em>not</em> the type who enjoys building things from source, there is an even <em>simpler</em> way to activate obsf4.</p>
    <p>When you first launch Tor, a window pops up called “Tor Network Settings.” (This probably looks familiar to those of you who already have it installed.)</p>
    <p><img class="wp-image-17081 aligncenter" src="/imgs/2016/12/word-image-114.png" srcset="/imgs/2016/12/word-image-114.png 559w, /imgs/2016/12/word-image-114-300x259.png 300w" sizes="(max-width: 559px) 100vw, 559px" /></p>
    <p>If you’re in the latter category, click “Configure.” After that, click “Next,” and select “obfs4” as your pluggable transport. Really easy, huh?</p>
    <p>Hopefully, the process isn’t too difficult, but again, if you don’t have obstacles stopping you from running Tor in the first place, pluggable transports should prove unnecessary.</p>
    <p>Still, given that law enforcement has been cracking down on cybercrime, and has become suspicious of anyone who tries to use privacy tools in general, it’s helpful to know about protocols like obfs4, just in case you should ever need to use them.</p>
    <p>They’re watching you…</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/censorship/" rel="tag">censorship</a> <a href="https://www.deepdotweb.com/tag/dodging/" rel="tag">dodging</a> <a href="https://www.deepdotweb.com/tag/pluggable/" rel="tag">pluggable</a>  <a href="https://www.deepdotweb.com/tag/transports/" rel="tag">transports</a></span> <span style="display:none" class="updated">2016-12-21</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/ciphas/" title="Posts by Ciphas" rel="author">Ciphas</a></strong></div>
    
