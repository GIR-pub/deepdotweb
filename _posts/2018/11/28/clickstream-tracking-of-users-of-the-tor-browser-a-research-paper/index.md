---
Clickstream tracking of users of the Tor browser &#8211; A research paper
---
<article class="post-listing post-27401 post type-post status-publish format-standard has-post-thumbnail hentry category-articles category-deepdot-news tag-browser tag-clickstream tag-paper tag-research tag-tor tag-tracking tag-users">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>November 28, 2018</span>
    <span>in <a href="https://www.deepdotweb.com/category/articles/" rel="category tag">Articles</a>, <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a></span>
    <span><a href="https://www.deepdotweb.com/2018/11/28/clickstream-tracking-of-users-of-the-tor-browser-a-research-paper/#comments">3 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>The growing significance of web analytics, we have been witnessing throughout the past few years, has been also accompanied by an enormous growth in the number of web users concerned about preserving their online anonymity. The Tor browser has been often considered as the best online browsing tool available, as evidenced by more than 2.5 million people using it daily. For the vast majority of Tor users, even though most of Tor&#8217;s terms and options are rather difficult to understand, they inarguably believe that the Tor browser offers them more anonymity protection than what it is actually capable of providing.</p>
    <p><a href="https://www.tandfonline.com/doi/abs/10.1080/23742917.2018.1518060">A recently published paper</a> proved that the Tor browser can provide very little privacy protection if used via its default settings. As such, to achieve near total anonymity, extra care must be exercised by users of the Tor browser. Let&#8217;s take a look at some of the ways that can be used to track the clickstream of Tor users that were presented in this paper.</p>
    <p><img class="wp-image-27404" src="https://www.deepdotweb.com/wp-content/uploads/2018/11/tor_network-clickstream-jpg-1.jpeg" alt="tor_network-clickstream.jpg" srcset="https://www.deepdotweb.com/wp-content/uploads/2018/11/tor_network-clickstream-jpg-1.jpeg 680w, https://www.deepdotweb.com/wp-content/uploads/2018/11/tor_network-clickstream-jpg-1-300x176.jpeg 300w" sizes="(max-width: 680px) 100vw, 680px" /></p>
    <p><strong>Clickstream tracking via timing and traffic correlation:</strong></p>
    <p>Tor users can be vulnerable to deanonymization using end-to-end timing attackers. An adversary <a href="https://www.deepdotweb.com/2018/10/10/digestor-comparative-tool-for-tor-passive-traffic-analysis-attacks/">monitoring network traffic sent to the initial relay node</a>, as well as traffic sent to the final relay node, can make use of statistical analysis to identify the circuit they belong to. Consequently, Tor technically does not provide total anonymity for its users. The user&#8217;s IP address as well as the destination IP of the observed traffic can be sniffed by the adversary, who can easily track the clickstream of a user via correlation attacks. Interestingly, the adversary needn&#8217;t control the entry and exit nodes within a Tor circuit to be able to correlate network traffic streams observed travelling across these relay nodes. The adversary only needs to be capable of observing the traffic.</p>
    <p>Sometimes, tracking the clickstream of a user does not require any complex forms of statistical analysis. For example, a student in Harvard University was caught sending fake bomb threats to ditch an exam! The student sent the emails using a Guerilla email, an email address provider, via the Tor browser. The Guerilla email service adds the IP address of the email sender to all sent messages, which helped in identification of the user&#8217;s Tor exit node.</p>
    <p>Clickstream tracking via traffic correlation attacks is, more or less, easy to conduct, especially when the anonymity set (number of users using the Tor client) is somehow small. In other words, whenever a small number of clients are using the Tor client, within a given local network, then deanonymizing them is relatively a simple task to accomplish. More sophisticated attack forms require more complex techniques of statistical analysis of traffic, as well as timing. Recent experimental studies have revealed that such techniques can help track the clickstream of a large percentage of users of the Tor browser and visitors of Tor hidden services.</p>
    <p><strong>Deanonymization and tracking clickstream via practical side channel attacks (Torben):</strong></p>
    <p>This is a unique form of deanonymization attack, named Torben. The technique utilizes an approach that is more reliable than timing and traffic correlation attacks, as it is much less intrusive. The attack relies on interaction of multiple technologies &#8211; firstly, web pages loaded via the Tor browser can be easily manipulated to load scripts from untrusted origins; secondly, even though Tor encrypts loaded content, using a low latency anonymization circuit is ineffective at hiding the magnitude of request-response pairs. The attack was first described by a group of researchers from the University of Gottingen, Germany, who exploited this interplay to create a side channel in the Tor communication circuit, which enables the transmission of short markers of web pages in order to expose the web pages a client visited using the Tor browser. In an experimental evaluation that involved 60,000 web pages, the attack enabled tracking the clickstream of Tor users via detecting web page markers with a 91% accuracy.</p>
    <p><strong>Failure of security of operations:</strong></p>
    <p>It is easy to track users by monitoring the pattern of their behavior. This is relatively simple to accomplish for users who neglect using a bridge to connect to the Tor network. This method involves following up the pattern of browsing behavior of users linked to the same aliases on multiple forums, social networks, etc. This approach was how the identity of the mastermind behind <a href="https://www.deepdotweb.com/2015/01/15/step-towards-the-star-chamber/">Silk Road</a>, Ross Ulbricht, revealed. Ulbricht made a big mistake using the same aliases on multiple forums and on the Silk Road marketplace itself such as &#8220;Dread Pirate Roberts&#8221; (DPR) and &#8220;frosty&#8221;.</p>
    <p>Recent experiments have shown that 10 web addresses are all that might be needed to identify who the Tor clickstream belongs to. The clickstream is identified by matching account aliases and other online data belonging to the clickstream to publicly available data. The stream can be accurate to the point that it reflects everything a user has been doing, minute by minute.</p>
    <p><strong>Clickstream tracking via modified exit/DoS node:</strong></p>
    <p>This form of deanonymization attack utilizes five components &#8211; a modified exit node, a modified DoS node, a lightweight DoS web server, a client side JS for measurement of latency, and an instrumentation client to receive data. Implementing this attack is conducted as follows:</p>
    <p>&#8211; The JS ping code is injected by the exit node into the HTML response.</p>
    <p>&#8211; As the user browses as per usual, the JS will continue to &#8220;phone home.&#8221;</p>
    <p>&#8211; As the attacker continues measuring, DoS attack will strain possible initial hop(s).</p>
    <p>&#8211; If no significant level of variance is detected, another node is selected from candidate nodes and the attack sequence will restart again.</p>
    <p>&#8211; Once sufficient change is detected within the measurements, the entry node will be detected, which will denaonymize the user and aid in tracking their clickstream.</p>
    <p>This attack method helps identify the whole patch of connection through the Tor network. The attack utilizes bandwidth multiplication which makes it possible for low bandwidth connections to DoS connections with high bandwidths.</p>
    <p><strong>Clickstream tracking via BGP:</strong></p>
    <p>Experimental studies have shown that Tor is vulnerable to Autonomous Systems (Ases) that can relay Tor traffic, thanks to their effective eavesdropping capabilities. When a malicious AS, or a group of colluding ASes, intervening between a Tor user and the entry relay node, and between the exit relay node and the destination, can conduct timing analysis to deanonymize Tor users. AS level adversaries are very powerful for many reasons. Firstly, routine BGP routing can alter the number of ASes that can effectively track the clickstream of Tor users. Secondly, ASes can effectively manipulate BGP announcements to place themselves on Tor circuits along the paths entering and exiting relay nodes. Thirdly, an AS can undergo timing analysis, even if it can only monitor a single traffic direction between the entry node and the exit node. It was proven that asymmetric routing boosts the efficiency of ASes in tracking the clickstream of a Tor user.</p>
    <p><strong>Final thoughts:</strong></p>
    <p>The paper presented multiple means for tracking the clickstream of Tor users. It is worth mentioning that the biggest weakness that can boost the success of deanonymization attacks is the user. Users should be aware of techniques that can increase their privacy via Tor such as using a bridge, disabling JS, avoiding using Windows OS, and others. The Tor Project is continuously offering users detailed guidelines and tutorials to help them maximize their privacy and protect their online anonymity.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/browser/" rel="tag">browser</a> <a href="https://www.deepdotweb.com/tag/clickstream/" rel="tag">clickstream</a> <a href="https://www.deepdotweb.com/tag/paper/" rel="tag">paper</a> <a href="https://www.deepdotweb.com/tag/research/" rel="tag">research</a> <a href="https://www.deepdotweb.com/tag/tor/" rel="tag">tor</a> <a href="https://www.deepdotweb.com/tag/tracking/" rel="tag">tracking</a> <a href="https://www.deepdotweb.com/tag/users/" rel="tag">users</a></span> <span style="display:none" class="updated">2018-11-28</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>
