---
Monitoring Malicious Activities On Darknets &#8211; A Research Study
---
<article class="post-listing post-20263 post type-post status-publish format-standard has-post-thumbnail hentry  tag-activities tag-darknets tag-malicious tag-monitoring tag-research tag-study">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>June 1, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/06/01/monitoring-malicious-activities-darknets-research-study/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Darknets are comprised of machines and/or servers with unassigned IP addresses, which operate in a passive mode that is characterized by minimal or no communication with public parts of the internet. It is rather unusual for data to be received on such networks; and if this happens, <a href="https://www.deepdotweb.com/2017/01/08/onion-router-darkweb-overview-current-state-vulnerabilities/">malicious activity is suspected</a>. Data sent in such way could represent an adversary looking for network vulnerabilities that he can use to launch future attacks.</p>
    <p>A group of researchers from the Indian Institute of Technology (IIT) Kanpur, India, studied <a href="http://home.iitk.ac.in/~devyadav/cs498a/report.pdf">the patterns of malicious activities on darknets</a>, via monitoring and analyzing darknet traffic across a /24 public IPv4 space of IIT Kanpur.</p>
    <p><strong>Study Approach:</strong></p>
    <p>Institutions such as IIT Kanpur usually have a considerably large pool of public IP addresses appointed to them. Some of these IP addresses represent active services, such as the institution&#8217;s website and departments&#8217; servers that manage incoming and outgoing traffic to the institution. At any point of time, there exists a group of IP addresses that are not allocated to any service. These IP addresses represent a darknet according to the definition of darknets proposed by <a href="http://users.encs.concordia.ca/~e_bouh/pubs/confs/crisis.pdf">Fachkha and colleagues via their study that was presented in the 2012 International Conference on Risks and Security of Internet and Systems (CRiSIS). </a>As these IP addresses are not allocated to any service, data sent to them is unusual and often represent malicious activities. The researchers monitored the darknet traffic of approximately 180 IPv4 addresses at IIT Kanpur, which included a small number of active IP addresses. The traffic was analyzed to detect patterns related to specific types of malicious attacks.</p>
    <p><strong>Types of data Received By The Studied Darknet:</strong></p>
    <p>Monitoring traffic on darknets is different from active network monitoring approaches such as network intrusion detection systems (NIDS), due to the fact that darknets operate in a passive mode with almost no form of interaction taking place with the attackers. Data received by darknets can be classified into three main groups:</p>
    <p>1. Data received secondary to misconfigurations.</p>
    <p>2. Backscatter data</p>
    <p>3. Data meant directly to the server.</p>
    <p><strong>Analysis of Darknet Traffic:</strong></p>
    <p>The researchers found out that data received by the darknet was approximately 4 MBps every hour. The below graph represents the percentage of darknet traffic as compared to the overall traffic sent to IIT Kanpur in a day, along a period of two weeks.</p>
    <p><img class="wp-image-20272 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-118.png" width="659" height="351" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-118.png 850w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-118-300x160.png 300w" sizes="(max-width: 659px) 100vw, 659px" /></p>
    <p>The majority of received data originated from IPv4 addresses and the most commonly used protocol was TCP, followed by UDP. These source addresses were mapped and their country of origin was identified as shown by the below map.</p>
    <p><img class="wp-image-20273 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-119.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-119.png 627w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-119-300x157.png 300w" sizes="(max-width: 627px) 100vw, 627px" /></p>
    <p><strong>Analyzing Darknet Traffic Using Bro:</strong></p>
    <p>Bro is a powerful, open source framework for network analysis. The researchers used bro to analyze the captured and filtered darknet traffic data for a period of approximately 2 weeks. Bro categorized the captured data and the researchers were able to detect multiple IP address scan attempts, along with other forms of attacks that seemed to involve an attacker attempting to guess SSH passwords. Various ports were used throughout these attempts and included TELNET (62.6%), SSH (15.4%), SNMP (10.4%) and HTTP (6.3%).</p>
    <p>Bro was able to detect IP address scanning attempts that originated from approximately 4,500 different IP addresses that are associated with countries from many parts of the world. Data packets sent to the IP addresses were considered to be IP address scanning attempts, whenever they were sent to a minimum of 25 different hosts within the address space. These IP address scanning attempts took place on TCP/UDP ports such as 1433 (SQL Server), 80 (HTTP), 22 (SSH) etc. The researchers included data packets from a small number of active IP addresses whose SSH port was found to be open; thus, they were most commonly engaged in password guessing attempts.</p>
    <p><strong>Implications of the study:</strong></p>
    <p>Although the study presented some interesting results, they cannot be universalized especially that the studied darknet is neither uniform, nor large enough to produce reliable conclusions. The researchers stated that they will continue on researching this field, as they intend on improving the efficiency of packet capturing and the scope of traffic analysis, through future studies, via utilization of an active monitoring system and/or studying a larger darknet space.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/activities/" rel="tag">activities</a> <a href="https://www.deepdotweb.com/tag/darknets/" rel="tag">darknets</a> <a href="https://www.deepdotweb.com/tag/malicious/" rel="tag">malicious</a> <a href="https://www.deepdotweb.com/tag/monitoring/" rel="tag">monitoring</a> <a href="https://www.deepdotweb.com/tag/research/" rel="tag">research</a> <a href="https://www.deepdotweb.com/tag/study/" rel="tag">study</a></span> <span style="display:none" class="updated">2017-06-01</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

