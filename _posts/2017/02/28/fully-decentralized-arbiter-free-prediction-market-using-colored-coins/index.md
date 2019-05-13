---
A Fully Decentralized, Arbiter-free, Prediction Market Using Colored Coins
---
<article class="post-listing post-18376 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-arbiterfree tag-coins tag-colored tag-decentralized tag-fully tag-market tag-prediction">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>February 28, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/02/28/fully-decentralized-arbiter-free-prediction-market-using-colored-coins/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>A prediction market (PM) is a digital market that enables users to continuously bid on the outcome of future events on the price of various assets. Given the fact that a PM is designed to be transparent and offer real-time price quotes, each user will usually consider the current market status when deciding whether to go long or short for given shares. PMs are also utilized to hedge positions. An individual may bid on a certain outcome, not because he/she is certain of this outcome, but due to the fact that it would affect his/her portfolio negatively. Accordingly, he/she is bidding on the outcome to reduce the risk of losses, even though this outcome anti-correlates with his/her current position. PMs are considered accurate forecasting tools, as research has proven that predictions, made by traders when risking their own money, are more accurate than forecasts provided through technical analyses, polls and other methods.</p>
    <p><img class="wp-image-18383 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/02/prediction-market-png.png" alt="prediction market.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/02/prediction-market-png.png 395w, https://www.deepdotweb.com/wp-content/uploads/2017/02/prediction-market-png-300x287.png 300w" sizes="(max-width: 395px) 100vw, 395px"/></p>
    <p><a href="https://arxiv.org/pdf/1701.08421.pdf">A recently published paper</a> considered a PM that is fully controlled by the market&#8217;s forces. In other words, the rightful outcome of events is determined by the market itself, rather than through a trusted group of arbiters. Such decentralized PM can catalyze bidding on events&#8217; outcomes that can remain unresolved for long time periods. It can also encourage trading operations among users from diverse geo-locations, users for whom anonymity is a priority, and trustless users. The paper illustrates how <a href="https://www.deepdotweb.com/2017/01/18/blockchain-use-cases-trump-shakira/">bitcoin</a> can be utilized to design a fully decentralized PM, via implementing a novel variant of the concept of &#8220;Colored Coins&#8221;.</p>
    <p>The Colored Coins concept allows bitcoin to support not only fungible coins, but also non-fungible assets. Accordingly, &#8220;colored&#8221;, or &#8220;tagged&#8221;, coins can be received and sent on bitcoin&#8217;s network. So, if Adam has a portfolio of <strong>{( 5, red), ( 6, blue)}</strong>, he can use the bitcoin network to send <strong>( 1.9, red)</strong> coins to Judy&#8217;s address and have <strong>{( 3.1, red), ( 6, blue)}</strong> coins remaining.</p>
    <p>The proposed PM system is based on bitcoin, with all assets represented by colored coins according to the following fixed form <strong>( amount, bet, history)</strong>. In the beginning, the system is comprised of uncolored assets according to the following form <strong>(amount, ⊥, ∅)</strong>, which can be used similarly to bitcoins. For instance, if Adam has <strong>( 9, ⊥, ∅)</strong> coins, he can send <strong>( 1.2, ⊥, ∅)</strong> coins to Judy and have <strong>(7.8, ⊥, ∅)</strong> coins remaining.</p>
    <p>To allow participation in the PM in a fully decentralized fashion, the system proposes 3 types of special transactions:</p>
    <p>1- Creation of a prediction pair:</p>
    <p>Any user can execute an outcome-split transaction that transform the asset represented by</p>
    <p><strong>( amount, ⊥, history )</strong></p>
    <p>to</p>
    <p><strong>{( amount, Yes:eid , history), ( amount, No:eid, history)}</strong></p>
    <p><strong>eid</strong> represents a specific event-id that is derived from:</p>
    <p><strong>eid = hash(“Textual description of an event”)</strong></p>
    <p>The <strong>hash()</strong> is assumed to be a cryptographic hash function. These split Yes/No shares can be transacted similarly to Colored Coins. For instance, Adam may split <strong>(m, ⊥, ∅)</strong> using event-id <strong>eid0</strong>, then send <strong>(2/3·m, Yes:eid0, ∅) </strong>shares to Judy, so there will be remaining <strong>{( 1/3·m, Yes:eid0, ∅),(m, No:eid0, ∅)}</strong> shares in his possession.</p>
    <p>2. Redeeming a prediction pair:</p>
    <p>Anyone who owns <strong>(amount, Yes:eid, h<sub>1</sub>) </strong>shares and <strong>(amount, No:eid, h<sub>2</sub>) </strong>shares can execute a special outcome-combine transaction that convert these shares to (<strong>amount, ⊥, h<sub>1</sub> ∪ h<sub>2</sub>)</strong>.</p>
    <p>Accordingly, irrespective of the present value of <strong>(amount, Yes:eid, ∅) </strong>and<strong> (amount, No:eid, ∅) </strong>individually, their combination will always yield a value of <strong>(amount, ⊥, ∅)</strong> ordinary coins.</p>
    <p>3.Forcing an encumbered history:</p>
    <p>Anyone is able to execute a special outcome-force transaction that exchannges his/her r <strong>(amount, Yes:eid, history)</strong> asset to <strong>(amount, ⊥, history ∪ {Yes:eid}).</strong></p>
    <p>As such, anyone can transform his/her <strong>(amount, No:eid, history)</strong> asset to <strong>(amount, ⊥, history ∪ {No:eid})</strong>.</p>
    <p>Classifying all trades using these three transaction types and recording the outcome provides the basis for a fully decentralized prediction market. For example, when the PM operates properly, the price of an asset, <strong>(1, Yes:eid, ∅) </strong>can be estimated via the probability that the market assigns to the event, simply because the cost of a losing share will be approximately zero.</p>
    <p>Finally, it is worth noting that setting up this PM system necessitates forking the bitcoin protocol, because anyone can &#8220;uncolor&#8221; a colored coin via transforming it to bitcoin, which means that colored coins within the bitcoin network are always worth at least as much as their uncolored amount. According to the authors, a fork is crucial to more efficiently support tagging based colored coins and the reference colored coin implementation with the three transaction types of split/combine/encumber to create an ideal PM without arbiters.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/arbiterfree/" rel="tag">arbiterfree</a> <a href="https://www.deepdotweb.com/tag/coins/" rel="tag">coins</a> <a href="https://www.deepdotweb.com/tag/colored/" rel="tag">colored</a> <a href="https://www.deepdotweb.com/tag/decentralized/" rel="tag">decentralized</a> <a href="https://www.deepdotweb.com/tag/fully/" rel="tag">fully</a> <a href="https://www.deepdotweb.com/tag/market/" rel="tag">market</a> <a href="https://www.deepdotweb.com/tag/prediction/" rel="tag">prediction</a></span> <span style="display:none" class="updated">2017-02-28</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

