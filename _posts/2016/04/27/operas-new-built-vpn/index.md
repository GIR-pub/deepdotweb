---
Opera&#8217;s New Built-In “VPN”
---
<article class="post-listing post-13889 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-builtin tag-operas tag-vpn">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/fuzzy/" title="">Fuzzy </a></span>
    <span>April 27, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/04/27/operas-new-built-vpn/#comments">6 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Opera, a browser that already has an ad-blocking feature, recently <a href="http://www.opera.com/blogs/desktop/2016/04/free-vpn-integrated-opera-for-windows-mac/">added</a> a new feature to their browser – a free VPN with unlimited data usage. It currently has IP addresses in the United States, Canada, and Germany. This addition was well-received and met with praise, but there&#8217;s a twist to it.</p>
    <p><img class="aligncenter size-full wp-image-13890" src="https://www.deepdotweb.com/wp-content/uploads/2016/04/opera.png" alt="opera" width="615" height="80" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/04/opera.png 615w, https://www.deepdotweb.com/wp-content/uploads/2016/04/opera-300x39.png 300w" sizes="(max-width: 615px) 100vw, 615px"/></p>
    <p>It&#8217;s actually an HTTP/S proxy that requires authentication. For some reason Opera insists on calling it a VPN even though it says below “Enable VPN”  that it&#8217;s a proxy.</p>
    <p>According to <a href="https://gist.github.com/spaze/558b7c4cd81afa7c857381254ae7bd10">research</a> by Michal Špaček, when you first enable the “VPN”, it makes 4 requests to SurfEasy&#8217;s API. The first request “subscribes” you to the VPN and the second gives you your credentials (ID and password). The last two obtain proxy IP addresses.</p>
    <p>When you request a web page, requests are made to *.opera-proxy.net with a Proxy-Authorization header. &#8216;*&#8217; being a country then a number, e.g. de0.opera-proxy.net. A few of the proxy servers appear to be hosted at <a href="https://www.xirra.net/">Xirra</a>. The Proxy-Authorization header is a SHA1 checksum of your ID with your password concatenated by a colon. An example of this header would be: CC68FE24C34B5B2414FB1DC116342EADA7D5C46B:9B9BE3FAE674A33D1820315F4CC94372926C8210B6AEC0B662EC7CAD611D86A3</p>
    <p>Due to the fact that this VPN is actually a proxy, you can technically use it on a different computer that doesn&#8217;t even have Opera installed.</p>
    <p>SurfEasy, the company that provides the proxies, is a VPN provider owned by Opera, and like Opera, they&#8217;re based in Canada – one of the <a href="https://www.privacytools.io/#ukusa">five eyes</a>.</p>
    <p>However, SurfEasy <a href="https://www.surfeasy.com/privacy_policy/">claims</a> to be a “no log network”: “SurfEasy does not store users originating IP address when connected to our service and therefore cannot identify users when provided IP addresses of our servers. …”. They then go on to say that they temporarily log usage, perform real-time analysis of traffic (which isn&#8217;t logged), comply work with law enforcement, and that their clients may use analytic technology like Google Analytics.</p>
    <p>We mustn&#8217;t forget that Opera itself is an <a href="http://www.operasoftware.com/press/faq">ad network</a> and <a href="http://www.opera.com/privacy">does</a> collect your usage data.</p>
    <p>As always, proceed with caution when selecting a VPN to use. Check out our <a href="https://www.deepdotweb.com/vpn-comparison-chart/">VPN comparison chart</a> if you need help.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/builtin/" rel="tag">builtin</a> <a href="https://www.deepdotweb.com/tag/operas/" rel="tag">operas</a> <a href="https://www.deepdotweb.com/tag/vpn/" rel="tag">vpn</a></span> <span style="display:none" class="updated">2016-04-27</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/fuzzy/" title="Posts by Fuzzy" rel="author">Fuzzy</a></strong></div>
    </div>
</article>

