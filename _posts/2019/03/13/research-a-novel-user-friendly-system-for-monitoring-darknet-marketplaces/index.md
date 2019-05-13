---
Research: A novel user friendly system for monitoring darknet marketplaces
---
<article class="post-listing post-28608 post type-post status-publish format-standard has-post-thumbnail hentry  tag-darknet tag-friendly tag-marketplaces tag-monitoring tag-research tag-system tag-user">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>March 13, 2019</span>
    
    <span><a href="https://www.deepdotweb.com/2019/03/13/research-a-novel-user-friendly-system-for-monitoring-darknet-marketplaces/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    
    <p>Darknet markets have been emerging during the past few years as the ideal online platforms for trading various forms of illicit goods and services including drugs, weapons, counterfeit documents, stolen private data, hacking tools, and others. As such, it is pivotal for law enforcement agencies all over the world to develop effective means for monitoring darknet marketplaces and tracing individuals engaging in illegal activities on these dark web based platforms.</p>
    <p><a href="https://dspace.cvut.cz/handle/10467/79794">A recently published research study</a> introduced the design of a novel system for collecting information about various goods and services offered for sale on darknet marketplaces. The proposed system enables users to search the harvested data and alerts them whenever changes take place on the monitored marketplaces. Throughout this article, we will overview this system and how it can benefit cyber crime investigation units.</p>
    <p><img class="wp-image-28615" src="/imgs/2019/03/darknetmm-jpg.jpeg" alt="darknetmm.jpg" srcset="/imgs/2019/03/darknetmm-jpg.jpeg 306w, /imgs/2019/03/darknetmm-jpg-300x162.jpeg 300w" sizes="(max-width: 306px) 100vw, 306px" /></p>
    <p><strong>Design of the system:</strong></p>
    <p>The goal of this research is to develop a system for monitoring darknet marketplaces, or <a href="https://www.deepdotweb.com/2016/09/06/everything-always-wanted-know-drug-cryptomarkets/">cryptomarkets</a>, for the cybercrime division of the SKPV police, Czech Republic. The system obtains data from cryptomarkets and organizes it into structured data that can be easily searched. The system crawls the same page repeatedly in order to track changes such as new product listings, price changes, etc. Users of the system will be notified, e.g. via email, whenever any changes are identified. The system maps darknet marketplaces and harvests the following information:</p>
    <p>&#8211; Overview of product listings</p>
    <p>&#8211; Prices of different products, shipping information, and other parameters that vary from one product listing to another</p>
    <p>&#8211; Vendor information including number of completed sales, buyers&#8217; feedback, etc.</p>
    <p>Tor proxy is used (SOCKS5 proxy) so that that the system&#8217;s login module and the crawler can access darknet marketplaces. The login module will create and store a cookie that will enable the crawler to collect information from the marketplace, emulating a user on the platform. As all cryptomarkets use CAPTCHA, the system relies on a CAPTCHA rescue service to overcome this problem. These services rely on human power to solve the CAPTCHA and send the solution automatically via an API to the login module.</p>
    <p><strong>The crawler:</strong></p>
    <p>The crawler&#8217;s task is to browse through HTML pages, search them for predefined data, and find links in them to other content pages. The crawler is programmed to find product listings from different categories, e.g. cannabis, opioids, synthetic cannabinoids, etc.</p>
    <p>For each marketplace, the crawler has to be individually configured before its launch in order to create the session cookie. The crawler was tested on Dream Market, which included more than 4,000 pages. The crawler works via a cookie database session created via the login module and obtains data that is saved to scraper HTML documents.</p>
    <p><strong>The scraper:</strong></p>
    <p>After the crawler saves data to scraper HTML documents, the scraper module will extract information from them about individual products. The data extracted by the scraper will be compared with data previously saved onto the database, and if a new item is detected, it will be added to the database. However, if the data involves a product item that had been previously added to the database, the scraper will only add any modifications that might have been identified by the crawler. The scraper will also include a timestamp for any database update.</p>
    <p><strong>Database datasheets:</strong></p>
    <p>Collected data is stored on datasheets via NoSQL databases. The main reasons for choosing NoSQL databases is the ease of implementation, the flexible database model, and the feasibility of notifying other system components of data modifications.</p>
    <p>The database will be used to store the following data:</p>
    <p>1- Cookies created via the login module to crawl various marketplaces</p>
    <p>2- Description of products obtained via the crawler and organized via the scraper</p>
    <p>3- The timestamps of scraped data by the scraper</p>
    <p>To make it easy for users to access data, an index of recorded data is included in the database. Database candidates include RethinkDB or MongoDB, while for the database index Apache Solr or Elasticsearch can be used.</p>
    <p><strong>The notification system:</strong></p>
    <p>The notification system is composed of two components:</p>
    <p>1- The notification queue which will receive changes to data stored onto the database</p>
    <p>2- The notifier which will process the notification queue and inform the user about changes made. The user can be notified via web applications&#8217; push notifications, or via sending notifications to external services such as Twitter or Slack.</p>
    <p><strong>The web application:</strong></p>
    <p>The web application is the main method via which the user can browse the data harvested by the system. The web application is composed of two main parts: a backend that handles the application&#8217;s logic as well as data acquisition and a frontend that enables the user to manage the application. The frontend is the application&#8217;s presentation layer for the data requested by the user. The frontend is displayed via a web browser and has three modules: a search engine module, a visualization module, and a notification module.</p>
    <p><strong>Testing the system:</strong></p>
    <p>A prototype of the system was tested on <a href="https://www.deepdotweb.com/2018/11/07/research-the-aftermaths-of-operation-bayonet-and-the-migration-of-vendors-to-dream-market/">Dream Market</a>. The test crawl run of the system was restricted to one of the largest categories on this marketplace &#8211; digital goods. At the time of the experiment, there were 49,263 items from this category. The system created one user account via the login module, which successfully logged into the market to crawl its content. The system&#8217;s run lasted for around 45 minutes and managed to collect data of 46,657 product listings. As such, the system&#8217;s data acquisition rate reached approximately 62,209 items per hour.</p>
    <p>During the data acquisition run, the system was blocked by <a href="https://www.deepdotweb.com/2018/11/23/prevention-against-ddos-attacks/">DDoS protection</a> once every 30 requests. For every identified product, the system obtained product description, price, vendor, shipping details, and feedback of buyers who bought the same product in the past. The system&#8217;s test run showed an accuracy of 94.71%.</p>
    <p><strong>Final thoughts: </strong></p>
    <p>This user friendly darknet marketplace monitoring system is one of the first systems that can be extremely helpful not only to law enforcement agents, but also to researchers interested in studying cryptomarkets. However, the system can be easily detected and blocked by administrators of these marketplaces, so it is recommended to look for means to mask the system via for example rotating different user accounts, or regularly changing Tor nodes. Another area that would benefit from development is finding means for exposing the information collected via the system and rendering it available for law enforcement agencies and researchers.</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/darknet/" rel="tag">darknet</a> <a href="https://www.deepdotweb.com/tag/friendly/" rel="tag">friendly</a> <a href="https://www.deepdotweb.com/tag/marketplaces/" rel="tag">marketplaces</a> <a href="https://www.deepdotweb.com/tag/monitoring/" rel="tag">monitoring</a> <a href="https://www.deepdotweb.com/tag/research/" rel="tag">research</a> <a href="https://www.deepdotweb.com/tag/system/" rel="tag">system</a> <a href="https://www.deepdotweb.com/tag/user/" rel="tag">user</a></span> <span style="display:none" class="updated">2019-03-13</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

