---
Browser Fingerprinting: Does Your Browser Stand Out?
---
<article class="post-listing post-16067 post type-post status-publish format-standard has-post-thumbnail hentry  tag-browser tag-fingerprinting tag-stand">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/ciphas/" title="">Ciphas </a></span>
    <span>October 28, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/10/28/browser-fingerprinting-browser-stand/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Those of us who use Tor are probably already concerned about privacy. So, in that sense, are you aware of your browser fingerprint?</p>
    <p>For those unfamiliar with the term, browser fingerprinting is a method of tracking web browsers by the configuration and settings data that they make available to websites. This type of tracking reveals a considerable amount of information about you, whether you realize it or not.</p>
    <p><strong>We Know Everything About You…</strong></p>
    <p>There are a number of sites where you can check to see if your device has a unique fingerprint, as well as what kind of information you’re sending out about yourself. One of the better known ones is <a href="https://panopticlick.eff.org/">Panopticlick</a>, by the <a href="https://www.eff.org/">Electronic Frontier Foundation</a>.</p>
    <p>Panopticlick, in a nutshell, tests whether or not your browser blocks tracking ads, invisible trackers, and other sorts of trackers.</p>
    <p><img class="wp-image-16068 aligncenter" src="/imgs/2016/10/word-image-71.png" width="1061" height="517" srcset="/imgs/2016/10/word-image-71.png 1572w, /imgs/2016/10/word-image-71-300x146.png 300w, /imgs/2016/10/word-image-71-1024x499.png 1024w" sizes="(max-width: 1061px) 100vw, 1061px"/></p>
    <p>If you then decide to view the details of the results, Panopticlick will display those in a chart. The chart shows such information as your screen size and color depth, limited supercookie test, browser plugin details, and time zone.</p>
    <p>Of course, Panopticlick is only one such site that can test your device fingerprint, and some actually do more thorough tests than others.</p>
    <p>JonDonym also offers a free fingerprinting test that actually goes into more detail than the Panopticlick test. Their tester can be found at <a href="http://ip-check.info/?lang=en">IP check</a>.</p>
    <p><img class="wp-image-16069 aligncenter" src="/imgs/2016/10/word-image-72.png" width="906" height="438" srcset="/imgs/2016/10/word-image-72.png 1578w, /imgs/2016/10/word-image-72-300x145.png 300w, /imgs/2016/10/word-image-72-1024x495.png 1024w" sizes="(max-width: 906px) 100vw, 906px"/></p>
    <p>If you aren’t protected by any sort of anonymizing software or privacy enhancement, IP Check will show your true IP address, location, and user-agent (web browser and operating system), among other information. (Someone I know described this as “Panopticlick on steroids.”)</p>
    <p>Besides these two fingerprint tests, there are others. Two you may want to try are <a href="https://amiunique.org/">Am I unique?</a> and <a href="https://browserprint.info">Browserprint</a> (which is based on publicly available code from “Am I unique” and <a href="https://github.com/Valve/fingerprintjs2">Fingerprintjs2</a>, another open-source test.)</p>
    <p>While you could write separate articles on each of these, here’s a quick summary. Like Panopticlick, Am I unique tells you how much you stand out based on what browser you’re using, which OS you’re running, what language you’re configured to use, and other settings.</p>
    <p><img class="wp-image-16070 aligncenter" src="/imgs/2016/10/word-image-73.png" width="870" height="422" srcset="/imgs/2016/10/word-image-73.png 1590w, /imgs/2016/10/word-image-73-300x145.png 300w, /imgs/2016/10/word-image-73-1024x497.png 1024w" sizes="(max-width: 870px) 100vw, 870px"/></p>
    <p>If you so choose, you can view your fingerprint in detail as well. Browserprint, in the same vein, will try to determine if you have a unique fingerprint. Before starting the test, you can specify if you’re using a VPN, spoofing part of your fingerprint, etc. Like the others, it will reveal a lot about your machine!</p>
    <p><img class="wp-image-16071 aligncenter" src="/imgs/2016/10/word-image-74.png" width="917" height="447" srcset="/imgs/2016/10/word-image-74.png 1579w, /imgs/2016/10/word-image-74-300x146.png 300w, /imgs/2016/10/word-image-74-1024x499.png 1024w" sizes="(max-width: 917px) 100vw, 917px"/></p>
    <p>All this to say &#8211; it’s a little scary how much information your device and/or browser can reveal about you. So, your next question may be, “How the hell can I protect myself?”</p>
    <p>There are a number of ways, as a matter of fact.</p>
    <p>If you try the Panopticlick test while using Tor, particularly at the highest security setting, it may say “Your browser has an almost-unique fingerprint.” (At least that was my experience.)</p>
    <p>Part of the reason that the Tor browser reduces the uniqueness of your fingerprint is because by default, it includes the <a href="https://noscript.net/">NoScript</a> extension, which I’m sure most Tor users are familiar with.</p>
    <p><img class="wp-image-16072 aligncenter" src="/imgs/2016/10/word-image-75.png" srcset="/imgs/2016/10/word-image-75.png 480w, /imgs/2016/10/word-image-75-150x150.png 150w, /imgs/2016/10/word-image-75-300x300.png 300w, /imgs/2016/10/word-image-75-55x55.png 55w, /imgs/2016/10/word-image-75-50x50.png 50w" sizes="(max-width: 480px) 100vw, 480px"/></p>
    <p>NoScript allows JavaScript, Java, Flash, and other plugins to be executed only on sites which you deem trustworthy. Plugins like these, as you may or may not know, collect a lot of information about you and your system.</p>
    <p>Granted, some sites won’t function properly with NoScript running, which is why it has a whitelist function for particular sites. It also protects against attacks like <a href="https://www.owasp.org/index.php/Cross-Site_Scripting_(XSS)">Cross-Site Scripting</a> and <a href="https://www.owasp.org/index.php/Clickjacking">Clickjacking</a>.</p>
    <p>You can also install NoScript on a standard Firefox browser, and it will serve the same function that it does on Tor.</p>
    <p>Anyhow, the basic point is that the more you appear to be like everyone else on the internet, the less of a unique fingerprint you have.</p>
    <p><strong>Suggestion: A Privacy Userscript</strong></p>
    <p><strong><img class="wp-image-16073 aligncenter" src="/imgs/2016/10/word-image-76.png" width="834" height="478" srcset="/imgs/2016/10/word-image-76.png 1248w, /imgs/2016/10/word-image-76-300x172.png 300w, /imgs/2016/10/word-image-76-1024x587.png 1024w" sizes="(max-width: 834px) 100vw, 834px"/></strong></p>
    <p>There is another tool which I came across that does not involve Tor, but can enhance your privacy while using Firefox.</p>
    <p>Specifically, it’s a privacy-enhancing userscript for Firefox, developed by <a href="https://github.com/blacklight447">blacklight447</a>.</p>
    <p>Are you familiar with the term userscript? If not, it refers to an open-source licensed add-on for a browser that can change a web page as it’s loaded.</p>
    <p>That being said, what this particular userscript does is to block some unsafe crypto-suites in Firefox, as well as blocking a number of standard scripts from running. It can be found at <a href="https://github.com/blacklight447/blacklight447-s-firefox-privacy-userscript">GitHub: blacklight447&#8217;s Firefox privacy enhancing userscript</a></p>
    <p>While this userscript doesn’t provide full anonymity, it is an improvement over the standard Firefox browser settings.</p>
    <p>For those of you who use Freenet, the same userscript is available on there as well &#8211; <a href="http://localhost:8888/freenet:USK@FKdTcKAKeak4jH7xs9N-jQwa~~0fjn6MuB~YHREsprM,DvJ1y8T5m4efVpDKV~K0pukeUOXAd2VuuZdR4wSvMIk,AQACAAE/blacklight%27s-userscript/14/code.html">Freenet: blacklight&#8217;s privacy userscript</a>. If any of you have a chance to try this out, feel free to share your experience in the comments.</p>
    <p><strong>JonDoFox and JonDo Proxy</strong></p>
    <p><strong><img class="wp-image-16074 aligncenter" src="/imgs/2016/10/word-image-77.png" srcset="/imgs/2016/10/word-image-77.png 503w, /imgs/2016/10/word-image-77-300x232.png 300w" sizes="(max-width: 503px) 100vw, 503px"/></strong></p>
    <p>As mentioned above, JonDo offers a number of privacy-enhancing tools (some of which are free, and some which you have to pay for). I’m more of a fan of the free stuff, personally.</p>
    <p>Among these is JonDoFox, a profile for Firefox that’s optimized for anonymity and security. While it’s not as secure as using the Tor browser, it’s definitely an improvement. JonDoFox automatically uses the JonDo Proxy by default, as well as NoScript and a few other plugins.</p>
    <p>So you may want to check this one out as well.</p>
    <p><strong>You Haven’t Seen Me…</strong></p>
    <p>These browsers and userscripts are just a few of the many tools that can reduce your browser fingerprint. It is, of course, something that’s good to become aware of, <em>especially</em> if you’re concerned about who’s tracking you and your browsing habits.</p>
    <p>Or did you <em>never</em> wonder why those same underwear ads keep following you on every website you visit?</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/browser/" rel="tag">browser</a> <a href="https://www.deepdotweb.com/tag/fingerprinting/" rel="tag">fingerprinting</a> <a href="https://www.deepdotweb.com/tag/stand/" rel="tag">stand</a></span> <span style="display:none" class="updated">2016-10-28</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/ciphas/" title="Posts by Ciphas" rel="author">Ciphas</a></strong></div>
    </div>
</article>

