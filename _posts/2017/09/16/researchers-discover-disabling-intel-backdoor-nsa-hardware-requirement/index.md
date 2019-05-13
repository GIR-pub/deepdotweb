---
Researchers Discover Disabling of Intel ME Backdoor Through NSA Hardware Requirement
---
<article class="post-listing post-22571 post type-post status-publish format-standard has-post-thumbnail hentry 
 tag-backdoor tag-disabling tag-discover tag-hardware tag-intel tag-nsa tag-requirement tag-researchers">
    
<div class="post-inner">
    
    
        
<span>Posted by: <a href="https://www.deepdotweb.com/author/dividedby0/" title="">DividedBy0 </a></span>
    
    
<span>September 16, 2017</span>
<span>in <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://www.deepdotweb.com/category/news-updates/" rel="category tag">News Updates</a></span>
    
<span><a href="https://www.deepdotweb.com/2017/09/16/researchers-discover-disabling-intel-backdoor-nsa-hardware-requirement/#comments">12 Comments</a></span>
</p>
<div class="clear"></div>
    
    
    
<p>Researchers from the cybersecurity company known as Positive Technologies have <a href="http://blog.ptsecurity.com/2017/08/disabling-intel-me.html">discovered a way to disable the embedded Management Engine (ME) controller chip</a> of Intel processors. It is also known as a coprocessor. The ME chip allows for remote management of a computer and has <a href="https://hackaday.com/2016/01/22/the-trouble-with-intels-management-engine/">long</a> been <a href="https://i.redd.it/id88hvysu3ny.png">considered</a> a <a href="https://www.deepdotweb.com/2017/01/25/comprehensive-guide-backdoors/">backdoor</a>. In the past, the Electronic Frontier Foundation (EFF) has called the <a href="https://www.eff.org/deeplinks/2017/05/intels-management-engine-security-hazard-and-users-need-way-disable-it">Management Engine a security hazard</a>, and demanded that users be given the ability to disable it. The embedded ME chip is part of Intel’s Active Management Technology (AMT) and it runs independently of the computer’s main processor and its operating system. ME is embedded onto the Platform Controller Hub (PCH), which gives it access to all data being sent and received by the main processor and all devices. The ME chip has its own firmware and operating system. The code on the ME chip is not publicly available, which has led many to mistrust it and call it a <a href="https://www.deepdotweb.com/tag/backdoor/">backdoor</a>.</p>
<p>The embedded ME chip can be found on every Intel x86 processor made after 2006. A <a href="https://nvd.nist.gov/vuln/detail/CVE-2017-5689">major vulnerability</a> with Intel’s AMT was discovered in May of this year, which was a remote code execution vulnerability <a href="https://www.deepdotweb.com/2017/05/21/intel-chips-from-last-7-years-can-be-hacked-remotely/">found in millions of Intel chips</a>. Prior attempts to disable the ME chip have failed, or were only partially successful. The <a href="https://github.com/corna/me_cleaner">me_cleaner project</a> created software that allowed a user to erase most of the ME firmware, but this would only work for about a half of an hour, after which the ME chip would enter a recovery mode which would cause the computer to reboot. Because the firmware is compressed using the Huffman encoding technique, the researchers at Positive Technologies had to develop a piece of software called the Intel ME 11.x Firmware Images Unpacker, or, unME11. The software has been released to the public on github. It consists of two Python scripts which unpack firmware regions for the <a href="https://www.deepdotweb.com/tag/intel/">Intel</a> ME 11 series.</p>
<p>The ability to disable the ME chip is made possible thanks to, of all things, an NSA program. The NSA established the <a href="https://trustedcomputinggroup.org/high-assurance-platform-program/">High Assurance Platform (HAP) program</a> to work with the tech industry to develop secure computing platforms. Since ME actually is a security risk, the NSA would want Intel to give them the ability to disable it. The NSA would want to minimize side-channel leaks. Intel confirmed this after the research from Positive Technologies was released.</p>
<p>“In response to requests from customers with specialized requirements we sometimes explore the modification or disabling of certain features. In this case, the modifications were made at the request of equipment manufacturers in support of their customer’s evaluation of the U.S. government’s “High Assurance Platform” program. These modifications underwent a limited validation cycle and are not an officially supported configuration,” a spokesperson for Intel said.</p>
<p>The researchers were able to find a <a href="https://www.bleepingcomputer.com/news/hardware/researchers-find-a-way-to-disable-much-hated-intel-me-component-courtesy-of-the-nsa/">HAP mode</a> thanks to a couple pieces of software that Intel creates for motherboard manufacturers. This software allows a few modifications to be made to ME. The two tools used are the Flash Image Tool (FIT) and the Flash Programming Tool (FPT). With these tools the researchers were able to obtain XML files that described the structure of the ME firmware and find special configuration bits for the PCH. One of these configurations was called “reserve_hap” that included the comment “High Assurance Platform (HAP) enable” which made the researchers curious.</p>
<p>The researchers then enabled the HAP enable configuration, and discovered that the ME chip was disabled. The ME chip would not respond to any commands with HAP mode enabled. Once HAP mode is enabled, a change is made to the Boot Guard policies. Positive Technologies will continue to investigate the Management Engine, and will try to uncover how exactly how HAP mode changes Boot Guard and other changes. They warn their hack is experimental and has not been fully tested and requires a Serial Peripheral Interface (SPI) programmer.</p>
    
    
</div><!-- .entry /-->
<a href="https://www.deepdotweb.com/tag/backdoor/" rel="tag">backdoor</a> <a href="https://www.deepdotweb.com/tag/disabling/" rel="tag">disabling</a> <a href="https://www.deepdotweb.com/tag/discover/" rel="tag">discover</a> <a href="https://www.deepdotweb.com/tag/hardware/" rel="tag">hardware</a> <a href="https://www.deepdotweb.com/tag/intel/" rel="tag">intel</a> <a href="https://www.deepdotweb.com/tag/nsa/" rel="tag">nsa</a> <a href="https://www.deepdotweb.com/tag/requirement/" rel="tag">requirement</a> <a href="https://www.deepdotweb.com/tag/researchers/" rel="tag">researchers</a></span>				<span style="display:none" class="updated">2017-09-16</span>
<div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/dividedby0/" title="Posts by DividedBy0" rel="author">DividedBy0</a></strong></div>
    
    
</div><!-- .post-inner -->
</article><!-- .post-listing -->

