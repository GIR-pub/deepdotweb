---
Mining Cryptocurrency With A Free Cloud Botnet, Why Not?
---
<article class="post-listing post-6739 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-botnet tag-cloud tag-cryptocurrency tag-free tag-mining">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/iburnez/" title="">iBurnEZ </a></span>
    <span>August 8, 2014</span>
    <span>in <a href="https://www.deepdotweb.com/category/articles/" rel="category tag">Articles</a>, <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a></span>
    <span><a href="https://www.deepdotweb.com/2014/08/08/mining-cryptocurrency-free-cloud-botnet/#comments">3 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Is it possible to mine cryptocurrency for free? According to security researchers Rob Ragan and Oscar Salazar, undoubtedly yes. They have kindly released the tools they used to sign up and exploit cloud services offering free accounts on Github But if your interested in attempting this experiment yourself you better act quickly, the duo have also released defense software designed to detect and defend against such attacks.</p>
    <p>At <a href="https://www.blackhat.com/us-14/" target="_blank">Black Hat in Las Vegas</a>, security researchers Ragan and Salazar demonstrated how to create an automated email creating and account sign up process to create a cloud botnet, then how the botnet could be monetized. To host their automated email applications Ragan and Salazar used Google App Engine.</p>
    <p>There are some basic flaws in the account sign up process for many cloud services. Ragan and Salazar identified 150 cloud services offering free accounts with varying types of account verification and programming language support. Of these 150 clouds services Ragan and Salazar identified 66% who only required email confirmation to verify the sign up process. Voile ah, they had their targets.</p>
    <p>While the sign up process for these servers was inadequate it wasn’t completely devoid of protective measures. Some of the cloud services blacklisted mass email services such as Mailinator.com to prevent abuse. Ragan and Salazar would need to use realistic email addresses to sign up for these free cloud service accounts.</p>
    <p>To create thousands of realistic email addresses they scraped data breach dumps and harvested the local-part (<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="2b4744484a47065b4a595f6b4f44464a424505484446">[email&#160;protected]</a>) of the email addresses to use when creating their own fake email accounts.</p>
    <p>Next they needed to create thousands of email addresses using several different domains. Originally they had planned to register cheap domains via Namecheap.com and create email addresses using the newly purchased domain names. But for their experiment they wanted to create a truly FREE bot. Then they discovered FreeDNS.afraid.org (and several other services like it). FreeDNS.afraid.org hosts 100,000+ domains you can use to create an email account, and about 30,000 of these domains allow you to create a subdomain and custom MX records. They selected their domains, created subs, and then pointed the MX records to a service, such as  @mailgun, capable of parsing out the activation link from the emails.</p>
    <p>Ragan and Salazar used the inbound mail handler to parse the activation links from cloud service verification emails into JSON and then post the data to a the C&amp;C server URL where the account link is clicked and activated. This process was demonstrated and took a matter of seconds from start to finish.</p>
    <p>To store cloud account information Ragan and Salazar used an open-source document database from MOngoDB.com. This allowed them to manage the registered email addresses and associated passwords, and information regarding the cloud account such as account space and supported programming languages.</p>
    <p>For their experiment Ragan and Salazar were not interested in testing the limits of their automated sign up process, and yet they registered around a thousand free accounts for cloud services. They also outline a tip to gain additional capacity on these free accounts by “referring friends” to sign up for the service. As you can imagine this process followed the same automated sign up process as before. Some cloud services capped the amount of additional space you could gain through referrals, others did not. Through the referral process Ragan and Salazar managed to achieve 1TB of space on an unnamed cloud service, more space then could be purchased if you were so inclined. 1TB wasn’t even the limit, the duo simply stopped there, but this cloud service would have allowed them to continue acquiring more space through the referral program.</p>
    <p>Now they had their bot, and it was time to harness its awesome free power.  Ragan and Salazar opted to mine for cryptocurrency, but realistically cryptocurrency mining was only one of several other equally practical options.</p>
    <ul>
    <li>Distributed network scanning</li>
    <li>Distributed password cracking</li>
    <li>DDoS</li>
    <li>Click-Fraud</li>
    <li>Crypto currency mining</li>
    <li>Data storage</li>
    </ul>
    <p>To control the backend of the C&amp;C server Ragan and Salazar used a python framework called Fabric, this allowed them to use a single command and deploy the cryptominers on all accounts across the botnet. Their C&amp;C server instructed the bots to download the crypto mining file and unzip it, start the mining process, and delete the file as an effort to prevent their bots from being discovered.</p>
    <p>Free cloud service accounts generally do not have GPUs and are not ideal for mining Bitcoins, so this experiment was directed toward mining Litecoins. Keeping in mind the entirely free nature of this botnet and that it was not exploited to its fullest extent, each bot account was capable of mining about $0.25 cents of Litecoin per day. Multiply this by the thousand bot accounts and you get $250 per day, or $1,750 per week of pure profit. Not too shabby, and there is opportunity for expansion.</p>
    <p>For this experiment Ragan and Salazar were not looking to make money or be malicious so they turned off their bot after a few hours. However, they left a few select accounts running to test whether the mining would be detected, after two weeks of mining they were still going strong.</p>
    <p>While cloud services are still using antiquated verification techniques such as email confirmation there is a good chance you will be able to set up your own free cloud botnet. At some point these cloud services will need to figure out how to monitor activity on their servers so they can choose to prevent this activity, but most of these cloud services are still unprepared and vulnerable to this kind of exploitation.</p>
    <p><span style="text-decoration: underline;">Link to the cloudbot tools git hub</span>:<br />
    <a href="https://github.com/BishopFox/anti-anti-automation" target="_blank">https://github.com/<wbr />BishopFox/anti-anti-automation</a></p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/botnet/" rel="tag">botnet</a> <a href="https://www.deepdotweb.com/tag/cloud/" rel="tag">cloud</a> <a href="https://www.deepdotweb.com/tag/cryptocurrency/" rel="tag">cryptocurrency</a> <a href="https://www.deepdotweb.com/tag/free/" rel="tag">free</a> <a href="https://www.deepdotweb.com/tag/mining/" rel="tag">mining</a></span> <span style="display:none" class="updated">2014-08-08</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/iburnez/" title="Posts by iBurnEZ" rel="author">iBurnEZ</a></strong></div>
    </div>
</article>

