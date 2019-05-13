---
title: "New Tor Security Advisory: &#8220;Relay Early&#8221; Traffic Confirmation Attack"
---

<article class="post-listing post-6653 post type-post status-publish format-standard has-post-thumbnail hentry  tag-advisory tag-attack tag-confirmation tag-early tag-relay tag-security  tag-traffic">
Posted by: DeepDotWeb
<span>July 30, 2014</span>
<span>in <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://www.deepdotweb.com/category/news-updates/" rel="category tag">News Updates</a></span>
<a href="/2014/07/30/new-tor-security-advisory-relay-early-traffic-confirmation-attack/#respond">Leave a comment</a></span>
</p>
<div class="clear"></div>
<div class="entry">
<p>This advisory was posted on the <a href="https://lists.torproject.org/pipermail/tor-announce/2014-July/000094.html">tor-announce</a> mailing list and published on the <a href="https://blog.torproject.org/blog/tor-security-advisory-relay-early-traffic-confirmation-attack">Torproject blog</a>, This is the summary:</p>
<blockquote><p>On July 4 2014 we found a group of relays that we assume were trying to deanonymize users. They appear to have been targeting people who operate or access Tor hidden services. The attack involved modifying Tor protocol headers to do traffic confirmation attacks.</p>
<p>The attacking relays joined the network on January 30 2014, and we removed them from the network on July 4. While we don&#8217;t know when they started doing the attack, <span style="color: #ff0000;"><strong>users who operated or accessed hidden services from early February through July 4 should assume they were affected</strong></span>.</p>
<p>Unfortunately, it&#8217;s still unclear what &#8220;affected&#8221; includes. We know the attack looked for users who fetched hidden service descriptors, but the attackers likely were not able to see any application-level traffic (e.g. what pages were loaded or even whether users visited the hidden service they looked up). The attack probably also tried to learn who published hidden service descriptors, which would allow the attackers to learn the location of that hidden service. In theory the attack could also be used to link users to their destinations on normal Tor circuits too, but we found no evidence that the attackers operated any exit relays, making this attack less likely. And finally, we don&#8217;t know how much data the attackers kept, and due to the way the attack was deployed (more details below), their protocol header modifications might have aided other attackers in deanonymizing users too.</p>
<p>Relays should upgrade to a recent Tor release (<a href="https://lists.torproject.org/pipermail/tor-announce/2014-July/000093.html">0.2.4.23</a> or <a href="https://lists.torproject.org/pipermail/tor-talk/2014-July/034180.html">0.2.5.6-alpha</a>), to close the particular protocol vulnerability the attackers used — but remember that preventing traffic confirmation in general remains an open research problem. Clients that upgrade (once new Tor Browser releases are ready) will take another step towards limiting the number of entry guards that are in a position to see their traffic, thus reducing the damage from future attacks like this one. <strong><span style="color: #ff0000;">Hidden service operators should consider changing the location of their hidden service.</span></strong></p></blockquote>
<p>This info followed by more technical details about this attack, you can and should read the rest of the post <a href="https://blog.torproject.org/blog/tor-security-advisory-relay-early-traffic-confirmation-attack">here.</a></p>
<p>And the final chapter was open questions about this attack:</p>
<blockquote><p>OPEN QUESTIONS:</p>
<p>Q1) Was this the Black Hat 2014 talk that got canceled recently?<br/>
    Q2) Did we find all the malicious relays?<br/>
    Q3) Did the malicious relays inject the signal at any points besides the HSDir position?<br/>
    Q4) What data did the attackers keep, and are they going to destroy it? How have they protected the data (if any) while storing it?</p>
<p>Great questions. We spent several months trying to extract information from the researchers who were going to give the Black Hat talk, and eventually we did get some hints from them about how &#8220;relay early&#8221; cells could be used for traffic confirmation attacks, which is how we started looking for the attacks in the wild. They haven&#8217;t answered our emails lately, so we don&#8217;t know for sure, but it seems likely that the answer to Q1 is &#8220;yes&#8221;. In fact, we hope they *were* the ones doing the attacks, since otherwise it means somebody else was. We don&#8217;t yet know the answers to Q2, Q3, or Q4.</p></blockquote>
<p>Keep yourself updated with this topic at the Torproject blog post: <a href="https://blog.torproject.org/blog/tor-security-advisory-relay-early-traffic-confirmation-attack">https://blog.torproject.org/blog/tor-security-advisory-relay-early-traffic-confirmation-attack</a></p>
<p>Also there are discussions going on reddit /r/dnm , /r/onions and /r/tor.</p>
</div>
<a href="https://www.deepdotweb.com/tag/advisory/" rel="tag">advisory</a> <a href="https://www.deepdotweb.com/tag/attack/" rel="tag">attack</a> <a href="https://www.deepdotweb.com/tag/confirmation/" rel="tag">confirmation</a> <a href="https://www.deepdotweb.com/tag/early/" rel="tag">early</a> <a href="https://www.deepdotweb.com/tag/relay/" rel="tag">relay</a>   <a href="https://www.deepdotweb.com/tag/traffic/" rel="tag">traffic</a></span> 
Updated: 2014-07-30
    
