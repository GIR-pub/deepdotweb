---
layout: single
title: "JAVASCRIPT VULNERABILITIES AND REMOVING PERSONAL METADATA FROM FILES"
sidebar:
  - title: "Jolly Rogers Security Guide"
    nav: "jolly"
  - title: "DeepDotWeb"
    nav: "pages"
  - title: "Security Tutorials"
    nav: "security"
  - title: "Blog Archive"
    nav: "blognav"
permalink: "jolly-rogers-security-guide-for-beginners/javascript-vulnerabilities-and-removing-personal-metadata-from-files/"
redirect_from: "jolly-rogers-security-guide-for-beginners/javascript-vulnerabilities-and-removing-personal-metadata-from-files"
---

<p>Welcome Back.</p>
<p>Before I get into removing harmful meta data from your files, I want to talk about another vulnerability to our browsing capabilities called Javascript.</p>
<p>In mid 2013, a person in Ireland was providing hosting to people that hosted hidden services including a secure email platform called Tor Mail. Unfortunately they busted him on an unrelated charge relating to child pornography and seized all his servers. Whether or not he was related to child porn or not, is unknown to me, or it could be a silly charge the feds slapped him with but either way, the feds ended up injecting malicious Javascript into his servers so that when users would visit certain sites, this malicious code would execute on their computers and reveal information about their computers to the feds. I suggest you read the following article to learn more about this.</p>
<p>https://openwatch.net/i/200/</p>
<p>With that being said, you may want to disable Javascript in your browsers, especially when visiting certain websites like Silk Road that may become compromised one day. Many users refuse to visit the original Silk Road website and forums with Javascript enabled because the feds likely injected it with malicious Javascript to identify users.</p>
<p>In Tails, the browser is called Iceweasel and when Tor in ran in Windows, it uses Firefox. Both browsers can disable Javascript using the exact same method. Open up a Window and type the following command in the address bar, &#8220;about:config&#8221; and click the button that says &#8220;I&#8217;ll be careful, I promise.&#8221;</p>
<p>This will bring up a bunch of settings including a search bar at the top. Enter javascript in the search bar and look for the following two entries, &#8220;javascript.enabled&#8221; and &#8220;browser.urlbar.filter.javascript&#8221;. Right click on these and click &#8220;Toggle&#8221; and you will see the Value changed to false. If you want to enable Javascript again, just click Toggle again and you will see the value change back to true.</p>
<p>Again, remember that every time you restart Tails you will have to do this again, so get into a habit of doing this every time. You never know when your favorite website could become compromised.</p>
<p>Moving onto meta data. There is a bit of a famous story about an online hacker named w0rmer that would take pictures of his girlfriend and post them online after he would deface a webpage. What he either forgot, or didn&#8217;t know was that photos taken with the iPhone and other smart phones save the GPS coordinates of where the picture was taken and store it in the meta data of the picture. Check out this article below.</p>
<p>https://encyclopediadramatica.es/W0rmer</p>
<p>You need to remove this meta data! Otherwise you could end up in federal prison with w0rmer. Luckily Tails has a solution for this! See why I love Tails?</p>
<p>Applications -&gt; Accessories -&gt; Metadata Anonymisation Toolkit</p>
<p>Please get a more clear idea of how this works by reading the following page.</p>
<p>https://mat.boum.org/</p>
<p>Please note the currently supported formats. In terms of pictures, jpg, jpeg and png. But unfortunately MAT is not perfect and I wouldn&#8217;t solely rely on it, so a better idea would be to never upload pictures of yourself or your significant other online, especially bragging about a hack you committed. Please read the site provided above for more information.</p>

Updated: 2014-02-12

