---
Deadmann : A New Dead Man Switch&#8217;s Network That Utilizes The Tor Network
---
<article class="post-listing post-19723 post type-post status-publish format-standard has-post-thumbnail hentry  tag-dead tag-deadmann tag-man tag-network tag-switchs  tag-utilizes">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>May 9, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/05/09/deadmann-new-dead-man-switchs-network-utilizes-tor-network/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p><a href="https://deadmann.com/docs/deadmann-design.pdf">Deadmann is a newly proposed anonymous network protocol</a> which is comprised of multiple dead man&#8217;s switches that can share data even when a user across the network becomes incapacitated. Previously proposed models of dead man&#8217;s switches failed at achieving the following:</p>
    <ul>
    <li>Preserve users&#8217; anonymity</li>
    <li>Enable users to efficiently manage their own data</li>
    <li>Encrypt users&#8217; data in a manner that can only be decrypted by them</li>
    <li>Interact efficiently with other dead man&#8217;s switches across the network</li>
    </ul>
    <p>Previous dead man&#8217;s switches models were either individualized solutions or based on third party services or centralized servers. The newly proposed Deadmann preserves the anonymity of users via the <a href="https://www.deepdotweb.com/2014/12/02/deep-web-will-continue-grow-part-1/">Tor network</a> and security is furthered even more via data encryption at rest and in transit. Deadmann offers standardized means for anonymously creating a dead man&#8217;s switch and enabling it to anonymously interact with other dead man&#8217;s switches across the network.</p>
    <p><strong>What is a dead man&#8217;s switch?</strong></p>
    <p>Users across a network usually need to share information with other users, even in case of incapacitation. A dead man&#8217;s switch represents a form of a switch that gets activated when the user becomes inactive, so whenever he/she becomes incapacitated, the dead man&#8217;s switch gets activated to share his/her information with others.</p>
    <p><strong>What is Deadmann?</strong></p>
    <p>Deadmann is the name used to refer to a newly proposed network that is comprised of multiple dead man&#8217;s switches that utilizes the Tor network to mask the geo-locations of users, as well as dead man&#8217;s switches. A user can create his/her own dead man&#8217;s switch and use it to communicate with other dead man&#8217;s switches across the network. Whenever a dead man&#8217;s switch gets activated, it will share information owned by the user, with other dead man&#8217;s switches.</p>
    <p>A Deadmann node is a server hosted on the Tor network that communicates with other Deadman nodes. Each Deadmann node represents a Tor hidden service, while the Deadmann ID represents Tor&#8217;s hidden service URL (a base32 encrypted string that is located before the .onion) of the Deadmann node.</p>
    <p>The web interface which is used for initiating, halting, and updating a Deadmann node is known as a Control Hub. Each and every Control Hub is represented by a Tor hidden service that can be accessed via means of the Tor browser. Only the user should know a Control Hub&#8217;s Tor hidden service address.</p>
    <p><strong>Deadmann&#8217;s Design Goals:</strong></p>
    <p>The Deadmann protocol relies on the threat model and was designed to achieve the following goals:</p>
    <ul>
    <li>Insurance of data delivery:</li>
    </ul>
    <p>Delivery of information to its intended receivers should be guaranteed even if the sender becomes inactive for a long period of time, for example, in case of incapacitation or death.</p>
    <ul>
    <li>Anonymity:</li>
    </ul>
    <p>Users should have the ability to host a Deadmann node anonymously via the Tor network.</p>
    <ul>
    <li>Decentralized:</li>
    </ul>
    <p>The decentralized infrastructure of the protocol prevents the occurrence of any single points of failure and offers users better control while managing their data. This can be accomplished via turning all Deadman nodes into Tor hidden services.</p>
    <ul>
    <li>Remote management:</li>
    </ul>
    <p>Users can manage their Deadmann nodes in a secure and anonymous manner remotely.</p>
    <ul>
    <li>Encryption:</li>
    </ul>
    <p>All traffic and data across the network have to be encrypted to offer users high levels of security.</p>
    <ul>
    <li>Plausible deniability:</li>
    </ul>
    <p>Protection of identification information in case of take down of the server, by e.g. a malicious user, hosting the Deadmann node.</p>
    <ul>
    <li>No Javascript:</li>
    </ul>
    <p>Javascript exploits can be utilized to uncover the identity, i.e. geo-location, of users of Tor browsers. A security slider helps users change the level of security provided by the Tor browser. High security level is achieved via disabling Javascript in addition to other features, including SVG images and remote fonts. Deadmann nodes should be managed using this security level on the Tor browser.</p>
    <p><strong>Deadmann&#8217;s Design Model:</strong></p>
    <p>As illustrated in the below figure, Alice, Bob and Carol communicate with their Control Hub using the Tor network via means of the Tor browser, in order to be able to efficiently manage their Deadmann nodes, which can communicate with each other across the Tor network in order to obtain the status of other Deadmann nodes. Users, like Dave, may also be able to obtain Deadmann nodes&#8217; statuses over the Tor browser.</p>
    <p><img class="wp-image-19730 aligncenter" src="/imgs/2017/05/word-image-17.png" srcset="/imgs/2017/05/word-image-17.png 551w, /imgs/2017/05/word-image-17-285x300.png 285w" sizes="(max-width: 551px) 100vw, 551px" /></p>
    <p>When Deadmann is started, a new instance of the Tor browser is initiated and an HTTP server is implemented for the Control Hub. After the Control Hub is successfully accessed, the user can enter his/her authentication code, if one exists. In case an authentication code is not present, the user will have to create a new one, which will be used to encrypt, then decrypt Deadmann files, which are files that include the info needed to administrate a Deadmann node.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/dead/" rel="tag">dead</a> <a href="https://www.deepdotweb.com/tag/deadmann/" rel="tag">deadmann</a> <a href="https://www.deepdotweb.com/tag/man/" rel="tag">man</a> <a href="https://www.deepdotweb.com/tag/network/" rel="tag">network</a> <a href="https://www.deepdotweb.com/tag/switchs/" rel="tag">switchs</a>  <a href="https://www.deepdotweb.com/tag/utilizes/" rel="tag">utilizes</a></span> <span style="display:none" class="updated">2017-05-09</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

