---
PSA: Cloudflare Now allows you To Whitelist ALL Tor&#8217;s Exit Nodes
---
<article class="post-listing post-13590 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news category-news-updates tag-cloudflare tag-exit tag-nodes tag-psa tag-tors tag-whitelist">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/admin/" title="">DeepDotWeb </a></span>
    <span>March 28, 2016</span>
    <span>in <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://www.deepdotweb.com/category/news-updates/" rel="category tag">News Updates</a></span>
    <span><a href="https://www.deepdotweb.com/2016/03/28/psa-cloudflare-now-allows-whitelist-tors-exit-nodes/#comments">2 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>As well as many other site owners who use Cloudflare as their CDN and DDoS protection provider, we always suffered from the famous &amp; annoying issue which we could never resolve &#8211; the fact that our visitors who use Tor were sometimes being forced to solve annoying captchas to access our site (or just use <a href="https://www.deepdotweb.com/2015/06/18/reminder-this-is-our-only-legit-onion-address-deepdot35wvmeyd5-onion/" target="_blank">our onion address</a> to avoid them), even when the Cloudflare protection was set to the lowest level, which isn&#8217;t always the case, due to many attacks we have to deal with.</p>
    <p>But now, we were happy to find out that Since late February 2016, Cloudflare started treating Tor exit nodes as a &#8220;country&#8221; of its own. There&#8217;s no geography associated with exit node IPs, but this approach lets CloudFlare customers override the default CloudFlare threat score to define the experience for their Tor visitors &#8211; <strong>and by doing this, disabling the captchas for all visitors who use Tor.</strong></p>
    <p>If you run a web site on CloudFlare, and you don&#8217;t want Tor users to see captchas, then the only thing you need to do is whitelist the &#8220;<strong>T1</strong>&#8221; country code in the <a class="ext-link" href="https://support.cloudflare.com/hc/en-us/articles/217074967-How-do-I-control-access-to-my-site-" target="_blank"><span class="icon">​</span>Access Rules</a> of the CloudFlare Firewall app.</p>
    <p>Here&#8217;s an example where a CloudFlare customer chooses in their dashboard to Whitelist Tor exit nodes. CloudFlare updates its list of Tor exit node IP addresses every 15 minutes:</p>
    <p><img class="aligncenter" src="https://support.cloudflare.com/hc/en-us/article_attachments/205677388/tor-whitelisted.png" alt="" /></p>
    <p>As soon as we found out about this new option, here on <a href="https://www.deepdotweb.com/">DeepDotWeb</a> made sure to whitelist all Tor&#8217;s exit nodes and decided to publish this PSA to let everyone else know its now possible, so if you come across a website who still blocks you when you try to access it using Tor, share this info with them.</p>
    <p><span style="text-decoration: underline;"><strong>Relevant info: </strong> </span></p>
    <ul>
    <li>Tor Wiki on &#8211; <a href="https://trac.torproject.org/projects/tor/wiki/org/doc/ListOfServicesBlockingTor#HowtounblockTorusers" target="_blank">How to unblock Tor users</a></li>
    <li>Cloudfalre support on <a href="https://support.cloudflare.com/hc/en-us/articles/203306930-Does-CloudFlare-block-Tor-" target="_blank">how to whitelist Tor exit nodes</a></li>
    <li>Use DeepDotWeb onion address with your JS disabled to maximize your privacy: <strong>deepdot35wvmeyd5.onion</strong></li>
    </ul>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/cloudflare/" rel="tag">cloudflare</a> <a href="https://www.deepdotweb.com/tag/exit/" rel="tag">exit</a> <a href="https://www.deepdotweb.com/tag/nodes/" rel="tag">nodes</a> <a href="https://www.deepdotweb.com/tag/psa/" rel="tag">psa</a> <a href="https://www.deepdotweb.com/tag/tors/" rel="tag">tors</a> <a href="https://www.deepdotweb.com/tag/whitelist/" rel="tag">whitelist</a></span> <span style="display:none" class="updated">2016-03-28</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/admin/" title="Posts by DeepDotWeb" rel="author">DeepDotWeb</a></strong></div>
    </div>
</article>

