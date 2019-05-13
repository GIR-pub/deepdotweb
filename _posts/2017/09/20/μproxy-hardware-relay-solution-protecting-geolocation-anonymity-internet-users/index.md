---
μProxy &#8211; A Hardware Relay Solution for Protecting Geolocation Anonymity of Internet Users
---
<article class="post-listing post-22650 post type-post status-publish format-standard has-post-thumbnail hentry 
tag-anonymity tag-geolocation tag-hardware tag-internet tag-protecting tag-relay tag-solution tag-users tag-proxy">
    
    <div class="post-inner">
    
    
        
    <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    
    
    <span>September 20, 2017</span>
    
    
    <span><a href="https://www.deepdotweb.com/2017/09/20/%ce%bcproxy-hardware-relay-solution-protecting-geolocation-anonymity-internet-users/#comments">2 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    
    
    <p>Anonymity and privacy of internet users have attracted considerable attention during the past few years. A pivotal privacy issue is that a user&#8217;s geographical location can be pinpointed, if his/her IP address has been detected, giving the attacker a relatively precise real-time location. In most cases, this information is adequate for an attacker, to close in and eventually determine the location of the user via implementation of traditional tracking methods.</p>
    <p>Presently available anonymity solutions, including The Onion Routing Project (TOR), proxy servers and <a href="https://www.deepdotweb.com/2016/07/15/on-public-and-private-wifi-vpns-tor-and-virtual-machines/">Virtual Private Networks (VPNs)</a> aim at mitigating this problem via routing network traffic through a single, or multiple third party relay nodes. This prevents an attacker from determining the real origin or destination of a data packet. This approach is effective in isolating a user from the websites he/she is visiting, yet it does little, when it comes to guarding the user&#8217;s geographical location, as the attacker can still detect VPN, or Tor traffic emerging from the user&#8217;s network connection. Consequently, a system is needed to sever the association between a user&#8217;s IP address and his/her geographical location.</p>
    <p><img class="wp-image-22655 aligncenter" src="/imgs/2017/09/word-image-34.jpeg" srcset="/imgs/2017/09/word-image-34.jpeg 500w, /imgs/2017/09/word-image-34-300x212.jpeg 300w" sizes="(max-width: 500px) 100vw, 500px" /></p>
    <p><a href="https://link.springer.com/chapter/10.1007/978-3-319-62024-4_13">A recently published paper</a> introduced μProxy, an inexpensive solution that can solve this problem and break the association between a user&#8217;s IP address and his/her corresponding geographical location. μProxy promotes location anonymity of internet users via an arbitrary set interconnected Wifi nodes that relay users&#8217; traffic. The relay extends between the user and the destination network, to which he/she chooses to connect, e.g. a public Wifi network. Network traffic will seem to emerge from the last device along the path of relay nodes. If an attacker attempts to trace back the IP address of the user, he will only be able to determine the IP address of the relay endpoint. Further tracking will require detecting the location of an arbitrary number of relay nodes (these are potentially covert relay nodes), which would yield an exponentially enlarging search radius. Such a search radius is well beyond the capabilities of most adversaries.</p>
    <p><strong>System Design of μProxy:</strong></p>
    <p>μProxy represents a series of Wifi nodes forming a &#8220;Wifi relay&#8221; with a &#8220;daisy chain&#8221; topology, as illustrated in the below figure. The relay has a pair of endpoints; a local endpoint to which the user connects, and a remote endpoint that connects to the internet, e.g. via a public Wifi network. Between the two endpoints, a group of relay nodes route the network traffic. In most cases, there will be <strong><em>N</em></strong> relay nodes, rather than the single relay node illustrated in the below figure. Hidden Wifi hotspots are broadcast via individual nodes, along the Wifi relay, realized with ESP modules. These modules are implanted physically along the path that connects between the locations of the two endpoints of the relay. A tunnel is created to seamlessly forward all network traffic between the two endpoints. Each one of these modules will connect to the node of the module ahead of it along the chain of relay nodes, while accepting an incoming connection from the node of the previous module. ESP&#8217;s ability to function both as a Wifi client, and as an access point simultaneously marks the basic infrastructure of μProxy .</p>
    <p><img class="wp-image-22656 aligncenter" src="/imgs/2017/09/word-image-1.gif" /></p>
    <p>The protocol is setup to control a relay network which is comprised of an arbitrary number of Wifi devices, provide interfaces for external endpoints, support necessary cryptography and efficiently transmit data along the relay nodes. The protocol has to be executed within the restrictive embedded system environment of the ESP modules. Consequently, usage of runtime resources, as well as the size of the compiled computer code had to be minimized. The protocol is extremely light weighted; this is necessary so as not to monopolize the 80 MHz processor core of the ESP, which would prevent the Wifi router from functioning normally.</p>
    <p><a id="post-22650-_gjdgxs"></a> Long relay can be established inexpensively, given the low cost nature of ESP modules. A measured delay per relay node of around 20 ms is adequately low to promote practicality of usage of μProxy when geolocation anonymity is concerned.</p>
    
    
    </div><!-- .entry /-->
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/anonymity/" rel="tag">anonymity</a> <a href="https://www.deepdotweb.com/tag/geolocation/" rel="tag">geolocation</a> <a href="https://www.deepdotweb.com/tag/hardware/" rel="tag">hardware</a> <a href="https://www.deepdotweb.com/tag/internet/" rel="tag">internet</a> <a href="https://www.deepdotweb.com/tag/protecting/" rel="tag">protecting</a> <a href="https://www.deepdotweb.com/tag/relay/" rel="tag">relay</a> <a href="https://www.deepdotweb.com/tag/solution/" rel="tag">solution</a> <a href="https://www.deepdotweb.com/tag/users/" rel="tag">users</a> <a href="https://www.deepdotweb.com/tag/%ce%bcproxy/" rel="tag">μproxy</a></span>				<span style="display:none" class="updated">2017-09-20</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    
    
    </div><!-- .post-inner -->
</article><!-- .post-listing -->

