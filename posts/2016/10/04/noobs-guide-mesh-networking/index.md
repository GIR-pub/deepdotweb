---
A Noob&#8217;s Guide to Mesh Networking
---
<article class="post-listing post-15659 post type-post status-publish format-standard has-post-thumbnail hentry category-articles category-deepdot-news tag-guide tag-mesh tag-networking tag-noobs">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/ciphas/" title="">Ciphas </a></span>
    <span>October 4, 2016</span>
    <span>in <a href="https://www.deepdotweb.com/category/articles/" rel="category tag">Articles</a>, <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a></span>
    <span><a href="https://www.deepdotweb.com/2016/10/04/noobs-guide-mesh-networking/#comments">3 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Have you ever seen <a href="https://i.imgur.com/Srbk0.jpg">Shadowmaster’s Web Hierarchy Primer</a>? A Redditor once referred to it as “the REAL guide to the deep web.”</p>
    <p>I mention this because one section of it describes what are called “Private Networks,” and I quote:</p>
    <p><em>These networks do not require Internet access. Examples: PANs (Personal Area Networks), LANs (Local Area Networks),WANs (Wide Area Networks). PANs are very short-range networks, connecting devices with technologies like bluetooth. LANs are short-range networks, connecting devices via routers or Ethernet cables. WANs are broad-range networks, capable of spanning the globe.</em></p>
    <p>So where do open mesh networks fit into all this? A wireless mesh network is created by connecting wireless access points at each user’s location. They would probably be analogous to the Personal Area Networks or Local Area Networks.</p>
    <p><img class="wp-image-15660 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-2.jpeg" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-2.jpeg 751w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-2-300x211.jpeg 300w" sizes="(max-width: 751px) 100vw, 751px" /></p>
    <p>What’s interesting about them is that they could potentially provide competition for the traditional internet infrastructure as we know it – independent of ISPs. I discussed two of these networks in the article <a href="https://www.deepdotweb.com/2016/08/14/netsukuku-gnunet-viable-tor-alternatives/">Netsukuku and GNUnet: Viable Tor Alternatives?</a></p>
    <p>Though those networks are some of the better known mesh protocols, there are <em>over 70</em> competing schemes for routing packets across mesh networks in existence, with more in development – which is why I’ll only elaborate on a few here.</p>
    <p><strong>CCNx</strong></p>
    <p><strong><img class="wp-image-15661 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-3.jpeg" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-3.jpeg 692w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-3-256x300.jpeg 256w" sizes="(max-width: 692px) 100vw, 692px" /></strong></p>
    <p>CCNx was one of the first mesh networks I was able to connect to. In their words, “The vision of Project CCNx® is to develop, promote and evaluate a new approach to a communication architecture we call content-centric networking.”</p>
    <p>Project CCNx is sponsored by the <a href="http://www.parc.com/">Palo Alto Research Center (PARC)</a>. They have created a new networking architecture that they call Content-Centric Networking (CCN). As opposed to IP-based Internet architecture, CCN makes content directly addressable and routable through a name-based system.</p>
    <p>The main principles of the system are:</p>
    <ul>
    <li>Content should be reachable by name, as opposed to a machine address. The process of using names to access information is more efficient than using IP and MAC addresses.</li>
    <li>Content should be safeguarded, instead of the connection (e.g. HTTPS); the data is what’s most important, so that’s what should be defended.</li>
    <li>Computing and memory can be programmed into the network as well, making up a full P2P network.</li>
    </ul>
    <p>To see CCNx’s protocol architecture in more detail, read <a href="http://www.ccnx.org/pubs/CCNxProtocolArchitecture.pdf">CCNx 1.0 Protocol Architecture</a>.</p>
    <p>You may wonder, can I actually connect to this network? Yes, in fact, you can, although like its mesh-routing peers, CCNx requires at least <em>some</em> prior knowledge. The source code is available at <a href="http://www.ccnx.org/releases/distillery-ccnx-absinthe-source-current.tgz">CCNx Sources</a>. PARC encourages developers to experiment with it and create original apps, etc.</p>
    <p>I also found a mobile CCNx relay for Android devices (developed by Razortooth Communications), which you can download at <a href="https://play.google.com/store/apps/details?id=com.rtc.ccnx.droid">CCNx TxRxRelay</a>. I can vouch that it works, although I have yet to connect to any peers. Anybody else want to be my wireless mesh neighbor?</p>
    <p><img class="wp-image-15662 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-4.jpeg" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-4.jpeg 307w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-4-180x300.jpeg 180w" sizes="(max-width: 307px) 100vw, 307px" /></p>
    <p>This is quite a condensement of the material, but some of the links will explain in greater detail. As the network catches on with more people, it’s likely that it will have more functionality.</p>
    <p><strong>Cjdns</strong></p>
    <p><strong><img class="wp-image-15663 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-5.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-5.png 612w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-5-300x228.png 300w" sizes="(max-width: 612px) 100vw, 612px" /></strong></p>
    <p>Cjdns, like CCNx, is a networking protocol. Its creator, Caleb James DeLisle (a.k.a. cjdelisle), wanted to create a network that was simple to set up, but also fast and secure.</p>
    <p>The protocol implements an encrypted IPv6 network. It allocates addresses using public-key cryptography, while using a distributed hash table (DHT) for routing. In this way, it’s very similar to the <a href="https://github.com/irungentoo/toxcore">Tox instant messenger</a>, the <a href="http://www.yacy.net/en/">YaCy search engine</a>, and <a href="https://freenetproject.org/">Freenet</a>.</p>
    <p>Cjdns communicates with other computer programs through a <a href="http://vtun.sourceforge.net/tun/faq.html">TUN device</a>; the computer interprets this as a network interface that would accept IP datagrams.</p>
    <p>You may ask, so, why should I care? Well, if you’re a user of Tor, I2P, or other anonymity networks, then this is right up your alley! Cjdns only allows computers to communicate with one another after they have been verified cryptographically, therefore leaving very little chance for an intruder to spy on their traffic.</p>
    <p>Like Tor’s hidden services, cjdns addresses are generated via a secure hash algorithm. In this case, the addresses are the first 16 bytes (128 bits) of the double <a href="https://en.wikipedia.org/wiki/SHA-2">SHA-512</a> of the public key. It is required, however, that all addresses begin with the byte 0xFC, which is a private address (a.k.a. a unique local address or ULA). Follow so far?</p>
    <p>If not, DeLisle’s <a href="https://github.com/cjdelisle/cjdns">Github repository</a> for cjdns may explain a bit further.</p>
    <p>The main point is that cjdns was designed with security as a top priority, yet it doesn’t have to load slowly either (as is one of the common complaints about the Tor network). I suggest you try it.</p>
    <p>I should also mention that there’s another network by the name of <a href="https://hyperboria.net/">Hyperboria</a> that uses the cjdns routing protocol. Hyperboria is a P2P IPv6 network that features such things as:</p>
    <ul>
    <li>Automatic end-to-end encryption</li>
    <li>Distributed IP address allocation</li>
    <li>DHT-based Source Routing</li>
    </ul>
    <p>Hyperboria’s motto is “The privacy friendly network without borders.” If you have the opportunity to connect to cjdns and like it, then I would further recommend you try out Hyperboria as well.</p>
    <p>Heck, how can you not like a network who took part in the <a href="https://battlemesh.org">Wireless Battle of the Mesh</a>?</p>
    <p><strong>Libre Mesh (LiMe)</strong></p>
    <p><img class="wp-image-15664 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-6.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-6.png 396w, https://www.deepdotweb.com/wp-content/uploads/2016/10/word-image-6-300x162.png 300w" sizes="(max-width: 396px) 100vw, 396px" /></p>
    <p>The Libre Mesh project (LiMe) was started in 2013, by a group of network activists from a number of different countries.</p>
    <p>Like CCNx, the project was founded with several philosophical goals in mind:</p>
    <ul>
    <li>It’s an open network; anyone can connect with the right hardware.</li>
    <li>It’s neutral; there are no restrictions on the type, origin, or destination of the data.</li>
    <li>It’s free, hence the Spanish word “libre”; it has no restrictions.</li>
    </ul>
    <p>The “project” isn’t one piece of hardware or software in and of itself – it consists of the development of several tools. Libre Mesh’s firmware will create the possibility to deploy automatically configurable multi-radio mesh networks.</p>
    <p>The network architecture, as you can see in the above diagram, is based in two layers:</p>
    <ul>
    <li>Cloud Layer 2: this uses the dynamic routing protocol known as BATMAN-ADV. B.A.T.M.A.N. stands for “Better Approach to Mobile Ad-Hoc Networking.” (They have their own site at <a href="https://www.open-mesh.org/projects/open-mesh/wiki">WikiStart &#8211; OpenMesh &#8211; B.A.T.M.A.N.</a>)</li>
    <li>Network Layer 3: this uses, by default, the routing protocol BMX (BatMan-eXperimental). BMX6 (and its latest version, BMX7) is an IPV6 native dynamic routing protocol that boasts advanced features.</li>
    </ul>
    <p>To see more details about how Libre Mesh works, visit <a href="http://libre-mesh.org/howitworks.html">Libre Mesh: Objectives to Achieve.</a> I have yet to actually connect to LiMe, but I’ll leave that up to you, my fellow dark web explorers. You can download the precompiled binaries at <a href="http://downloads.libre-mesh.org/community_chaos/">Index of /community_chaos</a>.</p>
    <p>Let’s not forget – they also have a GitHub repository at <a href="https://github.com/libremesh/">Libre Mesh</a>.</p>
    <p><strong>The Network is Out There…</strong></p>
    <p>Besides the three networks above, there are dozens of other mesh networks that are either active, or being developed. So, if none of those interest you, check out some of these links:</p>
    <p><a href="http://wiki.laptop.org/go/Mesh_Network_Details">OLPC Mesh Network</a></p>
    <p><a href="https://sites.google.com/a/opensailing.net/digitata/">Digitata</a></p>
    <p><a href="http://www.smesh.org/">SMesh</a></p>
    <p><a href="https://www.irif.fr/~jch/software/babel/">Babel</a></p>
    <p><a href="http://owl.eng.mcmaster.ca/~todd/SolarMESH/">SolarMESH</a></p>
    <p><a href="http://ronja.twibright.com/about.php">Ronja</a></p>
    <p>That being said, it looks as though there’s a much larger “<a href="https://www.deepdotweb.com/dark-net-market-comparison-chart/">dark web</a>” than I ever could have imagined. Time to explore, is it not?</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/guide/" rel="tag">guide</a> <a href="https://www.deepdotweb.com/tag/mesh/" rel="tag">mesh</a> <a href="https://www.deepdotweb.com/tag/networking/" rel="tag">networking</a> <a href="https://www.deepdotweb.com/tag/noobs/" rel="tag">noobs</a></span> <span style="display:none" class="updated">2016-10-04</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/ciphas/" title="Posts by Ciphas" rel="author">Ciphas</a></strong></div>
    </div>
</article>

