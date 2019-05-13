---
Tor Fingerprinting &#8211; Is the Tor Browser Immune Against Browser Fingerprinting?
---
<article class="post-listing post-23262 post type-post status-publish format-standard has-post-thumbnail hentry category-articles category-deepdot-news tag-browser tag-fingerprinting tag-immune tag-tor">
<div class="post-inner">
<p class="post-meta">
<span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
<span>October 25, 2017</span>
<span>in <a href="https://www.deepdotweb.com/category/articles/" rel="category tag">Articles</a>, <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a></span>
<span><a href="https://www.deepdotweb.com/2017/10/25/tor-fingerprinting-tor-browser-immune-browser-fingerprinting/#respond">Leave a comment</a></span>
</p>
<div class="clear"></div>
<div class="entry">
<p>On October 4, 2013, <a href="https://www.theguardian.com/world/2013/oct/04/nsa-gchq-attack-tor-network-encryption">the Guardian published a report</a> which stated that Edward Snowden, a former CIA employee and whistleblower, sent the British newspaper classified documents that proved that the National Security Agency (NSA) had been repeatedly making attempts to formulate successful attacks against Tor, or the onion router. However, the report claimed that all of NSA&#8217;s attempts failed to de-anonymize Tor users and as such, proved that the security of Tor is bulletproof and only those using an outdated version of the Tor browser can be successfully de-anonymized via quantum cookie attacks.</p>
<p>Nonetheless, Tor is a form of a two-edged sword. While most users appreciate the privacy and anonymity offered to them via Tor, others exploit them in various forms of online criminal activities. When online tracking and de-anonymization are concerned, internet tracebacks via browser fingerprinting are steadily growing, specifically on some commercial websites, such as BlueCava, Iovation, AddThis, 41st Parameter and ThreatMetrix. In 2010, a Panopticlick research program was initiated by the Electronic Frontier Foundation (EFF), to examine <a href="https://www.deepdotweb.com/2016/10/28/browser-fingerprinting-browser-stand/">browser fingerprinting</a>. The research proved that 94.2% of all the fingerprints of internet browsers, excluding Tor browser&#8217;s fingerprints, are unique. When a user points his/her browser to a server that runs browser fingerprinting, the server obtains some of the features of the user&#8217;s browser, which are referred to as browser fingerprints. Accordingly, the server conducting browser fingerprinting can associate the access to analyze the browser for tracking. Such association can lead to de-anonymization of users.</p>
<p><img class="wp-image-23265 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/10/word-image-50.jpeg" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/10/word-image-50.jpeg 590w, https://www.deepdotweb.com/wp-content/uploads/2017/10/word-image-50-300x156.jpeg 300w" sizes="(max-width: 590px) 100vw, 590px" /></p>
<p>Fingerprinting represents a serious threat to Tor&#8217;s main objective. As such, developers of Tor have been working on solutions to mitigate known fingerprinting techniques to preserve the anonymity of Tor users. In February 2016, Tor browser 5.5 was released to shield the browser against known browser fingerprinting techniques.</p>
<p><a href="https://link.springer.com/chapter/10.1007/978-3-319-65521-5_44">A recently published research study</a> attempted to detect how successful is Tor 5.5 in mitigating browser fingerprinting presently. The research utilized a special fingerprinting site to examine the characteristics of Tor browser accesses. Even though Tor browser resists browser fingerprinting via restriction of the functionalities of the browser, the study showed that a percentage of browser fingerprints are still vulnerable to some browser fingerprinting techniques. The paper analyzed the experimental results and the features of the Tor browser, which helped in identification of its prevention gears against various browser fingerprinting techniques. As per the performed analysis, the researchers introduced &#8220;Tor fingerprinting,&#8221; which represents a fingerprinting technique against Tor that utilizes special JavaScript codes.</p>
<p><strong>Tor Browser Fingerprinting:</strong></p>
<p>The Tor browser is immune against most of the conventional browser fingerprinting techniques. The research study introduced a unique fingerprinting technique, known as &#8220;Tor fingerprinting,&#8221; that can be utilized to track the Tor browser. The study fully examined the Tor browser to provide the following set of fingerprints. Even though some of these fingerprints have been previously reported, the study revealed how they can be used in Tor fingerprinting.</p>
<p><strong>HTTP Header:</strong></p>
<p>Essentially, in the HTTP header, the User-Agent&#8217;s value is constant. The version of a user&#8217;s Tor browser can be obtained. In versions older than 5.0, Accept-Language within the HTTP header is “en-us,en; q = 0.5”, while in version 5.0, or following versions, it is “en-US,en;q = 0.5”.</p>
<p>Size of the Content Window:</p>
<p>The window screen property can be utilized to identify Tor browser&#8217;s content window size. Furthermore, Cascading Style Sheets (CSS) media queries can be utilized to identify the size of the content window.</p>
<p><strong>Font List:</strong></p>
<p>It is well known that Font.enumerate.Fonts within the ActionScript can be utilized to obtain the installed fonts on the target&#8217;s device, along with their order. However, as the Tor browser turns off Flash plugins, the following methods can be used to hide the list of fonts in Tor 5.0 and newer versions, yet they won&#8217;t work with Tor 5.5 due to the newly developed countermeasures.</p>
<p>a. JavaScript with CSS can be utilized to identify the user&#8217;s list of fonts via comparison of the width and height of default fonts and examining the target fonts, the method&#8217;s script identifies the presence of a font when both target and default fonts are matched.</p>
<p>b. Utilizing @font-face, which is specified in CSS3, can identify the user&#8217;s fonts.</p>
<p><strong>SSE2 Test:</strong></p>
<p>Stream SIMD Extensions 2 (SSE2) can be used to detect if the user&#8217;s CPU is an Intel Pentium 4 or a newer version.</p>
<p>Detecting the Number of CPU Cores:</p>
<p>Execution of heavy calculations using multi-threads within the Web Workers API, the user&#8217;s number of CPU cores can be estimated along with the presence of Hyper-Threading Technology (HTT).</p>
<p><strong>Refresh Rate:</strong></p>
<p>A drawing&#8217;s refresh rate in a display can be estimated via means of the requestAnimationFrame method of the animation Timing API when Tor 5.0 or newer versions are used.</p>
<p>Web Storage:</p>
<p>Some of Tor browser users turn off HTTP cookies, yet they are turned on by default. As such, this operation can be a form of a fingerprint.</p>
</div>
<span style="display:none"><a href="https://www.deepdotweb.com/tag/browser/" rel="tag">browser</a> <a href="https://www.deepdotweb.com/tag/fingerprinting/" rel="tag">fingerprinting</a> <a href="https://www.deepdotweb.com/tag/immune/" rel="tag">immune</a> <a href="https://www.deepdotweb.com/tag/tor/" rel="tag">tor</a></span> <span style="display:none" class="updated">2017-10-25</span>
<div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
</div>
</article>

