---
HIDING TOR FROM YOUR ISP &#8211; PART 1 &#8211; BRIDGES AND PLUGGABLE TRANSPORTS
---
4128


<p>This post is going to talk about something that has been commonly discussed on the forums recently. How can I hide my tor usage from my ISP ?</p>
<p>People are more worried about hiding their tor usage from their ISP, than hiding it from a VPN. There seems to be a back and forth debate about whether using a VPN will or will not protect you. Whether or not the VPN can be convinced to log  your connection, and so forth. A few of my previous posts regarding LulzSec and the YardBird pedophile rings have shown that those who rely on VPNs to protect them are historically known to end up in jail. Even our friend we were recently introduced to, The Grugq says, TOR -&gt; VPN is ok, but VPN -&gt; TOR, go to jail.</p>
<p style="text-align: center;"><a href="https://www.deepdotweb.com/vpn-comparison-chart/">&gt;&gt;&gt;Attention: Use VPN with Tor! Click here to see the best VPN’s&lt;&lt;&lt;</a></p>
<p>In my previous posts about VPN -&gt; TOR and TOR -&gt; VPN, I tried to remain neutral in that you should be able to make your own decisions about how you wish to protect yourself. But just remember, at the end of the day, nobody is going to go to jail for you. If you simply want to hide the fact that you are using tor from your ISP, then we have other options than a VPN. We have bridges, and several different pluggable transports. What are these, and how can we use them in Tails?</p>
<div>
<div>Quote</div>
</div>
<blockquote><p><strong>What bridges are and when to use them</strong></p>
<p>When using Tor with Tails in its default configuration, anyone who can observe the traffic of your Internet connection (for example your Internet Service Provider and perhaps your government and law enforcement agencies) can know that you are using Tor.</p>
<p>This may be an issue if you are in a country where the following applies:</p>
<p>1. Using Tor is blocked by censorship: since all connections to the Internet are forced to go through Tor, this would render Tails useless for everything except for working offline on documents, etc.</p>
<p>2. Using Tor is dangerous or considered suspicious: in this case starting Tails in its default configuration might get you into serious trouble.</p>
<p>Tor bridges, also called Tor bridge relays, are alternative entry points to the Tor network that are not all listed publicly. Using a bridge makes it harder, but not impossible, for your Internet Service Provider to know that you are using Tor.</p>
<p>https://tails.boum.org/doc/first_steps/startup_options/bridge_mode/index.en.html</p></blockquote>
<p>The first thing we are going to do is get some bridges. Let us do this before we configure Tails to use bridges, because once Tails is in bridge mode, we will not be able to connect to tor without working bridges. So the first thing we want to do is visit the following webpage.</p>
<p>https://bridges.torproject.org/bridges</p>
<p>Enter the impossibly difficult captcha, and click &#8220;I am human&#8221;, and you should get a list of bridges that look like this. These are actual bridges pulled from the tor bridges page.</p>
<div>
<div>Quote</div>
</div>
<blockquote><p>  5.20.130.121:9001 63dd98cd106a95f707efe538e98e7a6f92d28f94<br />
106.186.19.58:443 649027f9ea9a8e115787425430460386e14e0ffa<br />
69.125.172.116:443 43c3a8e5594d8e62799e96dc137d695ae4bd24b2</p></blockquote>
<p>These bridges are publicly available on the Tor Project website, so they may or not may be the best choice to use, but they are a good start. Another option is to send an email to <strong><a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="2e4c5c474a494b5d6e4c5c474a494b5d005a415c5e5c41444b4d5a00415c49">[email&#160;protected]</a></strong> with a message in the body saying &#8220;get bridges&#8221; without the quotes. This will only work if sent from a Gmail account or Yahoo, unfortunately. If you want to use this, set up the email account using tor and you will receive a list of around 3 bridges shortly thereafter.  Save them somewhere you can use them the next time you boot up Tails, or write them down.</p>
<p>Ok, so now we have our bridges. How do we use bridges in Tails? This is an option we need to activate when we boot up Tails. To activate the bridge mode, we will be adding the <strong>bridge</strong> boot option to the boot menu. The boot menu is the first screen to appear when Tails starts. It is the black screen that says Boot Tails and gives you two options. 1. Live, 2. Live (Fail Safe). When you are on this screen, press Tab and a list of boot options will appear in the form of text at the bottom of the screen. To add a new boot option, add a Space then type &#8220;bridge&#8221; without the quotes and press enter. You have now activated bridge mode.</p>
<p>Once Tails boots up completely, you will get a warning that you have entered bridge mode and not to delete the default IP address in there, which is 127.0.0.1:*. This is advice we will follow, so just click OK and the settings window for tor will pop up. At this point you need to add your bridges. So you are going to take the three bridges you got, and enter the IP address and the port. If we were going to use the example above this is what we would enter.</p>
<div>
<div>Quote</div>
</div>
<blockquote><p>  5.20.130.121:9001<br />
106.186.19.58:443<br />
69.125.172.116:443</p></blockquote>
<p>For each bridge you add, type it in the available text box where it says &#8220;Add A Bridge&#8221; and then click the green + button to add that bridge. You will need to add one bridge at a time. Once you are finished adding your bridges, you can click OK. At this point, your yellow tor onion icon in the top right should turn green shortly after and you will be connected to the tor network using a bridge. Again, since these bridges are less likely to be known by your ISP, they are less likely to know that you are using tor when you use bridges.</p>
<p>You may wish to look up your bridge before you use it however. Maybe you want to find out where your bridge is located, maybe you want to see who is hosting the bridge, and you can do this by looking for a IP look up service online, by doing a search and typing in the IP address. The three listed above are located in the following locations.</p>
<div>
<div>Quote</div>
</div>
<blockquote><p>5.20.130.121 &#8211; Country:   Lithuania<br />
106.186.19.58:443 &#8211; Country: Japan<br />
69.125.172.116:443 &#8211; Country: New Jersey, United States</p></blockquote>
<p>And with that, you can decide which bridge would be a better choice for you to use. I suggest however, that you go and get new bridges and do not use the ones I listed above for obvious reasons that they are now linked to Silk Road users by me posting them on this forum. I should note that the way bridges hide the fact that you are using tor from your ISP, is that you are connected to an IP address that is likely not known to your ISP to be affiliated with tor entry nodes.</p>
<p>While bridges are a good idea, unfortunately they may not be enough. According to Jacob Applebaum, (a tor developer) bridge traffic is still vulnerable to something called DPI (deep packet inspection) to identify internet traffic flows by protocol, in other words they can tell you are using tor by analyzing the traffic. While tor uses bridge relays to get around a censor that blocks by IP address, the censor can use DPI to recognize and filter tor traffic flows even when they connect to unexpected IP addresses. This is less likely to be done by your ISP, and more likely to be done by the NSA, or other oppresive governments like in China and Iran, so you can choose if this is an issue for you.</p>
<div>
<div>Quote</div>
</div>
<blockquote><p>Lately, censors have found ways to block Tor even when clients are using bridges. They usually do this by installing boxes in ISPs that peek at network traffic and detect Tor; when Tor is detected they block the traffic flow.</p>
<p>To circumvent such sophisicated censorship Tor introduced obfuscated bridges. <strong>These bridges use special plugins called pluggable transports which obfuscate the traffic flow of Tor, making its detection harder.</strong></p>
<p>https://www.torproject.org/docs/bridges#PluggableTransports</p></blockquote>
<p>Pluggable transports are a more new, but less talked about technology being implemented by tor to disguise the fact that you are using tor to your ISP and other censors. As mentioned above, it attempts to transform your tor traffic into innocent looking traffic that would hopefully be indistinguishable from normal web browsing traffic. Currently the most popular pluggable transports are obfuscated bridges. Obfuscation by definition, is the hiding of the intended meaning in communication, making communication confusing, wilfully ambiguous, and harder to interpret. Obfuscated bridges actually transform the traffic to look like random packets of data. Obfuscated bridges currently have 2 protocols.</p>
<p><strong>1. obfs2<br />
2. obfs3</strong></p>
<p>Obfs2 (The Twobfuscator) is talked about at length at the following official page.</p>
<p>https://gitweb.torproject.org/pluggable-transports/obfsproxy.git/blob/HEAD:/doc/obfs2/obfs2-protocol-spec.txt</p>
<p>But for the laymans out there, basically obfs2 uses a protocol that disguises your traffic to look like random data, whereas tor has a more distinct structure to it. However, it should be noted in the case of obfs2, that if an attacker sniffs the initial handshake between your computer and the obfuscated bridge, they could get the encryption key used to disguise your traffic and use it to decrypt the disguised traffic which would reveal it as tor traffic. They would not be able to decrypt your tor traffic, but they would be able to see you are using tor. This is not likely something your ISP would do, but it may be something law enforcement or the NSA would do. So if you are only worried about your ISP, then obfs2 would likely suffice.</p>
<p>Obfs3 (The Threebfuscator) is talked about at length at the following official page.</p>
<p>https://gitweb.torproject.org/pluggable-transports/obfsproxy.git/blob/HEAD:/doc/obfs3/obfs3-protocol-spec.txt</p>
<p>Obfs3 uses a very similar protocol to disguise your traffic as obfs2, however it uses a more advanced method of an initial handshake called the Diffie Hellman key exchange. They however found some vulnerabilities in the protocol and had to go a step further and customize the Diffie Hellman key exchange to make it an even more robust method of establishing that initial handshake. Using obfs3 would be a better bet to disguise your traffic if your adversary is the NSA or other law enforcement.</p>
<p>So how do you get these obfuscated bridges? They are not as easy to get, but they can be obtained from tor through email. However, you need to request those bridges specifically to get them. You need to use a Gmail or Yahoo account and send an email to <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="90f2e2f9f4f7f5e3d0f2e2f9f4f7f5e3bee4ffe2e0e2fffaf5f3e4beffe2f7">[email&#160;protected]</a> and enter in the body of the email &#8220;transport obfs2&#8221; without the quotes, and for obfs3, simply enter &#8220;transport obfs3&#8221;. Please note that you can only send one request to tor per email, every 3 hours. Which one you should use, is entirely your choice, I am just giving you the information necessary to make an informed choice. Enter them in this format so that Tails knows which protocol to use.</p>
<p>obfs3 83.212.101.2:42782<br />
obfs2 70.182.182.109:54542</p>
<p>tor also provides a few obfuscated bridges on their home page which you can use as well, and I will list them below. If you send a request to tor and get a response containing bridges without obfs2 or obsf3 at the beginning of the lines, then these are normal bridges, not obfuscated, and they are likely to be out of obfuscated bridges at the moment. You will have to try again another day. So if you get a response with bridges that are without obfs2 or 3 at the beginning of each line, please again, be aware these are normal bridges, unlike the ones below.</p>
<p>obfs3 83.212.101.2:42782<br />
obfs3 83.212.101.2:443<br />
obfs3 169.229.59.74:31493<br />
obfs3 169.229.59.75:46328<br />
obfs3 209.141.36.236:45496<br />
obfs3 208.79.90.242:35658<br />
obfs3 109.105.109.163:38980<br />
obfs3 109.105.109.163:47779<br />
obfs2 83.212.100.216:47870<br />
obfs2 83.212.96.182:46602<br />
obfs2 70.182.182.109:54542<br />
obfs2 128.31.0.34:1051<br />
obfs2 83.212.101.2:45235</p>
<p>I have a feeling that some of you reading this will be inclined to go out and get yourself some obfs3 bridges right away, because you think they are the best choice out there for staying anonymous. And right now they have the potential of being what you hope for in that regard, except for one huge flaw. The number of obfs3 bridges is small. Last report I read put it at around 40 bridges running obfs3, and obfs2 was around 200. So while obfs3 is the most secure option out there, its limited number of available bridges would pool you into a smaller group of people making connections to the 40 available bridges and may not provide any more anonymity for you. tor is in depserate need of more obfs2 and obfs3 bridges at this time and these factors should be taken into account when using obfuscated bridges.</p>
<p>One of the solutions to this shortage problem, is to run your own obfuscated bridge. I am not going to go into it, but if you are interested in doing this, you should visit the following page to set up an obfuscated proxy, or better yet, purchase a few VPS and set them up as obfs2 or obfs3 proxies. One of the best things about doing it this way, is that you can configure it (with the instructions provided) to be a private obfuscated bridge, and therefore tor will not give it out to the public. You can then connect to your own private obfs3 bridge. You can also use a friend&#8217;s computer, or use a server that you know is secure. But again, make sure that you trust the computer you are using, otherwise it is no more secure than a VPN.</p>
<p>Another possible solution to the lack of obfuscated bridges may be another pluggable transport option, something called a <strong>flash proxy</strong>. This is brand new and not perfectly implemented yet, and please be aware that this is basically still in beta. When thinking about a flash proxy, think about the characteristics of a flash, quick and short lived. This protocol was developed by a tor developer who attended Stanford University, and the idea is that the IP addresses used are changed faster than a censoring agency can detect, track, and block them. This method is similar to using normal bridges, in that, it hides the fact you are connecting to IP addresses known to be related to tor, including when the bridge&#8217;s IP addresses listed by tor are discovered by your ISP or law enforcement. <strong>This does not however, hide the fact you are using tor if somebody is analyzing your traffic using DPI (deep packet inspection).</strong></p>
<p>The main benefit to this option is that the proxies are run by many people all over the world. They are run when random internet users visit a webpage with a specific plugin that turns their browser into a proxy as long as they are on that page. You are basically using somebody else&#8217;s connection through their browser to connect to a tor relay. You are only using 1 active connection at any time, but you have around 5 established connections to different proxies in case your active connection drops off, then you can start using another proxy in its place. Below is another explanation of how this process works.</p>
<div>
<div>Quote</div>
</div>
<blockquote><p>In addition to the Tor client and relay, we provide three new pieces. The Tor client contacts the facilitator to advertise that it needs a connection (proxy). The facilitator is responsible for keeping track of clients and proxies, and assigning one to another. The flash proxy polls the facilitator for client registrations, then begins a connection to the client when it gets one. The transport plugins on the client and relay broker the connection between WebSockets and plain TCP. (Diagram below)</p>
<p>https://crypto.stanford.edu/flashproxy/arch.png</p>
<p>A sample session may go like this:</p>
<p>1. The client starts Tor and the client transport plugin program (flashproxy-client), and sends a registration to the facilitator using a secure rendezvous. The client transport plugin begins listening for a remote connection.<br />
2. A flash proxy comes online and polls the facilitator.<br />
3. The facilitator returns a client registration, informing the flash proxy where to connect.<br />
4. The proxy makes an outgoing connection to the client, which is received by the client&#8217;s transport plugin.<br />
5. The proxy makes an outgoing connection to the transport plugin on the Tor relay. The proxy begins sending and receiving data between the client and relay.</p>
<p><strong>In other words, you end up going from your computer, to the proxy, then the proxy to the tor relay. &#8211; JR</strong></p>
<p>The whole reason this is necessary is because the client cannot communicate directly with the relay. (Perhaps the censor has enumerated all the relays and blocked them by IP address.) In the above diagram, there are two arrows that cross the censor boundary; here is why we think they are justified. The initial connection from the client to the facilitator (the client registration) is a very low-bandwidth, write-only communication that ideally may happen only once during a session. A careful, slow, specialized rendezvous protocol can provide this initial communication. The connection from the flash proxy to the client is from an IP address the censor has never seen before. If it is blocked within a few minutes, that&#8217;s fine; it wasn&#8217;t expected to run forever anyway, and there are other proxies lined up and waiting to provide service.</p></blockquote>
<p>I know this might be a bit complicated, but you really do not need to understand how it works to benefit from it. You also might be asking about somebody just blocking your ability to connect with the facilitator (the supplier of the proxies). But, the way you actually connect to the facilitator is in a very special way that tor has designed, and this is built into the flash proxy pluggable transport. This explanation is just for your comfort, not to help you make it work.</p>
<div>
<div>Quote</div>
</div>
<blockquote><p>The way the client registers with the facilitator, is a special rendezvous step that does not communicate directly with the facilitator, designed to be covert and very hard to block. The way this works in practice is that the flash proxy client transport plugin makes a TLS (HTTPS) connection to Gmail, and sends an encrypted email from an anonymous address (<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="046a6b666b607d44686b6765686c6b7770">[email&#160;protected]</a>) to a special facilitator registration address. The facilitator checks this mailbox periodically, decrypts the messages, and inserts the registrations they contain. The result is that anyone who can send email to a Gmail address can do rendezvous, even if the facilitator is blocked.</p>
<p>https://trac.torproject.org/projects/tor/wiki/FlashProxyFAQ</p></blockquote>
<p>Two questions you should be asking. 1) Can I trust the proxies, and/or facilitator? 2) How do I use this?</p>
<p>Well, the facilitator is chosen and currently only run by tor, so you can take that at face value. As far as the proxies go, the proxies themselves may or may not be trustworthy, and this is the risk you run every time you use tor. Your bridges that you use may be compromised, your entry nodes, your exit nodes, every single possible hop along your way to the internet can be compromised at any given time. Luckily, even if the proxy is compromised and logging your traffic, they are only going to be able to see encrypted tor traffic. And as I mentioned above, anybody who visits a webpage with a specific plugin on it, becomes a flash proxy as long as they are on that site. This means, some people will be a flash proxy without their knowledge, and others will be flash proxies because they want to be one. The idea behind this is to have multiple users, tens of thousands, if not hundreds of thousands of flash proxies available at all times to increase the number of possible IP addresses you rotate between to keep your ISP and possibly the NSA guessing.</p>
<p>So do you use this? <strong>It actually currently is not supported in Tails.</strong> But it can be used with Tor Pluggable Transports Tor Browser Bundle outside of Tails. You can get it at the following page and it will run on your normal operating system, whether it is Windows, MAC, or Linux. Get the package at the following page.</p>
<p>https://www.torproject.org/docs/pluggable-transports.html.en#download</p>
<p>Next follow the following tutorial, which is pretty straight forward and has pictures of exactly what you need to do, and will probably do a better job than I would at explaining how to set it up.</p>
<p>https://trac.torproject.org/projects/tor/wiki/FlashProxyHowto</p>
<p>Essentially it comes down to, enable port forwarding for port 9000, add &#8220;bridge flashproxy 0.0.1.0:1&#8221; without the quotes, to your torrc, and leave everything else alone unless you need to use a different port, which is unlikely. You may need to make an exception in your firewall for the flashproxy plugin if it asks you. As long as you are using the Tor Pluggable Transports Tor Browser Bundle, it should be pretty easy to get this feature working. But until Tails adds support for it, this is the only option you have if you want to use flash proxy bridges.</p>
<p>Ok, so you have a lot of information right now and maybe are left a bit confused, but read over this one a few times and try to extract as much out of it as possible at once. Try setting up normal bridges, then try doing the obfuscated bridges, and once you get those working, then maybe consider doing the flash proxies if you are okay without using Tails. Tails will likely implement support for this later. Ask yourself some questions, do I just want to hide the fact that I am using tor from my ISP? Or am I hiding from somebody much bigger than that?</p>
<p>Consider whether it is plausible for you to run a private obfuscated proxy, or even a private bridge. Hopefully now you have enough information to make an informed decision.</p>
<p>Currently there are other pluggable transports currently under developed, but not yet deployed. Here is a list of upcoming projects.</p>
<div>
<div>Quote</div>
</div>
<blockquote><p><strong>ScrambleSuit</strong> is a pluggable transport that protects against follow-up probing attacks and is also capable of changing its network fingerprint (packet length distribution, inter-arrival times, etc.). It&#8217;s part of the Obfsproxy framework. See its official page. Maintained by Philipp Winter.<br />
http://www.cs.kau.se/philwint/scramblesuit/<br />
Status: Undeployed</p>
<p><strong>StegoTorus</strong> is an Obfsproxy fork that extends it to a) split Tor streams across multiple connections to avoid packet size signatures, and b) embed the traffic flows in traces that look like html, javascript, or pdf. See its git repository. Maintained by Zack Weinberg.<br />
https://gitweb.torproject.org/stegotorus.git<br />
Status: Undeployed</p>
<p><strong>SkypeMorph</strong> transforms Tor traffic flows so they look like Skype Video. See its source code and design paper. Maintained by Ian Goldberg.<br />
http://crysp.uwaterloo.ca/software/SkypeMorph-0.5.1.tar.gz<br />
http://cacr.uwaterloo.ca/techreports/2012/cacr2012-08.pdf<br />
Status: Undeployed</p>
<p><strong>Dust</strong> aims to provide a packet-based (rather than connection-based) DPI-resistant protocol. See its git repository. Maintained by Brandon Wiley.<br />
https://github.com/blanu/Dust<br />
Status: Undeployed</p>
<p><strong>Format-Transforming Encryption (FTE)</strong> transforms Tor traffic to arbitrary formats using their language descriptions. See the research paper and web page.<br />
https://eprint.iacr.org/2012/494<br />
https://kpdyer.com/fte/<br />
Status: Undeployed</p>
<p>Also see the unofficial pluggable transports wiki page for more pluggable transport information.<br />
https://trac.torproject.org/projects/tor/wiki/doc/PluggableTransports</p>
<p>Source: https://www.torproject.org/docs/pluggable-transports.html.en</p></blockquote>

Updated: 2014-02-13

