---
A Noob’s Guide to I2P-Bote
---
<article class="post-listing post-16456 post type-post status-publish format-standard has-post-thumbnail hentry  tag-guide tag-i2pbote tag-noobs">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/ciphas/" title="">Ciphas </a></span>
    <span>November 16, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/11/16/noobs-guide-i2p-bote/#comments">2 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    <p>As darknets go, some people may think of I2P as one of the more technically-oriented ones. For that reason, I think it deserves more tutorials!</p>
    <p>If you’ve already read our 2013 article <a href="https://www.deepdotweb.com/2013/12/30/full-guide-how-to-access-i2p-sites-use-themarketplace-i2p/">Full Guide: How to Access I2P Sites &amp; Use themarketplace.i2p</a>, then you at least have some idea how to access I2P.</p>
    <p>Therefore, I thought I2P-Bote, a messaging platform that operates over the I2P network, deserved a little attention.</p>
    <p><strong>Synchronous Email!</strong></p>
    <p><img class="wp-image-16457 aligncenter" src="/imgs/2016/11/word-image-29.png" srcset="/imgs/2016/11/word-image-29.png 800w, /imgs/2016/11/word-image-29-300x169.png 300w" sizes="(max-width: 800px) 100vw, 800px" /></p>
    <p>Does the term “asynchronous communication” ring a bell? In a nutshell, it means transmission of data with a time lag. Email and forum communications are two well-known examples.</p>
    <p>Unlike most email platforms, I2P-Bote is asynchronous, and built for privacy and anonymity. Obviously, it operates over the I2P network, and therefore it is quite a bit more secure and anonymous than a standard email provider (e.g. Gmail).</p>
    <p><strong>Tales from the Crypto</strong></p>
    <p>One of the major ways in which I2P-Bote is more secure than its email competitors is through its use of encryption. If you’re using a clearnet email provider, you would type in the sender’s address, which might look something like <a href="/cdn-cgi/l/email-protection#97faf6f3fff8e2e4f2f6e0d7faf6f3faf6fefbb9f4f8fa"><strong><span class="__cf_email__" data-cfemail="533e32373b3c2620363224133e32373e323a3f7d303c3e">[email&#160;protected]</span></strong></a>.</p>
    <p>I2P-Bote, on the other hand, uses cryptographic keys as destinations, which are generated via a cryptographic hash function. (For example, a 504-bit WPA key might look something like this: &gt;7%vC&amp;Nyq4$ve?1suA=&amp;79r-K39qa8s2WmA&#8221;40=I`5|y89F&lt;bIduU5z!i0{;OT-.) That’s not a real one, by the way.</p>
    <p>When you send a message to someone over I2P-Bote, the message is encrypted using their public key; clear-text messages are not sent over the system. While it is possible to decrypt the messages, this at least puts that extra step in the way of an attacker.</p>
    <p><img class="wp-image-16458 aligncenter" src="/imgs/2016/11/word-image-30.png" width="753" height="390" srcset="/imgs/2016/11/word-image-30.png 1101w, /imgs/2016/11/word-image-30-300x155.png 300w, /imgs/2016/11/word-image-30-1024x530.png 1024w" sizes="(max-width: 753px) 100vw, 753px" /></p>
    <p>Credit: Funker Bernd 2012</p>
    <p>I2P-Bote also cleans up the headers (which can reveal <em>a lot</em> of information about the sender), and encrypts any remaining information.</p>
    <p><strong>We Are Anonymous</strong></p>
    <p>I2P-Bote is also far more anonymous than any standard email provider. Why, you ask? I2P-based email providers operate over the I2P network, which already adds a degree of anonymity in and of itself.</p>
    <p>If you really want the full details on how it works, read their <a href="https://geti2p.net/en/docs/how/tech-intro">tech intro</a> on the official site. To sum it up, I2P uses <a href="http://www.webopedia.com/TERM/P/packet_switching.html">packet switching</a> to break up communications before they’re sent, which are “reassembled” when they arrive at their destination. It’s also serverless, which reduces the surface area that attackers can target.</p>
    <p>Believe it or not, setting up I2P-Bote is actually very easy. Once you’re connected to the I2P network, type <strong>http://127.0.0.1:7657/configclients</strong> into the URL bar, and then go down to the bottom of the page. Copy and paste this link into the plugin install box: <strong>http://tjgidoycrw6s3guetge3kvrvynppqjmvqsosmtbmgqasa6vmsf6a.b32.i2p/i2pbote.xpi2p</strong></p>
    <p>After you’ve done that, then click “Install Plugin.” As you might expect, it will take time to install, but when it’s finished, the plugin should appear on your Router Console under the name “Secure Mail.”</p>
    <p>Once the plugin is finished installing, you’ll need to create an identity (similar to how you would in Freenet). You can do this under the “Addresses” menu at left (see above screenshot).</p>
    <p>The public name that you generate here will be the name that shows up on all emails you send, unless you choose to designate the message as anonymous.</p>
    <p>As for encrypting your messages, you have four options:</p>
    <ul>
    <li>256-bit Elliptic Curve Cryptography (ECC)</li>
    <li>521-bit ECC</li>
    <li>2048-bit ElGamal</li>
    <li>NTRU-1087</li>
    </ul>
    <p>Which one you choose is somewhat a matter of personal preference, but 521-bit ECC is considered to be one of the strongest (though it’s also sometimes overkill). It may depend on what you’re trying to encrypt!</p>
    <p>Finally, after you’ve created your identity, go into “Settings,” where you can adjust your anonymity. One of the things you can tweak, for instance, is the amount of time between when I2P-Bote searches for new e-mail. In addition, you can add relays with a large delay-range (which also adds to the anonymity factor).</p>
    <p>If you’re completely new to all of this, it may seem a little complex at first, but play around with it and you’ll get the hang of it. The more people that use I2P and I2P-Bote, the better it will become.</p>
    <p>Or I suppose you could always do the “anonymous message with the cut-out letters” thing, but that takes a lot more effort, doesn’t it?</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/guide/" rel="tag">guide</a> <a href="https://www.deepdotweb.com/tag/i2pbote/" rel="tag">i2pbote</a> <a href="https://www.deepdotweb.com/tag/noobs/" rel="tag">noobs</a></span> <span style="display:none" class="updated">2016-11-16</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/ciphas/" title="Posts by Ciphas" rel="author">Ciphas</a></strong></div>
    
