---
Tor Update Supports v3 Onion Services
---
<article class="post-listing post-23051 post type-post status-publish format-standard has-post-thumbnail hentry 
 tag-onion tag-services tag-supports  tag-update tag-v3">
<div class="post-inner">
<span>Posted by: <a href="https://www.deepdotweb.com/author/caliens/" title="">C. Aliens </a></span>
<span>October 14, 2017</span>
<span>in <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://www.deepdotweb.com/category/news-updates/" rel="category tag">News Updates</a></span>
<span><a href="https://www.deepdotweb.com/2017/10/14/tor-update-supports-v3-onion-services/#comments">7 Comments</a></span>


<p>&nbsp;</p>
<p>The second latest alpha build of Tor, Tor 0.3.2.2-alpha, enabled the more secure “next-generation hidden services protocol” (aka v3 onion services). Tor Project President Roger Dingledine said that next generation hidden (onion) services fix security and design flaws found in the original or legacy hidden services. He explained that mistakes he had made in the 2004 onion service protocol are being exploited by “fear-mongering ‘threat intelligence’ companies.” In this alpha build, some of the updates from <a href="https://gitweb.torproject.org/torspec.git/tree/proposals/224-rend-spec-ng.txt">proposal 224</a> have been added to Tor, including several directory protocol improvements and updated cryptographic building blocks.</p>
<p>At Def Con 25, <a href="https://defcon.org/html/defcon-25/dc-25-speakers.html#Dingledine">Dingledine presented v3 onion services</a> and announced that a public build would likely be available in December 2017. Until then, the alpha build(s) will support prop224 onion services for both onion service operators and clients themselves and hopefully provide a testing platform for a stable build in December. <a href="https://www.deepdotweb.com/tag/tor/">Tor Browser</a> 7.5a5 includes support for the new services, along with other significant changes to the way Tor functions.</p>
<p>￼￼ <img class="wp-image-23057 aligncenter" src="/imgs/2017/10/screenshot-from-2017-10-07-16-19-32-png.png" alt="Screenshot from 2017-10-07 16-19-32.png" srcset="/imgs/2017/10/screenshot-from-2017-10-07-16-19-32-png.png 576w, /imgs/2017/10/screenshot-from-2017-10-07-16-19-32-png-300x250.png 300w" sizes="(max-width: 576px) 100vw, 576px" /></p>
<p>Some of the included <a href="https://blog.torproject.org/tor-0322-alpha-released">updates in the 0.3.2.2-alpha</a> are listed as follows:</p>
<ul>
<li>The cryptographic building blocks use updated or more secure signature algorithms and hashing methods. For instance, the older SHA1/DH/RSA1024 was swapped with SHA3/ed25519/curve25519.</li>
<li>Directory protocol has been improved and now leaks less metadata to directory servers. This is, in part, to avoid attacks where a hidden service can be censored easily based on the descriptor. To prevent predictability Tor uses, different, pseudo random variables. Time period, public keys, shared random values, etc.</li>
<li>“Better onion address security against impersonation; more extensible introduction/rendezvous protocol; and a cleaner and more modular codebase.”</li>
</ul>
<p>As time goes on and more users test v3 onion services, additional prop224 features will likely make their way to Tor and the Tor Browser. They announced that, in the future, some of the next updates will include advanced client authorization and improved guard algorithms.</p>
<p><img class="wp-image-23058 aligncenter" src="/imgs/2017/10/screenshot-from-2017-10-07-16-29-07-png.png" alt="Screenshot from 2017-10-07 16-29-07.png" srcset="/imgs/2017/10/screenshot-from-2017-10-07-16-29-07-png.png 712w, /imgs/2017/10/screenshot-from-2017-10-07-16-29-07-png-300x219.png 300w" sizes="(max-width: 712px) 100vw, 712px" /></p>
<p>“[M]istakes in the original protocol are now being actively exploited by fear-mongering ‘threat intelligence’ companies to build lists of onion services even when the service operators thought they would stay under the radar,” the Tor Co-founder said at Def Con 25. “These design flaws are a problem because people rely on onion services for many cool use cases, like metadata-free chat and file sharing, safe interaction between journalists and their sources, safe software updates, and more secure ways to reach popular websites like Facebook.”</p>
<p>One can recognize the new onion service addresses by the length of the address: 56 characters. They are noticeably longer than v2 onion service addresses. One current example is <a href="https://www.deepdotweb.com/2015/08/03/which-secure-email-provider-is-the-one-for-you/">Riseup’s</a> v3 onion address: http://vww6ybal4bd7szmgncyruucpgfkqahzddi37ktceo3ah7ngmcopnpyyd[dot]onion.</p>
<p>Instructions on setting up a prop224 service can be found on the Tor Blog.</p>
</div>
<span style="display:none"><a href="https://www.deepdotweb.com/tag/onion/" rel="tag">onion</a> <a href="https://www.deepdotweb.com/tag/services/" rel="tag">services</a> <a href="https://www.deepdotweb.com/tag/supports/" rel="tag">supports</a> <a href="https://www.deepdotweb.com/tag/tor/" rel="tag">tor</a> <a href="https://www.deepdotweb.com/tag/update/" rel="tag">update</a> <a href="https://www.deepdotweb.com/tag/v3/" rel="tag">v3</a></span> <span style="display:none" class="updated">2017-10-14<a href="https://www.deepdotweb.com/author/caliens/" title="Posts by C. Aliens" rel="author">C. Aliens</a></strong></div>
</div>
</article>

