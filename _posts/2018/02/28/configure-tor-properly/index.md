---
How To Configure Tor Properly
---
<article class="post-listing post-24893 post type-post status-publish format-standard has-post-thumbnail hentry 
tag-configure tag-properly 
<div class="post-inner">
<span>Posted by: <a href="https://www.deepdotweb.com/author/theinnocent/" title="">TheInnocent </a></span>
<span>February 28, 2018</span>

<span><a href="https://www.deepdotweb.com/2018/02/28/configure-tor-properly/#comments">4 Comments</a></span>


<p>Tor is a renowned must in the anonymity field, and the first fundamental step in your fight for privacy. You could think that the only thing that you need to hide your identity while surfing the web is to download the Tor browser bundle, but this is not enough. There are, in fact, wrong behaviours that can reveal your real identity and location even if you’re using Tor, as well as tricks to keep you safe and stealth. In this article, I will explain the basics to introduce you to the Onion world, teaching you how to not get betrayed by your bad habits.</p>
<p><img class="wp-image-24896" src="/imgs/2018/02/word-image-33.png" srcset="/imgs/2018/02/word-image-33.png 1280w, /imgs/2018/02/word-image-33-300x181.png 300w, /imgs/2018/02/word-image-33-1024x619.png 1024w" sizes="(max-width: 1280px) 100vw, 1280px" /></p>
<h2>The Tor Network</h2>
<p>The <a href="https://www.deepdotweb.com/2017/12/21/novel-defense-techniques-secure-tor-communications-research-study/">Tor</a> network, made by servers run by volunteers, allow users to hide their identity from the sites they visit and prevent eavesdroppers to watch their traffic. Your communications are encrypted and bounced from a relay to another, lastly arriving to their destination. Combined with https, Tor provides end-to-end encryption, making it impossible even for the Tor volunteers to read your traffic, and your source IP is well masked by the last relay’s IP. So what could go wrong? Why are these security measures are not enough to keep you safe and <a href="https://www.deepdotweb.com/2016/04/12/onionscan-tests-anonymity-dark-net-domains/">anonymous</a>?</p>
<h2>Starting Tips</h2>
<p>To start correcting your browsing habits, we can follow a few suggestions:</p>
<ul>
<li>Use exclusively the Tor browser. Even if it is possible to make every browser connect to the Tor network, it is recommended to use the Tor browser that is fine tuned with this purpose in mind. The other browsers, in fact, all have issues with their configurations, that could lead to your identity leakage.</li>
<li>Don’t torrent over Tor. It is well known that the torrent file-sharing applications can ignore proxy settings, giving away your real IP to the external world. A further reason, is that torrenting over Tor can heavily slow down the entire network.</li>
<li>Use HTTPS Everywhere. The Tor browser has a plugin called HTTPS Everywhere, that forces the supported websites to use HTTPS, if possible. This results in end to end encryption for you. Check the <a href="https://www.eff.org/it/pages/tor-and-https">EFF</a>’s interactive page to better understand this key concept.</li>
<li>Don’t enable or install extra browser plugins. The only plugins that you need are included in the Tor browser. Other plugins could reveal your real identity, making completely useless your usage of Tor.</li>
<li>Don’t open documents downloaded with Tor when you’re online. If you open a document downloaded with Tor, it could contain links that connect to a website without passing through Tor. This would reveal your identity.</li>
<li>Completely disable javascript (only in extreme cases). Tor browser uses the NoScript plugin to limit, where possible, the usage of Javascript. Anyway, if you want to be completely safe from JS leakage of your IP, you can disable it in the configuration of your Tor browser. Go to about:config and turn the “javascript.enabled” voice, to false. Keep in mind that JS is fundamental to render almost all the websites today, so disable it only if truly necessary.</li>
<li>Disable referers. Go to about:config and disable “network.http.sendRefererHeader” (turn it from 2 to 0). The referer header tells the browser where you come from (from which page), so for privacy reasons you may want to disable it.</li>
<li>Disable iframes. Go to about:config and disable “noscript.forbidIFramesContext” changing its value to 0. Iframes can be used to spread a <a href="https://www.deepdotweb.com/2017/11/03/malware-analysis-tools-explained/">malware</a> through your browser. Like the case of JS, they are used everywhere so, disabling them, it’s an extreme measure.</li>
<li>Use bridges. While the observation of the above precautions will let you surf the internet anonymously, it won’t mask the fact that you are using Tor, thus, a traffic watcher could be notice that you are using Tor even ignoring sites you are visiting. If you are concerned about this problem, I strongly suggest to use Tor bridges. Let’s see together what Tor bridges are and how to configure them.</li>
</ul>
<h2>Configuring Tor Bridges</h2>
<p>If Tor does not work, click on “configure” in the main window, and skip the proxy phase:</p>
<p><img class="wp-image-24897" src="/imgs/2018/02/word-image-34.png" srcset="/imgs/2018/02/word-image-34.png 485w, /imgs/2018/02/word-image-34-300x270.png 300w" sizes="(max-width: 485px) 100vw, 485px" /> <img class="wp-image-24898" src="/imgs/2018/02/word-image-35.png" srcset="/imgs/2018/02/word-image-35.png 485w, /imgs/2018/02/word-image-35-300x270.png 300w" sizes="(max-width: 485px) 100vw, 485px" /></p>
<p>Then, click on “yes” in the following screen and choose “obfs4” as the default transport type:</p>
<p><img class="wp-image-24900" src="/imgs/2018/02/word-image-36.png" srcset="/imgs/2018/02/word-image-36.png 485w, /imgs/2018/02/word-image-36-300x267.png 300w" sizes="(max-width: 485px) 100vw, 485px" /> <img class="wp-image-24901" src="/imgs/2018/02/word-image-37.png" srcset="/imgs/2018/02/word-image-37.png 602w, /imgs/2018/02/word-image-37-300x197.png 300w" sizes="(max-width: 602px) 100vw, 602px" /></p>
<p>In the case that your Tor browser works, follow this other procedure: click on the onion button:</p>
<p><img class="wp-image-24902" src="/imgs/2018/02/word-image-38.png" /></p>
<p>then, select “Tor is censored in my country”:</p>
<p><img class="wp-image-24903" src="/imgs/2018/02/word-image-39.png" srcset="/imgs/2018/02/word-image-39.png 541w, /imgs/2018/02/word-image-39-300x278.png 300w" sizes="(max-width: 541px) 100vw, 541px" /></p>
<p>next, choose the transport type “obfs4”:</p>
<p><img class="wp-image-24904" src="/imgs/2018/02/word-image-40.png" srcset="/imgs/2018/02/word-image-40.png 541w, /imgs/2018/02/word-image-40-300x286.png 300w" sizes="(max-width: 541px) 100vw, 541px" /></p>
<p>Well, at the end of this procedure, it will be more difficult for anyone to know that you are using Tor.</p>
<h2>Let’s Clarify What We Did</h2>
<ul>
<li>First, we discussed what is a Tor bridge and why should it help us remain anonymous. A Tor bridge is an entry node of the Tor network that is not listed in the main Tor directory. While “normal” nodes are publicly available, the bridges are “hidden”, so no one, watching that you are connecting to a certain bridge’s IP, can know that you are using Tor.</li>
<li>What is a pluggable transport? The government can identify that your traffic belongs to the Tor network, blocking it using your ISP. The Tor volunteers then invented pluggable transport, a system that obfuscates your traffic making it similar to an innocuous traffic, making harder, for the government, to decide to block you. Going on with the time, many transports have been identified, so always newly available ones are developed. The current, recommended one, is obfs4, but other types exist. It is also possible to obtain your custom bridges sending an email to <a href="/cdn-cgi/l/email-protection#8be9f9e2efeceef8cbe9f9e2efeceef8a5ffe4f9fbf9e4e1eee8ffa5e4f9ec">this address</a> with the line “get bridges” in the body of the mail. You must send this mail from a Gmail, Yahoo!, or Riseup! Account, because only these providers are supported.</li>
</ul>
</div>
<a href="https://www.deepdotweb.com/tag/configure/" rel="tag">configure</a> <a href="https://www.deepdotweb.com/tag/properly/" rel="tag">properly</a> </span> <span style="display:none" class="updated">2018-02-28<a href="https://www.deepdotweb.com/author/theinnocent/" title="Posts by TheInnocent" rel="author">TheInnocent</a></strong></div>
</div>
</article>

