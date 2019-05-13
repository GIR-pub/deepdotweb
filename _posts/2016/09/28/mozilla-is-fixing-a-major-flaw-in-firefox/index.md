---
Mozilla is Fixing a Major Flaw in Firefox
---
<article class="post-listing post-15579 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news category-news-updates tag-firefox tag-fixing tag-flaw tag-major tag-mozilla">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/americanguerrilla/" title="">American Guerrilla </a></span>
    <span>September 28, 2016</span>
    <span>in <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://www.deepdotweb.com/category/news-updates/" rel="category tag">News Updates</a></span>
    <span><a href="https://www.deepdotweb.com/2016/09/28/mozilla-is-fixing-a-major-flaw-in-firefox/#comments">1 Comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Mozilla has announced that it will be <a href="http://www.theregister.co.uk/2016/09/18/mozilla_tor_flaws/">patching a flaw in Firefox</a> that if exploited could be used to impersonate the victim’s browser software update server. Doing so would allow attackers to inject malicious code into the victim’s computer.  Mozilla also stated that the vulnerability can also be used to unmask Tor users.</p>
    <p>Tor developer Georg Koppen stated:</p>
    <p>“The security hole allows an attacker who is able to obtain a valid certificate for addons.mozilla.org to impersonate Mozilla’s servers and to deliver a malicious extension update. This could lead to arbitrary code execution. Moreover, other built-in certificate pinning’s are affected as well. Obtaining such a certificate is not an easy task, but it’s within reach of powerful adversaries such as nation states.”</p>
    <p>Movrcx also commented on the security flaw by saying:</p>
    <p>“This attack enables arbitrary remote code execution against users accessing specific Clearnet resources when used along with a targeting mechanism; such as by passively monitoring exit node traffic for traffic destined for specific Clearnet resources. Additionally, this attack enables an attacker to conduct exploitation at a massive scale against all Tor Browser users and move towards implantation after selected criteria are met; such as an installed language pack, public IP address, DNS cache, stored cookie and web history, and so on.”</p>
    <p>Movrcx went on to say that obtaining a legitimate TLS certificate for addons.mozilla.org was a very hard feat, but not impossible. He also said that Tor Project members didn’t support his claims earlier.</p>
    <p>Independent Security Researcher Ryan Duff claimed that Firefox used its own weaker rendition of key pinning that created the attack angle, and that Mozilla already fixed the flaw in a nightly version of the browser.</p>
    <p>“Firefox uses its own static key pinning method for its own Mozilla certifications instead of using HPKP. Enforcing the static method appears to be much weaker than the HPKP method and is flawed to the point that it is by passable in its attack scenario,” Duff stated.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/firefox/" rel="tag">firefox</a> <a href="https://www.deepdotweb.com/tag/fixing/" rel="tag">fixing</a> <a href="https://www.deepdotweb.com/tag/flaw/" rel="tag">flaw</a> <a href="https://www.deepdotweb.com/tag/major/" rel="tag">major</a> <a href="https://www.deepdotweb.com/tag/mozilla/" rel="tag">mozilla</a></span> <span style="display:none" class="updated">2016-09-28</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/americanguerrilla/" title="Posts by American Guerrilla" rel="author">American Guerrilla</a></strong></div>
    </div>
</article>

