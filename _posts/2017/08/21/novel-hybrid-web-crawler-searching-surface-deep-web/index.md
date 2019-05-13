---
A Novel Hybrid Web Crawler For Searching Both The Surface and Deep Web"
---
<article class="post-listing post-22104 post type-post status-publish format-standard has-post-thumbnail hentry 
tag-crawler tag-deep tag-hybrid tag-searching tag-surface tag-web">
    
<div class="post-inner">
    
    
        
<span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    
    
<span>August 21, 2017</span>
    
    
<span><a href="https://www.deepdotweb.com/2017/08/21/novel-hybrid-web-crawler-searching-surface-deep-web/#comments">1 Comment</a></span>
</p>
<div class="clear"></div>
    
    
    
<p>&nbsp;</p>
<p>The spread of terrorism over the globe has led to an increase in the efforts of law enforcement agencies (LEAs) along the rough path of discovering information related to terrorist activities via taking advantage of <a href="https://www.deepdotweb.com/2017/02/01/new-concept-deep-web-crawlers/">the most recent innovations in the web search sector</a>. Their efforts have been centered upon the &#8220;surface web&#8221; which represents parts of the internet that can be indexed by traditional search engines e.g. Google, Bing, Yahoo! and Duckduckgo. Nevertheless, these search engines are only capable of indexing just a small percentage of the pages available on the world wide web. The remainder represents non-indexable content that is part of the so called &#8220;deep web&#8221;, which generally includes web pages that cannot be accessed by web crawlers, or spiders, that are utilized by traditional search engines, due to a myriad of limitations (such as dynamic pages generated in response to specific queries, as well as private content that requires private access).</p>
<p><a href="https://www.deepdotweb.com/2017/04/28/botnets-discovering-monitoring-terrorism-related-content-dark-web/">Focused web crawlers</a> permit automated discovery of web content relevant to a certain topic via a process that involves automatic navigation throughout the web link structure and picking up the recommended hyperlinks to follow by predicting their relevance to the topic in question. <a href="https://jis-eurasipjournals.springeropen.com/articles/10.1186/s13635-017-0064-5">A recently published paper</a> proposed a generic focused web crawling framework that is designed to discover web content on any topic that is hosted on either the surface web or the dark web. This novel web crawler is coded to impeccably navigate through various web pages across the surface web and multiple darknets that represent parts of the deep web (e.g. I2P, Tor and Freenet) during a single crawling instance by automatic fine tuning of its crawling behavior and its classifier guided hyperlink selection strategy which is determined by the type of the destination network and the power of the local evidence which exists in the vicinity of a hyperlink.</p>
<p>The proposed hybrid crawler combines 11 methods for selection of hyperlinks to produce a novel crawling strategy that relies on the dynamic linear combination of both a link-based, as well as a parent web page classifier. This novel hybrid web crawler has been tested by the developers for discovering web content that includes recipes for manufacturing homemade explosives. The experiment proved the effectiveness of the hybrid crawler in searching for content on both the surface web and the deep web.</p>
<p><strong>An Overview of the Framework of the New Hybrid Crawler:</strong></p>
<p>The novel hybrid crawler has the capability of navigating through the surface web and several darknets including Tor, Freenet and I2P, and adapting its crawling strategy according to the network it is supposed to navigate. The crawler relies on a hyperlink selection strategy that is capable of endorsing multiple methods utilized under various conditions, based on the target network type of each visited hyperlink, as well as the context of the vicinity of a given hyperlink. As such, it utilizes a suite including three classifiers which are utilized as per the hyperlink selection strategy employed:</p>
<ul>
<li>A link based classifier that predicts the relevance of a given hyperlink to an unvisited web page based on its relationship to the parent page.</li>
<li>A parent web page classifier that predicts the overall relevance of the parent page which includes a hyperlink based on its global context.</li>
<li>A target web page classifier that predicts the relevance of the target page, which a hyperlink links to, on the basis of its actual textual content.</li>
</ul>
<p>These three classifiers are utilized either individually, or in combination, as the link based classifier is combined with the parent, or the target web page classifier, when specific conditions are fulfilled. The proposed hybrid crawler is based on a modified version of Apache Nutch (version 1.9).</p>
<p>The below figure shows the hybrid crawler&#8217;s proposed crawling strategy. Initially, seed pages are included in the frontier list. During each iteration, a URL is selected from the frontier list and then passed by to the specific fetching module according to the network type (i.e. surface web, Tor, I2P and Freenet). The page patching the URL is then parsed to obtain its hyperlinks which are then passed by to the link selection component. Afterwards, the crawler predicts the relevance of each URL, linking to an unvisited page, as per the selection method deployed.</p>
<p><img class="wp-image-22106 aligncenter" src="/imgs/2017/08/word-image-15.png" srcset="/imgs/2017/08/word-image-15.png 522w, /imgs/2017/08/word-image-15-293x300.png 293w, /imgs/2017/08/word-image-15-55x55.png 55w, /imgs/2017/08/word-image-15-50x50.png 50w" sizes="(max-width: 522px) 100vw, 522px" /></p>
    
    
</div><!-- .entry /-->
<a href="https://www.deepdotweb.com/tag/crawler/" rel="tag">crawler</a> <a href="https://www.deepdotweb.com/tag/deep/" rel="tag">deep</a> <a href="https://www.deepdotweb.com/tag/hybrid/" rel="tag">hybrid</a> <a href="https://www.deepdotweb.com/tag/searching/" rel="tag">searching</a> <a href="https://www.deepdotweb.com/tag/surface/" rel="tag">surface</a> <a href="https://www.deepdotweb.com/tag/web/" rel="tag">web</a></span>				<span style="display:none" class="updated">2017-08-21</span>
<div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    
    
</div><!-- .post-inner -->
</article><!-- .post-listing -->

