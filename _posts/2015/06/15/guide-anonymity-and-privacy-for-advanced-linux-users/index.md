---
title: "Guide: Anonymity and Privacy for Advanced Linux Users"
---

   
Posted by: DeepDotWeb

<span>June 15, 2015</span>

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
sudo ufw status</textarea></div>

<p>


<img src="/imgs/2015/06/ufwbasics21.png">

<p>you can see I’ve blocked some specific ports in this example</p>
<p>For more advanced configuration <a href="https://help.ubuntu.com/community/UFW">visit</a>.</p>
<h3><a name="changing-mac-address"></a>Changing <span class="caps">MAC</span> Address</h3>
<p>A <span class="caps">MAC</span> Address is a hardware specific identifier for you network interface. In some cases it may be useful to change your mac address to avoid detection.</p>
<p><a href="https://wiki.archlinux.org/index.php/MAC_address_spoofing">Arch Linux Guide</a>:</p>
sudo apt-get install macchanger
    for a gui
    sudo apt-get install macchange-gtk</textarea></div>

<p>
    With macchanger-gtk</p>

<img src="/imgs/2015/06/macchanger-gtk1.png">

<p>heck your current mac addresses for future reference</p>
macchanger eth0
    macchanger wlan0</textarea></div>

<p>
    for a random macaddress</p>
sudo ifconfig wlan0 down</textarea></div>

<p>
    sudo macchanger -r wlan0</textarea></div>

<p>
    This will change the mac address to a random value</p>
macchanger -e wlan0</textarea></div>

<p>
    will change the mac address but keep it as the same vendor. This can be useful if you’re spoofing your address but you don’t want it obviously coming from a device not on the network.</p>
sudo macchanger -A wlan0</textarea></div>

<p>
    This will change the devices <span class="caps">MAC</span> to a random <span class="caps">MAC</span> of any kind, regardless of the original device.</p>
sudo macchanger —mac=XX:XX:XX:XX:XX:XX interface</textarea></div>

<p>
    Will change to a specific mac address of your choice</p>
<p>You may want to write a script to start automatically on network manager start, and network manager shut down.</p>
sudo nano /etc/init/macchanger.conf</textarea></div>

<p>
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

<p>
    you can switch out -A for -r or whatever other configuration you might want.</p>
sudo nano /etc/network/if-post-down.d/random-mac</textarea></div>

<p>
    #!/bin/sh
    
    MACCHANGER=/usr/bin/macchanger
    
    [ "$IFACE" != "lo" ] || exit 0
    
    # Bring down interface (for wireless cards that are up to scan for networks), change MAC address to a random vendor address, bring up the interface
    /sbin/ifconfig "$IFACE" down
    macchanger -A "$IFACE"
</textarea></div>

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

<img src="/imgs/2015/06/veracrypt11.png">

<p>Select Create an Encrypted File Container</p>

<img src="/imgs/2015/06/veracrypt21.png">

    Select Hidden Veracrypt volume</p>

<img src="/imgs/2015/06/veracrypt31.png">

    Choose volume location and select never save history:</p>

<img src="/imgs/2015/06/veracrypt41.png">

    Select your encryption algorithm, <span class="caps">AES</span> is fine, but you may chose more secure<br/>
    Select Hash Algorithm, <span class="caps">SHA</span>-512 is sufficient</p>

<img src="/imgs/2015/06/veracrypt51.png">

    Select Use Key files and click the key files box… <strong>optional:</strong></p>
<p>&nbsp;</p>

<img src="/imgs/2015/06/veracrypt61.png">

    Generate save the new key.</p>

<img src="/imgs/2015/06/veracrypt71.png">

    Click add files and add the key<br/>
    Click Generate Random Keyfile box if you want another key<br/>
    You may also use existing keys:</p>

<img src="/imgs/2015/06/veracrypt81.png">

    Click format to create the volume that will be visible:</p>

<img src="/imgs/2015/06/veracrypt101.png">

    Now it’s recommended to load this volume with contents that appear sensitive</p>

<img src="/imgs/2015/06/veracrypt111.png">

    You will follow the same steps, remember this is the hidden volume consider it’s security most important.</p>

