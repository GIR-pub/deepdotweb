---
ShadowCash deanonymized?
---
<article class="post-listing post-13221 post type-post status-publish format-standard has-post-thumbnail hentry category-news tag-deanonymized tag-shadowcash">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/fuzzy/" title="">Fuzzy </a></span>
    <span>February 17, 2016</span>
    <span>in <a href="https://www.deepdotweb.com/category/news/" rel="category tag">News</a></span>
    <span><a href="https://www.deepdotweb.com/2016/02/17/shadowcash-deanonymized/#comments">7 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>ShadowCash is a cryptocurrency of the very ambitious Shadow Project which <a href="https://shadowproject.io/en/faq">claims</a> to provide “near-instant, untraceable, unlinkable and trustless transactions”.</p>
    <p>A user that goes by “shnoe” who is a part of the Monero Research Lab, awaits a bounty payment ($1500 according to the bounty <a href="https://shadowproject.io/en/bounties">page</a>) after applying for a bounty for finding a bug that reveals ShadowCash is mathematically broken. Through his detailed <a href="https://shnoe.wordpress.com/2016/02/11/de-anonymizing-shadowcash-and-oz-coin/">blog post</a>, it is shown that an adversary can find out who signed a transaction and thus deanonymize them.</p>
    <p>ShadowCash implemented ring signatures for signature obfuscation, but apparently the implementation was done incorrectly. <a href="https://doc.shadowproject.io/#shadowsend-v2-0">Documentation</a> for the ShadowCore API says that “The ring signatures are a crucial part to anonymize the sender of a transaction.” A proof of concept that exploits this bug, along with a text file of the results of the proof of concept can be found on shnoe&#8217;s Github <a href="https://github.com/ShenNoether/Deanon">repository</a>. This would mean that <strong>all</strong> ShadowCash transactions are <strong>not</strong> really anonymous.</p>
    <p>This is to be expected since ShadowCash hasn&#8217;t been peer reviewed despite having <a href="https://blockchain.info/address/1GGzBQXnouv2LvSvBLcT9vR8CZ3X1sQi6y">raised</a> over 5BTC for it. They have also been <a href="https://bitcointalk.org/index.php?topic=1200091.0">known</a> to censor anyone who speaks negatively about them.</p>
    <p>The Shadow Project denies these deanonymization claims in a <a href="https://blog.shadowproject.io/2016/02/12/deanonymize-shadow-nope/">blog post</a> saying “We would like you -our dedicated users- to know that, after 10+ hours of testing by Shadow’s core developers, our team has not yet managed to deanonymize any private transaction. We will of course keep looking into the claim and come up with a detailed report as soon as possible.”</p>
    <p>The project has written off this bug as FUD (fear, uncertainty, and doubt) and will not be awarding the bounty.</p>
    <p>This disclosure has come under fire because it was done publicly instead of notifying the developers privately, it is speculated that the reasoning for this was because of the implications this bug has and that the users should know about it.</p>
    <p>If there&#8217;s anything to take away from this, it&#8217;s that you should choose what software you use wisely.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/deanonymized/" rel="tag">deanonymized</a> <a href="https://www.deepdotweb.com/tag/shadowcash/" rel="tag">shadowcash</a></span> <span style="display:none" class="updated">2016-02-17</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/fuzzy/" title="Posts by Fuzzy" rel="author">Fuzzy</a></strong></div>
    </div>
</article>

