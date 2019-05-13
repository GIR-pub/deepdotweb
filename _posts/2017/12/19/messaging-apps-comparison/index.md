---
Messaging Apps Comparison
---
<article class="post-listing post-23977 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-apps tag-comparison tag-messaging">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/puppie/" title="">Puppie </a></span>
    <span>December 19, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/12/19/messaging-apps-comparison/#comments">4 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>With the attack on privacy in todays world, having a means of secure messaging is more imperative than ever and within the world of the dark net and drugs this couldn’t be more true. Everyday it feels like big brothers shadowy talons are clawing us in and taking away more of our civil liberties and freedoms but with this has come the need to fight back. Because of this many feel that email is becoming an outdated means of communication with its centralized nature, lack of default encryption, requirement of trust and its bleeding metadata.</p>
    <p>In this article I’ll be exploring some popular email alternatives and how they stack up against each other with the intent of showing you the options you have available as you face this brave new world. It’s important to remember that for a service to be truly useful it must be accessible by everyone and work universally across devices and different OS. Before we continue a few key points.</p>
    <ul>
    <li>PGP encryption is still viable option an can be used with all these services, it should always be used when sending any sensitive content for extra protection.</li>
    <li>Always use Tor or another anonymity service.</li>
    <li>Installing these services on your system for darknet use can open you up to potential compromise, always verify your sources and preferably keep them separate, I would recommend using a dedicated VM.</li>
    </ul>
    <p>I am in no way affiliated with these services and you use them at your own risk, lets begin.</p>
    <p><strong>i2pbote</strong></p>
    <p><a href="https://i2pbote.xyz/">Official Site</a></p>
    <p><strong>Open Source</strong>&#8211; Yes</p>
    <p><strong>Decentralized</strong>&#8211; Yes</p>
    <p><strong>Hidden Metadata</strong>&#8211; Yes</p>
    <p><strong>External Security Audit</strong>&#8211; No</p>
    <p><strong>Message Speed Test</strong>&#8211; 20 minutes</p>
    <p><strong>Forward Secrecy</strong>&#8211; No</p>
    <p><strong>Compatibility</strong>&#8211; Windows, Mac, Linux, Whonix, Qubes, Tails (partial)</p>
    <p>i2pBote is an asynchronous email client operating over the i2p network meaning communications are delayed which can add to your anonymity but can make communications slow and inefficient. These messages are kept in a distributed hash table for 100 days before they are deleted. Since i2pbote operates over the i2p network you will need to install that first, this makes installation on Tails unrecommended and with Whonix and Qubes, more difficult. The installation of i2p can seem daunting but is not out of a noobs grasp with proper research, learn how to install i2p <a href="https://www.deepdotweb.com/2013/12/30/full-guide-how-to-access-i2p-sites-use-themarketplace-i2p/#installation-tails">here</a> and i2pbote <a href="https://www.deepdotweb.com/2016/11/16/noobs-guide-i2p-bote/">here</a>.</p>
    <p>This service is accessible through a webmail client and supports IMAP and SMTP to work with your favorite email client such a Thunderbird. The hidden metadata, decentralized and trustless nature makes this service ideal for our needs and is arguably the strongest in terms of encryption and deniability. The need for i2p makes this service far less desirable for the un-tech savvy user, vendors and market staff. This makes the service unreliable as a means of dark net communication as it will not be adopted by the majority of users.</p>
    <p><strong>Bitmessage</strong></p>
    <p><a href="https://bitmessage.org/wiki/Main_Page">Official Site</a></p>
    <p><strong>Open Source</strong>&#8211; Yes</p>
    <p><strong>Decentralized</strong>&#8211; Yes</p>
    <p><strong>Hidden Metadata</strong>&#8211; Yes</p>
    <p><strong>External Security Audit</strong>&#8211; No</p>
    <p><strong>Message Speed Test-</strong> Instant with fully synced nodes</p>
    <p><strong>Forward Secrecy</strong>&#8211; No</p>
    <p><strong>Compatibility</strong>&#8211; Windows, Mac, Linux, Tails, Whonix, Qubes</p>
    <p>Bitmessage is a trustless, decentralized P2P encrypted messaging platform that works similar to Bitcoin with each message requiring a proof of work. Message and metadata is encrypted and distributed throughout all nodes on the network but only the address the message was intended for can decrypt the received messages. Messages that are sent to an offline node are rebroadcasted every 2 days indefinitely with a decreasing difficulty of work, . There may be some older or low power machines that may have difficulty running Bitmessage due to the CPU work required. Other than that Bitmessage is easy to install on all operating systems with the most common issue being the need for a compiler like g++ to build the C PoW module. The deterministic addresses make regeneration easy and the regeneration password can be kept in a Keepass file for safe keeping. Learn how to install Bitmessage <a href="https://www.deepdotweb.com/2017/03/10/use-bitmessage-encrypted-messaging/">here</a>.</p>
    <p>The strong authentication and encryption plus the trustless, decentralized nature makes Bitmessage a great choice for dark net users. It already has a history of use with vendors like The Grand Wizard and market admins like Hansa, Traderoute the now offline Outlaw Market, this means adoption is already in progress and should flourish as more people become aware and start using the service. All this combined with the ease of installation makes Bitmessage my own personal choice for dark net communications. It also comes with many extra features, such as chans, subscriptions, whitelist/blacklist and email interfacing with <a href="https://bitmessage.ch/">bitmessage.ch</a> that supports IMAP POP3 and SMTP.</p>
    <p><strong>Retroshare</strong></p>
    <p><a href="http://retroshare.net/">Official Site</a></p>
    <p><strong>Open Source</strong>&#8211; Yes</p>
    <p><strong>Decentralized</strong>&#8211; Yes</p>
    <p><strong>Hidden Metadata</strong>&#8211; Yes</p>
    <p><strong>External Security Audit</strong>&#8211; <a href="https://www.elttam.com.au/blog/a-review-of-the-eff-secure-messaging-scorecard-pt1/">Yes</a>, fixed promptly.</p>
    <p><strong>Message Speed Test</strong>&#8211; Instant with online nodes</p>
    <p><strong>Forward Secrecy</strong>&#8211; Yes</p>
    <p><strong>Compatibility</strong>&#8211; Windows, Mac, Linux, Tails (not official but possible), Whonix (incomplete), Qubes (incomplete)</p>
    <p>Retroshare is a decentralized F2F where you make connections directly to the users of your choice which makes spying on communications near impossible. Because of this you’ll need to establish a line of communication with the intended recipient first to ensure you are connecting to each other. Retroshare sends messages directly which means both nodes will need to be online to connect and chat, indirect messaging can be done by both nodes having a common connection in between them to relay the message. It can be run over i2p or Tor; Tor use requires setting up a hidden service which some may find difficult but can be a great learning experience. I personally had no success setting it up in Whonix or Qubes with Tor but had success using it over i2p, you must use an anonymity with Retroshare or else everyone you connect to could see your IP address. Learn how to install Retroshare <a href="http://retroshare.sourceforge.net/wiki/index.php/Documentation:Installation_Guide">here</a>.</p>
    <p>Retroshare offers wide range of services; IM, email, file sharing, VoIP , video calling, forums and channels making it by far the most feature rich anonymous messaging platform available. This wide range of features including the need for direct connections can make Retroshare less desirable for security conscious users as it increases your attack surface and still requires an external means of communication to start off. The lack of complete support for Whonix and Qubes also means many users will be using it with Tails, Windows or Linux on the same machine they do their darknet business on. Even though it offers some of the best protection I wouldn’t recommend Retroshare for our needs as it requires trust between users and faces difficulty in widespread adoption.</p>
    <p><strong>Conclusion</strong></p>
    <p>Choosing software for sensitive tasks is never easy and the best solution for you is a question only you can answer, do your research and see what works for you based on your risk factor. I recommend Bitmessage as it is relatively easy to install across all OS and offers a great balance between protection, deniability and features. A external security audit is still a glaring hole that needs filled, any security researchers reading this should consider getting in touch with these services to help out the community! The lack of forward secrecy is also of concern but as long as your system remains uncompromised you have little worries.</p>
    <p>For my next article I’ll be doing IM software options. Signal, Wire, Wickr, Ricochet, XMPP and maybe others will be compared to find the best one for our needs. If you have any questions, suggestions or comments feel free to leave one down below!</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/apps/" rel="tag">apps</a> <a href="https://www.deepdotweb.com/tag/comparison/" rel="tag">comparison</a> <a href="https://www.deepdotweb.com/tag/messaging/" rel="tag">messaging</a></span> <span style="display:none" class="updated">2017-12-19</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/puppie/" title="Posts by Puppie" rel="author">Puppie</a></strong></div>
    </div>
</article>

