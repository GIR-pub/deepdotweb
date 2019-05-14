---
title: "PGP Tutorial For Windows (Kleopatra &#8211; Gpg4Win)"
---


Posted by: DeepDotWeb 

<span>February 21, 2015</span>


<div class="usertext-body may-blank-within md-container">
<div class="md">
<p><em>Full credit goes to <a href="http://www.reddit.com/user/MLP_is_my_OPSEC">MLP_is_my_OPSEC</a> for writing this tutorial – Thanks for publishing and giving your permission to repost!<br />
    Tutorial for </em>Gpg4Win using GPA can <a href="http://www.deepdotweb.com/2013/11/11/pgp-tutorial-for-newbs-gpg4win/" target="_blank">be found here</a>.</p>
<h3>Part 0 – Introduction</h3>
<p>Here&#8217;s the final guide in my PGP basics series, this time focusing on Windows. The OS in question will be Windows 7, but it should work for Win8 and Win8.1 as well. Obviously it&#8217;s not recommended to be using Windows to access the DNM, but I wont go into the reasons here. The tool we&#8217;ll be using is GPG4Win.</p>
<p style="text-align: center;"><a href="/vpn-comparison-chart/">&gt;&gt;&gt;Add A Layer Of Encryption: Click For The Best VPN Services&lt;&lt;&lt;</a></p>
<h3>Part 1 – Installing the software</h3>
<p>Just like I said above, we&#8217;ll be using GPG4Win. If you&#8217;re curious, you can view the source code for it <a href="https://git.gnupg.org/cgi-bin/gitweb.cgi?p=gpg4win.git;a=summary">here</a>.</p>
<ol>
<li>Head on over to <a href="https://gpg4win.org/download.html">https://gpg4win.org/download.html</a>. We want the full version, so click &#8216;Gpg4win 2.2.3&#8217; <a href="/imgs/2015/02/iXqHJld1.png"><img class="aligncenter size-full wp-image-9188" src="/imgs/2015/02/iXqHJld1.png" alt="iXqHJld[1]" width="600" height="202" srcset="/imgs/2015/02/iXqHJld1.png 600w, /imgs/2015/02/iXqHJld1-300x101.png 300w" sizes="(max-width: 600px) 100vw, 600px" /></a></li>
<li>Save it, open it when it&#8217;s done downloading. If you have UAC enabled, click &#8216;Yes&#8217; on the window that appears <a href="/imgs/2015/02/NFVNUCS1.png"><img class="aligncenter size-full wp-image-9189" src="/imgs/2015/02/NFVNUCS1.png" alt="NFVNUCS[1]" width="464" height="262" srcset="/imgs/2015/02/NFVNUCS1.png 464w, /imgs/2015/02/NFVNUCS1-300x169.png 300w" sizes="(max-width: 464px) 100vw, 464px" /></a></li>
<li>Choose your language, click &#8216;Ok&#8217; <a href="/imgs/2015/02/SUJ3aT21.png"><img class="aligncenter size-full wp-image-9190" src="/imgs/2015/02/SUJ3aT21.png" alt="SUJ3aT2[1]" width="294" height="156" /></a></li>
<li>Click &#8216;Next&#8217;, then &#8216;Next&#8217; again. You&#8217;ll now be at a screen asking what components you want to install. We&#8217;ll be selecting &#8216;Kleopatra&#8217;, &#8216;GpgEX&#8217;, and &#8216;Gpg4win Compendium&#8217;. Then click &#8216;Next&#8217; <a href="/imgs/2015/02/oNLB4Kk1.png"><img class="aligncenter size-full wp-image-9191" src="/imgs/2015/02/oNLB4Kk1.png" alt="oNLB4Kk[1]" width="503" height="390" srcset="/imgs/2015/02/oNLB4Kk1.png 503w, /imgs/2015/02/oNLB4Kk1-300x233.png 300w" sizes="(max-width: 503px) 100vw, 503px" /></a></li>
<li>It will ask where to install, just keep the default and click &#8216;Next&#8217;</li>
<li>Now it&#8217;ll ask where you want to install shortcuts. Select whichever you want, click &#8216;Next&#8217;</li>
<li>You can choose which Start Menu folder you want it installed in, just click &#8216;Next&#8217;</li>
<li>It will now install, when done you should see this. Click &#8216;Next&#8217;, then &#8216;Finish&#8217; <a href="/imgs/2015/02/RYUfaj41.png"><img class="aligncenter size-full wp-image-9192" src="/imgs/2015/02/RYUfaj41.png" alt="RYUfaj4[1]" width="502" height="390" srcset="/imgs/2015/02/RYUfaj41.png 502w, /imgs/2015/02/RYUfaj41-300x233.png 300w" sizes="(max-width: 502px) 100vw, 502px" /></a></li>
</ol>
<p>Now you have the tools you need to get started with PGP</p>
<h3>Part 2 – Generating your keypair</h3>
<p>The next step is to generate your keypair so you can encrypt/decrypt messages. Like always, we&#8217;ll be going with 4096 bit RSA.</p>
<ol>
<li>Open up Kleopatra, you should be greeted with this beautiful screen <a href="/imgs/2015/02/5i6tnlr1.png"><img class="aligncenter size-full wp-image-9193" src="/imgs/2015/02/5i6tnlr1.png" alt="5i6tnlr[1]" width="548" height="314" srcset="/imgs/2015/02/5i6tnlr1.png 548w, /imgs/2015/02/5i6tnlr1-300x172.png 300w" sizes="(max-width: 548px) 100vw, 548px" /></a></li>
<li>Go to &#8216;File&#8217;, then &#8216;New Certificate&#8230;&#8217; <a href="/imgs/2015/02/u069Ntb1.png"><img class="aligncenter size-full wp-image-9194" src="/imgs/2015/02/u069Ntb1.png" alt="u069Ntb[1]" width="550" height="382" srcset="/imgs/2015/02/u069Ntb1.png 550w, /imgs/2015/02/u069Ntb1-300x208.png 300w" sizes="(max-width: 550px) 100vw, 550px" /></a></li>
<li>The Certificate Creation Wizard should pop up, click on &#8216;Create a personal OpenPGP key pair&#8217; <a href="/imgs/2015/02/oVaws0J1.png"><img class="aligncenter size-full wp-image-9195" src="/imgs/2015/02/oVaws0J1.png" alt="oVaws0J[1]" width="500" height="388" srcset="/imgs/2015/02/oVaws0J1.png 500w, /imgs/2015/02/oVaws0J1-300x233.png 300w" sizes="(max-width: 500px) 100vw, 500px" /></a></li>
<li>Now you&#8217;ll enter your details. Use your marketplace username as &#8216;Name&#8217;, and fill out the rest with whatever you want. You don&#8217;t need to use a real email. Check the picture for an example on how it should look <a href="/imgs/2015/02/xJFjFGx1.png"><img class="aligncenter size-full wp-image-9196" src="/imgs/2015/02/xJFjFGx1.png" alt="xJFjFGx[1]" width="500" height="388" srcset="/imgs/2015/02/xJFjFGx1.png 500w, /imgs/2015/02/xJFjFGx1-300x233.png 300w" sizes="(max-width: 500px) 100vw, 500px" /></a></li>
<li><strong>Do not click &#8216;Next&#8217; yet</strong>, we need to fill out some more details. Click &#8216;Advanced Settings&#8230;&#8217;, and another window should appear. Under &#8216;Key Material&#8217;, make sure &#8216;RSA&#8217; is checked. In the drop down menu beside it, and select &#8216;4,096 bits&#8217;. Check the picture to confirm you have everything set correctly, then click &#8216;Ok&#8217; <a href="/imgs/2015/02/dcOihQG1.png"><img class="aligncenter size-full wp-image-9197" src="/imgs/2015/02/dcOihQG1.png" alt="dcOihQG[1]" width="391" height="465" srcset="/imgs/2015/02/dcOihQG1.png 391w, /imgs/2015/02/dcOihQG1-252x300.png 252w" sizes="(max-width: 391px) 100vw, 391px" /></a></li>
<li>Confirm you filled out all of your info correctly, then click &#8216;Create Key&#8217; <a href="/imgs/2015/02/hUIQgMb1.png"><img class="aligncenter size-full wp-image-9198" src="/imgs/2015/02/hUIQgMb1.png" alt="hUIQgMb[1]" width="500" height="386" srcset="/imgs/2015/02/hUIQgMb1.png 500w, /imgs/2015/02/hUIQgMb1-300x232.png 300w" sizes="(max-width: 500px) 100vw, 500px" /></a></li>
<li>Another window will pop up asking to enter a passphrase. Do so, then click &#8216;Ok&#8217; <a href="/imgs/2015/02/kIPFAQF1.png"><img class="aligncenter size-full wp-image-9199" src="/imgs/2015/02/kIPFAQF1.png" alt="kIPFAQF[1]" width="286" height="181" /></a></li>
<li>It will now generate your key. It will need you to do random things to create entropy. Mash keys, wiggle the mouse, watch porn, download torrents, whatever <a href="/imgs/2015/02/p8vJdbN1.png"><img class="aligncenter size-full wp-image-9200" src="/imgs/2015/02/p8vJdbN1.png" alt="p8vJdbN[1]" width="499" height="387" srcset="/imgs/2015/02/p8vJdbN1.png 499w, /imgs/2015/02/p8vJdbN1-300x233.png 300w" sizes="(max-width: 499px) 100vw, 499px" /></a></li>
<li>Your key is now created. Go ahead and click &#8216;Finish&#8217; <a href="/imgs/2015/02/1SRNdt61.png"><img class="aligncenter size-full wp-image-9201" src="/imgs/2015/02/1SRNdt61.png" alt="1SRNdt6[1]" width="499" height="455" srcset="/imgs/2015/02/1SRNdt61.png 499w, /imgs/2015/02/1SRNdt61-300x274.png 300w" sizes="(max-width: 499px) 100vw, 499px" /></a></li>
</ol>
<h3>Part 3 – Obtaining your public key</h3>
<p>Now we need to get your public key, without it vendors wont be able to send you secure messages.</p>
<ol>
<li>Right click on your key, then click &#8216;Export Certificates&#8230;&#8217; <a href="/imgs/2015/02/h86y7Le1.png"><img class="aligncenter size-full wp-image-9202" src="/imgs/2015/02/h86y7Le1.png" alt="h86y7Le[1]" width="653" height="471" srcset="/imgs/2015/02/h86y7Le1.png 653w, /imgs/2015/02/h86y7Le1-300x216.png 300w" sizes="(max-width: 653px) 100vw, 653px" /></a></li>
<li>Browse where you want to save, give it a name, then click &#8216;Save&#8217;</li>
<li>Open your favourite text editor, browse to where the file is saved. You may have to select &#8216;All files&#8217; from the dropdown menu. Click the file you saved, then open <a href="/imgs/2015/02/XIFqJy81.png"><img class="aligncenter size-full wp-image-9203" src="/imgs/2015/02/XIFqJy81.png" alt="XIFqJy8[1]" width="625" height="479" srcset="/imgs/2015/02/XIFqJy81.png 625w, /imgs/2015/02/XIFqJy81-300x230.png 300w" sizes="(max-width: 625px) 100vw, 625px" /></a></li>
<li>There&#8217;s your public key <a href="/imgs/2015/02/gJK0c9S1.png"><img class="aligncenter size-full wp-image-9204" src="/imgs/2015/02/gJK0c9S1.png" alt="gJK0c9S[1]" width="596" height="499" srcset="/imgs/2015/02/gJK0c9S1.png 596w, /imgs/2015/02/gJK0c9S1-300x251.png 300w" sizes="(max-width: 596px) 100vw, 596px" /></a></li>
</ol>
<p>Remember to add your public key to your market profile so people can message you easier!</p>
<h3>Part 4 – Obtaining your private key</h3>
<p>Just as easy as obtaining your public key</p>
<ol>
<li>Right click on your key, select &#8216;Export Secret Keys&#8230;&#8217; <a href="/imgs/2015/02/KBWbUBC1.png"><img class="aligncenter size-full wp-image-9205" src="/imgs/2015/02/KBWbUBC1.png" alt="KBWbUBC[1]" width="654" height="474" srcset="/imgs/2015/02/KBWbUBC1.png 654w, /imgs/2015/02/KBWbUBC1-300x217.png 300w" sizes="(max-width: 654px) 100vw, 654px" /></a></li>
<li>Select where you want it saved, give it a name, check &#8216;ASCII armor&#8217;, and click &#8216;Ok&#8217; <a href="/imgs/2015/02/d4MPQKB1.png"><img class="aligncenter size-full wp-image-9206" src="/imgs/2015/02/d4MPQKB1.png" alt="d4MPQKB[1]" width="387" height="232" srcset="/imgs/2015/02/d4MPQKB1.png 387w, /imgs/2015/02/d4MPQKB1-300x180.png 300w" sizes="(max-width: 387px) 100vw, 387px" /></a></li>
<li>You now have your private key <a href="/imgs/2015/02/M4osyVS1.png"><img class="aligncenter size-full wp-image-9207" src="/imgs/2015/02/M4osyVS1.png" alt="M4osyVS[1]" width="261" height="136" /></a></li>
</ol>
<p>Remember to keep this in a safe place, and never share it!</p>
<h3>Part 5 – Importing a public key</h3>
<p>It&#8217;s impossible to send a vendor an encrypted message without their public key.</p>
<ol>
<li>Find a public key you want to import</li>
<li>Copy everything from &#8216;&#8212;&#8211;BEGIN PGP PUBLIC KEY BLOCK&#8212;&#8211;&#8216; to &#8216;&#8212;&#8211;END PGP PUBLIC KEY BLOCK&#8212;&#8216;, see the picture for an example <a href="/imgs/2015/02/69UnFPR1.png"><img class="aligncenter size-full wp-image-9208" src="/imgs/2015/02/69UnFPR1.png" alt="69UnFPR[1]" width="520" height="266" srcset="/imgs/2015/02/69UnFPR1.png 520w, /imgs/2015/02/69UnFPR1-300x153.png 300w" sizes="(max-width: 520px) 100vw, 520px" /></a></li>
<li>In your task bar, right click on the Kleopatra icon, go to &#8216;Clipboard&#8217;, then click &#8216;Certificate Import&#8217; <a href="/imgs/2015/02/UG15ss61.png"><img class="aligncenter size-full wp-image-9209" src="/imgs/2015/02/UG15ss61.png" alt="UG15ss6[1]" width="363" height="206" srcset="/imgs/2015/02/UG15ss61.png 363w, /imgs/2015/02/UG15ss61-300x170.png 300w" sizes="(max-width: 363px) 100vw, 363px" /></a></li>
<li>If it worked, you should see a window pop up, click &#8216;Ok&#8217; <a href="/imgs/2015/02/J9kQIQB1.png"><img class="aligncenter size-full wp-image-9210" src="/imgs/2015/02/J9kQIQB1.png" alt="J9kQIQB[1]" width="282" height="147" /></a></li>
<li>You should now see the imported key in Kleopatra under the &#8216;Other Certificates&#8217; tab <a href="/imgs/2015/02/2G438Pi1.png"><img class="aligncenter size-full wp-image-9211" src="/imgs/2015/02/2G438Pi1.png" alt="2G438Pi[1]" width="654" height="314" srcset="/imgs/2015/02/2G438Pi1.png 654w, /imgs/2015/02/2G438Pi1-300x144.png 300w" sizes="(max-width: 654px) 100vw, 654px" /></a></li>
</ol>
<p>Thanks again Alan!</p>
<h3>Part 6 – Importing your private key</h3>
<p>Simple stuff.</p>
<ol>
<li>Go to &#8216;File&#8217;, then click &#8216;Import Certificates&#8230;&#8217; <a href="/imgs/2015/02/hHDqxpO1.png"><img class="aligncenter size-full wp-image-9212" src="/imgs/2015/02/hHDqxpO1.png" alt="hHDqxpO[1]" width="655" height="384" srcset="/imgs/2015/02/hHDqxpO1.png 655w, /imgs/2015/02/hHDqxpO1-300x176.png 300w" sizes="(max-width: 655px) 100vw, 655px" /></a></li>
<li>Browse to where your private key is, select it, then click &#8216;Open&#8217; <a href="/imgs/2015/02/Qq8OmEn1.png"><img class="aligncenter size-full wp-image-9213" src="/imgs/2015/02/Qq8OmEn1.png" alt="Qq8OmEn[1]" width="624" height="480" srcset="/imgs/2015/02/Qq8OmEn1.png 624w, /imgs/2015/02/Qq8OmEn1-300x231.png 300w" sizes="(max-width: 624px) 100vw, 624px" /></a></li>
<li>It will import your private key, and pop up a window to confirm. Click &#8216;Ok&#8217; <a href="/imgs/2015/02/m6YsDUv1.png"><img class="aligncenter size-full wp-image-9214" src="/imgs/2015/02/m6YsDUv1.png" alt="m6YsDUv[1]" width="415" height="178" srcset="/imgs/2015/02/m6YsDUv1.png 415w, /imgs/2015/02/m6YsDUv1-300x129.png 300w" sizes="(max-width: 415px) 100vw, 415px" /></a></li>
<li>You should now see your key information under the &#8216;My Certificates&#8217; tab <a href="/imgs/2015/02/SyPzPmp1.png"><img class="aligncenter size-full wp-image-9215" src="/imgs/2015/02/SyPzPmp1.png" alt="SyPzPmp[1]" width="655" height="315" srcset="/imgs/2015/02/SyPzPmp1.png 655w, /imgs/2015/02/SyPzPmp1-300x144.png 300w" sizes="(max-width: 655px) 100vw, 655px" /></a></li>
</ol>
<h3>Part 7 – Encrypting a message</h3>
<p>Now that we&#8217;re ready to go, lets go ahead and send a message.</p>
<ol>
<li>Open up your text editor of choice</li>
<li>Type out your message, select it all, and copy it <a href="/imgs/2015/02/fpsVEX21.png"><img class="aligncenter size-full wp-image-9216" src="/imgs/2015/02/fpsVEX21.png" alt="fpsVEX2[1]" width="579" height="440" srcset="/imgs/2015/02/fpsVEX21.png 579w, /imgs/2015/02/fpsVEX21-300x228.png 300w" sizes="(max-width: 579px) 100vw, 579px" /></a></li>
<li>In your task bar, right click on the Kleopatra icon, go to &#8216;Clipboard&#8217;, then click &#8216;Encrypt&#8230;&#8217; <a href="/imgs/2015/02/jSeuc6p1.png"><img class="aligncenter size-full wp-image-9217" src="/imgs/2015/02/jSeuc6p1.png" alt="jSeuc6p[1]" width="331" height="188" srcset="/imgs/2015/02/jSeuc6p1.png 331w, /imgs/2015/02/jSeuc6p1-300x170.png 300w" sizes="(max-width: 331px) 100vw, 331px" /></a></li>
<li>This gorgeous window will open. Click &#8216;Add Recipient&#8230;&#8217; <a href="/imgs/2015/02/xmzkSvm1.png"><img class="aligncenter size-full wp-image-9218" src="/imgs/2015/02/xmzkSvm1.png" alt="xmzkSvm[1]" width="655" height="518" srcset="/imgs/2015/02/xmzkSvm1.png 655w, /imgs/2015/02/xmzkSvm1-300x237.png 300w" sizes="(max-width: 655px) 100vw, 655px" /></a></li>
<li>Another window will appear. Click the &#8216;Other Certificates&#8217; tab, then select who you want to send your message to, then click &#8216;Ok&#8217;. <a href="/imgs/2015/02/88SqUA21.png"><img class="aligncenter size-full wp-image-9219" src="/imgs/2015/02/88SqUA21.png" alt="88SqUA2[1]" width="447" height="300" srcset="/imgs/2015/02/88SqUA21.png 447w, /imgs/2015/02/88SqUA21-300x201.png 300w, /imgs/2015/02/88SqUA21-290x195.png 290w" sizes="(max-width: 447px) 100vw, 447px" /></a></li>
<li>You should be back at the previous window with the recipient listed. Click &#8216;Next&#8217; <a href="/imgs/2015/02/g4qk0H61.png"><img class="aligncenter size-full wp-image-9220" src="/imgs/2015/02/g4qk0H61.png" alt="g4qk0H6[1]" width="657" height="518" srcset="/imgs/2015/02/g4qk0H61.png 657w, /imgs/2015/02/g4qk0H61-300x237.png 300w" sizes="(max-width: 657px) 100vw, 657px" /></a></li>
<li>If all went well, you should see this window. Click &#8216;Ok&#8217; <a href="/imgs/2015/02/jnIS7Wo1.png"><img class="aligncenter size-full wp-image-9221" src="/imgs/2015/02/jnIS7Wo1.png" alt="jnIS7Wo[1]" width="656" height="519" srcset="/imgs/2015/02/jnIS7Wo1.png 656w, /imgs/2015/02/jnIS7Wo1-300x237.png 300w" sizes="(max-width: 656px) 100vw, 656px" /></a></li>
<li>Your encrypted message will be in your clipboard, all you need to do is paste it into the message box and send <a href="/imgs/2015/02/hrQ9tb01.png"><img class="aligncenter size-full wp-image-9222" src="/imgs/2015/02/hrQ9tb01.png" alt="hrQ9tb0[1]" width="519" height="266" srcset="/imgs/2015/02/hrQ9tb01.png 519w, /imgs/2015/02/hrQ9tb01-300x154.png 300w" sizes="(max-width: 519px) 100vw, 519px" /></a></li>
</ol>
<h3>Part 8 – Decrypting a message</h3>
<p>This is just as easy as encrypting.</p>
<ol>
<li>Copy everything that was sent <a href="/imgs/2015/02/aj50dmL1.png"><img class="aligncenter size-full wp-image-9223" src="/imgs/2015/02/aj50dmL1.png" alt="aj50dmL[1]" width="541" height="281" srcset="/imgs/2015/02/aj50dmL1.png 541w, /imgs/2015/02/aj50dmL1-300x156.png 300w" sizes="(max-width: 541px) 100vw, 541px" /></a></li>
<li>In your task bar, right click on the Kleopatra icon, go to &#8216;Clipboard&#8217;, then click &#8216;Decrypt/Verify&#8230;&#8217; <a href="/imgs/2015/02/T8lqyCo1.png"><img class="aligncenter size-full wp-image-9224" src="/imgs/2015/02/T8lqyCo1.png" alt="T8lqyCo[1]" width="347" height="195" srcset="/imgs/2015/02/T8lqyCo1.png 347w, /imgs/2015/02/T8lqyCo1-300x169.png 300w" sizes="(max-width: 347px) 100vw, 347px" /></a></li>
<li>A window will pop up asking for your passphrase, enter that then click &#8216;Ok&#8217; <a href="/imgs/2015/02/yj6ciCG1.png"><img class="aligncenter size-full wp-image-9225" src="/imgs/2015/02/yj6ciCG1.png" alt="yj6ciCG[1]" width="486" height="199" srcset="/imgs/2015/02/yj6ciCG1.png 486w, /imgs/2015/02/yj6ciCG1-300x123.png 300w" sizes="(max-width: 486px) 100vw, 486px" /></a></li>
<li>A window should pop up verifying it was decrypted, and copied to your clipboard. Click &#8216;Finish&#8217;</li>
<li>Open your text editor of choice, and paste your message <a href="/imgs/2015/02/ENJY7tp1.png"><img class="aligncenter size-full wp-image-9226" src="/imgs/2015/02/ENJY7tp1.png" alt="ENJY7tp[1]" width="585" height="441" srcset="/imgs/2015/02/ENJY7tp1.png 585w, /imgs/2015/02/ENJY7tp1-300x226.png 300w" sizes="(max-width: 585px) 100vw, 585px" /></a></li>
</ol>
<h3>Part 9 – Conclusion</h3>
<p>I&#8217;m hoping this was in depth enough for you Windows users out there. PGP can seem complicated at first, but with an hour or two of your time you can see it&#8217;s actually pretty simple. There&#8217;s obviously more behind it, and different tools that can be used, but we might save that for another time. Stay safe everyone! Encrypt all messages!</p>
</div>

Updated: 2015-02-21