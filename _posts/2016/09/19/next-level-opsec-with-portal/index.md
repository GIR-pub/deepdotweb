---
Next Level OPSEC with PORTAL
---
<article class="post-listing post-15459 post type-post status-publish format-standard has-post-thumbnail hentry category-articles category-deepdot-news tag-level tag-opsec tag-portal">
    
    <div class="post-inner">
    
    
    <p class="post-meta">
    
    <span>Posted by: <a href="https://www.deepdotweb.com/author/jasper/" title="">Jasper </a></span>
    
    
    <span>September 19, 2016</span>
    <span>in <a href="https://www.deepdotweb.com/category/articles/" rel="category tag">Articles</a>, <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a></span>
    
    <span><a href="https://www.deepdotweb.com/2016/09/19/next-level-opsec-with-portal/#comments">1 Comment</a></span>
    </p>
    <div class="clear"></div>
    
    <div class="entry">
    
    <p>PORTAL is the “Personal Onion Router To Assure Liberty”. Despite it being highly beneficial to OPSEC and it requiring just an old Raspberry Pi, it&#8217;s not that talked about.</p>
    <p>With just one script, you can turn any old Raspberry Pi into a router specifically for the Tor network, meaning that when you&#8217;re connected to it, it will always send all of your traffic through Tor. The Raspberry Pi is a great option but it&#8217;s not the only one; You can do the same to any router with enough memory and space to install and run Tor, though that can be an issue which requires after-market hardware mods to achieve. PORTAL was created in 2012 by <a href="https://twitter.com/thegrugq">TheGrugq</a> and its goal is to have you fail closed, which is the ability to fail safely behind the PORTAL, giving up no trace of your real IP. To achieve this, the PORTAL project creates a hardware separation between your computer and your WAN connection, and as a result your workstation simply doesn&#8217;t know what&#8217;s beyond your PORTAL. Your workstation cannot give up your real IP because it simply doesn&#8217;t know it.</p>
    <p><b>Protection from Exploits</b></p>
    <p>PORTAL sets out to ensure that all of your traffic is transparently sent over Tor with the goal of removing your ability fall victim to exploits like those seen used on Flash, Firefox and JavaScript, which exposed the targets&#8217; real IPs by having their workstation make a request to a remote server, outside of their Tor connection, which would log the IP which made the request and any other identifying information the request may have contained. For example, in the FBI&#8217;s attack on Freedom Hosting, a JavaScript exploit was used to cause users of various dark net websites, who had not disabled JavaScript, send specific information about the computer being used via a request to an FBI-owned server.</p>
    <p>“<i>Briefly, this payload connects to 65.222.202.54:80 and sends it an HTTP request that includes the host name (via gethostname()) and the MAC address of the local host (via calling SendARP on gethostbyname()-&gt;h_addr_list). After that it cleans up the state and appears to deliberately crash.” &#8211; </i>Vlad Tsyrklevich</p>
    <p>While PORTAL leaves the task of obfuscating your hostname and MAC address to you, it would have meant a Tor exit node querying that FBI server rather than your home IP address. Your MAC address and username <i>might</i> be enough to get you busted, but it&#8217;s much less likely when they&#8217;re not paired with your home IP.</p>
    <p><b>Protection from Yourself</b></p>
    <p>Aside from exploits, there have been notable cases such as the one of LulzSec, specifically Sabu, where his real identity was revealed by merely forgetting to use Tor just one time when he was connecting to a public IRC channel in which there were agents watching. As a result, he was arrested and made to decide that his best option was to turn into a rat for the FBI, which ultimately helped bring down the rest of his team, LulzSec. Logging into any nefarious accounts even once without Tor is enough to get you busted.</p>
    <p><b>Why not a VPN too?</b></p>
    <p>To further improve the usefulness and anonymity of your new PORTAL setup, you can easily pair it with a VPN. There&#8217;s an added freedom of being able to chain VPNs together with Tor, so that even if Tor itself is exploited, it would only reveal your VPN&#8217;s IP, which you would be connecting to via another instance of Tor. For example, if you were to run a VPN on your workstation computer, your connection would look like this:</p>
    <p>WAN → [PORTAL] → Tor → [Workstation] → VPN → [Tor Browser] → Tor → deepdot35wvmeyd5.onion</p>
    <p>However, this addition is not foolproof and may cause more harm than good if you allow the VPN to be connected to your person in any way. Paying with a method which isn&#8217;t associated with your person and using Tor when you purchase, as well as always using Tor to connect to the VPN should be enough to keep you separated.</p>
    <p><b>Pairing with 3g</b></p>
    <p>TheGrugq, in the talk that&#8217;s embedded here, mentions that it&#8217;s possible to connect your PORTAL to a 3g connection using a 3g dongle. Even if its IP is somehow given up, they can be purchased anonymously and aren&#8217;t effectively tracked. Your connection would look like this:</p>
    [3g Dongle] → WAN → [PORTAL] → Tor → [Workstation] → VPN → [Tor Browser] → Tor → deepdot35wvmeyd5.onion</p>
    <p><b>Why not Tails?</b></p>
    <p>The Tails project essentially has a PORTAL built into the operating system. It&#8217;s a workstation OS with IPTABLES rules which attempts to have you route all of your traffic through Tor, but you have to trust the OS and all the applications on it to not give up your real IP. It&#8217;s great, but without the separation from your WAN connection that an external gateway gives, your OS knows that IP &#8211; It has to, else it wouldn’t be able to connect you to the internet.</p>
    <p><i>Can I pair TailsOS and PORTAL?</i></p>
    <p>Yes, but you shouldn&#8217;t. Your setup would look like this:</p>
    <p>WAN → [PORTAL] → Tor → [TAILS OS] → Tor → deepdot35wvmeyd5.onion</p>
    <p>Connecting to Tor over Tor is probably a bad idea. According to the Tor Project team, it&#8217;s not received significant testing yet.</p>
    <p>“<i>When using a transparent proxy, it is possible to start a Tor session from the client as well as from the transparent proxy, creating a &#8220;Tor over Tor&#8221; scenario. Doing so produces undefined and potentially unsafe behavior. In theory, however, you can get six hops instead of three, but it is not guaranteed that you&#8217;ll get three different hops &#8211; you could end up with the same hops, maybe in reverse or mixed order. It is not clear if this is safe. It has never been discussed.” &#8211; <a href="https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#ToroverTor">Source</a>.</i></p>
    <p><b>Why not Whonix? </b></p>
    <p>With <a href="https://www.deepdotweb.com/2014/06/13/simple-whonix-installation-tutorial/">Whonix</a>, you can use applications and run servers anonymously over the internet. DNS leaks are impossible, and not even malware with root privileges can find out the user&#8217;s real IP. Like PORTAL, there&#8217;s a gateway that creates an isolated network for a workstation, only with Whonix it&#8217;s achieved with virtual machines rather than hardware. If your home OS is compromised, so are your virtual machines. Whonix is a lot better than just Tor browser on Linux, and probably better than Tails because of the improved isolation of the workstation from the knowledge of your WAN IP.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2016/09/Whonix_concept_refined1.jpg"><img class="aligncenter size-full wp-image-15460" src="https://www.deepdotweb.com/wp-content/uploads/2016/09/Whonix_concept_refined1.jpg" alt="whonix_concept_refined1" width="799" height="430" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/09/Whonix_concept_refined1.jpg 799w, https://www.deepdotweb.com/wp-content/uploads/2016/09/Whonix_concept_refined1-300x161.jpg 300w" sizes="(max-width: 799px) 100vw, 799px" /></a></p>
    <p>Why not both? Well, why not? With Whonix on your workstation you could easily have a setup that looks like this:</p>
    <p>WAN → [PORTAL] → Tor → [Workstation] → <a href="https://www.deepdotweb.com/vpn-comparison-chart/">VPN</a> → [Whonix Gateway] → Tor → [Whonix Workstation] → VPN → [Tor Browser] -&gt; Tor → deepdot35wvmeyd5.onion</p>
    <p><b>What NOT to do with PORTAL</b></p>
    <p>Using PORTAL isn&#8217;t necessarily good for OPSEC because every tool can be used improperly. For example, if you connect your normal workstation to it, you&#8217;ll likely be telling several services your Tor IP. Every account you sign in to or are already signed into will now know which Tor exit node you&#8217;re using and at specifically what time, making correlation attacks likely. For further reading, Whonix&#8217;s wiki is a great resource for learning what&#8217;s not good to do with your new <a href="https://www.whonix.org/wiki/DoNot">isolated workstation</a>. <a href="https://www.torproject.org/download/download.html.en#warning">There&#8217;s also</a>.</p>
    
    
    </div><!-- .entry /-->
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/level/" rel="tag">level</a> <a href="https://www.deepdotweb.com/tag/opsec/" rel="tag">opsec</a> <a href="https://www.deepdotweb.com/tag/portal/" rel="tag">portal</a></span>				<span style="display:none" class="updated">2016-09-19</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/jasper/" title="Posts by Jasper" rel="author">Jasper</a></strong></div>
    
    
    </div><!-- .post-inner -->
</article><!-- .post-listing -->

