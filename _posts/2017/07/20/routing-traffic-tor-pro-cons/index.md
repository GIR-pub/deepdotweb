---
ROUTING ALL TRAFFIC THROUGH TOR: PRO AND CONS
---
<article class="post-listing post-21415 post type-post status-publish format-standard has-post-thumbnail hentry  tag-cons tag-pro tag-routing tag-tor tag-traffic">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/theinnocent/" title="">TheInnocent </a></span>
    <span>July 20, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/07/20/routing-traffic-tor-pro-cons/#comments">5 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Every reader of <a href="https://www.deepdotweb.com">DeepDotWeb</a> knows the importance of surfing the web protected by the Tor network and therefore uses a Tor Browser Bundle. The TBB not only helps us connecting through the Tor network while surfing the internet allowing us to visit onion sites and hiding our ip, but it also uses many security built-in plugins to increase our anonymity (e.g. HTTPS Everywhere, and NoScript). Why not considering the idea of extending the anonymizing features described above to every online action performed on our machine, routing all our traffic through the Tor network?</p>
    <h2>ROUTING ALL TRAFFIC THROUGH TOR: IS IT REALLY THAT GOOD?</h2>
    <p>What we would like to do is force all of our applications to connect through the Tor network to avoid our IP to be revealed when we use our mail client or we download a torrent movie. But is it that simple? The truth is that doing such a thing is highly deprecated by the Tor developers. Using an “all in one solution” which forces all the traffic through Tor in fact, does not prevent the applications to misbehave using unsafe settings or protocols, resulting in IP leaks. A well known example of what I’m saying, is explained clearly by the <a href="https://blog.torproject.org/blog/bittorrent-over-tor-isnt-good-idea">torproject</a> developers in a document regarding Bittorrent. In simple words, what they try to teach us, is that Bittorrent clients like uTorrent, simply ignore the proxy settings when we say them to connect over Tor. In fact Tor supports TCP while a torrent tracker runs over UDP, so it’s impossible for uTorrent to use the proxy settings we specify in this way. The result is an ip leak.</p>
    <p>So while using Bittorrent over Tor is a stupid idea, what about other applications? The answer is that every application behaves in a different manner with different settings, so it is just stupid expecting that every application will do its best to not betray you. Anyway many software products support the usage over Tor like Mozilla Thunderbird that allows you to connect over Tor through the TorBirdy plugin. Read a lot and find the tools that better suit your need of anonymity.</p>
    <p>By the way, if you still want to find a way to “torify” all your traffic, the torproject comes in help with two different approaches:</p>
    <ul>
    <li>Transparently routing traffic through Tor</li>
    <li>Isolating Proxy</li>
    </ul>
    <h2>TRANSPARENTLY ROUTING ALL TRAFFIC THROUGH TOR</h2>
    <p>A proxy is called “transparent” when the clients are not aware of it. Anyway the server knows that the requests come from a proxy. Normally, setting up a SOCKS server is not enough, thus you should configure every application to connect through the proxy but still not all the existing applications allow a connection through SOCKS. Furthermore, if you are the Network Administrator, you could also want the users not to know they’re using such a proxy. These problems can be avoided using a transparent proxy to redirect all the traffic. Tor has a transparent functionality that allows us to use it as a transparent proxy but there are many known issues with <a href="https://lists.torproject.org/pipermail/tor-talk/2013-April/027709.html">leaks</a> of different kinds. The recommended solution is therefore an Isolating Proxy.</p>
    <h2>ISOLATING PROXY: HOW DOES IT WORK?</h2>
    <p>An isolating proxy resolves the problem of transparent leaks implementing security by isolation. This solution requires two physical or virtual machines, one is called “the Gateway” and the other “the Workstation”. The Gateway has only two interfaces, one connected to the clearnet and another connected to the Workstation through a LAN cable. Tor can run on the first interface as well as on the second one. The Workstation is completely isolated and only runs the applications like the Tor Browser Bundle or Hexchat connecting through the SOCKS port towards the Gateway. This system protects you from malwares adding you to a botnet, from DNS leaks and IP leaks.</p>
    <h2>WHONIX</h2>
    <p><img class="wp-image-21419 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/07/word-image-22.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/07/word-image-22.png 800w, https://www.deepdotweb.com/wp-content/uploads/2017/07/word-image-22-300x161.png 300w" sizes="(max-width: 800px) 100vw, 800px" /></p>
    <p><a href="https://www.deepdotweb.com/2014/06/13/simple-whonix-installation-tutorial/">Whonix</a> is the best existing implementation of the isolating proxy concept.</p>
    <p>Whonix is a free Debian-based OS specifically designed to protect your privacy forcing all connections through Tor or blocking them. Whonix is run inside multiple virtual machines and all the applications you need are pre-installed and configured to connect over the Tor network. DNS leaks are impossible as well as IP leaks.</p>
    <p>The SocksPort setup prevents identity correlation by connecting any application to a different Tor SocksPort while normally you would use the same nodes for all the applications used simultaneously.</p>
    <p><img class="wp-image-21420 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/07/word-image-23.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/07/word-image-23.png 500w, https://www.deepdotweb.com/wp-content/uploads/2017/07/word-image-23-232x300.png 232w" sizes="(max-width: 500px) 100vw, 500px" /></p>
    <p>Whonix can be integrated with <a href="https://www.deepdotweb.com/2016/03/12/does-qube-os-has-a-leak-hole/">Qubes OS</a> to make you work in a high-privacy environment but it can cooperate also with Linux, Windows and OS X.</p>
    <p>To conclude, let me say that there are tools out there that promise you to help you route all your traffic through Tor. Built-in tools like these (often developed for Windows systems) ARE NOT RELIABLE, the only trustworthy existing system that allows you to do such a thing is Whonix inside Qubes.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/cons/" rel="tag">cons</a> <a href="https://www.deepdotweb.com/tag/pro/" rel="tag">pro</a> <a href="https://www.deepdotweb.com/tag/routing/" rel="tag">routing</a> <a href="https://www.deepdotweb.com/tag/tor/" rel="tag">tor</a> <a href="https://www.deepdotweb.com/tag/traffic/" rel="tag">traffic</a></span> <span style="display:none" class="updated">2017-07-20</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/theinnocent/" title="Posts by TheInnocent" rel="author">TheInnocent</a></strong></div>
    </div>
</article>

