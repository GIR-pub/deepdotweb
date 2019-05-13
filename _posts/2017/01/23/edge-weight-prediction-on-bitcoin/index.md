---
Edge Weight Prediction On Bitcoin And Other Weight Signed Networks WSNs
---
<article class="post-listing post-17664 post type-post status-publish format-standard has-post-thumbnail hentry
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>January 23, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/01/23/edge-weight-prediction-on-bitcoin/#comments">1 Comment</a></span>
    </p>
    <div class="clear"></div>
    
    <p>The bitcoin network is a <a href="https://www.deepdotweb.com/jolly-rogers-security-guide-for-beginners/obtaining-sending-and-receiving-bitcoins-anonymously/">semi-anonymous platform</a> where it is rather difficult to build trust among individuals receiving or sending bitcoin payments across the blockchain. <a href="https://pdfs.semanticscholar.org/29d0/f0556502566f1615ff347b5f568bce46063a.pdf">A group of researchers from University of Maryland experimented using edge weight prediction</a> along a group of models of weighted signed networks WSNs including bitcoin&#8217;s .</p>
    <p>A Weighted signed network WSN is a network where edges, or participants, are marked with positive and/or negative weights. In other words, a WSN can monitor and record like/dislike, trust/distrust and other forms of online social relationships between individuals across the network. The paper addressed the problem of weight prediction of edges across such networks. The researchers proposed two new parameters for node behavior:</p>
    <p>1- The goodness of a node: this parameter reflects how much a node it liked and trusted by other nodes across the network.</p>
    <p>2- The fairness of a node: this parameter reflects how fair is the node in evaluating the trust level and likeability of other nodes across the network.</p>
    <p>The authors of the paper proved that these 2 parameters have to be considered to provide a practical design that wasn&#8217;t fulfilled by previous work involving WSNs. The paper provided a detailed definition of these two parameters and proved that they both converge to yield an ideal solution with a linear time context. The two parameters were utilized to predict the weight of an edge, or <a href="https://www.deepdotweb.com/2013/11/14/down-the-bitcoin-rabbit-hole-is-the-currency-truly-anonymous/">a user in case of a bitcoin exchange, across a WSN</a>. The paper also compared the results of their experiment to various algorithms used in both signed and signed social networks and concluded that &#8220;fairness&#8221; and &#8220;goodness&#8221; parameters, that they defined in their work, yielded the best predictive power.</p>
    <p>They experimented using their proposed metrics with various regression models and showed that they can predict the weight of edges on 2 examples of bitcoin WSNs (bitcoin-OTC and bitcoin-alpha), Wikipedia and Twitter.</p>
    <p><img class="wp-image-17667 aligncenter" src="/imgs/2017/01/weighted-signed-networks-png.png" alt="weighted signed networks.png" srcset="/imgs/2017/01/weighted-signed-networks-png.png 460w, /imgs/2017/01/weighted-signed-networks-png-300x196.png 300w" sizes="(max-width: 460px) 100vw, 460px"/></p>
    <p><strong>Preliminaries of a Weighted Signed Network:</strong></p>
    <p>A weighted signed network WSN represents a directed weighted graph <strong><em>G = (V, E, W) </em></strong>where <strong><em>V</em></strong> is a group of users, <strong><em>E V x V </em></strong> and represent a group of edges, and <strong><em>W : E </em></strong>represents a mapping which assigns a value to each edge between <strong>-1 </strong>and <strong>+1</strong>. <strong><em>W(u,v) </em></strong>is a function that assigns degree of &#8220;likes&#8221;, &#8220;trust&#8221; or &#8220;agrees&#8221; score to describe how mush user <strong><em>v </em></strong>is liked by user <strong><em>u</em></strong>.</p>
    <p>As mentioned that <strong><em>G = (V, E, W) </em></strong>and <strong><em>u</em></strong> is a node across the network. ego-in-network of <strong><em>u</em></strong> is defined as the <strong>WSN ego-in<em>(u) = (V<sub>u</sub>, E<sub>u</sub>, W<sub>u</sub>) </em></strong>where:</p>
    <p><strong><em>V<sub>u</sub> = {u} in(u)</em></strong></p>
    <p><strong><em>E<sub>u</sub> = {(v, u)|v in(u)}</em></strong></p>
    <p><strong><em>W<sub>u</sub>(v, u) = W(u,v), </em></strong>∀<strong><em>(v, u) E<sub>u </sub></em></strong></p>
    <p>According to the aforementioned, two nodes <strong><em>w<sub>1 </sub></em></strong>and <strong><em>w<sub>2</sub> </em></strong>are considered to have identical ego-in-network only if:</p>
    <p><strong><em>|in(w<sub>1</sub>)| = |in(w<sub>2</sub>)|</em></strong></p>
    <p>and there will be a one-to-one mapping function:</p>
    <p><strong><em>h : in(w<sub>1</sub>) in(w<sub>2</sub>) s.t. W<sub>w1 </sub>(v, w<sub>1</sub>) = W<sub>w2</sub> (h(v), w<sub>2</sub>), </em></strong>∀<strong><em>v in(w<sub>1</sub>)</em></strong></p>
    <p>In a similar way, the concept of ego-out-network of a node <strong><em>u</em></strong> can be defined and denoted by the <strong><em>ego-out(u) </em></strong></p>
    <p><strong>The &#8220;Fairness&#8221; and &#8220;Goodness&#8221; Algorithms:</strong></p>
    <p>The researchers developed two parameters; fairness and goodness, to use them to predict the weight of edges across a WSN. The fairness of a vertex represents a parameter that measures the degree of fairness or reliability of a vertex along the process of assigning ratings (agree/disagree, like/dislike, trust/distrust). Accordingly, a fair or reliable rater would give each user the rating he/she really deserves, while an unfair or unreliable user would deviate from the value given by a fair user. Ratings given by unfair users would be marked as of low importance, while fair users&#8217; rating will be the most important. To better illustrate this, in the real context of bitcoin exchanges and similar sites, fraudsters would create multiple accounts to try to increase their own ratings and to manipulate the ratings of honest users; this would be prevented by giving those scammers a low fairness score.</p>
    <p>The goodness of a vertex denotes how much other vertices agree/disagree, like/dislike or trust/distrust this vertex. Having a higher goodness score means that the vertex is more trustworthy across the network. Consequently, a vertex with a high goodness score would receive positive ratings from a fair vertex, while a vertex with a low goodness score would receive negative ratings from a fair vertex.</p>
    </div>
    <span style="display:none" class="updated">2017-01-23</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    
