---
Three More Reasons to Keep JavaScript off in Tor
---
<article class="post-listing post-20226 post type-post status-publish format-standard has-post-thumbnail hentry  tag-javascript tag-reasons 
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/caliens/" title="">C. Aliens </a></span>
    <span>May 30, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/05/30/three-reasons-keep-javascript-off-tor/#comments">2 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    <p>Dr. Neal Krawetz, self-proclaimed security specialist and forensic researcher, took to his personal blog to <a href="http://www.hackerfactor.com/blog/index.php?/archives/761-Exploiting-the-TOR-Browser.html">publicize three low-level vulnerabilities</a> in the Tor browser bundle. Upon first read of that sentence, one might wonder why Dr. Krawetz used his personal blog instead of the proper channels. That, it seemed, was a majorly frustrating element for the researcher: that “official” channels rarely elicited a response at all.</p>
    <p>Based on his post that summarized three vulnerabilities in the Tor browser, one might consider lack of communication between the Tor Project and (at least in this case) security researchers a vulnerability of its own. A quick read of some of his posts revealed that the researcher had a complicated relationship with the Tor project and the Tor Browser itself. But, it also showed that he was not in experienced in the world of anonymity and <a href="https://www.deepdotweb.com/tag/privacy/">privacy on the internet</a>. Despite some of the fundamental differences between his blog, The Hacker Factor (Blog) and DeepDotWeb, Dr. Krawetz raised concerns that were undeniably relevant to any Tor user.</p>
    <p>Here, he explained the difficulties he faced when he attempted contact with anyone (other than the <a href="https://twitter.com/torproject/status/858346480553394177">official Twitter account</a> users) at the Tor Project.</p>
    <p>“<em>Over the last few years, I&#8217;ve tried to report some of these profiling methods (and solutions) to the Tor Project, but each time has resulted in failure. Often, my attempts to report a vulnerability or profiling risk has been met with silence. However, I&#8217;ll take silence over intentional ignorance. For example, exposing a risk on the TOR channel on Reddit often ends with people attempting to explain to me how a risk isn&#8217;t a risk. Here&#8217;s a helpful hint: if I can identify anything about you &#8212; beyond &#8220;you&#8217;re using the TOR browser&#8221;, then it&#8217;s a risk to your privacy. Any information disclosure defeats the purpose of trying to look like everyone else</em>.”</p>
    <p><img class="wp-image-20234 aligncenter" src="/imgs/2017/05/word-image-142.jpeg" srcset="/imgs/2017/05/word-image-142.jpeg 800w, /imgs/2017/05/word-image-142-300x131.jpeg 300w" sizes="(max-width: 800px) 100vw, 800px" /></p>
    <p>The privacy concerns outlined by Dr. Krawetz fell under the “<a href="https://www.deepdotweb.com/2016/03/19/yet-another-way-you-can-be-fingerprinted-while-using-tor/">fingerprinting</a>” section of de-anonymity. A brief explanation: the Tor browser, first and foremost, protects an IP address from being used (against you) as an identifying measure. Everybody using Tor should look the same as someone else using Tor. <a href="https://www.deepdotweb.com/security-tutorials/">More on that in our Security Tutorials</a>. Fingerprinting, if you will, usually translates into a seemingly non-critical data leak that, over time, can single out a user amongst hordes of others—even if they all <em>look</em> the same. Even <a href="https://www.deepdotweb.com/2017/01/13/firefox-52-adds-tor-like-font-whitelist-prevent-fingerprinting-os-fonts/">Mozilla worked on Tor-like fingerprinting countermeasures</a> in Firefox itself</p>
    <p>Security enthusiast Jose Carlos Norte explained the term far better than I could:</p>
    <p>“<em>One common problem that tor browser tries to address is user fingerprinting. If a website is able to generate a unique fingerprint that identifies each user that enters the page, then it is possible to track the activity of this user in time, for example, correlate visits of the user during an entire year, knowing that it&#8217;s the same user.</em>” (<a href="http://jcarlosnorte.com/security/2016/03/06/advanced-tor-browser-fingerprinting.html">Norte, 2016</a>)</p>
    <p>The first of the fingerprinting issues outlined by Dr. Krawetz was about window and screen size. Since computers and mobile devices come with screens of all sizes, the Tor browser reports a fake value: that the screen and window are the same size. If a window size and a screen size are the same, “JavaScript can immediately detect the TOR-Browser.”</p>
    <p>Dr. Krawetz’s fix: make the Tor browser always report that the client uses a screen with a size larger than that of the open window.</p>
    <p><img class="wp-image-20235 aligncenter" src="/imgs/2017/05/word-image-115.png" srcset="/imgs/2017/05/word-image-115.png 600w, /imgs/2017/05/word-image-115-300x193.png 300w" sizes="(max-width: 600px) 100vw, 600px" /></p>
    <p>The second problem, another screen issue, only impacted MacOS users. (Or mainly MacOS.) The browser sometimes incorrectly calculated the screen size and thus recalculated the standard window size—a consistent 1000×1000. “[I]f the screen is smaller than that, then it will choose a width that is a multiple of 200 pixels, and a height that is a multiple of 100 pixels.”</p>
    <p>He explained that this issue was inconsistent but was “fixed” upon removal of the dock. And therefore, the researcher explained, the <a href="https://www.deepdotweb.com/tag/tor/">Tor browser</a> revealed whether or not a user ran Tor on Mac OS.</p>
    <p>​</p>
    <p>Dr. Krawetz’s fix: correctly calculate the screen size.</p>
    <p>And the third issue is with the scrollbar. Different operating systems use different width scrollbars. The Tor browser makes <em>attempts</em> to keep everybody looking the same with respect to the screen and/or window size. But, “if scrollbars are displayed, then the Viewport Size can be subtracted from the Window Size in order to find the thickness of the scrollbars.”</p>
    <p>Thanks to his research, we know the specifics:</p>
    <ul>
    <li>Tor on Mac OS uses 15 pixels of the window size.</li>
    <li>Tor on modern Windows uses 17 pixels.</li>
    <li>Tor on Linux allows an even more specific identification. “The thickness depends on the Linux variant and desktop platform, like Gnome or KDE.” 10 pixels on Linux Mint with Gtk-3.0. 13 for Ubuntu 16.04 with Gnome.</li>
    <li>And unofficial Tor browsers for mobile use zero pixels.</li>
    </ul>
    <p>Dr. Krawetz’s fix: instead of pulling the true scrollbar value, have the Tor browser report a fake one. He suggested a value of 17 pixels—the size from the most prevalent operating system in existence, Windows.</p>
    <p>For DeepDotWeb readers, the fix, not from Dr. Krawetz: <a href="https://www.deepdotweb.com/2017/03/30/tor-browser-fully-anonymous-myth-reality/">turn off JavaScript</a>.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/javascript/" rel="tag">javascript</a> <a href="https://www.deepdotweb.com/tag/reasons/" rel="tag">reasons</a> </span> <span style="display:none" class="updated">2017-05-30</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/caliens/" title="Posts by C. Aliens" rel="author">C. Aliens</a></strong></div>
    </div>
</article>

