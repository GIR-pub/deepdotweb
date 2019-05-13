---
Does Qubes OS Has A Leak Hole ?
---
<article class="post-listing post-13433 post type-post status-publish format-standard has-post-thumbnail hentry  tag-hole tag-leak tag-os tag-qube">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/michaelatobraaboagye/" title="">Michael Atobra Aboagye </a></span>
    <span>March 12, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/03/12/does-qube-os-has-a-leak-hole/#comments">10 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <div class="wp-socializer-buttons clearfix">
    <span class="wpsr-btn">
    
    <div class="fb-like" data-href="https://www.deepdotweb.com/2016/03/12/does-qube-os-has-a-leak-hole/" data-share="false" data-layout="button_count" data-show-faces="0" data-action="like" data-colorscheme="light"></div>
    
    </span>
    <span class="wpsr-btn">
    
    <a href="http://twitter.com/share" class="twitter-share-button" data-count="horizontal" data-lang="en" data-url="https://www.deepdotweb.com/2016/03/12/does-qube-os-has-a-leak-hole/" data-text="Does Qubes OS Has A Leak Hole ? - "></a>
    
    </span>
    <span class="wpsr-btn">
    
    <div class="g-plusone" data-size="medium" data-href="https://www.deepdotweb.com/2016/03/12/does-qube-os-has-a-leak-hole/"></div>
    
    </span>
    <span class="wpsr-btn">
    
    <script type="IN/Share" data-url="https://www.deepdotweb.com/2016/03/12/does-qube-os-has-a-leak-hole/" data-counter="right"></script>
    
    </span>
    </div><span class="wpsr_floatbts_anchor" data-offset="25"></span><p>Another ideal option supported by opsec  experts  against cyber- attacks, and to prevent loss of data is Sandboxing. But is sandboxing enough to deter data intruders from pilfering massive data or is it another hyperbole paraded as a truth?</p>
    <p>The truth above all else is : if encryption or cryptographic methods have leak holes, what’s the essence of  domain sandboxing ?  Don’t you think sandboxing depends on cryptographic  method to prevent domain A from accessing the data of domain B?</p>
    <p>Sandboxing can be defined as a partition of domains or separation of domains from each other. Logically, it is similar to the block of cells at Guantanamo Bay Detention Camp.</p>
    <p>Technically, although Qubes  is not the only operating system to support virtualization, it is  the only or first operating system with domains allocated with special functions.  Qubes sandboxing is widely different from  day –to –day virtualization implemented by software vendors.</p>
    <p>Qubes’ virtualization is based on Xen, an open source hypervisor model. It is touted as the most preferred among others.</p>
    <p><strong><em>Hypervisor is simply a virtual machine monitor which enables operating system to host more than one virtual machines on a host machine. It is known as Virtualization. Qubes OS is designed to provide security by isolation . </em></strong></p>
    <p>Qubes OS has the following functional virtual domains for a user :</p>
    <p><strong>Dom0</strong> –</p>
    <p>It is the most privileged domain among other domains and also the most sensitive. It has direct access to the host hardware . Because it is sensitive, it is isolated from other domains especially the Network Vm . Dom0 hosts the GUI domain and controls the graphics device, as well as input devices, such as keyboard and mouse. The GUI domain runs the X server, which displays the user desktop, and the window manager, which allows the user to start and stop the applications and manipulate their windows.</p>
    <p><strong>App Vm</strong>  &#8211;</p>
    <p>AppVMs are the virtual machines used for hosting user applications, such as a web browser, an e-mail client or a text editor. For security purpose, these applications can be grouped in different domains, such as “personal”, “work”, “shopping”, “bank”, etc. The security domains are implemented separately. Virtual Machines (VMs), thus being isolated from each other as if they were executing on different machines.</p>
    <p><strong>Network Vm</strong> –</p>
    <p>The network mechanism is the most exposed to security attacks. This is why it is isolated in a separate, unprivileged virtual machine, called the Network Domain. An additional proxy virtual machine is used for advanced networking configuration .</p>
    <p><strong>Storage Domain</strong> –</p>
    <p>Disk space is saved by virtue of various virtual machines (VM) sharing the same root file system in a read-only mode. Separate disk storage is only used for userʼs directory and per-VM settings. This allows software installation and updates to be centralized. Of course, some software can be installed only on a specific VM. Encryption is used to protect the file systems, so that the storage domain cannot read confidential data owned by other domains.</p>
    <p>Among the domains or Vm’s on Qubes OS , the Network Vm is touted as the most viable to attack vectors  . Also within the App Vm, a user is likely to be attacked by viruses, trojans, keyloggers, and other malicious softwares .  Thus, it is the chief reason why the developers of Qubes OS decided to increase the proximity between  the Dom0 and the Network Vm.</p>
    <p>So it seems the developers of Qubes OS have in mind that the best possible option to protect the Dom0 from keyloggers or trojans is to separate it from the App Vm. Therefore, we can assert (that) it is at least safe to operate on Qubes but not entirely .</p>
    <p>According to technical documentation concerning Qubes structure, domains are separated from each other  via encryption . Like the Dom0, the storage domain is literally protected from other domains via encryption to prevent viruses in other domains [ such as Network Vm ] from penetrating into each other.</p>
    <p>If the storage domain were to be part or closely connected to other domains, then the essence of  security by isolation does not practically implement its intention to secure domains from each other .</p>
    <p>However, those in the opsec industry should [by now] be aware of  how connected devices [ or even separated devices like a wireless keyboard and computer] are susceptible to malicious agents.</p>
    <p>Even before I move on to how hackers can manage to detonate Qubes intention to protect domains by isolation, lets ponder over the following questions :</p>
    <p>Why should Joanna allow users to set domain policies on their own instead of implementing a wizard tool to automate settings ? Or perhaps manual configuration is better than wizard configuration ?</p>
    <p>Is the encryption between the storage domain and the others resilient enough without hidden bugs ?</p>
    <p>Is the Dom0 completely protected from Rootkits ?</p>
    <p>How does the encryption mode between domains prevent viruses from moving the Network Vm to Storage Vm ?</p>
    <p><strong>The  Problem With Qubes Mode of Security  </strong></p>
    <p>Honestly, I don’t have any problem with Qubes OS.  But if Joanna confirmed it is impossible to avoid bugs, then why should she assure users that Qubes OS is capable of sandboxing trojans and malicious software from domains on Qubes OS.</p>
    <p>In spite of Joanna’s opinion, there are other  two  areas  and techniques which could detonate isolation method being implemented  by Qubes OS developers .</p>
    <p>Seemingly, Qubes OS depends on a backup system to prevent huge mass of data.  In default, the backup system relies on weak key derivation scheme . So it is recommended that users select a high-entropy passphrase for use with Qubes backups  .</p>
    <p>But in all honesty, I have yet to find out if the backup system is a better option of avoiding heavy loss of data. Because according to Qubes security team,  a user  can send  backup documents to the App Vm. My concern here is : Does the user knows whether the App Vm is void of worms or viruses ?</p>
    <p><strong>First Area Of Vulnerability</strong>   :  According to Joanna,  users are allowed to configure domain settings on their own.  Of course not  all users are familiar with technical settings. In addition, humans are prone to mistakes ; so we should expect hackers to be aware of manual security policies , take advantage of  haphazard configuration and eventually inject viruses and trojans into users domain .</p>
    <p>Therefore hackers may count on human mistakes to compromise users domain. So in spite of the isolation method implemented by Qubes, users’ unseen mistakes may act as attack vectors or ‘leak holes’ which could compromise Qubes in-depth security .</p>
    <p><strong>Second Area Of Vulnerability</strong> :  Qubes allows users not to ‘send’ or ‘transport’ but to copy and paste files and folders . Let’s assume users download a file or a program from a ‘phished’ website ( designated as an https website ) unknowingly . Later, the file or program downloaded from the phished website is copied from the App Vm to the Storage Vm.</p>
    <p>The storage Vm is encrypted from the Network Vm to prevent replication of malwares ( i.e virus ) .  Can the encryption method employed to prevent malicious software in the programs or folders on the App Vm from attaching itself to the Storage Vm ?</p>
    <p>Nevertheless, we should not be surprised to hear of a new zero-day attack on Qubes OS . The complexity of Qubes OS is not invulnerable to compromise. But we can count on Qubes OS as the most reliable than other OSes.</p>
    <h3>Share and Enjoy</h3>
    
    <div class="wp-socializer 32px">
    <ul class="wp-socializer-opacity columns-no">
    <li><a href="http://www.facebook.com/share.php?u=https%3A%2F%2Fwww.deepdotweb.com%2F2016%2F03%2F12%2Fdoes-qube-os-has-a-leak-hole%2F&amp;t=Does+Qubes+OS+Has+A+Leak+Hole+%3F" title="Share this on Facebook" target="_blank" rel="nofollow"><img src="https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="Facebook" style="width:32px; height:32px; background: transparent url(https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -330px; border:0;"/></a></li>
    <li><a href="http://twitter.com/home?status=Does+Qubes+OS+Has+A+Leak+Hole+%3F%20-%20https%3A%2F%2Fwww.deepdotweb.com%2F2016%2F03%2F12%2Fdoes-qube-os-has-a-leak-hole%2F%20" title="Tweet this !" target="_blank" rel="nofollow"><img src="https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="Twitter" style="width:32px; height:32px; background: transparent url(https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -1386px; border:0;"/></a></li>
    <li><a href="http://delicious.com/post?url=https%3A%2F%2Fwww.deepdotweb.com%2F2016%2F03%2F12%2Fdoes-qube-os-has-a-leak-hole%2F&amp;title=Does+Qubes+OS+Has+A+Leak+Hole+%3F&amp;notes=Another+ideal+option+supported+by+opsec%C2%A0+experts%C2%A0+against+cyber-+attacks%2C+and+to+prevent+loss+of+data+is+Sandboxing.+But+is+sandboxing+enough+to+deter+data+intruders+from+pilfering+massive+data+or+is+it+another+hyperbole+paraded+as+a+truth%3F%0D%0A%0D%0AThe" title="Post this on Delicious" target="_blank" rel="nofollow"><img src="https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="Delicious" style="width:32px; height:32px; background: transparent url(https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -132px; border:0;"/></a></li>
    <li><a href="http://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A%2F%2Fwww.deepdotweb.com%2F2016%2F03%2F12%2Fdoes-qube-os-has-a-leak-hole%2F&amp;title=Does+Qubes+OS+Has+A+Leak+Hole+%3F&amp;source=Deep+Dot+Web+-+Surfacing+The+News+From+The+DeepWeb&amp;summary=Another+ideal+option+supported+by+opsec%C2%A0+experts%C2%A0+against+cyber-+attacks%2C+and+to+prevent+loss+of+data+is+Sandboxing.+But+is+sandboxing+enough+to+deter+data+intruders+from+pilfering+massive+data+or+is+it+another+hyperbole+paraded+as+a+truth%3F%0D%0A%0D%0AThe" title="Share this on LinkedIn" target="_blank" rel="nofollow"><img src="https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="LinkedIn" style="width:32px; height:32px; background: transparent url(https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -693px; border:0;"/></a></li>
    <li><a href="http://www.stumbleupon.com/submit?url=https%3A%2F%2Fwww.deepdotweb.com%2F2016%2F03%2F12%2Fdoes-qube-os-has-a-leak-hole%2F&amp;title=Does+Qubes+OS+Has+A+Leak+Hole+%3F" title="Submit this to StumbleUpon" target="_blank" rel="nofollow"><img src="https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="StumbleUpon" style="width:32px; height:32px; background: transparent url(https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -1287px; border:0;"/></a></li>
    <li><a href="https://www.deepdotweb.com/2016/03/12/does-qube-os-has-a-leak-hole/" onclick="addBookmark(event);" title="Add to favorites" target="_blank" rel="nofollow"><img src="https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="Add to favorites" style="width:32px; height:32px; background: transparent url(https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -0px; border:0;"/></a></li>
    <li><a href="/cdn-cgi/l/email-protection#7b440f14465d080e19111e180f463f141e08502a0e191e0850342850331a08503a50371e1a10503314171e505e483d5d19141f02463a15140f131e0950121f1e1a17X+option+supported+by+opsec%C2%A0+experts%C2%A0+against+cyber-+attacks%2C+and+to+prevent+loss+of+data+is+Sandboxing.+But+is+sandboxing+enough+to+deter+data+intruders+from+pilfering+massive+data+or+is+it+another+hyperbole+paraded+as+a+truth%3F%0D%0A%0D%0AThe%20-%20https://www.deepdotweb.com/2016/03/12/does-qube-os-has-a-leak-hole/" title="Email this" target="_blank" rel="nofollow"><img src="https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="Email" style="width:32px; height:32px; background: transparent url(https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -297px; border:0;"/></a></li>
    <li><a href="https://www.deepdotweb.com/feed/rss/" title="Subscribe to RSS" target="_blank" rel="nofollow"><img src="https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-mask-32px.gif" alt="RSS" style="width:32px; height:32px; background: transparent url(https://www.deepdotweb.com/wp-content/plugins/wp-socializer/public/social-icons/wp-socializer-sprite-32px.png?v1) no-repeat; background-position:0px -1221px; border:0;"/></a></li>
    </ul>
    <div class="wp-socializer-clearer"></div></div>
    
    </div>
    <a href="https://www.deepdotweb.com/tag/hole/" rel="tag">hole</a> <a href="https://www.deepdotweb.com/tag/leak/" rel="tag">leak</a> <a href="https://www.deepdotweb.com/tag/os/" rel="tag">os</a> <a href="https://www.deepdotweb.com/tag/qube/" rel="tag">qube</a></span> <span style="display:none" class="updated">2016-03-12</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/michaelatobraaboagye/" title="Posts by Michael Atobra Aboagye" rel="author">Michael Atobra Aboagye</a></strong></div>
    </div>
</article>

