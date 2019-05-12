---
Security Researchers Found a “One-Stop-Shop” for Hacking Tools on Command and Control Server
---
<article class="post-listing post-17409 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news category-news-updates tag-command tag-control tag-hacking tag-onestopshop tag-researchers tag-security tag-server tag-tools">
    
    <div class="post-inner">
    
    
    <p class="post-meta">
    
    <span>Posted by: <a href="https://www.deepdotweb.com/author/caliens/" title="">C. Aliens </a></span>
    
    
    <span>January 9, 2017</span>
    <span>in <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://www.deepdotweb.com/category/news-updates/" rel="category tag">News Updates</a></span>
    
    <span><a href="https://www.deepdotweb.com/2017/01/09/security-researchers-found-one-stop-shop-hacking-tools-command-control-server/#comments">4 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    <div class="entry">
    
    <p>Security researchers from Kaspersky Lab’s Secure List described the accidental discovery of a “one-stop-shop” for hacking tools. The <a href="https://www.deepdotweb.com/2016/12/26/shadow-brokers-take-zeronet-sell-stolen-nsa-exploits/">Kaspersky Lab team</a> intercepted traffic from machines infected with the Hawkeye RAT and “stumbled upon an interesting domain.” They found a command and control server that saved the keylog data provided by the HawEye RAT. The server <a href="https://securelist.com/blog/research/76986/one-stop-shop-server-steals-data-then-offers-it-for-sale/">additionally sold hacking software, tools, and site-specific logins</a>.</p>
    <p><img class="wp-image-17415 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-31.png" width="858" height="487" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-31.png 1352w, https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-31-300x170.png 300w, https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-31-1024x581.png 1024w" sizes="(max-width: 858px) 100vw, 858px" /></p>
    <p>The researchers scanned the running services on the command and control server and found the “interesting” aspect. The server functioned as both a backend for storing the stolen credentials from the HawkEye RAT, but also a front-end for selling them. Later scans revealed that the site was new yet operational. The front-end already allowed Individuals, presumably just buyers, to create accounts. After a user created an account, the server gave the accounts an interface to browse the available goods, as well as purchase them when ready.</p>
    <p>Upon creation of a new account and a subsequent successful login, a forum-type interface appears. No sign of the harvested credentials—at least the behind-the-scenes part—made itself apparent to the buyer (or researcher). The server’s operators ended new-user registration as of this post, although the login screen still allows attempted account registration. The “one-stop-shop” frontend, though, showed just how recently the project manifested itself. The server’s administrators intended the “goods” and data to be securely stored on the server. But, “[the server] contained a crucial vulnerability which allowed researchers to download the stolen data,” Ido Naor wrote.</p>
    <p>Additionally, the admin(s) added six new shell scripts in late November, one week prior to the Kaspersky Lab investigation into the HawEye RAT.</p>
    <p><img class="wp-image-17416 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-32.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-32.png 1024w, https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-32-300x89.png 300w" sizes="(max-width: 1024px) 100vw, 1024px" /></p>
    <p>The forum’s storefront, for lack of valid terminology, offered insight into the scope of the operation. In one set of scampages, valued at $13 each, the site in question are up-to-date. The Scam Page category listed several scam pages for popular sites, each appended with “2016.” The category contained scam page listings for Amazon, Apple, Netflix, Paypal, Barclays Bank, and Halifax Bank, among others. Naor wrote that the dates likely showed how “up-to-date the scam pages are in terms of the bank’s website updates.”</p>
    <p><img class="wp-image-17417 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-2.jpeg" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-2.jpeg 969w, https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-2-300x131.jpeg 300w" sizes="(max-width: 969px) 100vw, 969px" /></p>
    <p>The admins set the forum up to, for semi-standard reasons, only accept digital or cryptocurrencies such as Perfect Money or Bitcoin. The admins, or listing owners, offer clear and precise instructions for what to do after purchasing. In a similar vein, they explained—very explicitly—what not to do before “creating a ticket.”</p>
    <p><img class="wp-image-17418 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-33.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-33.png 1024w, https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-33-300x87.png 300w" sizes="(max-width: 1024px) 100vw, 1024px" /></p>
    <p>One rule, for instance, stated that buyers must not use insulting words in their complaint. Similarly, a word like “scam” would result in a permanent ban.</p>
    <p>The researchers described HawkEye as a “robust keylogger,” given the abilities the malware totes. It records keystrokes on a victim’s machine—in any application. It identifies login and password combinations, as well as the associated login event and landing page. The logs on the command and control server showed a massive diversity in types of breached accounts. Possibly the most extreme of the compromised accounts belonged to the <a href="https://www.deepdotweb.com/2016/06/22/70000-government-corporate-servers-sale-cheap-6-hacker-marketplace/">Pakistani government</a>, the article explained.</p>
    <p><img class="wp-image-17419 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-34.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-34.png 426w, https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-34-150x150.png 150w, https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-34-300x300.png 300w, https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-34-55x55.png 55w, https://www.deepdotweb.com/wp-content/uploads/2017/01/word-image-34-50x50.png 50w" sizes="(max-width: 426px) 100vw, 426px" /></p>
    
    
    </div><!-- .entry /-->
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/command/" rel="tag">command</a> <a href="https://www.deepdotweb.com/tag/control/" rel="tag">control</a> <a href="https://www.deepdotweb.com/tag/hacking/" rel="tag">hacking</a> <a href="https://www.deepdotweb.com/tag/onestopshop/" rel="tag">onestopshop</a> <a href="https://www.deepdotweb.com/tag/researchers/" rel="tag">researchers</a> <a href="https://www.deepdotweb.com/tag/security/" rel="tag">security</a> <a href="https://www.deepdotweb.com/tag/server/" rel="tag">server</a> <a href="https://www.deepdotweb.com/tag/tools/" rel="tag">tools</a></span>				<span style="display:none" class="updated">2017-01-09</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/caliens/" title="Posts by C. Aliens" rel="author">C. Aliens</a></strong></div>
    
    
    </div><!-- .post-inner -->
</article><!-- .post-listing -->

