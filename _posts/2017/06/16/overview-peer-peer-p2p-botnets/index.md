---
An Overview of Peer-to-peer (P2P) Botnets
---
<article class="post-listing post-20669 post type-post status-publish format-standard has-post-thumbnail hentry  tag-botnets tag-overview tag-p2p tag-peertopeer">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>June 16, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/06/16/overview-peer-peer-p2p-botnets/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>A <a href="https://www.deepdotweb.com/2017/05/03/botnets-deep-web/">botnet</a> is a network of machines that are infected and controlled by a malicious attacker. Botnets are by far the most serious security threat across the internet today. Even though most botnets rely on a central command and control (C&amp;C) server, <a href="http://cs.ucf.edu/~czou/research/P2PBotnets-bookChapter.pdf">peer-to-peer (P2P) botnets</a> have recently emerged as more dangerous forms of botnets. P2P botnets are more resistant to security defensive measures as they lack C&amp;C servers of conventional botnets.</p>
    <p><strong>Centralized Vs P2P Botnets:</strong></p>
    <p>A botnet is comprised of a network of infected machines (bots) that run malicious software, which has been silently installed via a myriad of techniques including worms, trojan horses and viruses. These compromised machines, or zombie computers, are controlled remotely by the attacker, or the &#8220;botmaster&#8221;. When a botnet is composed of a large number of machines, it has a huge cumulative bandwidth and robust computing capabilities. Botnets are exploited by their botmasters for launching various forms of malicious activities including email spamming, keylogging, password cracking and distributed denial of service (DDoS) attacks.</p>
    <p>Nowadays, centralized botnets are widely used by cybercriminals. Of those are Internet Relay Chat (IRC)-based botnets which are by far the most widely used to promote communications between botnets&#8217; bots and their botmasters. As shown in Figure (1), within a centralized botnet, bots are connected to one or more server to receive commands. This framework is simple to design and very effective in distributing the commands of the botmaster, yet is has a major point of failure; the command and control (C&amp;C) server. If the IRC server is shut down, all bots will lose all communications with their botmaster. Additionally, defenders can monitor a given botnet via creation of a decoy to join its matching IRC channel.</p>
    <p><img class="wp-image-20682 aligncenter" src="/imgs/2017/06/word-image-31.png" /></p>
    <p><strong>Figure (1): Centralized Botnets</strong></p>
    <p>More recently, peer-to-peer (P2P) botnets, e.g. Stormnet and Trojan.Peacomm botnet, have been innovated when attackers realized the limitations of conventional centralized botnets. Similarly to P2P networks, which are compatible with dynamic churn (i.e. peers join and leave the network at a high rate), communication across a P2P botnet won&#8217;t be disrupted if a number of bots lose communication with the botnet . Across a P2P botnet, as shown in figure (2), no centralized server exists and bots communicate with each other in a topological manner and they act both as a client and C&amp;C server. P2P botnets have proven to be far more efficient than conventional centralized botnets. Representing a novel era of botnets, P2P botnets are inarguably more powerful and difficult to counteract by security professionals.</p>
    <p><img class="wp-image-20683 aligncenter" src="/imgs/2017/06/word-image-32.png" srcset="/imgs/2017/06/word-image-32.png 507w, /imgs/2017/06/word-image-32-300x220.png 300w" sizes="(max-width: 507px) 100vw, 507px" /></p>
    <p><strong>Figure (2): Peer-to-peer (P2P) Botnet</strong></p>
    <p>Researchers have recently paid attention to various P2P botnets. <a href="http://www.cs.ucf.edu/~czou/research/P2P-Botnet-ICCCN09.pdf">Stormnet and Trojan.Peacomm botnet were studied extensively</a> as they represent the most commonly encountered P2P botnets. Nevertheless, to effectively counteract these new forms of botnets, analyzing every single P2P botnet available is not enough. Alternatively, P2P botnets have to be systematically studied to defend them properly.</p>
    <p><strong>Peer-to-peer (P2P) Botnet Framework:</strong></p>
    <p>Building a P2P botnet is a process that is comprised of two steps:</p>
    <p>1. The attacker has to infect as many machines as possible across the internet, so that he/she can remotely control them. To accomplish this, all kinds of malware vectors can be used such as viruses, trojan horses, worms and instant message (IM) malware.</p>
    <p>2. The compromised machines will perform specific actions determined by the botmasters. Depending on the target of the attacker, this step could be different with each of attack e.g. DDoS attacks, keylogging, spamming&#8230;etc. Throughout this step, bots act as both clients, performing the actions predefined by the botmaster, and C&amp;C servers that convey communication to other bots.</p>
    <p>There are two ways for new peers to join a P2P network such as that of a P2P botnet:</p>
    <p>1. An initial set of peers are hard coded within each P2P client. When a new peer shows up, it will try to communicate with each peer within that initial set to update information from neighbor peers.</p>
    <p>2. A shared web cache, e.g. Gnutella web cache, that is saved somewhere online, and this location is inserted into the bot&#8217;s code. Accordingly, new peers can update its list of neighbor peers by accessing the web cache and obtaining the latest updates.</p>
    <p>For example, Trojan.Peacomm is a malware that builds a P2P botnet that utilizes the Overnet P2P protocol for C&amp;C communications. The bot&#8217;s code will include a group of Overnet nodes that are most likely to be online. When a machine is infected and the Trojan.Peacomm code is executed, it will try to communicate with the group of peers listed within the bot&#8217;s code. Stormnet, another P2P botnet, uses a similar mechanism; information regarding peers with which newly infected machines communicate after the bot&#8217;s code is executed, is coded within a configuration file that is saved onto the victim&#8217;s machine by the Storm worm.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/botnets/" rel="tag">botnets</a> <a href="https://www.deepdotweb.com/tag/overview/" rel="tag">overview</a> <a href="https://www.deepdotweb.com/tag/p2p/" rel="tag">p2p</a> <a href="https://www.deepdotweb.com/tag/peertopeer/" rel="tag">peertopeer</a></span> <span style="display:none" class="updated">2017-06-16</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

