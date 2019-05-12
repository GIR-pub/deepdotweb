---
Anti-DDoS ways for VPS and Dedicated Servers
---
<article class="post-listing post-23630 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news category-news-updates tag-antiddos tag-dedicated tag-servers tag-vps tag-ways">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/anony/" title="">Anonymous </a></span>
    <span>November 22, 2017</span>
    <span>in <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://www.deepdotweb.com/category/news-updates/" rel="category tag">News Updates</a></span>
    <span><a href="https://www.deepdotweb.com/2017/11/22/anti-ddos-ways-for-vps-and-dedicated-servers/#comments">2 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>DDos (Distributed Denial of Service) attacks have become a major threat to current computer networks.</p>
    <p>If your website goes down due to an overload of website traffic, you’re probably a victim of the notorious distributed denial of service (DDoS) attack. DDoS attacks have become a nightmare for companies with an active online presence. From BBC to Twitter and from Donald Trump’s website to Netflix, 2016 saw some of the most unprecedented cyber attacks in the history of the Internet.</p>
    <p>In the ever-changing world of high-tech gadgets and rising popularity of Internet of Things, <a href="https://www.deepdotweb.com/2017/11/05/fbi-asks-businesses-report-ddos-attacks/">DDoS attacks</a> have increased 2.5 times over the last 3 years, and are believed to become increasingly frequent in the coming years.</p>
    <p>One thing is certainly true: A <a href="https://www.deepdotweb.com/2017/11/03/ddos-attack-explained/">DDoS</a> can bring your business to a halt and cause it to go offline in few minutes. Simply put, any visitor will not be able to access your website.</p>
    <p>This is because these attacks overwhelm a server’s resources and/or bandwidth to stop users from accessing their desired online applications.</p>
    <p>Typically, it involves using multiple external systems to flood the target system with requests with the intention of overwhelming the system with network traffic. These attacks work because an unprotected system may find it difficult to differentiate between genuine traffic and DDoS traffic.</p>
    <p>It is a good idea to also be aware of the actual risk of suffering a DDoS attack, before investing any of your money on an Anti-DDoS solution.</p>
    <p>To have a better understanding on DDoS attacks, this article provides an overview on existing DDoS attacks and major defense technologies in the Internet and we will discuss an effective solutions to safeguarding your server against future DDoS attacks.</p>
    <p>First of all if you are using a Virtual Private Server (VPS) or Cloud Server, then this will help you understand which open source software you can use to prevent DDoS attacks.</p>
    <p><strong>1. DDos Deflate</strong>: is a lightweight open source shell script that you can easily implement on your server and configure to mitigate most DDoS attacks.</p>
    <p>Here are some of the features of DDoS Deflate:</p>
    <ul>
    <li>It can automatically detect rules within iptables or an Advanced Policy Firewall (APF).</li>
    <li>Ability to block IP addresses temporarily (the default setting is 30 mins).</li>
    <li>Whitelist and blacklist features for blocking or allowing connections to the server.</li>
    <li>Management features to notify administrator of actions taken.</li>
    </ul>
    <p><strong>2. Fail2ban</strong>: works in a similar way to DDoS Deflate, as it also bans traffic based on malicious IP address profiling.</p>
    <p>It’s a good performer and some of the main features are as follows:</p>
    <ul>
    <li>Easy to configure with some automation features included.</li>
    <li>Compatible with existing firewalls, e.g. iptables.</li>
    <li>Customizable blacklisting and whitelisting features.</li>
    <li>Ability to block automated brute force attacks.</li>
    <li>Time-based IP blocking.</li>
    </ul>
    <p><strong>3. Apache mod_evasive module</strong>: the mod_evasive module is suited to protecting Apache web servers against DDoS attacks. It also includes notification features via email and SYSLOG.</p>
    <p>This module is a strong performer, which has the added benefit of adapting to real time situations by creating rules on the fly based on the following patterns being detected:</p>
    <ul>
    <li>Requesting access to the same page too many times per second.</li>
    <li>Making 50 concurrent connections to the same child process per second.</li>
    <li>Making other requests from blacklisted IP addresses.</li>
    <li>Some of the features which are available to prevent DDoS attacks are as follows:</li>
    <li>The server administrator can limit access to certain pages based on the number of requests one particular IP can make (DOSPageCount option).</li>
    <li>Access to an entire website can be limited based on how many connections one particular IP makes using the DOSSiteCount option.</li>
    <li>The DOSHashTable feature can monitor who is accessing what in the web server based on their previous visits and can make a decision whether to allow or block the connection.</li>
    <li>The administrator can be notified via email of what action Apache mod_evasive is taking.</li>
    </ul>
    <p>Mod_evasive is relatively easy to use and because the open source modules are built into Apache, it’s free to use.</p>
    <p><strong>4. HaProxy</strong>: is an excellent open source load balancing tool that is also effective against DDoS attacks against a cloud server.</p>
    <p>It has the following features:</p>
    <ul>
    <li>It can block traffic based on the bandwidth.</li>
    <li>Contains blacklist and whitelist tables of IPs which it builds into its configuration based on the rule set.</li>
    <li>Ability to block IPs which might be performing DDoS attacks.</li>
    <li>HaProxy can identify bots, which is why it’s effective against DDoS attacks.</li>
    <li>Can prevent Syn Flood type attacks as well as capabilities like connection limitations etc.</li>
    </ul>
    <p>there very effective solution for Anti-Ddos called DDoS Protected VPS which is a VPS with DDoS mitigation included. This is also named an ‘Anti-DDOS VPS’, indicating that it is situated on a server or server farm that is hardened against DDoS attacks.</p>
    <p>This requires a high data transmission limit. It also requires solid hardware firewalls that can halt a DDoS attack in its steps, before it can get up to any mischief.</p>
    <p>A DDoS Protected VPS should be capable of resisting the common types of DDOS attacks listed below:</p>
    <ul>
    <li>DDoS volumetric attacks (a fake traffic flood.)</li>
    <li>Protocol-based attacks (malicious traffic which affects the way data is transferred.)</li>
    <li>Attacks on a specific server or user applications (e.g. WordPress.)</li>
    <li>Most cheap hosting providers do not include protection against DDoS attacks. This is because it leads to higher running costs.</li>
    <li>Types of DDoS Attacks can be stopped with a DDoS Protected VPS</li>
    <li>ICMP (Ping) Flood</li>
    <li>UDP Flood</li>
    <li>Ping of Death</li>
    <li>HTTP Flood</li>
    <li>SYN Flood</li>
    </ul>
    <p><strong>Defenses in Transit Networks</strong></p>
    <p>DDoS defense mechanisms deployed at the intermediate network provide infrastructural defense to a large number of Internet hosts. They usually ask routers to collaboratively monitor and exchange certain information to defend against DDoS attacks. Distributed congestion puzzle:</p>
    <p>Client puzzles have been proposed to defend against DoS attacks in TCP, SYN cookie, authentication protocols, graphic Turing test, application traffic control&#8230;etc.</p>
    <p>In brief, when a client requests a service, the server first asks the client to solve a problem before accepting the service request. Then, the client needs to send an answer back to the server.</p>
    <p>Usually, solving the problem takes a certain amount of computing resource, while resource demand for verifying an answer is negligible. The server will discard service requests if either the client does not reply or the answer is incorrect.</p>
    <p><strong>Pushback</strong>:</p>
    <p>Proposed aggregate-based congestion control (ACC) method that manages packet flows at a finer granularity. An aggregate is defined as a collection of packets that share some properties. ACC provides a mechanism for detecting and controlling aggregates at a router using attack signatures and a pushback mechanism to propagate aggregate control requests (and attack signatures) to upstream routers. ACC mechanisms are triggered when a router experiences sustained congestion. The router first attempts to identify the aggregates responsible for the congestion. Then, the router asks its adjacent upstream routers to rate-limit the aggregates. Since the neighbors sending more traffic within the aggregate are more likely to be carrying attack traffic, this request is sent only to the neighbors that send a significant fraction of the aggregate traffic. The receiving routers can recursively propagate pushback further upstream.</p>
    <p><strong>IP Traceback:</strong></p>
    <p>Packets forwarded by routers can carry information to help victims reconstruct the attack path.</p>
    <p>Routers can add extra information as a header or an extra payload to packets so that the border router of the victim can identify the routes close to the attacking sources and ask these routers to filter flooding packets. Routers can also embed information into IP headers to help victims trace back the true attacking sources.</p>
    <p>Here&#8217;s some tips to protect yourself from DDoS attacks:</p>
    <ul>
    <li>Create an Action Plan in Advance</li>
    <li>Monitor Traffic Levels</li>
    <li>Pay Attention to Connected Devices</li>
    <li>Ensure You Have Extra Bandwidth</li>
    <li>Train Your Customers On Security</li>
    <li>Block Spoofed IP Addresses</li>
    <li>Install Patches and Updates Frequently</li>
    <li>Aggressively Monitor Half-Open Connections</li>
    <li>Setup RST Cookies</li>
    <li>Filter UDP Traffic With Remote Black Holing</li>
    <li>Schedule stress test to your server</li>
    </ul>
    <p>I recommend to install <strong>nShield</strong> is An Easy and Simple Anti-DDoS solution for VPS,Dedicated Servers and IoT devices based on iptables.</p>
    <p>Blocking from Xmass Scan, Smurf, ICMP Attack and Syn Floods. Requirements:</p>
    <ol>
    <li>Linux System with python, iptables</li>
    <li>Nginx (Will be installed automatically by install.sh)</li>
    </ol>
    <p>Attention This script will replace all your iptables rules and installs Nginx so take that into account.</p>
    <p><strong>Usage</strong>:<br />
    
    <div id="crayon-5c8bc8c41d174688459253" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    git clone https://github.com/fnzv/nShield.git &amp;&amp; bash nShield/install.sh
    
    sudo python nshield-main.py -dry
    
    sudo python nshield-main.py -ssl</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5c8bc8c41d174688459253-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5c8bc8c41d174688459253-2">2</div><div class="crayon-num" data-line="crayon-5c8bc8c41d174688459253-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5c8bc8c41d174688459253-4">4</div><div class="crayon-num" data-line="crayon-5c8bc8c41d174688459253-5">5</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5c8bc8c41d174688459253-1"><span class="crayon-e">git </span><span class="crayon-r">clone</span><span class="crayon-h"> </span><span class="crayon-v">https</span><span class="crayon-o">:</span><span class="crayon-c">//github.com/fnzv/nShield.git &amp;&amp; bash nShield/install.sh</span></div><div class="crayon-line crayon-striped-line" id="crayon-5c8bc8c41d174688459253-2">&nbsp;</div><div class="crayon-line" id="crayon-5c8bc8c41d174688459253-3"><span class="crayon-e">sudo </span><span class="crayon-e">python </span><span class="crayon-v">nshield</span><span class="crayon-o">-</span><span class="crayon-v">main</span><span class="crayon-sy">.</span><span class="crayon-v">py</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-e">dry</span></div><div class="crayon-line crayon-striped-line" id="crayon-5c8bc8c41d174688459253-4">&nbsp;</div><div class="crayon-line" id="crayon-5c8bc8c41d174688459253-5"><span class="crayon-e">sudo </span><span class="crayon-e">python </span><span class="crayon-v">nshield</span><span class="crayon-o">-</span><span class="crayon-v">main</span><span class="crayon-sy">.</span><span class="crayon-v">py</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-v">ssl</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/antiddos/" rel="tag">antiddos</a> <a href="https://www.deepdotweb.com/tag/dedicated/" rel="tag">dedicated</a> <a href="https://www.deepdotweb.com/tag/servers/" rel="tag">servers</a> <a href="https://www.deepdotweb.com/tag/vps/" rel="tag">vps</a> <a href="https://www.deepdotweb.com/tag/ways/" rel="tag">ways</a></span> <span style="display:none" class="updated">2017-11-22</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/anony/" title="Posts by Anonymous" rel="author">Anonymous</a></strong></div>
    </div>
</article>

