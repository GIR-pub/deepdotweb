---
How Hackers Avoid Honeypots
---
<article class="post-listing post-22492 post type-post status-publish format-standard has-post-thumbnail hentry 
tag-avoid tag-hackers tag-honeypots">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/theinnocent/" title="">TheInnocent </a></span>
    <span>September 11, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/09/11/hackers-avoid-honeypots/#comments">1 Comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>&nbsp;</p>
    <p>Honeypots are networks, servers or web applications purposely built to appear vulnerable, thus showing obsolete operating systems and software, open services and ports, in order to attract malign visitors and induce them to try exploiting the system. While in a preceding <a href="https://www.deepdotweb.com/2017/08/24/how-to-setup-your-own-honeypot/">tutorial</a> I explained how to build your own honeypot, here I will explain how hackers try to avoid them, what shrewdness they can apply when surfing the internet looking for victims and how you can fall victim of a honeypot surfing the deep web. Finally we’ll talk about how enterprises system administrators deal with fake access points put in the enterprise’s networks just to steal juicy sensitive data.<img class="wp-image-22495 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/09/word-image-26.png" width="695" height="188" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/09/word-image-26.png 1200w, https://www.deepdotweb.com/wp-content/uploads/2017/09/word-image-26-300x81.png 300w, https://www.deepdotweb.com/wp-content/uploads/2017/09/word-image-26-1024x276.png 1024w" sizes="(max-width: 695px) 100vw, 695px" /></p>
    <h2>Scan The Honeypot</h2>
    <p>You are a hacker, so then all you do is scan IPs every night to search vulnerabilities and open ports don’t you? So fire up your trustworthy nmap and begin to scan your victim as you would normally do with any other victim. Now, if you see a result like the subsequent, you should really become very suspicious:</p>
    <p><img class="wp-image-22496 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/09/word-image-27.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/09/word-image-27.png 638w, https://www.deepdotweb.com/wp-content/uploads/2017/09/word-image-27-300x173.png 300w" sizes="(max-width: 638px) 100vw, 638px" /></p>
    <p>As you can see, too many open ports are showed in the nmap result. A modern server, probably firewalled, it would never appear like this, so this is the moment in which you start thinking you’re right in front of a trap purposely prepared for you. Another signal would be an extremely obsolete operating system. Performing a banner grabbing with Netcat would show (for example) a similar result:</p>
    <p><img class="wp-image-22497 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/09/word-image-28.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/09/word-image-28.png 665w, https://www.deepdotweb.com/wp-content/uploads/2017/09/word-image-28-300x159.png 300w" sizes="(max-width: 665px) 100vw, 665px" /></p>
    <p>A fairly old version of Apache as you can see.</p>
    <h2>Deep Web Honeypots</h2>
    <p>It is possible to encounter several kinds of honeypots surfing the deep web, but we can consider two main typologies: a honeypot made by federal agents or a honeypot made by phishers.</p>
    <p>Federal agents build honeypots that can simulate drug markets to child-pornography sites, so the criminals connect to them and they are easily caught.</p>
    <p>Phishers instead, can build a site that acts like the legitimate one, just to present to you a fake login form that will steal your credentials, or other personal informations.</p>
    <p>Well, there are both methods to recognize honeypots and protect yourself from them, but you will see that the second option will be easier for you, as honeypots are often very well developed and difficult to recognize. In order to find out if you’re visiting a honeypot is to always check the URL. Often malicious URLs differ from the benign ones only for a letter; taking your time to check the URL, can save your life! Beyond this, if a trusted website you know starts to ask you for your credentials or even money that it never required before, you should become suspicious as well. There are also methods to avoid the traps: never give away personal informations on a darknet and never click on links shared by anyone. These links can bring you to a fake site or can download <a href="https://www.deepdotweb.com/2017/08/18/malicious-websites-explained/">malicious</a> software on your machine! Also check for malicious sites looking at the <a href="https://www.spamhaus.org/dbl/">DBL</a> (Domain Block List) site, where hundreds of malicious sites are listed.</p>
    <h2>Hide Your Identity To Honeypots</h2>
    <p>You really should know these few things if you’re surfing the <a href="https://www.deepdotweb.com/">deep web</a> but I will tell you the same:</p>
    <ul>
    <li>Always use a VPN</li>
    <li>Always use TOR</li>
    <li>Use a fake identity</li>
    <li>Never give away personal informations that can make someone link your fake identity to your real one</li>
    <li>Do not download software, open executable software, images, PDFs or any other file if it does not come from a VERY trusted source</li>
    <li>If you’re really serious about privacy, use <a href="https://www.whonix.org/">Whonix</a>.</li>
    </ul>
    <h2>Study Honeypots</h2>
    <p>You really should install any honeypot you encounter on the web just to become familiar with their settings. In fact, if the honeypot’s owner is lazy, he will have the default settings on his trap. If you know how the default configuration of (let’s say) KFSensor looks like, you will easily recognize it when you’ll encounter it. The following is a list of very common honeypots you should try to download and install to study their default settings:</p>
    <ul>
    <li>KFSensor</li>
    <li>Honeyd</li>
    <li>Artillery</li>
    <li>Dionaea</li>
    <li>Glastopf</li>
    <li>Kippo</li>
    <li>LaBrea</li>
    <li>PentBox</li>
    </ul>
    <p>Also check <a href="https://github.com/paralax/awesome-honeypots">this awesome list</a> to find more.</p>
    <h2>Internal Network’s Honeypots</h2>
    <p>You are inside an internal network and you suspect someone is running a honeypot. How could you discover it? Unfortunately if you want to avoid being detected you cannot run a vulnerability scan neither nmap, you can only listen for suspicious activity. With an ARP scan you can link any IP to the respective host and then you can fire up Wireshark to sniff for NetBios name requests. From wikipedia:</p>
    <p><em>“</em><strong><em>NetBIOS</em></strong><em> is an acronym for </em><strong><em>Network Basic Input/Output System</em></strong><em>. It provides services related to the </em><a href="https://en.wikipedia.org/wiki/Session_layer"><em>session layer</em></a><em> of the </em><a href="https://en.wikipedia.org/wiki/OSI_model"><em>OSI model</em></a><em> allowing applications on separate computers to communicate over a </em><a href="https://en.wikipedia.org/wiki/Local_area_network"><em>local area network</em></a><em>. As strictly an </em><a href="https://en.wikipedia.org/wiki/Application_programming_interface"><em>API</em></a><em>, NetBIOS is not a </em><a href="https://en.wikipedia.org/wiki/Networking_protocol"><em>networking protocol</em></a><em>. Older </em><a href="https://en.wikipedia.org/wiki/Operating_system"><em>operating systems</em></a><em>[</em><a href="https://en.wikipedia.org/wiki/Wikipedia:Please_clarify"><em>clarification needed</em></a><em>] ran NetBIOS over </em><a href="https://en.wikipedia.org/wiki/IEEE_802.2"><em>IEEE 802.2</em></a><em> and </em><a href="https://en.wikipedia.org/wiki/IPX/SPX"><em>IPX/SPX</em></a><em> using the </em><a href="https://en.wikipedia.org/wiki/NetBIOS_Frames_protocol"><em>NetBIOS Frames</em></a><em> (NBF) and </em><a href="https://en.wikipedia.org/w/index.php?title=NetBIOS_over_IPX/SPX&amp;action=edit&amp;redlink=1"><em>NetBIOS over IPX/SPX</em></a><em> (NBX) protocols, respectively. In modern networks, NetBIOS normally runs over </em><a href="https://en.wikipedia.org/wiki/TCP/IP"><em>TCP/IP</em></a><em> via the </em><a href="https://en.wikipedia.org/wiki/NetBIOS_over_TCP/IP"><em>NetBIOS over TCP/IP</em></a><em> (NBT) protocol. This results in each computer in the network having both an </em><a href="https://en.wikipedia.org/wiki/IP_address"><em>IP address</em></a><em> and a NetBIOS name corresponding to a (possibly different) host name.”</em></p>
    <p>It is highly unlikely therefore, that a NetBios request comes from the honeypot workstation. So any host without a NetBios name could potentially be a honeypot.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/avoid/" rel="tag">avoid</a> <a href="https://www.deepdotweb.com/tag/hackers/" rel="tag">hackers</a> <a href="https://www.deepdotweb.com/tag/honeypots/" rel="tag">honeypots</a></span> <span style="display:none" class="updated">2017-09-11</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/theinnocent/" title="Posts by TheInnocent" rel="author">TheInnocent</a></strong></div>
    </div>
</article>

