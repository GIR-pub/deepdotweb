---
title: "PGP Tutorial For Windows (Kleopatra &#8211; Gpg4Win)"
---


Posted by: DeepDotWeb 

<span>February 21, 2015</span>


<div class="usertext-body may-blank-within md-container">
<div class="md">
<p><em>Full credit goes to <a href="http://www.reddit.com/user/MLP_is_my_OPSEC">MLP_is_my_OPSEC</a> for writing this tutorial – Thanks for publishing and giving your permission to repost!<br />
    Tutorial for </em>Gpg4Win using GPA can <a href="/2013/11/11/pgp-tutorial-for-newbs-gpg4win/" target="_blank">be found here</a>.</p>
<h3>Part 0 – Introduction</h3>
<p>Here&#8217;s the final guide in my PGP basics series, this time focusing on Windows. The OS in question will be Windows 7, but it should work for Win8 and Win8.1 as well. Obviously it&#8217;s not recommended to be using Windows to access the DNM, but I wont go into the reasons here. The tool we&#8217;ll be using is GPG4Win.</p>
<p style="text-align: center;"><a href="/vpn-comparison-chart/">&gt;&gt;&gt;Add A Layer Of Encryption: Click For The Best VPN Services&lt;&lt;&lt;</a></p>
<h3>Part 1 – Installing the software</h3>
<p>Just like I said above, we&#8217;ll be using GPG4Win. If you&#8217;re curious, you can view the source code for it <a href="https://git.gnupg.org/cgi-bin/gitweb.cgi?p=gpg4win.git;a=summary">here</a>.</p>
<ol>
<li>Head on over to <a href="https://gpg4win.org/download.html">https://gpg4win.org/download.html</a>. We want the full version, so click &#8216;Gpg4win 2.2.3&#8217; 

<img src="/imgs/2015/02/iXqHJld1.png">

<li>Save it, open it when it&#8217;s done downloading. If you have UAC enabled, click &#8216;Yes&#8217; on the window that appears 

<img src="/imgs/2015/02/NFVNUCS1.png">

<li>Choose your language, click &#8216;Ok&#8217; 

<img src="/imgs/2015/02/SUJ3aT21.png">

<li>Click &#8216;Next&#8217;, then &#8216;Next&#8217; again. You&#8217;ll now be at a screen asking what components you want to install. We&#8217;ll be selecting &#8216;Kleopatra&#8217;, &#8216;GpgEX&#8217;, and &#8216;Gpg4win Compendium&#8217;. Then click &#8216;Next&#8217; 

<img src="/imgs/2015/02/oNLB4Kk1.png">

<li>It will ask where to install, just keep the default and click &#8216;Next&#8217;</li>
<li>Now it&#8217;ll ask where you want to install shortcuts. Select whichever you want, click &#8216;Next&#8217;</li>
<li>You can choose which Start Menu folder you want it installed in, just click &#8216;Next&#8217;</li>
<li>It will now install, when done you should see this. Click &#8216;Next&#8217;, then &#8216;Finish&#8217; 

<img src="/imgs/2015/02/RYUfaj41.png">

</ol>
<p>Now you have the tools you need to get started with PGP</p>
<h3>Part 2 – Generating your keypair</h3>
<p>The next step is to generate your keypair so you can encrypt/decrypt messages. Like always, we&#8217;ll be going with 4096 bit RSA.</p>
<ol>
<li>Open up Kleopatra, you should be greeted with this beautiful screen 

<img src="/imgs/2015/02/5i6tnlr1.png">

<li>Go to &#8216;File&#8217;, then &#8216;New Certificate&#8230;&#8217; 

<img src="/imgs/2015/02/u069Ntb1.png">

<li>The Certificate Creation Wizard should pop up, click on &#8216;Create a personal OpenPGP key pair&#8217; 

<img src="/imgs/2015/02/oVaws0J1.png">

<li>Now you&#8217;ll enter your details. Use your marketplace username as &#8216;Name&#8217;, and fill out the rest with whatever you want. You don&#8217;t need to use a real email. Check the picture for an example on how it should look 

<img src="/imgs/2015/02/xJFjFGx1.png">

<li><strong>Do not click &#8216;Next&#8217; yet</strong>, we need to fill out some more details. Click &#8216;Advanced Settings&#8230;&#8217;, and another window should appear. Under &#8216;Key Material&#8217;, make sure &#8216;RSA&#8217; is checked. In the drop down menu beside it, and select &#8216;4,096 bits&#8217;. Check the picture to confirm you have everything set correctly, then click &#8216;Ok&#8217; 

<img src="/imgs/2015/02/dcOihQG1.png">

<li>Confirm you filled out all of your info correctly, then click &#8216;Create Key&#8217; 

<img src="/imgs/2015/02/hUIQgMb1.png">

<li>Another window will pop up asking to enter a passphrase. Do so, then click &#8216;Ok&#8217; 

<img src="/imgs/2015/02/kIPFAQF1.png">

<li>It will now generate your key. It will need you to do random things to create entropy. Mash keys, wiggle the mouse, watch porn, download torrents, whatever 

<img src="/imgs/2015/02/p8vJdbN1.png">

<li>Your key is now created. Go ahead and click &#8216;Finish&#8217; 

<img src="/imgs/2015/02/1SRNdt61.png">

</ol>
<h3>Part 3 – Obtaining your public key</h3>
<p>Now we need to get your public key, without it vendors wont be able to send you secure messages.</p>
<ol>
<li>Right click on your key, then click &#8216;Export Certificates&#8230;&#8217; 

<img src="/imgs/2015/02/h86y7Le1.png">

