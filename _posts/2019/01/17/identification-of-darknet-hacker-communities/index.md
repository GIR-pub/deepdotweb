---
Identification of darknet hacker communities (forums, IRCs, carding shops, and darknet marketplaces)
---
<article class="post-listing post-28117 post type-post status-publish format-standard has-post-thumbnail hentry  tag-approaches tag-current tag-cyber tag-dark tag-intelligence tag-overseeing tag-research tag-threat tag-web">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>January 17, 2019</span>
    
    <span><a href="https://www.deepdotweb.com/2019/01/17/identification-of-darknet-hacker-communities/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Cyber attacks lead to global losses that exceed $450 billion each year. To address this problem, ethical hackers and researchers put great efforts into Cyber Threat Intelligence (CTI) development in order to identify hackers and emerging threats. CTI analysts have highlighted the significance of studying the ever-growing online hacker communities. Despite their valuable CTI importance, collection of data from online hacker communities represents a non-trivial task.</p>
    <p><a href="https://ieeexplore.ieee.org/abstract/document/8587327">A recently published paper</a> summarizes the efforts of a group of researchers in systemic identification and analysis of hacker forums, Internet Relay Chats (IRCs), carding shops, and darknet marketplaces. The paper presents 102 hacker platforms with a total of 43,902,913 records.</p>
    <p>Throughout this article, we will overview the hacker communities presented via this paper.</p>
    <p><strong>1- Hacker forums:</strong></p>
    <p>Hacker forums represent the most common and largest online platforms for hackers to share various hacking resources. Hackers use these platforms to post messages via forum threads related to hacking tools, techniques, and malicious source code. Among all hacker platforms, forums are the only ones enabling hackers to post malicious exploit code for others to download freely. Figure (1) shows an example of <a href="https://www.deepdotweb.com/2018/11/14/research-how-ransomware-and-hacking-services-are-sold-on-darknet-marketplaces/">a hacker sharing ransomware code</a> on a forum. Sharing hacking tools enables users with limited hacking skills to be able to conduct cyberattacks. This feature, combined with the rich metadata (e.g. post content, post date) renders forums a pivotal data source for tracking the TTP of hackers, pinpointing key actors, and identifying emerging threats.</p>
    <p><img class="wp-image-28125" src="/imgs/2019/01/word-image-20.png" srcset="/imgs/2019/01/word-image-20.png 788w, /imgs/2019/01/word-image-20-300x187.png 300w" sizes="(max-width: 788px) 100vw, 788px" /></p>
    <p><strong>Figure (1) An example of a hacker sharing ransomware code on a hackers&#8217; forum</strong></p>
    <p>The research identified 51 hacking forums including 32,266,852 posts in 2,961,363 threads. 25,939,871 were in English, 5,975,821 were in Russian, and 2,624,658 were in Arabic. Generally speaking, the study identified a high frequency of hacking/security tools – for example, online shopping site receipt generators for phishing purposes.</p>
    <p>Some forums specialized in other services such as mobile malware, breached data, cryptocurrency mining malware, code for AI bots, and login dumps. The multilingual feature of the study&#8217;s collection can facilitate cybersecurity research in cross-countries comparison. The highly prolific nature of forums as well as their dynamic and time-sensitive features enables CTI analysts to detect trends of cyber threats easier and sometimes earlier than other platforms. As such, a promising research direction can formulate time-sensitive methods in order to analyze the trends of cyber threat landscape via constant monitoring of data obtained from various forums.</p>
    <p><strong>2- IRCs:</strong></p>
    <p>The study collected 2,791,120 lines of chat conversations obtained from 13 IRC cybersecurity specific IRC channels in the period between September 2016 and January 2018. The data collection is summarized in Table (1) which includes the top 6 channels.</p>
    <table>
    <tbody>
    <tr>
    <td>Channel</td>
    <td># of lines</td>
    <td>Description</td>
    </tr>
    <tr>
    <td>#anonops</td>
    <td>1,696,024</td>
    <td>General discussion of hacking-related topics</td>
    </tr>
    <tr>
    <td>#ed</td>
    <td>574,024</td>
    <td>Discussion about current hacking topics</td>
    </tr>
    <tr>
    <td>#hackers</td>
    <td>174,328</td>
    <td>General discussion of tips and tricks for Anonymous hackers</td>
    </tr>
    <tr>
    <td>#Evilzone</td>
    <td>163,402</td>
    <td>Casual discussions on cyber security</td>
    </tr>
    <tr>
    <td>#ddos</td>
    <td>23,172</td>
    <td>Posts about currently available ddos tools recommended by Anonymous hackers</td>
    </tr>
    <tr>
    <td>#tutorials</td>
    <td>77,903</td>
    <td>Offers selected members tutorials via a separate interactive IRC channel</td>
    </tr>
    <tr>
    <td><strong>Total (of all channels)</strong></td>
    <td><strong>2,791,120</strong></td>
    <td></td>
    </tr>
    </tbody>
    </table>
    <p><strong>Table (1): Summary of collected IRC data</strong></p>
    <p>The most popular IRC channel, “anonops,” is the main channel for the well known hacktivist group, Anonymous. Anonymous also runs other channels, such as “ddos” which is centered on Distributed Denial-of-Service (DDoS) attacks and “hacker” in which users share hacking tips. IRC users also provide and ask for hacking services with target information. While previous studies have delved into the IRC participant duration, the CTI value of IRC data is still undiscovered. The URLs, links, and named entities exchanged in IRC chatrooms can be used in a snowball sampling manner to maximize cyber threat resources. Following identification of resources, a promising research direction would be identification of conversation topics via topic modeling approaches (e.g., Latent Dirichlet Allocation). Techniques including Named Entity Recognition (NER) and relationship extraction can pinpoint the targets of hackers and hacktivists in IRC.</p>
    <p><strong>3- Darknet marketplaces:</strong></p>
    <p>The study identified 12 darknet marketplaces in the period between September 2016 and January 2018. Table (2) summarizes the darknet marketplace data collection.</p>
    <table>
    <tbody>
    <tr>
    <td>Darknet marketplace</td>
    <td># of listing</td>
    <td># of security listing</td>
    <td>Language</td>
    </tr>
    <tr>
    <td>0day</td>
    <td>28,330</td>
    <td>28,330+</td>
    <td>English</td>
    </tr>
    <tr>
    <td>Alphabay</td>
    <td>25,118</td>
    <td>N/A</td>
    <td>English</td>
    </tr>
    <tr>
    <td>Apple Market</td>
    <td>2,012</td>
    <td>N/A</td>
    <td>English</td>
    </tr>
    <tr>
    <td>Dream Market</td>
    <td>120,962</td>
    <td>1,916+</td>
    <td>English</td>
    </tr>
    <tr>
    <td>French Deep Web</td>
    <td>1,536</td>
    <td>134+</td>
    <td>French</td>
    </tr>
    <tr>
    <td>Hansa</td>
    <td>14,149</td>
    <td>N/A</td>
    <td>English</td>
    </tr>
    <tr>
    <td>Minerva</td>
    <td>166</td>
    <td>N/A</td>
    <td>English</td>
    </tr>
    <tr>
    <td>Russian Silk Road</td>
    <td>488</td>
    <td>N/A</td>
    <td>Russian</td>
    </tr>
    <tr>
    <td>SilkRoad3</td>
    <td>1,798</td>
    <td>70+</td>
    <td>English</td>
    </tr>
    <tr>
    <td>TradeRoute</td>
    <td>35,504</td>
    <td>547+</td>
    <td>English</td>
    </tr>
    <tr>
    <td>TOCHKA</td>
    <td>1,958</td>
    <td>300+</td>
    <td>Russian/English</td>
    </tr>
    <tr>
    <td>Valhalla</td>
    <td>17,576</td>
    <td>695+</td>
    <td>English</td>
    </tr>
    <tr>
    <td><strong>Total:</strong></td>
    <td><strong>249,597</strong></td>
    <td><strong>31,992+</strong></td>
    <td><strong>English/Russian/ French/Dutch</strong></td>
    </tr>
    </tbody>
    </table>
    <p><strong>Table (2): Summary of darknet marketplace data collection</strong></p>
    <p>All darknet marketplaces, except for 0day, include illicit products which are not limited to cybersecurity. Among these darknet marketplaces, 60% of the product listings were drug related. Cybersecurity-related products represented around 20%, while the remainder were related to weapons and stolen personal data. 0day data, on the other hand, included only exploits. Such listings included information about the exploit category, description, the platform the exploit is related to and its severity level. Most of the product listings were originally priced. Once a patch or fix for the exploit emerges, the product listing becomes free. In the study&#8217;s collection, only 37 out of 28,330 exploits were priced, and the remainder were free. Figure (2) is an example of <a href="https://www.deepdotweb.com/2015/04/08/therealdeal-dark-net-market-for-code-0days-exploits/">0day exploit</a> listing.</p>
    <p><img class="wp-image-28126" src="/imgs/2019/01/word-image-21.png" srcset="/imgs/2019/01/word-image-21.png 687w, /imgs/2019/01/word-image-21-300x224.png 300w" sizes="(max-width: 687px) 100vw, 687px" /></p>
    <p><strong>Figure (2): An example of a product listing of a zero day exploit</strong></p>
    <p>Since darknet marketplaces are relatively new compared to other hacker platforms, there are more untapped research opportunities in this area. Based on the collected darknet marketplace data the study obtained, a rise in the number of non-English marketplaces was identified. More specifically, multilingual identification of cyber threats across darknet marketplaces with different languages, such as Russian and French, can markedly add a global insight to cyber threats. Cross-platform studies can be expanded beyond analysis of darknet marketplaces with different languages.</p>
    <p><strong>4- Carding shops:</strong></p>
    <p>From May 2014 to January 2018, the study collected data from 26 carding shops with 8,674,078 listings. The majority represented <a href="https://www.deepdotweb.com/2018/11/19/an-overview-of-the-armor-black-market-quarterly-report/">credit card dumps</a> (6,596,093 listings), followed by Fullz and SSNs at respectively 1,999,251 and 78,734. Table (3) summarizes the study&#8217;s data collection from nine carding shops.</p>
    <table>
    <tbody>
    <tr>
    <td>Name</td>
    <td># of CVV and Fullz</td>
    <td># of Dumps</td>
    <td># of SSN</td>
    <td>Total</td>
    </tr>
    <tr>
    <td>Jokers Stash</td>
    <td>566,600</td>
    <td>446,642</td>
    <td>0</td>
    <td>1,013,242</td>
    </tr>
    <tr>
    <td>DUMPS MANIA</td>
    <td>42,311</td>
    <td>777,634</td>
    <td>0</td>
    <td>819,945</td>
    </tr>
    <tr>
    <td>Buybest</td>
    <td>9,008</td>
    <td>790,325</td>
    <td>0</td>
    <td>799,333</td>
    </tr>
    <tr>
    <td>United Dumps</td>
    <td>63,575</td>
    <td>734,495</td>
    <td>0</td>
    <td>798,070</td>
    </tr>
    <tr>
    <td>THE MONEY TEAM</td>
    <td>20,462</td>
    <td>750,642</td>
    <td>0</td>
    <td>771,104</td>
    </tr>
    <tr>
    <td>EBIN CC</td>
    <td>13,786</td>
    <td>752,441</td>
    <td>0</td>
    <td>766,227</td>
    </tr>
    <tr>
    <td>Golden Shop</td>
    <td>19,732</td>
    <td>727,888</td>
    <td>0</td>
    <td>747,620</td>
    </tr>
    <tr>
    <td>Getcc Shop</td>
    <td>609,770</td>
    <td>0</td>
    <td>0</td>
    <td>609,770</td>
    </tr>
    <tr>
    <td>BuySSN</td>
    <td>0</td>
    <td>0</td>
    <td>78,734</td>
    <td>78,734</td>
    </tr>
    <tr>
    <td><strong>Total (of all shops)</strong></td>
    <td><strong>1,999,251</strong></td>
    <td><strong>6,596,093</strong></td>
    <td><strong>78,734</strong></td>
    <td><strong>8,674,078</strong></td>
    </tr>
    </tbody>
    </table>
    <p><strong>Table (3): Summary of carding shops data collection</strong></p>
    <p>Nine shops focused on selling payment card information. Six of them, such as Getcc Shop and Diamond Dumps, contained only Fullz data. Generally speaking, price for payment card data varied greatly, and similar card data were frequently found across different carding shops. BuySSN (78,734 records), specialized in selling SSNs. Such information can result in serious personal losses. One promising CTI direction is identifying individuals whose data have been breached. That is, having both the name and zip code of each stolen card would help identify the individual with high precision, which is greatly useful for credit card companies and law enforcement agencies. Given that both darknet marketplaces and carding shops share credit card information, cross-referencing the stolen or breached data on carding shops with darknet marketplaces provides new insights regarding the dissemination patterns of stolen data in the ecosystem.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/approaches/" rel="tag">approaches</a> <a href="https://www.deepdotweb.com/tag/current/" rel="tag">current</a> <a href="https://www.deepdotweb.com/tag/cyber/" rel="tag">cyber</a> <a href="https://www.deepdotweb.com/tag/dark/" rel="tag">dark</a> <a href="https://www.deepdotweb.com/tag/intelligence/" rel="tag">intelligence</a> <a href="https://www.deepdotweb.com/tag/overseeing/" rel="tag">overseeing</a> <a href="https://www.deepdotweb.com/tag/research/" rel="tag">research</a> <a href="https://www.deepdotweb.com/tag/threat/" rel="tag">threat</a> <a href="https://www.deepdotweb.com/tag/web/" rel="tag">web</a></span> <span style="display:none" class="updated">2019-01-17</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

