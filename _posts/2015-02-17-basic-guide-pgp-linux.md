---
title: "Basic Guide to PGP On Linux"
---

Posted by: DeepDotWeb 

<span>February 17, 2015</span>


<div class="usertext-body may-blank-within md-container">
<div class="md">
<p><em>Full credit goes to <a href="http://www.reddit.com/user/MLP_is_my_OPSEC">MLP_is_my_OPSEC</a> for writing this tutorial &#8211; Thanks for publishing  and giving us your permission to post it!</em></p>
<h3>Part 0 &#8211; Introduction</h3>
<p>I promised it, and here it is! The PGP guide for Linux! Great timing too for Moronic Monday. For this guide we&#8217;ll be using GnuPG with Gnu Privacy Assistant as a graphical front-end. We will be using CLI to install these two pieces of software, and creating the keypair. The example OS in question is Linux Mint, so the commands for install may differ from your current OS. Don&#8217;t fret though! That&#8217;s the only part that may not be relevant to your OS, the rest of the guide will be the same across distros.</p>
<p style="text-align: center;"><a href="/vpn-comparison-chart/">&gt;&gt;&gt;Add A Layer Of Encryption: Click For The Best VPN Services&lt;&lt;&lt;</a></p>
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

<img src="/imgs/2015/02/TVjAVPp1.png">

<h3>Part 2 – Generating your keypair</h3>
<p>Part 1 was easy, eh? Don&#8217;t worry things don&#8217;t get much harder. The next step is to create your keypair. We&#8217;ll be using 4096 bit RSA to keep things extra secure!</p>
<ol>
<li>In your Terminal, type without quotes &#8216;gpg &#8211;gen-key&#8217;, then hit &#8216;enter&#8217;</li>
<li>It will ask you what kind of key you want. For our usecase, we want option &#8216;1&#8217; :

<img src="/imgs/2015/02/TsvxqSl1.png">

<li>Next step is key length. The longer the length, the more secure it is. We&#8217;ll go with 4096 bits: 

<img src="/imgs/2015/02/33FN8mb1.png">

<li>It will now ask if you want your key to expire after a certain amount of time. This is up to personal preference, but we&#8217;ll choose &#8216;key does not expire&#8217;, so just hit &#8216;enter&#8217; 

<img src="/imgs/2015/02/EmYMtKE1.png">

<li>Confirm that yes, the key will not expire. Type &#8216;y&#8217;, then hit &#8216;enter&#8217; 

<img src="/imgs/2015/02/eGqruqQ1.png">

<li>The next step will be to enter an ID to make it easier for people to identify your key. If you&#8217;ve made it this far, you should know what to do 

<img src="/imgs/2015/02/LgkPV7n1.png">

<li>It will ask if this information is correct. If it is, type &#8216;O&#8217; and hit &#8216;enter&#8217; 

<img src="/imgs/2015/02/xxdJ8g41.png">

<a href="https://xkcd.com/936/">Here is a great XKCD comic on creating secure passphrases</a></li>
<li>Enter a passphrase to protect your secret key. 

<img src="/imgs/2015/02/ZKXIiPW1.png">

<li>Here comes the fun part. It&#8217;s going to generate your key, and will ask you to do some random stuff to create entropy. I like to have a Youtube video going with a torrent running in the background, while randomly mashing keys in a text editor. See the picture for an example of what will be output in the terminal 

<img src="/imgs/2015/02/bshPVDM1.png">

<li>annnddddd we&#8217;re done! 

<img src="/imgs/2015/02/QFynRxp1.png">

</ol>
<h3>Part 3 – Obtaining your public key</h3>
<p>So we&#8217;ve installed the software, generated our super secure keypair. Now what? Well if you want to actually use it we need to obtain our public key. Everything from here will be done through the graphical front-end.</p>
<ol>
<li>Open Terminal, type &#8216;sudo gpa&#8217;, hit &#8216;enter&#8217;. Type in your password <sup>yeahIknowwhatyou&#8217;rethinking</sup></li>
<li>You&#8217;ll be greeted by this beautiful window 

<img src="/imgs/2015/02/eNSqF341.png">

<li>Click on the keypair you just created, click &#8216;Keys&#8217; up at the top, then &#8216;Export keys&#8230;&#8217; 

<img src="/imgs/2015/02/reYpsUv1.png">

