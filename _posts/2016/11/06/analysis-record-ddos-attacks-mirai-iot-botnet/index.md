---
Analysis: Record DDoS Attacks by Mirai &#8211; IoT Botnet
---
<article class="post-listing post-16263 post type-post status-publish format-standard has-post-thumbnail hentry  tag-analysis tag-attacks tag-botnet tag-ddos tag-iot tag-mirai tag-record">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/filipjelic/" title="">Filip Jelic </a></span>
    <span>November 6, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/11/06/analysis-record-ddos-attacks-mirai-iot-botnet/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    
    <p>Number of Internet of Things (IoT) devices is growing exponentially over time. Internet connected cameras, thermostats, refrigerators and others were recently part of biggest Distributed Denial of Service Attack (DDoS) in the history.</p>
    <p>This article contains explanation of botnets, DDoS and analysis of recent record breaking DDoS attack by Mirai Botnet and brief analysis of the C++ source code!</p>
    <p>DDoS attack is an attempt to make an online service unavailable by overwhelming it with traffic from multiple sources. For example, if a website&#8217;s server is capable of serving 1 byte per second and a DDoS attack of 5 bytes per second is launched against your site: in the first second, 1 byte would be processed, and then the remaining 5 bytes would be queued until the next second. At first, visitors don&#8217;t have to wait too long in the queue, but as the queue becomes longer, timeouts will increase.</p>
    <p><img class="wp-image-16264 aligncenter" src="/imgs/2016/11/word-image-1.png" srcset="/imgs/2016/11/word-image-1.png 525w, /imgs/2016/11/word-image-1-300x181.png 300w" sizes="(max-width: 525px) 100vw, 525px" /></p>
    <p>Most servers today are capable of serving 1 Gbps. To recreate illustrated example, an attacker needs to request 5 Gbps from the server.</p>
    <p>Just to get a picture &#8211; $50 per month is the cost of 1Gbps server,</p>
    <p>&#8211; $300 per month is the cost of 10Gbps server.</p>
    <p><strong>How do hackers generate vast amount of traffic? </strong></p>
    <p>This is where botnets come into play. Botnet is a piece of malware that sleeps in the infected operating system waiting for a command from Command and Control (C&amp;C) center. Strength of particular botnet lies in the number of infected victims (aka bots, zombies) and devices&#8217; capability to generate traffic.</p>
    <p>Botnets that target computers are unreliable because computers are often offline or turned off so they can&#8217;t be used for an attack, meaning that the number of infected victims needs to be at least 5 times greater than the optimal.</p>
    <p>IoT devices are almost always connected to the internet and also terribly unsecure. Those 2 facts were exploited in <strong>Mirai</strong>, IoT botnet that broke the record of DDoS. This pseudonym shared the source code:</p>
    <p><img class="wp-image-16265 aligncenter" src="/imgs/2016/11/word-image-2.png" width="1073" height="287" srcset="/imgs/2016/11/word-image-2.png 1789w, /imgs/2016/11/word-image-2-300x80.png 300w, /imgs/2016/11/word-image-2-1024x274.png 1024w" sizes="(max-width: 1073px) 100vw, 1073px" /></p>
    <p>He leaked the source code in <a href="https://hackforums.net/showthread.php?tid=5420472">that post</a>, although his share links don&#8217;t work anymore so check github for the source code.</p>
    <p>&#8220;I made my money, there&#8217;s lots of eyes looking at IOT now, so it&#8217;s time to GTFO.&#8221;</p>
    <p>&#8220;With Mirai, I usually pull max 380k bots from telnet alone.&#8221;</p>
    <p><strong>IoT Devices Discovery</strong></p>
    <p>Potential victims can be found using search engines such as <a href="https://www.shodan.io/">Shodan</a> and <a href="https://censys.io/">Censys</a>. Amazing tools that search the world wide web for all devices connected to it.</p>
    <p>&#8220;Use Shodan to discover which of your devices are connected to the Internet, where they are located and who is using them.&#8221;</p>
    <p>&#8220;Websites are just one part of the Internet. There are power plants, Smart TVs, refrigerators and much more that can be found with Shodan!&#8221;</p>
    <p>Censys is a search engine that allows computer scientists to ask questions about the devices and networks that compose the Internet. Driven by Internet-wide scanning, Censys lets researchers find specific hosts and create aggregate reports on how devices, websites, and certificates are configured and deployed.</p>
    <p><strong>Actual DDoS Attacks</strong></p>
    <p>Mirai malware was used for several extremely large DDoS attacks including:</p>
    <p><a href="http://thehackernews.com/2016/09/ddos-attack-iot.html">27/9/2016</a> &#8211; with peaks over 1 Tbps from 152 000 IoT devices: 100,000 Smart TVs, Refrigerator, and other smart household appliances; rest were probably security cameras – 25 000 just from China</p>
    <p><a href="http://thehackernews.com/2016/10/iot-dyn-ddos-attack.html">21/10/2016</a> &#8211; record one, over 1Tbps against Dyn DNS server.</p>
    <p>Dyn DNS is used by many websites and services as their upstream DNS provider, including Twitter, Spotify, SaneBox, Reddit, Box, Github, Zoho CRM, PayPal, Airbnb, Freshbooks, Wired.com, Pinterest, Heroku and Vox Media properties.</p>
    <p><strong>Infrastructure</strong></p>
    <p>Although the attack is pretty simple, it requires sizeable infrastructure. Author&#8217;s recommended setup:</p>
    <p>&#8211; 1 VPS with extremely bulletproof host for database server<br />
    &#8211; 1 VPS, rootkitted, for scanReceiver and distributor<br />
    &#8211; 1 server for C&amp;C (used like 2% CPU with 400k bots)<br />
    &#8211; 3x 10gbps NForce servers for loading (distributor distributes to 3 servers equally)</p>
    <p>VPS stands for Virtual Private Server meaning that you control a server over virtual environment that is actually running on the server.</p>
    <p><strong>Mirai Analysis</strong></p>
    <p>Mirai malware is a C++ program continuously scanning the internet for IoT devices and attacks them. It tries to connect to them with <strong>default factory </strong>credentials mostly via telnet. Each device is attacked by a quick dictionary attack, trying all default credentials. Dictionary used:</p>
    <p>root xc3511</p>
    <p>root vizxv</p>
    <p>root admin</p>
    <p>admin admin</p>
    <p>root 888888</p>
    <p>root xmhdipc</p>
    <p>root default</p>
    <p>root juantech</p>
    <p>root 123456</p>
    <p>root 54321</p>
    <p>support support</p>
    <p>root (none)</p>
    <p>admin password</p>
    <p>root root</p>
    <p>root 12345</p>
    <p>user user</p>
    <p>admin (none)</p>
    <p>root pass</p>
    <p>admin admin1234</p>
    <p>root 1111</p>
    <p>admin smcadmin</p>
    <p>admin 1111</p>
    <p>root 666666</p>
    <p>root password</p>
    <p>root 1234</p>
    <p>root klv123</p>
    <p>Administrator admin</p>
    <p>service service</p>
    <p>supervisor supervisor</p>
    <p>guest guest</p>
    <p>guest 12345</p>
    <p>guest 12345</p>
    <p>admin1 password</p>
    <p>administrator 1234</p>
    <p>666666 666666</p>
    <p>888888 888888</p>
    <p>ubnt ubnt</p>
    <p>root klv1234</p>
    <p>root Zte521</p>
    <p>root hi3518</p>
    <p>root jvbzd</p>
    <p>root anko</p>
    <p>root zlxx.</p>
    <p>root 7ujMko0vizxv</p>
    <p>root 7ujMko0admin</p>
    <p>root system</p>
    <p>root ikwb</p>
    <p>root dreambox</p>
    <p>root user</p>
    <p>root realtek</p>
    <p>root 00000000</p>
    <p>admin 1111111</p>
    <p>admin 1234</p>
    <p>admin 12345</p>
    <p>admin 54321</p>
    <p>admin 123456</p>
    <p>admin 7ujMko0admin</p>
    <p>admin 1234</p>
    <p>admin pass</p>
    <p>admin meinsm</p>
    <p>tech tech</p>
    <p>mother fucker</p>
    <p>While not executing an attack command, bots are doing same search and infect method further spreading the virus.</p>
    <p>Infected devices will continue to function normally, except for occasional sluggishness and an increased use of bandwidth. After a reboot, unless the login password is changed immediately, the device will be infected within minutes.</p>
    <p><strong>Command and Control</strong></p>
    <p>Instead of hardcoding IP address, bots would resolve a domain to get the IP address of C&amp;C server. This way, IP address of the server can be changed which is very useful defensive mechanism. These commands are programmed for bots:</p>
    <p>#define CNC_OP_PING 0x00</p>
    <p>#define CNC_OP_KILLSELF 0x10</p>
    <p>#define CNC_OP_KILLATTKS 0x20</p>
    <p>#define CNC_OP_PROXY 0x30</p>
    <p>#define CNC_OP_ATTACK 0x40</p>
    <p>C&amp;C is coded in Go and it simply issues commands that bots read and translate into C++ functions.</p>
    <p><strong>Don&#8217;t Touch These List</strong></p>
    <p>One of the most interesting things revealed by the code was a hardcoded list of IPs Mirai bots are programmed to avoid when performing their scans.</p>
    <p>This list, which you can find below, includes the US Postal Service, the Department of Defense, the Internet Assigned Numbers Authority (IANA) and IP ranges belonging to Hewlett-Packard and General Electric.</p>
    <p>127.0.0.0/8 &#8211; Loopback</p>
    <p>0.0.0.0/8 &#8211; Invalid address space</p>
    <p>3.0.0.0/8 &#8211; General Electric (GE)</p>
    <p>15.0.0.0/7 &#8211; Hewlett-Packard (HP)</p>
    <p>56.0.0.0/8 &#8211; US Postal Service</p>
    <p>10.0.0.0/8 &#8211; Internal network</p>
    <p>192.168.0.0/16 &#8211; Internal network</p>
    <p>172.16.0.0/14 &#8211; Internal network</p>
    <p>100.64.0.0/10 &#8211; IANA NAT reserved</p>
    <p>169.254.0.0/16 &#8211; IANA NAT reserved</p>
    <p>198.18.0.0/15 &#8211; IANA Special use</p>
    <p>224.*.*.*+ &#8211; Multicast</p>
    <p>6.0.0.0/7 &#8211; Department of Defense</p>
    <p>11.0.0.0/8 &#8211; Department of Defense</p>
    <p>21.0.0.0/8 &#8211; Department of Defense</p>
    <p>22.0.0.0/8 &#8211; Department of Defense</p>
    <p>26.0.0.0/8 &#8211; Department of Defense</p>
    <p>28.0.0.0/7 &#8211; Department of Defense</p>
    <p>30.0.0.0/8 &#8211; Department of Defense</p>
    <p>33.0.0.0/8 &#8211; Department of Defense</p>
    <p>55.0.0.0/8 &#8211; Department of Defense</p>
    <p>214.0.0.0/7 &#8211; Department of Defense</p>
    <p><strong>DDoS Possibilities</strong></p>
    <p>For network layer assaults, Mirai is capable of launching GRE IP and GRE ETH floods, as well as SYN and ACK floods, STOMP (Simple Text Oriented Message Protocol) floods, DNS floods and UDP flood attacks.</p>
    <p><strong>Fighting Other Malware</strong></p>
    <p>The malware holds several killer scripts meant to eradicate other worms and Trojans, as well as prohibiting remote connection attempts of the hijacked device.</p>
    <p>For example, the following scripts close all processes that use SSH, Telnet and HTTP ports:</p>
    <p>killer_kill_by_port(htons(23)) // Kill telnet servicekiller_kill_by_port(htons(22)) // Kill SSH servicekiller_kill_by_port(htons(80)) // Kill HTTP service</p>
    <p>These locate/eradicate other botnet processes from memory, a technique known as memory scraping:</p>
    <p>#DEFINE TABLE_MEM_QBOT // REPORT %S:%S</p>
    <p>#DEFINE TABLE_MEM_QBOT2 // HTTPFLOOD</p>
    <p>#DEFINE TABLE_MEM_QBOT3 // LOLNOGTFO</p>
    <p>#DEFINE TABLE_MEM_UPX // \X58\X4D\X4E\X4E\X43\X50\X46\X22</p>
    <p>#DEFINE TABLE_MEM_ZOLLARD // ZOLLARD</p>
    <p><strong>Author(s) Footprints</strong></p>
    <p>Command and Control is in English, but there are some Russian strings in it for username, password etc. There is also this string &#8211; “я люблю куриные наггетсы” meaning &#8220;I love chicken nuggets&#8221;.</p>
    <p>In table.c, just above some table entries, there is this comment:</p>
    <p>// safe string <a href="https://youtu.be/dQw4w9WgXcQ">https://youtu.be/dQw4w9WgXcQ</a></p>
    <p>I will leave the conclusions about the author(s) to the readers.</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/analysis/" rel="tag">analysis</a> <a href="https://www.deepdotweb.com/tag/attacks/" rel="tag">attacks</a> <a href="https://www.deepdotweb.com/tag/botnet/" rel="tag">botnet</a> <a href="https://www.deepdotweb.com/tag/ddos/" rel="tag">ddos</a> <a href="https://www.deepdotweb.com/tag/iot/" rel="tag">iot</a> <a href="https://www.deepdotweb.com/tag/mirai/" rel="tag">mirai</a> <a href="https://www.deepdotweb.com/tag/record/" rel="tag">record</a></span> <span style="display:none" class="updated">2016-11-06</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/filipjelic/" title="Posts by Filip Jelic" rel="author">Filip Jelic</a></strong></div>
    </div>
</article>

