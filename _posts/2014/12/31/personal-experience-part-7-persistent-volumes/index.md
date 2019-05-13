---
Personal Experience: Part 7 – Persistent Volumes
---
<article class="post-listing post-8087 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-experience tag-experiencetag tag-part tag-persistent tag-personal tag-volumes">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/josephmeehan/" title="">Joseph Meehan </a></span>
    <span>December 31, 2014</span>
    
    <span><a href="https://www.deepdotweb.com/2014/12/31/personal-experience-part-7-persistent-volumes/#comments">1 Comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p><em>This a post in series of posts describing a personal experience from learning about the DNM’s to becoming a vendor – all the parts of this series will be available to here: <a href="http://www.deepdotweb.com/tag/ExperienceTag/">ExperienceTag</a></em></p>
    <p><a title="Personal Experience: Part 2 – Tails" href="http://www.deepdotweb.com/2014/10/06/personal-experience-part-2-tails/">TAILS</a> is a versatile piece of software with many features and uses. It&#8217;s hard to imagine all of the functionality of a completely anonymous operating system being packed into a tiny thumbdrive, but the developers of TAILS have done it. One thing <a title="Simple TAILS Installation" href="http://www.deepdotweb.com/2014/06/14/simple-tails-installation/">TAILS</a> can lack is a certain persistence between work sessions. For instance, in Claws mail you have to enter in your email account information every time you boot up.<br />
    TAILS does have a solution for this though. You can set up an encrypted volume on your thumbdrive. TAILS will use this space to store sensitive information that is useful to have stored – email account information, encryption keys, software configurations, etc. You can even download and install software packages to the encrypted volume so you don&#8217;t have to install them every time you boot the OS.</p>
    <p>The TAILS documentation gives some security concerns to consider when you set up a persistent volume to store some of your information. Installing additional software and plug-ins can change the way TAILS works and potentially interfere with the anonymity of the OS. Creating configurations for software that overwrite the defaults can do the same. The documentation also notes the persistent volume is encrypted but is not hidden from view.</p>
    <p>This process must be done on a thumbdrive by the TAILS Installer within a running TAILS environment, so you have to have TAILS installed on a media and have another media to which you can install. The Tails Installer is easy to use and ran for me without a hitch. I installed it to another thumbdrive and booted it up.</p>
    <p>After TAILS booted all the way up I found the persistent volume configuration application in the application menu under System Tools. First I was asked to create a passphrase. I entered the passphrase previously created through Diceware. I clicked Create and the application got to work creating the volume.</p>
    <p>Once it was done I was presented with a menu of options for what I will use the persistent volume for. There were a number of options to choose from, but I was interested in only a couple for now. I wanted to be able to save my PGP keys, some personal documents, and my email credentials for Claws. Once I made my selections it was as simple as that. I created some PGP keys. I entered my email account information into Claws. I made a couple of documents and saved them to my personal folder. I restarted my machine and in the TAILS Greeter I chose to enable the persistent volume for this session. TAILS kept my PGP keys were ready to go and Claws automatically loaded my email. My documents were right where I had left them. It is not necessary to enable the persistent volume every time you start TAILS. If your tasks in TAILS don&#8217;t include anything you need your persistent volume for you can leave it unactivated. In fact, the documentation recommends using the persistent volume as little as possible to minimize security threats.</p>
    <p>The persistent volume option that TAILS offers is not necessary but it can be a very convenient tool. Configuring it properly to meet your needs can make using TAILS a more efficient and customized experience.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/experience/" rel="tag">experience</a> <a href="https://www.deepdotweb.com/tag/experiencetag/" rel="tag">ExperienceTag</a> <a href="https://www.deepdotweb.com/tag/part/" rel="tag">part</a> <a href="https://www.deepdotweb.com/tag/persistent/" rel="tag">persistent</a> <a href="https://www.deepdotweb.com/tag/personal/" rel="tag">personal</a> <a href="https://www.deepdotweb.com/tag/volumes/" rel="tag">volumes</a></span> <span style="display:none" class="updated">2014-12-31</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/josephmeehan/" title="Posts by Joseph Meehan" rel="author">Joseph Meehan</a></strong></div>
    </div>
</article>

