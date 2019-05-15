---
title: "AN INTRODUCTION TO AN EXPERT ON OPSEC, PLUS MD5 &#038; SHA-1 CHECKSUMs"
sidebar:
  - title: "Jolly Rogers Security Guide"
    nav: "jolly"
  - title: "Security Tutorials"
    nav: "security"
  - title: "Blog Archive"
    nav: "blognav"

---



<p>ers to people keeping themselves anonymous online. He goes by the online handle, &#8220;The Grugq&#8221;, and Grugq has his own blog which can be found at the following webpage.</p>
<p><strong>http://grugq.github.io/</strong></p>
<p>It should be noted that Grugq was at one time on the payroll of the US government for finding and selling zero day exploits. If you remember the previous post about how the US federal government is the singlemost purchaser of malware in the world, well Grugq was one of those who sold malware to the government. Unfortunately for him, when he went public about it, they no longer wanted to buy malware from him because they like to maintain their own anonymity when purchasing these exploits. And here is a short biography from an online website.</p>
<div>
<div>Quote</div>
</div>
<blockquote><p>Biography:</p>
<p>The Grugq is an Information Security Professional who has has worked with digital forensic analysis, binary reverse engineering, rootkits, Voice over IP, telecommunications and financial security. He has reported to be an exploit broker for 15% of the sale. Last but not least, he has also spoken at various security conferences.</p>
<p><strong>Facts</strong></p>
<p>He developed &#8220;userland exec&#8221;</p>
<p>He is the author of Hash (hacker shell), a tool to enable people to evade detection while penetrating a system.</p>
<p>He has released a voip attack software.</p>
<p>Claims to have made mad loot on being an exploit broker (middleman).</p>
<p>https://www.soldierx.com/hdb/Grugq</p></blockquote>
<p>Why are we talking about the Grugq? Who cares? Well, he has some of the best information on keeping yourself anonymous and maintaining privacy online and he is somebody who you should all familiarize yourselves with. He writes blog posts, and he has done video presentations at security and hacker conferences, with his most famous presentation, at least in the world of Silk Road being the one he did on OpSec. Since I know it is hard for Tails users to watch videos on YouTube, I decided to download it from YouTube and upload it to AnonFiles.com so you all can watch it. The presentation is about 1 hour long, and an essential to everyone who wishes to maintain their anonymity online. Remember, you only have to screw up once.</p>
<p><strong>https://anonfiles.com/file/b6de41da8d1fca2fabf725f79d2a90df</strong></p>
<p><strong>SHA1 Sum: 1a9e6c67a527b42a05111e1b18c7a037744bb51e</strong><br/>
<strong>MD5 Sum: b6de41da8d1fca2fabf725f79d2a90df</strong></p>
<p>Once you have downloaded the file, I want you to check something called the checksum of the file. The checksum is where the contents of the entire file get plugged into a mathematical algorithm and output a specific string. You can see the two strings above. This is something you should all get into the habit of doing when possible is verifying the checksum of your files. If you remember when we talked about signature files and PGP, this is another method of verifying your downloads but not as good as the signature files. It should however, whenever provided be performed to verify your downloads when the signature file + PGP combination is not available.</p>
<p>Once you have downloaded the file in Tails, the first thing you should do, is move the file you downloaded to your tmp folder. In order to do this, look up at the top and click <strong>Places -&gt; Computer -&gt; File System -&gt; tmp</strong>. This is where you move the file your downloaded to, and to keep things easier, rename the file <strong>grugq.zip</strong> and you will see why you want to do that in a second.</p>
<p>Next we are going to open a terminal window (like a DOS prompt) by clicking the black rectangle icon in the upper left center area of Tails. Once you have opened your terminal window, we are going to perform some Linux commands.</p>
<p><strong>cd /tmp</strong> &#8211; This will change the current directory you are operating within the terminal to your tmp folder and allow you to more easily access the files in that folder.</p>
<p><strong>sha1sum grugq.zip</strong> &#8211; This will perform a SHA1 checksum on the file you just downloaded, and you can see why you wanted to rename the file. It should give you the same output as the SHA1 sum listed above.</p>
<p><strong>md5sum grugq.zip</strong> &#8211; This will perform an MD5 checksum on the file you just downloaded, and is another way of checking the file. SHA1 is better because it is harder produce the same output twice with different file contents using SHA1 versus MD5, but nonetheless, use both whenever possible and always check your downloaded files.</p>
<p>Ok, assuming your downloaded video passed the checksum test, you can be assured that the video file that I uploaded has not been tampered with, or had any malicious code injected into it. When even a single character is changed in the source code of a given file, the checksum output will be completely different. Most people think it may be off by a a few characters, but the difference is always quite large and is why performing checksums is an important way of verifying your downloads.</p>
<p>Since you now have a 1 hour video presentation that you all need to watch and rewatch (You can do this in Tails), I will end this post and continue with my next post from the assumption that you can completed watching this highly recommended and endorsed (by SR administrators and moderators) video on OpSec. We will start looking more into the recommendations from the Grugq. He will be an invaluable resource of information for us, and I will mainly be translating some of his posts into a more understandable format for those of you who are less technically capable and also keeping them on the Silk Road forum hidden services.</p>
<p>&#8212;&#8211;BEGIN PGP SIGNATURE&#8212;&#8211;</p>
<p>iQIcBAEBCgAGBQJS7wteAAoJEPuh6tSg81nyhyYP/0nFaWRq0GPe6/5XeMUj3yiZ<br/>
2fBaJ+7SXOMxnNXPZw9XAN5Hkpp9wPQmk8W27otuIk2N+iom8H0tJcGZi7hiMd45<br/>
Dv0NOrt/gS3bst/G37I+tPwdnWxb1pVNCS+3XnuLOo9IA7VdykU8tz6R+68kPB25<br/>
9lDguaUYVeGp2AJMezQ01LL60xQvv25TFLgiPrYD611bscVadckhSV5upXlbMW9+<br/>
WVzJG1mgY9gmUYQV6D5ErPGIvxm8cC+IVlzwgGHQPd3kq2QlmQF3XJrXqWGPXd8d<br/>
ewkD6VnrU8yO6tVMCG57K1xO9a9zPYp6yN1IOe69IsRkK7g266D+cz6Idwt97/Vr<br/>
5jgu1Ook8dfFGA3Sxg+qpoARt5diWKchvmqbxRrnFdOtCAawH1+DgNcVdepi7agk<br/>
zhIES1drHdIM1uQ9Wg3vegCLrU3HDpRwwyWoSZxH4kxruU7aByOH5ZdAZw9JV6Lk<br/>
b5JzVjrvrhayXwiHPQnnjM50RT9jPH44PhNZCN4G7Ln2Rkb7qa/kS5sA4W2dRwXf<br/>
SjtYXf+18pCp/7NL09LD+LsabZHEAa/MilWxjsAnLLIrJsnw3YbSUola/ebmnIq8<br/>
oUW20yP0fDOHdeSGVq1uLNZIadZHZtmZIGqBigPU3XAKLxYajssglAgcPxD8E4vc<br/>
rkKb3PIyz1k1/JXulymR<br/>
=zJvP<br/>
&#8212;&#8211;END PGP SIGNATURE&#8212;&#8211;</p>

Updated: 2014-02-13

