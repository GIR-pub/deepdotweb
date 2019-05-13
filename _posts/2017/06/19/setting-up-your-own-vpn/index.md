---
A WORLD OF POSSIBILITIES
---
---
Setting Up Your Own VPN
---
<article class="post-listing post-20732 post type-post status-publish format-standard has-post-thumbnail hentry  tag-setting tag-vpn">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/theinnocent/" title="">TheInnocent </a></span>
    <span>June 19, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/06/19/setting-up-your-own-vpn/#comments">9 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    <p>A <a href="https://www.deepdotweb.com/vpn-comparison-chart/">VPN is a virtual private network</a>. It is virtual because one creates a virtual tunnel between your computer and a server to exchange data. It is private because it is supposed to require a username and a password to be accessed and it is a network because it links more devices to one or more servers all over different locations. A VPN helps you surf the web anonymously for two reasons:</p>
    <ul>
    <li>the websites you visit, see the VPN server’s ip, not yours.</li>
    <li>VPN basically encrypts all the traffic before ISP (internet service provider) can intercept it.</li>
    </ul>
    <p>There are free versions and paid ones. But still the VPN provider can read your traffic. So you have to trust someone one way or another. What if you could set up your own VPN instead ? It would be totally free and totally (really ?) secure…</p>
    <p><img class="wp-image-20746 aligncenter" src="/imgs/2017/06/word-image-33.png" /></p>
    <p>When you set your mind on the idea of creating your own virtual private network, a world of different possibilities comes to you. Reading on, you’ll encounter some technicalities but the detailed explanation of software’s installation is left to other articles you can find on the web. This article wants, in particular, to help you discerning what is the best choice for you. The following list is used as a guideline:</p>
    <ul>
    <li>VPN on a cloud
    <ul>
    <li>streisand</li>
    <li>algo</li>
    </ul>
    </li>
    <li>VPN on a NAS</li>
    <li>VPN on a router
    <ul>
    <li>supported routers</li>
    <li>flashing DD-WRT</li>
    <li>flashing OpenWrt</li>
    <li>flashing TomatoUSB</li>
    </ul>
    </li>
    <li>VPN on a personal computer</li>
    <li>VPN on a Raspberry Pi</li>
    </ul>
    <h2>VPN ON A CLOUD</h2>
    <p><img class="wp-image-20747 aligncenter" src="/imgs/2017/06/word-image-34.png" width="765" height="430" srcset="/imgs/2017/06/word-image-34.png 1074w, /imgs/2017/06/word-image-34-300x168.png 300w, /imgs/2017/06/word-image-34-1024x575.png 1024w" sizes="(max-width: 765px) 100vw, 765px" /></p>
    <p>Hosting a VPN on a cloud is becoming a very common practice. Installing softwares like Algo and Streisand on your laptop, give you the possibility of creating servers on cloud services like Amazon EC2, Azure, Digital Ocean, Google, Linode and Rackspace Cloud. The basic process is creating an account on one of the above cited cloud providers (there are free and paid versions), installing the particular software you need (it requires a little configuration but nothing very hard) and you’re done. In the following lines, I’ll explain in details the process of installing Streisand and Algo.</p>
    <p>STREISAND</p>
    <p>Streisand is a software that allows you to create an Ubuntu 16.04 server on a variety of cloud providers like Amazon, Google and many more. More than this, Streisand installs on your server a lot of <a href="https://www.deepdotweb.com/2016/12/30/turkish-government-permanently-bans-tor-vpn-services/">anti-censorship</a> tools like Stunnel, Tor, sslh, OpenVPN, OpenSSH, Monit, L2TP/IPsec, Shadowsocks, UFW. Installing Streisand is easy and requires only few commands in your terminal:</p>
    <div id="crayon-5bd681e880a9e546538207" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    ssh-keygen
    
    sudo apt-get install python-paramiko python-pip python-pycurl python-dev build-essential
    
    sudo pip install ansible markupsafe
    
    Sudo pip install boto</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5bd681e880a9e546538207-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5bd681e880a9e546538207-2">2</div><div class="crayon-num" data-line="crayon-5bd681e880a9e546538207-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5bd681e880a9e546538207-4">4</div><div class="crayon-num" data-line="crayon-5bd681e880a9e546538207-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-5bd681e880a9e546538207-6">6</div><div class="crayon-num" data-line="crayon-5bd681e880a9e546538207-7">7</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5bd681e880a9e546538207-1"><span class="crayon-v">ssh</span><span class="crayon-o">-</span><span class="crayon-e">keygen</span></div><div class="crayon-line crayon-striped-line" id="crayon-5bd681e880a9e546538207-2">&nbsp;</div><div class="crayon-line" id="crayon-5bd681e880a9e546538207-3"><span class="crayon-e">sudo </span><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-e">install </span><span class="crayon-v">python</span><span class="crayon-o">-</span><span class="crayon-e">paramiko </span><span class="crayon-v">python</span><span class="crayon-o">-</span><span class="crayon-e">pip </span><span class="crayon-v">python</span><span class="crayon-o">-</span><span class="crayon-e">pycurl </span><span class="crayon-v">python</span><span class="crayon-o">-</span><span class="crayon-e">dev </span><span class="crayon-v">build</span><span class="crayon-o">-</span><span class="crayon-e">essential</span></div><div class="crayon-line crayon-striped-line" id="crayon-5bd681e880a9e546538207-4">&nbsp;</div><div class="crayon-line" id="crayon-5bd681e880a9e546538207-5"><span class="crayon-e">sudo </span><span class="crayon-e">pip </span><span class="crayon-e">install </span><span class="crayon-e">ansible </span><span class="crayon-e">markupsafe</span></div><div class="crayon-line crayon-striped-line" id="crayon-5bd681e880a9e546538207-6">&nbsp;</div><div class="crayon-line" id="crayon-5bd681e880a9e546538207-7"><span class="crayon-e">Sudo </span><span class="crayon-e">pip </span><span class="crayon-e">install </span><span class="crayon-v">boto</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    (To install the python libraries for Amazon EC2 you’ll find the commands for every other provider on <a href="https://github.com/jlund/streisand">streisand’s page on github</a>.)</p>
    <div id="crayon-5bd681e880aaa367601180" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    git clone &amp;&amp; cd streisand
    
    ./streisand</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5bd681e880aaa367601180-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5bd681e880aaa367601180-2">2</div><div class="crayon-num" data-line="crayon-5bd681e880aaa367601180-3">3</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5bd681e880aaa367601180-1"><span class="crayon-e">git </span><span class="crayon-r">clone</span><span class="crayon-h"> </span><span class="crayon-o">&amp;&amp;</span><span class="crayon-h"> </span><span class="crayon-e">cd </span><span class="crayon-i">streisand</span></div><div class="crayon-line crayon-striped-line" id="crayon-5bd681e880aaa367601180-2">&nbsp;</div><div class="crayon-line" id="crayon-5bd681e880aaa367601180-3"><span class="crayon-sy">.</span><span class="crayon-o">/</span><span class="crayon-v">streisand</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    Next you can follow the terminal-wizard choosing the provider, the location of the server, the name of the server and so on. At the end of the procedure, an HTML file will be generated, with the instructions to connect to the server through SSL or Tor. Now you’re done with the installation and you can enjoy the navigation through your brand new VPN.</p>
    <p><strong>ALGO</strong></p>
    <p>From <a href="https://github.com/trailofbits/algo">github</a>:</p>
    <p><em>Algo VPN is a set of Ansible scripts that simplify the setup of a personal IPSEC VPN. It uses the most secure defaults available, works with common cloud providers, and does not require client software on most devices.</em></p>
    <p>To install algo on your personal computer, write the following commands in your terminal:</p>
    <div id="crayon-5bd681e880ab0865883556" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    sudo apt-get update &amp;&amp; sudo apt-get install \
    
    build-essential \
    
    libssl-dev \
    
    libffi-dev \
    
    python-dev \
    
    python-pip \
    
    python-setuptools \
    
    python-virtualenv -y</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5bd681e880ab0865883556-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5bd681e880ab0865883556-2">2</div><div class="crayon-num" data-line="crayon-5bd681e880ab0865883556-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5bd681e880ab0865883556-4">4</div><div class="crayon-num" data-line="crayon-5bd681e880ab0865883556-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-5bd681e880ab0865883556-6">6</div><div class="crayon-num" data-line="crayon-5bd681e880ab0865883556-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-5bd681e880ab0865883556-8">8</div><div class="crayon-num" data-line="crayon-5bd681e880ab0865883556-9">9</div><div class="crayon-num crayon-striped-num" data-line="crayon-5bd681e880ab0865883556-10">10</div><div class="crayon-num" data-line="crayon-5bd681e880ab0865883556-11">11</div><div class="crayon-num crayon-striped-num" data-line="crayon-5bd681e880ab0865883556-12">12</div><div class="crayon-num" data-line="crayon-5bd681e880ab0865883556-13">13</div><div class="crayon-num crayon-striped-num" data-line="crayon-5bd681e880ab0865883556-14">14</div><div class="crayon-num" data-line="crayon-5bd681e880ab0865883556-15">15</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5bd681e880ab0865883556-1"><span class="crayon-e">sudo </span><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-v">update</span><span class="crayon-h"> </span><span class="crayon-o">&amp;&amp;</span><span class="crayon-h"> </span><span class="crayon-e">sudo </span><span class="crayon-v">apt</span><span class="crayon-o">-</span><span class="crayon-e">get </span><span class="crayon-i">install</span><span class="crayon-h"> </span><span class="crayon-sy">\</span></div><div class="crayon-line crayon-striped-line" id="crayon-5bd681e880ab0865883556-2">&nbsp;</div><div class="crayon-line" id="crayon-5bd681e880ab0865883556-3"><span class="crayon-v">build</span><span class="crayon-o">-</span><span class="crayon-i">essential</span><span class="crayon-h"> </span><span class="crayon-sy">\</span></div><div class="crayon-line crayon-striped-line" id="crayon-5bd681e880ab0865883556-4">&nbsp;</div><div class="crayon-line" id="crayon-5bd681e880ab0865883556-5"><span class="crayon-v">libssl</span><span class="crayon-o">-</span><span class="crayon-i">dev</span><span class="crayon-h"> </span><span class="crayon-sy">\</span></div><div class="crayon-line crayon-striped-line" id="crayon-5bd681e880ab0865883556-6">&nbsp;</div><div class="crayon-line" id="crayon-5bd681e880ab0865883556-7"><span class="crayon-v">libffi</span><span class="crayon-o">-</span><span class="crayon-i">dev</span><span class="crayon-h"> </span><span class="crayon-sy">\</span></div><div class="crayon-line crayon-striped-line" id="crayon-5bd681e880ab0865883556-8">&nbsp;</div><div class="crayon-line" id="crayon-5bd681e880ab0865883556-9"><span class="crayon-v">python</span><span class="crayon-o">-</span><span class="crayon-i">dev</span><span class="crayon-h"> </span><span class="crayon-sy">\</span></div><div class="crayon-line crayon-striped-line" id="crayon-5bd681e880ab0865883556-10">&nbsp;</div><div class="crayon-line" id="crayon-5bd681e880ab0865883556-11"><span class="crayon-v">python</span><span class="crayon-o">-</span><span class="crayon-i">pip</span><span class="crayon-h"> </span><span class="crayon-sy">\</span></div><div class="crayon-line crayon-striped-line" id="crayon-5bd681e880ab0865883556-12">&nbsp;</div><div class="crayon-line" id="crayon-5bd681e880ab0865883556-13"><span class="crayon-v">python</span><span class="crayon-o">-</span><span class="crayon-i">setuptools</span><span class="crayon-h"> </span><span class="crayon-sy">\</span></div><div class="crayon-line crayon-striped-line" id="crayon-5bd681e880ab0865883556-14">&nbsp;</div><div class="crayon-line" id="crayon-5bd681e880ab0865883556-15"><span class="crayon-v">python</span><span class="crayon-o">-</span><span class="crayon-v">virtualenv</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-v">y</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    &nbsp;</p>
    <div id="crayon-5bd681e880ab3914694823" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    python -m virtualenv env &amp;&amp; source env/bin/activate &amp;&amp; python -m pip install -U pip
    
    python -m pip install -r requirements.txt</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5bd681e880ab3914694823-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5bd681e880ab3914694823-2">2</div><div class="crayon-num" data-line="crayon-5bd681e880ab3914694823-3">3</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5bd681e880ab3914694823-1"><span class="crayon-v">python</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-i">m</span><span class="crayon-h"> </span><span class="crayon-e">virtualenv </span><span class="crayon-v">env</span><span class="crayon-h"> </span><span class="crayon-o">&amp;&amp;</span><span class="crayon-h"> </span><span class="crayon-e">source </span><span class="crayon-v">env</span><span class="crayon-o">/</span><span class="crayon-v">bin</span><span class="crayon-o">/</span><span class="crayon-v">activate</span><span class="crayon-h"> </span><span class="crayon-o">&amp;&amp;</span><span class="crayon-h"> </span><span class="crayon-v">python</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-i">m</span><span class="crayon-h"> </span><span class="crayon-e">pip </span><span class="crayon-v">install</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-i">U</span><span class="crayon-h"> </span><span class="crayon-e">pip</span></div><div class="crayon-line crayon-striped-line" id="crayon-5bd681e880ab3914694823-2">&nbsp;</div><div class="crayon-line" id="crayon-5bd681e880ab3914694823-3"><span class="crayon-v">python</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-i">m</span><span class="crayon-h"> </span><span class="crayon-e">pip </span><span class="crayon-v">install</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-i">r</span><span class="crayon-h"> </span><span class="crayon-v">requirements</span><span class="crayon-sy">.</span><span class="crayon-v">txt</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    Open config.cfg in a text editor and choose the list of users in the <strong>users</strong> list.</p>
    <p>In the Algo directory run</p>
    <div id="crayon-5bd681e880ab7306781725" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    ./algo</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5bd681e880ab7306781725-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5bd681e880ab7306781725-1"><span class="crayon-sy">.</span><span class="crayon-o">/</span><span class="crayon-v">algo</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    As you can see, Algo does not support a Tor bridge which is the reason why I prefer Streisand for the moment.</p>
    <p>Now you can follow the wizard. At the end of the procedure you will see the subsequent message:</p>
    <p><img class="wp-image-20748 aligncenter" src="/imgs/2017/06/word-image-35.png" srcset="/imgs/2017/06/word-image-35.png 624w, /imgs/2017/06/word-image-35-300x90.png 300w" sizes="(max-width: 624px) 100vw, 624px" /></p>
    <h2>VPN ON A NAS</h2>
    <p>A NAS (Network Attached Storage) is basically a storage system that has all the key features of a small server. It often has a linux based operating system on it and it usually can be accessible by operating systems of all kind. A NAS can be linked to one or more hard disks. Connecting to the NAS gives many people all over the world the possibility to access the data stored in it. You can implement a VPN on your NAS, using it as a real server.</p>
    <h2>VPN ON A ROUTER</h2>
    <p>Many routers support the creation of a VPN, many others don’t. On the routers that are not supported, you can flash a new firmware that</p>
    <ul>
    <li>drastically improves your router’s performances</li>
    <li>gives you the possibility of creating a VPN on your router</li>
    </ul>
    <p>Here is the key question: why should you install a VPN on your router? The answer is that having the VPN installed on your router, gives you the possibility of connecting any devices you want having them fully covered with your VPN with a single account. Said this, there are many custom firmwares that you can flash into your router. The most famous are:</p>
    <ul>
    <li>DD-WRT</li>
    <li>OpenWrt</li>
    <li>TomatoUSB</li>
    </ul>
    <p>There are also many routers that come with this custom firmwares pre-installed. Some VPN vendors also sell routers of this genre.</p>
    <h2>VPN ON A PERSONAL COMPUTER</h2>
    <p>All the existent operating systems offer the possibility of installing a VPN server software. The con of this option is that your pc may not be always on, so the VPN wouldn’t be always accessible. Anyway it is much cheaper than buying a NAS.</p>
    <h2>VPN ON A RASPBERRY PI</h2>
    <p>At this point of my article you’ve certainly understood that you can install a VPN on every computer-like device&#8230;So why don’t you try with a Raspberry Pi ? You shouldn’t trust a public Wi-Fi when using your credentials on a bank site, instead it would recommendable using a virtual private network residing, for example, on your Raspberry Pi. Setting up a VPN on a Raspberry Pi is a little bit complex, I’ll try to explain the key concepts of the installation procedure in the most user-friendly manner, but for an in-depth tutorial I invite you to read the numerous specific articles you’ll find on the web. So the key concepts are:</p>
    <ul>
    <li>Raspberry Pi model B.</li>
    <li>NOOBS (new out of the box software), an easy OS installer.</li>
    <li>Raspbian, the official supported operating system for Raspberry Pi.</li>
    <li>Open VPN, the open source software which will give life to your VPN.</li>
    <li>Change your Raspberry Pi’s default username and password to something strong (this is fundamental to achieve the security you need for your VPN).</li>
    <li>Generate keys with Easy_RSA. You do this because you don’t want your VPN address to be accessible by anyone. In this way, only the authorized devices can access your VPN.</li>
    <li>Build the CA certificate. The CA (certificate authority), is the organization that checks if a website declares a false identity. When you visit your bank’s site and you sign in with your account, the site presents to you a certificate validated by the CA. Only in this way you can be sure you’re visiting exactly your bank’s site and not a phishing site. In this case you are the certificate authority of yourself.</li>
    <li>Static IP on the local network. We want our Raspberry Pi to have always the same IP, being always easily accessible. We achieve this, modifying the etc/network/interfaces file on Raspbian.</li>
    <li>Portforwarding on your router. We want the router’s firewall to allow a connection between the external network and the internal one, through the UDP port 1194.</li>
    <li>Generate keys for all the client devices. I recommend generating a different one for each device, or you’ll not be able to connect with every device at the same time.</li>
    </ul>
    <h2>CONCLUSIONS</h2>
    <p>Now that we briefly looked over all the possibilities you have when you’re creating your personal VPN, it’s time to punctuate some important considerations. Setting up a VPN with the methods explained, protects you from showing your activity to your ISP, gives you the possibility of accessing data stored on the server from all over the world and guarantees protection from censorship. For what concerns anonymity, I must warn you, setting up a VPN on a laptop, on a Raspberry Pi, on a NAS, on a router or on any other device located in your home WILL NOT GRANT YOU ANONYMITY. So you may think that the cloud solution is the best one, because it lets you connect to a virtual server pretending to be located in any location you want.</p>
    <p>To be sincere, even this option is not really reliable. In fact in order to use Algo or Streisand, you have to create an account with Amazon, Azure on any other provider; during the registration process you’ll be asked for a lot of personal informations and many security checks and identification processes will be applied. So even if the server is virtually untraceable, it is related to your personal account. It’s not that easy to create an anonymous Amazon account…but it’s still not impossible (if you know how to do it). Don’t think to use this kind of VPN to hack or do anything illicit. For this kind of purposes, just for the pleasure of discussing, the paid versions like HMA, <a href="https://www.deepdotweb.com/2015/12/26/nordvpn-review/">NordVPN</a> and so on, are often preferred. You’ll be thinking that there “still remains the problem of the provider spying on my activity”&#8230;and you’re right, but fortunately Tor <a href="https://www.deepdotweb.com/2016/04/19/tor-vpn-a-necessary-couple/">comes in help</a>. If you <strong>first </strong>connect to Tor and then to your VPN provider, the VPN server will only see the Tor ip, not yours.</p>
    <p>Concluding, always remember: if you do something stupid enough to anger people with enough resources, there’s no hope for you to remain anonymous. <em>Anonymity is a fact of not carrying out a stupid action, more than worrying about how to hide that action</em>.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/setting/" rel="tag">setting</a> <a href="https://www.deepdotweb.com/tag/vpn/" rel="tag">vpn</a></span> <span style="display:none" class="updated">2017-06-19</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/theinnocent/" title="Posts by TheInnocent" rel="author">TheInnocent</a></strong></div>
    </div>
</article>

