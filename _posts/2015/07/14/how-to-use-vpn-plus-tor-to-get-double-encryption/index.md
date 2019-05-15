---
title: "How To Use VPN Plus Tor To Get Double Encryption?"
---

Posted by: DeepDotWeb 

<span>July 14, 2015</span>
    

<p><em>Guest post by <a href="https://privatoria.net/">privatoria.net:</a></em></p>
<p>Tor is a great solution for people looking for on-line privacy and anonymity. Keeping all the positive sides of Tor in a mind one also has to take its vulnerabilities into account as well. Among those are incompatibility with P2P downloads and variable connection speed (it all depends on the exact Tor node you connect to every time). There is a solution to stay with Tor and forget about all of its weak points. In this article we showcase how to use popular Tor technology with good old VPN technology.</p>
<p style="text-align: center;"><a href="/vpn-comparison-chart/">&#8211;&gt; Click here to see the best VPN&#8217;s for privacy &lt;&#8211;</a></p>
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
<img src="imgs/2015/07/1-tails.png">
<p><strong>Use VPN+TOR in Tails OS</strong></p>
<p>Using VPN+TOR does not differ from using a stand alone VPN in any Linux-based system. We recommend utilizing OpenVPN protocol. Once OpenVPN daemon is installed, launch it to activate VPN connection. After that you can run Iceweasel and use Tor as if you were using just that. One major downside to this method is that both Tor and VPN go through the same channel, which might decrease your connection speed. You also do not isolate your VPN connection from Tor, which provides lower security level and gives additional loophole that can be used by an attacker.</p>
<p><a href="https://www.whonix.org/"><strong>Whonix</strong></a></p>
<p>This OS runs inside a virtual environment to prevent any DNS leaks. In fact, two separate virtual machines are needed to get this thing to work:</p>
<ul>
<li>Tor gateway Virtual Machine</li>
<li>Workstation virtual machine</li>
</ul>
<p>Tor gateway VM uses host OS&#8217;s network hardware and connect directly to Internet via NAT. Once connection is established it starts to force all traffic through Tor nodes and that&#8217;s what this is really all about. The Workstation VM is connected to Tor gateway VM and that&#8217;s the only way it gets Internet connectivity. So now we can route all our Internet traffic through Tor without Tor browser. The only downside to this is that you need to get a relatively powerful computer to actually make this work as you will be running 3 OS&#8217;s (1 host and 2 VM&#8217;s) at the same time.</p>
<img src="imgs/2015/07/2-whonix.jpg">
<p><strong>VPN+TOR in Whonix</strong></p>
<p>Unfortunately, we were not able to set up a reliable VPN+TOR connection on Whonix OS. The reason for that is Tor gateway VM that routes 100% of system traffic through Tor nodes. OS architecture does not provide the functionality to utilize both Tor and VPN at the same time. Activating VPN on a Workstation VM will most likely kill Internet connection. Whonix is still a great solution for Tor enthusiasts.</p>
<p><strong>Ready to go VPN+TOR solution</strong></p>
<p>There is a way to get a VPN to work with TOR without specific browsers, VM&#8217;s and OS&#8217;s. Great example is <a href="https://privatoria.net/vpn-tor/">Privatoria&#8217;s VPN plus TOR</a>. The way it works is simple that makes it a must-try.</p>
<p>The request is sent from the user machine to the VPN server via secure encrypted channel. The VPN server routes that traffic through Tor net using random Tor nodes to provide optimal security.</p>
<img src="imgs/2015/07/3-vpn.jpg">
<p>This scheme has a lot to offer, most notably:</p>
<ul>
<li>It will let you use VPN+TOR the right way with each of them having their own channels to get better security and speed</li>
<li>It will spare you from the installation pains</li>
<li>It works with any OS&#8217;s and browsers</li>
<li>It will ensure seamless experience without breaks due to dynamically changing nodes with checking their quality in real time</li>
</ul>
<p>Here&#8217;s how you can configure VPN+TOR on any Debian/Ubuntu based Linux distro:</p>
<p>Open your terminal emulator and type in</p>
sudo apt-get install openvpn</textarea></div>

<p>
<a href="/imgs/2015/07/42.png">
wget “https://my.privatoria.net/public/uploads/pr-openvpn.conf”</textarea></div>

<p>
<a href="/imgs/2015/07/51.png">
sudo cp openvpn.conf /etc/openvpn/</textarea></div>

<p>
<a href="/imgs/2015/07/61.png">
sudo nano /etc/openvpn/pr-openvpn.conf</textarea></div>

<p>
<a href="/imgs/2015/07/7.png">
replace “privatoria.net” with “gateway-tornet.privatoria.net” , hit Ctrl+O and Ctrl+X</textarea></div>

<p>
<a href="/imgs/2015/07/8.png">
sudo service openvpn restart</textarea></div>

<p>
<a href="/imgs/2015/07/9.png">
<p>Overall VPN+TOR is only getting it popularity. It is still a young technology, which means there is a room for improvement. This solution, however has more to offer that its components used alone. Therefore we do recommend that you give it a try a let us know about your experience.</p>

Updated: 2015-07-14

