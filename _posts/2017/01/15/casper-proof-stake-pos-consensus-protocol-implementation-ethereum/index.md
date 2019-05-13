---
CASPER &#8211; Proof of Stake (PoS) Consensus Protocol For Implementation On Ethereum
---
<article class="post-listing post-17536 post type-post status-publish format-standard has-post-thumbnail hentry  tag-casper tag-consensus tag-ethereum tag-implementation tag-pos tag-proof tag-protocol tag-stake">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>January 15, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/01/15/casper-proof-stake-pos-consensus-protocol-implementation-ethereum/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    
    <p>CASPER represents a security deposit protocol that relies on an economic consensus approach. Accordingly, nodes across the network, which are called &#8220;bonded validators&#8221;, must pay a security deposit, along an action named &#8220;bonding&#8221;, in order to be part of the consensus via means of block production. Casper determines the amount of rewards received by the validators mainly through the protocol&#8217;s control over security deposits. Whenever a validator produces a block that is considered &#8220;invalid&#8221; by Casper, his/her security deposit will be forfeited as well as the privilege to participate in the network&#8217;s consensus. Using addresses for security deposits, raises the problem of &#8220;nothing at stake&#8221; which implies that deviating away from the blockchain protocol will more probably put you at a demerit rather than a merit.</p>
    <p><a href="https://arxiv.org/pdf/1612.04518v1.pdf">A group of researchers published a paper</a> that proposed a project that attempted fitting <a href="http://drum.lib.umd.edu/bitstream/handle/1903/18622/Miller_umd_0117E_17522.pdf?sequence=1">Miller&#8217;s definition of provable security</a> into CASPER to implement it on <a href="https://www.deepdotweb.com/2014/08/18/ethereum-making-entire-world-trustless/">Ethereum&#8217;s blockchain</a></p>
    <p><img class="wp-image-17544 aligncenter" src="/imgs/2017/01/pos-png.png" alt="POS.png" srcset="/imgs/2017/01/pos-png.png 256w, /imgs/2017/01/pos-png-150x150.png 150w, /imgs/2017/01/pos-png-55x55.png 55w, /imgs/2017/01/pos-png-50x50.png 50w" sizes="(max-width: 256px) 100vw, 256px"/> .</p>
    <p><strong>Ethereum&#8217;s Scratch Off Puzzles:</strong></p>
    <p>A scratch off puzzle represents a tuple <strong>(d, , t<sub>0</sub>, γ)</strong> and a group of 3 algorithms:</p>
    <p><strong><em>G </em>(1<sup>λ</sup> ) → params </strong></p>
    <p><strong> Work(puz, <em>m</em>) → ticket </strong></p>
    <p><strong> Verify(puz, <em>m</em>, ticket) → {0, 1}</strong></p>
    <p><strong>d</strong> is the mean difficulty, is the amount of work per each puzzle, <strong>t<sub>0</sub></strong> is the algorithm initialization overhead and <strong>γ</strong> represents the amount of adversary advantage over honest workers. For optimum conditions, <strong>γ</strong> has to be kept as close as possible to 1. <strong><em>G</em></strong> initializes all of the public parameters. Work formulates a puzzle instance, <strong>puz</strong>, and a payload, <strong><em>m</em></strong>, to generate a ticket instance, <strong>ticket</strong>. <strong>Verify</strong> will formulate a puzzle instance, a payload and a ticket to generate one of two outputs; 1 or 0.</p>
    <p>A scratch off puzzle has to satisfy the following three requirements:</p>
    <p>1- Correctness:</p>
    <p>For any <strong>(puz, m, ticket), if Work<sub>ticket</sub>(puz, <em>m</em>) ≠⊥ then Verify(ticket, puz, <em>m</em>) = 1</strong></p>
    <p>2- Parallel Feasibility:</p>
    <p>Without much loss, the algorithm representing honest work can be formally represented by:</p>
    <p><img class="wp-image-17545 aligncenter" src="/imgs/2017/01/casper1-png.png" alt="CASPER1.PNG" srcset="/imgs/2017/01/casper1-png.png 511w, /imgs/2017/01/casper1-png-300x64.png 300w" sizes="(max-width: 511px) 100vw, 511px"/></p>
    <p>3- γ-Incompressibility:</p>
    <p>The work needed to solve a given puzzle has to be &#8220;incompressible&#8221;. The best available adversary should not possess the ability to increase the work speed more than by a factor of γ. This can be represented by:</p>
    <p><img class="wp-image-17546 aligncenter" src="/imgs/2017/01/casper2-png.png" alt="CASPER2.PNG" srcset="/imgs/2017/01/casper2-png.png 566w, /imgs/2017/01/casper2-png-300x66.png 300w" sizes="(max-width: 566px) 100vw, 566px"/></p>
    <p>Note that <strong><em>Q</em></strong> represents a transcript of work queries by the Aversary A. The non-malleability property (IND-CCA) is included into this definition. The adversary will be able to observe as many valid puzzles, ticket instances and payloads as he/she wants, but he/she won&#8217;t be able to create his/her own without performing work.</p>
    <p>Accordingly, we can propose the ζ function from the above as:</p>
    <p><img class="wp-image-17547 aligncenter" src="/imgs/2017/01/word-image-68.png" srcset="/imgs/2017/01/word-image-68.png 343w, /imgs/2017/01/word-image-68-300x57.png 300w" sizes="(max-width: 343px) 100vw, 343px"/></p>
    <p><strong>What Is CASPER?</strong></p>
    <p>CASPER is a new proof of stake (PoS) consensus algorithm, which satisfies the requirements of ethereum&#8217;s scratch off puzzle, for implementation on <a href="https://www.deepdotweb.com/2014/08/19/bitcoin-ethereum/">Ethereum&#8217;s blockchain</a>, that is pillared on the following principles:</p>
    <p>1- Security deposits: stakeholders are required to make security deposits behind blocks. Whenever a security deposit is placed behind a block, it can introduced as a transaction that is part of an incompatible block aiming at destroying the security deposit of a validator. A block can be only marked as &#8220;finalized&#8221; when a large number of the network&#8217;s validators place security deposits behind it.</p>
    <p>2- Consensus by bet: Philosophically, the security deposit concept is extended to become a concept of &#8220;bets&#8221;. Within a PoS system, a bet is a transaction which, according to the consensus incentivization rules, will reward you with X coins along every chain that includes a block that you have bet on, in exchange for taking Y coins from you for every chain that doesn&#8217;t include that block. A proper scoring rule should be used to set the values for X and Y. CASPER is based on the principle that validators bet according to the bets of other validators and rational play represents a loop of positive feedback that accelerates consensus. &#8220;Finality&#8221; is determined by 2/3 of validators willing to bet on a block that is large enough so that Y would be equal to their overall deposits.</p>
    <p>3- By-block consensus: it is a yes/no vote casted separately on each block height. The inclusion of a block doesn&#8217;t simply denote inclusion of any block at any given previous heights.</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/casper/" rel="tag">casper</a> <a href="https://www.deepdotweb.com/tag/consensus/" rel="tag">consensus</a> <a href="https://www.deepdotweb.com/tag/ethereum/" rel="tag">Ethereum</a> <a href="https://www.deepdotweb.com/tag/implementation/" rel="tag">implementation</a> <a href="https://www.deepdotweb.com/tag/pos/" rel="tag">pos</a> <a href="https://www.deepdotweb.com/tag/proof/" rel="tag">proof</a> <a href="https://www.deepdotweb.com/tag/protocol/" rel="tag">protocol</a> <a href="https://www.deepdotweb.com/tag/stake/" rel="tag">stake</a></span> <span style="display:none" class="updated">2017-01-15</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

