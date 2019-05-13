---
Types of Cyberattacks Hitting the Dark Web &#8211; A Research Paper
---
<article class="post-listing post-20172 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-cyberattacks tag-dark tag-hitting tag-paper tag-research tag-types tag-web">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>May 27, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/05/27/types-cyberattacks-hitting-dark-web-research-paper/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>The dark web represents parts of the internet that only exist on darknets and overlay networks. Special software, such as the Tor browser, and network configurations are required to access various parts of the dark web. Darknets are forms of peer-to-peer (P2P) networks that are operated by individuals as well as public organizations. Tor, I2P and Freenet are the most prominent examples of darknets that exist today. Since the emergence of the dark web, the research community has been only focusing on analyzing the size and features of the dark web, along <a href="https://www.deepdotweb.com/2017/05/12/italy-watched-italian-darknet-community-since-2016/">with the goods and services offered on its various marketplaces</a>. Nevertheless, very little is known about the nature and forms of attacks that take place on the dark web.</p>
    <p>When websites of the surface web are considered, today professionals understand exactly how website vulnerabilities are exploited, in addition to the pivotal role played by botnets and Google Dorks to create a form of &#8220;background attack noise&#8221; to heighten the efficacy of attacks launched on websites on the surface web.</p>
    <p><img class="wp-image-20185 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-136.jpeg" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-136.jpeg 620w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-136-300x202.jpeg 300w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-136-290x195.jpeg 290w" sizes="(max-width: 620px) 100vw, 620px"/></p>
    <p><a href="http://www.madlab.it/papers/sac17_darknets.pdf">A recently published paper</a> attempted to examine if the basic concepts and elements of cyberattacks on the surface web apply to the dark web. Particularly, via implementation of a high interaction honeypot onto Tor&#8217;s network for seven months, the researchers underwent an analysis of the types of attack and the behavioral patterns of attackers that affect the dark web.</p>
    <p>First, we have to understand what a honeypot is.</p>
    <p><strong>What is a honeypot?</strong></p>
    <p>A honeypot is a special form of computer system that is constructed to act as a form of decoy to ambush hackers, and to monitor, mitigate or analyze attempts of cyber attackers to gain unauthorized access to websites, datacenters&#8230;.etc. Generally speaking, it is comprised of a computer, software programs, and data that emulate the behavior of a real machine connecting to the network, yet the system is actually isolated and meticulously monitored. All attempts to communicate with the honeypot are considered hostile, as no reason can justify access of legitimate users to any given honeypot.</p>
    <p><strong>Honeypot Deployment Onto The Tor Network:</strong></p>
    <p>For the purpose of the study, the researchers used three forms of internet based honeypots, as well as a system based honeypot. Each of the four honeypots was installed on a single virtual machine (VM) that was hosted on the research&#8217;s premises. Using virtual machines allowed for reversion of honeypots to the clean state, in case they had been compromised. All honeypots were hosted on the Tor network in the form of Tor websites, or hidden services.</p>
    <p>All used VMs were fully patched to shield the honeypots against privilege escalation; in other words, an attacker who successfully took down any of the used machines would not have access to modify any of the system&#8217;s files and would only be able to view the content of some directories.</p>
    <p>A group of firewall rules were used to restrict the networking capabilities of the attackers. Particularly, all outgoing and incoming connections to all ports were blocked, apart from the ones needed by Tor to run, and the ports associated with the services explicitly offered by the researchers. The firewall was also set up to prevent denial-of-service attacks by enforcing strict rate limits.</p>
    <p><strong>Types of attacks:</strong></p>
    <p>During the seven months throughout which the experiment was conducted, 287 files were uploaded onto the used honeypots by attackers. The authors of the paper classified the attacks detected into three categories:</p>
    <p>Scattered attacks:</p>
    <p>Conventional search engines sometimes index pages from the dark web via Tor2web proxies. Accordingly, websites on Tor can receive a portion of the background noise of various automated attacks that hit the surface web, scattered via the proxies that represent forms of gateways between the surface web and the deep web.</p>
    <p>Automated attacks via Tor:</p>
    <p>The honeypots received at least 1,500 attempts for path reversal. As could be concluded from the User Agent, hackers were most probably using the scripting engine &#8220;NMap&#8221; to scan their targets. The honeypots received multiple scan attempts to retrieve the Tor service&#8217;s private key, which was voluntarily hosted on the root directory of the web applications used in the experiment.</p>
    <p>During the period of operation of the honeypots, the researchers detected 400 attempts to fetch the Tor&#8217;s service private key.</p>
    <p>Manual attacks:</p>
    <p>This category included more sophisticated attacks. Attackers launching manual attacks connected via the Tor network, rather than via Tor proxies. Post-exploitation actions performed by attackers included, checking local databases, phishing <strong><em>php.info</em></strong> and system files including <strong><em>passwd, crontab, pam.conf and fstab</em></strong></p>
    <p>The researchers also detected 71 file downloads via FTP. Interestingly, attackers first communicated with the SSH server to send real usernames for login, mostly because this occurs automatically by SSH clients. Attackers then killed the active session and reconnected using valid usernames phished from the honeypot documents.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/cyberattacks/" rel="tag">cyberattacks</a> <a href="https://www.deepdotweb.com/tag/dark/" rel="tag">dark</a> <a href="https://www.deepdotweb.com/tag/hitting/" rel="tag">hitting</a> <a href="https://www.deepdotweb.com/tag/paper/" rel="tag">paper</a> <a href="https://www.deepdotweb.com/tag/research/" rel="tag">research</a> <a href="https://www.deepdotweb.com/tag/types/" rel="tag">types</a> <a href="https://www.deepdotweb.com/tag/web/" rel="tag">web</a></span> <span style="display:none" class="updated">2017-05-27</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

