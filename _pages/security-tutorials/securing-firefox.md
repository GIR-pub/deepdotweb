---
title: "Securing Firefox"
sidebar:
  - title: "Security Tutorials"
    nav: "security"
  - title: "Jolly Rogers Security Guide"
    nav: "jolly"
  - title: "Blog Archive"
    nav: "blognav"

---



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




Updated: 2014-05-11


