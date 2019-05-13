---
Botnets and the Deep Web
---
<article class="post-listing post-19602 post type-post status-publish format-standard has-post-thumbnail hentry  tag-botnets tag-deep tag-web">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>May 3, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/05/03/botnets-deep-web/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>A bot is a special form of malware that is considered one of today&#8217;s most sophisticated tools of cybercrime. They enable hackers to control a large number of computers simultaneously, and turn them into an army of &#8220;zombie&#8221; machines, that operate collectively as a powerful &#8220;botnet&#8221; to create spam, and commit various forms of malicious activities.</p>
    <p><strong>What is a botnet?</strong></p>
    <p>A botnet is usually comprised of a large number of infected victim machines located across various parts of the globe. Given the fact that botnet infected machines will perform the computational operations ordered by its master, these victim machines are sometimes referred to as &#8220;zombies&#8221;. The hacker that controls these botnets is known as a botmaster or a botherder.</p>
    <p>Some botnets are composed of a few hundred or a few thousands of victim machines, while others may reach up to 500,000 of zombies at the disposal of their botmasters. In most cases, the victim won&#8217;t even known that his/her machine is infected with a bot. Some possible manifestations of a bot infection include slowing down of your computer, display of strange messages or even total crash of your machine.</p>
    <p><img class="wp-image-19607 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-5.jpeg" width="726" height="545" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-5.jpeg 1430w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-5-300x225.jpeg 300w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-5-1024x768.jpeg 1024w" sizes="(max-width: 726px) 100vw, 726px" /></p>
    <p>Bots are usually silently installed on victims&#8217; machines via a number of ways. They spread across the internet via seeking and infecting unprotected, vulnerable machines. After infecting a vulnerable machine, the bot reports back to the botmaster the IP address of the victim. The aim is for the bots to remain quiescent until ordered to carry out a specific task by their botmaster at a specific time in the future. After a computer is enslaved by a bot, it becomes part of the botherder&#8217;s botnet network and can be used by him/her to carry out a myriad of tasks including:</p>
    <p>1. Sending spam email, viruses and spyware.</p>
    <p>2. Phishing of private and personal information and sending it back to the botmaster including credit card numbers, bank account data and other forms of private personal information.</p>
    <p>3. <a href="https://www.deepdotweb.com/2016/11/06/analysis-record-ddos-attacks-mirai-iot-botnet/">DDoS (Distributed Denial of Service) attacks</a>. Planning DDoS attacks can be facilitated by botnets against a predefined target. Black hat hackers blackmail website owners, via DDoS attacks to extort money from them, in exchange for cessation of the attack and giving the owners control back over their websites. However, DDoS attacks are often launched against individuals&#8217; PCs, or other forms of machines connecting to the internet via targeting their IP addresses. The botmaster will order all enslaved machines, i.e. machines infected by the bots, to go to the website at the same time to launch a DDoS attack.</p>
    <p>4. Click Fraud: Botmasters can use bots to direct the victim machines to pay per click (PPC) ads as the bots deceivingly impersonate real internet users, so the botmaster can make a large amount of money, especially if he/she manages to control a large number of machines via the bot.</p>
    <p>5. Mining cryptocurrency: botmasters can code their botnets to mine bitcoin or altcoins. In 2015, uTorrent, the most widely used bittorrent client, was found to silently install a bot that mined bitcoin. Back then, uTorrent users experienced marked slowing down of their PCs, as bitcoin mining utilizes enormous processing power.</p>
    <p><strong>Botnets and the Deep Web:</strong></p>
    <p>A botmaster has to carefully hide the Command and Control servers (C&amp;C) of his/her botnet and network traffic from and to these servers to avoid discovery and/or takeover of the malicious structure of the botnet. Nowadays, most botmasters choose to conceal their Command and Control servers on the Tor network. The following represent the advantages of botnets based on the Tor network:</p>
    <ul>
    <li>High availability and low down times of authenticated hidden Tor services.</li>
    <li>Reasonable availability of private Tor networks.</li>
    <li>Exit node flooding capabilities.</li>
    </ul>
    <p>Traffic analysis is usually done by Law Enforcement Agencies (LEAs) to detect various activities related to botnets and pinpoint their C&amp;C servers. Practically speaking, this is done via utilizing network analyzers and Intrusion Detection Systems. Once detected, LEAs have various options to eradicate a botnet:</p>
    <ul>
    <li>Blocking the IP addresses of the C&amp;C server.</li>
    <li>Cleaning the server used to host the botnet and other compromised hosts.</li>
    <li>Revoking domain name(s).</li>
    <li>De-peering of the hosting provider.</li>
    </ul>
    <p>The botnet traffic is redirected to the C&amp;C server via the Tor network which encrypts it, rendering the analysis harder to accomplish. There are 2 botnet models based on the Tor network:</p>
    <p>Tor2Web Proxy Based Botnet Model:</p>
    <p>The routing procedure redirects .onion internet traffic via Tor2Web proxy. The bot connects to the Tor hidden service via the Tor2Web proxy which points to an onion domain that hosts the C&amp;C server.</p>
    <p>Proxy-aware Malware Via the Tor Network:</p>
    <p>This model utilizes the proxy-aware malware. As the Tor2Web service is not used, the bot has to execute the Tor clients on the victim hosts. Bots have to have SOCK55 support in order to be able to reach onion addresses on the Tor network via running Tor on infected machines.</p>
    <p>Moreover, you can <a href="https://www.deepdotweb.com/2016/12/21/zeus-botnet-successor-floki-bot-available-alphabay/">buy botnet malware on some of the marketplaces on the deep web</a>. However, if you choose to buy any malware from the deep web, you should be extremely careful, as you can get your machine infected when dealing with black hat hackers.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/botnets/" rel="tag">botnets</a> <a href="https://www.deepdotweb.com/tag/deep/" rel="tag">deep</a> <a href="https://www.deepdotweb.com/tag/web/" rel="tag">web</a></span> <span style="display:none" class="updated">2017-05-03</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

