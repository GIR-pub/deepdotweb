---
Man In The Middle Attacks"
---
<article class="post-listing post-15734 post type-post status-publish format-standard has-post-thumbnail hentry  tag-attacks tag-man tag-middle">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/filipjelic/" title="">Filip Jelic </a></span>
    <span>October 10, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/10/10/man-in-the-middle-attacks/#comments">5 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>In this article I&#8217;m going to explain theory, prevention, some practical attacks and forensics related to the Man in the Middle (MitM) attacks to help you understand the risk to your privacy. Those are attacks used to eavesdrop your communication by having access to at least one part of the communication protocol.</p>
    <p>Example, Alice sends a letter to Bob and uses Lucifer to deliver it, Lucifer has the MitM position which gives him the ability to read and change the message. Safety of the communication protocol depends Lucifer&#8217;s trustworthiness.</p>
    <p><strong>Understanding how internet works:</strong></p>
    <p>To understand MitM attacks on internet connection, first you have to learn how the internet works in it&#8217;s basic form. Three types of devices are used: clients, routers and servers. The most common protocol for client – server communication is Hypertext Transfer Protocol (HTTP). Majority of web browsing, emails, instant messaging etc. is implemented through HTTP.</p>
    <p>When you type <a href="http://www.deepdotweb.com">http://www.deepdotweb.com</a> to your browser, client (you) sends a request for the webpage to the server. The packet (HTTP GET request) is forwarded through several routers to the server. The server then responds with a webpage that gets routed back to client where it is rendered on their screen. It is vital for HTTP messages to be transmitted in a secure manner to ensure privacy and anonymity.</p>
    <p><img class="wp-image-15790 aligncenter" src="/imgs/2016/10/word-image-18.png" srcset="/imgs/2016/10/word-image-18.png 785w, /imgs/2016/10/word-image-18-300x143.png 300w" sizes="(max-width: 785px) 100vw, 785px" /></p>
    <p><strong>Securing communication protocol:</strong></p>
    <p><strong>Secure communication protocol</strong> must have each of the following properties:</p>
    <ol>
    <li><strong>Privacy </strong>– only the intended receiver is able to read the message</li>
    <li><strong>Authenticity</strong> – the identity of communicating parties is proven</li>
    <li><strong>Integrity</strong> – confirmation that the message has not been changed in transit</li>
    </ol>
    <p>If any one this fails – the whole protocol fails!</p>
    <p><strong>Man in the Middle attack on HTTP</strong></p>
    <p>In computer networking, the attacker can easily gain MitM position using a technique called ARP spoofing. Anyone on your Wi-Fi can send you spoofed ARP packets and you will unknowingly start sending all your traffic through the attacker instead of the router.</p>
    <p>The attacker can then sniff, modify or stop all the traffic. He usually wants you to continue browsing so he will setup a specific port which he will use to forward your requests back and forth.</p>
    <p><img class="wp-image-15791 aligncenter" src="/imgs/2016/10/word-image-19.png" srcset="/imgs/2016/10/word-image-19.png 580w, /imgs/2016/10/word-image-19-300x127.png 300w" sizes="(max-width: 580px) 100vw, 580px" /></p>
    <p>To prevent such attacks, secure version of HTTP protocol was created. Transport Layer Security (TLS) and it&#8217;s predecessor, Secure Socket Layer (SSL) are cryptographic protocols that provide communications security over the network. Both are frequently referred to as SSL and that&#8217;s what I will call it; HTTPS means HTTP protocol implemented through SSL. You can instruct your browser to use SSL by requesting <a href="https://www.deepdotweb.com">https://www.deepdotweb.com</a> (notice the &#8216;s&#8217; in http<strong>s</strong>).</p>
    <p><strong>Man in the Middle attack on poorly implemented SSL</strong></p>
    <p>Modern SSL uses good encryption algorithm, but it means nothing if implemented incorrectly. Since the attacker can change the request he is intercepting, he can easily remove &#8216;s&#8217; from the requested URL which allows the attacker to prevent SSL from ever being used.</p>
    <p>You can notice that your connection is being intercepted. If you request http<strong>s</strong>://login.yahoo.com/ and the response is http://login.yahoo.com/ you should get suspicious. This simple attack really works on yahoo email login server at the time of writing.</p>
    <p><img class="wp-image-15792 aligncenter" src="/imgs/2016/10/word-image-20.png" srcset="/imgs/2016/10/word-image-20.png 620w, /imgs/2016/10/word-image-20-300x161.png 300w" sizes="(max-width: 620px) 100vw, 620px" /></p>
    <p>To prevent this version of attack, servers can implement HTTP Strict Transport Security (HSTS) which simply forces all connections to go through SSL. If the attacker strips &#8216;s&#8217; in this version, server will not respond with a webpage, but with 302 redirect to protected version (SSL).</p>
    <p><img class="wp-image-15793 aligncenter" src="/imgs/2016/10/word-image-21.png" srcset="/imgs/2016/10/word-image-21.png 656w, /imgs/2016/10/word-image-21-300x187.png 300w" sizes="(max-width: 656px) 100vw, 656px" /></p>
    <p>This way of implementing SSL is vulnerable to another practical attack – the attacker creates SSL connection to the server, but tricks user into using HTTP.</p>
    <p><img class="wp-image-15794 aligncenter" src="/imgs/2016/10/word-image-22.png" srcset="/imgs/2016/10/word-image-22.png 898w, /imgs/2016/10/word-image-22-300x72.png 300w" sizes="(max-width: 898px) 100vw, 898px" /></p>
    <p>To prevent such attacks, modern browsers such as Chrome, Firefox and Tor keep track of websites that use HSTS and force SSL connection to them from the client side. Now, the man in the middle has to create SSL connection to the victim. If the attacker has no access to the victim&#8217;s browser, MitM has to act as a server in SSL protocol (which is not easy to achieve):</p>
    <p><img class="wp-image-15796 aligncenter" src="/imgs/2016/10/word-image-23.png" srcset="/imgs/2016/10/word-image-23.png 499w, /imgs/2016/10/word-image-23-300x151.png 300w" sizes="(max-width: 499px) 100vw, 499px" /></p>
    <p>To provide SSL connection to the victim, attacker has to know how to act as a server so let&#8217;s dig into technicalities of SSL.</p>
    <p><strong>Understanding SSL:</strong></p>
    <p>Let&#8217;s take a look through hacker&#8217;s eyes. Compromising any communication protocol comes down to attacking the weakest link of mentioned three properties (privacy, integrity and authenticity).</p>
    <p>SSL uses asymmetric encryption algorithm as opposed to symmetric. In symmetric encryption, same key is used to encrypt and decrypt the data. This is bad for internet protocols because the attacker can always sniff the key during handshake (part where communicating parties choose the key).</p>
    <p>Asymmetric encryption involves 2 keys for each participant: public key used for encrypting and corresponding private key used for decrypting data. All you have to do is tell everyone to use your public key and everyone can send an encrypted message only you will be able to decrypt.</p>
    <p><img class="wp-image-15797 aligncenter" src="/imgs/2016/10/word-image-24.png" srcset="/imgs/2016/10/word-image-24.png 250w, /imgs/2016/10/word-image-24-55x55.png 55w, /imgs/2016/10/word-image-24-50x50.png 50w" sizes="(max-width: 250px) 100vw, 250px" /></p>
    <p>How SSL provides the three properties needed for secure communication?</p>
    <ol>
    <li>The connection is <strong>private</strong> because asymmetric cryptography is used to encrypt the data transmitted. This encryption is not something an average Joe can break so an attacker cannot modify the communications without being detected – <strong>integrity.</strong></li>
    <li>Server <strong>authenticates</strong> itself to the client by sending SSL Certificate signed by Certificate Authority (CA) &#8211; a trusted third party. Certificates rely on the fact that only the valid server will have the private key.</li>
    </ol>
    <p>If the attacker somehow gets the certificate, he can gain MitM position. Attacker will create 2 SSL connections: one with the server and one with the victim. Server thinks he&#8217;s normal client and the victim has no way of detecting the attacker because he provided a certificate &#8216;proving&#8217; that he is the server.</p>
    <p>Your messages are end-to-end encrypted, except on the attacker&#8217;s computer where he has full control! This can also improve mentioned attacks because there is no missing &#8216;s&#8217;.</p>
    <p><img class="wp-image-15798 aligncenter" src="/imgs/2016/10/word-image-25.png" srcset="/imgs/2016/10/word-image-25.png 620w, /imgs/2016/10/word-image-25-300x161.png 300w" sizes="(max-width: 620px) 100vw, 620px" /></p>
    <p>If everything is implemented correctly, the attacker&#8217;s best shot lies in manipulating certificates.</p>
    <p>A certificate doesn&#8217;t have to be forged if the attacker compromises the victim&#8217;s browser. In that case he can insert a self-signed certificate to be trusted by default. That&#8217;s how the most MitM attacks are done. In other cases, the attacker has to take a bigger challenge – forging a certificate.</p>
    <p><strong>Problems with Certificate Authorities</strong></p>
    <p>Certificates the server sends to you are issued and signed by Certificate Authorities. Each browser has the list of trusted CAs and you can add or remove any. The problem here is that if you choose to remove for example 3<sup>rd</sup> biggest authority, you can&#8217;t visit any sites that use their certificates because of HSTS or risk of MitM attack.</p>
    <p>Certificates and CAs have always been the weakest link of HTTPS connection. Even if everything was implemented correctly and every CA is hackerproof, I still can&#8217;t get over the fact that I have to trust some set of people.</p>
    <p>Today, that set of people are 650+ organizations capable of issuing certificates – a number I&#8217;m sure many of us are not okay with. If any of those get hacked, attacker will get himself all certificates he desires.</p>
    <p>Even when there was a single CA, VeriSign, there was an absurd problem – those people that we are supposed to trust to prevent MitM attacks on internet communication &#8211; were selling intercept <a href="https://cryptome.org/verispy.htm">services</a>.</p>
    <p>Many certificates were created by hacking CAs on so many levels. Countless exploits have been used to trick the victim in trusting fraudulent certificates. If you are interested in this topic I recommend you to watch Moxie Marlinspike&#8217;s talks at DEFCON about it.</p>
    <p><strong>Forensics</strong></p>
    <p>Because attacker is sending spoofed ARP packets, you will not see his IP address anywhere, but you should look for MAC address which is specific for each piece of hardware on the network. If you know your router MAC you can compare it with the MAC address of your default gateway to see if it is truly your router or an intruder.</p>
    <p>On windows for example you can use &#8220;ipconfig&#8221; command in cmd terminal to see your default gateway IP address (last line):</p>
    <p><img class="wp-image-15799 aligncenter" src="/imgs/2016/10/word-image-26.png" srcset="/imgs/2016/10/word-image-26.png 653w, /imgs/2016/10/word-image-26-300x215.png 300w" sizes="(max-width: 653px) 100vw, 653px" /></p>
    <p>Then use &#8220;arp –a&#8221; command to see the MAC address (Physical Address) of that gateway:</p>
    <p><img class="wp-image-15800 aligncenter" src="/imgs/2016/10/word-image-27.png" srcset="/imgs/2016/10/word-image-27.png 500w, /imgs/2016/10/word-image-27-300x64.png 300w" sizes="(max-width: 500px) 100vw, 500px" /></p>
    <p>When you don&#8217;t know the router MAC address, you can still notice the attack if you have been monitoring (or logging) the network activity while the attack started by watching out for ARP packets. You can use Wireshark to monitor and log the network activity. If you have reason to believe someone will try a MitM attack, it&#8217;s not crazy to run an automated tool that notifies you if the MAC address of default gateway changes.</p>
    <p>Note: if the attacker correctly spoofs the MAC address, forensics become a big challenge.</p>
    <p><strong>Conclusion </strong></p>
    <p>SSL is a good protocol because it forces an attacker to do a lot of work if he wants to sniff on your confidential data, but it doesn&#8217;t guard you from state-sponsored attacks or skilled hacking organizations.</p>
    <p>As a regular privacy-concerned internet user, your job is to protect your browser and personal computer to prevent inserting fake certificates as trusted (very common technique). The other thing you should consider is going through the list of trusted Certificate Authorities and removing those you don&#8217;t trust.</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/attacks/" rel="tag">attacks</a> <a href="https://www.deepdotweb.com/tag/man/" rel="tag">man</a> <a href="https://www.deepdotweb.com/tag/middle/" rel="tag">middle</a></span> <span style="display:none" class="updated">2016-10-10</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/filipjelic/" title="Posts by Filip Jelic" rel="author">Filip Jelic</a></strong></div>
    
