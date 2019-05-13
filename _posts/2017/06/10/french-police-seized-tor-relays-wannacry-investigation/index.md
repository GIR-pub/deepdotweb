---
French Police Seized Tor Relays in WannaCry Investigation
---
<article class="post-listing post-20529 post type-post status-publish format-standard has-post-thumbnail hentry  tag-french tag-investigation tag-police tag-relays tag-seized  tag-wannacry">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/caliens/" title="">C. Aliens </a></span>
    <span>June 10, 2017</span>
    <span>in <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://www.deepdotweb.com/category/news-updates/" rel="category tag">News Updates</a></span>
    <span><a href="https://www.deepdotweb.com/2017/06/10/french-police-seized-tor-relays-wannacry-investigation/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>On March 17, news outlets reported the sudden absence of several French Tor relays. Further data revealed that law enforcement agencies in France seized the the relays in connection with the investigation into WannaCrypt. WannaCrypt, the ransomware that struck “<a href="https://www.golem.de/news/wanna-cry-mehrere-tor-server-in-frankreich-beschlagnahmt-1705-127905.html">more than 200,000 devices worldwide</a>,” used Tor to connect to a C2 server.</p>
    <p>The Central Office for Combating Crime Related to Information and Communication Technologies (OCLCTIC) took down at least three servers, one French news report explained. According to another source, the nodes taken down were <a href="https://www.deepdotweb.com/tag/tor/">Tor entry guard nodes</a>. Tor guard nodes, or entry nodes with the guard flag, are basically a relay that the Tor network trusts more so than other nodes.</p>
    <p>As listed on the Tor blog, the requirements for a guard node are not particularly overwhelming:</p>
    <ol>
    <li><em>The relay needs to have first appeared longer ago than 12.5% of the relays, or 8 days ago, whichever is shorter.</em></li>
    <li><em>The relay needs to advertise at least the median bandwidth in the network, or 250KB/s, whichever is smaller.</em></li>
    <li><em>The relay needs to have at least the median weighted-fractional-uptime of relays in the network, or 98% WFU, whichever is smaller. (For WFU, the clock starts ticking when we first hear about the relay; we track the percentage of that time the relay has been up, discounting values by 95% every 12 hours.)</em></li>
    </ol>
    <p>But the relays are essential for Tor operation and usability. And, one can assume that while accessing the C2 server, WannaCrypt passed through more than three guard nodes.</p>
    <p><img class="wp-image-20530 aligncenter" src="/imgs/2017/06/word-image-41.jpeg" srcset="/imgs/2017/06/word-image-41.jpeg 800w, /imgs/2017/06/word-image-41-300x204.jpeg 300w" sizes="(max-width: 800px) 100vw, 800px" /></p>
    <p>One user wrote the following on the <a href="https://lists.torproject.org/pipermail/tor-relays/2017-May/012334.html">Tor relays mailing list</a>:</p>
    <p><em>“Dear Tor Project,</p>
    <p>Currently, my server hosting kitten1 and kitten2 (tor guard and fallback<br />
    directory) is under seizure since 14/05 11h.<br />
    Private key are under encrypted volume and may be protected, but please revoke<br />
    immediatly kitten1 &amp; kitten2 tor node.<br />
    Those nodes are also fallback directory.</p>
    <p>Regards,<br />
    &#8212;<br />
    Aeris”</em></p>
    <p>The user explained what he knew and what he could speak about. Aeris said that WannaCrypt infected a French company on May 12. The <a href="https://www.deepdotweb.com/2017/05/13/ransomeware-hackers-launch-global-assault/">infected systems reached out to the C2 via .onion addresses</a>, inevitably passing through Tor nodes. And “possibly bridges, directory authorities and fallback directories can be affected too, or any Tor nodes which can be joined directly by standard Tor client,” Aeris explained.</p>
    <p>Then, come May 13 and 14, police seized Aeris&#8217;s servers. The system admin of the infected company reported all of traffic as malicious and reported the destination IPs to the authorities. And the rest of that situation is self explanatory. In many countries and states, the police understand the basics of Tor nodes, even Tor exit nodes. Meaning: normally they know that the network activity may have no relation to the actual nice operator. Apparently not in this case.</p>
    <p><img class="wp-image-20531 aligncenter" src="/imgs/2017/06/word-image-42.jpeg" srcset="/imgs/2017/06/word-image-42.jpeg 620w, /imgs/2017/06/word-image-42-300x160.jpeg 300w" sizes="(max-width: 620px) 100vw, 620px" /></p>
    <p>And similarly, they usually know that the logs kept by these relays reveal nothing more than uptime and downtime resisted information. Any evidence regarding WannaCrypt, unless Aeris hid <em>something</em> on those encrypted discs, is not likely to show up on the seized servers. However, as the Tor blog reveals, some officers know <a href="https://www.deepdotweb.com/tag/analysis/">how to identify</a> a node operator but still at as if the operator is at fault.</p>
    <p>“One regional Dutch police woman told us that they know how to check if it&#8217;s a Tor exit IP, but sometimes they do the raid anyway ‘to discourage people from helping Tor,’” <a href="https://blog.torproject.org/blog/trip-report-tor-trainings-dutch-and-belgian-police">Roger Dingledine wrote</a> following a trip to educate Dutch police.</p>
    <p>The Paris Public Prosecutor&#8217;s Office did not respond to golem.de’s request for comment.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/french/" rel="tag">french</a> <a href="https://www.deepdotweb.com/tag/investigation/" rel="tag">investigation</a> <a href="https://www.deepdotweb.com/tag/police/" rel="tag">police</a> <a href="https://www.deepdotweb.com/tag/relays/" rel="tag">relays</a> <a href="https://www.deepdotweb.com/tag/seized/" rel="tag">seized</a> <a href="https://www.deepdotweb.com/tag/tor/" rel="tag">tor</a> <a href="https://www.deepdotweb.com/tag/wannacry/" rel="tag">wannacry</a></span> <span style="display:none" class="updated">2017-06-10</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/caliens/" title="Posts by C. Aliens" rel="author">C. Aliens</a></strong></div>
    </div>
</article>

