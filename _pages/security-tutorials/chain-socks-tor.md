---
layout: single
title: "How to chain socks with Tor"
sidebar:
  - title: "Security Tutorials"
    nav: "security"
  - title: "Jolly Rogers Security Guide"
    nav: "jolly"
  - title: "Blog Archive"
    nav: "blognav"

---

<p><strong>How to chain socks with Tor</strong></p>
<p><strong>Written By:</strong> ?</p>
<p><strong>Introduction</strong></p>
<p>There are many reasons why you would need to add an extra hop after the exit node. If you&#8217;re trying to card some items on any site with fraud filters you&#8217;re obviously going to raise some flags if the cardholder lives in New York and you&#8217;re connecting from a German exit node. Same goes for Paypal logins. Keep in mind you will need to use a clean socks5 within the same region as the cardholder/account. If US within the same state, or otherwise within the same area. A link to sites providing private socks services is provided at the end of this article.</p>
<p>Even if carding isn&#8217;t your thing many sites filter out exit nodes, so it&#8217;s a necessity to have some control over where you appear to be connecting from.</p>
<p>Note: If you have the Tor Browser Bundle and haven&#8217;t installed Tor separately, use port 9150 in place of 9050 for the following configurations.</p>
<p><strong>Proxychains</strong></p>
<div class="quoteheader">
<div class="topslice_quote">Quote</div>
</div>
<blockquote class="bbc_standard_quote"><p>First download &amp; install proxychains:</p>
<p>sudo apt-get install proxychains</p>
<p>Then configure proxychains to setup your chain:</p>
<p>sudo nano /etc/proxychains.conf</p></blockquote>
<p>Down towards the bottom you should see:</p>
<div class="quoteheader">
<div class="topslice_quote">Quote</div>
</div>
<blockquote class="bbc_standard_quote">[ProxyList]
# add proxy here &#8230;<br />
# meanwile<br />
# defaults set to &#8220;tor&#8221;</p></blockquote>
<p>Just write your list in using Tor as the first listed:</p>
<div class="quoteheader">
<div class="topslice_quote">Quote</div>
</div>
<blockquote class="bbc_standard_quote"><p>socks4 127.0.0.1 9050<br />
socks5 ip.address.here port</p></blockquote>
<p>After that you should be done. Just go to terminal and set your browser to go through proxychains:</p>
<p>proxychains firefox</p>
<p><strong>Proxifier</strong></p>
<p>If you are on Windows you will want to setup your chain using Proxifier. First download and install a cracked copy of proxifier. Once you have it installed and run go to Options -&gt; Proxy Settings and configure your chain:</p>
<div class="quoteheader">
<div class="topslice_quote">Quote</div>
</div>
<blockquote class="bbc_standard_quote"><p>127.0.0.1  | 9050 | SOCKS 5<br />
IP.ADDRESS | PORT | SOCKS 5</p></blockquote>
<p>Once you have set your proxy settings go to Options -&gt; Proxification Rules and set the following rules:</p>
<div class="quoteheader">
<div class="topslice_quote">Quote</div>
</div>
<blockquote class="bbc_standard_quote"><p>Loopback | ALL | 127.0.0.1 | ALL<br />
Tor           | tor.exe | ALL  | ALL</p></blockquote>
<p>Once you are finished go to Name Resolution, choose Remote, click OK, and you&#8217;re set. Keep in mind that if you use Proxifier you need to use a browser that isn&#8217;t already configured to connect through Tor or it will ignore the Proxifier settings and just route strictly through Tor. For this guide my recommendation is a copy of Firefox Portable that has been secured.<br />
Instructions for Proxifier 3.0</p>
<p>Profile -&gt; Proxy Servers -&gt; Add.</p>
<p>Address 127.0.0.1, Port 9050, Socks v5 -&gt; Ok. Popup box will ask whether to set as default. Select Yes.</p>
<p>Now add your proxy you want to use in the same way. Click &#8216;Proxychains&#8217; button then &#8216;Create&#8217;, and drag &amp; drop to the new rule. You should have something that looks like this.</p>
<p>New<br />
127.0.0.1:9050<br />
IP address:port (the details you entered earlier)</p>
<p>Now go to Profile -&gt; Proxification Rules.</p>
<p>In the drop down menu for &#8216;Default&#8217; select &#8216;Proxy socks5 127.0.0.1&#8217; &amp; uncheck the localhost rule.</p>
<p>Then Add -&gt; change action to &#8216;Chain new&#8217;. -&gt;Ok.</p>
<p>Next, Profile -&gt; Name Resolution. Select Resolve hostname through Proxy.</p>
<div class="quoteheader">
<div class="topslice_quote">Quote</div>
</div>
<blockquote class="bbc_standard_quote"><p>Socks Providers</p>
<p>http://vip72.com<br />
http://super-socks.com<br />
http://5socks.net<br />
http://winsocks.net</p>
<p>Blacklists</p>
<p>http://www.ip-score.com<br />
http://whoer.net</p></blockquote>
<p>Thats it&#8230;.you&#8217;re good to go.</p>

Updated: 2014-05-11

