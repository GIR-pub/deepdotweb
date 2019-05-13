---
What Can ISPs See?"
---
<article class="post-listing post-13525 post type-post status-publish format-standard has-post-thumbnail hentry  tag-isps">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/fuzzy/" title="">Fuzzy </a></span>
    <span>March 20, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/03/20/can-isps-see/#comments">5 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Last year, ISPs were <a href="https://apps.fcc.gov/edocs_public/attachmatch/FCC-15-24A1_Rcd.pdf">classified</a> as common carriers under Title II of the Communications Act by the FCC to enforce net neutrality. The FCC is now looking to implement regulation that ISPs will have to follow in order to protect their customers&#8217; information. In light of this, Team Upturn <a href="https://www.teamupturn.com/reports/2016/what-isps-can-see">published</a> a report to “provide technical grounding for policymakers and other interested parties, regarding the extent of ISP visibility into the activities of their subscribers.”</p>
    <p>The report opens with 4 observations:</p>
    <ul>
    <li>Many sites still don&#8217;t provide encryption, allowing ISPs to easily monitor their users.</li>
    <li>Even with HTTPS, ISPs can still see domains visited which can be <strong>very</strong> revealing over a long period of time. In fact, ISPs already look at this data.</li>
    <li>Sometimes HTTPS isn&#8217;t enough.</li>
    <li><a href="https://www.deepdotweb.com/vpn-comparison-chart/">VPNs</a> are hardly used and provide “incomplete protection”.</li>
    </ul>
    <p>Unencrypted HTTP allows ISPs to see the full URL and page contents of sites visited. If that wasn&#8217;t enough to convince you that unencrypted HTTP is bad, then consider the fact that unencrypted HTTP in general <a href="http://www.leviathansecurity.com/blog/the-case-of-the-modified-binaries">isn&#8217;t fun</a> at all. A brief survey done by Team Upturn revealed that 85% of the top 50 health, news, and shopping sites – as ranked by Alexa – didn&#8217;t fully support encryption by default. Team Upturn explained that it can very hard for sites to fully adopt encryption because a lot of them depend on third-party services that provide analytics, advertising, tracking, and embedded videos. Many of these third-parties don&#8217;t provide encryption. A 2015 survey of 2,156 online advertising services revealed that over 85% of them didn&#8217;t support HTTPS.</p>
    <p>The report also found that IoT (Internet Of Things) devices often use unencrypted HTTP to transfer data – as if IoT wasn&#8217;t <a href="http://www.theguardian.com/technology/2016/feb/09/internet-of-things-smart-home-devices-government-surveillance-james-clapper">already</a> bad enough.</p>
    <p>“Researchers at the Center for Information Technology Policy at Princeton recently found a range of popular devices — from the Nest thermostat to the Ubi voice system, to the PixStar photo frame — transmitting unencrypted data across the network &#8221;Investigating the traffic to and from these devices turned out to be much easier than expected,&#8221; observed Professor Nick Feamster.”</p>
    <p>Even if you used HTTPS, ISPs would still see the domains visited due to how HTTPS works and because DNS queries are rarely ever encrypted. Although ISPs would only see the domains, that data can still be very sensitive as Team Upturn points out:</p>
    <p>“Even a short series of visited domains from one subscriber can be sensitive. A pivotal moment in a user’s life, for example, could generate the following log at the user’s ISP (assuming the user hasn’t invested in special privacy tools):</p>
    [2015/03/09 18:34:44] abortionfacts.com<br />
    [2015/03/09 18:35:23] plannedparenthood.org<br />
    [2015/03/09 18:42:29] dcabortionfund.org<br />
    [2015/03/09 19:02:12] maps.google.com”</p>
    <p>ISPs already do monitor DNS queries and real time user traffic to identify and block malware using services from companies such as Damballa. It&#8217;s been <a href="http://www.cnet.com/news/comcast-takes-free-anti-botnet-service-nationwide/">reported</a> that Comcast deploys this functionality to customers. It&#8217;s also been reported that small ISPs use DNS servers that are <a href="http://arstechnica.com/tech-policy/2011/08/small-isps-turn-to-malicious-dns-servers-to-make-extra-cash/">malicious</a> just to make a quick buck.</p>
    <p>Sometimes HTTPS isn&#8217;t enough either. The report explains that “A growing body of computer science research demonstrates that a network operator can learn a surprising amount about the contents of encrypted traffic without breaking or weakening encryption. By examining the features of the traffic — like the size, timing and destination of the encrypted packets — it is possible to uniquely identify certain web page visits or otherwise reveal information about what those packets likely contain. In the technical literature, inferences reached in this way are called “side channel” information.”</p>
    <p>However, the report also states that side-channel attacks are very unlikely to be carried out by ISPs; but as encryption becomes more widespread, it may be more and more tempting to do.</p>
    <p>“Policymakers should have a clear understanding of what’s <em>possible</em> for ISPs to learn, both now and in the future.”</p>
    <p>One way that users can protect themselves is by using a <a href="https://www.deepdotweb.com/vpn-comparison-chart/">VPN</a> but they are rarely ever used. A 2014 survey reveals that only 14% of users in North America have used a <a href="https://www.deepdotweb.com/vpn-comparison-chart/">VPN</a>. Even if a user does start using a VPN, the privacy it provides is questionable as the report brings up:</p>
    <p>“VPNs are not a privacy silver bullet. The use of <a href="https://www.deepdotweb.com/vpn-comparison-chart/">VPNs</a> and encrypted proxies merely shifts user trust from one intermediary (the ISP) to another (the VPN or proxy operator). In order to more thoroughly protect their traffic from their ISP, a subscriber must entrust that same traffic to another network operator.”</p>
    <p>It&#8217;s also possible that a DNS leak could occur and thus allow a user&#8217;s ISP to see their DNS queries.</p>
    <p>Those out there who want to protect their privacy must consider whether or not their ISP is an adversary and act accordingly as Team Upturn concludes, “Today, ISPs can see a significant amount of their subscribers’ Internet activity, and have the ability to infer substantial amounts of sensitive information from it. &#8230;”</p>
    <p><em>Note: The sources for the surveys mentioned in this article can be found in Team Upturn&#8217;s <a href="https://www.teamupturn.com/reports/2016/what-isps-can-see">report</a>.</em></p>
    </div>
    <a href="https://www.deepdotweb.com/tag/isps/" rel="tag">isps</a></span> <span style="display:none" class="updated">2016-03-20</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/fuzzy/" title="Posts by Fuzzy" rel="author">Fuzzy</a></strong></div>
    
