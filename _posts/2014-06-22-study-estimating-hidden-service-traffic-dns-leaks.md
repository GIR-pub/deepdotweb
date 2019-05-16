---
title: "Study: Estimating hidden service traffic from DNS leaks"
---

Posted by: DeepDotWeb

<span>June 22, 2014</span>

<p>A new and interesting study that was published recently under the name   <a href="http://www.verisigninc.com/assets/labs/Measuring-the-Leakage-of-Onion-at-the-Root.pdf">&#8220;Measuring the Leakage of Onion at the Root: A measurement of Tor’s .onion pseudo-top-level domain in the global domain name system&#8221;</a>, By Thomas &amp; Mohaisen 2014, Suggest the following things as they were summarized in a <a href="http://www.reddit.com/r/DarkNetMarkets/comments/28qy0u/estimating_hidden_service_traffic_from_dns_leaks/" target="_blank">reddit post</a> by <a href="http://www.gwern.net/" target="_blank">Gwern</a>:</p>
<blockquote><p>Tor is capable of providing anonymity to servers, which are configured to receive inbound connections only through Tor—more commonly called hidden services. In order to route requests to these hidden services, a is used to identify the resolution requests to such services. A namespace under a non-delegated (pseudo) top-level-domain (TLD) of .onion was elected. Although the Tor system was designed to prevent .onion requests from leaking into the global DNS resolution process, numerous requests are still observed in the global DNS. In this paper we will present the state of .onion requests received at the global public DNS A and J root nodes, potential explanations of the leakage, and highlights of trends associated with global censorship events.</p>
<p>&#8230;These unintended leaked DNS queries have been shown to expose sensitive private information and present potential new security threat vectors [5–7]. During the analysis of potential colliding name spaces within the global DNS, queries suffixed in .onion appeared to be one of the more prevalent non-delegated TLDs at the global root DNS.</p>
<p>&#8230;To this end, in this paper we present a first look at the .onion leakage at the DNS root. We use two root servers, A and J, that are operated by Verisign, and explore .onion resolutions seen at both of them over a period of time close to six months. Our findings highlight that a large amount of .onion traffic is observed at both servers and the requests originate from a diverse set of locations (at the recursive name server level). Furthermore, we illustrate .onion’s heavy tailed distribution (with respect to the number of queries per .onion), and a very interesting weekly traffic pattern&#8230;Verisign operates the A and J root servers in the DNS root zone. NXDomain (NXD) responses for the non-delegated TLD .onion were captured over slightly more than six months from both root servers starting on 10 September 2013 and ending 31 March 2014. The data set consists of approximately 27.6 million NXD records spanning 81,409 unique SLDs. The DNS requests originated from a wide variety of sources: in total, they are sent from 172,170 IP addresses, 105,772 unique /24 net blocks, and 21,345 distinct Autonomous System Numbers (ASNs). During the multi-month collection period, numerous NXD TLDs appeared at the roots. Based on the total query volume, we ranked the various TLDs and found that the .onion TLD ranked 461 out of 13.8 billion TLDs. The following section will further depict the traffic patterns and trends observed within the .onion TLD.</p>
<p>Table 1 provides a list of the most requested hidden services along with their total percentage of .onion traffic and the type of service provided using them. The mapping of SLDs to their type of service was constructed manually by searching for references of the hidden service online. The SLDs listed in the table have been anonymized (masked) for privacy concerns, where the first and last two characters of each SLD are shown.</p>
<p>Rank &#8211; Type &#8211; Traffic (%):<img class="aligncenter wp-image-6172 size-full" src="/imgs/2014/06/traffic.png" alt="traffic" width="454" height="234" srcset="/imgs/2014/06/traffic.png 454w, /imgs/2014/06/traffic-300x155.png 300w" sizes="(max-width: 454px) 100vw, 454px"/></p></blockquote>
<ul>
<li>2 Silk Road-1-forums 2.1%</li>
<li>4 Silk Road-1 1.4%</li>
<li>6 Tor Mail 1.2%</li>
<li>8 Agora 1.1%</li>
</ul>
<blockquote><p>&#8230;The geographical distribution of .onion requestors deviates from the Top-10 countries by directly connecting users as reported by the Tor project over the same period of time. At nearly 36%, the US is 3 times higher than reported from Tor. Other countries such as Germany, France, and Spain also di↵ered significantly, with 7.7%, 7.23% 6.17% and 4.8% respectively [12].</p></blockquote>
<img src="https://info-gir.github.io/deepdotweb/imgs/2014/06/geo.png" />

<p><a href="http://www.reddit.com/user/gwern" target="_blank">Gwern</a> also mentioned that:</p>
<blockquote><p>Given the time period, the table suggests that Agora may now be as popular as SR1 was before shutdown.</p></blockquote>
<p>This is interesting data about the traffic amount an sources related to the known marketplaces.</p>
<p>See also <a title="Biryukov et al 2013" href="http://www.ieee-security.org/TC/SP2013/papers/4977a080.pdf">&#8216;Trawling for Tor Hidden Services: Detection, Measurement, Deanonymization&#8217;</a> &amp; <a href="http://donncha.is/2013/05/trawling-tor-hidden-services/">&#8220;Trawling Tor Hidden Service &#8211; Mapping the DHT&#8221;</a>.</p>

Updated: 2014-06-22
    
