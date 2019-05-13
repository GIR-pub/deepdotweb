---
Battle of the Secure Smartphones
---
<article class="post-listing post-16227 post type-post status-publish format-standard has-post-thumbnail hentry  tag-battle tag-secure tag-smartphones">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/ciphas/" title="">Ciphas </a></span>
    <span>November 2, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/11/02/battle-secure-smartphones/#comments">4 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    <p>Dark web users just <em>love</em> having their smartphone communications spied on, right? (Detect any sarcasm there?)</p>
    <p>While no internet-connected device is 100% secure, some definitely are more armored than others.  In the smartphone arena, several phones consistently rank among the best.</p>
    <p>To which ones might I be referring? The Kali Linux NetHunter 3.0, Copperhead OS, and Blackphone 2 are a few favorites. Obviously these devices can be used by more than just those who explore the dark web, but if you&#8217;re someone who does, a little protection can&#8217;t hurt, right?</p>
    <p><strong>Kali Linux NetHunter 3.0</strong></p>
    <p><img class="wp-image-16228 aligncenter" src="/imgs/2016/11/kali-nethunter-n10-2.png" alt="kali-nethunter-n10-2" srcset="/imgs/2016/11/kali-nethunter-n10-2.png 680w, /imgs/2016/11/kali-nethunter-n10-2-300x200.png 300w, /imgs/2016/11/kali-nethunter-n10-2-290x195.png 290w" sizes="(max-width: 680px) 100vw, 680px" /></p>
    <p>Those of you in the pen testing field already know the Kali Linux name. Given that it’s almost synonymous with security, I expected nothing less of the latest NetHunter distro.</p>
    <p>NetHunter was created as a joint effort between Kali community member &#8220;BinkyBear&#8221; and Offensive Security. Specifically, it&#8217;s compatible with Nexus devices, including Nexus 5, Nexus 6, Nexus 7, Nexus 9, Nexus 10, and OnePlusOne.</p>
    <p>NetHunter 3.0 supports the following attacks (and tools):</p>
    <ol>
    <li>Wireless 802.11 frame injection and AP mode support</li>
    <li><a href="https://www.tripwire.com/state-of-security/latest-security-news/usb-attacks-with-mobile-devices-using-kali-nethunter/">USB HID Keyboard Attacks</a></li>
    <li><a href="http://www.networkworld.com/article/3087484/security/say-hello-to-badusb-20-usb-man-in-the-middle-attack-proof-of-concept.html">BadUSB MITM Attacks</a></li>
    <li>Full Kali Linux toolset</li>
    <li>USB Y-cable support in the Nethunter kernel</li>
    <li>Software-defined radio support</li>
    </ol>
    <p>In addition, the NetHunter features many of the pentesting weapons that its desktop counterpart has in its arsenal, such as Aircrack-ng (a suite of tools to assess Wi-Fi network security); <a href="http://tools.kali.org/vulnerability-analysis/bbqsql">BBQSQL</a>, which simplifies blind SQL injection tests; and <a href="http://tools.kali.org/information-gathering/ghost-phisher">Ghost Phisher</a>, a wireless and Ethernet security auditing and attack software program.</p>
    <p>So, great, I have an armory of &#8220;attack&#8221; tools, but can the NetHunter defend itself? Of course!</p>
    <p>While it includes a number of tools for defensive purposes as well, one of its more impressive features is the ability to cause the  Linux Unified Key Setup (LUKS) to self-destruct, a.k.a. a &#8220;nuke option.&#8221; (This feature is available on its other platforms as well).</p>
    <p>The self-destruct process hasn&#8217;t officially been implemented yet, but if you&#8217;re already a Kali user and would like to try it out, there are more detailed instructions here: <a href="https://www.kali.org/tutorials/emergency-self-destruction-luks-kali/">Testing the LUKS Nuke Patch</a></p>
    <p>Beyond this, the same tools that can be used to simulate attacks against other systems could be used to find vulnerabilities on yours.</p>
    <p>As with the versions of Kali on other platforms, however, I <em>wouldn&#8217;t</em> recommend them to a beginner with Linux distros. It&#8217;s possible that it could either prove frustrating, or you might do something with it that you don&#8217;t intend. Its tools have a specific user base in mind.</p>
    <p>One possible security issue to note: if you’re using an older device (such as the Nexus 7) with Nethunter 3.0, it may have trouble encrypting the device.</p>
    <p>A collaborator named jmingov on Github suggested the following fix for this problem:</p>
    <p><img class="wp-image-16229 aligncenter" src="/imgs/2016/11/kalilinux_issue-png.png" alt="kalilinux_issue.png" srcset="/imgs/2016/11/kalilinux_issue-png.png 942w, /imgs/2016/11/kalilinux_issue-png-300x96.png 300w" sizes="(max-width: 942px) 100vw, 942px" /></p>
    <p>“Atm, the easiest way is to remove the chroot from Nethunter app, encrypt the device, and then reinstall the chroot.” (For the full conversation, see <a href="https://github.com/offensive-security/kali-nethunter/issues/343">GitHub: Kali NetHunter issues</a>.)</p>
    <p>Overall, however, it seems to be well protected.</p>
    <p><strong>Copperhead OS</strong></p>
    <p><img class="wp-image-16230 aligncenter" src="/imgs/2016/11/secure_android_phone-86fb917c460bbea15bf5dc43e74c3.png" alt="secure_android_phone-86fb917c460bbea15bf5dc43e74c3480" srcset="/imgs/2016/11/secure_android_phone-86fb917c460bbea15bf5dc43e74c3.png 442w, /imgs/2016/11/secure_android_phone-86fb917c460bbea15bf5dc43e74c3-300x281.png 300w" sizes="(max-width: 442px) 100vw, 442px" /></p>
    <p>Like the venomous snake that inspired its name, CopperheadOS is an Android operating system you don&#8217;t want to mess with.</p>
    <p>Though it isn&#8217;t necessarily designed for pentesting like the NetHunter, it features its fair share of security attributes as well. Want to know more? Here are just a few examples:</p>
    <ul>
    <li>Full Disk Encryption (FDE) at the filesystem layer securing all data with AES-256-XTS and all metadata with AES-256-CBC+XTS.</li>
    <li>Full verified boot for all firmware and partitions of the OS. Unverified partitions containing user data are wiped via a factory reset.</li>
    <li>App permission model allows ability to revoke permissions and supply false data</li>
    </ul>
    <p>CopperheadOS  also uses the Zygote service to launch apps using the fork and exec commands, as opposed to Android, which only uses fork. The main purpose of this change is to add buffer overflow protection.</p>
    <p>In addition, the system makes it simple to adjust security levels. A slider located under Settings-&gt;Security-&gt;Advanced enables you to balance performance speed with security. The slider starts at 50% by default, but can easily be changed when necessary. Besides using the slider, all of the security settings can be changed manually, if that’s your preference.</p>
    <p>Beyond these basic features, CopperheadOS offers:</p>
    <ul>
    <li><strong>Hardened allocator: </strong>CopperheadOS replaces the standard system allocator with a port of OpenBSD’s malloc implementation, i.e. it basically manages the memory.</li>
    <li><strong>Protection from zero-day exploits: </strong>It patches up many vulnerabilities and makes it more difficult for an attacker to gain access</li>
    <li><strong>Improved sandboxing and isolation for apps and services: </strong>A stricter set of policies guides the SELinux security engine, and apps are sandboxed according to <a href="https://wiki.mozilla.org/Security/Sandbox/Seccomp">seccomp-bpf</a>.</li>
    </ul>
    <p>This is only a very basic summary of the features, but more or less, CopperheadOS is saying, “Go ahead. Attack me. I dare you.”</p>
    <p>Despite its numerous protections, it is still possible that Copperhead may have security issues under certain circumstances.</p>
    <p>A user on Twitter recently asked about being able to install Open GApps onto his device, and CopperheadOS replied, “Sideloading stuff like opengapps compromises the security of the system by requiring an insecure recovery and no verified boot.”</p>
    <p>It sounds as though installing certain types of apps like this one can have unintended consequences for the security of the OS. It’s for this reason that the developers always recommend that you <em>always</em> use F-Droid to download apps.</p>
    <p><strong>Blackphone 2.0 </strong></p>
    <p><img class="wp-image-16231 aligncenter" src="/imgs/2016/11/angle-frontback_homescreen_v3-png.png" alt="Angle-frontBack_homescreen_v3.png" srcset="/imgs/2016/11/angle-frontback_homescreen_v3-png.png 759w, /imgs/2016/11/angle-frontback_homescreen_v3-png-223x300.png 223w" sizes="(max-width: 759px) 100vw, 759px" /></p>
    <p>You may already know the name Blackphone – like Kali Linux, its brand conjures images of <em>Mr. Robot</em>-like scenarios, where privacy is of the utmost importance.</p>
    <p>One of Blackphone 2’s basic features that offers protection right off the bat is its Security Center, which sits at the bottom-right of the home screen. In this area, you can configure how much access individual apps have to any of your data.</p>
    <p>The Security Center gives you the ability to seclude apps and services from one another, while still giving you an all-inclusive overview of your phone’s features.</p>
    <p>Beyond this, it also offers a feature called Spaces, which gives you the ability to build remote, secure areas within the system. It’s very much akin to the way that Qubes OS sandboxes its virtual machines so that they have limited access to one another.</p>
    <p>Yet another valuable tool is Blackphone’s Remote Wipe feature, which lets you power off your phone, kill specific apps, or even completely wipe the device (in case of theft or loss). You can set up these features through the <a href="https://manage.blackphone.ch/login/?next=/">Blackphone Remote Access</a> page. Of course, this can only be accessed with a passphrase, so as I always say, make sure it’s a strong passphrase, and one that you won’t forget!</p>
    <p>By the way, part of configuring the remote wipe process is giving your phone a name. I think I’d name mine “Nick Fury.”</p>
    <p>Unfortunately, like any OS, Blackphone 2.0 is not without its flaws. On January 6, 2016, ZDNet featured an article entitled <a href="http://www.zdnet.com/article/severe-silent-circle-blackphone-vulnerability-lets-hackers-take-over/">Severe Silent Circle Blackphone vulnerability lets hackers take over</a>, in which they explained that there was a socket left open on Blackphone 1 that’s also used by SELinux on Android.</p>
    <p>Specifically, they found certain apps that interact with said socket, in particular agps_daemon, which has, as they put it, “…more elevated privileges than a normal shell/app user since it is a system/radio user.” It appears that they’re still searching for a solution to this problem.</p>
    <p>That aside, the Blackphone 2, for the most part, is still a pretty hardened device, and has stronger defenses than most phones of its type.</p>
    <p><strong>You Blew My Cover!</strong></p>
    <p>As with any high-security technology, these phones (and the accompanying OS’s) may take some getting used to. Plus, in spite of their numerous security features, the user has to take steps to make sure that the private info inside remains just that…private.</p>
    <p>That being said, I’d recommend them to any average citizen who places a high value on confidentiality. And maybe to anyone who likes a “vodka martini, shaken, not stirred.”</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/battle/" rel="tag">battle</a> <a href="https://www.deepdotweb.com/tag/secure/" rel="tag">secure</a> <a href="https://www.deepdotweb.com/tag/smartphones/" rel="tag">smartphones</a></span> <span style="display:none" class="updated">2016-11-02</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/ciphas/" title="Posts by Ciphas" rel="author">Ciphas</a></strong></div>
    
