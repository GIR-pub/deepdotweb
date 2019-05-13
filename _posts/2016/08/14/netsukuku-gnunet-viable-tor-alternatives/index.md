---
Netsukuku and GNUnet: Viable Tor Alternatives?
---
<article class="post-listing post-15100 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-alternatives tag-gnunet tag-netsukuku tag-tor">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/ciphas/" title="">Ciphas </a></span>
    <span>August 14, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/08/14/netsukuku-gnunet-viable-tor-alternatives/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <div class="wp-socializer-buttons clearfix">
    <span class="wpsr-btn">
    
    <div class="fb-like" data-href="https://www.deepdotweb.com/2016/08/14/netsukuku-gnunet-viable-tor-alternatives/" data-share="false" data-layout="button_count" data-show-faces="0" data-action="like" data-colorscheme="light"></div>
    
    </span>
    <span class="wpsr-btn">
    
    <a href="http://twitter.com/share" class="twitter-share-button" data-count="horizontal" data-lang="en" data-url="https://www.deepdotweb.com/2016/08/14/netsukuku-gnunet-viable-tor-alternatives/" data-text="Netsukuku and GNUnet: Viable Tor Alternatives? - "></a>
    
    </span>
    <span class="wpsr-btn">
    
    <div class="g-plusone" data-size="medium" data-href="https://www.deepdotweb.com/2016/08/14/netsukuku-gnunet-viable-tor-alternatives/"></div>
    
    </span>
    <span class="wpsr-btn">
    
    <script type="IN/Share" data-url="https://www.deepdotweb.com/2016/08/14/netsukuku-gnunet-viable-tor-alternatives/" data-counter="right"></script>
    
    </span>
    </div><span class="wpsr_floatbts_anchor" data-offset="25"></span><p>On an earlier Deepdotweb article entitled <a href="https://www.deepdotweb.com/2016/05/09/tor-viable-alternative/">TOR: Is There a Viable Alternative?</a>, I was intrigued by this quote: “The annoying thing about the DarkNet is that there is no “DarkNet”; instead there are DarkNets, all specific to their particular system.”</p>
    <p>Not long after I started to become more familiar with Tor, I wondered what other darknets existed out there, and two that I came across were <a href="http://netsukuku.freaknet.org/">Netsukuku</a> and <a href="http://www.gnunet.org/">GNUnet</a>.  Though they may not be as widely used as Tor, I2P, and Freenet (at present), both sounded promising.</p>
    <p><strong>In with the GNU</strong></p>
    <p>Unrelated to the older P2P protocol Gnutella, GNUnet is an official GNU project, written in C.  Its topology is essentially that of a mesh network (i.e. radio nodes organized in a mesh topology).  It includes a distributed hash table (DHT); in this case, it’s a randomized version of Kademlia intended for small networks.</p>
    <p>As opposed to the clearnet, GNUnet uses Uniform Resource Identifiers (URIs), which have not yet been approved by IANA.</p>
    <p>Unlike Tor, GNUnet cannot be accessed with a browser, because currently, according to <a href="https://www.gnunet.org/faq-page#t33n18">the GNUnet FAQ</a>, there is no proxy (as opposed to Freenet’s fproxy, for example).  GNUnet is a P2P framework, which gives it a number of different capabilities.</p>
    <p>Among these are both anonymous and non-anonymous file sharing, a decentralized and censorship-resistant alternative to DNS, and a system for IPv4-IPv6 protocol translation and tunneling (NAT-PT with DNS-ALG).</p>
    <p>Contrasted with P2P file-sharing networks like BitTorrent and Ares Galaxy, GNUnet was designed with both security and anonymity in mind as top priorities.  In fact, on their main site, at <a href="https://www.gnunet.org/compare">How does GNUnet compare to other filesharing applications?</a>, they offer a chart summing up the differences between their network and other popular ones.</p>
    <p>While the chart is an oversimplified explanation, one characteristic that stands out is in the “anonymity” category.  Of the networks listed (like OneSwarm, Napster, FastTrack, and Freenet), only GNUnet and Freenet feature anonymity.  A second chart explains (in a nutshell) how anonymity is achieved between several different networks (including GNUnet, Tor, and I2P).  As compared to others of its type, GNUnet is a medium-latency network, while Tor, I2P, and Freenet are all low-latency networks.</p>
    <p>Again, these charts don’t really offer a lot of detail; go into the more thorough documentation such as the <a href="https://www.gnunet.org/developer-handbook">developer handbook</a> for that.  Finally, if it’s not enough just to take their word for it – they also have repositories on <a href="https://github.com/GNUnet/gnunet">GitHub</a> and at <a href="https://gnunet.org/svn/">https://gnunet.org/svn/</a>.  The code doesn’t lie…</p>
    <p><strong>Learning to Share</strong></p>
    <p>As stated above, GNUnet’s primary use at present is anonymous file-sharing (also, in a sense, similar to Freenet); users can publish or retrieve information without revealing their identities.  GNUnet’s protocol that allows for such anonymity is called, appropriately, GAP (GNUnet Anonymity Protocol).</p>
    <p>As with I2P, installing GNUnet is a bit more complex than installing and running Tor.  Tor, more or less, can be downloaded and run without much manual configuration.  GNUnet, on the other hand, requires you to install a number of software packages prior to running the program.  These <em>include</em> GNU libmicrohttpd (0.9.30 or higher); GNU libextractor (1.0 or higher); GNU libtool (2.2. or higher); and GNU libunistring (0.9.1.1 or higher).</p>
    <p>If you visit the page at <a href="https://www.gnunet.org/dependencies">https://www.gnunet.org/dependencies</a>, you’ll see a list of all the requirements.  The components can be downloaded from <a href="ftp://ftp.gnu.org/gnu/gnunet/">GNU&#8217;s FTP server</a>.</p>
    <p>Beyond just the file-sharing aspect, users can build sites using the GNU Name System (GNS), which is a secure and decentralized naming system.  It gives users the capability to register names with the .gnu top-level domain (TLD).  For more details on how to configure a GNS site, see <a href="https://www.gnunet.org/gns-setup">Configuring the GNU Name System</a>.</p>
    <p>Now, it’s not worth it to write out <em>all</em> the details here, but if you are truly interested in setting up and using the network, it seems like it would pay off (particularly for developers and hackers).  Are you still skeptical?  Try them out for yourself.</p>
    <p><strong>Netsuku-d’état</strong></p>
    <p>Netsukuku, as described on their homepage, “aims to be a mesh network or a peer to peer protocol that generates and sustains itself autonomously.”  While it may have all the trappings of an A.I., the concept behind it is fascinating.</p>
    <p>Netsukuku is an ad-hoc network designed to handle a substantial number of nodes with the least possible expenditure of CPU and memory resources.</p>
    <p>The creators intend to generate a network that isn’t dependent on authorities like ISPs, multinational corporations, and governments to stay in operation.  In the same vein, they also intend this network to have far greater privacy and anonymity than the current DNS allows.</p>
    <p>In their official FAQ, the creators say they chose the name “Netsukuku” because “Netsukuku sounds like ‘network’ in Japanese, and we like Japanese stuff.  Moreover, when the project started, no results could be found for ‘Netsukuku’ on Google.”  Sounds like a good enough reason, doesn’t it?</p>
    <p>To be clear – Netsukuku isn’t just another P2P network built on top of the Internet (like Tor).  Rather, it’s a physical network, as well as a dynamic routing system intended to handle up to 2^32 nodes without servers or central systems.</p>
    <p>In the words of the creators, Netsukuku might be called a “scalable ad-hoc network architecture for cheap self-configuring Internets.”  This type of architecture allows for the opportunity to build and maintain a network as large as the Internet without any human interference.  (Picture that for a moment).</p>
    <p>Netsukuku makes use of a distance vector routing protocol that is thoroughly integrated into the layers of its hierarchical network topology.  In turn, it requires very little memory or computational resources – its whole network routing table can be stored in a few mere kilobytes.</p>
    <p>Thanks to Netsukuku’s architecture, it’s able to feature several impressive attributes.  According to its documentation: “…a distributed, non-hierarchical, and decentralised system of hostname management; the easy integration of P2P overlay services; an Internet tunneling system that connects nodes which aren’t physically linked; [and] a system which enables full anonymity, hiding the source and destination of packets and encrypting them.”</p>
    <p>It seems to be in somewhat of a beta phase at present, but it can be downloaded and run on Ubuntu and OpenWRT.  Its source code is available at <a href="http://netsukuku.freaknet.org/sourcecode.html">Netsukuku: Source Code</a>.</p>
    <p>By the way, they are looking for developers to help write the Netsukuku software, improve the network, and also expand and translate the documentation.  Does that appeal to you?  Contact them!</p>
    <p><strong>Which Network is Best?</strong></p>
    <p>It’s not really accurate to say that GNUnet and Netsukuku are replacements for Tor, in particular because they’re a <em>little</em> more complex to learn, and they also function very differently.  On the other hand, if they prove to be more secure, and even offer the opportunity for more people to have network access, they’re both valuable tools.</p>
    <p>For those reasons, I recommend them both.  Plus, this isn’t a reason to stop using Tor – it’s just a way to expand your knowledge, and learn new ways to protect your privacy.</p>
    <p>That’s certainly not a bad thing, is it?</p>
    <h3>Share and Enjoy</h3>
    
    <div class="wp-socializer 32px">
    <ul class="wp-socializer-opacity columns-no">
    <li><a href="http://www.facebook.com/share.php?u=https%3A%2F%2Fwww.deepdotweb.com%2F2016%2F08%2F14%2Fnetsukuku-gnunet-viable-tor-alternatives%2F&amp;t=Netsukuku+and+GNUnet%3A+Viable+Tor+Alternatives%3F" title="Share this on Facebook" target="_blank" rel="nofollow"><img src="https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="Facebook" style="width:32px; height:32px; background: transparent url(https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -330px; border:0;"/></a></li>
    <li><a href="http://twitter.com/home?status=Netsukuku+and+GNUnet%3A+Viable+Tor+Alternatives%3F%20-%20https%3A%2F%2Fwww.deepdotweb.com%2F2016%2F08%2F14%2Fnetsukuku-gnunet-viable-tor-alternatives%2F%20" title="Tweet this !" target="_blank" rel="nofollow"><img src="https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="Twitter" style="width:32px; height:32px; background: transparent url(https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -1386px; border:0;"/></a></li>
    <li><a href="http://delicious.com/post?url=https%3A%2F%2Fwww.deepdotweb.com%2F2016%2F08%2F14%2Fnetsukuku-gnunet-viable-tor-alternatives%2F&amp;title=Netsukuku+and+GNUnet%3A+Viable+Tor+Alternatives%3F&amp;notes=On+an+earlier+Deepdotweb+article+entitled+TOR%3A+Is+There+a+Viable+Alternative%3F%2C+I+was+intrigued+by+this+quote%3A+%E2%80%9CThe+annoying+thing+about+the+DarkNet+is+that+there+is+no+%E2%80%9CDarkNet%E2%80%9D%3B+instead+there+are+DarkNets%2C+all+specific+to+their+particular+syst" title="Post this on Delicious" target="_blank" rel="nofollow"><img src="https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="Delicious" style="width:32px; height:32px; background: transparent url(https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -132px; border:0;"/></a></li>
    <li><a href="http://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A%2F%2Fwww.deepdotweb.com%2F2016%2F08%2F14%2Fnetsukuku-gnunet-viable-tor-alternatives%2F&amp;title=Netsukuku+and+GNUnet%3A+Viable+Tor+Alternatives%3F&amp;source=Deep+Dot+Web+-+Surfacing+The+News+From+The+DeepWeb&amp;summary=On+an+earlier+Deepdotweb+article+entitled+TOR%3A+Is+There+a+Viable+Alternative%3F%2C+I+was+intrigued+by+this+quote%3A+%E2%80%9CThe+annoying+thing+about+the+DarkNet+is+that+there+is+no+%E2%80%9CDarkNet%E2%80%9D%3B+instead+there+are+DarkNets%2C+all+specific+to+their+particular+syst" title="Share this on LinkedIn" target="_blank" rel="nofollow"><img src="https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="LinkedIn" style="width:32px; height:32px; background: transparent url(https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -693px; border:0;"/></a></li>
    <li><a href="http://www.stumbleupon.com/submit?url=https%3A%2F%2Fwww.deepdotweb.com%2F2016%2F08%2F14%2Fnetsukuku-gnunet-viable-tor-alternatives%2F&amp;title=Netsukuku+and+GNUnet%3A+Viable+Tor+Alternatives%3F" title="Submit this to StumbleUpon" target="_blank" rel="nofollow"><img src="https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="StumbleUpon" style="width:32px; height:32px; background: transparent url(https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -1287px; border:0;"/></a></li>
    <li><a href="https://www.deepdotweb.com/2016/08/14/netsukuku-gnunet-viable-tor-alternatives/" onclick="addBookmark(event);" title="Add to favorites" target="_blank" rel="nofollow"><img src="https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="Add to favorites" style="width:32px; height:32px; background: transparent url(https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -0px; border:0;"/></a></li>
    <li><a href="/cdn-cgi/l/email-protection#360942590b104543545c5355420b78534245435d435d431d5758521d7178635853421305771d605f57545a531d6259441d775a4253445857425f4053451305701054Xody=On+an+earlier+Deepdotweb+article+entitled+TOR%3A+Is+There+a+Viable+Alternative%3F%2C+I+was+intrigued+by+this+quote%3A+%E2%80%9CThe+annoying+thing+about+the+DarkNet+is+that+there+is+no+%E2%80%9CDarkNet%E2%80%9D%3B+instead+there+are+DarkNets%2C+all+specific+to+their+particular+syst%20-%20https://www.deepdotweb.com/2016/08/14/netsukuku-gnunet-viable-tor-alternatives/" title="Email this" target="_blank" rel="nofollow"><img src="https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="Email" style="width:32px; height:32px; background: transparent url(https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -297px; border:0;"/></a></li>
    <li><a href="https://www.deepdotweb.com/feed/rss/" title="Subscribe to RSS" target="_blank" rel="nofollow"><img src="https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="RSS" style="width:32px; height:32px; background: transparent url(https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -1221px; border:0;"/></a></li>
    </ul>
    <div class="wp-socializer-clearer"></div></div>
    
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/alternatives/" rel="tag">alternatives</a> <a href="https://www.deepdotweb.com/tag/gnunet/" rel="tag">gnunet</a> <a href="https://www.deepdotweb.com/tag/netsukuku/" rel="tag">netsukuku</a> <a href="https://www.deepdotweb.com/tag/tor/" rel="tag">tor</a></span> <span style="display:none" class="updated">2016-08-14</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/ciphas/" title="Posts by Ciphas" rel="author">Ciphas</a></strong></div>
    </div>
</article>