<img src="/imgs/2015/06/veracrypt121.png">

    When complete you will see this warning, read it carefully.</p>

<img src="/imgs/2015/06/veracrypt131.png">

<h2>Browsers</h2>
<h3>Tor Browser</h3>
<p>Download at: <a href="https://torproject.org">torproject.org</a></p>
<p>All Tor network addresses will be followed with .onion, not .com. It is far more secure browsing .onion services.</p>
<p>In depth explanation of Tor <a href="https://media.torproject.org/video/tor-internet-days-2010.mp4">by its head developer Arma</a>.</p>
<p>Once you’ve download tor browser, expand the zipped file. Then</p>
cd tordirectory
    ./start-tor-browser.desktop</textarea></div>

<p>


<img src="/imgs/2015/06/starttor1.png">

<p>Forbidding javascript and other elements can make web browsing less convenient, but by allowing more elements you open yourself to potential vulnerabilities. It’s best to find the best possible security setting you can withstand while the web browsing experience is still functional.</p>
<p><strong>Configuring Security Settings</strong></p>
<p>Privacy and security settings can be easily configured. Click on the Onion in the top left.</p>

<img src="/imgs/2015/06/toronion_large1.png">

<p>Select “Privacy and Security Settings” Adjust the slider to your desired level of security.</p>

<img src="/imgs/2015/06/torprivacysettings1.png">

<p><strong>Noscript basics</strong></p>
<p>Depending on your security level selected in Tor, Noscript may not provide any advantage. That main advantage of Noscript is it’s easier to tailor allowing on specific sites, or for specific elements on the fly. Click the S in the Top Left next to the Tor Onion symbol and select forbid scripts globally. You should see a red line across the S. If you allow specific sites, you should check that the red line is there for those you do not allow. Allowing only specific sites may create a fingerprint of your activity. There are some advanced settings under options worth taking a look at.</p>

<img src="/imgs/2015/06/tornoscripts_large1.png">

<h2>Tor bridge</h2>
<p>in some cases if Tor is blocked or you wish to conceal the use of Tor a bridge can be configured. This makes it more difficult for an <span class="caps">ISP</span> to detect Tor. Bridges can help avoid censorship, and if your <span class="caps">ISP</span> Blocks Tor Traffic it is much more difficult to detect the nature of the traffic unless deep packet inspection is employed. It’s one of those things that since it’s there, might as well set it up as a per-cautionary measure and see if your connection is still, reliable and fast enough for your standards.</p>
<ul>
<li>Click Open Settings on the Pop-up Connection Box

<img src="/imgs/2015/06/torconnectionpopup1.png">

</a></li>
<li>Click configure<br/>


<img src="/imgs/2015/06/torconfigurebridge1.png">

<li>Select Yes to <span class="caps">ISP</span> Censors or Blocks

<img src="/imgs/2015/06/torispblocks1.png">

<li>obfs3 is fine, see below for information on other options.<br/>


<img src="/imgs/2015/06/torselectbridge1.png">

<li>Most likely just skip use a local proxy</li>
<li>Click connect

<img src="/imgs/2015/06/torconnectbridge1.png">

</ul>
<p>Optionally if Tor is already started you can:</p>
<ul>
<li>click the onoin icon in the top left of the browser and select</li>
<li>Open Network Settings</li>
<li>check My <span class="caps">ISP</span> Blocks Connections and hit OK.

<img src="/imgs/2015/06/torbridgeselect1.png">

<li>Use obfs 3 which is recommended, see next section on other types.</li>
</ul>
<h3>Pluggable Transports</h3>
<p>Pluggable Transports are extensions to Tor which utilize it’s pluggable transport <span class="caps">API</span>. These are more advanced ways to disguise traffic flow, for instance making it appear as skype traffic or utilizing a flash proxy. Many are now included in the Bridge Option Menu, so this is a good resource to learn more about the specifics. Some may require <a href="https://www.torproject.org/docs/pluggable-transports.html.en#download">custom installation</a>.</p>
<h3>Firefox</h3>
<p>If you need to use another browser Firefox is preferred. Here are some configuration settings and extensions that can be helpful.</p>
<p><strong>Optional Configuration:</strong></p>
<p>In the <span class="caps">URL</span> Bar enter: about:config</p>

