---
A novel system for monitoring and analysis of dark web content &#8211; (A patent)
---
<article class="post-listing post-28248 post type-post status-publish format-standard has-post-thumbnail hentry  tag-analysis tag-content tag-dark tag-monitoring tag-patent tag-system tag-web">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/admin/" title="">DeepDotWeb </a></span>
    <span>January 30, 2019</span>
    
    <span><a href="https://www.deepdotweb.com/2019/01/30/a-novel-system-for-monitoring-and-analysis-of-dark-web-content-a-patent/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    
    <p>The dark web refers to a collection of websites that are accessible via special software, e.g. the Tor browser, but the IP addresses of their hosting servers are innately hidden. The dark web represents a small percentage of the deep web, which refers to portions of the internet that cannot be indexed by traditional search engines. Darknets, which collectively form the dark web, are comprised of small P2P networks, in addition to large, popular networks, such as Tor, <a href="https://www.deepdotweb.com/2018/11/25/i2p-network-current-status-and-censorship-resistance-a-research-paper/">I2P</a>, <a href="https://www.deepdotweb.com/2018/12/04/categorization-of-content-hosted-on-freenet/">Freenet</a>, and Riffle, operated by volunteering individuals and organizations. Due to the anonymous nature of the dark web and the illegal activities it facilitates, there is a pressing need for a reliable system for monitoring it, harvesting data from various hidden services present on its darknets, and providing necessary alerts according to predetermined parameters.</p>
    <p><a href="https://patents.google.com/patent/US20190007440A1/en">A recently published patent</a> presents a novel system for monitoring and analysis of the dark web. The invention also includes an alert system with a data receiving module particularly designed to receive collected data from the deep web and compile it into a Structured Data Database (SDD), which is directly connected to the system&#8217;s data receiving module. The SDD is programmed to record all obtained structured data. The system also involves a Text Search and Analytic Engine (TSAE), which is directly connected to the SDD and programmed to offer advanced search capabilities of dark web content and basic analysis of the obtained structured data. The system also includes a Knowledge Deduction Service (KDS) which is connected directly to the TSAE and programmed to perform deep analysis of the obtained data via extraction of insights regarding the interactions and behavioral patterns of various dark web surfers. The system also includes a Structured Knowledge Database (SKD) which is directly connected to the KDS and programmed to record the results of deep analysis. Lastly, the system includes an Alert Service, which is connected to the SKD and TSAE and programmed to offer prioritized alerts on the basis of the performed deep analysis.</p>
    <p>Throughout this article, we will take a look at this novel dark web monitoring and analysis system.</p>
    <p><strong>Structure of the system:</strong></p>
    <p>The patent represents a novel dark web analysis, monitoring, and alert system, which is comprised of the following, as shown via figure (1):</p>
    <p><img class="wp-image-28250" src="/imgs/2019/01/patent1-png.png" alt="patent1.PNG" srcset="/imgs/2019/01/patent1-png.png 792w, /imgs/2019/01/patent1-png-300x214.png 300w" sizes="(max-width: 792px) 100vw, 792px" /></p>
    <p><strong>Figure (1): Design of the proposed dark web monitoring, analysis, and alert system</strong></p>
    <p>&#8211; A minimum of <a href="https://www.deepdotweb.com/2018/10/26/research-a-novel-intelligent-rule-based-deep-web-crawler/">one web crawler connected to the dark web</a>. At least one web crawler is configured to specifically scan and fetch data from the dark web.</p>
    <p>&#8211; A Structured Data Database Extractor (SDE) which is directly connected to a minimum of one web crawler. The SDE is programmed to perform analysis of the data collected by at least one of the connected web crawlers and to obtain structural parameters.</p>
    <p>&#8211; A Structured Data Database (SDD), which is connected to the SDE, and programmed to record the structural parameters obtained by the SDE</p>
    <p>&#8211; A Text Search and Analytic Engine (TSAE), which is connected to the SDD, and programmed to perform advanced searches as well as basic analysis on the gathered data</p>
    <p>&#8211; A Knowledge Deduction Service (KDS), which is connected to the TSAE, and programmed to perform deep analysis on the gathered data</p>
    <p>&#8211; A Structured Knowledge Database (SKD), which is connected to the KDS, and programmed to enable storage of the results of deep analysis</p>
    <p>&#8211; An alert service module, which is connected to the SKD and TSAW, and programmed to offer prioritized alerts that are based on the results of the performed deep analysis.</p>
    <p><strong>Capabilities of the system:</strong></p>
    <p>The deep analysis performed by the system includes at least one date on which most of the comments associated with a search query were published, number of posts a user published for a given search query, distribution of content categories within a hidden service, timeline trending associated with a given search query, and top hidden services for that specific query. The deep analysis also yields users with highest reputation on the associated hidden service and monitors their online activities. The obtained data includes the users&#8217; activity hours, group dynamics, and social connections.</p>
    <p>The system&#8217;s KDS groups post into separate categories and analyze the sentiment of associated comments (positive, negative, and neutral sentiments). The TSAE identifies users&#8217; niches of interest via summation of users&#8217; posts within each category. The KDS identifies different groups via monitoring of the overall number of interactions taking place between users. The KDS also provides activity time analysis which includes:</p>
    <p>&#8211; Calculation of a temporal data distribution taking place within a given time frame</p>
    <p>&#8211; Recording the time frame that includes most of the obtained data</p>
    <p>&#8211; Saving the standard deviation and average of temporal data distribution</p>
    <p>The KDS can identify different users who use different aliases on various hidden services. This data involves:</p>
    <p>&#8211; Location of communication information which is used by multiple users</p>
    <p>&#8211; Searching for similar aliases with exclusion of common names</p>
    <p>&#8211; Location of users with similar patterns of activity via means of activity time analysis</p>
    <p>&#8211; Location of users with similar niches of interest</p>
    <p>&#8211; Location of users who are active for a specific time period and then resume their activities from other locations, or using other aliases</p>
    <p>&#8211; Location of users who publish the same content at the same time from different locations</p>
    <p>&#8211; Counting the words most frequently used by a user and performing analysis on a user&#8217;s &#8220;text&#8221;</p>
    <p><strong>The dark web alert service:</strong></p>
    <p>The alert service is composed of:</p>
    <p>&#8211; A Scheduler programmed to schedule monitoring tasks associated with each alert</p>
    <p>&#8211; An Alert Rule module configured to determine wake up intervals, enable search via a keyword, enable search via an activity associated with a certain user, enable search triggered by a certain group&#8217;s activity, enable search triggered by a trend change in a certain keyword density, and enable search triggered by appearance of a keyword or a phrase more than the usual number of times</p>
    <p>&#8211; An Alert Engine programmed to send prioritized alerts, according to the rules saved within the database of the Alert Rules module</p>
    <p>The alert service builds a connection map that includes existing users in a &#8220;case file,&#8221; analyzes connections, and recommends the addition of users that are found to have strong connections with the existing users to the &#8220;case file.&#8221;</p>
    <p>The alert service receives a client&#8217;s preferences for definition of a minimum of one alert. It also structures data obtained from the dark web on the basis of the created alerts and provides a minimum of a single prioritized alert based on the performed deep analysis.</p>
    <p><strong>Final thoughts:</strong></p>
    <p>The overviewed patent provides a novel system for monitoring and analysis of dark web content, in addition to an alert module that can trigger dark web scans based on predefined changes in keyword density of content, activity of certain users, and others. The system can progress from one hidden service to the other while extracting the addresses associated with each scanned web page, classifying the extracted content, and controlling timing of operation and data collection pace.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/analysis/" rel="tag">analysis</a> <a href="https://www.deepdotweb.com/tag/content/" rel="tag">content</a> <a href="https://www.deepdotweb.com/tag/dark/" rel="tag">dark</a> <a href="https://www.deepdotweb.com/tag/monitoring/" rel="tag">monitoring</a> <a href="https://www.deepdotweb.com/tag/patent/" rel="tag">patent</a> <a href="https://www.deepdotweb.com/tag/system/" rel="tag">system</a> <a href="https://www.deepdotweb.com/tag/web/" rel="tag">web</a></span> <span style="display:none" class="updated">2019-01-30</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name">
    </div>
</article>

