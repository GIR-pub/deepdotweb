---
What is a User Activated Soft Fork?
---
<article class="post-listing post-19469 post type-post status-publish format-standard has-post-thumbnail hentry  tag-activated tag-fork tag-kptx tag-soft tag-user">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/kptx/" title="">kptx </a></span>
    <span>April 29, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/04/29/user-activated-soft-fork/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>We’re at crosspoint in the Bitcoin journey, where it is up to members of the community to decide what Bitcoin will become and how it will adapt to its growing user base. In the future, we’ll probably look back at this as another page in a long history book and be proud to have been part of this technological revolution.</p>
    <p>Now, however, we have a choice to make as a community and it’s not just up to the miners any more. While the Bitcoin debate is one that has been dependent on miners’ decisions for years, it appears that now users (nodes) will get a say in how Bitcoin will scale due to the prospect of an User Activated Soft Forks (UASF).</p>
    <p>Currently, two popular scaling solutions are competing for miner approval, <a href="https://www.deepdotweb.com/2017/03/21/brief-summary-bitcoin-unlimited/">Bitcoin Unlimited</a> and <a href="https://www.deepdotweb.com/2017/01/29/a-brief-introduction-to-segwit/">SegWit</a>. Both proposals need to reach a predetermined percentage of miner support in order to be activated. SegWit needs 95% and Bitcoin Unlimited needs 75%.</p>
    <p>Although BU is currently the favored choice among miners, there seems to be <a href="https://coin.dance/blocks">no resolution</a> in sight. As so, some are now pushing for the implementation of SegWit through a UASF (<a href="https://github.com/bitcoin/bips/blob/master/bip-0148.mediawiki">BIP 148</a>). But what is a UASF?</p>
    <p><img class="wp-image-19487 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/04/word-image-109.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/04/word-image-109.png 925w, https://www.deepdotweb.com/wp-content/uploads/2017/04/word-image-109-300x44.png 300w" sizes="(max-width: 925px) 100vw, 925px" /></p>
    <p>The User Activated Soft Fork is not about users activating the SegWit soft fork themselves, but rather about pressuring miners to do so. The UASF consists of an update to a Bitcoin client, in this case the Bitcoin Core Client.</p>
    <p>In this update, a time limit is introduced in the form of block height, from which the node stops accepting non-SegWit blocks. What this means is that every node (user) that downloads and runs the Bitcoin Core Client with UASF will not accept blocks that are not signaling SegWit from a certain block height.</p>
    <p>This is a problem for miners, who are not signaling for SegWit activation, since Bitcoin Core nodes make up the grand majority of Bitcoin nodes, <a href="https://coin.dance/nodes/share">roughly 80%</a>. In this case, nodes that did not update to the UASF will continue to accept both kinds which means that SegWit blocks are accepted by all and non-SegWit blocks would be rejected by the majority.</p>
    <p><img class="wp-image-19488 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/04/word-image-110.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/04/word-image-110.png 735w, https://www.deepdotweb.com/wp-content/uploads/2017/04/word-image-110-300x224.png 300w" sizes="(max-width: 735px) 100vw, 735px" /></p>
    <p>The above strategy creates a powerful incentive for miners to switch to SegWit signaling, or better yet, a punishment for those that don’t. The time limit given by the UASF clients create a period in which miners would have to choose between the two updates once and for all.</p>
    <p>If miners decide that they don’t want to upgrade to SegWit, they will mine blocks that are considered valid only to them, and will be left in their own blockchain. The support of exchanges and the majority of nodes for the UASF, means that the coins mined by the miners that create non-SegWit blocks aren&#8217;t worth anything. This also poses a problem for the majority of nodes that stay on the SegWit blockchain, as these will be left with a much weaker network with far less hashing power.</p>
    <p>The idea of this UASF is to “blackmail” miners into signaling SegWit causing the regular activation of the soft fork before UASF needs to kick in. For obvious reasons, this latest move is somewhat controversial and has spawn outrage amongst those that are not in favor of SegWit.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/activated/" rel="tag">activated</a> <a href="https://www.deepdotweb.com/tag/fork/" rel="tag">fork</a> <a href="https://www.deepdotweb.com/tag/kptx/" rel="tag">kptx</a> <a href="https://www.deepdotweb.com/tag/soft/" rel="tag">soft</a> <a href="https://www.deepdotweb.com/tag/user/" rel="tag">user</a></span> <span style="display:none" class="updated">2017-04-29</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/kptx/" title="Posts by kptx" rel="author">kptx</a></strong></div>
    </div>
</article>

