---
Guest Post: VPN Tor vs Proxy Tor
---
<article class="post-listing post-16122 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-guest tag-post tag-proxy tag-tor tag-vpn">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/admin/" title="">DeepDotWeb </a></span>
    <span>October 28, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/10/28/guest-post-vpn-tor-vs-proxy-tor/#comments">1 Comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p><em>Disclaimer: This is a guest post provided by privatoria.net &#8211; VPN service provider.</em></p>
    <p>The Internet today is huge. It offers many opportunities but also brings certain dangers. That is why need decent protection when we browse the web. The topic is quite popular and there are many options you can try. You can find much information about VPN, Proxy, TOR and other technologies but what does all that mean and which option should you choose. In this article, we will explain popular options in details, namely the trended TOR bundles TOR plus VPN and TOR plus Proxy.</p>
    <p>Architecture</p>
    <p>TOR is quite popular right now and it provides a decent level of protection. However, there are certain risks involved like <a href="https://www.deepdotweb.com/2015/04/26/70-malicious-tor-exit-nodes-exposed-by-siganit-org/">malicious exit nodes</a> .</p>
    <p>There is a remedy. VPN or Proxy may serve as a great addition to TOR but only one of them can secure your traffic from malicious TOR nodes. Let us clarify why is that. The reason for that lies in the difference between VPN and Proxy technologies.</p>
    <p>Security and Privacy</p>
    <p>HTTP Proxy simply changes your IP for web traffic and SOCKS Proxy extends the functionality to work with other traffic (e.g FTP, BitTorrent, etc). Therefore, Proxy offers anonymity but not privacy.</p>
    <p><img class="wp-image-16123 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-20.jpeg" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-20.jpeg 1057w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-20-300x115.jpeg 300w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-20-1024x393.jpeg 1024w" sizes="(max-width: 1057px) 100vw, 1057px"/></p>
    <p>VPN has an option of traffic encryption and DNS leaks protection. In other words, VPN provides both anonymity and privacy. VPN plus takes the concept to a new level and introduces an e<a href="https://www.deepdotweb.com/jolly-rogers-security-guide-for-beginners/combining-tor-with-a-vpn/">xtra security layer</a> .</p>
    <p>This is a DNS leak test result for Privatoria’s VPN TOR service</p>
    <p><img class="wp-image-16124 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-81.png" width="1026" height="564" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-81.png 1920w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-81-300x165.png 300w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-81-1024x563.png 1024w" sizes="(max-width: 1026px) 100vw, 1026px"/></p>
    <p>Set-up process</p>
    <p>There are not so many ways to use TOR together with Proxy and VPN. Proxy is more flexible in this regard as it can be used ensemble with TOR browser or Tails OS. The configuration process is trivial. You simply have to enter web browser’s preferences&gt;advanced&gt;network and enter the settings.</p>
    <p>This is how Privatoria Proxy plus TOR settings look like on a Debian 8 with MATE desktop</p>
    <p><img class="wp-image-16125 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-82.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-82.png 541w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-82-300x215.png 300w" sizes="(max-width: 541px) 100vw, 541px"/></p>
    <p>There are also more advanced configurations that you can try, for example a <a href="http://tor.stackexchange.com/questions/4062/tails-os-configuring-proxychains-for-tor-socks5-proxy">Proxy Chain</a> .</p>
    <p>Unfortunately, VPN cannot be used inside Tails OS. The developers clearly state that on the <a href="https://tails.boum.org/blueprint/vpn_support/">official site</a> . Fortunately, <a href="https://privatoria.net">Privatoria</a> offers a way to use TOR plus VPN. The best, you don’t have to use Tails OS or a web-browser for that. To configure Privatoria’s VPN TOR service on Debian-based systems use regular OpenVPN functionality (you’ll need packages “openvpn” “network-manager-openvpn” and “network-manager-openvpn-gnome” packages for it to work).</p>
    <p>This is how the settings look like on a Debian 8 with MATE desktop</p>
    <p><img class="wp-image-16126 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-83.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-83.png 572w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-83-150x150.png 150w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-83-300x300.png 300w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-83-55x55.png 55w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-83-50x50.png 50w" sizes="(max-width: 572px) 100vw, 572px"/></p>
    <p><img class="wp-image-16127 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-84.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-84.png 509w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-84-300x273.png 300w" sizes="(max-width: 509px) 100vw, 509px"/></p>
    <p><img class="wp-image-16128 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-85.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-85.png 509w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-85-300x273.png 300w" sizes="(max-width: 509px) 100vw, 509px"/></p>
    <p>Speed</p>
    <p>Proxy is an absolute winner in this situation. This is most because your connection only goes through one extra computer and not the whole network. The proxy also does not touch your OS networking infrastructure, unlike VPN. That is why VPN can slow the system down a little. Also, VPN connection speed should be slower compared to VPN due to a longer path that the data has to travel. Add TOR to the mix and what you’ll get is a pretty long distance. Fortunately, with Privatoria Proxy and VPN connection speed does not differ due to service’s specific system architecture.</p>
    <p>Here is the speed test screenshot</p>
    <p><img class="wp-image-16129 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-86.png" width="975" height="536" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-86.png 1920w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-86-300x165.png 300w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-86-1024x563.png 1024w" sizes="(max-width: 975px) 100vw, 975px"/></p>
    <p>Conclusion</p>
    <p>Internet anonymity and privacy tools finally make their way to the mainstream audience. It is important to know the differences between Proxy and VPN and how both interact with the TOR network. The main point to remember is the that Proxy TOR should be used for simpler tasks like watching YouTube while <a href="https://privatoria.net/vpn-tor-2/">VPN TOR</a> is a choice better for sending a personal e-mail.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/guest/" rel="tag">guest</a> <a href="https://www.deepdotweb.com/tag/post/" rel="tag">post</a> <a href="https://www.deepdotweb.com/tag/proxy/" rel="tag">proxy</a> <a href="https://www.deepdotweb.com/tag/tor/" rel="tag">tor</a> <a href="https://www.deepdotweb.com/tag/vpn/" rel="tag">vpn</a></span> <span style="display:none" class="updated">2016-10-28</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/admin/" title="Posts by DeepDotWeb" rel="author">DeepDotWeb</a></strong></div>
    </div>
</article>

