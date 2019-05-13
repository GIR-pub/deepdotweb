---
Important forensic tools used in harvesting the deep web
---
<article class="post-listing post-27349 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-deep tag-forensic tag-harvesting tag-important tag-tools tag-web">
<div class="post-inner">
<span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
<span>November 23, 2018</span>

<span><a href="https://www.deepdotweb.com/2018/11/23/important-forensic-tools-used-in-harvesting-the-deep-web/#respond">Leave a comment</a></span>
</p>
<div class="clear"></div>
<div class="entry">
<p>The internet, especially the dark web, has become a place where illegal activities such as fraud, the trading of illegal drugs, human trafficking, extremism, firearm smuggling, etc. take place. The legitimate concerns, including privacy and anonymity, are exploited to catalyze nefarious needs within various parts of the deep web. The anonymity and cryptographic approaches utilized by dark web visitors impose <a href="https://www.deepdotweb.com/2018/10/27/india-dsps-undergo-training-to-enhance-skills-on-cybercrime-and-dark-web-crackdown/">serious challenges for law enforcement agencies</a> to monitor, investigate, control, and prosecute criminal activities taking part in these darker parts of the internet.</p>
<p><a href="https://dl.acm.org/citation.cfm?id=3277584">A recently published paper</a> offered an overview on some of the currently used methods for identification, collection, analysis, and reporting of information obtained from the dark web in a forensically sound way. Throughout this article, we will examine some of the tools presented in this paper which are currently used in network forensic investigations.</p>
<p><img class="wp-image-27353" src="https://www.deepdotweb.com/wp-content/uploads/2018/11/digital-forensics-jpg.jpeg" alt="digital forensics.jpg" srcset="https://www.deepdotweb.com/wp-content/uploads/2018/11/digital-forensics-jpg.jpeg 900w, https://www.deepdotweb.com/wp-content/uploads/2018/11/digital-forensics-jpg-300x167.jpeg 300w" sizes="(max-width: 900px) 100vw, 900px" /></p>
<p>Even though the field of Computer Forensics and Cybercrime Investigation represents a relatively new area of research among the more conventional computer security models, there are currently some companies and opens-source communities that specialize in forensic investigations. The following represent the most commonly used tools during evidence collection of a digital investigation:</p>
<p>1- Firewall and router logs: These devices are configured so that they may record any form of suspicious activity.</p>
<p>2- Packet sniffing: This procedure enables the investigator to monitor in real time various activities taking place on a network.</p>
<p>3- Intrusion Detection Systems (IDS): Larger networks can sometimes deploy IDS to capture data packets that can be linked to suspicious activities.</p>
<p>4- Remote Access Servers: This includes devices, e.g. modem servers and VPN gateways, that facilitate various forms of connections between networks.</p>
<p>5- Security Event Management Software: These tools help with the analysis of log files which are typically produced by IDS tools, routers, and firewalls.</p>
<p>6- Network Forensic Analysis Tools: These tools are useful in reconstructing events via visualization and replaying of network traffic taking place within a given period of time.</p>
<p>7- Other sources: These sources can include Internet Service Provider (ISP) records, hosts&#8217; network connections and configuration, client/server applications, and Dynamic Host Configuration Protocol (DHCP) records.</p>
<p><strong>Network investigation tools:</strong></p>
<p>The following are the most commonly used packet sniffing software tools:</p>
<p>TCPDump/WinDump:</p>
<p><a href="https://www.deepdotweb.com/2017/09/04/setup-pentest-lab/">TCPDump and WinDump</a> are respectively the Lunix and Windows representatives of the tool that runs on a local machine to capture all network traffic taking place over ethernet and/or <a href="https://www.deepdotweb.com/2016/03/23/wi-fi-security/">wireless connections</a>.</p>
<p>Ethereal:</p>
<p>Ethereal is available for both Linux and Windows OSs. They boast a more user-friendly UI than TCPDump. Ethereal also has multiple protocol decoding options (&gt;400). The tool enables the forensic investigator to analyze collected data on a protocol basis or a packet basis.</p>
<p><strong>Network Forensic Analysis Tools (NFATs):</strong></p>
<p>NFATs are special forms of packet analysis tools which are capable of detecting firewall circumvention. For instance, corporate firewalls can block access to their staff from using social networks and instant messengers at work. Usually, Yahoo Messenger operates via port 5050, yet when this port is blocked, it will automatically shift to port 23. Even this port shift can bypass a firewall rule, an NFAT would be still able to detect that the network is being used by Yahoo Messenger via means of packet analysis. NFATs are not meant to replace firewalls or IDS software but are developed to operate in conjunction with them. Usually, NFATs depend on another software to capture traffic data packets such as TCPDump.</p>
<p><strong>Security Incident and Event Management Software (SIEM):</strong></p>
<p>SIEM software represents a combination of different software categories of Security Incident Management Software and Security Event Management Software and has a rather different investigative approach to the aforementioned &#8220;on-the-fly&#8221; analysis tools. SIEM software usually focuses on importing security event information related to a number of network traffic sources including IDS logs, firewall logs, and others. It operates on the basis of &#8220;after the fact,&#8221; while it analyzes different copies of the logs that attempt to detect suspicious network activity events via matching IP addresses, data timestamps, and other features of network traffic. OSSIM is an example of open source forms of such software.</p>
<p><strong>Packet Inspection Hardware:</strong></p>
<p>In the regular operation of Network Interface Cards (NICs), the devices only accept incoming packets that are specifically addressed to its IP address. However, when a NIC is placed in promiscuous mode, it will accept all packets that it sees, regardless of their intended destinations. Packet sniffing hardware generally operates on this principle, with configuration available to capture all packets or only those with specific features, e.g., certain TCP ports, certain source or destination IP addresses, etc. This style of network traffic capture can be used in combination with software sampling optimization techniques in order to reduce the overall size of the data to be investigated.</p>
</div>
<span style="display:none"><a href="https://www.deepdotweb.com/tag/deep/" rel="tag">deep</a> <a href="https://www.deepdotweb.com/tag/forensic/" rel="tag">forensic</a> <a href="https://www.deepdotweb.com/tag/harvesting/" rel="tag">harvesting</a> <a href="https://www.deepdotweb.com/tag/important/" rel="tag">important</a> <a href="https://www.deepdotweb.com/tag/tools/" rel="tag">tools</a> <a href="https://www.deepdotweb.com/tag/web/" rel="tag">web</a></span> <span style="display:none" class="updated">2018-11-23</span>
<div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
</div>
</article>

