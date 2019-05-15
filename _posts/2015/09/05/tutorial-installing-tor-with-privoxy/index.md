---
title: "Tutorial: Installing Tor With Privoxy"
---

Posted by: Jack Meyer 

<span>September 5, 2015</span>




<p>When it comes to keeping your activities out of the prying-eyes of Evil-Alphabet-Agency&#8217;s, one must not slack on beefing up security on both their computer&#8217;s and networks. The consequences for those who are involved are just too serious to take lightly. If you are accessing the Dark Net at home at all, there&#8217;s a few simple steps you can take to ensure you&#8217;re anonymity stays a secret. In this tutorial I am going to go over installing and configuring tor, privoxy, and a free <a href="/vpn-comparison-chart/">VPN</a>.</p>
<p style="text-align: center;"><a href="/vpn-comparison-chart/">&gt;&gt;Hide Your Tor Usage: Click Here For VPN&#8217;s Who Respect Your Privacy&lt;&lt;</a></p>
<p>First of all, absolutely do not use Windows thinking it&#8217;s safe. Use Windows at your own risk, I am not going to chance it. Especially when it is publicly known that since the release of Windows Seven Microsoft has been working the NSA, installing secret back doors to pretty much what ever they could scare people in to doing. The NSA can access everything that is accessible on the windows partition of your machine if its not encrypted (Yes, you can remove the back doors within Windows, but that is to say, you can remove the ones that we KNOW about, and I would not put it past the NSA to have a few tricks up their sleeves) I prefer using Linux anyway, I understand that some have difficulties making the transition from Windows to Linux, but that&#8217;s why they created man pages, my friend.</p>
<p>(If you don&#8217;t know what a command does, just type man &lt;COMMAND&gt; in a terminal, read the manual page, and you&#8217;re good to go. Honestly, once you use any flavor of Linux for a while, the scripting will come naturally and Windows will become obsolete (well aside from a small, encrypted partition for what ever Windows applications you can not live with out, but please do make sure you encrypt you hard-drives and make sure you disable WPS on your modems and routers and such (because it is a lot easier to crack a WPS key than to sniff out a handshake sequence, then crack that against a .pcap sniffing file). In windows, use <a href="/2015/02/09/veracrypt-tutorial-how-to-encrypt-usb-drive/">Veracrypt</a>, and while installing Linux, wipe the disk completely and encrypt it all with VSLM. Of course back ups should be made first, but an encrypted hard-drive really give me piece of mind. I do not do anything illegal even I just get sick when I think about Government Agents who are supposed to protect us, pilfering through my computers, and precipitating the demise of American&#8217;s Right to Privacy. Since 9/11. they have basically made The Right To Privacy a joke, and it was done in the name of Patriotism. My retort to their Ranging Rover Taps and Legalized Racism.</p>
<p>Anyway, so now to the technical stuff (Sorry it&#8217;s kind of boring, but our Right To Privacy as a Nation is at stake, not to mention our personal freedoms (which is a really good reason to put up with the boring) If we don&#8217;t take a stand and take hold of this situation now, privacy as we know it will become another yet another causality of war.</p>
<p>I am defiantly not here to tell you what you should do, mind you, just here to urge you to do something. As for which flavor of Linux you should (if you&#8217;re not already using one), I would recommend Kali-Linux. It is Debian-based (which even if you don&#8217;t know already, it&#8217;s still way worth it to get use to Debian-based distributions (because Ubuntu is cool or what not, but, all the sudooing is tiresome) and plus Kali is a security-auditing distribution of Linux, meaning it can easily achieve the things we need it for. You can install the same things on any distribution of Linux, it just may require a little more reading (but if you use Kali you can just follow these steps and then you&#8217;re good to go.</p>
<p>Now you should download what ever Kali*.iso is compatible with your machine (32 or 64 bit, AMD or Intel, etc) from Offense Security, install it and I recommend completely wiping your system (unless it is good already :) and encrypting the entire hard-drive with VSLM. It is an option when installing, do it, just remember the key you use because if you forget it it&#8217;ll will be a hassle.</p>
<p>After the install, go to this website and follow these instructions (things like installing the proper audio-drivers, which is a trademark problem of Debian-based flavors, but the pros defiantly outweigh the cons here, defiantly. <a href="http://www.blackmoreops.com/2014/03/03/20-things-installing-kali-linux/">This</a> is the url you need. After those things are done, we need to install Viadalia (the gui-front-end-to-Tor), tor itself, privoxy, proxy-chains, and open dns (to prevent people from being able to see the dns address of the ISP you use). Also when making pgp keys please don&#8217;t put your normal email address, I recommend trying to figure out how i2p email or FreeNet mail works (kind of easier said than done, but the reward will be piece of mind and a clean, anonymous email address, because they are more secure than using a Gmail account, for example. Also, if you use your computer at home for accessing the DarkWeb, I highly recommend the use a VPN with these measures, then I would consider it pretty safe, or at least, way too much of a hassle for people to go through.</p>
<p>In prompt, type $&#8217;sudo -s&#8217; for a root shell, enter your password, then enter these commands as Root:</p>

    #apt-get install network-manager-openvpn-gnome
    #apt-get install network-manager-pptp
    #apt-get install network-manager-pptp-gnome
    #apt-get install network-manager-strongswan
    #apt-get install network-manager-vpnc
    #apt-get install network-manager-vpnc-gnome/etc/init.d/network-manager restart</textarea></div>

    
<p>
    The after that, use this server (for US, for other country&#8217;s just google it.)</p>

    Server: us.justfreevpn.com
    PPTP Username: justfreevpn
    PPTP Password: USA Free VPN Account</textarea></div>

    
<p>
    That will configure your VPN properally, now to install tor and the other tools (and to make sure they are working properly).</p>

    #apt-get install tor
    
    #apt-get update
    
    #apt-get install privoxy
    
    #apt-get update
    
    #apt-get install vidalia
    
    #apt-get update</textarea></div>

    
<p>
    Now, we have to edit a configureation file, simply type</p>

    #leafpad /etc/privoxy/config</textarea></div>

    
<p>
    And go down to line (it was 699 on my config file)</p>

    697 # Default Value:
    
    698 #
    
    699 # 127.0.0.1:8118
    
    700 #</textarea></div>

    
<p>
    Now, take the # sign out of line 699 and make it read</p>

    699: listen-address 127.0.0.1:8118</textarea></div>

    
<p>
    And then go to the very bottom of the file, and add these lines:</p>

    forward-socks4     /     127.0.0.1:9050 .
    
    forwardsocks4a   /     127.0.0.1:9050 .</textarea></div>

    
<p>
    *Make sure you put a period at the end of the address:port combination. (Copying and pasting would probably be how I would do it) I forgot that once and it took a while to realize what I had done wrong. We are almsost finished! Now Type,</p>

    #leafpad /etc/tor/torrc
    
    #service privoxy stop &amp;&amp; service tor stop
    
    #service privoxy start &amp;&amp; service tor start-tor</textarea></div>

    
<p>
    Now, you need to set you browser to use the proxy (or just download the add-on FoxyProxyStandart and once installed Go &gt; File &gt; Tor Wizard, and just choose the options that come (all you have to is hit enter, then chose that proxy configuration you just made, and go to Google and search am I using Tor. Assuming you were successful, there is just one last step.</p>

    #leafpad /etc/tor/torric and put this line at the end of the file: “DNSPort 53”</textarea></div>

    
<p>
    Then, you save it, and #leafpad /etc/resolv.conf, delete everything in the file (it&#8217;s about three to five lines in length), and replace it “nameserver 127.0.0.1”, then save it.</p>
<p>If it were me I would just restart the computer (to see if Tor and Privoxy are both installed and starting during the other init.d daemons.) but you could just restart the services, but you&#8217;re through the process now. To make sure you are safe, check out “<a href="http://www.ipchicken.com/">http://www.ipchicken.com</a>” or “<a href="https://www.whatismyip.com/">https://www.whatismyip.com</a>” and make sure both your current IP Address is masked as well as you&#8217;re ISP&#8217;s DNS is hidden as well. This is an example of a properly configured box:</p>
<p><a href="/imgs/2015/05/privtor.png"><img class="aligncenter wp-image-10265" src="/imgs/2015/05/privtor.png" alt="privtor" width="1058" height="595" srcset="/imgs/2015/05/privtor.png 1366w, /imgs/2015/05/privtor-300x169.png 300w, /imgs/2015/05/privtor-1024x576.png 1024w" sizes="(max-width: 1058px) 100vw, 1058px"/></a></p>

Updated: 2015-09-05

