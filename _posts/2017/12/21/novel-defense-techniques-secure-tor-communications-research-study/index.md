---
Novel Defense Techniques To Secure Tor Communications &#8211; A Research Study
---
<article class="post-listing post-24002 post type-post status-publish format-standard has-post-thumbnail hentry  tag-communications tag-defense tag-research tag-secure tag-study tag-techniques 
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>December 21, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/12/21/novel-defense-techniques-secure-tor-communications-research-study/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>The Tor network depends mainly on resources, which are owned and managed by volunteers, to cater daily for millions of internet users seeking to maintain high levels of anonymity and privacy. As such, these resources have to be efficiently managed, by the Tor network, while also dealing with challenges facing its utility and robustness. A large percentage of the challenges facing Tor emerge from insufficient trust in three main entities:</p>
    <ol>
    <li>Operators of relay nodes whose function is to manages the flow of Tor network traffic through the relay nodes.</li>
    <li>Autonomous Systems (ASes) which own the various networks across which the relay nodes operate.</li>
    <li>Internet users who access the world wide web via means of the Tor network.</li>
    </ol>
    <p>ASes can precisely de-anonymize Tor users as well as the servers they access. On the other hand, adversaries at the network level, such as ASes representing restrictive governments, can markedly decrease network utility via identification and blockage of Tor related traffic. Moreover, some Tor users can sometimes abuse the anonymity offered to them via the network.</p>
    <p><img class="wp-image-24005 aligncenter" src="/imgs/2017/12/word-image-37.jpeg" srcset="/imgs/2017/12/word-image-37.jpeg 660w, /imgs/2017/12/word-image-37-300x169.jpeg 300w" sizes="(max-width: 660px) 100vw, 660px" /></p>
    <p><a href="https://search.proquest.com/openview/1148dde9e391dd5e9c2585f52dc027d0/1?pq-origsite=gscholar&amp;cbl=18750&amp;diss=y">A recently published research study</a> addressed each of the aforementioned threats. Particularly, the study presented:</p>
    <ol>
    <li>Strategies to modify network traffic flows to countermeasure the threats imposed by eavesdropping and relay-level adversaries.</li>
    <li>Relay selection techniques which utilize internet measurement approaches to counteract deanonymization threats imposed by adversaries at network level.</li>
    <li>A covert channel construction scheme that mitigates the threat of blockage by adversaries at the network level via means of reversal of imbalance of resources throughout the arms race between censoring on one side, and circumvention tool developers on the other.</li>
    <li>Measurements that estimate the magnitude of server-side discrimination facing honest Tor users secondary to the dishonest behavior of malicious users across the network.</li>
    </ol>
    <p>Interestingly, this research study presented theoretically derived ideas for maximizing the robustness of any form of network. The suggested approaches for flow modification illustrate how secure means of traffic correlation defense measures can be efficient even in the presence of low bandwidth resources. The relay selection strategies presented via the study demonstrate how to minimize various forms of traffic correlation attacks via utilization of network measurement analysis to bypass adversaries without having to modify the infrastructure of the network. The proposed covert channel scheme demonstrates how wise protocol selection approaches can render communication blockage extremely expensive for censors.</p>
    <p>Let&#8217;s take a look at some of the defenses proposed via this study:</p>
    <p><strong>Website Fingerprinting Defenses:</strong></p>
    <p>The study presented three forms of defenses against website fingerprinting:</p>
    <p>Congestion sensitive BuFlo:</p>
    <p>The study proposed the Congestion Sensitive Buffered Fixed Length Obfuscator (CS-BuFLO) which maximizes the security and performance of known defense technique, the BuFLO. The CS-BuFLO represents a new strategy in fingerprinting defenses. Most of the previously known fingerprinting defenses were formulated to counteract known attacks, and hence adopt black listing to address information leaks; in other words, they act to conceal certain features from attackers including packet sizes. Oppositely, CS-BuFLO adopts a whitelisting defensive approach. The design is based on concealment of traffic flow characteristics and iterative refinement of the design to uncover certain features of traffic flow.</p>
    <p>The Highly secure Glove website fingerprinting defense:</p>
    <p>Glove shows that secure and effective website fingerprinting can be securely achieved. The main idea underlying &#8220;Glove&#8221; is relatively simple; even though webpages usually widely vary in size and structure, protecting a large number of webpages from fingerprinting is possible via categorization of similar webpages into clusters. Consequently, to countermeasure website fingerprinting, one only has to add a small magnitude of cover traffic to categorize all webpages in a cluster that will all seem to be the same webpage to the attacker. Whenever a user loads a webpage while utilizing this defense technique, the attacker will be able to determine the cluster to which that webpage belongs, yet he/she won&#8217;t be able to gain any additional information regarding which specific page within that cluster the user is actually browsing.</p>
    <p><strong>Network Level Correlation Defenses:</strong></p>
    <p>The research study made contribution, regarding network level defenses, in two dimensions. Firstly, via means of a series of simulated and real world experiments, the study quantified the threat imposed by adversaries via Tor traffic correlation at network level. Secondly, the study developed a method for relay selection to counteract such attacks by adversaries at the network level.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/communications/" rel="tag">communications</a> <a href="https://www.deepdotweb.com/tag/defense/" rel="tag">defense</a> <a href="https://www.deepdotweb.com/tag/research/" rel="tag">research</a> <a href="https://www.deepdotweb.com/tag/secure/" rel="tag">secure</a> <a href="https://www.deepdotweb.com/tag/study/" rel="tag">study</a> <a href="https://www.deepdotweb.com/tag/techniques/" rel="tag">techniques</a> <a href="https://www.deepdotweb.com/tag/tor/" rel="tag">tor</a></span> <span style="display:none" class="updated">2017-12-21</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

