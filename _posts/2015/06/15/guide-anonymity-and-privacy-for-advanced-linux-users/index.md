---
Guide: Anonymity and Privacy for Advanced Linux Users
---
<article class="post-listing post-10726 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-advanced tag-anonymity tag-linux tag-privacy tag-users">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/admin/" title>DeepDotWeb </a></span>
    <span>June 15, 2015</span>
    
    <span><a href="https://www.deepdotweb.com/2015/06/15/guide-anonymity-and-privacy-for-advanced-linux-users/#comments">10 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>All Credits go to <strong>beac0n</strong>, thanks for contacting us and contributing the guide you created!</p>
    <p>As people requested &#8211; here is a link to <a href="https://we.riseup.net/opsec/anonymity-and-privacy-for-advanced-linux+303781">download this guide as a PDF</a>.</p>
    <h2 class="first"><a name="intro"></a>Intro</h2>
    <p>The goal is to bring together enough information in one document for a beginner to get started. Visiting countless sites, and combing the internet for information can make it obvious your desire to obtain anonymity, and lead to errors, due to conflicting information. Every effort has been made to make this document accurate. This guide is image heavy so it may take some time to load via Tor.</p>
    <h2><a name="some-general-sources-big-thanks"></a>Some general sources/Big Thanks</h2>
    <p><strong>For more general guides checkout:</strong><br/>
    <a href="https://ssd.eff.org"> <span class="caps">EFF</span> Surveillance Self-Defense project</a><br/>
    <a href="https://help.riseup.net/en/security">Riseup.net Security Guide</a><br/>
    <a href="https://securityinabox.org"> Security in a box</a><br/>
    <a href="https://tails.boum.org/doc/index.en.html"><span class="caps">TAILS</span> Documentation</a> &#8211; for those looking for a solid starting place <span class="caps">TAILS</span> OS is a great choice.</p>
    <p><strong>Thanks</strong>!<br/>
    securityinabox.org<br/>
    <a href="https://Deepdotweb.com"> Deepdotweb.com</a><br/>
    <span class="caps">EFF</span> and <span class="caps">EPIC</span><br/>
    riseup.net</p>
    <p>For educational purposes.<br/>
    Not legal advice or call to action.</p>
    <p><strong>Table of Contents</strong></p>
    <ul class="toc">
    <li class="toc1"><a href="#intro">1 Intro</a></li>
    <li class="toc1"><a href="#some-general-sources-big-thanks">2 Some general sources/Big Thanks</a></li>
    <li class="toc1"><a href="#technical-information">3 Technical Information</a>
    <ul>
    <li class="toc2"><a href="#strong-passwords">3.1 Strong Passwords</a></li>
    <li class="toc2"><a href="#internet-connectivity">3.2 Internet Connectivity</a>
    <ul>
    <li class="toc3"><a href="#firewall">3.2.1 Firewall</a></li>
    <li class="toc3"><a href="#changing-mac-address">3.2.2 Changing MAC Address</a></li>
    <li class="toc3"><a href="#intrustion-detection">3.2.3 Intrustion Detection</a></li>
    <li class="toc3"><a href="#disk-encryption">3.2.4 Disk Encryption</a></li>
    <li class="toc3"><a href="#browsers">3.2.5 Browsers</a></li>
    <li class="toc3"><a href="#router-configuration">3.2.6 Router Configuration</a></li>
    <li class="toc3"><a href="#anonymity-networking">3.2.7 Anonymity Networking</a></li>
    <li class="toc3"><a href="#vpn">3.2.8 VPN</a></li>
    <li class="toc3"><a href="#proxy-chains">3.2.9 Proxy Chains</a></li>
    </ul>
    </li>
    <li class="toc2"><a href="#operating-systems">3.3 Operating Systems</a>
    <ul>
    <li class="toc3"><a href="#flash-firmware">3.3.1 Flash Firmware</a></li>
    <li class="toc3"><a href="#enabling-a-bios-boot-password">3.3.2 Enabling a BIOS boot password</a></li>
    <li class="toc3"><a href="#usb-bootable-operating-systems">3.3.3 USB Bootable Operating Systems:</a></li>
    <li class="toc3"><a href="#linux-image-files-can-be-found-at-http-distrowatch">3.3.4 Linux (image files can be found at http://distrowatch.org)</a></li>
    </ul>
    </li>
    <li class="toc2"><a href="#secure-data-wiping-linux">3.4 Secure Data-Wiping Linux</a></li>
    <li class="toc2"><a href="#physical-destruction">3.5 Physical Destruction</a></li>
    <li class="toc2"><a href="#cold-boot-attack">3.6 Cold-Boot Attack</a></li>
    <li class="toc2"><a href="#basic-communications">3.7 Basic Communications</a>
    <ul>
    <li class="toc3"><a href="#images">3.7.1 Images</a></li>
    <li class="toc3"><a href="#email-providers">3.7.2 Email Providers</a></li>
    <li class="toc3"><a href="#jabber_xmpp-otr">3.7.3 Jabber_XMPP/OTR</a></li>
    <li class="toc3"><a href="#alternative-messaging-options">3.7.4 Alternative Messaging Options</a></li>
    </ul>
    </li>
    <li class="toc2"><a href="#gnupg-pgp-basics">3.8 GNUPG/PGP Basics</a>
    <ul>
    <li class="toc3"><a href="#tails-pgp">3.8.1 TAILS PGP</a></li>
    <li class="toc3"><a href="#additional-reading-on-pgp">3.8.2 Additional reading on PGP</a></li>
    <li class="toc3"><a href="#pgp-versions">3.8.3 PGP Versions</a></li>
    </ul>
    </li>
    <li class="toc2"><a href="#validating-files-with-md5-or-sha1">3.9 Validating Files with MD5 or SHA1:</a>
    <ul>
    <li class="toc3"><a href="#sha1-sum">3.9.1 SHA1 Sum</a></li>
    <li class="toc3"><a href="#md5-sum">3.9.2 MD5 Sum</a></li>
    </ul>
    </li>
    </ul>
    </li>
    </ul>
    <h2>Technical Information</h2>
    <h3><a name="strong-passwords"></a>Strong Passwords</h3>
    <p>It’s difficult to remember many passwords. First off it’s good to select a strong password manager. <a href="https://www.keepassx.org/">Keepassx</a> is cross-platform, and has good security features, like encryption by password and using a keyfile. It also allows you to generate strong passwords, so if you’re not worried about memorization it’s good practice to let Keepassx generate secure random passwords.</p>
    <p>It’s best not to use services that store your passwords in the cloud. If you need you can back up your encrypted password database, on a secure server, in an encrypted directory, and store your keyfile in a separate location.</p>
    <p>Passwords for encryption and critical access should be prioritized. Even a long randomized password may not be a secure enough method. <span class="caps">EFF</span> recommends you try the diceware method, or basically randomly chain a number of words selected from a word list based on dice roles. Full details are <a href="http://world.std.com/%7Ereinhold/diceware.html">available here</a>.</p>
    <p>Although it’s an annoyance, passwords are the ever present key to what matters most to you.</p>
    <h3><a name="internet-connectivity"></a>Internet Connectivity</h3>
    <p>No service provider should be presumed to completely protect your privacy. Even if your <span class="caps">VPN</span>/Proxy or other <span class="caps">ISP</span> promises no logs, or identifiable information, time and time again information has been collected and used against those seeking anonymity. Open-Source technologies where you are able to examine source, yet trust is still ultimately placed in the hands of developers, are better than trusting a Government of other entity with your security.</p>
    <p>Consider reading the Terms of Service any time you sign up for a service or install something.</p>
    <p>Also remember that the times you use technology can be used to build a profile of your location for identification. Consider changing up your times of connectivity. On forums, chat and other services, it may be worthwhile to disable the notification that outwardly displays when you are on line or select invisible mode when applicable.</p>
    <h3><a name="firewall"></a>Firewall</h3>
    <p><span class="caps">UFW</span> (Uncomplicated Firewall) is a great general firewall for linuux</p>
    <ol>
    <li>sudo apt-get install ufw</li>
    <li>sudo ufw enable</li>
    <li>sudo ufw default deny incoming</li>
    </ol>
    <p>as some malware may utilize outgoing traffic, like encrypted udp, it may be worthwhile to limit outgoing ports</p>
    <ol>
    <li>sudo ufw default deny outgoing</li>
    </ol>
    <p>it may be better to specifically allow/deny the specific ports of concern.</p>
    <ol>
    <li>sudo ufw allow port/tcp</li>
    <li>sudo ufw allow port/udp</li>
    </ol>
    <p>Then when you’re done check the status</p>
    <div id="crayon-59a39d9a6d942805151562" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo ufw status</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d942805151562-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d942805151562-1"><span class="crayon-e">sudo </span><span class="crayon-e">ufw </span><span class="crayon-v">status</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    <a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/ufwbasics21.png"><img class="aligncenter size-full wp-image-10733" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/ufwbasics21.png" alt="ufwbasics2[1]" width="525" height="361" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/ufwbasics21.png 525w, https://www.deepdotweb.com/wp-content/uploads/2015/06/ufwbasics21-300x206.png 300w" sizes="(max-width: 525px) 100vw, 525px"/></a></p>
    <p>you can see I’ve blocked some specific ports in this example</p>
    <p>For more advanced configuration <a href="https://help.ubuntu.com/community/UFW">visit</a>.</p>
    <h3><a name="changing-mac-address"></a>Changing <span class="caps">MAC</span> Address</h3>
    <p>A <span class="caps">MAC</span> Address is a hardware specific identifier for you network interface. In some cases it may be useful to change your mac address to avoid detection.</p>
    <p><a href="https://wiki.archlinux.org/index.php/MAC_address_spoofing">Arch Linux Guide</a>:</p>
    <div id="crayon-59a39d9a6d94e001575231" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo apt-get install macchanger
    for a gui
    sudo apt-get install macchange-gtk</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d94e001575231-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-59a39d9a6d94e001575231-2">2</div><div class="crayon-num" data-line="crayon-59a39d9a6d94e001575231-3">3</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d94e001575231-1"><span class="crayon-e">sudo </span><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-e">install </span><span class="crayon-e">macchanger</span></div><div class="crayon-line crayon-striped-line" id="crayon-59a39d9a6d94e001575231-2"><span class="crayon-st">for</span><span class="crayon-h"> </span><span class="crayon-i">a</span><span class="crayon-h"> </span><span class="crayon-e">gui</span></div><div class="crayon-line" id="crayon-59a39d9a6d94e001575231-3"><span class="crayon-e">sudo </span><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-e">install </span><span class="crayon-v">macchange</span><span class="crayon-o">-</span><span class="crayon-v">gtk</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    With macchanger-gtk</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/macchanger-gtk1.png"><img class="aligncenter size-full wp-image-10734" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/macchanger-gtk1.png" alt="macchanger-gtk[1]" width="410" height="287" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/macchanger-gtk1.png 410w, https://www.deepdotweb.com/wp-content/uploads/2015/06/macchanger-gtk1-300x210.png 300w" sizes="(max-width: 410px) 100vw, 410px"/></a></p>
    <p>heck your current mac addresses for future reference</p>
    <div id="crayon-59a39d9a6d953770417351" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    macchanger eth0
    macchanger wlan0</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d953770417351-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-59a39d9a6d953770417351-2">2</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d953770417351-1"><span class="crayon-e">macchanger </span><span class="crayon-e">eth0</span></div><div class="crayon-line crayon-striped-line" id="crayon-59a39d9a6d953770417351-2"><span class="crayon-e">macchanger </span><span class="crayon-v">wlan0</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    for a random macaddress</p>
    <div id="crayon-59a39d9a6d956606638521" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo ifconfig wlan0 down</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d956606638521-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d956606638521-1"><span class="crayon-e">sudo </span><span class="crayon-e">ifconfig </span><span class="crayon-e">wlan0 </span><span class="crayon-v">down</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    </p>
    <div id="crayon-59a39d9a6d959387094841" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo macchanger -r wlan0</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d959387094841-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d959387094841-1"><span class="crayon-e">sudo </span><span class="crayon-v">macchanger</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-i">r</span><span class="crayon-h"> </span><span class="crayon-v">wlan0</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    This will change the mac address to a random value</p>
    <div id="crayon-59a39d9a6d95c977840479" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    macchanger -e wlan0</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d95c977840479-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d95c977840479-1"><span class="crayon-v">macchanger</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-i">e</span><span class="crayon-h"> </span><span class="crayon-v">wlan0</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    will change the mac address but keep it as the same vendor. This can be useful if you’re spoofing your address but you don’t want it obviously coming from a device not on the network.</p>
    <div id="crayon-59a39d9a6d95f999977807" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo macchanger -A wlan0</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d95f999977807-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d95f999977807-1"><span class="crayon-e">sudo </span><span class="crayon-v">macchanger</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-i">A</span><span class="crayon-h"> </span><span class="crayon-v">wlan0</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    This will change the devices <span class="caps">MAC</span> to a random <span class="caps">MAC</span> of any kind, regardless of the original device.</p>
    <div id="crayon-59a39d9a6d963548728742" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo macchanger —mac=XX:XX:XX:XX:XX:XX interface</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d963548728742-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d963548728742-1"><span class="crayon-e">sudo </span><span class="crayon-i">macchanger</span><span class="crayon-h"> </span>—<span class="crayon-v">mac</span><span class="crayon-o">=</span><span class="crayon-v">XX</span><span class="crayon-o">:</span><span class="crayon-v">XX</span><span class="crayon-o">:</span><span class="crayon-v">XX</span><span class="crayon-o">:</span><span class="crayon-v">XX</span><span class="crayon-o">:</span><span class="crayon-v">XX</span><span class="crayon-o">:</span><span class="crayon-e">XX </span><span class="crayon-t">interface</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    Will change to a specific mac address of your choice</p>
    <p>You may want to write a script to start automatically on network manager start, and network manager shut down.</p>
    <div id="crayon-59a39d9a6d966081035831" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo nano /etc/init/macchanger.conf</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d966081035831-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d966081035831-1"><span class="crayon-e">sudo </span><span class="crayon-v">nano</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">etc</span><span class="crayon-o">/</span><span class="crayon-v">init</span><span class="crayon-o">/</span><span class="crayon-v">macchanger</span><span class="crayon-sy">.</span><span class="crayon-v">conf</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    </p>
    <div id="crayon-59a39d9a6d969416812475" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    description     "change mac addresses"
    
    start on starting network-manager
    
    pre-start script
    /usr/bin/macchanger -A wlan0
    /usr/bin/macchanger -A eth0
    /usr/bin/macchanger -A wmaster0
    /usr/bin/macchanger -A pan0
    #/usr/bin/logger wlan0 `/usr/bin/macchanger -s wlan0`
    #/usr/bin/logger eth0 `/usr/bin/macchanger -s eth0`
    end script
    </textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d969416812475-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-59a39d9a6d969416812475-2">2</div><div class="crayon-num" data-line="crayon-59a39d9a6d969416812475-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-59a39d9a6d969416812475-4">4</div><div class="crayon-num" data-line="crayon-59a39d9a6d969416812475-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-59a39d9a6d969416812475-6">6</div><div class="crayon-num" data-line="crayon-59a39d9a6d969416812475-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-59a39d9a6d969416812475-8">8</div><div class="crayon-num" data-line="crayon-59a39d9a6d969416812475-9">9</div><div class="crayon-num crayon-striped-num" data-line="crayon-59a39d9a6d969416812475-10">10</div><div class="crayon-num" data-line="crayon-59a39d9a6d969416812475-11">11</div><div class="crayon-num crayon-striped-num" data-line="crayon-59a39d9a6d969416812475-12">12</div><div class="crayon-num" data-line="crayon-59a39d9a6d969416812475-13">13</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d969416812475-1"><span class="crayon-i">description</span><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="crayon-s">"change mac addresses"</span></div><div class="crayon-line crayon-striped-line" id="crayon-59a39d9a6d969416812475-2">&nbsp;</div><div class="crayon-line" id="crayon-59a39d9a6d969416812475-3"><span class="crayon-e">start </span><span class="crayon-e">on </span><span class="crayon-e">starting </span><span class="crayon-v">network</span><span class="crayon-o">-</span><span class="crayon-e">manager</span></div><div class="crayon-line crayon-striped-line" id="crayon-59a39d9a6d969416812475-4">&nbsp;</div><div class="crayon-line" id="crayon-59a39d9a6d969416812475-5"><span class="crayon-v">pre</span><span class="crayon-o">-</span><span class="crayon-e">start </span><span class="crayon-v">script</span></div><div class="crayon-line crayon-striped-line" id="crayon-59a39d9a6d969416812475-6"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-o">/</span><span class="crayon-v">usr</span><span class="crayon-o">/</span><span class="crayon-v">bin</span><span class="crayon-o">/</span><span class="crayon-v">macchanger</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-i">A</span><span class="crayon-h"> </span><span class="crayon-v">wlan0</span></div><div class="crayon-line" id="crayon-59a39d9a6d969416812475-7"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-o">/</span><span class="crayon-v">usr</span><span class="crayon-o">/</span><span class="crayon-v">bin</span><span class="crayon-o">/</span><span class="crayon-v">macchanger</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-i">A</span><span class="crayon-h"> </span><span class="crayon-v">eth0</span></div><div class="crayon-line crayon-striped-line" id="crayon-59a39d9a6d969416812475-8"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-o">/</span><span class="crayon-v">usr</span><span class="crayon-o">/</span><span class="crayon-v">bin</span><span class="crayon-o">/</span><span class="crayon-v">macchanger</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-i">A</span><span class="crayon-h"> </span><span class="crayon-v">wmaster0</span></div><div class="crayon-line" id="crayon-59a39d9a6d969416812475-9"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-o">/</span><span class="crayon-v">usr</span><span class="crayon-o">/</span><span class="crayon-v">bin</span><span class="crayon-o">/</span><span class="crayon-v">macchanger</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-i">A</span><span class="crayon-h"> </span><span class="crayon-v">pan0</span></div><div class="crayon-line crayon-striped-line" id="crayon-59a39d9a6d969416812475-10"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-p">#/usr/bin/logger wlan0 `/usr/bin/macchanger -s wlan0`</span></div><div class="crayon-line" id="crayon-59a39d9a6d969416812475-11"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-p">#/usr/bin/logger eth0 `/usr/bin/macchanger -s eth0`</span></div><div class="crayon-line crayon-striped-line" id="crayon-59a39d9a6d969416812475-12"><span class="crayon-st">end</span><span class="crayon-h"> </span><span class="crayon-i">script</span></div><div class="crayon-line" id="crayon-59a39d9a6d969416812475-13">&nbsp;</div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    you can switch out -A for -r or whatever other configuration you might want.</p>
    <div id="crayon-59a39d9a6d96d348797317" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo nano /etc/network/if-post-down.d/random-mac</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d96d348797317-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d96d348797317-1"><span class="crayon-e">sudo </span><span class="crayon-v">nano</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">etc</span><span class="crayon-o">/</span><span class="crayon-v">network</span><span class="crayon-o">/</span><span class="crayon-st">if</span><span class="crayon-o">-</span><span class="crayon-v">post</span><span class="crayon-o">-</span><span class="crayon-v">down</span><span class="crayon-sy">.</span><span class="crayon-v">d</span><span class="crayon-o">/</span><span class="crayon-v">random</span><span class="crayon-o">-</span><span class="crayon-v">mac</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    </p>
    <div id="crayon-59a39d9a6d970340952700" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    #!/bin/sh
    
    MACCHANGER=/usr/bin/macchanger
    
    [ "$IFACE" != "lo" ] || exit 0
    
    # Bring down interface (for wireless cards that are up to scan for networks), change MAC address to a random vendor address, bring up the interface
    /sbin/ifconfig "$IFACE" down
    macchanger -A "$IFACE"
    </textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d970340952700-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-59a39d9a6d970340952700-2">2</div><div class="crayon-num" data-line="crayon-59a39d9a6d970340952700-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-59a39d9a6d970340952700-4">4</div><div class="crayon-num" data-line="crayon-59a39d9a6d970340952700-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-59a39d9a6d970340952700-6">6</div><div class="crayon-num" data-line="crayon-59a39d9a6d970340952700-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-59a39d9a6d970340952700-8">8</div><div class="crayon-num" data-line="crayon-59a39d9a6d970340952700-9">9</div><div class="crayon-num crayon-striped-num" data-line="crayon-59a39d9a6d970340952700-10">10</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d970340952700-1"><span class="crayon-p">#!/bin/sh</span></div><div class="crayon-line crayon-striped-line" id="crayon-59a39d9a6d970340952700-2">&nbsp;</div><div class="crayon-line" id="crayon-59a39d9a6d970340952700-3"><span class="crayon-v">MACCHANGER</span><span class="crayon-o">=</span><span class="crayon-o">/</span><span class="crayon-v">usr</span><span class="crayon-o">/</span><span class="crayon-v">bin</span><span class="crayon-o">/</span><span class="crayon-i">macchanger</span></div><div class="crayon-line crayon-striped-line" id="crayon-59a39d9a6d970340952700-4">&nbsp;</div><div class="crayon-line" id="crayon-59a39d9a6d970340952700-5"><span class="crayon-sy">[</span><span class="crayon-h"> </span><span class="crayon-s">"$IFACE"</span><span class="crayon-h"> </span><span class="crayon-o">!=</span><span class="crayon-h"> </span><span class="crayon-s">"lo"</span><span class="crayon-h"> </span><span class="crayon-sy">]</span><span class="crayon-h"> </span><span class="crayon-o">||</span><span class="crayon-h"> </span><span class="crayon-i">exit</span><span class="crayon-h"> </span><span class="crayon-cn">0</span></div><div class="crayon-line crayon-striped-line" id="crayon-59a39d9a6d970340952700-6">&nbsp;</div><div class="crayon-line" id="crayon-59a39d9a6d970340952700-7"><span class="crayon-p"># Bring down interface (for wireless cards that are up to scan for networks), change MAC address to a random vendor address, bring up the interface</span></div><div class="crayon-line crayon-striped-line" id="crayon-59a39d9a6d970340952700-8"><span class="crayon-o">/</span><span class="crayon-v">sbin</span><span class="crayon-o">/</span><span class="crayon-i">ifconfig</span><span class="crayon-h"> </span><span class="crayon-s">"$IFACE"</span><span class="crayon-h"> </span><span class="crayon-e">down</span></div><div class="crayon-line" id="crayon-59a39d9a6d970340952700-9"><span class="crayon-v">macchanger</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-i">A</span><span class="crayon-h"> </span><span class="crayon-s">"$IFACE"</span></div><div class="crayon-line crayon-striped-line" id="crayon-59a39d9a6d970340952700-10">&nbsp;</div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    <ol>
    <li>sudo chmod +x /etc/network/if-post-down.d/random-mac</li>
    <li>sudo service network-manager restart</li>
    </ol>
    <h3><a name="intrustion-detection"></a>Intrustion Detection</h3>
    <p>The basic premise is monitoring the system for unusual activity. First is to keep an eye on the logs, and the next step is to consider an <span class="caps">IDS</span> like snort. There’s a learning curve, but here are some useful tools, that with some research can increase security especially if you allow others to access the system.</p>
    <ol>
    <li>logwatch
    <ol>
    <li><a href="https://help.ubuntu.com/community/Logwatch">help.ubuntu.com</a></li>
    </ol>
    </li>
    </ol>
    <ol>
    <li>snort
    <ol>
    <li><a href="http://snort.org">snort.org</a></li>
    <li><a href="http://manual.snort.org/">http://manual.snort.org/</a></li>
    </ol>
    </li>
    </ol>
    <ol>
    <li>Open Source SECurity
    <ol>
    <li><a href="http://www.ossec.net">www.ossec.net</a></li>
    <li><a href="http://www.ossec.net/?page_id=160">http://www.ossec.net/?page_id=160</a></li>
    </ol>
    </li>
    </ol>
    <p>You may want to get yourself acquainted with some of the common security tools available. Here’s a good list, definitely nmap, tcpdump, netcat and wireshark <a href="https://sectools.org/">are useful</a>.</p>
    <h3><a name="disk-encryption"></a>Disk Encryption</h3>
    <p>On first install of a linux operating system you should be prompted to create an encrypted <span class="caps">LVM</span> partition, and encrypt your home folder. This is a good start. For further security there is veracrypt.</p>
    <p>Veracrypt is a fork of Truecrypt that is better at patching vulnerabilities. I see a lot of tutorials touting Truecrypt, and it’s in most package managers. However, you should download Veracrypt.</p>
    <p>Download: <a href="https://veracrypt.codeplex.com/releases/view/565079">veracrypt.codeplex.com/releases/view/56&#8230;</a></p>
    <p><a href="https://veracrypt.codeplex.com/wikipage?title=Beginner%27s%20Tutorial">Here’s a good beginners tutorial for Veracrypt</a></p>
    <p><strong>How to create a hidden encrypted volume with Veracrypt</strong></p>
    <p>Select Create Volume</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt11.png"><img class="aligncenter size-full wp-image-10735" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt11.png" alt="veracrypt1[1]" width="595" height="578" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt11.png 595w, https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt11-300x291.png 300w, https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt11-50x50.png 50w" sizes="(max-width: 595px) 100vw, 595px"/></a></p>
    <p>Select Create an Encrypted File Container</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt21.png"><img class="aligncenter size-full wp-image-10736" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt21.png" alt="veracrypt2[1]" width="763" height="485" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt21.png 763w, https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt21-300x191.png 300w" sizes="(max-width: 763px) 100vw, 763px"/></a><br/>
    Select Hidden Veracrypt volume</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt31.png"><img class="aligncenter size-full wp-image-10737" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt31.png" alt="veracrypt3[1]" width="771" height="491" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt31.png 771w, https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt31-300x191.png 300w" sizes="(max-width: 771px) 100vw, 771px"/></a><br/>
    Choose volume location and select never save history:</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt41.png"><img class="aligncenter size-full wp-image-10738" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt41.png" alt="veracrypt4[1]" width="767" height="485" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt41.png 767w, https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt41-300x190.png 300w" sizes="(max-width: 767px) 100vw, 767px"/></a><br/>
    Select your encryption algorithm, <span class="caps">AES</span> is fine, but you may chose more secure<br/>
    Select Hash Algorithm, <span class="caps">SHA</span>-512 is sufficient</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt51.png"><img class="aligncenter size-full wp-image-10739" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt51.png" alt="veracrypt5[1]" width="767" height="488" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt51.png 767w, https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt51-300x191.png 300w" sizes="(max-width: 767px) 100vw, 767px"/></a><br/>
    Select Use Key files and click the key files box… <strong>optional:</strong></p>
    <p>&nbsp;</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt61.png"><img class="aligncenter size-full wp-image-10740" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt61.png" alt="veracrypt6[1]" width="761" height="487" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt61.png 761w, https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt61-300x192.png 300w" sizes="(max-width: 761px) 100vw, 761px"/></a><br/>
    Generate save the new key.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt71.png"><img class="aligncenter size-full wp-image-10741" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt71.png" alt="veracrypt7[1]" width="657" height="468" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt71.png 657w, https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt71-300x214.png 300w" sizes="(max-width: 657px) 100vw, 657px"/></a><br/>
    Click add files and add the key<br/>
    Click Generate Random Keyfile box if you want another key<br/>
    You may also use existing keys:</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt81.png"><img class="aligncenter size-full wp-image-10742" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt81.png" alt="veracrypt8[1]" width="640" height="525" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt81.png 640w, https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt81-300x246.png 300w" sizes="(max-width: 640px) 100vw, 640px"/></a><br/>
    Click format to create the volume that will be visible:</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt101.png"><img class="aligncenter size-full wp-image-10743" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt101.png" alt="veracrypt10[1]" width="763" height="487" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt101.png 763w, https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt101-300x191.png 300w" sizes="(max-width: 763px) 100vw, 763px"/></a><br/>
    Now it’s recommended to load this volume with contents that appear sensitive</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt111.png"><img class="aligncenter size-full wp-image-10744" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt111.png" alt="veracrypt11[1]" width="764" height="483" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt111.png 764w, https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt111-300x190.png 300w" sizes="(max-width: 764px) 100vw, 764px"/></a><br/>
    You will follow the same steps, remember this is the hidden volume consider it’s security most important.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt121.png"><img class="aligncenter size-full wp-image-10745" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt121.png" alt="veracrypt12[1]" width="756" height="485" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt121.png 756w, https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt121-300x192.png 300w" sizes="(max-width: 756px) 100vw, 756px"/></a><br/>
    When complete you will see this warning, read it carefully.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt131.png"><img class="aligncenter size-full wp-image-10746" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt131.png" alt="veracrypt13[1]" width="489" height="353" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt131.png 489w, https://www.deepdotweb.com/wp-content/uploads/2015/06/veracrypt131-300x217.png 300w" sizes="(max-width: 489px) 100vw, 489px"/></a></p>
    <h2>Browsers</h2>
    <h3>Tor Browser</h3>
    <p>Download at: <a href="https://torproject.org">torproject.org</a></p>
    <p>All Tor network addresses will be followed with .onion, not .com. It is far more secure browsing .onion services.</p>
    <p>In depth explanation of Tor <a href="https://media.torproject.org/video/tor-internet-days-2010.mp4">by its head developer Arma</a>.</p>
    <p>Once you’ve download tor browser, expand the zipped file. Then</p>
    <div id="crayon-59a39d9a6d985838665005" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    cd tordirectory
    ./start-tor-browser.desktop</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d985838665005-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-59a39d9a6d985838665005-2">2</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d985838665005-1"><span class="crayon-e">cd </span><span class="crayon-i">tordirectory</span></div><div class="crayon-line crayon-striped-line" id="crayon-59a39d9a6d985838665005-2"><span class="crayon-sy">.</span><span class="crayon-o">/</span><span class="crayon-v">start</span><span class="crayon-o">-</span><span class="crayon-v">tor</span><span class="crayon-o">-</span><span class="crayon-v">browser</span><span class="crayon-sy">.</span><span class="crayon-v">desktop</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    <a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/starttor1.png"><img class="aligncenter size-full wp-image-10747" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/starttor1.png" alt="starttor[1]" width="497" height="145" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/starttor1.png 497w, https://www.deepdotweb.com/wp-content/uploads/2015/06/starttor1-300x88.png 300w" sizes="(max-width: 497px) 100vw, 497px"/></a></p>
    <p>Forbidding javascript and other elements can make web browsing less convenient, but by allowing more elements you open yourself to potential vulnerabilities. It’s best to find the best possible security setting you can withstand while the web browsing experience is still functional.</p>
    <p><strong>Configuring Security Settings</strong></p>
    <p>Privacy and security settings can be easily configured. Click on the Onion in the top left.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/toronion_large1.png"><img class="aligncenter size-full wp-image-10748" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/toronion_large1.png" alt="toronion_large[1]" width="500" height="349" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/toronion_large1.png 500w, https://www.deepdotweb.com/wp-content/uploads/2015/06/toronion_large1-300x209.png 300w" sizes="(max-width: 500px) 100vw, 500px"/></a></p>
    <p>Select “Privacy and Security Settings” Adjust the slider to your desired level of security.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/torprivacysettings1.png"><img class="aligncenter size-full wp-image-10749" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/torprivacysettings1.png" alt="torprivacysettings[1]" width="619" height="495" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/torprivacysettings1.png 619w, https://www.deepdotweb.com/wp-content/uploads/2015/06/torprivacysettings1-300x240.png 300w" sizes="(max-width: 619px) 100vw, 619px"/></a></p>
    <p><strong>Noscript basics</strong></p>
    <p>Depending on your security level selected in Tor, Noscript may not provide any advantage. That main advantage of Noscript is it’s easier to tailor allowing on specific sites, or for specific elements on the fly. Click the S in the Top Left next to the Tor Onion symbol and select forbid scripts globally. You should see a red line across the S. If you allow specific sites, you should check that the red line is there for those you do not allow. Allowing only specific sites may create a fingerprint of your activity. There are some advanced settings under options worth taking a look at.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/tornoscripts_large1.png"><img class="aligncenter size-full wp-image-10750" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/tornoscripts_large1.png" alt="tornoscripts_large[1]" width="500" height="357" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/tornoscripts_large1.png 500w, https://www.deepdotweb.com/wp-content/uploads/2015/06/tornoscripts_large1-300x214.png 300w" sizes="(max-width: 500px) 100vw, 500px"/></a></p>
    <h2>Tor bridge</h2>
    <p>in some cases if Tor is blocked or you wish to conceal the use of Tor a bridge can be configured. This makes it more difficult for an <span class="caps">ISP</span> to detect Tor. Bridges can help avoid censorship, and if your <span class="caps">ISP</span> Blocks Tor Traffic it is much more difficult to detect the nature of the traffic unless deep packet inspection is employed. It’s one of those things that since it’s there, might as well set it up as a per-cautionary measure and see if your connection is still, reliable and fast enough for your standards.</p>
    <ul>
    <li>Click Open Settings on the Pop-up Connection Box<a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/torconnectionpopup1.png"><img class="aligncenter size-full wp-image-10751" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/torconnectionpopup1.png" alt="torconnectionpopup[1]" width="401" height="260" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/torconnectionpopup1.png 401w, https://www.deepdotweb.com/wp-content/uploads/2015/06/torconnectionpopup1-300x195.png 300w" sizes="(max-width: 401px) 100vw, 401px"/><br/>
    </a></li>
    <li>Click configure<br/>
    <a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/torconfigurebridge1.png"><img class="aligncenter size-full wp-image-10752" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/torconfigurebridge1.png" alt="torconfigurebridge[1]" width="679" height="539" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/torconfigurebridge1.png 679w, https://www.deepdotweb.com/wp-content/uploads/2015/06/torconfigurebridge1-300x238.png 300w" sizes="(max-width: 679px) 100vw, 679px"/></a></li>
    <li>Select Yes to <span class="caps">ISP</span> Censors or Blocks<a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/torispblocks1.png"><img class="aligncenter size-full wp-image-10753" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/torispblocks1.png" alt="torispblocks[1]" width="681" height="538" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/torispblocks1.png 681w, https://www.deepdotweb.com/wp-content/uploads/2015/06/torispblocks1-300x237.png 300w" sizes="(max-width: 681px) 100vw, 681px"/></a></li>
    <li>obfs3 is fine, see below for information on other options.<br/>
    <a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/torselectbridge1.png"><img class="aligncenter size-full wp-image-10754" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/torselectbridge1.png" alt="torselectbridge[1]" width="686" height="537" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/torselectbridge1.png 686w, https://www.deepdotweb.com/wp-content/uploads/2015/06/torselectbridge1-300x235.png 300w" sizes="(max-width: 686px) 100vw, 686px"/></a></li>
    <li>Most likely just skip use a local proxy</li>
    <li>Click connect<a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/torconnectbridge1.png"><img class="aligncenter size-full wp-image-10755" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/torconnectbridge1.png" alt="torconnectbridge[1]" width="680" height="532" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/torconnectbridge1.png 680w, https://www.deepdotweb.com/wp-content/uploads/2015/06/torconnectbridge1-300x235.png 300w" sizes="(max-width: 680px) 100vw, 680px"/></a></li>
    </ul>
    <p>Optionally if Tor is already started you can:</p>
    <ul>
    <li>click the onoin icon in the top left of the browser and select</li>
    <li>Open Network Settings</li>
    <li>check My <span class="caps">ISP</span> Blocks Connections and hit OK.<a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/torbridgeselect1.png"><img class="aligncenter size-full wp-image-10756" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/torbridgeselect1.png" alt="torbridgeselect[1]" width="662" height="632" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/torbridgeselect1.png 662w, https://www.deepdotweb.com/wp-content/uploads/2015/06/torbridgeselect1-300x286.png 300w" sizes="(max-width: 662px) 100vw, 662px"/></a></li>
    <li>Use obfs 3 which is recommended, see next section on other types.</li>
    </ul>
    <h3>Pluggable Transports</h3>
    <p>Pluggable Transports are extensions to Tor which utilize it’s pluggable transport <span class="caps">API</span>. These are more advanced ways to disguise traffic flow, for instance making it appear as skype traffic or utilizing a flash proxy. Many are now included in the Bridge Option Menu, so this is a good resource to learn more about the specifics. Some may require <a href="https://www.torproject.org/docs/pluggable-transports.html.en#download">custom installation</a>.</p>
    <h3>Firefox</h3>
    <p>If you need to use another browser Firefox is preferred. Here are some configuration settings and extensions that can be helpful.</p>
    <p><strong>Optional Configuration:</strong></p>
    <p>In the <span class="caps">URL</span> Bar enter: about:config</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/aboutconfigbasics1.png"><img class="aligncenter size-full wp-image-10757" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/aboutconfigbasics1.png" alt="aboutconfigbasics[1]" width="689" height="512" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/aboutconfigbasics1.png 689w, https://www.deepdotweb.com/wp-content/uploads/2015/06/aboutconfigbasics1-300x223.png 300w" sizes="(max-width: 689px) 100vw, 689px"/></a></p>
    <ul>
    <li>geo.enabled = false</li>
    <li>geo.wifi.uri =leave blank</li>
    <li>network.http.accept.default = text/html,application/xhtml+xml,application/xml;q=0.9,<strong>/</strong>;q=0.8</li>
    <li>network.http.use-cache = false</li>
    <li>network.http.keep-alive.timeout = 600</li>
    <li>network.http.max-persistent-connections-per-proxy = 16</li>
    <li>network.proxy.socks_remote_dns = true</li>
    <li>network.cookie.lifetimePolicy = 2</li>
    <li>network.http.sendRefererHeader = 0</li>
    <li>network.http.sendSecureXSiteReferrer = false</li>
    <li>network.protocol-handler.external = false #set the default and all the sub-settings to false</li>
    <li>network.protocol-handler.warn-external = true #set the default and all the sub-settings to true</li>
    <li>network.http.pipelining = true</li>
    <li>network.http.pipelining.maxrequests = 8</li>
    <li>network.http.proxy.keep-alive = true</li>
    <li>network.http.proxy.pipelining = true</li>
    <li>network.prefetch-next = false</li>
    <li>browser.cache.disk.enable = false</li>
    <li>browser.cache.offline.enable = false</li>
    <li>browser.sessionstore.privacy_level = 2</li>
    <li>browser.sessionhistory.max_entries = 2</li>
    <li>browser.display.use_document_fonts = 0</li>
    <li>intl.charsetmenu.browser.cache = <span class="caps">ISO</span>-8859-9, windows-1252, windows-1251, <span class="caps">ISO</span>-8859-1, <span class="caps">UTF</span>-8</li>
    <li>dom.storage.enabled = false</li>
    <li>extensions.blocklist.enabled = false</li>
    </ul>
    <p><strong>Other useful options:</strong></p>
    <ol>
    <li>Disable all plugins: tools → addons → plugins</li>
    <li>Disable all live bookmarks: bookmarks → bookmarks toolbar → R/click latest headlines → delete</li>
    <li>Disable all updates: tools → options → advanced → update</li>
    <li>Enable ‘do not track’ feature: tools → options → privacy</li>
    <li>Enable private browsing, configure to remember nothing &amp; disable 3rd party cookies: tools → options → privacy</li>
    </ol>
    <p><strong>Useful plugins:</strong><br/>
    it’s best to keep plugins at a minimum but here are some to consider</p>
    <ul>
    <li><a href="https://www.eff.org/https-everywhere"><span class="caps">HTTPS</span> Everywhere</a></li>
    <li><a href="https://www.eff.org/privacybadger">Privacy Badger</a></li>
    <li><a href="https://addons.mozilla.org/en-us/firefox/addon/closen-forget">Close n forget</a></li>
    <li><a href="https://github.com/chrisaljoudi/uBlock#getting-started">ublock</a></li>
    <li><a href="https://addons.mozilla.org/en-us/firefox/addon/modify-headers">Modify Headers</a></li>
    <li><a href="https://addons.mozilla.org/en-us/firefox/addon/noscript">NoScript</a></li>
    <li><a href="https://addons.mozilla.org/en-us/firefox/addon/refcontrol">RefControl</a></li>
    <li><a href="https://addons.mozilla.org/en-us/firefox/addon/user-agent-switcher">User Agent Switcher</a></li>
    <li><a href="https://addons.mozilla.org/en-us/firefox/addon/adblock-plus">Adblock plus</a></li>
    </ul>
    <p>You may consider visiting <a href="http://ip-check.info">ip-check.info</a> to see what data your browser is sending.</p>
    <h3><a name="router-configuration"></a>Router Configuration</h3>
    <p>It’s recommended to get a router compatible with an open source firmware. The two major recommended firmwares are Tomato and dd-wrt. In some cases Tor, or a vpn can be run directly on the router, and this can be useful if you find yourself forgetting at times to enable your desired connection. A backup router only used for specific connections may also be useful to swap in and out when secure connection is needed.. For the crafty, a Raspberry Pi can be configured as a local device to route connections through.</p>
    <p>Installation is device specific navigate to either the Tomato or dd-wrt site for more information.</p>
    <h3>Tomato</h3>
    <p><a href="http://tomatousb.org">tomatousb.org</a><br/>
    <a href="http://tomatousb.org/forum/t-644375/tor-relay-with-shibby-build">Tor Version</a>: (may not work for all versions)</p>
    <p>dd-wrt<br/>
    <a href="https://www.dd-wrt.com/site/support/router-database">www.dd-wrt.com/site/support/router-data&#8230;</a><br/>
    Tor: do your own research</p>
    <h3>Raspberry Pi</h3>
    <p><a href="http://raspberrypihq.com/how-to-turn-a-raspberry-pi-into-a-wifi-router">raspberrypihq.com/how-to-turn-a-raspber&#8230;</a><br/>
    <a href="https://makezine.com/projects/browse-anonymously-with-a-diy-raspberry-pi-vpntor-router">makezine.com/projects/browse-anonymousl&#8230;</a></p>
    <h3><a name="anonymity-networking"></a>Anonymity Networking</h3>
    <h3>Tor</h3>
    <p>The stand alone Tor daemon can be be found in the Ubuntu/Debian/Arch package manager.</p>
    <p>sudo apt-get install tor<br/>
    sudo pacman -S tor</p>
    <p>However, you may wish to visit <a href="https://www.torproject.org/docs/debian.html.en">this link</a> and add their <span class="caps">PPA</span> to get the latest version.</p>
    <p>You can use Tor as a socks proxy once the service is started, either with the browser bundle or Tor daemon.<br/>
    Navigate to the Network Settings, and Proxy section of the desired application.<br/>
    Select Socks 4 Proxy and enter 127.0.0.1 port 9050.</p>
    <p>This will route desired connections through Tor. <span class="caps">TAILS</span> automatically routes all connections through Tor.</p>
    <h3>i2p</h3>
    <p>Alternative to Tor, not as widely used since it requires some more dependencies and not as simple setup. i2p addresses always display as .i2p</p>
    <p>Unlike tor i2p is a self contained network, it does not function as a proxy with traditional exit nodes. It is generally used to browse with the network of what are called eepsites.</p>
    <p>Ubuntu/Debian based systems</p>
    <ol>
    <li>follow guide to add i2p to package list</li>
    <li>for ubuntu: sudo apt-add-repository ppa:i2p-maintainers/i2p</li>
    <li><a href="https://geti2p.net/en/download/debian">for debian</a></li>
    <li>other see, and download <a href="https://geti2p.net/en/download">necessary java files</a>.</li>
    </ol>
    <ol>
    <li>sudo apt-get update</li>
    <li>sudo apt-get install i2p</li>
    </ol>
    <p>starting i2p in terminal:<br/>
    <strong>do not run as root or use sudo</strong></p>
    <ul>
    <li>i2p router start</li>
    </ul>
    <p>If you have issue connecting to .i2p addresses check configuration by visiting: localhost:7657/confignet</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/networksettings1.png"><img class="aligncenter size-full wp-image-10758" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/networksettings1.png" alt="networksettings[1]" width="893" height="554" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/networksettings1.png 893w, https://www.deepdotweb.com/wp-content/uploads/2015/06/networksettings1-300x186.png 300w" sizes="(max-width: 893px) 100vw, 893px"/></a></p>
    <p>One main issue is your firewall or router is blocking connections. Click networking.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/ports1.png"><img class="aligncenter size-full wp-image-10759" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/ports1.png" alt="ports[1]" width="691" height="420" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/ports1.png 691w, https://www.deepdotweb.com/wp-content/uploads/2015/06/ports1-300x182.png 300w" sizes="(max-width: 691px) 100vw, 691px"/></a></p>
    <p>Basic port unblocking</p>
    <p>IP Tables</p>
    <ol>
    <li>sudo iptables -A <span class="caps">INPUT</span> -p tcp —dport i2p port here -j <span class="caps">ACCEPT</span></li>
    <li>sudo iptables -L</li>
    </ol>
    <p><span class="caps">UFW</span></p>
    <ol>
    <li>sudo ufw allow i2p port here/tcp</li>
    <li>sudo ufw status</li>
    </ol>
    <h3>Other Anonymity Networks and Software</h3>
    <p>Here are two good resources for additional information on available Anonymity Networks and Software:<br/>
    <a href="https://gnunet.org/links">gnunet.org/links</a>/<br/>
    <a href="http://freehaven.net/anonbib/topic.html">freehaven.net/anonbib/topic.html</a></p>
    <h3><a name="vpn"></a><span class="caps">VPN</span></h3>
    <h3>Community VPNs</h3>
    <p>Good for activists and journalists:<br/>
    <a href="https://riseup.net">riseup.net</a><br/>
    <a href="https://autistici.org">autistici.org</a></p>
    <p><strong>Paid VPNs</strong></p>
    <p>Recommended resource:<br/>
    <a href="https://www.deepdotweb.com/vpn-comparison-chart/">Our Best VPN&#8217;s Chart</a> and &#8220;<a href="https://www.deepdotweb.com/2014/07/08/is-your-vpn-legit-or-shit/">Is your VPN legit or shit?</a>&#8221; post (remember their claims, are not a promise and even their systems could be vulnerable)</p>
    <h3>Free VPNs</h3>
    <p>I don’t recommend these at all but will list one that has been reliable. You’ll have to search for more.</p>
    <p>Unfortunately you should have no expectation of privacy on a free <span class="caps">VPN</span> but for one time use if you have no other choice it may be helpful.</p>
    <h3><a href="https://VPNBOOK.com">VPNBOOK.com</a></h3>
    <p>Of the free VPNs seems most reliable, please delicately read terms of service and<br/>
    utilize Tor on-top of the <span class="caps">VPN</span> with any sensitive content. Free VPNs are often banned<br/>
    from posting on many services due to trolling. You can search for others but so far <span class="caps">VPNBOOK</span> just works.</p>
    <h3><a name="proxy-chains"></a>Proxy Chains</h3>
    <p>Sometimes it may be necessary to use a proxy after the Tor exit node, for instance to appear in a desired location, or if exit nodes are banned on a service.</p>
    <p>The setup is relatively simple on Linux.</p>
    <ol>
    <li>sudo apt-get install proxychains</li>
    <li>sudo nano /etc/proxychains.conf</li>
    <li>following ProxyList add<br/>
    socks4 127.0.0.1 9050 #Tor must go first<br/>
    socks5 ipaddress port<br/>
    proxies etc……</li>
    </ol>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/proxychains1.png"><img class="aligncenter size-full wp-image-10760" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/proxychains1.png" alt="proxychains[1]" width="760" height="456" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/proxychains1.png 760w, https://www.deepdotweb.com/wp-content/uploads/2015/06/proxychains1-300x180.png 300w" sizes="(max-width: 760px) 100vw, 760px"/></a></p>
    <p>You will need to search for public socks proxy lists to populate.</p>
    <p>start firefox in terminal: proxychains firefox</p>
    <h3><a name="operating-systems"></a>Operating Systems</h3>
    <p>The best first step is stop the use of Windows and <span class="caps">MAC</span> <span class="caps">OSX</span>, and stick with Linux.</p>
    <h3><a name="flash-firmware"></a>Flash Firmware</h3>
    <p>Locate the firmware model of the motherboard on your computer and flash it with a fresh version. Some deeper level attacks embed themselves in the firmware, so it’s good practice for a clean start.</p>
    <h3><a name="enabling-a-bios-boot-password"></a>Enabling a <span class="caps">BIOS</span> boot password</h3>
    <p>Usually f12 to enter <span class="caps">BIOS</span>, find security section (<span class="caps">UEFI</span> may be different)</p>
    <h3><a name="usb-bootable-operating-systems"></a><span class="caps">USB</span> Bootable Operating Systems:</h3>
    <p>Recommended: <span class="caps">TAILS</span>, Alternatives: Whonix, Liberté Linux and QubesOS</p>
    <p>This guide shows how to install <span class="caps">TAILS</span> on a <span class="caps">USB</span> Drive from a Virtual Machine</p>
    <ol>
    <li><a href="http://www.oracle.com/technetwork/server-storage/virtualbox/downloads/index.html#vbox">Download Virtual Box</a></li>
    <li><a href="http://www.oracle.com/technetwork/server-storage/virtualbox/downloads/index.html#extpack">Download the latest extension package</a></li>
    <li>Double click on the extension package and it should open Virtual Box, click install</li>
    <li><a href="https://tails.boum.org/download/index.en.html#first_time">Download <span class="caps">TAILS</span></a></li>
    <li>Verify file identity with <span class="caps">PGP</span></li>
    <li>Open Virtualbox and connect the <span class="caps">USB</span> drive</li>
    </ol>
    <p>Click new in the top left:</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails11.png"><img class="aligncenter size-full wp-image-10761" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails11.png" alt="tails1[1]" width="765" height="560" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails11.png 765w, https://www.deepdotweb.com/wp-content/uploads/2015/06/tails11-300x220.png 300w" sizes="(max-width: 765px) 100vw, 765px"/></a><br/>
    Name your VM and select Linux 64bit or 32bit depending on which you downloaded:</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails21.png"><img class="aligncenter size-full wp-image-10762" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails21.png" alt="tails2[1]" width="564" height="414" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails21.png 564w, https://www.deepdotweb.com/wp-content/uploads/2015/06/tails21-300x220.png 300w" sizes="(max-width: 564px) 100vw, 564px"/></a><br/>
    Set memory size at least 1024 for smooth performance</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails31.png"><img class="aligncenter size-full wp-image-10763" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails31.png" alt="tails3[1]" width="559" height="425" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails31.png 559w, https://www.deepdotweb.com/wp-content/uploads/2015/06/tails31-300x228.png 300w" sizes="(max-width: 559px) 100vw, 559px"/></a><br/>
    Create a virtual hard drive</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails41.png"><img class="aligncenter size-full wp-image-10764" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails41.png" alt="tails4[1]" width="561" height="416" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails41.png 561w, https://www.deepdotweb.com/wp-content/uploads/2015/06/tails41-300x222.png 300w" sizes="(max-width: 561px) 100vw, 561px"/></a><span class="caps"><br/>
    VDI</span> Image is suitable</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails51.png"><img class="aligncenter size-full wp-image-10765" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails51.png" alt="tails5[1]" width="665" height="478" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails51.png 665w, https://www.deepdotweb.com/wp-content/uploads/2015/06/tails51-300x216.png 300w" sizes="(max-width: 665px) 100vw, 665px"/></a><br/>
    You can select dynamically allocated and set a starting amount at a couple gigabytes</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails61.png"><img class="aligncenter size-full wp-image-10766" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails61.png" alt="tails6[1]" width="656" height="468" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails61.png 656w, https://www.deepdotweb.com/wp-content/uploads/2015/06/tails61-300x214.png 300w" sizes="(max-width: 656px) 100vw, 656px"/></a><br/>
    Select the image and click start</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails81.png"><img class="aligncenter size-full wp-image-10767" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails81.png" alt="tails8[1]" width="764" height="573" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails81.png 764w, https://www.deepdotweb.com/wp-content/uploads/2015/06/tails81-300x225.png 300w" sizes="(max-width: 764px) 100vw, 764px"/></a><br/>
    Select the location of the .iso file you downloaded.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails71.png"><img class="aligncenter size-full wp-image-10768" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails71.png" alt="tails7[1]" width="561" height="381" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails71.png 561w, https://www.deepdotweb.com/wp-content/uploads/2015/06/tails71-300x204.png 300w" sizes="(max-width: 561px) 100vw, 561px"/></a><br/>
    Once started go to Applications→Tails→Tails Installer</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails91.png"><img class="aligncenter size-full wp-image-10769" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails91.png" alt="tails9[1]" width="809" height="646" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails91.png 809w, https://www.deepdotweb.com/wp-content/uploads/2015/06/tails91-300x240.png 300w" sizes="(max-width: 809px) 100vw, 809px"/></a><br/>
    Make sure the <span class="caps">USB</span> Drive is present you will see a green plus, over the usb icon in this image</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails101.png"><img class="aligncenter size-full wp-image-10770" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails101.png" alt="tails10[1]" width="370" height="169" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails101.png 370w, https://www.deepdotweb.com/wp-content/uploads/2015/06/tails101-300x137.png 300w, https://www.deepdotweb.com/wp-content/uploads/2015/06/tails101-272x125.png 272w" sizes="(max-width: 370px) 100vw, 370px"/></a><br/>
    Select clone and install and follow the steps for installation</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails111.png"><img class="aligncenter size-full wp-image-10771" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails111.png" alt="tails11[1]" width="530" height="397" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails111.png 530w, https://www.deepdotweb.com/wp-content/uploads/2015/06/tails111-300x225.png 300w" sizes="(max-width: 530px) 100vw, 530px"/></a><br/>
    Once you’ve started tails you can create a persistent volume to store static content</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails121.png"><img class="aligncenter size-full wp-image-10772" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails121.png" alt="tails12[1]" width="577" height="432" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/tails121.png 577w, https://www.deepdotweb.com/wp-content/uploads/2015/06/tails121-300x225.png 300w" sizes="(max-width: 577px) 100vw, 577px"/></a></p>
    <ol>
    <li>Next reboot you will be prompted if you wish to use persistent or not, only use when necessary.</li>
    </ol>
    <h3><a name="linux-image-files-can-be-found-at-http-distrowatch"></a>Linux (image files can be found at http://distrowatch.org)</h3>
    <p>Recommended base Operating Systems: Archlinux, or Kali, alternatives: Debian Mint Ubuntu<br/>
    although just using Tails as a bootable OS and having some persistent storage is probably better than most can do in terms of hardening their base system.</p>
    <h3>Secure VM with Whonix and Virtualbox</h3>
    <ol>
    <li><a href="https://www.whonix.org/wiki/Download#Download_Whonix">Download both Whonix-Gateway and Workstation</a></li>
    <li><a href="http://www.oracle.com/technetwork/server-storage/virtualbox/downloads/index.html#vbox">Download Virtual Box</a></li>
    <li>You may want to verify the file identities using the Signing key see other sections on this.</li>
    </ol>
    <p>Click file import appliance and select the Whonix Gateway .ova file:</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix11.png"><img class="aligncenter size-full wp-image-10773" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix11.png" alt="whonix1[1]" width="624" height="437" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix11.png 624w, https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix11-300x210.png 300w" sizes="(max-width: 624px) 100vw, 624px"/></a><br/>
    Keep the settings default and click import</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix21.png"><img class="aligncenter size-full wp-image-10774" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix21.png" alt="whonix2[1]" width="629" height="441" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix21.png 629w, https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix21-300x210.png 300w" sizes="(max-width: 629px) 100vw, 629px"/></a><br/>
    Repeat for workstation, select the .ova</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix31.png"><img class="aligncenter size-full wp-image-10775" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix31.png" alt="whonix3[1]" width="629" height="443" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix31.png 629w, https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix31-300x211.png 300w" sizes="(max-width: 629px) 100vw, 629px"/></a><br/>
    Import without changing settings</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix41.png"><img class="aligncenter size-full wp-image-10776" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix41.png" alt="whonix4[1]" width="632" height="428" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix41.png 632w, https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix41-300x203.png 300w, https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix41-290x195.png 290w" sizes="(max-width: 632px) 100vw, 632px"/></a><br/>
    Select both and start both at the same time.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix51.png"><img class="aligncenter size-full wp-image-10777" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix51.png" alt="whonix5[1]" width="768" height="567" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix51.png 768w, https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix51-300x221.png 300w" sizes="(max-width: 768px) 100vw, 768px"/></a><br/>
    Once workstation has finished booting you will see this screen.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix61.png"><img class="aligncenter size-full wp-image-10778" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix61.png" alt="whonix6[1]" width="1031" height="852" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix61.png 1031w, https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix61-300x248.png 300w, https://www.deepdotweb.com/wp-content/uploads/2015/06/whonix61-1024x846.png 1024w" sizes="(max-width: 1031px) 100vw, 1031px"/></a></p>
    <p>You will keep both VM Windows open but all activities will be within the Whonix-Workstation VM Window</p>
    <h3>Base System</h3>
    <p>Essentials:<br/>
    Disk encryption – <span class="caps">LVM</span> Encryption during install, encrypt home directory<br/>
    Bleachbit – clearing day to day files (<span class="caps">RAM</span> wiping is experimental but worth it on shutdown)<br/>
    secure-delete package – secure wiping content</p>
    <p>Intro guides on hardening other recommended base systems.<br/>
    (may be out of date look for hardening guides)</p>
    <ol>
    <li>Kali has basic hardening</li>
    <li><a href="https://wiki.archlinux.org/index.php/Security">Arch Security</a></li>
    <li><a href="https://wiki.ubuntu.com/BasicSecurity">Ubuntu Security</a></li>
    <li><a href="https://www.debian.org/doc/manuals/securing-debian-howto/ch7">Debian Security</a></li>
    </ol>
    <h3><a name="secure-data-wiping-linux"></a>Secure Data-Wiping Linux</h3>
    <p>Consider using an OS like <span class="caps">TAILS</span> with minimal persistent storage and automatic memory wiping to make this easier.</p>
    <p>Proceed with extreme caution, man pages are your friend.</p>
    <p><strong>BleachBit</strong><br/>
    easy, less effective</p>
    <p>First:<br/>
    sudo apt-get install bleachbit<br/>
    sudo bleachbit</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/bleachbit11.png"><img class="aligncenter size-full wp-image-10779" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/bleachbit11.png" alt="bleachbit1[1]" width="604" height="516" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/bleachbit11.png 604w, https://www.deepdotweb.com/wp-content/uploads/2015/06/bleachbit11-300x256.png 300w" sizes="(max-width: 604px) 100vw, 604px"/></a><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/bleachbit21.png"><img class="aligncenter size-full wp-image-10780" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/bleachbit21.png" alt="bleachbit2[1]" width="394" height="623" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/bleachbit21.png 394w, https://www.deepdotweb.com/wp-content/uploads/2015/06/bleachbit21-190x300.png 190w" sizes="(max-width: 394px) 100vw, 394px"/></a></p>
    <p>You can “Shred” files and folders from the file menu, and wipe free space, which may remove excess data that still exists, without pointers.<br/>
    file→Shred files<br/>
    file→Shred folder<br/>
    file→wipe free space</p>
    <p><strong><span class="caps">DBAN</span></strong><br/>
    advanced, boot from usb/cd ideal when discarding a hard drive</p>
    <p>go to <a href="http://dban.org">dban.org</a> download the dban.iso and either burn CD/<span class="caps">DVD</span> or write to <span class="caps">USB</span> and boot off the device.<br/>
    Select “RCMP <span class="caps">TSSIT</span> <span class="caps">OPS</span>-II” for the deletion method<br/>
    Select the drive<br/>
    Prepare to wait 12+ hours</p>
    <p><strong>Secure-Delete</strong><br/>
    hard mode, more secure deletion that bleachbit, easier to use if you want to remove specific partitions or files, rather than complete wipe with <span class="caps">DBAN</span></p>
    <p>you will need to boot off a usb/cd if you wish to wipe your primary hard drive.</p>
    <p>Properly deleting a drive will take time, if you’re in a hurry, you can at least use fast mode.</p>
    <p>First:</p>
    <div id="crayon-59a39d9a6d9cf517297318" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo apt-get secure-delete</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d9cf517297318-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d9cf517297318-1"><span class="crayon-h"> </span><span class="crayon-e">sudo </span><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-v">secure</span><span class="crayon-o">-</span><span class="crayon-v">delete</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    If you’re wiping a disk</p>
    <div id="crayon-59a39d9a6d9d4815819878" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    fdisk-l</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d9d4815819878-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d9d4815819878-1"><span class="crayon-v">fdisk</span><span class="crayon-o">-</span><span class="crayon-v">l</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    find the disk/partition name: should be /dev/sdxx<br/>
    at this point if you haven’t already, consider encrypting the partition, see veracrypt.<br/>
    wipe space considered free (-f is fast mode “insecure mode”)</p>
    <div id="crayon-59a39d9a6d9d7967549587" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo sfill /dev/sddisk#</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d9d7967549587-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d9d7967549587-1"><span class="crayon-h"> </span><span class="crayon-e">sudo </span><span class="crayon-v">sfill</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">dev</span><span class="crayon-o">/</span><span class="crayon-v">sddisk</span><span class="crayon-p">#</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    if you need to clear swap space-<br/>
    (-f is fast mode “insecure mode”)</p>
    <ol>
    <li>cat /proc/swaps</li>
    <li>sudo swapoff /dev/sddisk#</li>
    <li>sudo sswap /dev/sddisk#</li>
    <li>sudo swapon /dev/sdFdisk#</li>
    </ol>
    <p>if you are strapped for time, use -m for 7 passes or -s for simple 1 pass “insecure mode”</p>
    <div id="crayon-59a39d9a6d9db543830192" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo srm file</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d9db543830192-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d9db543830192-1"><span class="crayon-e">sudo </span><span class="crayon-e">srm </span><span class="crayon-v">file</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    or</p>
    <div id="crayon-59a39d9a6d9de685434288" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo srm -r /directory</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d9de685434288-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d9de685434288-1"><span class="crayon-h"> </span><span class="crayon-e">sudo </span><span class="crayon-v">srm</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-v">r</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">directory</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    or</p>
    <div id="crayon-59a39d9a6d9e0030677895" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    srm /dev/sddisk#</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d9e0030677895-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d9e0030677895-1"><span class="crayon-h"> </span><span class="crayon-v">srm</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">dev</span><span class="crayon-o">/</span><span class="crayon-v">sddisk</span><span class="crayon-p">#</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    At the end you may also be interested at the end to wipe memory on the system.<br/>
    (-f is fast mode “insecure mode)</p>
    <p>Enter:</p>
    <div id="crayon-59a39d9a6d9e4770026858" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo sdmem</textarea></div>
    <div class="crayon-main" style>
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59a39d9a6d9e4770026858-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59a39d9a6d9e4770026858-1"><span class="crayon-h"> </span><span class="crayon-e">sudo </span><span class="crayon-v">sdmem</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    <h3><a name="physical-destruction"></a>Physical Destruction</h3>
    <p>Try to at least encrypt the disk first, if you have time to spare, follow the instructions for disk erasure with <span class="caps">DBAN</span>.</p>
    <p>Open the drive. Find the platter, score it, smash it. Then you will need to locate any memory chips which may store cached files, and destroy them as well. This is an important step, and can be missed easily. Remember not to dispose in normal garbage as it’s not secure. Consider alternate means of disposable for best measure.</p>
    <p>Fun Fact: To “officially” destroy all remnants of magnetic data you’ll need to heat it to 1500 kelvin.</p>
    <h3><a name="cold-boot-attack"></a>Cold-Boot Attack</h3>
    <p>Older attack method recovering encryption keys stored in <span class="caps">RAM</span>. If possible use DDR3 or better memory. When not at the computer always shut down completely.</p>
    <p>Consider using Bleachbit or more advanced sdmem to wipe <span class="caps">RAM</span> contents.</p>
    <h3><a name="basic-communications"></a>Basic Communications</h3>
    <p>Keep in mind that your use of grammar, spelling and language can be used as identifying factors. It is possible to single you out based on your specific ways of communication and link you to other public content linked to your alternate identities. When attempting to communicate anonymously remember not to mention nicknames, locations favorite music, weather or any other information that can be used to reveal your identity. Something that seems mundane and friendly can quickly be used for identification.</p>
    <h3><a name="images"></a>Images</h3>
    <p><span class="caps">JPG</span>, <span class="caps">JPEG</span>, <span class="caps">TIF</span> and <span class="caps">WAV</span> files store <span class="caps">EXIF</span> data, or Exchangeable image file format, that can store sensitive information, including <span class="caps">GPS</span>-location, and the unique ID of the device used. It is recommended to always use the <span class="caps">PNG</span> format, and scrub any metadata, if you need to exchange an image. One option is the Metadata Anonymisation Toolkit that comes with <span class="caps">TAILS</span>, and also available at https://mat.boum.org/</p>
    <h3><a name="email-providers"></a>Email Providers</h3>
    <p>No mail provider can be trusted completely no matter what their security claims are. Utilize <span class="caps">PGP</span> as often as possible and utilize an anonymous connection when connecting.</p>
    <h3><a href="https://protonmail.ch/">protonmail.ch</a></h3>
    <p>Protonmail is currently invite only and requires a wait time of anywhere from a month or more to get in. However, it’s a highly respected secure email solution. You can employ <span class="caps">PGP</span> and encrypted storage. They have a favorable location</p>
    <h3><a href="https://tutanota.com/">Tutanota.com</a></h3>
    <p>Tutanota offers encrypted mail-storage and the use of a one time password, however <span class="caps">PGP</span> has to be done manually as there is no smtp or imap mail servers. They have a favorable location that is difficult to retrieve data from with legal orders.</p>
    <h3><a href="http://mail2tor.com/">mail2tor.com</a></h3>
    <p>While tor based mail providers have had a storied history. If <span class="caps">PGP</span> is utilized for all communications, the threat is eliminated. If you receive something compromising in plain text, don’t consider this information secure, and inform any correspondents to employ <span class="caps">PGP</span>.</p>
    <h3><a href="https://help.riseup.net/">riseup.net</a></h3>
    <p>United States based privacy centric collective that offers mail and other privacy capabilities.</p>
    <h3><a href="https://www.openmailbox.org/">openmailbox.org</a></h3>
    <p>free, secure email provider</p>
    <h3><a href="https://www.startmail.com/">startmail.com</a></h3>
    <p>paid email<br/>
    pgp webmail client<br/>
    offshore hosting more protected from spying</p>
    <h3><a href="https://www.vmail.me/en/">vmail.me</a></h3>
    <p>free, no personal information<br/>
    account deletion<br/>
    encrypted data storage<br/>
    user details like ip address and user agent stripped from headers</p>
    <h3><a href="http://www.autistici.org">autistici</a></h3>
    <p>privacy centric collective offering email, hosting, vpn and other anonymity service</p>
    <h3><a name="jabber_xmpp-otr"></a>Jabber_XMPP/<span class="caps">OTR</span></h3>
    <ol>
    <li>sudo apt-get install pidgin</li>
    <li>go to tools→preferences</li>
    <li>Logging: disable log all instant messages/log all chats</li>
    <li>Go to proxy</li>
    <li>Select Socks 4</li>
    <li>enter: 127.0.0.1 9050</li>
    <li><a href="https://developer.pidgin.im/wiki/ThirdPartyPlugins">Go to this link</a></li>
    <li>Under Security</li>
    <li>Download/Install: Off-The-Record, Pidgin-<span class="caps">GPG</span></li>
    <li>Install any dependencies Activate Plugins in: Tools→Plugins</li>
    <li>Once activated, select configure plugin for both</li>
    </ol>
    <h3>For <span class="caps">OTR</span></h3>
    <ol>
    <li>you will need to generate a unique key</li>
    <li>Enable Private messaging</li>
    <li>Disable logging</li>
    <li>Automatically initiate private messaging (optional)</li>
    <li>Select show <span class="caps">OTR</span> in tool-bar</li>
    <li>If a conversation is not private you will see a box saying Not Private</li>
    <li>Click Start Private Conversation</li>
    <li>If your partner has <span class="caps">OTR</span> properly configured it will display private.</li>
    </ol>
    <h3>For Pidgin-<span class="caps">GPG</span></h3>
    <ol>
    <li>select main key in options</li>
    <li>toggle encryption mode in conversations:</li>
    <li>options→toggle openpgp encryption</li>
    </ol>
    <h3><a name="alternative-messaging-options"></a>Alternative Messaging Options</h3>
    <h3>pond (<a href="https://pond.imperialviolet.org/">pond.imperialviolet.org)</a></h3>
    <p>forward secure, asynchronous messaging for the discerning. Pond messages are asynchronous, but are not a record; they expire automatically a week after they are received. Pond seeks to prevent leaking traffic information against everyone except a global passive attacker.</p>
    <h3><a href="https://scramble.io/">scramble</a>.io</h3>
    <p>secure messaging between scramble users</p>
    <h3><a href="https://bitmessage.org/wiki/Main_Page">bitmessage.org</a></h3>
    <p>p2p encrypted messaging, like sending messages as Bitcoins</p>
    <h3><a href="https://bitmessage.ch/">bitmessage.ch</a> (tor and i2p urls available)</h3>
    <p>webmail gateway for bitmessage with instant send to other users with @bitmessage.ch address</p>
    <h3><a name="gnupg-pgp-basics"></a><span class="caps">GNUPG</span>/<span class="caps">PGP</span> Basics</h3>
    <p>A <span class="caps">PGP</span> Key is a unique identifier, do not re-use across accounts and especially not with any public address.<br/>
    Simple <span class="caps">PGP</span> On Linux<br/>
    terminal<br/>
    Ubuntu- sudo apt-get install gpa gnupg2<br/>
    Arch- sudo pacman -s gpa gnupg2</p>
    <p>Generating Keys-</p>
    <ol>
    <li>in terminal enter: gpg –gen-key or open gpa in terminal and it will prompt you to create one.</li>
    <li>follow the prompts</li>
    </ol>
    <p>in most cases select option 1 – <span class="caps">RSA</span> and <span class="caps">RSA</span> (default)<br/>
    select at least 2048 key size<br/>
    key expiration, hit enter if not needed.<br/>
    do not enter real information for contact (unless intended)<br/>
    use a secure passphrase for the key<br/>
    it will then ask you to move the mouse, type etc to create entropy</p>
    <p>Simple <span class="caps">PGP</span> with <span class="caps">GNU</span> Privacy Assistant</p>
    <p>If you open gpa it will guide you through creating your first key<br/>
    don’t put real information unless intended, obviously<a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa11.png"><img class="aligncenter size-full wp-image-10781" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa11.png" alt="gpa1[1]" width="393" height="155" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa11.png 393w, https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa11-300x118.png 300w" sizes="(max-width: 393px) 100vw, 393px"/></a><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa21.png"><img class="aligncenter size-full wp-image-10782" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa21.png" alt="gpa2[1]" width="706" height="741" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa21.png 706w, https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa21-286x300.png 286w" sizes="(max-width: 706px) 100vw, 706px"/></a>Either click refresh or restart gpa and the keys will appear<br/>
    Click the clipboard</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa71.png"><img class="aligncenter size-full wp-image-10783" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa71.png" alt="gpa7[1]" width="675" height="175" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa71.png 675w, https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa71-300x78.png 300w" sizes="(max-width: 675px) 100vw, 675px"/></a>Enter your message</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa81.png"><img class="aligncenter size-full wp-image-10784" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa81.png" alt="gpa8[1]" width="628" height="506" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa81.png 628w, https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa81-300x242.png 300w" sizes="(max-width: 628px) 100vw, 628px"/></a>Select the key you wish to sign it with</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa91.png"><img class="aligncenter size-full wp-image-10785" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa91.png" alt="gpa9[1]" width="408" height="552" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa91.png 408w, https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa91-222x300.png 222w" sizes="(max-width: 408px) 100vw, 408px"/></a><br/>
    You will now see an encrypted message.<br/>
    To decrypt a message click the mail icon with the key, and it will allow you to choose the appropriate key.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa101.png"><img class="aligncenter size-full wp-image-10786" src="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa101.png" alt="gpa10[1]" width="628" height="508" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa101.png 628w, https://www.deepdotweb.com/wp-content/uploads/2015/06/gpa101-300x243.png 300w" sizes="(max-width: 628px) 100vw, 628px"/></a></p>
    <p><strong>More details on <span class="caps">GPA</span></strong></p>
    <p>Exporting/Importing Public Key<br/>
    gpa</p>
    <ol>
    <li>select your key-pair, and then select keys→export or import keys and proceed</li>
    </ol>
    <p>Exporting/Importing Private Key<br/>
    gpa</p>
    <ol>
    <li>select your key-pair, and then select→keys→export or import keys and proceed</li>
    <li>either choose where to save or paste the desired key</li>
    </ol>
    <p>Verifying a message<br/>
    gpa</p>
    <ol>
    <li>select→keys→imports</li>
    <li>paste the public key</li>
    <li>Select window→clipboard</li>
    <li>Paste the entire text</li>
    <li>Click icon with the green key (hover over for title if hard to see)</li>
    <li>If the information is genuine it will display the name of the previously imported public key.</li>
    </ol>
    <p>Verify a file</p>
    <ol>
    <li>gpa</li>
    <li>select→keys→import</li>
    <li>paste the public key</li>
    <li>back to terminal</li>
    <li>gpg —verify file</li>
    </ol>
    <p><span class="caps">PGP</span> with Email<br/>
    Thunderbird is probably the most widely known, if you prefer reference the Ubuntu guide below which explains alternates.</p>
    <ol>
    <li>sudo apt-get install thunderbird enigmail</li>
    <li>Open Thunderbird</li>
    <li>Open Preferences→enigmail→Preferences</li>
    <li>Set the <span class="caps">GPG</span> path, in Ubuntu default is /usr/bin/gpg</li>
    </ol>
    <p>You can also cut and paste your messages from <span class="caps">GPA</span> into the message window.</p>
    <h3><a name="tails-pgp"></a><span class="caps">TAILS</span> <span class="caps">PGP</span></h3>
    <p><span class="caps">TAILS</span> has an OpenPGP Applet &#8211; <a href="https://tails.boum.org/doc/encryption_and_privacy/gpgapplet/public-key_cryptography/index.en.html">Visual Guide</a></p>
    <h3><a name="additional-reading-on-pgp"></a>Additional reading on <span class="caps">PGP</span></h3>
    <p>Recommended Best Practices for <span class="caps">PGP</span> from <a href="https://help.riseup.net/en/security/message-security/openpgp/best-practices">Riseup.net</a> or:<br/>
    http://nzh3fv6jc6jskki3.onion/en/security/message-security/openpgp/best-practices</p>
    <p>Additional Reading:</p>
    <ul>
    <li><a href="https://help.ubuntu.com/community/GnuPrivacyGuardHowto">GnuPrivacyGuardHowto</a></li>
    <li><a href="http://www.math.utah.edu/%7Ebeebe/PGP-notes.html">PGP (Pretty Good Privacy) and GnuPG (GNU Privacy Guard) notes </a></li>
    </ul>
    <h3><a name="pgp-versions"></a><span class="caps">PGP</span> Versions</h3>
    <p><span class="caps">PGP</span> Versions can reveal the users operating system, and you should research strange versions as some <span class="caps">PGP</span> Libraries are known to have weak encryption.</p>
    <h3><a name="validating-files-with-md5-or-sha1"></a>Validating Files with MD5 or SHA1:</h3>
    <h3><a name="sha1-sum"></a>SHA1 Sum</h3>
    <p>When the file is provided ideally a SHA1/MD5/<span class="caps">PGP</span> Sum will be provided. It will look like a long string of characters.<br/>
    In Linux terminal type: sha1sum filename<br/>
    The output should be the same as the supplied string.</p>
    <h3><a name="md5-sum"></a>MD5 Sum</h3>
    <p>When a file is provided ideally an SHA1/MD5/<span class="caps">PGP</span> Sum will be provided. It will look like a long string of characters.<br/>
    In Linux terminal type: md5sum filename<br/>
    The output should be the same as the supplied string.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/advanced/" rel="tag">advanced</a> <a href="https://www.deepdotweb.com/tag/anonymity/" rel="tag">anonymity</a> <a href="https://www.deepdotweb.com/tag/linux/" rel="tag">linux</a> <a href="https://www.deepdotweb.com/tag/privacy/" rel="tag">privacy</a> <a href="https://www.deepdotweb.com/tag/users/" rel="tag">users</a></span> <span style="display:none" class="updated">2015-06-15</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/admin/" title="Posts by DeepDotWeb" rel="author">DeepDotWeb</a></strong></div>
    </div>
</article>

