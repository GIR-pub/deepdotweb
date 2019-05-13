---
How To Use VPN Plus Tor To Get Double Encryption?
---
<article class="post-listing post-11017 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-double tag-encryption tag-tor tag-vpn">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/admin/" title="">DeepDotWeb </a></span>
    <span>July 14, 2015</span>
    
    <span><a href="https://www.deepdotweb.com/2015/07/14/how-to-use-vpn-plus-tor-to-get-double-encryption/#comments">33 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p><em>Guest post by <a href="https://privatoria.net/">privatoria.net:</a></em></p>
    <p>Tor is a great solution for people looking for on-line privacy and anonymity. Keeping all the positive sides of Tor in a mind one also has to take its vulnerabilities into account as well. Among those are incompatibility with P2P downloads and variable connection speed (it all depends on the exact Tor node you connect to every time). There is a solution to stay with Tor and forget about all of its weak points. In this article we showcase how to use popular Tor technology with good old VPN technology.</p>
    <p style="text-align: center;"><a href="https://www.deepdotweb.com/vpn-comparison-chart/">&#8211;&gt; Click here to see the best VPN&#8217;s for privacy &lt;&#8211;</a></p>
    <p><strong>Advantages of using VPN plus Tor:</strong></p>
    <ul>
    <li>Hide the fact of using Tor from your ISP</li>
    <li>If your traffic is being monitored by a malicious Tor exit node, it will see only IP address of your VPN provider. It therefore provides an additional level of privacy.</li>
    </ul>
    <p>So, using VPN plus Tor will help us achieve double security and avoid corrupted Tor nodes.</p>
    <p><strong>What are the ways to use VPN through Tor?</strong></p>
    <p><a href="https://tails.boum.org/"><strong>Tails OS</strong></a></p>
    <p>This is one of the most popular security-oriented operating systems that you can get on-line for free. It is based on Linux and offers old-school user interface. It is not the best-looking OS in the world, but it takes your security extremely seriously. It offers certain features to provide secured web experience:</p>
    <ul>
    <li>Tor web browser (Iceweasel) is installed by default</li>
    <li>All data is stored in RAM (which means it all get deleted when you power off the system)</li>
    <li>It comes with whole range of open sourced security tools that will be helpful to any Internet user with privacy concerns</li>
    </ul>
    <p>Some users would claim that this OS is not something you can use on a daily basis. To some extend that might be true. OS developers do not advise to use it every day, however stating that you have to start a new session for every task in order to have the best security.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/07/1-tails.png"><img class="aligncenter wp-image-11018" src="https://www.deepdotweb.com/wp-content/uploads/2015/07/1-tails.png" alt="1-tails" width="536" height="335" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/07/1-tails.png 1280w, https://www.deepdotweb.com/wp-content/uploads/2015/07/1-tails-300x188.png 300w, https://www.deepdotweb.com/wp-content/uploads/2015/07/1-tails-1024x640.png 1024w" sizes="(max-width: 536px) 100vw, 536px"/></a></p>
    <p><strong>Use VPN+TOR in Tails OS</strong></p>
    <p>Using VPN+TOR does not differ from using a stand alone VPN in any Linux-based system. We recommend utilizing OpenVPN protocol. Once OpenVPN daemon is installed, launch it to activate VPN connection. After that you can run Iceweasel and use Tor as if you were using just that. One major downside to this method is that both Tor and VPN go through the same channel, which might decrease your connection speed. You also do not isolate your VPN connection from Tor, which provides lower security level and gives additional loophole that can be used by an attacker.</p>
    <p><a href="https://www.whonix.org/"><strong>Whonix</strong></a></p>
    <p>This OS runs inside a virtual environment to prevent any DNS leaks. In fact, two separate virtual machines are needed to get this thing to work:</p>
    <ul>
    <li>Tor gateway Virtual Machine</li>
    <li>Workstation virtual machine</li>
    </ul>
    <p>Tor gateway VM uses host OS&#8217;s network hardware and connect directly to Internet via NAT. Once connection is established it starts to force all traffic through Tor nodes and that&#8217;s what this is really all about. The Workstation VM is connected to Tor gateway VM and that&#8217;s the only way it gets Internet connectivity. So now we can route all our Internet traffic through Tor without Tor browser. The only downside to this is that you need to get a relatively powerful computer to actually make this work as you will be running 3 OS&#8217;s (1 host and 2 VM&#8217;s) at the same time.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/07/2-whonix.jpg"><img class="aligncenter wp-image-11019" src="https://www.deepdotweb.com/wp-content/uploads/2015/07/2-whonix.jpg" alt="2-whonix" width="461" height="597" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/07/2-whonix.jpg 741w, https://www.deepdotweb.com/wp-content/uploads/2015/07/2-whonix-232x300.jpg 232w" sizes="(max-width: 461px) 100vw, 461px"/></a></p>
    <p><strong>VPN+TOR in Whonix</strong></p>
    <p>Unfortunately, we were not able to set up a reliable VPN+TOR connection on Whonix OS. The reason for that is Tor gateway VM that routes 100% of system traffic through Tor nodes. OS architecture does not provide the functionality to utilize both Tor and VPN at the same time. Activating VPN on a Workstation VM will most likely kill Internet connection. Whonix is still a great solution for Tor enthusiasts.</p>
    <p><strong>Ready to go VPN+TOR solution</strong></p>
    <p>There is a way to get a VPN to work with TOR without specific browsers, VM&#8217;s and OS&#8217;s. Great example is <a href="https://privatoria.net/vpn-tor/">Privatoria&#8217;s VPN plus TOR</a>. The way it works is simple that makes it a must-try.</p>
    <p>The request is sent from the user machine to the VPN server via secure encrypted channel. The VPN server routes that traffic through Tor net using random Tor nodes to provide optimal security.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2015/07/3-vpn.jpg"><img class="aligncenter wp-image-11020" src="https://www.deepdotweb.com/wp-content/uploads/2015/07/3-vpn.jpg" alt="3-vpn" width="682" height="262" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/07/3-vpn.jpg 1057w, https://www.deepdotweb.com/wp-content/uploads/2015/07/3-vpn-300x115.jpg 300w, https://www.deepdotweb.com/wp-content/uploads/2015/07/3-vpn-1024x393.jpg 1024w" sizes="(max-width: 682px) 100vw, 682px"/></a></p>
    <p>This scheme has a lot to offer, most notably:</p>
    <ul>
    <li>It will let you use VPN+TOR the right way with each of them having their own channels to get better security and speed</li>
    <li>It will spare you from the installation pains</li>
    <li>It works with any OS&#8217;s and browsers</li>
    <li>It will ensure seamless experience without breaks due to dynamically changing nodes with checking their quality in real time</li>
    </ul>
    <p>Here&#8217;s how you can configure VPN+TOR on any Debian/Ubuntu based Linux distro:</p>
    <p>Open your terminal emulator and type in</p>
    <div id="crayon-5962a06116250560997835" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo apt-get install openvpn</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5962a06116250560997835-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5962a06116250560997835-1"><span class="crayon-e">sudo </span><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-e">install </span><span class="crayon-v">openvpn</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    <a href="https://www.deepdotweb.com/wp-content/uploads/2015/07/42.png"><img class="aligncenter size-full wp-image-11021" src="https://www.deepdotweb.com/wp-content/uploads/2015/07/42.png" alt="4" width="896" height="249" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/07/42.png 896w, https://www.deepdotweb.com/wp-content/uploads/2015/07/42-300x83.png 300w" sizes="(max-width: 896px) 100vw, 896px"/></a></p>
    <div id="crayon-5962a0611625c430464933" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    wget “https://my.privatoria.net/public/uploads/pr-openvpn.conf”</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5962a0611625c430464933-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5962a0611625c430464933-1"><span class="crayon-i">wget</span><span class="crayon-h"> </span>“<span class="crayon-v">https</span><span class="crayon-o">:</span><span class="crayon-c">//my.privatoria.net/public/uploads/pr-openvpn.conf”</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    <a href="https://www.deepdotweb.com/wp-content/uploads/2015/07/51.png"><img class="aligncenter size-full wp-image-11022" src="https://www.deepdotweb.com/wp-content/uploads/2015/07/51.png" alt="5" width="894" height="352" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/07/51.png 894w, https://www.deepdotweb.com/wp-content/uploads/2015/07/51-300x118.png 300w" sizes="(max-width: 894px) 100vw, 894px"/></a></p>
    <div id="crayon-5962a06116260624401657" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo cp openvpn.conf /etc/openvpn/</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5962a06116260624401657-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5962a06116260624401657-1"><span class="crayon-e">sudo </span><span class="crayon-e">cp </span><span class="crayon-v">openvpn</span><span class="crayon-sy">.</span><span class="crayon-v">conf</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">etc</span><span class="crayon-o">/</span><span class="crayon-v">openvpn</span><span class="crayon-o">/</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    <a href="https://www.deepdotweb.com/wp-content/uploads/2015/07/61.png"><img class="aligncenter size-full wp-image-11023" src="https://www.deepdotweb.com/wp-content/uploads/2015/07/61.png" alt="6" width="898" height="275" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/07/61.png 898w, https://www.deepdotweb.com/wp-content/uploads/2015/07/61-300x92.png 300w" sizes="(max-width: 898px) 100vw, 898px"/></a></p>
    <div id="crayon-5962a06116264026757979" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo nano /etc/openvpn/pr-openvpn.conf</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5962a06116264026757979-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5962a06116264026757979-1"><span class="crayon-e">sudo </span><span class="crayon-v">nano</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">etc</span><span class="crayon-o">/</span><span class="crayon-v">openvpn</span><span class="crayon-o">/</span><span class="crayon-v">pr</span><span class="crayon-o">-</span><span class="crayon-v">openvpn</span><span class="crayon-sy">.</span><span class="crayon-v">conf</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    <a href="https://www.deepdotweb.com/wp-content/uploads/2015/07/7.png"><img class="aligncenter size-full wp-image-11024" src="https://www.deepdotweb.com/wp-content/uploads/2015/07/7.png" alt="7" width="916" height="201" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/07/7.png 916w, https://www.deepdotweb.com/wp-content/uploads/2015/07/7-300x66.png 300w" sizes="(max-width: 916px) 100vw, 916px"/></a></p>
    <div id="crayon-5962a06116268751380352" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    replace “privatoria.net” with “gateway-tornet.privatoria.net” , hit Ctrl+O and Ctrl+X</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5962a06116268751380352-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5962a06116268751380352-1"><span class="crayon-i">replace</span><span class="crayon-h"> </span>“<span class="crayon-v">privatoria</span><span class="crayon-sy">.</span><span class="crayon-i">net</span>”<span class="crayon-h"> </span><span class="crayon-i">with</span><span class="crayon-h"> </span>“<span class="crayon-v">gateway</span><span class="crayon-o">-</span><span class="crayon-v">tornet</span><span class="crayon-sy">.</span><span class="crayon-v">privatoria</span><span class="crayon-sy">.</span><span class="crayon-i">net</span>”<span class="crayon-h"> </span><span class="crayon-sy">,</span><span class="crayon-h"> </span><span class="crayon-e">hit </span><span class="crayon-v">Ctrl</span><span class="crayon-o">+</span><span class="crayon-i">O</span><span class="crayon-h"> </span><span class="crayon-st">and</span><span class="crayon-h"> </span><span class="crayon-v">Ctrl</span><span class="crayon-o">+</span><span class="crayon-v">X</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    <a href="https://www.deepdotweb.com/wp-content/uploads/2015/07/8.png"><img class="aligncenter size-full wp-image-11025" src="https://www.deepdotweb.com/wp-content/uploads/2015/07/8.png" alt="8" width="916" height="326" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/07/8.png 916w, https://www.deepdotweb.com/wp-content/uploads/2015/07/8-300x107.png 300w" sizes="(max-width: 916px) 100vw, 916px"/></a></p>
    <div id="crayon-5962a0611626c269324493" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo service openvpn restart</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5962a0611626c269324493-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5962a0611626c269324493-1"><span class="crayon-e">sudo </span><span class="crayon-e">service </span><span class="crayon-e">openvpn </span><span class="crayon-v">restart</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    <a href="https://www.deepdotweb.com/wp-content/uploads/2015/07/9.png"><img class="aligncenter size-full wp-image-11026" src="https://www.deepdotweb.com/wp-content/uploads/2015/07/9.png" alt="9" width="900" height="250" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/07/9.png 900w, https://www.deepdotweb.com/wp-content/uploads/2015/07/9-300x83.png 300w" sizes="(max-width: 900px) 100vw, 900px"/></a></p>
    <p>Overall VPN+TOR is only getting it popularity. It is still a young technology, which means there is a room for improvement. This solution, however has more to offer that its components used alone. Therefore we do recommend that you give it a try a let us know about your experience.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/double/" rel="tag">double</a> <a href="https://www.deepdotweb.com/tag/encryption/" rel="tag">encryption</a> <a href="https://www.deepdotweb.com/tag/tor/" rel="tag">tor</a> <a href="https://www.deepdotweb.com/tag/vpn/" rel="tag">vpn</a></span> <span style="display:none" class="updated">2015-07-14</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/admin/" title="Posts by DeepDotWeb" rel="author">DeepDotWeb</a></strong></div>
    </div>
</article>

