---
DHL Goes Down After Hacker Exposes Clearnet IP Address"
---
<article class="post-listing post-21805 post type-post status-publish format-standard has-post-thumbnail hentry  tag-address tag-clearnet tag-dhl tag-exposes tag-hacker tag-ip">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/caliens/" title="">C. Aliens </a></span>
    <span>August 6, 2017</span>
    <span>in <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://www.deepdotweb.com/category/news-updates/" rel="category tag">News Updates</a></span>
    <span><a href="https://www.deepdotweb.com/2017/08/06/dhl-goes-hacker-exposes-clearnet-ip-address/#comments">9 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    <p>&nbsp;</p>
    <p>Reddit user known as /u/t0mcheck publicly disclosed “crippling” vulnerabilities in two <a href="https://www.deepdotweb.com/2013/10/28/updated-llist-of-hidden-marketplaces-tor-i2p/">darknet markets</a>: DHL and Sourcery Market. As usual, the posts increased the number of heated conversations between users and moderators. Eventually everything came down to DHL. According to a DHL representative, was not new to marketplace staff—they had known for two years. Now, along with Sourcery Market, both marketplaces vanished.</p>
    <p>Either may come back, but Reddit users called exit scam. “Yeah, I don&#8217;t think we&#8217;ll see them around anymore,” one user wrote.</p>
    <p>As of August 5, the two stickied posts in that subreddit are market warnings. One post is the vulnerability disclosure of both marketplaces. The second, though, is a post titled “<a href="https://www.reddit.com/r/DarkNetMarkets/comments/6r5o1s/dhl_market_current_problems_consider_avoiding/">DHL Market &#8211; Current problems &#8211; Consider avoiding right now.</a>” The vulnerabilities were serious enough to warrant the removal of the formerly stickied post about a significant number of <a href="https://www.deepdotweb.com/tag/vendor/">Dream vendor accounts</a> that the Dutch National Police controlled.</p>
    <p><img class="wp-image-21806 aligncenter" src="/imgs/2017/08/word-image-4.jpeg" srcset="/imgs/2017/08/word-image-4.jpeg 800w, /imgs/2017/08/word-image-4-300x166.jpeg 300w" sizes="(max-width: 800px) 100vw, 800px" /></p>
    <p>The Reddit user behind the disclosures claimed the DHL vulnerabilities took only 60 minutes to find. In the Gist, he published three major issues.</p>
    <ol>
    <li><strong>Vulnerability 1</strong>: <strong>Reflected XSS in Main Search</strong>
    <ol>
    <li>“XSS in main search field. Does not filter any characters”</li>
    </ol>
    </li>
    <li><strong>Vulnerability 2</strong>: <strong>Persistent XSS in PGP key upload</strong>
    <ol>
    <li>“PGP key comments can contain HTML and Javascript and it isn&#8217;t escaped.”</li>
    </ol>
    </li>
    <li><strong>Vulnerability 3</strong>: <strong>Persistent XSS In Support Forum</strong>
    <ol>
    <li>“While reporting the last two bugs to support I noticed that pasting in the vulnerable code triggered an XSS in the support forum.”</li>
    <li>“To XSS support simply message them with: <em>&lt;/textarea&gt;&lt;img src=/ onerror=javascript:alert(1)&gt;</em>”</li>
    </ol>
    </li>
    </ol>
    <p>The cross-site scripting in the main search drew attention, especially from the DHL “hidden moderator” account. The mod, under the handle “DHL-3,” pointed out that an entity had already created a forum post regarding the XSS vulnerability. The Reddit users exchanged words, another penetration tester verified the XSS vulnerabilities, and then t0mcheck dropped another surprise on the subreddit.</p>
    <p><img class="wp-image-21807 aligncenter" src="/imgs/2017/08/word-image-5.jpeg" srcset="/imgs/2017/08/word-image-5.jpeg 800w, /imgs/2017/08/word-image-5-300x130.jpeg 300w" sizes="(max-width: 800px) 100vw, 800px" /></p>
    <p>In “DHL Market Security Part 2,” t0mcheck expressed a new level of discontent with DHL admins and the subreddit moderators. “[We] are now disclosing that the market contains a very simple bug that allows anybody to read any message on the site. [<a href="https://gist.github.com/anonymous/97d1e2319b78210606d41f3309aa4c21">Gist link</a>…],” the user wrote.</p>
    <p><img class="wp-image-21808 aligncenter" src="/imgs/2017/08/word-image-6.jpeg" srcset="/imgs/2017/08/word-image-6.jpeg 800w, /imgs/2017/08/word-image-6-300x156.jpeg 300w" sizes="(max-width: 800px) 100vw, 800px" /></p>
    <p>“The administrators of DHL have not replied to any of our previous reports nor messages and it has been over 48 hours,” the entity wrote. “One more note &#8211; we are not going to put up with shit from admins, paid spokespeople or shill moderators any longer.”</p>
    <p>In the Gist, the “watchful community member” outlined the process required to read any messages on the site. And he did. At roughly the same time, an I.P. address that connected to DHL surfaced. Accessing the site from the I.P. address allowed users to log into DHL. Oddly, some users could change their passwords on <a href="https://www.deepdotweb.com/marketplace-directory/listing/darknet-heroes-league/">the DHL forums</a> via the official hidden service and then use their old passwords to log into the marketplace via the clearnet server.</p>
    <p><img class="wp-image-21809 aligncenter" src="/imgs/2017/08/word-image-7.jpeg" srcset="/imgs/2017/08/word-image-7.jpeg 800w, /imgs/2017/08/word-image-7-300x168.jpeg 300w" sizes="(max-width: 800px) 100vw, 800px" /></p>
    <p>In the recent past, a hacker known as “Cipher0007” <a href="https://www.deepdotweb.com/2017/06/01/alphabay-hacker-cipher0007-takes-sanctuary-market/">demolished Sanctuary Market</a>, shutting it down prior to a true launch. The market was beyond repair, the hacker explained. A moderator of the darknetmarkets subreddit banned an account claiming to be Cipher0007 for posting “fake” I.P. addresses.</p>
    <p>A post later appeared on the DHL forums that <a href="https://www.reddit.com/r/DarkNetMarkets/comments/6re4ch/dhl_explanation/">confirmed the I.P. leak as legitimate</a>. The announcement reported “good” news: that DHL admins were about to launch a new version of the marketplace. The I.P. address was a test server for DHL admins, SeriousSam wrote in the forum post.</p>
    <p>The announcement is as follows</p>
    <p>“<em>A few more hours and we [will] have an answer to everything in its entirety. But we also have very good news. We are </em><strong><em>deploying the new market</em></strong><em> where everything is fixed earlier than we wanted e.g not feature complete. But what can we do :( </em><strong><em>The IP leak is true</em></strong><em>. </em><strong><em>That was one of our test servers</em></strong><em>. But we killed everything already and besides some fresh loaded but now worthless virtual credit cards nothing is left :( </em><strong><em>Apparently we had a traitor in our mids</em></strong><em>t. The person doing various tests for us after each new version. Looks like he sold this info to the highest bidder. But encryption worked. Manual and automatic. Our system does not allow for any code changes inside read-only containers besides a signed push from our servers.</p>
    <p>But yeah, we fucked up here. Gotta admit that for sure. But we&#8217;ll make very good on this within 24hours, I hope.</p>
    <p></em> EDIT<em>: Support will fix issues soon again. And we are waiting for a fresh btchost to complete syncing before we process payments again. But that should be only max 10-12 hours. Usually we have emergency machines around but we decided to burn everything for the redeployment</em>. &#8211; SeriousSam</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/address/" rel="tag">address</a> <a href="https://www.deepdotweb.com/tag/clearnet/" rel="tag">clearnet</a> <a href="https://www.deepdotweb.com/tag/dhl/" rel="tag">dhl</a> <a href="https://www.deepdotweb.com/tag/exposes/" rel="tag">exposes</a> <a href="https://www.deepdotweb.com/tag/hacker/" rel="tag">hacker</a> <a href="https://www.deepdotweb.com/tag/ip/" rel="tag">ip</a></span> <span style="display:none" class="updated">2017-08-06</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/caliens/" title="Posts by C. Aliens" rel="author">C. Aliens</a></strong></div>
    
