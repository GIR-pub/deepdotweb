---
COMBINING TOR WITH A VPN CONTINUED
---
4007



<p>Ok, now let us talk about why you may want to connect to a VPN over TOR.</p>
<p>The data flow would look like this. You -&gt; Tor -&gt; VPN -&gt; Internet</p>
<p style="text-align: center;"><a href="https://www.deepdotweb.com/vpn-comparison-chart/">&gt;&gt;&gt;Be sure to use a VPN with Tor. Click here to see the best VPN’s&lt;&lt;&lt;</a></p>
<p>The benefits of doing that are as follows. You are more anonymous to your VPN in case they happen to keep logs, or if you do something using the VPN that you are not supposed to and a website or server grabs your VPN IP address. In the case of this happening, even if the VPN manages to keep logs of everything you do, they can only identify you as an anonymous TOR user as long as you did not purchase the service like an idiot with your credit card or Paypal account. If you use Bitcoin, and made sure the the Bitcoin trail is not easily traceable you should be okay. Some websites block TOR users from connecting to their websites or servers, by using your VPN to appear as the exit node, you are hiding your TOR activity from the website you are visiting and hopefully bypassing their filters.</p>
<p>Another advantage, is that if your VPN connection does drop, your fall back will be your TOR IP address instead of your real IP address. And finally, if you are passing through a compromised TOR exit node, your information will remain encrypted through the VPN&#8217;s encryption protocol until it reaches the exit node of the VPN. This is a good thing if you are passing through a compromised exit node, but do not forget that the VPN could be logging everything you are doing anyways. <strong>Do not trust anybody who has access to your unecrypted data!</strong></p>
<p>A few of the downsides of doing things this way, as mentioned in the previous post are that your ISP knows you are using TOR, when and for how long. This may or may not matter to you, but it is just something to consider. Second, you will be unable to visit hidden services websites. Remember those <strong>.onion</strong> sites we talked about in the beginning? You need to be connected to the TOR network to visit those hidden service websites.</p>
<p><strong>But I am connected to TOR aren&#8217;t I?</strong> Yes you are, but your final method of communicating with the internet does not come from the TOR network, it comes from your VPN. And your VPN is likely not configured for TOR. In order for you to be able to connect to a hidden services, you must either be connected directly to TOR, or use a VPN to connect to TOR. TOR must be your final node of connectivity in order to visit onion websites.</p>
<p>The choice is ultimately up to you, and every person in every state, province and country will have different reasons for wanting to do VPN to TOR or TOR to VPN, or just TOR, or just VPN. Whatever choice you make, please keep all the things mentioned in this post and the previous post in mind. None of these methods will save you if you enter anything identifying about yourself online. Do not log into your Facebook account using your VPN. Do not check your email or search a nearby address on Google using your VPN. In fact, stay away from Google altogether unless absolutely necessary.</p>
<p>There are two other search engines out now that do not store information about their users.</p>
<p>#1 &#8211; DuckDuckGo. They have both a clearnet URL and a hidden services URL for both types of users.<br />
https://www.duckduckgo.com<br />
http://3g2upl4pq6kufc4m.onion/ &#8211; Please note the hidden services mirror is not HTTPS</p>
<p>#2 &#8211; StartPage. This server also does not store any information about its users.<br />
https://www.startpage.com</p>
<p>Before we move on, I want to go back to how to choose a good VPN. When looking for a VPN provider, you will most likely come across two protocols to choose from. Find out which one your VPN provider is using before you sign up with them. PPTP and OpenVPN. At this time, I am going to highly recommend that you avoid PPTP and stick with OpenVPN providers. Check out this site for a quick comparison.</p>
<p>http://www.goldenfrog.com/vyprvpn/openvpn-vs-pptp</p>
<p>As you can see, PPTP uses a weaker encryption, 128-bit versus 160-bit to 256-bit for OpenVPN. It offers basic security versus a high level of security using something called digital certificates. This is basically a way to make sure they data coming in is sent from your VPN provider and not injected by some malicious third party because the incoming and outgoing data are signed using specially obtained certificates, similar to showing your ID to get into a a restricted area.</p>
<p>The only downside is that setting up OpenVPN can be a little challenging for the less technical users, but there are plenty of great tutorials online to set up OpenVPN providers and your VPN provider itself will likely help you get set up as well. PPTP has been abandoned by those who demand the highest level of security, so I would recommend to avoid it. A third option for VPN providers is L2TP/IPsec, but many users now believe it has also been compromised by the NSA due to its weaker levels of encryption and should be avoided as well. <strong>Stick with OpenVPN.</strong></p>
<p>Lastly, if you want to know how to connect to TOR over a VPN. If you are using OpenVPN like I recommended, then you it is really quite simple. Make sure you are connected to your VPN, check your IP address to on any website such as <strong>WhatIsMyIpAddress.com</strong> to make sure it has changed. Then, open TOR or open TAILS and start using TOR and you are now connected to TOR over a VPN.</p>
<p>Connecting to a VPN over TOR is a more tricky and currently above my skill set since OpenVPN reconfigures your network routes so Tor can&#8217;t be running on the same host. As soon as I figure it out, I will post a tutorial, and if anybody can share an easy way to connect a VPN over TOR, then please share it with this thread.</p>
<p><strong>UPDATE</strong></p>
<p>A method of connecting to a VPN over TOR has been added to this thread but is currently only able to be used by Windows users. You can read it about it at the link below.</p>
<p><a href="http://www.deepdotweb.com/jolly-rogers-security-guide-for-beginners/connecting-tor-vpn-for-windows-users/"><strong>CONNECTING TOR -&gt; VPN FOR WINDOWS USERS</strong></a></p>


</div><!-- .entry /-->

Updated: 2014-02-12</span>


</div><!-- .post-inner -->
</article><!-- .-->

