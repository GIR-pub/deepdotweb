---
title: "VPN Service Providers With Port Forwarding Affected By IP Leak"
---

Posted by: Benjamin Vitáris 

<span>December 4, 2015</span>



<p>Perfect Privacy has discovered and <a href="https://www.perfect-privacy.com/blog/2015/11/26/ip-leak-vulnerability-affecting-vpn-providers-with-port-forwarding/">posted about</a> a potential attack vector on VPN service providers’ network that could be exploited by hackers or law enforcement agencies. “Port Fail”, if used by an attacker could result in the unmasking of the VPN user’s real IP address. The vulnerability point affects VPN service providers that offer the forwarding option and have no protection for this kind of specific attacks.</p>
<p>This IP leak is affecting all VPN users, however, the victim does not have to necessarily use port forwarding, only the attacker has to set it up.</p>
<p>According to the blog post, they have tested this vulnerability with nine different VPN providers, however, only 4 of them had the required protection for the attack. The other five has been notified by Perfect Privacy so they can fix the issue ASAP before someone is abusing it. They also state that other VPN service providers could be also vulnerable since they could not test all services.</p>
<p>Perfect Privacy made a list of the requirements and the specific IP leak. It goes by this quoting from their blog:</p>
<p>“The attacker needs to meet the following requirements:</p>
<p>&#8211;   Has an active account at the same VPN provider as the victim</p>
<p>&#8211;   Knows victim’s VPN exit IP address (can be obtained by various means, e.g. IRC or torrent client or by making the victim visit a website under the attacker&#8217;s control)</p>
<p>&#8211;   The attacker sets up port forwarding. It makes no difference whether the victim has port forwarding activated or not.”</p>
<p>“The IP leak can then be triggered as follows:</p>
<ol>
<li>Victim is connected to VPN server 1.2.3.4</li>
<li>Victim’s routing table will look something like this:</li>
</ol>
<p>0.0.0.0/0 -&gt; 10.0.0.1 (internal vpn gateway ip)</p>
<p>1.2.3.4/32 -&gt; 192.168.0.1 (old default gateway)</p>
<ol start="3">
<li>Attacker connects to same server 1.2.3.4 (knows victim’s exit through IRC or other means)</li>
<li>Attacker activates Port Forwarding on server 1.2.3.4, example port 12345</li>
<li>Attacker gets the victim to visit 1.2.3.4:12345 (for example via embedding &lt;img src=”http://1.2.3.4:12345/x.jpg”&gt; on a website)</li>
<li>This connection will reveal the victim’s real IP to the attacker because of the “1.2.3.4/32 -&gt; 192.168.0.1” vpn route.”</li>
</ol>
<p>The crucial problem is that a VPN user connecting to his own Virtual Private Network server will use his default route with his real IP address since this is a requirement for the VPN connection in order to work. If another user (the attacker) has port forwarding activated for his account on the same server he can find out the real IP addresses of all the users on the same VPN server by tricking each user into visiting a link that redirects the traffic to a port under the attacker’s control.</p>
<p>Since the nature of this attack all VPN protocols (IPSec, OpenVPN, PPTP, etc.) and all operating systems are affected.</p>
<p>Perfect Privacy also made this statement that could help VPN service providers:</p>
<p>”Affected VPN providers should implement one of the following:</p>
<ul>
<li>Have multiple IP addresses, allow incoming connections to ip1, exit connections through ip2-ipx, have portforwardings on ip2-ipx</li>
<li>On Client connect set server side firewall rule to block access from Client real ip to portforwardings that are not his own.”</li>
</ul>
<p>According to Perfect Privacy, all of their users are protected from such attacks.</p>

Updated: 2015-12-04

