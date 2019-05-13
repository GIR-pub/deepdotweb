---
Identity Based Onion Routing &#8211; A Secure and Efficient New Scheme for Tor
---
<article class="post-listing post-19421 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-based tag-efficient tag-identity tag-onion tag-routing tag-scheme tag-secure tag-tor">
    
    <div class="post-inner">
    
    
    <p class="post-meta">
    
    <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    
    
    <span>April 27, 2017</span>
    
    
    <span><a href="https://www.deepdotweb.com/2017/04/27/identity-based-onion-routing-secure-efficient-new-scheme-tor/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    
    <div class="entry">
    
    <p>The onion routing internet protocol promotes anonymous networking on various forms of public networks. Today, the are several onion routing schemes, such as Tor, to deploy the anonymous networking protocol across public networks. Despite the fact that the multi-pass schemes for the construction of the cryptographic circuit are somehow satisfactory, their circuit construction algorithms exhibit some drawbacks when it comes to security and efficiency.</p>
    <p><a href="http://www.ripublication.com/ijaer17/ijaerv12n6_41.pdf">A newly published paper</a> proposed a new identity based onion routing scheme that enables users to communicate with public networks via unique anonymous channels. The newly presented scheme excludes interactive and iterative procedures of symmetric keys, between network users and onion routers, via implementing a circuit construction into the process of non-interactive message delivery. It greatly improves the costs of communication, in terms of computing resources and storage capacity, required from each internet user and the onion router, when compared to the previous protocols of onion routing; thus, offering internet users secure anonymous connection to the internet at competitive computation costs.</p>
    <p><img class="wp-image-19429 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/04/onion-routing-with-identity-png.png" alt="onion routing with identity.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/04/onion-routing-with-identity-png.png 624w, https://www.deepdotweb.com/wp-content/uploads/2017/04/onion-routing-with-identity-png-300x225.png 300w" sizes="(max-width: 624px) 100vw, 624px" /></p>
    <p><strong>Security Analysis of the New Onion Routing Scheme:</strong></p>
    <p>The newly presented scheme makes use of the <a href="https://www.google.com.eg/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;cad=rja&amp;uact=8&amp;ved=0ahUKEwiS1qnEz6TTAhWRL1AKHajdD4cQFggjMAA&amp;url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FBoneh%25E2%2580%2593Franklin_scheme&amp;usg=AFQjCNGZIN-bPzauVr52ipOTtOh-4KjB0w&amp;sig2=zGuBw">Boneh Franklin&#8217;s basic encryption algorithm</a> as the basis for the encryption, which has been proven to be immune against the chosen plaintext attack (IND-CPA). Nevertheless, the security features of the new scheme can be extended to include chosen ciphertext attack (IND-CCA) in an efficient manner via application of a random oracle technique e.g. <a href="https://www.google.com.eg/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;cad=rja&amp;uact=8&amp;ved=0ahUKEwishaKU0KTTAhXIY1AKHQk6AYQQFggjMAA&amp;url=https%3A%2F%2Fwww-old.cs.uni-paderborn.de%2Fuploads%2Ftx_sibibtex%2FBA_Lippert_FOT_final.pdf&amp;usg=AFQjCNHUTm7aRAZHtHrulwY9lHRt">Fujisaki Okamoto transformation</a>.</p>
    <p>The newly proposed scheme promotes integrity and correctness. Additionally, confidentiality is also endorsed via the CPA security that belongs to the primitive identity based encryption algorithm, provided that the BDH problem is hard enough (beyond a specific hardness threshold). The CPA security guarantees that no entity (e.g. an adversary) , except the intended service provider or onion router, can ever decipher the external layer of encryption. When considering an anonymous user, <strong><em>r<sub>i</sub>P </em></strong>represents the sole parameter which is exposed to the onion router <strong><em>O<sub>l</sub> </em></strong> in the circuit, and <strong><em>r<sub>i</sub>P ≠r<sub>j</sub>P </em></strong>for <strong><em>i</em></strong> <strong><em>≠j. </em></strong>This blinds the user&#8217;s identity perfectly and ensures that the user remains anonymous during usage of the protocol.</p>
    <p>Throughout the previous schemes, forward secrecy is successfully achieved on a course grained level. The network&#8217;s protocol periodically changes the keys of all onion routers in an attempt to lessen the exposed period under control of symmetric keys, which is also referred to as the <a href="https://www.deepdotweb.com/2017/01/08/onion-router-darkweb-overview-current-state-vulnerabilities/">&#8220;window of vulnerability&#8221;</a>, to adversaries who have successfully sniffed and undermined any onion router on the network. This will lead to a considerably enormous communication overhead for users to establish communication with onion routers, or KGC, in order to sniff any updated keys. On the other hand, throughout the newly proposed scheme, forward secrecy could be enhanced, oppositely to the past schemes, as a user will not have to establish keys for his/her session with each onion router he/she connects to. This successfully addresses the &#8220;windows of vulnerability&#8221; problem which is prominent in previous schemes.</p>
    <p>The proposed scheme maximizes the security and efficiency of the onion routing protocol via elimination of the requirement of iterative and interactive procedures of symmetric key agreement that takes place between internet users and onion routers. When the essentiality of scalability across large scaled public networks such as the internet is considered, the newly proposed scheme can be utilized as an ideal solution for various forms of anonymous networks.</p>
    <p>The great thing also about the new scheme is that it markedly reduces the computation costs when compared to previous schemes that are also identity based. In the new scheme, a user has to perform only multiplication and pairing operations. Even when the computation overhead of a given users is higher than that of Tor, it is ideally efficient within an identity based cryptographic setting. Furthermore, the computation overhead of a given onion router is by far the least among the schemes. These features denote that the newly proposed scheme can represent an efficient and practical means to permit graceful scaling of anonymity networks.</p>
    
    
    </div><!-- .entry /-->
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/based/" rel="tag">based</a> <a href="https://www.deepdotweb.com/tag/efficient/" rel="tag">efficient</a> <a href="https://www.deepdotweb.com/tag/identity/" rel="tag">identity</a> <a href="https://www.deepdotweb.com/tag/onion/" rel="tag">onion</a> <a href="https://www.deepdotweb.com/tag/routing/" rel="tag">routing</a> <a href="https://www.deepdotweb.com/tag/scheme/" rel="tag">scheme</a> <a href="https://www.deepdotweb.com/tag/secure/" rel="tag">secure</a> <a href="https://www.deepdotweb.com/tag/tor/" rel="tag">tor</a></span>				<span style="display:none" class="updated">2017-04-27</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    
    
    </div><!-- .post-inner -->
</article><!-- .post-listing -->

