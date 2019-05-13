---
Yet Another Way You Can Be Fingerprinted While Using Tor
---
<article class="post-listing post-13518 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-fingerprinted tag-tor">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/fuzzy/" title="">Fuzzy </a></span>
    <span>March 19, 2016</span>
    <span>in <a href="https://www.deepdotweb.com/category/articles/" rel="category tag">Articles</a>, <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a></span>
    <span><a href="https://www.deepdotweb.com/2016/03/19/yet-another-way-you-can-be-fingerprinted-while-using-tor/#comments">10 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p><em>Notice: This doesn&#8217;t mean that Tor is broken.</em></p>
    <p>Security Enthusiast Jose Carlos Norte recently made a <a href="http://jcarlosnorte.com/security/2016/03/06/advanced-tor-browser-fingerprinting.html">blog post</a> detailing how Tor Browser users can be uniquely fingerprinted using the mouse wheel, mouse speed, a CPU benchmark, and “getClientRects”.</p>
    <p>A POC (proof-of-concept) is <a href="http://jcarlosnorte.com/assets/ubercookie/">available</a> to try out which utilizes the methods he goes over.</p>
    <p>Right off the bat, Norte explains that these methods rely on javascript.</p>
    <p>“All the provided fingerprinting methods are based on javascript (enabled by default in tor browser as of today).”</p>
    <p>Norte quickly noticed that the Tor Browser implemented a counter measure against fingerprinting methods that relied on time accuracy – which is something that he needed. He noted that “there are a lot of ways to measure times smaller than 100ms using javascript in tor browser, some are obvious, or ther [sic] are intersting [sic]”, and so, he was able to get around this countermeasure with ease.</p>
    <p>With that out of the way, Norte moved on to fingerprinting the mouse wheel where he states that “the mouse wheel event in Tor Browser (and most browsers) leaks information of the underlying hardware used to scroll the webpage.” He contrasted what&#8217;s leaked when you use a regular mouse or a trackpad:</p>
    <p>“The event provides information about the delta scrolled, however if you are using a normal computer mouse with a mouse wheel, the delta is always three, but if you are using a trackpad, the deltas are variable and related to your trackpad and your usage patterns.”</p>
    <p>He also stated another fingerprinting vector is the mouse&#8217;s scroll speed.</p>
    <p>A POC for this method is <a href="http://jcarlosnorte.com/assets/fingerprint/">available</a> as well.</p>
    <p>Because the time accuracy countermeasure was bypassed, Norte said that it would be “easy to create a CPU intensive script (or even memory intensive) and measure how long it takes for the user browser to execute it.” This could be used to fingerprint users as when he ran tests on different computers they all returned different results.</p>
    <p>Another fingerprinting vector that Norte found – one that he described as “interesting” – utilizes <a href="https://developer.mozilla.org/en-US/docs/Web/API/Element/getClientRects">getClientRects</a>, which is described by Mozilla as a “method [that] returns a collection of rectangles that indicate the bounding rectangles for each box in a client.”</p>
    <p>Norte remarked at how it was “strange that reading back from a canvas has been prevented but simply asking the browser javascript API how a specific DOM elements has been drawn on the screen has not been prevented or protected in any way.”</p>
    <p>He even stated that this method was better than fingerprinting users using the canvas.</p>
    <p>In an online chat with <a href="https://motherboard.vice.com/read/how-you-move-your-mouse-could-help-others-track-youeven-on-tor">Motherboard</a>, Norte said that “Every user moves the mouse in a unique way”, where he then went on to say “The only solution is to deactivate Javascript completely, As long as there’s Javascript, they’ll be able to fingerprint you, one way or the other.”</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/fingerprinted/" rel="tag">fingerprinted</a> <a href="https://www.deepdotweb.com/tag/tor/" rel="tag">tor</a></span> <span style="display:none" class="updated">2016-03-19</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/fuzzy/" title="Posts by Fuzzy" rel="author">Fuzzy</a></strong></div>
    </div>
</article>