<li>Select where you want it saved, enter a filename, and click &#8216;Save&#8217;</li>
<li>Browse to the location in your file manager, open up that file with a text editor</li>
</ol>
<p>There&#8217;s your public key! Don&#8217;t forget to put this on your market profile so people can contact you easier.</p>
<h3>Part 4 – Obtaining your private key</h3>
<p>If you ever want to switch operating systems or PGP programs, you&#8217;ll need to do this. It&#8217;s just as easy as obtaining your public key. Make sure you keep this file safe!</p>
<ol>
<li>Hopefully you still have GPA open. If not, follow step #1 of Part 3</li>
<li>Click on your keypair, click &#8216;Keys&#8217; up at the top then &#8216;Backup&#8217; 

<img src="/imgs/2015/02/reYpsUv11.png">

<li>Select where you want it saved, keep the filename it gives you, and click &#8216;Save&#8217;</li>
<li>A window will pop up, you can back up to a floppy if you&#8217;re stuck in the &#8217;80s 

<img src="/imgs/2015/02/ucMIWk61.png">

</ol>
<p>Remember to keep this file safe! Don&#8217;t forget your passphrase!</p>
<h3>Part 5 – Importing a public key</h3>
<p>So you want to buy some dank marijuanas, you&#8217;ll need to encrypt your message unless you want LE kicking down your door and putting a boot to your throat. How is this done? Easy!</p>
<ol>
<li>Obtain the recipients public key, which can hopefully be found on their profile</li>
<li>Copy everything, paste into a text editor, save it somewhere</li>
<li>Up at the top, click &#8216;Keys&#8217;, then &#8216;Import key&#8230;&#8217; 

<img src="/imgs/2015/02/reYpsUv12.png">

<li>Select the key, then click &#8216;Open&#8217;. You&#8217;ll see this window 

<img src="/imgs/2015/02/QKWYuU51.png">

<li>We&#8217;re done! 

<img src="/imgs/2015/02/yFoD0X41.png">

</ol>
<p>I used some random key found on DDG. Thanks Alan!</p>
<h3>Part 6 – Importing a private key</h3>
<p>You finally realized that Microsoft/Apple is spying on you, and want to switch to an operating system that respects your right to privacy. How do you bring your key over?</p>
<ol>
<li>Up at the top, select &#8216;Keys&#8217;, then &#8216;Import Keys&#8230;&#8217; 

<img src="/imgs/2015/02/DT815bw1.png">

<li>Select your backup, it should have a file extension of .asc</li>
<li>This window will appear 

<img src="/imgs/2015/02/q96G5m81.png">

<li>Your key is now imported</li>
</ol>
<p>I could do this blindfolded!</p>
<h3>Part 7 – Encrypting a message</h3>
<p>GPA makes this easy as pie. Seriously, if you still can&#8217;t do it after following the below steps you shouldn&#8217;t be here.</p>
<ol>
<li>Click &#8216;Windows&#8217; at the top, then &#8216;Clipboard&#8217; 

<img src="/imgs/2015/02/Rxffusl1.png">

<li>This beautiful window will appear 

<img src="/imgs/2015/02/BLjxPd01.png">

<li>Type in your message 

<img src="/imgs/2015/02/56KECk81.png">

<li>Click the envelope with the blue key</li>
<li>Select the recipient of the message, sign it with your key if you want, then click &#8216;Ok&#8217; 

<img src="/imgs/2015/02/VGhlx8M1.png">

<li>Your encrypted message will now appear in the buffer. Copy everything and send this to the recipient 

<img src="/imgs/2015/02/URp5e5a1.png">

</ol>
<h3>Part 8 – Decrypting a message</h3>
<p>You sent your message, and the vendor responded! Now what? You&#8217;ll want to decrypt the message with your public key.</p>
<ol>
<li>Copy everything the vendor sent you, paste it into the buffer 

<img src="/imgs/2015/02/SMpYD1U1.png">

<li>Click the envelope at the top with the yellow key</li>
<li>Enter your passphrase 

<img src="/imgs/2015/02/Iki22bD1.png">

<li>Read your message 

<img src="/imgs/2015/02/UyOiGI11.png">

</ol>
<h3>Part 9 – Conclusion</h3>
<p>There we have it, an easy to follow PGP guide for Linux with pictures! PGP can be overwhelming at first, but with persistence and the willingness to learn anyone can do it. Hopefully this guide will keep you guys safe on the DNM! I&#8217;ll have an OS X guide coming soon, and possibly a Windows guide following that. Any and all constructive feedback is appreciated, as well as suggestions for other guides!</p>
</div>

Updated: 2015-02-17