---
Intel chips from last 7 years can be hacked remotely
---
<article class="post-listing post-20019 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-chips tag-hacked tag-intel tag-remotely tag-years">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/filipjelic/" title="">Filip Jelic </a></span>
    <span>May 21, 2017</span>
    <span>in <a href="https://www.deepdotweb.com/category/articles/" rel="category tag">Articles</a>, <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a></span>
    <span><a href="https://www.deepdotweb.com/2017/05/21/intel-chips-from-last-7-years-can-be-hacked-remotely/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Before we dwell into this vulnerability, allow me to set the table. Once upon a time, Intel decided to add some hardware to their chips to allow admins to remotely control their servers. So today, Intel chips for server solutions contain &#8220;Management Engine&#8221; (ME) &#8211; a microcontroller inside of a processor. ME works independently to the operating system and it works even if the OS is shutdown (provided power supply and network access) so administrators can remotely turn the machine on and off, manage the server and even reinstall the operating system. You can access network, memory, storage, processors, and connected hardware, all of that completely out of sight to the operating system, let alone anti-virus. This level of privileges is called ring –2 and, once again, it&#8217;s connected to the internet. For obvious reasons, this feature bugs security and privacy conscious people to the extent that you can find many tutorials that teach you how to physically rip off that part of the chip.</p>
    <p>In February 2017 (but patched in May 2017), security researcher Maksim Malyutin from researching team Embedi, discovered a logical flaw in ME firmware that allows hackers to use technologies such as AMT and ISM to bypass authentication and gain control over ME over the network. If you use mentioned technologies for your server, head over to <a href="https://security-center.intel.com/advisory.aspx?intelid=INTEL-SA-00075&amp;languageid=en-fr">this advisory</a> and patch up! Otherwise, let&#8217;s delve into the (trivial) technical details of this vulnerability.</p>
    <p>ME firmware was written in C, so it wasn&#8217;t too hard to find the authentication part in reverse engineered firmware – function: int strncmp (string s1, string s2, int cmplength). This function takes two strings and a number. Strings are to be compared and the number specifies how many characters from the beginning of the string are to be compared. Based on the comparison, the function returns 0 if the first &#8216;cmplength&#8217; characters are the same, in which case, admin is authenticated.</p>
    <p>The firmware handles authentication by comparing user response string with the one stored on the server (computed response) like this:</p>
    <p><img class="wp-image-20026 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-85.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-85.png 478w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-85-300x54.png 300w" sizes="(max-width: 478px) 100vw, 478px" /></p>
    <p>Flaw resides in the third argument – number of characters to be compared is the length of the user response! If the user could somehow send nothing (null), the program would compare first 0 characters which would always be true. Communication with AMT happens over HTTP so nothing stops an attacker to set up a proxy and remove the user response string on the fly. Third argument should&#8217;ve been computed response&#8217;s length!</p>
    <p>For more detailed version, check out <a href="https://www.embedi.com/files/white-papers/Silent-Bob-is-Silent.pdf">Embedi&#8217;s whitepaper</a> on the topic. It also contains an exploitation example. Before I go, it&#8217;s worth mentioning that vulnerable remote control technologies are turned off by default, which is a lifesaver for many people right now.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/chips/" rel="tag">chips</a> <a href="https://www.deepdotweb.com/tag/hacked/" rel="tag">hacked</a> <a href="https://www.deepdotweb.com/tag/intel/" rel="tag">intel</a> <a href="https://www.deepdotweb.com/tag/remotely/" rel="tag">remotely</a> <a href="https://www.deepdotweb.com/tag/years/" rel="tag">years</a></span> <span style="display:none" class="updated">2017-05-21</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/filipjelic/" title="Posts by Filip Jelic" rel="author">Filip Jelic</a></strong></div>
    </div>
</article>

