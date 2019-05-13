---
Prevention against DDoS attacks
---
<article class="post-listing post-27352 post type-post status-publish format-standard has-post-thumbnail hentry 
tag-attacks tag-ddos tag-prevention">
<div class="post-inner">
<span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
<span>November 23, 2018</span>

<span><a href="https://www.deepdotweb.com/2018/11/23/prevention-against-ddos-attacks/#comments">2 Comments</a></span>


<p>DDoS attacks lead to the most devastating effects within a network. <a href="https://www.deepdotweb.com/2017/11/03/ddos-attack-explained/">DDoS attacks</a> are forms of congestion-control problems, and because most forms of such congestion are secondary to the effects of malicious hosts not following conventional end-to-end congestion control, the problem must be solved by routers. Designing a mechanism to counteract unidentified attacks targeting the application and transport layer represents a goal of intrusion identification and intrusion prevention techniques.</p>
<p><a href="https://www.academia.edu/37657486/Distributed_Denial_of_Service_DDOS_Attacks_Detection_Mechanism">A recently published paper</a> delved into the current tools of modern DDoS attacks and proposed a preventive technique to stop the attacks from imposing damage within a network setting. Throughout this article, we will review this interesting paper.</p>
<p><img class="wp-image-27359" src="https://www.deepdotweb.com/wp-content/uploads/2018/11/ddos-jpg.jpeg" alt="ddos.jpg" srcset="https://www.deepdotweb.com/wp-content/uploads/2018/11/ddos-jpg.jpeg 800w, https://www.deepdotweb.com/wp-content/uploads/2018/11/ddos-jpg-300x169.jpeg 300w" sizes="(max-width: 800px) 100vw, 800px" /></p>
<p><strong>DDoS attack tools:</strong></p>
<p>The following represents the DDoS attack tools represented via the paper:</p>
<p>DDOSIM:</p>
<p>DDOSIM is one of the tools commonly used for DDOS attacks. It is coded in C++ and runs on Linux. It simulates multiple compromised hosts (spoof IP addresses) and establishes full TCP connections to the victim server. The current functionalities of DDOSIM attacks include HTTP DDoS with valid requests, HTTP DDoS with invalid requests, and SMTP DDoS and TCP connection flood on a random port.</p>
<p>Slowloris:</p>
<p>Slowloris is another common tool used in modern DDoS attacks. It is different from other tools as it sends legitimate HTTP traffic. This tool does not act by flooding the victim&#8217;s server – it just makes a full TCP connection and then requires no more than several hundred requests at long term and regular intervals. This tool attempts to exhaust all connections which will render hackers capable of undermining the victim’s server.</p>
<p>DAVOSET:</p>
<p>DAVOSET is a tool for launching DDoS attacks on sites by means of the abuse of functionality and XML External Entities’ vulnerabilities on other sites.</p>
<p>HYENAE:</p>
<p>The HYENAE tool allows <a href="https://www.deepdotweb.com/2018/09/03/interview-with-a-professional-ddos-extortionist/">attackers to replicate several MITM, Dos and DDoS attack scenarios</a> and, along with an interactive attack assistant, it is also associated with a clusterable remote daemon. The features of Hyenae’s include ARP-Request flooding, ICMP-Echo flooding, ARP-Cache poisoning, and others.</p>
<p><strong>Proposed system for prevention of DDoS attacks:</strong></p>
<p>The paper proposed a system for <a href="https://www.deepdotweb.com/2017/11/22/anti-ddos-ways-for-vps-and-dedicated-servers/">preventing DDoS attacks</a> via filtering the outgoing packets from the network&#8217;s local server by means of Deep Packet Inspection (DPI). Whenever malicious data or an entity has been detected, the IP from which the particular request was sent is spotted and the corresponding IP address is blocked with the IP blocking method.</p>
<p>Deep Packet Inspection represents a type of data processing which closely examines the contents of the sent data (i.e. it monitors the payload of the packet). It is used to check whether the sent packet provides content free of viruses and other forms of malicious content. Various headers exist for IP packets; only the usage of the first header (the IP header) is required by network equipment for normal operation. Use of second headers, such as the TCP and UDP headers, is generally deemed as shallow packet inspection. There are multiple methods through which the packet for Deep Packet Inspection can be acquired, and one such method is port mirroring. DPI enables advanced network protection, user service, and other security functions. For many years, DPI has been implemented for internet management. DPI is also used in a variety of other applications – including at the &#8220;enterprise&#8221; level (corporations and larger institutions), in government sectors, and in telecommunications’ service providers.</p>
<p>IP address blocking acts by preventing the connection between a website or server and particular IP addresses or ranges of IP addresses. Undesired connections from hosts by means of affected addresses to a mail server, website, or other internet server are effectively stopped by IP address blocking. IP address blocking bans the connection between a website or server and specific IP addresses or ranges of IP addresses. IP address blocking works to ban unwanted connections from hosts using affected addresses to a website, mail server, or other Internet server. IP address blocking is also used to effectively guard against brute force attacks.</p>
<p><strong>Final thoughts:</strong></p>
<p>The proposed method offers an effective defense mechanism strategy against DDoS attacks, and it also prevents other forms of malicious attacks from compromising networks and websites. The main function of the proposed method is to control the traffic nature and protect servers from attackers&#8217; hosts.</p>
</div>
<span style="display:none"><a href="https://www.deepdotweb.com/tag/attacks/" rel="tag">attacks</a> <a href="https://www.deepdotweb.com/tag/ddos/" rel="tag">ddos</a> <a href="https://www.deepdotweb.com/tag/prevention/" rel="tag">prevention</a></span> <span style="display:none" class="updated">2018-11-23</span>
<div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
</div>
</article>

