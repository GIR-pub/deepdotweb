---
Tor to Combat Malicious Node Problem
---
<article class="post-listing post-14962 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news category-news-updates tag-combat tag-malicious tag-node tag-problem tag-tor">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/caliens/" title="">C. Aliens </a></span>
    <span>July 31, 2016</span>
    <span>in <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://www.deepdotweb.com/category/news-updates/" rel="category tag">News Updates</a></span>
    <span><a href="https://www.deepdotweb.com/2016/07/31/tor-combat-malicious-node-problem/#comments">6 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>The discovery of over a <a href="https://www.deepdotweb.com/2016/07/07/researchers-found-over-100-snooping-tor-hsdir-relays/">hundred malicious nodes</a> has prompted the Tor Network to develop a new design which is designed to fight this ongoing problem.</p>
    <p><a href="https://threatpost.com/upcoming-tor-design-battles-hidden-services-snooping/119462/">Developer Sebastian Hahn assured</a> that code has already been written to address this issue, and that the release date is being determined. The Tor Network has said that the attacks do not unmask the operator behind the hidden service, which the law enforcement community has been trying to accomplish for some time now.</p>
    <p>Amirali Sanatinia, who is working on his PhD in computer science at Northeastern University, is responsible for this discovery. Alongside his professor at the College of Computer and Information Science, Guevara Noubir; they are set to present their paper next week at DEF CON.</p>
    <p>The paper, “<a href="https://www.securityweek2016.tu-darmstadt.de/fileadmin/user_upload/Group_securityweek2016/pets2016/10_honions-sanatinia.pdf">HOnions: Towards Detection and Identification of Misbehaving Tor HSDirs</a>”, tells of a framework called Honey onions, or HOnions that Sanatinia and Noubir developed that identifies these malicious HSDirs.</p>
    <p>They two launched the framework in daily, weekly, and monthly runs from Feb. 12 to April 24 and found exactly 110 malicious nodes, most of which were hosted in the US. Others from Germany, France, the Netherlands and the UK were found. They exposed Tor relays wish HSDirs capabilities that have been made to spoof hidden services. Tor estimated that there are currently around 3,000 HSDirs within its network.</p>
    <p>“What the attack allows you to do is to learn about the existence of a hidden service. This does not mean that the identity of the operator is revealed or anything catastrophic like that,” Hahn said.</p>
    <p>“Noubir and Sanatinia’s attack essentially snoops hidden service’s metadata and tells the attacker that a service exists and when it’s available,” Hahn added.</p>
    <p>In an interview Noubir said that the hidden service directories they have found to be malicious could be run <a href="https://blog.torproject.org/blog/new-research-northeastern-university">by researchers studying the dark web</a>, or law enforcement or other state agencies as part of investigations.</p>
    <p>“At this stage, hard to tell who is doing what. What we could see is there is some diversity in what they are doing. Some are attacking these hidden services, or in some way collecting information about them,” Noubir said in his interview.</p>
    <p>More than 70 percent of the malicious directories they discovered are hosted on cloud infrastructure. A quarter of which are exit nodes. Hosting the services on cloud infrastructure makes it difficult to find out who is behind them. These are paid for in bitcoin, and have no contact information attacked to them.</p>
    <p>Hahn reported that the number of exit nodes found in this research is alarming and is most likely and indicator saying that the operators didn’t take necessary care as being an exit node is the default configuration.</p>
    <p>“The way we’re working on it for the future is by using a stronger cryptographic protocol that does not allow the Tor servers involved in the regular operation of the network to see a portion of the metadata about hidden services,” Hahn said.</p>
    <p>Noubir commented that the ones snooping are trying to learn information about services like the .onion address where it is being operated on. They’re paper explains how the attack could use the information gained to build a list of targets to launch other attacks at.</p>
    <p>“They’re trying to look inside the .onion and carry out user enumeration or run cross site scripting attacks, typical attacks you’d see against regular websites which are more interesting in context. If you’re running a hidden service, you don’t want to be discovered,” Noubir said.</p>
    <p>The paper described one snooping directory as sending hourly queries to an Apache server for status updates, that are provided by mod status in Apache. More were executed using SQL injection, path traversal attacks, and XSS.</p>
    <p>Running their investigation Noubir and Sanatinia used HOnions to detect these malicious nodes. They ran 1,500 at one time, on the daily, weekly or monthly schedule. Each answering to a process running locally that would log visits by those HSDirs. In the paper, they said that most of the 40,000 visits from that were logged were said to be automated and queried the root path of the server, but that they also didn’t detect manual probing in around 20 percent of the requests. Some of them would not visit a service right away after hosting it, to avoid suspicion and be detected.</p>
    <p>&nbsp;</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/combat/" rel="tag">combat</a> <a href="https://www.deepdotweb.com/tag/malicious/" rel="tag">malicious</a> <a href="https://www.deepdotweb.com/tag/node/" rel="tag">node</a> <a href="https://www.deepdotweb.com/tag/problem/" rel="tag">problem</a> <a href="https://www.deepdotweb.com/tag/tor/" rel="tag">tor</a></span> <span style="display:none" class="updated">2016-07-31</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/caliens/" title="Posts by C. Aliens" rel="author">C. Aliens</a></strong></div>
    </div>
</article>

