---
Two New Models For Double Spending Attacks On Bitcoin&#8217;s Blockchain
---
<article class="post-listing post-17242 post type-post status-publish format-standard has-post-thumbnail hentry  tag-attacks tag-bitcoins tag-blockchain tag-double tag-models tag-spending">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>December 31, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/12/31/two-new-models-double-spending-attacks-bitcoins-blockchain/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p><a href="https://www.deepdotweb.com/2016/10/06/cryptocurrency-hacks-biggest-heists-blockchain-history/">Counterfeiting a digital signature on bitcoin&#8217;s blockchain</a> is a significantly hard task to execute successfully in terms of processing power. Accordingly, it is almost impossible to change a bitcoin transaction that has been already been signed. Nevertheless, it is still possible to alter the state of a valid transaction via a technique known as &#8220;double spend attack&#8221; that requires enormous processing power.</p>
    <p><img class="wp-image-17250 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2016/12/double-spend-cartoon-jpg.jpeg" alt="double spend cartoon.jpg" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/12/double-spend-cartoon-jpg.jpeg 638w, https://www.deepdotweb.com/wp-content/uploads/2016/12/double-spend-cartoon-jpg-300x225.jpeg 300w" sizes="(max-width: 638px) 100vw, 638px"/></p>
    <p>Here are the elements of a successful double spend attack:</p>
    <p>1- The person performing the double spend attack <em>A </em>seeks a product or a service from another person <em>B</em></p>
    <p>2- <em>A </em>will create two bitcoin transactions; one that include payments for the product or service he seeks from <em>B</em> and the other pays the same amount to himself/herself.</p>
    <p>3- <em>A </em>will broadcast the &#8220;<em>A </em>to <em>B&#8221; </em>transaction and then start secretly mining the block that includes the &#8220;<em>A </em>to <em>A&#8221; </em>payment. Once he/she successfully mines this block, further blocks will be added to it.</p>
    <p>4- <em>B </em>will give the service or product to <em>A</em>, on seeing the transaction on the <a href="https://www.deepdotweb.com/2015/10/12/we-love-the-blockchain-not-the-bitcoin-the-currency/">public ledger</a>, whether or not the transaction was confirmed, if he/she doesn&#8217;t wait for the confirmation to send the products.</p>
    <p>5- <em>A </em>can be lucky and the attack succeeds , if the fraudulent branch grows longer than the branch that includes the valid transaction when the nodes set up by the attackers broadcast all newly formed blocks to the new branch and all other nodes on the network agree on considering the valid branch the one that includes the fraudulent transaction.</p>
    <p><img class="wp-image-17251 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2016/12/double-spend-png.png" alt="double spend.PNG" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/12/double-spend-png.png 483w, https://www.deepdotweb.com/wp-content/uploads/2016/12/double-spend-png-300x221.png 300w" sizes="(max-width: 483px) 100vw, 483px"/></p>
    <p>Figure 1: Elements of a Successful Double Spend Attack</p>
    <p><strong>Two Classic Double Spend Attack Models:</strong></p>
    <p>Before delving into the new models, we will shortly outline the basic elements of the classic attack models. There were 2 double spend attack models proposed by S. Nakamoto and M.Rosenfeld. To better understand the models, we shall set the following parameters:</p>
    <p>&#8211; Quantity <em>q </em>∈ [0,1] represents the probability of success of attackers&#8217; nodes to mine a block before the honest nodes given that they both started mining at the same time.</p>
    <p>&#8211; Quantity <em>K </em>∈ N represents a threshold of the number of confirmations needed to validate transactions belonging to a certain block.</p>
    <p>&#8211; Quantity <em>T </em>∈ R<sub>&gt;0 </sub> represents the time in seconds needed by the mining nodes, both the attacker&#8217;s and the honest ones, to successfully mine a block.</p>
    <p>&#8211; Also, we will use an <em>N </em>subscript to point out functions used exclusively in S. Nakamoto&#8217;s model and an <em>R </em>subscript to point out functions used exclusively in M. Rosenfeld&#8217;s attack model</p>
    <p><em>DS<sub>N </sub>(q,K)</em> and <em>DS<sub>R </sub>(q,K)</em> represent Nakamoto&#8217;s and Rosenfeld&#8217;s models respectively for measuring the probability of success of an attacker to perform a double spend given that he/she controls <em>q </em>percent of the network&#8217;s nodes and the remaining honest nodes have successfully mined the <em>K</em> <sup>th </sup>block.</p>
    <p><strong>Two New Double Spend Attack Models:</strong></p>
    <p><a href="http://www.sciencedirect.com/science/article/pii/S157106611630113X">Two new double spend attack models were proposed in a research paper</a> that was published a few days ago. The two models were named &#8220;The generalized model&#8221; and the &#8220;Time based model&#8221;.</p>
    <p><strong>The Generalized Model:</strong></p>
    <p>This model is a generalization mode of Rosenfeld&#8217;s model by adding an extra parameter to the formula that reflects the time advantage serving the attacker i.e. the time spent by the attacker to secretly mine the fraudulent block.</p>
    <p>The Attacker potential progress can be represented by the following function:</p>
    <p style="text-align: center;"><em>P (q, m, n, t)</em></p>
    <p>This function generalizes the progress of Rosenfeld&#8217;s model. Function <em>P </em>represents the probability of success of an attacker to mine exactly <em>n </em>blocks provided that the honest nodes have successfully mined the <em>m<sup>th </sup></em>block (the proceeding block). The added parameter <em>t </em>represents the time advantage serving the attacker&#8217;s nodes to produce the block containing the fraudulent transaction.</p>
    <p><strong>The Time Based Model:</strong></p>
    <p>This new model is different from Nakamoto&#8217;s and Rosenfeld models. Throughout this attack model, states are setup via determination of lengths of both the valid and fraudulent blockchain branches and the difference between the time needed by the honest and the attacker&#8217;s nodes to mine the block in question (block <em>n</em>)</p>
    <p>The attacker&#8217;s progress function can be represented by the following function:</p>
    <p style="text-align: center;"><em>P<sub>T</sub> (q, m, n, t)</em></p>
    <p>The function represents that the probability of the time needed by the attacker&#8217;s nodes to mine the <em>n<sup>th</sup></em> block is exactly equal to <em>t </em>seconds after the time needed by the honest nodes to mine the proceeding block (the <em>m<sup>th</sup> </em>block).</p>
    <p><strong>Conclusion:</strong></p>
    <p>Two new double spend attack models were proposed by a group of researchers in a paper that was published a few days ago. The generalization model is a generalization mode of Rosenfeld classic attack model, while the new time based mode is different from both classic models; Nakamoto&#8217;s and Rosenfeld&#8217;s.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/attacks/" rel="tag">attacks</a> <a href="https://www.deepdotweb.com/tag/bitcoins/" rel="tag">bitcoins</a> <a href="https://www.deepdotweb.com/tag/blockchain/" rel="tag">blockchain</a> <a href="https://www.deepdotweb.com/tag/double/" rel="tag">double</a> <a href="https://www.deepdotweb.com/tag/models/" rel="tag">models</a> <a href="https://www.deepdotweb.com/tag/spending/" rel="tag">spending</a></span> <span style="display:none" class="updated">2016-12-31</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

