---
Quick Tutorial: Sylpheed Email Client With Lelantos
---
<article class="post-listing post-9672 post type-post status-publish format-standard has-post-thumbnail hentry  tag-client tag-email tag-lelantos tag-quick tag-sylpheed tag-tutorial">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/admin/" title="">DeepDotWeb </a></span>
    <span>January 14, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/01/14/quick-tutorial-sylpheed-email-client-lelantos/#comments">1 Comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Thanks to Gros Lulu for contributing this article! A manual for the Sylpheed email client with Lelantos Tor webmail accounts:</p>
    <p>Some of you already use a Tor based email system, or are looking for one.</p>
    <p>I really like the Lelantos Tor webmail service: <strong>http://lelantoss7bcnwbv.onion</strong><br/>
    It’s not free: it costs around 30$ in Bitcoin to obtain a lifetime membership. However, this money should ensure that you receive a quality service.</p>
    <p>I’m not going to explain all of the intricate Lelantos details, but with that price, you will get 1 GB of space, 5 email addresses, as well as up to 100 aliases. You can tell Lelantos system to automatically encrypt any incoming mail with your public PGP key, and to destroy any mail older than a number of pre-defined days that you choose. There is a non-JavaScript webmail (Squirrelmail) and a Java-enabled one (Roundcube).</p>
    <p>Once we have such a webmail address, it can be very time consuming to use it to check, receive, open or send emails.</p>
    <p>Here comes the Sylpheed part: great desktop mail software, available for BSD, Linux, Mac OS, Unix and Windows. It was created in 2000 and continues to improve. The better known Claws Mail is a <a href="http://en.wikipedia.org/wiki/Sylpheed">fork of Sylpheed</a>! and can be found <a href="http://sylpheed.sraoss.jp/en" target="_blank">here</a>.</p>
    <p>Configured with your Lelantos account(s), this software can help you to save a lot of time, and is a more user friendly way of managing your emails.</p>
    <p>I think Sylpheed + Lelantos is the (or my) best deal between security and easy/fast use of (quite) secure email, as a small home darknet curious/user without any criminal activity, but a lover of his privacy. And, last but not least, it’s important to know that GnuPG is natively supported by Sylpheed.</p>
    <p>Why choose Sylpheed instead of Claws? Because I was never able to make Claws work like I wanted with Lelantos…</p>
    <p>So, now I want to share my precious knowledge!  :-)</p>
    <p>The procedure below is to manage your Lelantos mails with IMAP (Sylpheed becomes a mirror display of your Lelantos webmail), but I suppose you can configure the software to work with POP3 as well; it could even work faster, but I haven’t tried.</p>
    <p>Install Sylpheed.  You will need to be connected to the Tor network.</p>
    <p>In the top menu Configuration, Create new account… (from now, do exactly as shown on the screen captures):</p>
    <p><a href="/imgs/2015/03/image001.png"><img class="aligncenter size-full wp-image-9673" src="/imgs/2015/03/image001.png" alt="image001" width="538" height="356" srcset="/imgs/2015/03/image001.png 538w, /imgs/2015/03/image001-300x199.png 300w" sizes="(max-width: 538px) 100vw, 538px"/></a></p>
    <p><a href="/imgs/2015/03/image002.png"><img class="aligncenter size-full wp-image-9674" src="/imgs/2015/03/image002.png" alt="image002" width="538" height="356" srcset="/imgs/2015/03/image002.png 538w, /imgs/2015/03/image002-300x199.png 300w" sizes="(max-width: 538px) 100vw, 538px"/></a></p>
    <p><a href="/imgs/2015/03/image003.png"><img class="aligncenter size-full wp-image-9675" src="/imgs/2015/03/image003.png" alt="image003" width="538" height="356" srcset="/imgs/2015/03/image003.png 538w, /imgs/2015/03/image003-300x199.png 300w" sizes="(max-width: 538px) 100vw, 538px"/></a></p>
    <p>Once done, right click on your new account in left column of Sylpheed: Properties…</p>
    <p><a href="/imgs/2015/03/image004.png"><img class="aligncenter size-full wp-image-9676" src="/imgs/2015/03/image004.png" alt="image004" width="404" height="429" srcset="/imgs/2015/03/image004.png 404w, /imgs/2015/03/image004-283x300.png 283w" sizes="(max-width: 404px) 100vw, 404px"/></a></p>
    <p><a href="/imgs/2015/03/image005.png"><img class="aligncenter size-full wp-image-9677" src="/imgs/2015/03/image005.png" alt="image005" width="404" height="429" srcset="/imgs/2015/03/image005.png 404w, /imgs/2015/03/image005-283x300.png 283w" sizes="(max-width: 404px) 100vw, 404px"/></a></p>
    <p><a href="/imgs/2015/03/image006.png"><img class="aligncenter size-full wp-image-9678" src="/imgs/2015/03/image006.png" alt="image006" width="404" height="429" srcset="/imgs/2015/03/image006.png 404w, /imgs/2015/03/image006-283x300.png 283w" sizes="(max-width: 404px) 100vw, 404px"/></a></p>
    <p><a href="/imgs/2015/03/image007.png"><img class="aligncenter size-full wp-image-9679" src="/imgs/2015/03/image007.png" alt="image007" width="404" height="429" srcset="/imgs/2015/03/image007.png 404w, /imgs/2015/03/image007-283x300.png 283w" sizes="(max-width: 404px) 100vw, 404px"/></a></p>
    <p><a href="/imgs/2015/03/image008.png"><img class="aligncenter size-full wp-image-9680" src="/imgs/2015/03/image008.png" alt="image008" width="404" height="429" srcset="/imgs/2015/03/image008.png 404w, /imgs/2015/03/image008-283x300.png 283w" sizes="(max-width: 404px) 100vw, 404px"/></a></p>
    <p><a href="/imgs/2015/03/image009.png"><img class="aligncenter size-full wp-image-9681" src="/imgs/2015/03/image009.png" alt="image009" width="404" height="429" srcset="/imgs/2015/03/image009.png 404w, /imgs/2015/03/image009-283x300.png 283w" sizes="(max-width: 404px) 100vw, 404px"/></a></p>
    <p>The GnuPG option is in the Privacy tab, but I haven’t tried this. Check also the Privacy tab of the General Settings panel of Sylpheed in the top menu Configuration.</p>
    <p>I hope this information will be helpful for some of you.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/client/" rel="tag">client</a> <a href="https://www.deepdotweb.com/tag/email/" rel="tag">email</a> <a href="https://www.deepdotweb.com/tag/lelantos/" rel="tag">lelantos</a> <a href="https://www.deepdotweb.com/tag/quick/" rel="tag">quick</a> <a href="https://www.deepdotweb.com/tag/sylpheed/" rel="tag">sylpheed</a> <a href="https://www.deepdotweb.com/tag/tutorial/" rel="tag">tutorial</a></span> <span style="display:none" class="updated">2016-01-14</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name">
    </div>
</article>