<li>Browse where you want to save, give it a name, then click &#8216;Save&#8217;</li>
<li>Open your favourite text editor, browse to where the file is saved. You may have to select &#8216;All files&#8217; from the dropdown menu. Click the file you saved, then open 

<img src="/imgs/2015/02/XIFqJy81.png">

<li>There&#8217;s your public key 

<img src="/imgs/2015/02/gJK0c9S1.png">

</ol>
<p>Remember to add your public key to your market profile so people can message you easier!</p>
<h3>Part 4 – Obtaining your private key</h3>
<p>Just as easy as obtaining your public key</p>
<ol>
<li>Right click on your key, select &#8216;Export Secret Keys&#8230;&#8217; 

<img src="/imgs/2015/02/KBWbUBC1.png">

<li>Select where you want it saved, give it a name, check &#8216;ASCII armor&#8217;, and click &#8216;Ok&#8217; 

<img src="/imgs/2015/02/d4MPQKB1.png">

<li>You now have your private key 

<img src="/imgs/2015/02/M4osyVS1.png">

</ol>
<p>Remember to keep this in a safe place, and never share it!</p>
<h3>Part 5 – Importing a public key</h3>
<p>It&#8217;s impossible to send a vendor an encrypted message without their public key.</p>
<ol>
<li>Find a public key you want to import</li>
<li>Copy everything from &#8216;&#8212;&#8211;BEGIN PGP PUBLIC KEY BLOCK&#8212;&#8211;&#8216; to &#8216;&#8212;&#8211;END PGP PUBLIC KEY BLOCK&#8212;&#8216;, see the picture for an example 

<img src="/imgs/2015/02/69UnFPR1.png">

<li>In your task bar, right click on the Kleopatra icon, go to &#8216;Clipboard&#8217;, then click &#8216;Certificate Import&#8217; 

<img src="/imgs/2015/02/UG15ss61.png">

<li>If it worked, you should see a window pop up, click &#8216;Ok&#8217; 

<img src="/imgs/2015/02/J9kQIQB1.png">

<li>You should now see the imported key in Kleopatra under the &#8216;Other Certificates&#8217; tab 

<img src="/imgs/2015/02/2G438Pi1.png">

</ol>
<p>Thanks again Alan!</p>
<h3>Part 6 – Importing your private key</h3>
<p>Simple stuff.</p>
<ol>
<li>Go to &#8216;File&#8217;, then click &#8216;Import Certificates&#8230;&#8217; 

<img src="/imgs/2015/02/hHDqxpO1.png">

<li>Browse to where your private key is, select it, then click &#8216;Open&#8217; 

<img src="/imgs/2015/02/Qq8OmEn1.png">

<li>It will import your private key, and pop up a window to confirm. Click &#8216;Ok&#8217; 

<img src="/imgs/2015/02/m6YsDUv1.png">

<li>You should now see your key information under the &#8216;My Certificates&#8217; tab 

<img src="/imgs/2015/02/SyPzPmp1.png">

</ol>
<h3>Part 7 – Encrypting a message</h3>
<p>Now that we&#8217;re ready to go, lets go ahead and send a message.</p>
<ol>
<li>Open up your text editor of choice</li>
<li>Type out your message, select it all, and copy it 

<img src="/imgs/2015/02/fpsVEX21.png">

<li>In your task bar, right click on the Kleopatra icon, go to &#8216;Clipboard&#8217;, then click &#8216;Encrypt&#8230;&#8217; 

<img src="/imgs/2015/02/jSeuc6p1.png">

<li>This gorgeous window will open. Click &#8216;Add Recipient&#8230;&#8217; 

<img src="/imgs/2015/02/xmzkSvm1.png">

<li>Another window will appear. Click the &#8216;Other Certificates&#8217; tab, then select who you want to send your message to, then click &#8216;Ok&#8217;. 

<img src="/imgs/2015/02/88SqUA21.png">

<li>You should be back at the previous window with the recipient listed. Click &#8216;Next&#8217; 

<img src="/imgs/2015/02/g4qk0H61.png">

<li>If all went well, you should see this window. Click &#8216;Ok&#8217; 

<img src="/imgs/2015/02/jnIS7Wo1.png">

<li>Your encrypted message will be in your clipboard, all you need to do is paste it into the message box and send 

<img src="/imgs/2015/02/hrQ9tb01.png">

</ol>
<h3>Part 8 – Decrypting a message</h3>
<p>This is just as easy as encrypting.</p>
<ol>
<li>Copy everything that was sent 

<img src="/imgs/2015/02/aj50dmL1.png">

<li>In your task bar, right click on the Kleopatra icon, go to &#8216;Clipboard&#8217;, then click &#8216;Decrypt/Verify&#8230;&#8217; 

<img src="/imgs/2015/02/T8lqyCo1.png">

<li>A window will pop up asking for your passphrase, enter that then click &#8216;Ok&#8217; 

<img src="/imgs/2015/02/yj6ciCG1.png">

<li>A window should pop up verifying it was decrypted, and copied to your clipboard. Click &#8216;Finish&#8217;</li>
<li>Open your text editor of choice, and paste your message 

<img src="/imgs/2015/02/ENJY7tp1.png">

</ol>
<h3>Part 9 – Conclusion</h3>
<p>I&#8217;m hoping this was in depth enough for you Windows users out there. PGP can seem complicated at first, but with an hour or two of your time you can see it&#8217;s actually pretty simple. There&#8217;s obviously more behind it, and different tools that can be used, but we might save that for another time. Stay safe everyone! Encrypt all messages!</p>

Updated: 2015-02-21