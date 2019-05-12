---
Securing Firefox
---
post-5490


<div class="wp-socializer-buttons clearfix">
<span class="wpsr-btn">

<div class="fb-like" data-href="http://www.deepdotweb.com/security-tutorials/securing-firefox/" data-share="false" data-layout="button_count" data-show-faces="0" data-action="like" data-colorscheme="light"></div>

</span>
<span class="wpsr-btn">

<a href="http://twitter.com/share" class="twitter-share-button" data-count="horizontal" data-lang="en" data-url="http://www.deepdotweb.com/security-tutorials/securing-firefox/" data-text="Securing Firefox - "></a>

</span>
<span class="wpsr-btn">

<div class="g-plusone" data-size="medium" data-href="http://www.deepdotweb.com/security-tutorials/securing-firefox/"></div>

</span>
<span class="wpsr-btn">

<script type="IN/Share" data-url="http://www.deepdotweb.com/security-tutorials/securing-firefox/" data-counter="right"></script>

</span>
<span class="wpsr-btn">

<su:badge layout="1"></su:badge>

</span>
</div><span class="wpsr_floatbts_anchor" data-offset="25"></span><p><strong>Written By:</strong> Unknown</p>
<p><strong>Introduction</strong></p>
<p>Chaining a socks with proxychains/proxifier means forfeiting the protection of Torbutton, which leaves you open to browser fingerprinting.</p>
<p>Set everything up as you would at the point of entering card details (enable javascript &amp; allow noscript), then run a test at http://ip-check.info (just cancel the pop-up).</p>
<p>You might get a nasty surprise at some of the info your browser is leaking. Admittedly some of it is a bit alarmist (they&#8217;re trying to sell a product after all), but some are of genuine concern &#8211; particularly if you&#8217;re trying to card the same site a few times.</p>
<p>I tend to use one browser (regular firefox) for only chaining proxies, and have found the following adjustments helpful. Please feel free to add to the list. http://check2ip.com is also a useful check for mismatches</p>
<p><strong>about:config</strong></p>
<div class="quoteheader">
<div class="topslice_quote">Quote</div>
</div>
<blockquote class="bbc_standard_quote"><p>geo.enabled = false</p>
<p>geo.wifi.uri = [leave blank]
<p>network.http.accept.default = text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8</p>
<p>network.http.use-cache = false</p>
<p>network.http.keep-alive.timeout = 600</p>
<p>network.http.max-persistent-connections-per-proxy = 16</p>
<p>network.proxy.socks_remote_dns = true</p>
<p>network.cookie.lifetimePolicy = 2</p>
<p>network.http.sendRefererHeader = 0</p>
<p>network.http.sendSecureXSiteReferrer = false</p>
<p>network.protocol-handler.external = false [set the default and all the subsettings to false]
<p>network.protocol-handler.warn-external = true [set the default and all the subsettings to true]
<p>network.http.pipelining = true</p>
<p>network.http.pipelining.maxrequests = 8</p>
<p>network.http.proxy.keep-alive = true</p>
<p>network.http.proxy.pipelining = true</p>
<p>network.prefetch-next = false</p>
<p>browser.cache.disk.enable = false</p>
<p>browser.cache.offline.enable = false</p>
<p>browser.sessionstore.privacy_level = 2</p>
<p>browser.sessionhistory.max_entries = 2</p>
<p>browser.display.use_document_fonts = 0</p>
<p>intl.charsetmenu.browser.cache = ISO-8859-9, windows-1252, windows-1251, ISO-8859-1, UTF-8</p>
<p>dom.storage.enabled = false</p>
<p>extensions.blocklist.enabled = false</p></blockquote>
<p><strong>Other Settings</strong></p>
<div class="quoteheader">
<div class="topslice_quote">Quote</div>
</div>
<blockquote class="bbc_standard_quote"><p>Disable all plugins [tools -&gt; addons -&gt; plugins]
Disable all live bookmarks [bookmarks -&gt; bookmarks toolbar -&gt; R/click latest headlines -&gt; delete]
Disable all updates [tools -&gt; options -&gt; advanced -&gt; update]
Enable &#8216;do not track&#8217; feature [tools -&gt; options -&gt; privacy]
Enable private browsing, configure to remember nothing &amp; disable 3rd party cookies. [tools -&gt; options -&gt; privacy]</blockquote>
<p><strong>Useful add-ons</strong></p>
<p>BetterPrivacy<br/>
Close n forget<br/>
Ghostery<br/>
Https-Everywhere<br/>
Modify Headers<br/>
NoScript<br/>
RefControl<br/>
User Agent Switcher</p>
<h3>Share and Enjoy</h3>

<div class="wp-socializer 32px">
<ul class="wp-socializer-opacity columns-no">
<li><a href="http://www.facebook.com/share.php?u=http%3A%2F%2Fwww.deepdotweb.com%2Fsecurity-tutorials%2Fsecuring-firefox%2F&amp;t=Securing+Firefox" title="Share this on Facebook" target="_blank" rel="nofollow"><img src="http://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="Facebook" style="width:32px; height:32px; background: transparent url(http://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -330px; border:0;"/></a></li>
<li><a href="http://twitter.com/home?status=Securing+Firefox%20-%20http%3A%2F%2Fwww.deepdotweb.com%2Fsecurity-tutorials%2Fsecuring-firefox%2F%20" title="Tweet this !" target="_blank" rel="nofollow"><img src="http://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="Twitter" style="width:32px; height:32px; background: transparent url(http://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -1386px; border:0;"/></a></li>
<li><a href="http://delicious.com/post?url=http%3A%2F%2Fwww.deepdotweb.com%2Fsecurity-tutorials%2Fsecuring-firefox%2F&amp;title=Securing+Firefox&amp;notes=Written+By%3A+Unknown%0D%0A%0D%0AIntroduction%0D%0A%0D%0AChaining+a+socks+with+proxychains%2Fproxifier+means+forfeiting+the+protection+of+Torbutton%2C+which+leaves+you+open+to+browser+fingerprinting.%0D%0A%0D%0ASet+everything+up+as+you+would+at+the+point+of+entering+card+details" title="Post this on Delicious" target="_blank" rel="nofollow"><img src="http://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="Delicious" style="width:32px; height:32px; background: transparent url(http://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -132px; border:0;"/></a></li>
<li><a href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http%3A%2F%2Fwww.deepdotweb.com%2Fsecurity-tutorials%2Fsecuring-firefox%2F&amp;title=Securing+Firefox&amp;source=Deep+Dot+Web+-+Meme+and+News+From+the+Other+side+of+the+Web&amp;summary=Written+By%3A+Unknown%0D%0A%0D%0AIntroduction%0D%0A%0D%0AChaining+a+socks+with+proxychains%2Fproxifier+means+forfeiting+the+protection+of+Torbutton%2C+which+leaves+you+open+to+browser+fingerprinting.%0D%0A%0D%0ASet+everything+up+as+you+would+at+the+point+of+entering+card+details" title="Share this on LinkedIn" target="_blank" rel="nofollow"><img src="http://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="LinkedIn" style="width:32px; height:32px; background: transparent url(http://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -693px; border:0;"/></a></li>
<li><a href="http://www.stumbleupon.com/submit?url=http%3A%2F%2Fwww.deepdotweb.com%2Fsecurity-tutorials%2Fsecuring-firefox%2F&amp;title=Securing+Firefox" title="Submit this to StumbleUpon" target="_blank" rel="nofollow"><img src="http://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="StumbleUpon" style="width:32px; height:32px; background: transparent url(http://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -1287px; border:0;"/></a></li>
<li><a href="http://www.deepdotweb.com/security-tutorials/securing-firefox/" onclick="addBookmark(event);" title="Add to favorites" target="_blank" rel="nofollow"><img src="http://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="Add to favorites" style="width:32px; height:32px; background: transparent url(http://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -0px; border:0;"/></a></li>
<li><a href="/cdn-cgi/l/email-protection#2e115a4113085d5b4c444b4d5a137d4b4d5b5c4740490568475c4b484156084c414a5713795c475a5a4b40056c570b1d6f057b4045404159400b1e6a0b1e6f0b1e6aX%0AIntroduction%0D%0A%0D%0AChaining+a+socks+with+proxychains%2Fproxifier+means+forfeiting+the+protection+of+Torbutton%2C+which+leaves+you+open+to+browser+fingerprinting.%0D%0A%0D%0ASet+everything+up+as+you+would+at+the+point+of+entering+card+details%20-%20http://www.deepdotweb.com/security-tutorials/securing-firefox/" title="Email this" target="_blank" rel="nofollow"><img src="http://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="Email" style="width:32px; height:32px; background: transparent url(http://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -297px; border:0;"/></a></li>
<li><a href="http://www.deepdotweb.com/feed/rss/" title="Subscribe to RSS" target="_blank" rel="nofollow"><img src="http://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="RSS" style="width:32px; height:32px; background: transparent url(http://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -1221px; border:0;"/></a></li>
</ul>
<div class="wp-socializer-clearer"></div></div>


Updated: 2014-05-11</span>
<a href="http://www.deepdotweb.com/author/admin/" title="Posts by DeepDotWeb" rel="author">DeepDotWeb</a></strong></div>