<img src="/imgs/2015/06/aboutconfigbasics1.png">

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

<img src="/imgs/2015/06/networksettings1.png">

<p>One main issue is your firewall or router is blocking connections. Click networking.</p>

<img src="/imgs/2015/06/ports1.png">

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
<a href="/vpn-comparison-chart/">Our Best VPN&#8217;s Chart</a> and &#8220;<a href="/2014/07/08/is-your-vpn-legit-or-shit/">Is your VPN legit or shit?</a>&#8221; post (remember their claims, are not a promise and even their systems could be vulnerable)</p>
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

<img src="/imgs/2015/06/proxychains1.png">

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

<img src="/imgs/2015/06/tails11.png">

    Name your VM and select Linux 64bit or 32bit depending on which you downloaded:</p>

<img src="/imgs/2015/06/tails21.png">

    Set memory size at least 1024 for smooth performance</p>

<img src="/imgs/2015/06/tails31.png">

    Create a virtual hard drive</p>

<img src="/imgs/2015/06/tails41.png">

    VDI</span> Image is suitable</p>

<img src="/imgs/2015/06/tails51.png">

    You can select dynamically allocated and set a starting amount at a couple gigabytes</p>

<img src="/imgs/2015/06/tails61.png">

    Select the image and click start</p>

<img src="/imgs/2015/06/tails81.png">

    Select the location of the .iso file you downloaded.</p>

<img src="/imgs/2015/06/tails71.png">

    Once started go to Applications→Tails→Tails Installer</p>

<img src="/imgs/2015/06/tails91.png">

    Make sure the <span class="caps">USB</span> Drive is present you will see a green plus, over the usb icon in this image</p>

<img src="/imgs/2015/06/tails101.png">

    Select clone and install and follow the steps for installation</p>

<img src="/imgs/2015/06/tails111.png">

    Once you’ve started tails you can create a persistent volume to store static content</p>

<img src="/imgs/2015/06/tails121.png">

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

<img src="/imgs/2015/06/whonix11.png">

    Keep the settings default and click import</p>

<img src="/imgs/2015/06/whonix21.png">

    Repeat for workstation, select the .ova</p>

<img src="/imgs/2015/06/whonix31.png">

    Import without changing settings</p>

<img src="/imgs/2015/06/whonix41.png">

    Select both and start both at the same time.</p>

<img src="/imgs/2015/06/whonix51.png">

    Once workstation has finished booting you will see this screen.</p>

<img src="/imgs/2015/06/whonix61.png">

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

<img src="/imgs/2015/06/bleachbit11.png">

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
sudo apt-get secure-delete</textarea></div>

<p>
    If you’re wiping a disk</p>
fdisk-l</textarea></div>

<p>
    find the disk/partition name: should be /dev/sdxx<br/>
    at this point if you haven’t already, consider encrypting the partition, see veracrypt.<br/>
    wipe space considered free (-f is fast mode “insecure mode”)</p>
sudo sfill /dev/sddisk#</textarea></div>

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
sudo srm file</textarea></div>

<p>
    or</p>
sudo srm -r /directory</textarea></div>

<p>
    or</p>
srm /dev/sddisk#</textarea></div>

<p>
    At the end you may also be interested at the end to wipe memory on the system.<br/>
    (-f is fast mode “insecure mode)</p>
<p>Enter:</p>
sudo sdmem</textarea></div>

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
    don’t put real information unless intended, obviously

<img src="/imgs/2015/06/gpa11.png">

    Click the clipboard</p>

<img src="/imgs/2015/06/gpa71.png">


<img src="/imgs/2015/06/gpa81.png">


<img src="/imgs/2015/06/gpa91.png">

    You will now see an encrypted message.<br/>
    To decrypt a message click the mail icon with the key, and it will allow you to choose the appropriate key.</p>

<img src="/imgs/2015/06/gpa101.png">

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


Updated: 2015-06-15

