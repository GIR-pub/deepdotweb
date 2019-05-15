---
title: "PGP Tutorial For OS X"
---


Posted by: DeepDotWeb 

<span>February 20, 2015</span>
    

<div class="usertext-body may-blank-within md-container">
<div class="md">
<p><em>Full credit goes to <a href="http://www.reddit.com/user/MLP_is_my_OPSEC">MLP_is_my_OPSEC</a> for writing this tutorial – Thanks for publishing and giving your permission to repost!</em></p>
<p><strong>Part 0 – Introduction</strong></p>
<p>Here&#8217;s my basic guide for PGP on OS X. The OS in question is OS X 10.9 Mavericks, but it should still work for other versions. As for the tool itself, we&#8217;ll be using GPG Suite Beta 5. This is my first time using OS X in&#8230; years. If you see anything I&#8217;m doing wrong, or could be done easier, feel free to correct me in the comments.</p>
<p>If you&#8217;ve done your research, you&#8217;ll see it&#8217;s not recommended to do anything darknet related on OS X, but I&#8217;m not going to go over the details here. You&#8217;ve obviously made your decision.</p>
<p style="text-align: center;"><a href="/vpn-comparison-chart/">&gt;&gt;&gt;Add A Layer Of Encryption: Click For The Best VPN Services&lt;&lt;&lt;</a></p>
<p><strong>Part 1 – Installing the software</strong></p>
<p>Like I said above, we&#8217;ll be using GPG Suite Beta 5. If you&#8217;re curious and want to see the source code, you can do so <a href="https://gpgtools.org/opensource.html">here</a>.</p>
<ol>
<li>Head on over to <a href="https://gpgtools.org">https://gpgtools.org</a>, and download &#8216;GPG Suite Beta 5&#8217; <a href="/imgs/2015/02/UAQo3Ca1.png">
<li>Open the file you downloaded, you should see this screen. Double click on &#8216;Install&#8217; <a href="/imgs/2015/02/dV8D0FZ1.png">
<li>Follow the installation process. If successful, you should see this screen. You can now close the window <a href="/imgs/2015/02/m8qytPb1.png">
</ol>
<p><strong>Part 2 – Creating your keypair</strong></p>
<p>GPG Suite actually makes this a super simple process. Just like the Linux guide, we&#8217;ll be using 4096 bit length for encryption.</p>
<ol>
<li>Open up GPG Keychain, you should be greeted by this beautiful window <a href="/imgs/2015/02/1xvho3K1.png">
<li>Click &#8216;New&#8217; at the top left of the window <a href="/imgs/2015/02/JH57cE51.png">
<li>You should see a small popup. Click the arrow beside &#8216;Advanced options&#8217;, make sure the key length is 4096. For our purposes, we&#8217;ll uncheck &#8216;key expires&#8217;. Put your username where it says &#8216;full name&#8217;, fill out what you want for email, and create a secure passphrase. Check the picture for an example on how to fill it out. When complete, click &#8216;Generate key&#8217; <a href="/imgs/2015/02/UPn7xO41.png">
<li>GPG Keychain will begin generating your key. Move the mouse around, mash keys in a text editor, have something downloading. Do random stuff to create entropy for a secure key. <a href="/imgs/2015/02/1oFPI101.png">
<li>annndddddd we&#8217;re done! <a href="/imgs/2015/02/J0HkvZG1.png">
</ol>
<p><strong>Part 3 – Setting up the environment</strong></p>
<p>This is where OS X differs from other platforms. The suite itself doesn&#8217;t provide a window to encrypt/decrypt messages, so we need to enable some options.</p>
<ol>
<li>Go into system preferences, open up &#8216;Keyboard&#8217; <a href="/imgs/2015/02/EYKyVkn1.png">
<li>You should see this window. Click the &#8216;Keyboard Shortcuts&#8217; tab at the top, then &#8216;Services&#8217; in the left pane. Scroll down in the right pane to the subsection labeled &#8216;Text&#8217;, and to the OpenPGP options. Here you can create keyboard shortcuts. We&#8217;ll uncheck everything OpenPGP that&#8217;s under &#8216;Text&#8217;, and delete their shortcuts. Now we&#8217;ll enable &#8216;Decrypt&#8217;, &#8216;Encrypt&#8217;, and &#8216;Import key&#8217;. Create keyboard shortcuts for these if you wish. Check the picture to make sure you&#8217;re doing everything correctly. You can now close the window. <a href="/imgs/2015/02/2vQlkq81.png">
</ol>
<p><strong>Part 4 – Obtaining your public key</strong></p>
<p>This part is super simple.</p>
<ol>
<li>Open up GPG Keychain, select your key</li>
<li>At the top of the window, click &#8216;Export&#8217; <a href="/imgs/2015/02/pvVfw2V1.png">
<li>Give it a name, make sure &#8216;include secret key in exported file&#8217; is <strong>unchecked</strong>, and click &#8216;save&#8217; <a href="/imgs/2015/02/xwjzDoI1.png">
<li>Open your text editor of choice, browse to where you saved the key, open it</li>
<li>There it is. Copy and paste this on your market profile to make it easier for people to contact you <a href="/imgs/2015/02/RJhHUWx1.png">
</ol>
<p><strong>Part 5 – Obtaining your private key</strong></p>
<p>Again, super simple.</p>
<ol>
<li>Open up GPG Keychain, select your key</li>
<li>At the top of the window, click &#8216;Export&#8217;</li>
<li>Keep the file name it gives you, <strong>check</strong> &#8216;Include secret key in exported file&#8217;, then click save <a href="/imgs/2015/02/QSLfhqW1.png">
</ol>
<p>Keep this file in a safe place, and don&#8217;t forget your passphrase. You&#8217;re fucked without it!</p>
<p>Part 6 – Importing a public key</p>
<p>This is really easy.</p>
<ol>
<li>Find the key you want to import.</li>
<li>Copy everything from &#8216;&#8212;&#8211;BEGIN PGP PUBLIC KEY BLOCK&#8212;&#8211;&#8216; to &#8216;&#8212;&#8211;END PGP PUBLIC KEY BLOCK&#8212;&#8211;&#8216; <a href="/imgs/2015/02/nH6MBYc1.png">
<li>Paste it into your favourite text editor, highlight everything, right click, go to &#8216;Services&#8217;, then &#8216;OpenPGP: Import key&#8217; <a href="/imgs/2015/02/Uq40mv11.png">
<li>You&#8217;ll see this window pop up confirming the key has been imported, click &#8216;Ok&#8217; <a href="/imgs/2015/02/CWv0ySL1.png">
<li>Open up GPG Keychain just to confirm the key is there <a href="/imgs/2015/02/zQYRK9c1.png">
</ol>
<p><strong>Part 7 – Importing a private key</strong></p>
<p>Again, really easy.</p>
<ol>
<li>Open GPG Keychain, click &#8216;Import&#8217; at the top <a href="/imgs/2015/02/o7XMOBq1.png">
<li>Browse to where your key is, click it, then click &#8216;Open&#8217;. It should have a .asc file extension <a href="/imgs/2015/02/yUTGU3o1.png">
<li>You&#8217;ll see this pop up confirming your key has been imported. Click &#8216;Close&#8217; <a href="/imgs/2015/02/5Cadwt81.png">
</ol>
<p><strong>Part 8 – Encrypting a message</strong></p>
<ol>
<li>Open your text editor of choice, write your message</li>
<li>Highlight the message, right click, &#8216;Services&#8217;, &#8216;OpenPGP: Encrypt&#8217; <a href="/imgs/2015/02/LWjLFfL1.png">
<li>A window should appear. Select who you&#8217;re sending it to, sign it with your key if you wish, click &#8216;Ok&#8217; <a href="/imgs/2015/02/g4UyC6Y1.png">
<li>Copy everything, and send it to the recipient <a href="/imgs/2015/02/AFGqEOx1.png">
</ol>
<p><strong>Part 9 – Decrypting a message</strong></p>
<p>Pretty much the same process as encrypting</p>
<ol>
<li>Open your text editor of choice, paste the message</li>
<li>Highlight everything, right click, &#8216;Services&#8217;, &#8216;OpenPGP: Decrypt&#8217; <a href="/imgs/2015/02/u2wWMtA1.png">
<li>A window should pop up. Enter your passphrase, then click &#8216;Ok&#8217; <a href="/imgs/2015/02/gL2nnbq1.png">
<li>aannnddddd there&#8217;s your message <a href="/imgs/2015/02/zNX94M71.png">
</ol>
<p><strong>Part 10 – Conclusion</strong></p>
<p>That wasn&#8217;t too hard, was it? Like I said in the intro, you shouldn&#8217;t be using OS X for DNM activities due to privacy issues, but I won&#8217;t go into it. This took forever to complete because OS X is a bitch to get running properly in a virtual machine. A guide for Windows will be coming next week!</p>

Updated: 2015-02-20

