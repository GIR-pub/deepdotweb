---
Examples Of Hidden Service Deanonymization
---
<article class="post-listing post-21971 post type-post status-publish format-standard has-post-thumbnail hentry  tag-deanonymization tag-examples tag-service">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/caliens/" title="">C. Aliens </a></span>
    <span>August 15, 2017</span>
    <span>in <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://www.deepdotweb.com/category/news-updates/" rel="category tag">News Updates</a></span>
    <span><a href="https://www.deepdotweb.com/2017/08/15/examples-hidden-service-deanonymization/#comments">18 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    <p><strong>All have been disclosed and fixed</strong></p>
    <p>A penetration tester under the name “UnhandledException,” with credit to “bl00d,” wrote an essay on hidden service deanonymization for DeepDotWeb in an effort to warn the community. In the wake of current situations and in preparation for future events, extra scrutinization is in high demand as new markets rise to fill <a href="https://www.deepdotweb.com/2017/07/20/globally-coordinated-operation-just-took-alphabay-hansa/">the Alphabay and Hansa void</a>.</p>
    <p>In the first topic covered, UnhandledException explained where safest place to host a hidden service would be—a physical host controlled by the hidden service owner or through anonymous hosting providers. UnhandledException’s proposal was to take the physical route over a host owned by an unaffiliated third party. (This is a controversial topic as many believe that taking the anonymous server route—especially an anonymous server in Russia or Kazakhstan.) UnhandledException backed up the decision with a set of “pros” that outlined the positives to hosting a hidden service on one&#8217;s own hardware.</p>
    <p><img class="wp-image-21975" src="/imgs/2017/08/screenshot_2017-07-28_19-21-55-png.png" alt="Screenshot_2017-07-28_19-21-55.png" srcset="/imgs/2017/08/screenshot_2017-07-28_19-21-55-png.png 563w, /imgs/2017/08/screenshot_2017-07-28_19-21-55-png-300x192.png 300w" sizes="(max-width: 563px) 100vw, 563px" /></p>
    <p>For a physical host:</p>
    <ul>
    <li>The first argument was in relation to the level of control enabled by a host owned by the hidden service owner. Complete control over security, “multiple levels of encryption, [setting] your own iptables rules, and hardening your permissions.”</li>
    <li>Owning the hardware means a third party host would not have identifying metadata, despite the anonymity steps taken in an effort to keep an identity from said hosting provider.</li>
    <li>Physical devices are easily destructible in an emergency situation.</li>
    <li>The ability to physically access a server allows for a smaller attack surface.</li>
    </ul>
    <p>“You have no idea about how many hidden services are still using default credentials and standard port for [these] access points,” UnhandledException wrote, in reference to leaving ports open for SSH, FTP, etc. With credit to bl00d, UnhandledException gave us current example involving Berlusconi Market, a recently created <a href="https://www.deepdotweb.com/tag/italy/">Italian marketplace</a>. (The marketplace looks roughly a month old, if not less). With a Shodan search, they found the hosting provider and and <a href="https://www.shodan.io/host/185.61.137.160">the server’s real IP address</a>—simply by searching the market name.</p>
    <p><img class="wp-image-21976" src="/imgs/2017/08/screenshot_2017-07-28_19-00-51-png.png" alt="Screenshot_2017-07-28_19-00-51.png" srcset="/imgs/2017/08/screenshot_2017-07-28_19-00-51-png.png 726w, /imgs/2017/08/screenshot_2017-07-28_19-00-51-png-300x179.png 300w" sizes="(max-width: 726px) 100vw, 726px" /></p>
    <p>They then explained web server setups and the basic mistakes they had stumbled upon. One of which occurred on the market mentioned above. UnhandledException scanned the market with nmap and found a <a href="https://pastebin.com/YHdRXXaX">near-default setup</a>. The Berlusconi Market was leaking the http port through a Nginx bug. “The directory &#8220;/img&#8221; will redirect you at http://berluscqui3nj4qz[dot]onion:8080/img/,” the Ex0du$ team member wrote.</p>
    <p><img class="wp-image-21977" src="/imgs/2017/08/screenshot_2017-07-28_19-20-11-png.png" alt="Screenshot_2017-07-28_19-20-11.png" srcset="/imgs/2017/08/screenshot_2017-07-28_19-20-11-png.png 708w, /imgs/2017/08/screenshot_2017-07-28_19-20-11-png-300x139.png 300w, /imgs/2017/08/screenshot_2017-07-28_19-20-11-png-272x125.png 272w" sizes="(max-width: 708px) 100vw, 708px" /></p>
    <p>According to UnhandledException, Apache servers can be even more dangerous than Nginx servers when default settings are in use. And apparently hidden services use default setups rather frequently. The admins of <a href="https://www.deepdotweb.com/2013/10/28/updated-llist-of-hidden-marketplaces-tor-i2p/">darknet markets or forums</a>, in UnhandledException’s experience, leave the Apache modules “<a href="https://httpd.apache.org/docs/2.4/mod/mod_info.html">mod-info</a>” and “mod-server” available for public access. The enabled modules would allow a user to visit /server-info and /server-status, respectively.</p>
    <p><img class="wp-image-21978" src="/imgs/2017/08/sympo-1-png.png" alt="sympo (1).png" srcset="/imgs/2017/08/sympo-1-png.png 1004w, /imgs/2017/08/sympo-1-png-300x203.png 300w, /imgs/2017/08/sympo-1-png-290x195.png 290w" sizes="(max-width: 1004px) 100vw, 1004px" /></p>
    <p>An Italian forum called Astaroth, along with <a href="https://www.deepdotweb.com/marketplace-directory/listing/italian-deep-web/">Symposion/IDW</a>, served as an example for the Apache module leakage. UnhandledException potential demonstrated the damage caused by a module leaking sensitive information. “I was able to find the remote ip address of the server above the hosting provider as shown previously,” UnhandledException explained:</p>
    <p>&nbsp;</p>
    <ul>
    <li><em>“I prepared a php page with this exploit:</em></li>
    </ul>
    <p><img class="wp-image-21979" src="/imgs/2017/08/exploit-png.png" alt="exploit.png" srcset="/imgs/2017/08/exploit-png.png 805w, /imgs/2017/08/exploit-png-300x60.png 300w" sizes="(max-width: 805px) 100vw, 805px" /></p>
    <ul>
    <li><em>And passed it inside the &#8220;upload avatar from URL&#8221; function which is vulnerable: </em></li>
    </ul>
    <p><img class="wp-image-21980" src="/imgs/2017/08/sympoexploit-1-png.png" alt="sympoexploit (1).png" srcset="/imgs/2017/08/sympoexploit-1-png.png 1065w, /imgs/2017/08/sympoexploit-1-png-300x215.png 300w, /imgs/2017/08/sympoexploit-1-png-1024x734.png 1024w" sizes="(max-width: 1065px) 100vw, 1065px" /></p>
    <ul>
    <li><em>Got the remote server address in the log file:</em></li>
    </ul>
    <p><img class="wp-image-21981" src="/imgs/2017/08/sympoip-png.png" alt="sympoip.png" srcset="/imgs/2017/08/sympoip-png.png 529w, /imgs/2017/08/sympoip-png-300x77.png 300w" sizes="(max-width: 529px) 100vw, 529px" /></p>
    <ul>
    <li><em>This kind of tricky requests can be easily blocked by restricting dangerous php functions.”</em></li>
    </ul>
    <p>UnhandledException concluded:</p>
    <p><em>“Most of the people probably don&#8217;t understand that risks are REAL when running an illegal service. Do not announce your shit if you are still not ready to announce it. As we have seen we could be able to find hosting providers, VPS numbers and even ip addresses of some illegal websites. These info are enough for LE to start an inquiry on you. You should always use multiple levels of proxy like VPN, virtualized environments with a safe connection and encryption. Be sure to update your stuff constantly and move your server from time to time.”</em></p>
    </div>
    <a href="https://www.deepdotweb.com/tag/deanonymization/" rel="tag">deanonymization</a> <a href="https://www.deepdotweb.com/tag/examples/" rel="tag">examples</a>  <a href="https://www.deepdotweb.com/tag/service/" rel="tag">service</a></span> <span style="display:none" class="updated">2017-08-15</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/caliens/" title="Posts by C. Aliens" rel="author">C. Aliens</a></strong></div>
    </div>
</article>

