---
Hybrid Consensus and Fair Proof-of-Work (fPoW)
---
<article class="post-listing post-19135 post type-post status-publish format-standard has-post-thumbnail hentry  tag-consensus tag-fair tag-fpow tag-hybrid tag-proofofwork">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>April 12, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/04/12/hybrid-consensus-fair-proof-work-fpow/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    
    <p>Bitcoin&#8217;s <a href="https://www.deepdotweb.com/2017/03/21/public-consensus-networks-secret-management-access-control-ransomware/">proof-of-work (PoW) distributed consensus</a> has attracted the attention of bitcoin enthusiasts and those who are interested in the blockchain technology in general. Apart from its brilliant decentralization property, it has a critical limitation when efficiency is considered, as transactions cannot be confirmed in a matter of seconds. During 2016, the hybrid consensus approach was proposed to address this issue, at least partly, via introduction of a community whose responsibility is to validate transactions. Nevertheless, there are still some issues related to the hybrid consensus approach including fairness of the process of election of committee members, selfish mining and incentives for the hybrid consensus scheme and others.</p>
    <p>A group of developers recently introduced an alternative to the conventional PoW protocol, which they named fair-proof-of-work (fPoW), to further improve the hybrid consensus approach via addressing issues related to selfish mining and fair election of committee members. <a href="http://eprint.iacr.org/2017/192/20170228:193152">Through their published paper</a>, they also presented the incentives for adopting their improved concept of hybrid consensus. They also utilized this consensus to create privacy preserving constructions, including preserving identity and content, to render the improved consensus more powerful and applicable. The paper also formally proved the security of their proposed hybrid scheme. This new hybrid consensus scheme is expected to be adopted by blockchains that seek high efficiency, decentralization and preservation of privacy of users.</p>
    <p><img class="wp-image-19139 aligncenter" src="/imgs/2017/04/hybrid-jpg.jpeg" alt="hybrid.jpg" srcset="/imgs/2017/04/hybrid-jpg.jpeg 555w, /imgs/2017/04/hybrid-jpg-300x135.jpeg 300w" sizes="(max-width: 555px) 100vw, 555px"/></p>
    <p><strong>An Overview of the Newly Proposed Hybrid Consensus Protocol:</strong></p>
    <p>The team of developers modified <a href="https://www.zurich.ibm.com/dccl/papers/pass_dccl.pdf">the originally proposed hybrid consensus protocol</a>. The following are features of their proposed hybrid consensus protocol:</p>
    <ul>
    <li><strong>Transaction Privacy: </strong>the transactions are solely accessible to the rotating committee members. However committee members cannot see the identity of the sender or receiver of transactions.</li>
    <li><strong>An excellently efficient permissionless model: </strong>the protocol offers a permissionless model that permits nodes to join and leave the network dynamically. Along conventional constructions, a permissionless model is translated into inconvenient efficiency levels when it comes to confirmation of transactions. Nevertheless, when the rotating committee is elected from a snailchain, transactions can be validated via committee members, which maximizes efficiency. Just like the originally described hybrid consensus, this protocol&#8217;s confirmation time is influenced by actual delay, rather than hypothetical upper bound of delay.</li>
    <li><strong>Forking free: </strong>In a conventional blockchain, forking can occur under certain circumstances, yet forking wastes considerable amounts of time and energy, which undermines the fairness of the process of committee election. Users would have to wait for creation of sufficient amount of new blocks for a transaction to be confirmed. Energy consumed by miners who follow a faulty block will be wasted in vain, due to the same reason, fairness is at stake. Moreover, whenever forking exists, selfish mining will exist too. Even though forking is possible in the originally proposed hybrid consensus, forking can be prevented in the newly proposed hybrid consensus protocol .</li>
    <li><strong>Security: </strong>Compared with previous hybrid consensus protocols, the new protocol is characterized by the following security properties:</li>
    </ul>
    <p>1. Tolerated corruption: The new protocol requires approximately 2/3 of all nodes to be honest to achieve a chain quality of 2/3, so as to guarantee that 2/3 of members of the BFT committee are honest.</p>
    <p>2. Loose assumption in response to mildly agile corruption: A hybrid consensus allows an adversary to exhibit mildly agile corruption, i.e. they can select nodes to corrupt as per the environment&#8217;s configuration. τ -agility denotes that an adversary will have to wait for τ amount of time to successfully corrupt an honest node. In the new protocol, τ assumptions are much looser than is the case with previous hybrid consensus protocols.</p>
    <p>3. Prevention of selfish mining.</p>
    <p>4. Prevention of retroactive attacks.</p>
    <ul>
    <li><strong>Fairness in competition: </strong>with the absence of forking, selfish mining is not possible. Moreover, with the newly proposed fPoW, improved fairness levels are guaranteed to committee candidates.</li>
    <li><strong>Arbitrary combination between PoS and PoW:</strong> POA16 is an adaptive version of fPoW which provides means to arbitrarily combine PoS and PoW.</li>
    <li><strong>Chain quality &amp; tolerated corruption: </strong>The new protocol&#8217;s demand for chain quality along with tolerated corruption goes along the same line of the originally described hybrid consensus. Approximately, 2/3 of all nodes have to be honest to achieve a 2/3 chain quality in order to perform PBFT in a safe manner.</li>
    </ul>
    </div>
    <a href="https://www.deepdotweb.com/tag/consensus/" rel="tag">consensus</a> <a href="https://www.deepdotweb.com/tag/fair/" rel="tag">fair</a> <a href="https://www.deepdotweb.com/tag/fpow/" rel="tag">fpow</a> <a href="https://www.deepdotweb.com/tag/hybrid/" rel="tag">hybrid</a> <a href="https://www.deepdotweb.com/tag/proofofwork/" rel="tag">proofofwork</a></span> <span style="display:none" class="updated">2017-04-12</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    
