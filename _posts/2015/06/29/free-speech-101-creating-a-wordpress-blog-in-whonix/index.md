---
Free Speech 101: Creating a WordPress Blog in Whonix
---
<article class="post-listing post-9376 post type-post status-publish format-standard has-post-thumbnail hentry  tag-1941 tag-blog tag-creating tag-free tag-speech tag-whonix tag-wordpress">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/politech/" title="">Politech </a></span>
    <span>June 29, 2015</span>
    
    <span><a href="https://www.deepdotweb.com/2015/06/29/free-speech-101-creating-a-wordpress-blog-in-whonix/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>With this guide, I hope to enable anyone with access to a computer to set up their own place to speak freely on the internet. The ability to publish anonymously is sadly becoming an increasingly important one – <em>the Guardian, </em>for example, <a href="http://www.theregister.co.uk/2014/06/03/revealed_beyond_top_secret_british_intelligence_middleeast_internet_spy_base">was pressured</a> by the UK government into not revealing certain details from the Snowden documents; the persecution of WikiLeaks is ongoing with Julian Assange still trapped in the Ecuadorian embassy in London; and in Britain, Russia Today is currently <a href="https://firstlook.org/theintercept/2015/03/02/uk-media-regulator-threatens-rt-bias-airing-anti-western-views/">being investigated</a> for “bias” by OFCOM. The list of these cases in supposedly free countries could go on. But if journalism and other forms of expression crucial to functioning democracies occurs anonymously, it becomes harder to suppress as it is no longer simple for governments to find the right door to kick down.</p>
    <p>Before we begin, I&#8217;ll give a disclaimer: if your quality of life depends on the security of your hidden service, you should seek a more advanced guide than this. This is a beginner-friendly guide. There are more secure options than WordPress, for instance Drupal or simply static HTML, but WordPress is a good choice for a beginner who wants to regularly update their site using a GUI.</p>
    <p><a href="/imgs/2015/03/wpscreen.jpeg"><img class="aligncenter  wp-image-9381" src="/imgs/2015/03/wpscreen.jpeg" alt="wpscreen" width="927" height="508" srcset="/imgs/2015/03/wpscreen.jpeg 1920w, /imgs/2015/03/wpscreen-300x164.jpeg 300w, /imgs/2015/03/wpscreen-1024x561.jpeg 1024w" sizes="(max-width: 927px) 100vw, 927px"/></a></p>
    <p>Similarly, if you are reading this in the hope of setting up a criminal enterprise, know that the protection of Tor will only buy you time. Hidden services are not immune to investigation. Moreover, please do not give anonymity a bad name by abusing hidden services.</p>
    <p>The following setup uses <a href="https://www.whonix.org/">Whonix</a>, a virtual operating system for use with <a href="https://www.virtualbox.org/">Oracle VirtualBox</a>. It comes in two parts: the Whonix Gateway and the Whonix Workstation. The sole purpose of the Whonix Gateway is controlling Tor and forcing all traffic over the Tor network. The Whonix Workstation is where most of our work will be done and all its traffic is transparently proxied through the Whonix Gateway. This is done to prevent leaks.</p>
    <p>This means that if someone wants to de-anonymize your site, they would first have to compromise the Workstation with malware, and from there engineer a virtual machine escape, infecting your host operating system. The attacker could then connect to a server outside of Tor, revealing your real IP address. This is quite hard, but there is a reference to exploiting virtual machines in a <a href="http://ac4jrkjk4ialqkoh.onion/wp-content/uploads/2015/01/media-35686.pdf">Snowden document</a>, so carefully gauge the sophistication of your adversary when deciding if this guide is appropriate for you.</p>
    <p><strong>Getting Started</strong></p>
    <p>VirtualBox is available for Windows, Mac OS X, Linux, Solaris and FreeBSD. I recommend avoiding Windows and Mac OS because *NIX-based OSes are more secure, but the choice is yours. Make sure to verify the Whonix images before installing them, to make sure they haven&#8217;t been corrupted or maliciously tampered with. Whonix has several guides on how to do that according to your chosen OS <a href="https://www.whonix.org/wiki/Download#Verify_the_Whonix_images">here</a>.</p>
    <p>It would also be wise to encrypt your hard drive and harden the security of your host OS. That is too much to go into here, but if you search “hardening &lt;your OS&gt;” you will find many guides. If you want extra protection against virtual machine escapes, you might consider configuring your firewall to connect solely through a non-logging VPN. This will make it harder for an attacker to find out your real IP address if you are compromised, but bear in mind that VPNs offer much weaker anonymity than Tor.</p>
    <p>Once you have installed VirtualBox and are satisfied that your machine is sufficiently secure, you are ready to install Whonix. Simply click File&gt;Import Appliance in VirtualBox and import both the Whonix Gateway and Workstation. When activated, the Whonix VMs will take you through a guided installation process. You can accept everything as is.</p>
    <p>The default root and user password is “changeme” and you should do that immediately. Enter:</p>
    <div id="crayon-59628f9d37390608169374" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    su</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59628f9d37390608169374-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59628f9d37390608169374-1"><span class="crayon-v">su</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    in the Konsole and type “changeme”. Now you are root, type:</p>
    <div id="crayon-59628f9d3739a977014362" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    passwd</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59628f9d3739a977014362-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59628f9d3739a977014362-1"><span class="crayon-v">passwd</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    and enter your new, strong UNIX password. Now enter:</p>
    <div id="crayon-59628f9d3739e074530242" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    passwd user</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59628f9d3739e074530242-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59628f9d3739e074530242-1"><span class="crayon-e">passwd </span><span class="crayon-v">user</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    and repeat. You have to do this in both the Gateway and Workstation.</p>
    <p>You should also update Whonix as soon as possible by typing:</p>
    <div id="crayon-59628f9d373a2508706933" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo apt-get update &amp;amp;&amp;amp; sudo apt-get dist-upgrade</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59628f9d373a2508706933-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59628f9d373a2508706933-1"><span class="crayon-e">sudo </span><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-v">update</span><span class="crayon-h"> </span><span class="crayon-o">&amp;</span><span class="crayon-v">amp</span><span class="crayon-sy">;</span><span class="crayon-o">&amp;</span><span class="crayon-v">amp</span><span class="crayon-sy">;</span><span class="crayon-h"> </span><span class="crayon-e">sudo </span><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-v">dist</span><span class="crayon-o">-</span><span class="crayon-v">upgrade</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    in both VMs. You may be warned that the packages can&#8217;t be verified. If that happens, see Whonix&#8217;s <a href="https://www.whonix.org/wiki/Download#KEYEXPIRED_Error">guide</a> for updating the signing key. Do not update without verification as it is a needless security risk.</p>
    <p>Now we are ready to install the site&#8217;s components.</p>
    <p><strong>Setting Up WordPress</strong></p>
    <p>From the Konsole, enter:</p>
    <div id="crayon-59628f9d373a6257523469" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo apt-get install libapache2-mod-php5 php5 mysql-server</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59628f9d373a6257523469-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59628f9d373a6257523469-1"><span class="crayon-e">sudo </span><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-e">install </span><span class="crayon-v">libapache2</span><span class="crayon-o">-</span><span class="crayon-v">mod</span><span class="crayon-o">-</span><span class="crayon-e">php5 </span><span class="crayon-e">php5 </span><span class="crayon-v">mysql</span><span class="crayon-o">-</span><span class="crayon-v">server</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    . Once they&#8217;re installed, you should be prompted to choose a root password for MySQL. Pick something strong and remember it. Once done, enter:</p>
    <div id="crayon-59628f9d373a9967618403" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    mysql_secure_installation</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59628f9d373a9967618403-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59628f9d373a9967618403-1"><span class="crayon-v">mysql_secure_installation</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    to remove some of the vulnerabilities that come with a default MySQL installation. Enter your root password, and when asked if you want to change the root password enter “n” if you chose a good one. Choose “y” for the rest of the questions.</p>
    <p>Now is a good time to make your web server accessible in the Whonix Gateway. Open “Tor Examples” on the desktop and find the hidden services section. Copy:</p>
    <div id="crayon-59628f9d373ad901941856" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    HiddenServiceDir /var/lib/tor/webserver
    
    HiddenServicePort 80 10.152.152.11:80</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59628f9d373ad901941856-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-59628f9d373ad901941856-2">2</div><div class="crayon-num" data-line="crayon-59628f9d373ad901941856-3">3</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59628f9d373ad901941856-1"><span class="crayon-v">HiddenServiceDir</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-t">var</span><span class="crayon-o">/</span><span class="crayon-v">lib</span><span class="crayon-o">/</span><span class="crayon-v">tor</span><span class="crayon-o">/</span><span class="crayon-e">webserver</span></div><div class="crayon-line crayon-striped-line" id="crayon-59628f9d373ad901941856-2">&nbsp;</div><div class="crayon-line" id="crayon-59628f9d373ad901941856-3"><span class="crayon-i">HiddenServicePort</span><span class="crayon-h"> </span><span class="crayon-cn">80</span><span class="crayon-h"> </span><span class="crayon-cn">10.152.152.11</span><span class="crayon-o">:</span><span class="crayon-cn">80</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    and paste it into the torrc. You can access the torrc by opening “Tor User Config” on the desktop. Restart Tor to enable the new settings. There are also instructions in “Tor Examples” on how to find out your new host name: simply enter:</p>
    <div id="crayon-59628f9d373b1586864858" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo cat /var/lib/tor/webserver/hostname</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59628f9d373b1586864858-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59628f9d373b1586864858-1"><span class="crayon-e">sudo </span><span class="crayon-v">cat</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-t">var</span><span class="crayon-o">/</span><span class="crayon-v">lib</span><span class="crayon-o">/</span><span class="crayon-v">tor</span><span class="crayon-o">/</span><span class="crayon-v">webserver</span><span class="crayon-o">/</span><span class="crayon-v">hostname</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    Try visiting it in Tor Browser – if you see the Apache “It works” message, congratulations! You&#8217;ll need your hostname for the next step: installing WordPress.</p>
    <p>Simply type:</p>
    <div id="crayon-59628f9d373b4129105142" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo apt-get install wordpress</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59628f9d373b4129105142-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59628f9d373b4129105142-1"><span class="crayon-e">sudo </span><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-e">install </span><span class="crayon-v">wordpress</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    Since Whonix is based on Debian 7, any guide that works for Debian should also work for Whonix. The Debian wiki&#8217;s extensive <a href="https://wiki.debian.org/WordPress">guide</a> to WordPress is very useful here.</p>
    <p>We&#8217;ve already done the first step of the Debian wiki&#8217;s guide – we can skip to “Create a Site”. Follow the default instructions given, but when copying from boxes containing line numbers, make sure to remove them; they will break the config files if you don&#8217;t. You will also need to change some permissions using “chmod” for some steps of the guide to work. I&#8217;ll cover that here.</p>
    <p>In order for:</p>
    <div id="crayon-59628f9d373b8372520134" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo cat ~/wp.sql | mysql –defaults-extra-file=/etc/mysql/debian.cnf</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59628f9d373b8372520134-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59628f9d373b8372520134-1"><span class="crayon-e">sudo </span><span class="crayon-v">cat</span><span class="crayon-h"> </span><span class="crayon-o">~</span><span class="crayon-o">/</span><span class="crayon-v">wp</span><span class="crayon-sy">.</span><span class="crayon-v">sql</span><span class="crayon-h"> </span><span class="crayon-o">|</span><span class="crayon-h"> </span><span class="crayon-i">mysql</span><span class="crayon-h"> </span>–<span class="crayon-v">defaults</span><span class="crayon-o">-</span><span class="crayon-v">extra</span><span class="crayon-o">-</span><span class="crayon-v">file</span><span class="crayon-o">=</span><span class="crayon-o">/</span><span class="crayon-v">etc</span><span class="crayon-o">/</span><span class="crayon-v">mysql</span><span class="crayon-o">/</span><span class="crayon-v">debian</span><span class="crayon-sy">.</span><span class="crayon-v">cnf</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    to work you will need to enter:</p>
    <div id="crayon-59628f9d373bb891014068" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo chmod 755 /etc/mysql/debian.cnf</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59628f9d373bb891014068-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59628f9d373bb891014068-1"><span class="crayon-e">sudo </span><span class="crayon-i">chmod</span><span class="crayon-h"> </span><span class="crayon-cn">755</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">etc</span><span class="crayon-o">/</span><span class="crayon-v">mysql</span><span class="crayon-o">/</span><span class="crayon-v">debian</span><span class="crayon-sy">.</span><span class="crayon-v">cnf</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    beforehand, and then change it to:</p>
    <div id="crayon-59628f9d373be153094963" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo chmod 100 /etc/mysql/debian.cnf</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59628f9d373be153094963-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59628f9d373be153094963-1"><span class="crayon-e">sudo </span><span class="crayon-i">chmod</span><span class="crayon-h"> </span><span class="crayon-cn">100</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">etc</span><span class="crayon-o">/</span><span class="crayon-v">mysql</span><span class="crayon-o">/</span><span class="crayon-v">debian</span><span class="crayon-sy">.</span><span class="crayon-v">cnf</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    afterwards. Note that “wp.sql” contains your MySQL password – it is therefore a good idea to lock it down afterwards using</p>
    <div id="crayon-59628f9d373c2411868072" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo chmod 100 ./wp.sql</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59628f9d373c2411868072-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59628f9d373c2411868072-1"><span class="crayon-e">sudo </span><span class="crayon-i">chmod</span><span class="crayon-h"> </span><span class="crayon-cn">100</span><span class="crayon-h"> </span><span class="crayon-sy">.</span><span class="crayon-o">/</span><span class="crayon-v">wp</span><span class="crayon-sy">.</span><span class="crayon-v">sql</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    in case the virtual machine is compromised.</p>
    <p>Now you have to copy the contents of /usr/share/wordpress to /var/www and delete the existing “index.html”. Again, you may have to change some permissions for it to work. This time enter:</p>
    <div id="crayon-59628f9d373c5298877462" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo chmod 777 -R /var/www</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59628f9d373c5298877462-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59628f9d373c5298877462-1"><span class="crayon-e">sudo </span><span class="crayon-i">chmod</span><span class="crayon-h"> </span><span class="crayon-cn">777</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-v">R</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-t">var</span><span class="crayon-o">/</span><span class="crayon-v">www</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    before copying and then change it to 755 afterwards.</p>
    <p>Now navigate to your site&#8217;s homepage in Tor Browser once again. If all went to plan, you&#8217;ll see the WordPress installation page. This section is self-explanatory. Once it&#8217;s installed, you&#8217;ll have a working WordPress site, and you can log in at &lt;your site&gt;.onion/wp-login.php. However the work isn&#8217;t done yet.</p>
    <p><strong>Maintaining and Securing WordPress</strong></p>
    <p>By default, WordPress fetches content from the non-anonymous internet. This is a highly undesirable quality for a hidden service, so let&#8217;s disable it to make the site more secure and private. In the Whonix Workstation, go to the page for the WordPress plugin <a href="https://wordpress.org/plugins/disable-google-fonts/">Disable Google Fonts</a>. Download the latest version and extract it. Copy the resulting folder into /var/lib/wordpress/wp-content/plugins. Once again, you&#8217;ll probably have to change permissions:</p>
    <div id="crayon-59628f9d373ca064890915" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo chmod 777 -R /var/lib/wordpress/wp-content/plugins</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59628f9d373ca064890915-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59628f9d373ca064890915-1"><span class="crayon-e">sudo </span><span class="crayon-i">chmod</span><span class="crayon-h"> </span><span class="crayon-cn">777</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-v">R</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-t">var</span><span class="crayon-o">/</span><span class="crayon-v">lib</span><span class="crayon-o">/</span><span class="crayon-v">wordpress</span><span class="crayon-o">/</span><span class="crayon-v">wp</span><span class="crayon-o">-</span><span class="crayon-v">content</span><span class="crayon-o">/</span><span class="crayon-v">plugins</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    and once you&#8217;re done:</p>
    <div id="crayon-59628f9d373cf657403535" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo chmod 755 -R /var/lib/wordpress/wp-content/plugins</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59628f9d373cf657403535-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59628f9d373cf657403535-1"><span class="crayon-e">sudo </span><span class="crayon-i">chmod</span><span class="crayon-h"> </span><span class="crayon-cn">755</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-v">R</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-t">var</span><span class="crayon-o">/</span><span class="crayon-v">lib</span><span class="crayon-o">/</span><span class="crayon-v">wordpress</span><span class="crayon-o">/</span><span class="crayon-v">wp</span><span class="crayon-o">-</span><span class="crayon-v">content</span><span class="crayon-o">/</span><span class="crayon-v">plugins</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    Activate the plugin using the plugins page in the WordPress GUI.</p>
    <p>In the WordPress admin Dashboard, go to Settings&gt;Discussion and uncheck “Show avatars” as they are also pulled from the normal internet.</p>
    <p>With this setup, you will not be able to update or install anything from inside your browser. That requires FTP which you can set up if you want to, but it will take extra effort to secure. If you have access to the computer your site is hosted on, you might as well administer it from there. This involves finding the web page for any out of date packages such as themes and plugins and re-extract them into the relevant directories in /var/lib/wordpress/wp-content. This will also require changing permissions with chmod, but it is exactly the same procedure as outlined for plugins, online changing the directory.</p>
    <p>Enjoy your anonymous blog.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/101/" rel="tag">101</a> <a href="https://www.deepdotweb.com/tag/blog/" rel="tag">blog</a> <a href="https://www.deepdotweb.com/tag/creating/" rel="tag">creating</a> <a href="https://www.deepdotweb.com/tag/free/" rel="tag">free</a> <a href="https://www.deepdotweb.com/tag/speech/" rel="tag">speech</a> <a href="https://www.deepdotweb.com/tag/whonix/" rel="tag">whonix</a> <a href="https://www.deepdotweb.com/tag/wordpress/" rel="tag">wordpress</a></span> <span style="display:none" class="updated">2015-06-29</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/politech/" title="Posts by Politech" rel="author">Politech</a></strong></div>
    </div>
</article>

