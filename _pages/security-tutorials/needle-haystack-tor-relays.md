---
layout: single
title: "Needle in a Haystack ~ Tor Relays"
sidebar:
  - title: "Security Tutorials"
    nav: "security"
  - title: "Jolly Rogers Security Guide"
    nav: "jolly"
  - title: "Blog Archive"
    nav: "blognav"

---



</div><span class="wpsr_floatbts_anchor" data-offset="25"></span><p>Since people expressed interest in running relays, I&#8217;ve written a guide that can get you set up. There are many ways to run a relay, so for the sake of simplicity, I will focus on virtual private servers running Ubuntu 12.04. Feedback is definitely welcome.</p>
<p>This guide includes instructions for Windows users. I will write Linux instructions in a separate post, and if someone would like to add Mac instructions, I&#8217;d greatly appreciate it.</p>
<p><strong><span class="bbc_u">Finding a Hosting Provider</span></strong></p>
<p>In order to run a relay, you will need a dedicated server or a virtual private server. There are two features you should look for:</p>
<p>1. Geographical location<br/>
2. Bandwidth</p>
<p>Other specs like RAM and CPU tend not to matter until the bandwidth gets really high, like on an unmetered server. Most of the time, your bandwidth limits will keep the Tor client well below your RAM and CPU limits.</p>
<p>There is no minimum amount that you need to spend on a server. You can lease a VPS for under $10 a month or a dedicated server for hundreds of dollars. I think every little bit helps, especially if the servers are geographically diverse. For this guide, I&#8217;m going to assume you don&#8217;t want to drop hundreds of dollars on your first server, so we&#8217;ll focus on setting up a small to medium sized VPS. The price range I&#8217;m thinking is $10 &#8211; $50 a month, which should give you 512 MB to 1 GB of RAM and 200 GB to 1 TB of bandwidth.</p>
<p>I&#8217;m not going to make specific recommendations for hosting providers, for obvious reasons, but most relays are in North America and Europe. It would be nice if we had more relays in South America, Asia and Africa. The infrastructure in Africa is the most underdeveloped, so you may want to focus on finding providers in South America and Asia. They will be more expensive than providers in North America and Europe. If you can&#8217;t find providers in your price range, it&#8217;s OK to run a relay in North America and Europe. As I said, every little bit helps.</p>
<p>Another thing to consider when searching for a VPS is that there are different virtualization technologies. These include OpenVZ, Xen, VMWare, Virtuozzo, and KVM. For this guide, I&#8217;m going to recommend running your relay in an OpenVZ container, because it is one of the most popular virtualization technologies, it is generally cheaper than the others for the same specs, your operating system will be installed for you by the hosting provider, and the OpenVZ connection limits aren&#8217;t really a problem with low bandwidth relays. If you want your relay to push more than 1 TB of traffic a month, you should switch to something like Xen or KVM, or a dedicated server.</p>
<p>It&#8217;s a good idea to read reviews of the hosting provider before ordering, but this can be tricky. There are a lot of fake web sites with shill reviews. In general, well-known forums with large communities (like webhostingtalk.com) are a better place to look for reviews than random web sites.</p>
<p>When you find a provider that you like, look for their Acceptable Use Policy (AUP), which will sometimes be part of their Terms of Service (TOS). Most hosting providers have links to these documents on their main page. Read through them to find out if they ban proxies. If there is no mention of Tor, &#8220;proxies&#8221; or &#8220;open proxies&#8221; almost always include Tor. Some hosting providers specifically ban Tor. Some only ban exit nodes. The latter case is OK, because we will be setting up non-exit relays. You don&#8217;t want to waste time setting up a relay that will be shut down a week later because it violates your hosting provider&#8217;s AUP.</p>
<p><strong><span class="bbc_u">Ordering a Server</span></strong></p>
<p>Once you find a hosting provider, you can create an account and order the VPS. I don&#8217;t see a problem with leasing a VPS with your real identity. There are 4300 relays at the moment. You will be lost in a big crowd. However, you shouldn&#8217;t mention that you set up a relay in this thread or anywhere else on the forum! You shouldn&#8217;t use information (like a username) that links you to your Silk Road identity! If you really want anonymity, at the end of this guide there&#8217;s a section that offers some suggestions, but keep in mind that takes a lot more work.</p>
<p>During the ordering process, you will be asked to choose an operating system. Select Ubuntu Server 12.04, so we can simplify things. Every VPS provider should have an OpenVZ image for that OS. If the VPS has 512 MB of RAM or less, use the 32 bit version. If it has 1 GB or more, use the 64 bit version.</p>
<p>A common box that you have to fill out is the &#8220;domain name&#8221;. You don&#8217;t need a domain name to order a VPS. You can fill in anything, like example.org. For the server name, put anything you want, it will become the hostname. If it asks for DNS information, just put ns1 and ns2, it doesn&#8217;t matter.</p>
<p>Also, lease the VPS on a monthly basis for the first few months, even if there are discounts for longer terms. Your VPS may turn out to have crappy networking or frequent reboots, so you don&#8217;t want to pay for a year of hosting and be forced to abandon the VPS after a month.</p>
<p>After ordering, you&#8217;ll get an email with the IP address and login details of your VPS.</p>
<p><strong><span class="bbc_u">Configuring the Relay</span></strong></p>
<p>The first thing we need to do is figure out the RelayBandwidthRate based on the monthly bandwidth limit of the VPS. Keep in mind that most hosting providers count both incoming and outgoing bandwidth, so Tor relay traffic gets counted twice. A VPS that pushes 1 TB of traffic from the perspective of the hosting provider, actually pushes 500 GB of traffic from the perspective of the Tor network (it&#8217;s the same data, coming and going).</p>
<p>Let&#8217;s say your VPS is allowed 1 TB of traffic per month. That&#8217;s 1,000,000 MB. So the rate (per second) that you would use in your Tor configuration is:</p>
<p>1,000,000 / 30 / 24 / 60 / 60 / 2 = 0.192 MB or 192 KB</p>
<p>This is a good place to start. In practice, most relays don&#8217;t max out their bandwidth. In fact, many relays only use 30-50% of their max bandwidth rate. You can watch the bandwidth of your relay for a few weeks and increase it if you are using much less than your limit. For example, if in the first two weeks it uses 250 GB (and could have used 500 GB, because that&#8217;s half of your 1 TB per month), then you can double the RelayBandwidthRate. It can take a few weeks of adjusting to find the right balance.</p>
<p>After you get the login information, download PuTTy from the web site:</p>
<p>http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe</p>
<p>This program lets you connect over a protocol called SSH, or Secure Shell, which creates an encrypted connection to a command prompt on the server. Run PuTTy and fill out the following information:</p>
<p>Host name (or IP address): &lt;your VPS IP address&gt;<br/>
Port: 22<br/>
Connection type: SSH</p>
<p>Before we go any further, click on the words &#8220;Default Settings&#8221; under &#8220;Saved Sessions&#8221; and click the Save button to the right of it. That way you don&#8217;t have to enter the IP address each time.</p>
<p>Then click Open. You&#8217;ll see a prompt to accept the server&#8217;s host key, click Yes. You only have do this the first time.</p>
<p>login as: root<br/>
password: &lt;what you were given&gt;</p>
<p>Note that you can resize the window if it&#8217;s too small.</p>
<p>The first thing you should do after logging in is change the root password, especially since it was emailed to you in plaintext. Do that with the following command:</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be41b7761671728" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
passwd</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be41b7761671728-1">1</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be41b7761671728-1"><span class="crayon-v">passwd</span></div></div></td>
</tr>
</table>
</div>
</div>

And enter the password twice.</p>
<p>BTW, for all of these commands, you can copy them from this guide and paste them into PuTTy by right-clicking in the command prompt window.</p>
<p>Now type</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be41c3994543519" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
nano /etc/apt/sources.list</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be41c3994543519-1">1</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be41c3994543519-1"><span class="crayon-v">nano</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">etc</span><span class="crayon-o">/</span><span class="crayon-v">apt</span><span class="crayon-o">/</span><span class="crayon-v">sources</span><span class="crayon-sy">.</span><span class="crayon-v">list</span></div></div></td>
</tr>
</table>
</div>
</div>

Add this line at the end of the file:</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be41c8033327355" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
deb http://deb.torproject.org/torproject.org precise main</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be41c8033327355-1">1</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be41c8033327355-1"><span class="crayon-e">deb </span><span class="crayon-v">http</span><span class="crayon-o">:</span><span class="crayon-c">//deb.torproject.org/torproject.org precise main</span></div></div></td>
</tr>
</table>
</div>
</div>

Enter the following sequence to save the file and exit: ctrl+x, y, enter</p>
<p>Enter the following lines into the command prompt to install Tor and the relay monitor ARM:</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be41cd342313334" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
apt-get update
apt-get install deb.torproject.org-keyring
apt-get update
apt-get install tor tor-arm
</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be41cd342313334-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5534cb1be41cd342313334-2">2</div><div class="crayon-num" data-line="crayon-5534cb1be41cd342313334-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5534cb1be41cd342313334-4">4</div><div class="crayon-num" data-line="crayon-5534cb1be41cd342313334-5">5</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be41cd342313334-1"><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-e">update</span></div><div class="crayon-line crayon-striped-line" id="crayon-5534cb1be41cd342313334-2"><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-e">install </span><span class="crayon-v">deb</span><span class="crayon-sy">.</span><span class="crayon-v">torproject</span><span class="crayon-sy">.</span><span class="crayon-v">org</span><span class="crayon-o">-</span><span class="crayon-e">keyring</span></div><div class="crayon-line" id="crayon-5534cb1be41cd342313334-3"><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-e">update</span></div><div class="crayon-line crayon-striped-line" id="crayon-5534cb1be41cd342313334-4"><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-e">install </span><span class="crayon-e">tor </span><span class="crayon-v">tor</span><span class="crayon-o">-</span><span class="crayon-i">arm</span></div><div class="crayon-line" id="crayon-5534cb1be41cd342313334-5">&nbsp;</div></div></td>
</tr>
</table>
</div>
</div>

Hit Y[enter] whenever it asks you to confirm an action. The first install command will give you a warning because you haven&#8217;t imported the PGP key for that software repository yet, which is what you&#8217;re doing with that command.</p>
<p>Now we&#8217;ll edit the configuration file to turn our Tor client into a relay. First, backup the original configuration file:</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be41d1002662578" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
cp /etc/tor/torrc /etc/tor/torrc.backup</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be41d1002662578-1">1</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be41d1002662578-1"><span class="crayon-v">cp</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">etc</span><span class="crayon-o">/</span><span class="crayon-v">tor</span><span class="crayon-o">/</span><span class="crayon-v">torrc</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">etc</span><span class="crayon-o">/</span><span class="crayon-v">tor</span><span class="crayon-o">/</span><span class="crayon-v">torrc</span><span class="crayon-sy">.</span><span class="crayon-v">backup</span></div></div></td>
</tr>
</table>
</div>
</div>

If you screw something up, you can restore Tor to its default state with the following commands:</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be41d6927212412" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
cp /etc/tor/torrc.backup /etc/tor/torrc
service tor restart</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be41d6927212412-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5534cb1be41d6927212412-2">2</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be41d6927212412-1"><span class="crayon-v">cp</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">etc</span><span class="crayon-o">/</span><span class="crayon-v">tor</span><span class="crayon-o">/</span><span class="crayon-v">torrc</span><span class="crayon-sy">.</span><span class="crayon-v">backup</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">etc</span><span class="crayon-o">/</span><span class="crayon-v">tor</span><span class="crayon-o">/</span><span class="crayon-e">torrc</span></div><div class="crayon-line crayon-striped-line" id="crayon-5534cb1be41d6927212412-2"><span class="crayon-e">service </span><span class="crayon-e">tor </span><span class="crayon-v">restart</span></div></div></td>
</tr>
</table>
</div>
</div>

Let&#8217;s edit the configuration file:</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be41da007083008" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
nano /etc/tor/torrc</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be41da007083008-1">1</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be41da007083008-1"><span class="crayon-v">nano</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">etc</span><span class="crayon-o">/</span><span class="crayon-v">tor</span><span class="crayon-o">/</span><span class="crayon-v">torrc</span></div></div></td>
</tr>
</table>
</div>
</div>

Find the following lines and remove the # at the beginning. Anything that follows a # is treated as a comment instead of an instruction to Tor, so we are adding these instructions.</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be41df305177571" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
ControlPort 9051              # This is a comment that Tor ignores, but everything before the hash is an instruction that Tor reads
CookieAuthentication 1

ORPort 9001                   # Change this to ORPort 443  !!!!

Nickname ididnteditheconfig   # Change ididnteditheconfig to whatever nickname you want, no spaces, nothing drug or SR related

RelayBandwidthRate 100 KB     # Change 100 KB to whatever you calculated for your server earlier
RelayBandwidthBurst 200 KB    # Make this double the value above. If you server is using too much bandwidth, make this the same as the line above

ContactInfo Random Person &amp;lt;nobody AT example dot com&amp;gt;  # Create a throwaway email address and put it here

ExitPolicy reject *:*         # This line makes your relay a non-exit</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be41df305177571-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5534cb1be41df305177571-2">2</div><div class="crayon-num" data-line="crayon-5534cb1be41df305177571-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5534cb1be41df305177571-4">4</div><div class="crayon-num" data-line="crayon-5534cb1be41df305177571-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-5534cb1be41df305177571-6">6</div><div class="crayon-num" data-line="crayon-5534cb1be41df305177571-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-5534cb1be41df305177571-8">8</div><div class="crayon-num" data-line="crayon-5534cb1be41df305177571-9">9</div><div class="crayon-num crayon-striped-num" data-line="crayon-5534cb1be41df305177571-10">10</div><div class="crayon-num" data-line="crayon-5534cb1be41df305177571-11">11</div><div class="crayon-num crayon-striped-num" data-line="crayon-5534cb1be41df305177571-12">12</div><div class="crayon-num" data-line="crayon-5534cb1be41df305177571-13">13</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be41df305177571-1"><span class="crayon-i">ControlPort</span><span class="crayon-h"> </span><span class="crayon-cn">9051</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-p"># This is a comment that Tor ignores, but everything before the hash is an instruction that Tor reads</span></div><div class="crayon-line crayon-striped-line" id="crayon-5534cb1be41df305177571-2"><span class="crayon-i">CookieAuthentication</span><span class="crayon-h"> </span><span class="crayon-cn">1</span></div><div class="crayon-line" id="crayon-5534cb1be41df305177571-3">&nbsp;</div><div class="crayon-line crayon-striped-line" id="crayon-5534cb1be41df305177571-4"><span class="crayon-i">ORPort</span><span class="crayon-h"> </span><span class="crayon-cn">9001</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-p"># Change this to ORPort 443  !!!!</span></div><div class="crayon-line" id="crayon-5534cb1be41df305177571-5">&nbsp;</div><div class="crayon-line crayon-striped-line" id="crayon-5534cb1be41df305177571-6"><span class="crayon-e">Nickname </span><span class="crayon-i">ididnteditheconfig</span> <span class="crayon-h"> </span> <span class="crayon-p"># Change ididnteditheconfig to whatever nickname you want, no spaces, nothing drug or SR related</span></div><div class="crayon-line" id="crayon-5534cb1be41df305177571-7">&nbsp;</div><div class="crayon-line crayon-striped-line" id="crayon-5534cb1be41df305177571-8"><span class="crayon-i">RelayBandwidthRate</span><span class="crayon-h"> </span><span class="crayon-cn">100</span><span class="crayon-h"> </span><span class="crayon-i">KB</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-p"># Change 100 KB to whatever you calculated for your server earlier</span></div><div class="crayon-line" id="crayon-5534cb1be41df305177571-9"><span class="crayon-i">RelayBandwidthBurst</span><span class="crayon-h"> </span><span class="crayon-cn">200</span><span class="crayon-h"> </span><span class="crayon-i">KB</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-p"># Make this double the value above. If you server is using too much bandwidth, make this the same as the line above</span></div><div class="crayon-line crayon-striped-line" id="crayon-5534cb1be41df305177571-10">&nbsp;</div><div class="crayon-line" id="crayon-5534cb1be41df305177571-11"><span class="crayon-e">ContactInfo </span><span class="crayon-e">Random </span><span class="crayon-v">Person</span><span class="crayon-h"> </span><span class="crayon-o">&amp;</span><span class="crayon-v">lt</span><span class="crayon-sy">;</span><span class="crayon-e">nobody </span><span class="crayon-e">AT </span><span class="crayon-e">example </span><span class="crayon-e">dot </span><span class="crayon-v">com</span><span class="crayon-o">&amp;</span><span class="crayon-v">gt</span><span class="crayon-sy">;</span> <span class="crayon-h"> </span><span class="crayon-p"># Create a throwaway email address and put it here</span></div><div class="crayon-line crayon-striped-line" id="crayon-5534cb1be41df305177571-12">&nbsp;</div><div class="crayon-line" id="crayon-5534cb1be41df305177571-13"><span class="crayon-e">ExitPolicy </span><span class="crayon-e ">reject *</span><span class="crayon-o">:</span><span class="crayon-o">*</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-p"># This line makes your relay a non-exit</span></div></div></td>
</tr>
</table>
</div>
</div>

Then type: ctrl+x, y, enter</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be41e4950539172" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
service tor reload</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be41e4950539172-1">1</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be41e4950539172-1"><span class="crayon-e">service </span><span class="crayon-e">tor </span><span class="crayon-v">reload</span></div></div></td>
</tr>
</table>
</div>
</div>

Congratulations, you&#8217;re running a relay!</p>
<p>The RelayBandwidthRate and RelayBandwidthBurst are what you will probably want to adjust after a few weeks of watching your relay&#8217;s bandwidth.</p>
<p>A note about the contact info. You don&#8217;t need to enter a name. Remove the &#8220;Random Person&#8221; part entirely. However, you should enter a real email address. The purpose of providing an email address is if your relay is misconfigured, the Tor people can contact you and tell you about it. On the other hand, this email address will appear in your relay&#8217;s descriptor, which is public, so use an alternate address from any of your main ones.</p>
<p>There is a program called ARM (Anonymous Relay Monitor) that lets you monitor your relay. To run it, type:</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be41e9314053780" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
arm</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be41e9314053780-1">1</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be41e9314053780-1"><span class="crayon-v">arm</span></div></div></td>
</tr>
</table>
</div>
</div>

You can click the left and right arrow keys to see the different panels of info. To exit arm, type: q, q</p>
<p>Another way to view info about your relay is to search for it on https://atlas.torproject.org</p>
<p>Finally, to exit the SSH session, type:</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be41ed813661488" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
exit</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be41ed813661488-1">1</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be41ed813661488-1"><span class="crayon-v">exit</span></div></div></td>
</tr>
</table>
</div>
</div>

<strong><span class="bbc_u">Securing Your Server</span></strong></p>
<p>The following is not necessary, but it&#8217;s an extremely good idea.</p>
<p>A better way to log in to your server is to create a regular user account, disable root logins, create an SSH key for your regular user, and disable password logins. That makes it virtually impossible for someone to break into your server (people try to hack into servers through SSH all day long).</p>
<p>To create a regular user account, enter this command:</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be41f2566877719" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
adduser &amp;lt;username&amp;gt;</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be41f2566877719-1">1</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be41f2566877719-1"><span class="crayon-v">adduser</span><span class="crayon-h"> </span><span class="crayon-o">&amp;</span><span class="crayon-v">lt</span><span class="crayon-sy">;</span><span class="crayon-v">username</span><span class="crayon-o">&amp;</span><span class="crayon-v">gt</span><span class="crayon-sy">;</span></div></div></td>
</tr>
</table>
</div>
</div>

Change &lt;username&gt; to any one-word username you want.</p>
<p>Enter the password for that user twice, and make it different from root&#8217;s password. Leave the rest of the prompts (like Full Name) blank by hitting enter through them, then hit y at the end.</p>
<p>You can test out your new user. Exit the SH session and launch PuTTy again. Now that you have a regular user, you can add it to the PuTTy configuration so you don&#8217;t have to type it in every time.</p>
<p>In the configuration window that you get when PuTTy launches, go to Connection -&gt; Data</p>
<p>Auto-login username: &lt;the regular user you created&gt;</p>
<p>Go back to the Session section, highlight &#8220;Default Settings&#8221;, and click Save again. Connect to your server. You should only have to enter the password this time, and of course it will be your regular user&#8217;s password.</p>
<p>When you login as the regular user, you can&#8217;t do much outside of your home folder. You can&#8217;t install or remove software. This is a security feature. You have to become root. In order to do that, type:</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be41f7931521513" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
su</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be41f7931521513-1">1</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be41f7931521513-1"><span class="crayon-v">su</span></div></div></td>
</tr>
</table>
</div>
</div>

And enter root&#8217;s password.</p>
<p>To exit being root, type exit, and to completely exit the SSH session, type exit again.</p>
<p>Let&#8217;s make this even more secure by adding an SSH key.</p>
<p>Download this program and run it:</p>
<p>http://the.earth.li/~sgtatham/putty/latest/x86/puttygen.exe</p>
<p>Next to &#8220;Generate a public/private key pair&#8221;, click Generate. This will take a few minutes. Click around randomly to create entropy and speed it up.</p>
<p>When it&#8217;s done, it&#8217;ll say &#8220;Public key for pasting into OpenSSH authorized_keys file&#8221;. Copy the entire thing in the box. Log into your server as the regular user and type this:</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be41fc058191385" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
mkdir .ssh
nano .ssh/authorized_keys
</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be41fc058191385-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5534cb1be41fc058191385-2">2</div><div class="crayon-num" data-line="crayon-5534cb1be41fc058191385-3">3</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be41fc058191385-1"><span class="crayon-i">mkdir</span><span class="crayon-h"> </span><span class="crayon-sy">.</span><span class="crayon-e">ssh</span></div><div class="crayon-line crayon-striped-line" id="crayon-5534cb1be41fc058191385-2"><span class="crayon-i">nano</span><span class="crayon-h"> </span><span class="crayon-sy">.</span><span class="crayon-v">ssh</span><span class="crayon-o">/</span><span class="crayon-v">authorized</span><span class="crayon-sy">_</span>keys</div><div class="crayon-line" id="crayon-5534cb1be41fc058191385-3">&nbsp;</div></div></td>
</tr>
</table>
</div>
</div>

Paste that public key in (by right-clicking once, as before). Then hit ctrl+x, y, enter.</p>
<p>Back in PuTTyGen, enter a key pass phrase and confirm it, then click &#8220;Save private key&#8221; and save it somewhere on your computer. The pass phrase protects your private key just like with PGP. At this point you can exit out of PuTTyGen.</p>
<p>Now launch PuTTy again, and in the configuration window, go to Connection -&gt; SSH -&gt; Auth.</p>
<p>Find the field that says Private key file for authentication, click Browse and select your private key.</p>
<p>Go back to Session, highlight &#8220;Default Settings&#8221; and Save.</p>
<p>Connect to your server again. This time it will ask you for the pass phrase to your private key, not the password to the regular user.</p>
<p>If you login successfully, great! You can disable root and password logins. Type:</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be4201751988783" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
su
nano /etc/ssh/sshd_config</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be4201751988783-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5534cb1be4201751988783-2">2</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be4201751988783-1"><span class="crayon-e">su</span></div><div class="crayon-line crayon-striped-line" id="crayon-5534cb1be4201751988783-2"><span class="crayon-v">nano</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">etc</span><span class="crayon-o">/</span><span class="crayon-v">ssh</span><span class="crayon-o">/</span><span class="crayon-v">sshd_config</span></div></div></td>
</tr>
</table>
</div>
</div>

Find these lines:</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be4205584816713" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
PermitRootLogin yes             # Change it to no

#PasswordAuthentication yes     # Remove the # at the beginning and change it to no
</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be4205584816713-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5534cb1be4205584816713-2">2</div><div class="crayon-num" data-line="crayon-5534cb1be4205584816713-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5534cb1be4205584816713-4">4</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be4205584816713-1"><span class="crayon-e">PermitRootLogin </span><span class="crayon-i">yes</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-p"># Change it to no</span></div><div class="crayon-line crayon-striped-line" id="crayon-5534cb1be4205584816713-2">&nbsp;</div><div class="crayon-line" id="crayon-5534cb1be4205584816713-3"><span class="crayon-p">#PasswordAuthentication yes     # Remove the # at the beginning and change it to no</span></div><div class="crayon-line crayon-striped-line" id="crayon-5534cb1be4205584816713-4">&nbsp;</div></div></td>
</tr>
</table>
</div>
</div>

Save and exit with ctrl+x, y, enter.</p>
<p>Restart the SSH server:</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be420a866736355" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
service ssh restart</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be420a866736355-1">1</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be420a866736355-1"><span class="crayon-e">service </span><span class="crayon-e">ssh </span><span class="crayon-v">restart</span></div></div></td>
</tr>
</table>
</div>
</div>

Exit completely out and log back in as the regular user. You should login just fine. To test your settings, you can change PuTTy to login as root and it should deny you.</p>
<p>Now think about what an attacker has to do to get into your server. First he has to guess your regular username. Then he has to steal your private key or brute force one that works with your public key. That&#8217;s like having a 2048 bit password! Then he has to guess root&#8217;s password. Your server is very secure.</p>
<p><strong><span class="bbc_u">Server Maintenance</span></strong></p>
<p>You should login in to your server every once in a while and update the software. Login as the regular user, change to root (su), and issue these commands:</p>
<div class="codeheader">Code: <a class="codeoperation">[Select]</a></div>

<div id="crayon-5534cb1be420f387292741" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
apt-get update
apt-get dist-upgrade</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5534cb1be420f387292741-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5534cb1be420f387292741-2">2</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5534cb1be420f387292741-1"><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-e">update</span></div><div class="crayon-line crayon-striped-line" id="crayon-5534cb1be420f387292741-2"><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-v">dist</span><span class="crayon-o">-</span><span class="crayon-v">upgrade</span></div></div></td>
</tr>
</table>
</div>
</div>

<strong><span class="bbc_u">Purchasing a Server Anonymously</span></strong></p>
<p>As I said before, I don&#8217;t think it&#8217;s necessary, but if you want to get a server anonymously, here are some ideas that may or may not work. Suggestions are definitely welcome. <img class="smiley" title="Smiley" src="http://silkroad5v7dywlc.onion/Smileys/default/smiley.gif" alt=":)"/></p>
<p>The first thing you need to realize is that the vast majority of hosting providers use fraud detection services, because hackers and spammers love leasing servers anonymously or with stolen credit cards. You almost certainly can&#8217;t sign up with a hosting provider from a Tor exit node. A popular fraud detection service called MaxMind claims to block VPNs and open proxies too:</p>
<p>https://www.maxmind.com/en/ipauthentication</p>
<p>If you really want to be anonymous, I don&#8217;t think you should be using a VPN anyway, because you&#8217;re trusting their word that they don&#8217;t log, or that LE won&#8217;t compel them to log in the future. The best way to find a &#8220;clean&#8221; IP address is to point Tor browser at a web proxy. There are web sites that list thousands of them, but for obvious reasons I won&#8217;t list them here. You may have try many web proxies before you find one that isn&#8217;t blocked.</p>
<p>The other issue is payment method. There are a few dozen hosting providers that accept bitcoins, which you could use by anonymizing them your normal way, but all of the ones that I know about are in North America and Europe, which doesn&#8217;t help the diversity of the Tor network. Again, if you really want to be anonymous, that&#8217;s fine because a relay in NA or EU is better than no relay.</p>
<p>Other than bitcoins, there are a few potentially anonymous payment methods with fiat currency.</p>
<p>1. Prepaid debit cards<br/>
2. e-currency and precious metals exchanges, like Pecunix<br/>
3. an anonymous PayPal account</p>
<p>MaxMind claims to block prepaid debit cards:</p>
<p>https://www.maxmind.com/en/ccv_overview</p>
<p>So I don&#8217;t know if that will work.</p>
<p>As far as e-currency exchanges go, Liberty Reserve is gone, so I don&#8217;t know what else exists other than Pecunix, but by routing money through several exchanges, you can potentially anonymize it. You&#8217;ll have to find a hosting provider that takes these payment methods, or cash out to a different payment method.</p>
<p>Also, you might be able to register a PayPal account by pointing Tor Browser at a web proxy, and use fake info that is geographically close to that proxy, then go to Freenode #bitcoin-otc or localbitcoins.com and sell BTC for PayPal credit that gets deposited to your account, then use that to pay for the server.</p>
<p>All of these methods involve some work and a high chance of failure, but you&#8217;re welcome to try them.</p>
<h3>Share and Enjoy</h3>




Updated: 2014-05-11


