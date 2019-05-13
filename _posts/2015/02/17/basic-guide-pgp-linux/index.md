---
Basic Guide to PGP On Linux
---
<article class="post-listing post-9094 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-basic tag-guide tag-linux tag-pgp">
<div class="post-inner">
<span>Posted by: <a href="https://www.deepdotweb.com/author/admin/" title="">DeepDotWeb </a></span>
<span>February 17, 2015</span>

<span><a href="https://www.deepdotweb.com/2015/02/17/basic-guide-pgp-linux/#comments">68 Comments</a></span>
</p>
<div class="clear"></div>
<div class="entry">
<div class="usertext-body may-blank-within md-container">
<div class="md">
<p><em>Full credit goes to <a href="http://www.reddit.com/user/MLP_is_my_OPSEC">MLP_is_my_OPSEC</a> for writing this tutorial &#8211; Thanks for publishing  and giving us your permission to post it!</em></p>
<h3>Part 0 &#8211; Introduction</h3>
<p>I promised it, and here it is! The PGP guide for Linux! Great timing too for Moronic Monday. For this guide we&#8217;ll be using GnuPG with Gnu Privacy Assistant as a graphical front-end. We will be using CLI to install these two pieces of software, and creating the keypair. The example OS in question is Linux Mint, so the commands for install may differ from your current OS. Don&#8217;t fret though! That&#8217;s the only part that may not be relevant to your OS, the rest of the guide will be the same across distros.</p>
<p style="text-align: center;"><a href="https://www.deepdotweb.com/vpn-comparison-chart/">&gt;&gt;&gt;Add A Layer Of Encryption: Click For The Best VPN Services&lt;&lt;&lt;</a></p>
<h3>Part 1 – Installing the software</h3>
<p>Like I said in the intro, we&#8217;ll be using GnuPG with Gnu Privacy Assistant. I like GPA as a graphical front-end because its layout is really easy to understand and follow.</p>
<ol>
<li>Open up Terminal</li>
<li>Type, without quotes, &#8216;sudo apt-get install gpa gnupg2&#8217;, then hit &#8216;enter&#8217;</li>
<li>Enter your password, hit &#8216;enter&#8217;</li>
<li>It will pull the dependancies needed for both to work properly, tell you the space needed, and ask you to confirm. Type &#8216;y&#8217; then hit &#8216;enter&#8217; to confirm</li>
<li>Wait a bit as everything installs</li>
</ol>
<p>This should only take a few minutes to complete. See this picture to confirm you&#8217;re doing the steps correctly:</p>
<p><a href="/imgs/2015/02/TVjAVPp1.png"><img class="aligncenter size-full wp-image-9095" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/TVjAVPp1.png" alt="TVjAVPp[1]" width="657" height="284" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/TVjAVPp1.png 657w, https://www.deepdotweb.com/wp-content/uploads/2015/02/TVjAVPp1-300x130.png 300w" sizes="(max-width: 657px) 100vw, 657px" /></a></p>
<h3>Part 2 – Generating your keypair</h3>
<p>Part 1 was easy, eh? Don&#8217;t worry things don&#8217;t get much harder. The next step is to create your keypair. We&#8217;ll be using 4096 bit RSA to keep things extra secure!</p>
<ol>
<li>In your Terminal, type without quotes &#8216;gpg &#8211;gen-key&#8217;, then hit &#8216;enter&#8217;</li>
<li>It will ask you what kind of key you want. For our usecase, we want option &#8216;1&#8217; :<a href="/imgs/2015/02/TsvxqSl1.png"><img class="aligncenter size-full wp-image-9096" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/TsvxqSl1.png" alt="2" width="659" height="322" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/TsvxqSl1.png 659w, https://www.deepdotweb.com/wp-content/uploads/2015/02/TsvxqSl1-300x147.png 300w" sizes="(max-width: 659px) 100vw, 659px" /></a></li>
<li>Next step is key length. The longer the length, the more secure it is. We&#8217;ll go with 4096 bits: <a href="/imgs/2015/02/33FN8mb1.png"><img class="aligncenter size-full wp-image-9097" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/33FN8mb1.png" alt="33FN8mb[1]" width="657" height="37" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/33FN8mb1.png 657w, https://www.deepdotweb.com/wp-content/uploads/2015/02/33FN8mb1-300x17.png 300w" sizes="(max-width: 657px) 100vw, 657px" /></a></li>
<li>It will now ask if you want your key to expire after a certain amount of time. This is up to personal preference, but we&#8217;ll choose &#8216;key does not expire&#8217;, so just hit &#8216;enter&#8217; <a href="/imgs/2015/02/EmYMtKE1.png"><img class="aligncenter size-full wp-image-9098" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/EmYMtKE1.png" alt="3" width="658" height="139" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/EmYMtKE1.png 658w, https://www.deepdotweb.com/wp-content/uploads/2015/02/EmYMtKE1-300x63.png 300w" sizes="(max-width: 658px) 100vw, 658px" /></a></li>
<li>Confirm that yes, the key will not expire. Type &#8216;y&#8217;, then hit &#8216;enter&#8217; <a href="/imgs/2015/02/eGqruqQ1.png"><img class="aligncenter size-full wp-image-9099" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/eGqruqQ1.png" alt="eGqruqQ[1]" width="658" height="38" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/eGqruqQ1.png 658w, https://www.deepdotweb.com/wp-content/uploads/2015/02/eGqruqQ1-300x17.png 300w" sizes="(max-width: 658px) 100vw, 658px" /></a></li>
<li>The next step will be to enter an ID to make it easier for people to identify your key. If you&#8217;ve made it this far, you should know what to do <a href="/imgs/2015/02/LgkPV7n1.png"><img class="aligncenter size-full wp-image-9100" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/LgkPV7n1.png" alt="LgkPV7n[1]" width="655" height="129" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/LgkPV7n1.png 655w, https://www.deepdotweb.com/wp-content/uploads/2015/02/LgkPV7n1-300x59.png 300w" sizes="(max-width: 655px) 100vw, 655px" /></a></li>
<li>It will ask if this information is correct. If it is, type &#8216;O&#8217; and hit &#8216;enter&#8217; <a href="/imgs/2015/02/xxdJ8g41.png"><img class="aligncenter size-full wp-image-9101" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/xxdJ8g41.png" alt="xxdJ8g4[1]" width="657" height="70" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/xxdJ8g41.png 657w, https://www.deepdotweb.com/wp-content/uploads/2015/02/xxdJ8g41-300x32.png 300w" sizes="(max-width: 657px) 100vw, 657px" /></a><br />
<a href="https://xkcd.com/936/">Here is a great XKCD comic on creating secure passphrases</a></li>
<li>Enter a passphrase to protect your secret key. <a href="/imgs/2015/02/ZKXIiPW1.png"><img class="aligncenter size-full wp-image-9102" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/ZKXIiPW1.png" alt="ZKXIiPW[1]" width="657" height="55" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/ZKXIiPW1.png 657w, https://www.deepdotweb.com/wp-content/uploads/2015/02/ZKXIiPW1-300x25.png 300w" sizes="(max-width: 657px) 100vw, 657px" /></a></li>
<li>Here comes the fun part. It&#8217;s going to generate your key, and will ask you to do some random stuff to create entropy. I like to have a Youtube video going with a torrent running in the background, while randomly mashing keys in a text editor. See the picture for an example of what will be output in the terminal <a href="/imgs/2015/02/bshPVDM1.png"><img class="aligncenter size-full wp-image-9103" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/bshPVDM1.png" alt="bshPVDM[1]" width="676" height="422" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/bshPVDM1.png 676w, https://www.deepdotweb.com/wp-content/uploads/2015/02/bshPVDM1-300x187.png 300w" sizes="(max-width: 676px) 100vw, 676px" /></a></li>
<li>annnddddd we&#8217;re done! <a href="/imgs/2015/02/QFynRxp1.png"><img class="aligncenter size-full wp-image-9104" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/QFynRxp1.png" alt="QFynRxp[1]" width="676" height="196" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/QFynRxp1.png 676w, https://www.deepdotweb.com/wp-content/uploads/2015/02/QFynRxp1-300x87.png 300w" sizes="(max-width: 676px) 100vw, 676px" /></a></li>
</ol>
<h3>Part 3 – Obtaining your public key</h3>
<p>So we&#8217;ve installed the software, generated our super secure keypair. Now what? Well if you want to actually use it we need to obtain our public key. Everything from here will be done through the graphical front-end.</p>
<ol>
<li>Open Terminal, type &#8216;sudo gpa&#8217;, hit &#8216;enter&#8217;. Type in your password <sup>yeahIknowwhatyou&#8217;rethinking</sup></li>
<li>You&#8217;ll be greeted by this beautiful window <a href="/imgs/2015/02/eNSqF341.png"><img class="aligncenter size-full wp-image-9106" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/eNSqF341.png" alt="eNSqF34[1]" width="681" height="627" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/eNSqF341.png 681w, https://www.deepdotweb.com/wp-content/uploads/2015/02/eNSqF341-300x276.png 300w" sizes="(max-width: 681px) 100vw, 681px" /></a></li>
<li>Click on the keypair you just created, click &#8216;Keys&#8217; up at the top, then &#8216;Export keys&#8230;&#8217; <a href="/imgs/2015/02/reYpsUv1.png"><img class="aligncenter size-full wp-image-9107" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/reYpsUv1.png" alt="reYpsUv[1]" width="682" height="628" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/reYpsUv1.png 682w, https://www.deepdotweb.com/wp-content/uploads/2015/02/reYpsUv1-300x276.png 300w" sizes="(max-width: 682px) 100vw, 682px" /></a></li>
<li>Select where you want it saved, enter a filename, and click &#8216;Save&#8217;</li>
<li>Browse to the location in your file manager, open up that file with a text editor</li>
</ol>
<p>There&#8217;s your public key! Don&#8217;t forget to put this on your market profile so people can contact you easier.</p>
<h3>Part 4 – Obtaining your private key</h3>
<p>If you ever want to switch operating systems or PGP programs, you&#8217;ll need to do this. It&#8217;s just as easy as obtaining your public key. Make sure you keep this file safe!</p>
<ol>
<li>Hopefully you still have GPA open. If not, follow step #1 of Part 3</li>
<li>Click on your keypair, click &#8216;Keys&#8217; up at the top then &#8216;Backup&#8217; <a href="/imgs/2015/02/reYpsUv11.png"><img class="aligncenter size-full wp-image-9108" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/reYpsUv11.png" alt="reYpsUv[1]" width="682" height="628" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/reYpsUv11.png 682w, https://www.deepdotweb.com/wp-content/uploads/2015/02/reYpsUv11-300x276.png 300w" sizes="(max-width: 682px) 100vw, 682px" /></a></li>
<li>Select where you want it saved, keep the filename it gives you, and click &#8216;Save&#8217;</li>
<li>A window will pop up, you can back up to a floppy if you&#8217;re stuck in the &#8217;80s <a href="/imgs/2015/02/ucMIWk61.png"><img class="aligncenter size-full wp-image-9109" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/ucMIWk61.png" alt="ucMIWk6[1]" width="472" height="195" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/ucMIWk61.png 472w, https://www.deepdotweb.com/wp-content/uploads/2015/02/ucMIWk61-300x124.png 300w" sizes="(max-width: 472px) 100vw, 472px" /></a></li>
</ol>
<p>Remember to keep this file safe! Don&#8217;t forget your passphrase!</p>
<h3>Part 5 – Importing a public key</h3>
<p>So you want to buy some dank marijuanas, you&#8217;ll need to encrypt your message unless you want LE kicking down your door and putting a boot to your throat. How is this done? Easy!</p>
<ol>
<li>Obtain the recipients public key, which can hopefully be found on their profile</li>
<li>Copy everything, paste into a text editor, save it somewhere</li>
<li>Up at the top, click &#8216;Keys&#8217;, then &#8216;Import key&#8230;&#8217; <a href="/imgs/2015/02/reYpsUv12.png"><img class="aligncenter size-full wp-image-9110" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/reYpsUv12.png" alt="reYpsUv[1]" width="682" height="628" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/reYpsUv12.png 682w, https://www.deepdotweb.com/wp-content/uploads/2015/02/reYpsUv12-300x276.png 300w" sizes="(max-width: 682px) 100vw, 682px" /></a></li>
<li>Select the key, then click &#8216;Open&#8217;. You&#8217;ll see this window <a href="/imgs/2015/02/QKWYuU51.png"><img class="aligncenter size-full wp-image-9111" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/QKWYuU51.png" alt="QKWYuU5[1]" width="224" height="209" /></a></li>
<li>We&#8217;re done! <a href="/imgs/2015/02/yFoD0X41.png"><img class="aligncenter size-full wp-image-9112" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/yFoD0X41.png" alt="yFoD0X4[1]" width="681" height="627" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/yFoD0X41.png 681w, https://www.deepdotweb.com/wp-content/uploads/2015/02/yFoD0X41-300x276.png 300w" sizes="(max-width: 681px) 100vw, 681px" /></a></li>
</ol>
<p>I used some random key found on DDG. Thanks Alan!</p>
<h3>Part 6 – Importing a private key</h3>
<p>You finally realized that Microsoft/Apple is spying on you, and want to switch to an operating system that respects your right to privacy. How do you bring your key over?</p>
<ol>
<li>Up at the top, select &#8216;Keys&#8217;, then &#8216;Import Keys&#8230;&#8217; <a href="/imgs/2015/02/DT815bw1.png"><img class="aligncenter size-full wp-image-9114" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/DT815bw1.png" alt="DT815bw[1]" width="682" height="628" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/DT815bw1.png 682w, https://www.deepdotweb.com/wp-content/uploads/2015/02/DT815bw1-300x276.png 300w" sizes="(max-width: 682px) 100vw, 682px" /></a></li>
<li>Select your backup, it should have a file extension of .asc</li>
<li>This window will appear <a href="/imgs/2015/02/q96G5m81.png"><img class="aligncenter size-full wp-image-9115" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/q96G5m81.png" alt="q96G5m8[1]" width="224" height="209" /></a></li>
<li>Your key is now imported</li>
</ol>
<p>I could do this blindfolded!</p>
<h3>Part 7 – Encrypting a message</h3>
<p>GPA makes this easy as pie. Seriously, if you still can&#8217;t do it after following the below steps you shouldn&#8217;t be here.</p>
<ol>
<li>Click &#8216;Windows&#8217; at the top, then &#8216;Clipboard&#8217; <a href="/imgs/2015/02/Rxffusl1.png"><img class="aligncenter size-full wp-image-9116" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/Rxffusl1.png" alt="Rxffusl[1]" width="681" height="627" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/Rxffusl1.png 681w, https://www.deepdotweb.com/wp-content/uploads/2015/02/Rxffusl1-300x276.png 300w" sizes="(max-width: 681px) 100vw, 681px" /></a></li>
<li>This beautiful window will appear <a href="/imgs/2015/02/BLjxPd01.png"><img class="aligncenter size-full wp-image-9117" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/BLjxPd01.png" alt="BLjxPd0[1]" width="642" height="508" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/BLjxPd01.png 642w, https://www.deepdotweb.com/wp-content/uploads/2015/02/BLjxPd01-300x237.png 300w" sizes="(max-width: 642px) 100vw, 642px" /></a></li>
<li>Type in your message <a href="/imgs/2015/02/56KECk81.png"><img class="aligncenter size-full wp-image-9118" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/56KECk81.png" alt="56KECk8[1]" width="642" height="508" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/56KECk81.png 642w, https://www.deepdotweb.com/wp-content/uploads/2015/02/56KECk81-300x237.png 300w" sizes="(max-width: 642px) 100vw, 642px" /></a></li>
<li>Click the envelope with the blue key</li>
<li>Select the recipient of the message, sign it with your key if you want, then click &#8216;Ok&#8217; <a href="/imgs/2015/02/VGhlx8M1.png"><img class="aligncenter size-full wp-image-9119" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/VGhlx8M1.png" alt="VGhlx8M[1]" width="416" height="561" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/VGhlx8M1.png 416w, https://www.deepdotweb.com/wp-content/uploads/2015/02/VGhlx8M1-222x300.png 222w" sizes="(max-width: 416px) 100vw, 416px" /></a></li>
<li>Your encrypted message will now appear in the buffer. Copy everything and send this to the recipient <a href="/imgs/2015/02/URp5e5a1.png"><img class="aligncenter size-full wp-image-9120" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/URp5e5a1.png" alt="URp5e5a[1]" width="643" height="507" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/URp5e5a1.png 643w, https://www.deepdotweb.com/wp-content/uploads/2015/02/URp5e5a1-300x237.png 300w" sizes="(max-width: 643px) 100vw, 643px" /></a></li>
</ol>
<h3>Part 8 – Decrypting a message</h3>
<p>You sent your message, and the vendor responded! Now what? You&#8217;ll want to decrypt the message with your public key.</p>
<ol>
<li>Copy everything the vendor sent you, paste it into the buffer <a href="/imgs/2015/02/SMpYD1U1.png"><img class="aligncenter size-full wp-image-9121" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/SMpYD1U1.png" alt="SMpYD1U[1]" width="642" height="506" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/SMpYD1U1.png 642w, https://www.deepdotweb.com/wp-content/uploads/2015/02/SMpYD1U1-300x236.png 300w" sizes="(max-width: 642px) 100vw, 642px" /></a></li>
<li>Click the envelope at the top with the yellow key</li>
<li>Enter your passphrase <a href="/imgs/2015/02/Iki22bD1.png"><img class="aligncenter size-full wp-image-9122" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/Iki22bD1.png" alt="Iki22bD[1]" width="398" height="236" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/Iki22bD1.png 398w, https://www.deepdotweb.com/wp-content/uploads/2015/02/Iki22bD1-300x178.png 300w" sizes="(max-width: 398px) 100vw, 398px" /></a></li>
<li>Read your message <a href="/imgs/2015/02/UyOiGI11.png"><img class="aligncenter size-full wp-image-9123" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/UyOiGI11.png" alt="UyOiGI1[1]" width="641" height="506" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/UyOiGI11.png 641w, https://www.deepdotweb.com/wp-content/uploads/2015/02/UyOiGI11-300x237.png 300w" sizes="(max-width: 641px) 100vw, 641px" /></a></li>
</ol>
<h3>Part 9 – Conclusion</h3>
<p>There we have it, an easy to follow PGP guide for Linux with pictures! PGP can be overwhelming at first, but with persistence and the willingness to learn anyone can do it. Hopefully this guide will keep you guys safe on the DNM! I&#8217;ll have an OS X guide coming soon, and possibly a Windows guide following that. Any and all constructive feedback is appreciated, as well as suggestions for other guides!</p>
</div>
</div>
</div>
<span style="display:none"><a href="https://www.deepdotweb.com/tag/basic/" rel="tag">basic</a> <a href="https://www.deepdotweb.com/tag/guide/" rel="tag">guide</a> <a href="https://www.deepdotweb.com/tag/linux/" rel="tag">linux</a> <a href="https://www.deepdotweb.com/tag/pgp/" rel="tag">pgp</a></span> <span style="display:none" class="updated">2015-02-17</span>
<div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name">