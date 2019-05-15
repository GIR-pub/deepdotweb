---
title: "VPN: Encrypt every device on your network for $20"
---

Posted by: c3lt1c 

<span>August 28, 2015</span>




<p>Staying in-line with the VPN theme I decided to build a site-to-site VPN solution &#8211; otherwise known as a &#8216;branch office tunnel&#8217;. First, you will need to make sure that your VPN provider supports this function. I personally use NordVPN, however many of the best popular providers support this option in the form of OpenVPN running on a flashed consumer router. Nord supports DDWRT and Tomato router. If you are not familiar with these custom firmwares I would advise that you do some reading and become comfortable with what they are and what they do. In a nutshell, both DDWRT and Tomato router are custom firmwares for many consumer grade routers, which leverage many additional features not available in the stock Linksys, D-Link, etc. firmware. Features include wireless function like bridges, repeaters, access points, etc. From a LAN/WAN perspective they support VPN, advanced routing, VLAN support, firewalling, etc.</p>
<p style="text-align: center;"><a href="/vpn-comparison-chart/">–&gt; Click here to see the best VPN’s for privacy &lt;–</a></p>
<p>Why would you want this you ask? In most scenarios you will be using clients to authenticate to your VPN provider. This is fine unless you&#8217;re using a device which is not supported or if your devices exceed your VPN license. More and more VPN providers are releasing clients for Android, IOS, Linux and just about any other OS around. Some are still a work in progress and on top of that you&#8217;re usually limited to a certain number of simultaneously connect devices. For example, I am limited to 2 devices &#8211; This is not a problem for me personally as I will rarely, if ever, use more than 2 devices on VPN simultaneously. <strong>Figure 1A</strong> illustrates a negotiation then tunnel establishment via software client to your VPN provider. <strong>Figure 1B</strong> will help you to visualize the difference in a site-to-site setup:</p>
<p><strong>FIGURE 1A:</strong></p>
<p><a href="/imgs/2015/04/12.jpg"><img class="aligncenter size-full wp-image-10150" src="/imgs/2015/04/12.jpg" alt="1" width="1042" height="293" srcset="/imgs/2015/04/12.jpg 1042w, /imgs/2015/04/12-300x84.jpg 300w, /imgs/2015/04/12-1024x288.jpg 1024w" sizes="(max-width: 1042px) 100vw, 1042px"/></a></p>
<p><strong>FIGURE 1B:</strong></p>
<p><a href="/imgs/2015/04/21.jpg"><img class="aligncenter size-full wp-image-10151" src="/imgs/2015/04/21.jpg" alt="2" width="1042" height="293" srcset="/imgs/2015/04/21.jpg 1042w, /imgs/2015/04/21-300x84.jpg 300w, /imgs/2015/04/21-1024x288.jpg 1024w" sizes="(max-width: 1042px) 100vw, 1042px"/></a></p>
<p>With a client you generally only launch your software and authenticate when you need privacy or perhaps you always &#8216;dial in&#8217; to VPN anytime you are using the internet. A site-to-site configuration, sometimes known as a BOT (Branch Office Tunnel), is always on. You set it up once then following the phase negotiations you have a constant VPN tunnel. Depending on which mode you use, you can set your VPN router to automatically renegotiate if it drops. For added security, devices which support TOR (The Onion Router) can provide any additional layer of security and anonymity as demonstrated in <strong>FIGURE 1C:</strong><a href="/imgs/2015/04/31.jpg"><img class="aligncenter size-full wp-image-10152" src="/imgs/2015/04/31.jpg" alt="3" width="906" height="557" srcset="/imgs/2015/04/31.jpg 906w, /imgs/2015/04/31-300x184.jpg 300w" sizes="(max-width: 906px) 100vw, 906px"/></a>Although you won&#8217;t benefit from TOR anonymity on things like tablets and smartphones, it&#8217;s important to be mindful of any identifiable devices running on your identifiable internet while using TOR. For example some may feel that VPNs are redundant as long as they are using TOR. So you log on to Agora, Blackbank (or your favorite DNM) to pick up some Bang Bros passwords (or whatever). While you&#8217;re waiting for coins to transfer, you decide to fire up Firefox and check your Gmail or it just so happens that you use Chrome which is always logged in to your Google account. This is a risk. You are simultaneously creating internet sessions in the clear as well as doing naughty things on TOR. This kind of behavior could create patterns which LE may seek to use against you if you become entangled in some legal issues.</p>
<p>There are a few ways to mitigate this risk: you could close out all other programs and network sessions while browsing the DarkNet. This seems like the safest solution, however in this day and age almost all major apps run live software updating and keep in mind when using Windows 8 that Onedrive is always on. You could run TOR exclusively in a virtual machine or using Tails. This is probably a better choice as it will do a little more to segregate your heroin addicted porn watching evil criminal identity from the chartered accountant with two kids and camper trailer. Even still, don&#8217;t forget that things like iPhones and Android phones are always on, connected and chattering with the internet. The absolute safest way to cruise around the DarkNet would be using Tails on a public free Wi-Fi network somewhere, such as your least favorite restaurant or coffee shop &#8211; somewhere you don&#8217;t frequent. Find a cheap dive with free Wi-Fi so you can be sure they don&#8217;t have the money to spring for cameras all over the premises. If you&#8217;re anything like me you&#8217;ll get complacent and start surfing the DarkNet from home again before long.</p>
<p><strong>TASK 1: Purchase a DDWRT or Tomato compatible consumer router</strong></p>
<p>This is where the $20 comes in. If you&#8217;re happy with some slightly older technology then the most common choice is a Linksys WRT54G. I have one of these with wireless G and 100 Mbps ports which I picked up for $20 on Craigslist a few years back. It certainly does the trick, but being a technology whore I decided to upgrade my DDWRT hardware this week and picked up a Linksys WRT310N. This model supports N wireless and boasts 1 Gbps switch ports. For this tutorial we are going to stick with a Linksys WRT310N running DDWRT. The 310 has two versions: 1 &amp; 2. I have a version 1 which means that I am limited to running the DDWRT mini or standard packages. You may find that you prefer Tomato, but DDWRT supports a massive list of devices, which can be found here:</p>
<p><a href="https://www.dd-wrt.com/wiki/index.php/Supported_Devices">https://www.dd-wrt.com/wiki/index.php/Supported_Devices</a></p>
<p>The process is really quite simple, however it is important to ensure that you have downloaded the correct image and VERY important that you do not interrupt the installation process &#8211; if you do, you can end up with a brick. With that said, it&#8217;s quite easy:</p>
<p><strong>TASK 2: Replace stock firmware with DDWRT </strong></p>
<p><strong>**NEITHER MYSELF NOR DEEPDOTWEB.COM ARE IN ANY WAY RESPONSIBLE FOR ANY DAMAGE ACCRUED WHILE ATTEMPTING TO FLASH A ROUTER WITH DDWRT SOFTWARE**</strong></p>
<p>First let me say that this article is meant as a basic overview of a site-to-site VPN infrastructure so as a courtesy I have included an extremely high level guide to router flashing. The detailed instructions can be found on numerous DDWRT-related sites such as ddwrt.com. I would recommend following said instructions if you are inexperienced or unsure of what you are doing. First, you&#8217;ll need to connect an Ethernet cable from your PC to one of the LAN ports on the router &#8211; make sure you don&#8217;t plug in to the WAN port or you won&#8217;t get far. You should be able to pick up an IP using the onboard DHCP scope. They usual mgmt IP of the device is 192.168.0.1 or 192.168.1.1. If you are unsure then open up cmd.exe and perform the <em>ipconfig </em>command to reveal your current IP and your router&#8217;s IP (default gateway). If the device has some mysterious username and password, or it&#8217;s not handing out DHCP leases then you may want to restore its factory defaults. The default credentials are often username: admin password: admin or username: admin password: password (or something similar). If you are uncertain it may be printed on the bottom of the router or else you can easily find this with Google. Now for the firmware flash:</p>
<ol>
<li>Setup &#8211;&gt; Administration &#8211;&gt; Firmware Upgrade</li>
</ol>
<p>2. Browse to the file previously downloaded image and click upgrade</p>
<p><strong>FIGURE 2A:</strong></p>
<p><a href="/imgs/2015/04/42.jpg"><img class="aligncenter size-full wp-image-10153" src="/imgs/2015/04/42.jpg" alt="4" width="609" height="393" srcset="/imgs/2015/04/42.jpg 609w, /imgs/2015/04/42-300x194.jpg 300w" sizes="(max-width: 609px) 100vw, 609px"/></a></p>
<p>If the upgrade fails quickly then you have either downloaded the wrong image or the file may be corrupt. Even though the DDWRT site said that my model supports the mini, standard and VPN images only the mini was successful &#8211; both others failed. Now again it is very important that you don&#8217;t interrupt the upgrade or you will end up with a brick. Once the upgrade is complete you should perform a hard reboot of the router before continuing on.</p>
<p>From here on in I won&#8217;t get into the various options available in DDWRT, but you will know that you have been successful when presented with a GUI similar to <strong>Figure 2B:</strong></p>
<p><a href="/imgs/2015/04/51.jpg"><img class="aligncenter wp-image-10154" src="/imgs/2015/04/51.jpg" alt="5" width="1160" height="639" srcset="/imgs/2015/04/51.jpg 1430w, /imgs/2015/04/51-300x165.jpg 300w, /imgs/2015/04/51-1024x564.jpg 1024w" sizes="(max-width: 1160px) 100vw, 1160px"/></a></p>
<p><strong>TASK 3: Bring your DDWRT router online</strong></p>
<p>If your home internet already uses a router that you&#8217;ve provided then you should be able to port over your basic settings to the newly flashed device (wireless SSID, security, etc.). But if you are like many of us you have an ISP-provided modem/router combo or some similar variation. Depending on your service and the way it is set up, this could be simple. For many, you will need to just replace the ISP router with the new DDWRT router, however you will need to know how to port over any settings for wireless etc. My ISP provides fiber to the home, which enters my house on a single mode fiber run which terminates with an SC connector into an ONT. The ONT (Optical Network Terminal) serves as a transceiver (among other things) which converts the fiber to copper (Ethernet). Setting up a site-to-site VPN tunnel on this sort of network can become pretty advanced because the ISP is offering television and data services through the same fiber. This necessitates the need for VLANs right to my home router so that traffic can be segregated and prioritized. If your internet is similar then you may have additional learning and troubleshooting ahead of you. For many DSL and cable internet services it will be as simple as replacing the router. You will need to ensure that there are no special requirements for the WAN port on your router. For example, my ISP uses MAC address filtering (or MAC address sticky) on the WAN port of the router. This means that when I plug in my own device, their DHCP server doesn&#8217;t recognize the MAC address and will not provide a public IP. Luckily you can set the MAC address of the ISP provided device on the port &#8211; this is also true of DDWRT:</p>
<ol>
<li>Setup &#8211;&gt; MAC Address Clone &#8211;&gt; Enable</li>
<li>Obtain the WAN interface MAC address from the ISP router and add to the above location</li>
<li>Save</li>
</ol>
<p><strong>FIGURE 2C:</strong></p>
<p><a href="/imgs/2015/04/6.jpg"><img class="aligncenter size-full wp-image-10155" src="/imgs/2015/04/6.jpg" alt="6" width="1261" height="459" srcset="/imgs/2015/04/6.jpg 1261w, /imgs/2015/04/6-300x109.jpg 300w, /imgs/2015/04/6-1024x373.jpg 1024w" sizes="(max-width: 1261px) 100vw, 1261px"/></a></p>
<p>The primary goal is to ensure that the WAN interface on your DDWRT router picks up a DHCP lease from your ISP. If you are one of the lucky few and have a static public IP (not normally available these days without paying a premium), then you will need to find out this IP and manually configure it:</p>
<p><strong>FIGURE 2D:</strong></p>
<p><a href="/imgs/2015/04/7.jpg"><img class="aligncenter size-full wp-image-10156" src="/imgs/2015/04/7.jpg" alt="7" width="1189" height="441" srcset="/imgs/2015/04/7.jpg 1189w, /imgs/2015/04/7-300x111.jpg 300w, /imgs/2015/04/7-1024x380.jpg 1024w" sizes="(max-width: 1189px) 100vw, 1189px"/></a></p>
<p><strong>TASK 4: Configure your DDWRT router for VPN</strong></p>
<p>Once you have a working WAN connection then the rest of your internal LAN setup is easy. If you have trouble with this please consult any of the numerous tutorials on ddwrt.com. So at this point it seems as though you are back to where you started&#8230;not even&#8230;now I have you reconfiguring your LAN and WLAN (Wireless LAN) settings. Because VPN providers like NordVPN are so wonderful, they have actually written up all of the VPN commands on their website. You can simply copy the config, replace the variables and then you should be able to negotiate a VPN connection to their server. The configuration instructions are available for customers at: <a href="https://nordvpn.com/tutorials/">https://nordvpn.com/tutorials/</a></p>
<p>The above link will provide step-by-step instructions to configure the commands on DDWRT to negotiate and maintain a VPN tunnel which will then encrypt ALL and ANY network traffic leaving your network. You will see in <strong>Figures 3A</strong> and <strong>3B</strong> that not much changes when you initially replace your ISP or home router with a DDWRT device. <strong>Figure 3C</strong> again demonstrates the virtual tunnel which will carry your traffic to our VPN provider&#8217;s network and egress all sessions from their devices and public IPs:</p>
<p><strong>FIGURE 3A:</strong></p>
<p><a href="/imgs/2015/04/8.jpg"><img class="aligncenter size-full wp-image-10157" src="/imgs/2015/04/8.jpg" alt="8" width="607" height="608" srcset="/imgs/2015/04/8.jpg 607w, /imgs/2015/04/8-150x150.jpg 150w, /imgs/2015/04/8-300x300.jpg 300w, /imgs/2015/04/8-55x55.jpg 55w, /imgs/2015/04/8-50x50.jpg 50w" sizes="(max-width: 607px) 100vw, 607px"/></a></p>
<p><strong>FIGURE 3B:</strong></p>
<p><a href="/imgs/2015/04/9.jpg"><img class="aligncenter size-full wp-image-10158" src="/imgs/2015/04/9.jpg" alt="9" width="607" height="608" srcset="/imgs/2015/04/9.jpg 607w, /imgs/2015/04/9-150x150.jpg 150w, /imgs/2015/04/9-300x300.jpg 300w, /imgs/2015/04/9-55x55.jpg 55w, /imgs/2015/04/9-50x50.jpg 50w" sizes="(max-width: 607px) 100vw, 607px"/></a></p>
<p><strong>FIGURE 3C:</strong></p>
<p><a href="/imgs/2015/04/10.jpg"><img class="aligncenter size-full wp-image-10159" src="/imgs/2015/04/10.jpg" alt="10" width="785" height="617" srcset="/imgs/2015/04/10.jpg 785w, /imgs/2015/04/10-300x236.jpg 300w" sizes="(max-width: 785px) 100vw, 785px"/></a></p>
<p>Don’t be deceived by the suggestion in <strong>Figure 3C</strong>; your traffic is still leaving up through your ISP Public IP, however it may as well not be. The above figure illustrates a logical topology of your network’s traffic (rather than a physical topology). Again, there are various flavours and methods by which to achieve the same goals and this is only one of many. Additional detailed guides on DDWRT VPN can be found at:</p>
<p><a href="http://www.dd-wrt.com/wiki/index.php/OpenVPN_Remote_Access_by_Static_Key_%28The_Simple_Way%29">http://www.dd-wrt.com/wiki/index.php/OpenVPN_Remote_Access_by_Static_Key_%28The_Simple_Way%29</a></p>
<p>OR</p>
<p><a href="http://www.dd-wrt.com/wiki/index.php/VPN_%28the_easy_way%29_v24%2B">http://www.dd-wrt.com/wiki/index.php/VPN_%28the_easy_way%29_v24%2B</a></p>
<p>Take note that additional DDWRT functionality (such as VPN) can be limited or even restricted by system resources such as RAM and product version. If you have the know-how and resources you might look to a solution normally suited for enterprise solution. An old Cisco ASA or Pix firewall could be obtained cheaply if you look hard enough. Some additional options include Nortel Contivity Extranet routers such as the CES 1100. This one might be a bit easier to learn as it’s mainly GUI-driven. For those looking for a challenge, you might look for a user Juniper SRX Firewall/Security Gateway. Although a GUI is available, the power is contained in the command line driven JunOS, which sits on top of BSD. All of the above devices would make fantastic ‘Branch Office Tunnel’ endpoints; and although they will likely provide additional customization and functionality, they also require a bit more technical skill to operate.</p>
<p>The DDWRT is a fine solution for most home network aficionados and from my experience it can be easily set up as a VPN router with likes of NordVPN – I have included the NordVPN configuration template for OpenVPN via DDWRT in <strong>Appendix A</strong>. No matter what your skill level is, it’s clear that these kinds of solutions are becoming more necessary in this day and age. With Big Brother poking its nose further into our private affairs you cannot lose by arming yourself with this type of protection. Remember: knowledge is power, but so is a badge and a gun.</p>
<p><strong>Appendix A</strong></p>
<ol>
<li>Go to Administration à Commands</li>
<li>Paste this whole text to the Command Box</li>
</ol>
<p>Replace the words in <span style="color: #ff0000;">red</span> with your valid credentials:</p>

    #!/bin/sh
    nvram set openvpncl_lzo=”yes”
    killall openvpn
    touch /tmp/openvpn-auth.conf
    echo YourNordVPNusername &gt; /tmp/openvpn-auth.conf
    echo YourNordVPNpassword &gt;&gt; /tmp/openvpn-auth.conf
    touch /tmp/openvpn.ovpn
    cat &gt; /tmp/openvpn.ovpn &lt;&lt;EOF
    client
    dev tun1
    proto udp
    remote vpn-nl.nordvpn.com 1194
    remote 95.211.224.1 1194
    resolv-retry infinite
    remote-random
    nobind
    tun-mtu 1500
    tun-mtu-extra 32
    mssfix 1450
    persist-key
    persist-tun
    ping 15
    ping-restart 0
    ping-timer-rem
    remote-cert-tls server
    #mute 10000
    auth-user-pass /tmp/openvpn-auth.conf
    comp-lzo
    verb 3
    pull
    fast-io
    cipher AES-256-CBC
    &lt;ca&gt;
    —–BEGIN CERTIFICATE—–
    MIID7DCCA1WgAwIBAgIJAJBW0AnvvfI9MA0GCSqGSIb3DQEBBQUAMIGrMQswCQYD
    VQQGEwJOTDELMAkGA1UECBMCTkwxFTATBgNVBAcTDFNhbkZyYW5jaXNjbzEQMA4G
    A1UEChMHTm9yZFZQTjELMAkGA1UECxMCTkwxGzAZBgNVBAMTEnZwbi1ubC5ub3Jk
    dnBuLmNvbTEbMBkGA1UEKRMSdnBuLW5sLm5vcmR2cG4uY29tMR8wHQYJKoZIhvcN
    AQkBFhBtYWlsQGhvc3QuZG9tYWluMB4XDTE0MDQyMjEwMjY0OVoXDTI0MDQxOTEw
    MjY0OVowgasxCzAJBgNVBAYTAk5MMQswCQYDVQQIEwJOTDEVMBMGA1UEBxMMU2Fu
    RnJhbmNpc2NvMRAwDgYDVQQKEwdOb3JkVlBOMQswCQYDVQQLEwJOTDEbMBkGA1UE
    AxMSdnBuLW5sLm5vcmR2cG4uY29tMRswGQYDVQQpExJ2cG4tbmwubm9yZHZwbi5j
    b20xHzAdBgkqhkiG9w0BCQEWEG1haWxAaG9zdC5kb21haW4wgZ8wDQYJKoZIhvcN
    AQEBBQADgY0AMIGJAoGBANWLMY7HjzfL0zgWCmCCQRNxoqbhi1Kxd5/U/uJgPmME
    nKTp89kQ3janQJTsIK/M8r96C+YgTua9ElRTIri6GmAD8lAfMV5CujI5N9iEs8AU
    Bl3x8T22nzmTI+IYF+qBPp6g+ks+5/LiYNVBbIebNnnwvWZDBNenTRCITE/8ymsH
    AgMBAAGjggEUMIIBEDAdBgNVHQ4EFgQU7tE7MjUdkRr+n2h3faMRty3zs/8wgeAG
    A1UdIwSB2DCB1YAU7tE7MjUdkRr+n2h3faMRty3zs/+hgbGkga4wgasxCzAJBgNV
    BAYTAk5MMQswCQYDVQQIEwJOTDEVMBMGA1UEBxMMU2FuRnJhbmNpc2NvMRAwDgYD
    VQQKEwdOb3JkVlBOMQswCQYDVQQLEwJOTDEbMBkGA1UEAxMSdnBuLW5sLm5vcmR2
    cG4uY29tMRswGQYDVQQpExJ2cG4tbmwubm9yZHZwbi5jb20xHzAdBgkqhkiG9w0B
    CQEWEG1haWxAaG9zdC5kb21haW6CCQCQVtAJ773yPTAMBgNVHRMEBTADAQH/MA0G
    CSqGSIb3DQEBBQUAA4GBAIOc3yXYw7O7D+lPXrOW2CYcsGKnXS5+9Kvn+rOTOCMH
    4+GlSW38gwiUCYi7C2kH52VhMOLMmYosVQZMRgNRAB0immKUi1JaVq5UDkOgo+rK
    keifSsGBJH4dnKUrG5lOQ7tGA88oT4Qlal6U1tFe2tR7keSXWVZYwtPz6jIrzK3q
    —–END CERTIFICATE—–
    &lt;/ca&gt;
    key-direction 1
    &lt;tls-auth&gt;
    —–BEGIN OpenVPN Static key V1—–
    6ee32f05bd25efbd64cf08a469c6aa36
    755dab4ea4cfa434c708faa51426848e
    afaab0e7d275af6924aaa8fd48d5098d
    7cd50b5a79d80fb85a0bcb0a9b2ec4d9
    f021e8d8584902736f8090a98e2eea88
    edbd26dc88361bac87d2151ade2f67be
    0ffd5fcf26a1d72ac7374079b46a79e8
    df52be0a49d590d80ad9bcc67ea5a01d
    0e2629b3de628c3e29229d8cda7c1fa1
    45111ecd7b123fda2d831216eab6c01b
    2d00a0a0c48109f2d0903bd93e8a0088
    c861d0b1d34513f01e075b655441662f
    d36b27a51841dffd7abc8535550330f6
    17266a0d891f55a6be533de8ec6483bc
    c36a67ed57e215861ab408cbc218bb24
    a6cbc028cfbf56a6b11ff64ed7073be0
    —–END OpenVPN Static key V1—–
    &lt;/tls-auth&gt;
    EOF
    openvpn –config /tmp/openvpn.ovpn –route-up /tmp/openvpncl/route-up.sh –down-pre /tmp/openvpncl/route-down.sh –daemon</textarea></div>

    
<p>


Updated: 2015-08-28

