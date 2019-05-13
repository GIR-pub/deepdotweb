---
The Darkmail Alliance
---
<article class="post-listing post-8749 post type-post status-publish format-standard has-post-thumbnail hentry category-articles category-deepdot-news tag-alliance tag-darkmail">
<div class="post-inner">
<p class="post-meta">
<span>Posted by: <a href="https://www.deepdotweb.com/author/zubairmuadh/" title="">Zubair Muadh </a></span>
<span>February 25, 2015</span>
<span>in <a href="https://www.deepdotweb.com/category/articles/" rel="category tag">Articles</a>, <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a></span>
<span><a href="https://www.deepdotweb.com/2015/02/25/the-darkmail-alliance/#comments">4 Comments</a></span>
</p>
<div class="clear"></div>
<div class="entry">
<p>After being forced to shut down his service in order to <a href="http://en.wikipedia.org/wiki/Lavabit" target="_blank">not hand over user data</a>, Lavabit founder Ladar Levison teamed up with Mike Janke and Jon Callas, the CEO and CTO of <a href="https://silentcircle.com/" target="_blank">Silent Circle</a>. They also shut down their email service out of fear of being forced to <a href="http://www.forbes.com/sites/parmyolson/2013/08/09/encryption-app-silent-circle-shuts-down-e-mail-service-to-prevent-spying">hand over user data</a> to authorities. They together have formed ‘<a href="http://darkmail.info/">The Darkmail Technical Alliance</a>’ along with Phil Zimmerman, the man who brought PGP encryption to the masses.</p>
<p>The mission aim is to create a Darkmail Protocol. A new email protocol that’s end-to-end encrypted and all that an outside observer can see is the size of the email.</p>
<p>The Darkmail Whitepaper can be found here (<a href="https://darkmail.info/downloads/dark-internet-mail-environment-december-2014.pdf">WhitePaper</a>) the project is known collectively as Dark Internet Mail Environment (DIME). The Source code for DIME-Integrated Lavabit: <a href="https://github.com/lavabit/">Lavabit SourceCode</a></p>
<p>The way DIME works is that it applies multiple layers of encryption to an e-mail to make sure each actor in each stage of the email’s journey to sender to receiver can only see the information about the email as they need to see.</p>
<blockquote>
<div>Anyone monitoring the email would be able to see the size of the message but that&#8217;s about it</div>
<div>&#8211; Iain Thomson</p>
<div></div>
</div>
</blockquote>
<p>When an author sends an email they can see where it’s bound, the email server can’t the email server only can only decrypt the part of the message that contains the recipients email server. The Recipient e-mail server knows the destination server and the recipient but doesn’t know the sender so each actor can see only one hop before it and after it.</p>
<p>This relies on a federated key management system to handle the encryption layers as every actor in the DIME chain has to have its own Key pairs (a set of public and private keys) to encrypt and decrypt the required email portions it needs. Ladar Levison sees this to work in a DNS-like system with each organization that uses DIME being the authoritative source of the encryption keys for its servers and email addresses. Though specifically Levison settled for DNSSEC as the preferred method for holding a domain’s email trust anchor. This though runs into the problem of poor adoption which means that a Certificate authority signed TLS certificate would be required to validate the keys.</p>
<p>There’s an optional mode available wherein email servers transparently do the client’s email encryption for them in what’s called “trustful mode” and can either be a bridge for users to use until they have a client program that fully supports DIME. This gives email-hosting companies the potential to deploy DIME for hosted accounts without having to have mail client issues.</p>
<p>Levison plans on releasing Lavabit’s source code under an open source license after incorporating in the dark mail protocol into the Lavabit source code.</p>
<p>Issue with Darkmail would be backwards compatibility since it’s a completely new email protocol it will be incompatible with current email system. This will have to be bridged by darkmail gateways. Some darkmail providers would offer an email gateway to facilitate for a darkmail email to be sent out into the normal e-mail system using SMTP etc.</p>
<p>Darkmail offers flexible user-security with a basic level of encryption and security built into the protocol. Administrators setting up DIME can specify additional ciphers and encryption methods to deploy in order to secure the email and the DIME protocol would wrap it all in the baseline encryption that’s known to be secure.</p>
</div>
<span style="display:none"><a href="https://www.deepdotweb.com/tag/alliance/" rel="tag">alliance</a> <a href="https://www.deepdotweb.com/tag/darkmail/" rel="tag">darkmail</a></span> <span style="display:none" class="updated">2015-02-25</span>
<div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/zubairmuadh/" title="Posts by Zubair Muadh" rel="author">Zubair Muadh</a></strong></div>
</div>
</article>

