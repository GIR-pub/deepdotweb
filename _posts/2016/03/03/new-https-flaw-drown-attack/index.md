---
New HTTPS Flaw: “DROWN” Attack"
---
<article class="post-listing post-13391 post type-post status-publish format-standard has-post-thumbnail hentry  tag-attack tag-drown tag-flaw tag-https">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/fuzzy/" title="">Fuzzy </a></span>
    <span>March 3, 2016</span>
    <span>in <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://www.deepdotweb.com/category/news-updates/" rel="category tag">News Updates</a></span>
    <span><a href="https://www.deepdotweb.com/2016/03/03/new-https-flaw-drown-attack/#comments">4 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>The OpenSSL project recently released a new update to address a critical vulnerability (CVE-2016-0800) dubbed “DROWN” which stands for “Decrypting RSA using Obsolete and Weakened eNcryption”.</p>
    <p>From the OpenSSL <a href="https://www.openssl.org/news/secadv/20160301.txt">security advisory</a>:</p>
    <p>“A cross-protocol attack was discovered that could lead to decryption of TLS sessions by using a server supporting SSLv2 and EXPORT cipher suites as a Bleichenbacher RSA padding oracle. Note that traffic between clients and non-vulnerable servers can be decrypted provided another server supporting SSLv2 and EXPORT ciphers (even with a different protocol such as SMTP, IMAP or POP) shares the RSA keys of the non-vulnerable server. This vulnerability is known as DROWN (CVE-2016-0800).”</p>
    <p>In a nutshell, the DROWN attack relies on servers that support SSLv2. The first version of the attack relies on servers that support both SSLv2 and TLS. The second version relies on SSLv2 servers and TLS servers that both share the same keypair. The second version means that an SSLv2 server could be used to decrypt the TLS server&#8217;s traffic.</p>
    <p>This vulnerability could easily be mitigated by disabling SSLv2 and never reusing keypairs across servers. “But if it&#8217;s so easy to mitigate, why is it such a big deal?”, one might ask. According to the DROWN <a href="https://drownattack.com/">website</a> (which is ironically behind CloudFlare who is in a position to MITM SSL traffic), the vulnerability affects 33% of all HTTPS servers on the internet, including Yahoo, BuzzFeed, and HostGator.</p>
    <p>Although CVE-2016-0800 is the CVE assigned to DROWN, there are other CVEs that make DROWN even worse, as the website explains:</p>
    <p>“The DROWN attack itself was assigned <a href="https://www.openssl.org/news/secadv/20160301.txt">CVE-2016-0800</a>. DROWN is made worse by two additional OpenSSL implementation vulnerabilities. <a href="https://www.openssl.org/news/secadv/20160128.txt">CVE-2015-3197</a>, which affected OpenSSL versions prior to 1.0.2f and 1.0.1r, allows a DROWN attacker to connect to the server with disabled SSLv2 ciphersuites, provided that support for SSLv2 itself is enabled. <a href="https://www.openssl.org/news/secadv/20160301.txt">CVE-2016-0703</a>, which affected OpenSSL versions prior to 1.0.2a, 1.0.1m, 1.0.0r, and 0.9.8zf, greatly reduces the time and cost of carrying out the DROWN attack.”</p>
    <p>The US government is largely responsible for this vulnerability due it restricting the export of strong cryptography up until the end of the 1990s. The DROWN website explains:</p>
    <p>“The U.S. government deliberately weakened three kinds of cryptographic primitives: RSA encryption, Diffie-Hellman key exchange, and symmetric ciphers. <a href="https://mitls.org/pages/attacks/SMACK#freak">FREAK</a> exploited export-grade RSA, and <a href="https://weakdh.org/">Logjam</a> exploited export-grade Diffie-Hellman. Now, DROWN exploits export-grade symmetric ciphers, demonstrating that all three kinds of deliberately weakened crypto have come to put the security of the Internet at risk decades later.”</p>
    <p>The system administrators are also to blame for not disabling a protocol that has been known to be weak and vulnerable for over a decade.</p>
    <p>The security researchers have said “We&#8217;ve been able to execute the attack against OpenSSL versions that are vulnerable to <a href="http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0703">CVE-2016-0703</a> in under a minute using a single PC. Even for servers that do not have these particular bugs, the general variant of the attack, which works against any SSLv2 server, can be conducted in under 8 hours at a total cost of $440.”</p>
    <p>Not only is traffic decryption possible, MITM attacks are possible as well according to the <a href="https://drownattack.com/drown-attack-paper.pdf">technical paper</a></p>
    <p>Configuring your browser to reject SSLv2 will only prevent the first version of this attack, the second version can still be carried out.</p>
    <p>You can read the <a href="https://drownattack.com/drown-attack-paper.pdf">technical paper</a>, get more <a href="https://drownattack.com/#question-answer">information</a>, and <a href="https://drownattack.com/#check">check</a> if your site is vulnerable to this attack at the DROWN <a href="https://drownattack.com/">website</a>.</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/attack/" rel="tag">attack</a> <a href="https://www.deepdotweb.com/tag/drown/" rel="tag">drown</a> <a href="https://www.deepdotweb.com/tag/flaw/" rel="tag">flaw</a> <a href="https://www.deepdotweb.com/tag/https/" rel="tag">https</a></span> <span style="display:none" class="updated">2016-03-03</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/fuzzy/" title="Posts by Fuzzy" rel="author">Fuzzy</a></strong></div>
    
