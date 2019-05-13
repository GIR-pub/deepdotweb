---
Byteball: Make DAGs, Not Chains!
---
<article class="post-listing post-16632 post type-post status-publish format-standard has-post-thumbnail hentry  tag-byteball tag-chains tag-dags">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/kptx/" title="">kptx </a></span>
    <span>November 28, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/11/28/byteball-make-dags-not-chains/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    
    <p><a href="https://byteball.org/">Byteball</a> is a decentralized cryptocurrency like none seen before it. It has no blocks, hence no blockchain, hence no block size issue. It relies instead in DAG (Directed Acyclic Graph) to partially organize transactions, which form their own “blocks” called units. These units are limitless, but the fee paid for each transactions ir proportional to their size. &#8211; <a href="https://byteball.org/Byteball.pdf">Read Whitepaper</a></p>
    <p><img class="wp-image-16633 aligncenter" src="/imgs/2016/11/word-image-33.png" srcset="/imgs/2016/11/word-image-33.png 628w, /imgs/2016/11/word-image-33-300x89.png 300w" sizes="(max-width: 628px) 100vw, 628px"/></p>
    <p>Byteball DAG</p>
    <p>The native currency within the Byteball network is called “Byte”. Bytes are the standard form in which value exchanges hands and it’s also used to pay the transaction fees, which are charged by the network on a one-to-one scale, meaning that if a transaction contains 2000 bytes of data, the sender will be required to pay 2000 Bytes (2 KBytes) for said transaction. Fees do not go to Proof of Work miners, however, as there are none. Instead, the fees go to “Witnesses”, who can be anyone in the network that makes a transaction.</p>
    <p>Since transactions are, in a sense, their own blocks, they confirm each other in a chronological order, meaning that new transactions confirm older transactions. When a user creates an outgoing transaction, he is required to choose a list of 12 witnesses. These witnesses can be randomly chosen or they can be selected by the individual on a “popularity basis”. When the witnesses that are selected by the sender post new transactions they are confirming the old transaction that referenced them.</p>
    <p>If users want to be certain that their transactions will be confirmed, the logical thing to do would be to reference witnesses that they know post new transactions regularly. Therefore, Witnesses can campaign for popularity in order to be chosen by users. This helps the witness earn fees and it helps the users that want to get their transactions confirmed.</p>
    <p>Thanks to this system, a Main Chain (MC) is createn within the DAG. The Main Chain will go through the transactions that are authored by well known witnesses. This MC allows a <strong>total </strong>order to be defined between transaction, avoiding double-spends by checking which transactions get included earlier on the Main Chain.</p>
    <p><img class="wp-image-16634 aligncenter" src="/imgs/2016/11/word-image-34.png" srcset="/imgs/2016/11/word-image-34.png 628w, /imgs/2016/11/word-image-34-300x94.png 300w" sizes="(max-width: 628px) 100vw, 628px"/></p>
    <p>Byteball Main Chain (MC)</p>
    <p>Some may be wondering how can Byteball prevent sybil attacks if there is no Proof of Work or Proof of Stake consensus. The sheer complexity of the system acts as protection measure, since it would take an impossible amount of collaboration between all users in the network, most of which will remain anonymous and have an economic incentive to maintain the network honest.</p>
    <p>This system is 100% new and unseen, but it’s more than just a novel piece of technology. This network can potentially solve some of the most pressing issues found in Bitcoin and many other cryptocurrencies, such has the block size dilemma, the energy wasted on PoW mining, and the lack of speed and privacy.</p>
    <p>The privacy features comes in the form of BlackByte, a private asset issued on the Byteball network. When transacting in BlackByte, the plaintext of the transaction (readable format) is not published on the Byteball database and is instead sent directly to the receiver. In order to assure that there is no double-spending going on with BlackBytes, the hash of the transactions and a spendproof are permanently stored. These ensure that the transaction is “honest” but that nothing about it is known. This system has also been previously proposed as an improvement on Bitcoin technology:</p>
    <p><em>“The central idea of the proposed design is to hide the entire inputs and outputs, and publish only the hash of inputs and outputs in the blockchain. The hash can be published as OP_RETURN. The plaintext of inputs and outputs is sent directly to the payee via a private message, and never goes into the blockchain. The payee then calculates the hash and looks it up in the blockchain to verify that the hash was indeed published by the payer.” &#8211; </em><a href="https://bitcointalk.org/index.php?topic=1574508.0"><em>Read more</em></a></p>
    <p>Other features include <a href="https://bitcointalk.org/index.php?topic=1617816.0">smart contracts</a>, multi-signature wallets, encrypted messaging, and even regulated assets.</p>
    <p>Unlike most cryptocurrency projects, Byteball will have no ICO. Instead, 98% the total supply of 10^15 Bytes and BlackBytes will be given to Bitcoin holder for free according to their BTC balance. The other 2% will be kept for a give away campaign and as a reward for the creator of the Byteball protocol.</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/byteball/" rel="tag">byteball</a> <a href="https://www.deepdotweb.com/tag/chains/" rel="tag">chains</a> <a href="https://www.deepdotweb.com/tag/dags/" rel="tag">dags</a></span> <span style="display:none" class="updated">2016-11-28</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/kptx/" title="Posts by kptx" rel="author">kptx</a></strong></div>
    </div>
</article>

