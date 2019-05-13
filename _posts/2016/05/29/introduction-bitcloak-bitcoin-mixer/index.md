---
Introduction: BitCloak Bitcoin Mixer
---
<article class="post-listing post-14270 post type-post status-publish format-standard has-post-thumbnail hentry  tag-bitcloak tag-bitcoin tag-introduction tag-mixer">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/admin/" title="">DeepDotWeb </a></span>
    <span>May 29, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/05/29/introduction-bitcloak-bitcoin-mixer/#comments">3 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p><em>This is an introduction post about a bitcoin mixing service called BitCloak, the post has been provided by the service admin and is posted as is.</em></p>
    <p>BitCloak is a Bitcoin mixer present only in the darknet as Tor hidden service at the following url: <strong><a href="http://bitcloak43blmhmn.onion" target="_blank">http://bitcloak43blmhmn.onion</a></strong></p>
    <p><a href="/imgs/2016/05/home.jpg"><img class="aligncenter size-full wp-image-14271" src="/imgs/2016/05/home.jpg" alt="home" width="1100" height="935" srcset="/imgs/2016/05/home.jpg 1100w, /imgs/2016/05/home-300x255.jpg 300w, /imgs/2016/05/home-1024x870.jpg 1024w" sizes="(max-width: 1100px) 100vw, 1100px" /></a></p>
    <p>It requires the user to completely disable Javascript in his browser, otherwise it keeps redirecting to an error page. The service fee is randomly set every order in a range around 2%. When requesting mixing BitCloak will generate a PGP signed message containing the order details, this and has 3 purposes:</p>
    <ol>
    <li>It gives the user a verifiable proof that everything is working as expected.</li>
    <li>It gives BitCloak the ability to trust and help the user if he needs help.</li>
    <li>It gives the user a way to not get phished, on a clone website the PGP signed message will be invalid raising a huge red flag.</li>
    </ol>
    <p><a href="/imgs/2016/05/mix.jpg"><img class="aligncenter size-full wp-image-14272" src="/imgs/2016/05/mix.jpg" alt="mix" width="1097" height="939" srcset="/imgs/2016/05/mix.jpg 1097w, /imgs/2016/05/mix-300x257.jpg 300w, /imgs/2016/05/mix-1024x877.jpg 1024w" sizes="(max-width: 1097px) 100vw, 1097px" /></a></p>
    <p>The order details also contain the amounts predictions (send X receive Y), a qr code link as well as the dirty and clean Bitcoin addresses. With a single order a user can clean any amount between 0.028 and 25 btc. It&#8217;s highly suggested to send the same amount set, BitCloak accepts amounts with a maximum difference of 10%.</p>
    <p><a href="/imgs/2016/05/mix1.jpg"><img class="aligncenter size-full wp-image-14273" src="/imgs/2016/05/mix1.jpg" alt="mix1" width="1100" height="937" srcset="/imgs/2016/05/mix1.jpg 1100w, /imgs/2016/05/mix1-300x256.jpg 300w, /imgs/2016/05/mix1-1024x872.jpg 1024w" sizes="(max-width: 1100px) 100vw, 1100px" /></a></p>
    <p>The differences compared to other tumblers/mixers like helix or payshield are many, the amounts prediction, javascript checks and PGP implementation are not present in others. Another big difference is speed, no tumbler currently is this fast when sending clean coins. Like payshield it offers a &#8220;pay someone&#8221; feature for exact amounts payment.</p>
    <p><a href="/imgs/2016/05/mix2.jpg"><img class="aligncenter size-full wp-image-14274" src="/imgs/2016/05/mix2.jpg" alt="mix2" width="1100" height="934" srcset="/imgs/2016/05/mix2.jpg 1100w, /imgs/2016/05/mix2-300x255.jpg 300w, /imgs/2016/05/mix2-1024x869.jpg 1024w" sizes="(max-width: 1100px) 100vw, 1100px" /></a></p>
    <p>The actual Bitcoin tumbling works in such a way that no coins can remain stuck, every couple of minutes a script runs some checks and sends clean coins out as soon as it detects dirty coins with 1 confirmation. Every mixer input address is valid for 12 hours, it can accept multiple transactions and will keep sending clean coins to the address specified. After that the input address gets deleted. Usually the user receives the clean Bitcoins back in 15 minutes.</p>
    <p><a href="/imgs/2016/05/pay.jpg"><img class="aligncenter size-full wp-image-14275" src="/imgs/2016/05/pay.jpg" alt="pay" width="1099" height="937" srcset="/imgs/2016/05/pay.jpg 1099w, /imgs/2016/05/pay-300x256.jpg 300w, /imgs/2016/05/pay-1024x873.jpg 1024w" sizes="(max-width: 1099px) 100vw, 1099px" /></a></p>
    <p>There are two main sections:</p>
    <p><strong>Mix your Bitcoins section:</strong></p>
    <p>This is straight mixing, you decide the Bitcoin address to receive clean coins and the amount to clean. You will get back as clean coins the amount minus fee. The two optional features can be used to split the clean coins to a maximum of 5 Bitcoin  addresses and to set a time delay (1 hour, 12 hours). A random time delay is not present to  avoid the anxiety of not knowing when the clean coins will be sent back.</p>
    <p><a href="/imgs/2016/05/simple1.jpg"><img class="aligncenter size-full wp-image-14276" src="/imgs/2016/05/simple1.jpg" alt="simple1" width="1099" height="932" srcset="/imgs/2016/05/simple1.jpg 1099w, /imgs/2016/05/simple1-300x254.jpg 300w, /imgs/2016/05/simple1-1024x868.jpg 1024w" sizes="(max-width: 1099px) 100vw, 1099px" /></a></p>
    <p><strong>Pay Anonymously section:</strong></p>
    <p>This feature is useful to pay someone with Bitcoin completely anonymously. You first enter the destination Bitcoin address, decide the exact amount of clean coins that  you want to be sent to the destination address and after the order creating you will have  to send that amount plus fee. This section has no optional features such as time delay.In addition BitCloak provides other two small features:</p>
    <p><strong>DnMarket url check:</strong></p>
    <p>A tool you can use when sending Bitcoin to a darknet market. It simply checks against a white list of correct market urls.</p>
    <p><strong>Simple version:</strong></p>
    <p>There&#8217;s also a simpler version of BitCloak, the only difference is the user interface which is flat dark and very minimal.</p>
    <p>The contact section has both an email address to contact the owner of BitCloak and jabber.<br />
    There is also a <a href="https://reddit.com/u/BitCloak">reddit account</a>. The owner said he checks the contact channels at least once a day and he is very open to  help with anything related (how to use PGP, a Bitcoin wallet,..).</p>
    <p><a href="/imgs/2016/05/simple2.jpg"><img class="aligncenter size-full wp-image-14277" src="/imgs/2016/05/simple2.jpg" alt="simple2" width="1096" height="900" srcset="/imgs/2016/05/simple2.jpg 1096w, /imgs/2016/05/simple2-300x246.jpg 300w, /imgs/2016/05/simple2-1024x841.jpg 1024w" sizes="(max-width: 1096px) 100vw, 1096px" /></a></p>
    <p>BitCloak is made with a responsive design that will adapt parts of the page to smaller screens such as smartphones and netbooks. For the mobile users there is also a qr code on the order  screen to quickly get the mixer input address.</p>
    <p>Since the launch date (2 months and half ago) it successfully cleaned Bitcoins more than 820 times without a single issue, in fact there are no negative feedbacks around. The owner says he never had to manually send Bitcoins to a user. The onion website goes to &#8220;maintenance mode&#8221; at least once every 2 weeks for 1-2 hours. The owner says he also wipes the server and re-deploys a fresh copy periodically, which is surely a good thing to do.</p>
    <p><a href="/imgs/2016/05/urlcheck.jpg"><img class="aligncenter size-full wp-image-14278" src="/imgs/2016/05/urlcheck.jpg" alt="urlcheck" width="1100" height="674" srcset="/imgs/2016/05/urlcheck.jpg 1100w, /imgs/2016/05/urlcheck-300x184.jpg 300w, /imgs/2016/05/urlcheck-1024x627.jpg 1024w" sizes="(max-width: 1100px) 100vw, 1100px" /></a></p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/bitcloak/" rel="tag">bitcloak</a> <a href="https://www.deepdotweb.com/tag/bitcoin/" rel="tag">bitcoin</a> <a href="https://www.deepdotweb.com/tag/introduction/" rel="tag">introduction</a> <a href="https://www.deepdotweb.com/tag/mixer/" rel="tag">mixer</a></span> <span style="display:none" class="updated">2016-05-29</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/admin/" title="Posts by DeepDotWeb" rel="author">DeepDotWeb</a></strong></div>
    </div>
</article>

