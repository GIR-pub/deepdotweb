---
PGP Tutorial For OS X
---
<article class="post-listing post-9153 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-os tag-pgp tag-tutorial">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/admin/" title="">DeepDotWeb </a></span>
    <span>February 20, 2015</span>
    
    <span><a href="https://www.deepdotweb.com/2015/02/20/pgp-tutorial-os-x/#comments">28 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <div class="usertext-body may-blank-within md-container">
    <div class="md">
    <p><em>Full credit goes to <a href="http://www.reddit.com/user/MLP_is_my_OPSEC">MLP_is_my_OPSEC</a> for writing this tutorial – Thanks for publishing and giving your permission to repost!</em></p>
    <p><strong>Part 0 – Introduction</strong></p>
    <p>Here&#8217;s my basic guide for PGP on OS X. The OS in question is OS X 10.9 Mavericks, but it should still work for other versions. As for the tool itself, we&#8217;ll be using GPG Suite Beta 5. This is my first time using OS X in&#8230; years. If you see anything I&#8217;m doing wrong, or could be done easier, feel free to correct me in the comments.</p>
    <p>If you&#8217;ve done your research, you&#8217;ll see it&#8217;s not recommended to do anything darknet related on OS X, but I&#8217;m not going to go over the details here. You&#8217;ve obviously made your decision.</p>
    <p style="text-align: center;"><a href="https://www.deepdotweb.com/vpn-comparison-chart/">&gt;&gt;&gt;Add A Layer Of Encryption: Click For The Best VPN Services&lt;&lt;&lt;</a></p>
    <p><strong>Part 1 – Installing the software</strong></p>
    <p>Like I said above, we&#8217;ll be using GPG Suite Beta 5. If you&#8217;re curious and want to see the source code, you can do so <a href="https://gpgtools.org/opensource.html">here</a>.</p>
    <ol>
    <li>Head on over to <a href="https://gpgtools.org">https://gpgtools.org</a>, and download &#8216;GPG Suite Beta 5&#8217; <a href="/imgs/2015/02/UAQo3Ca1.png"><img class="aligncenter size-full wp-image-9154" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/UAQo3Ca1.png" alt="UAQo3Ca[1]" width="1084" height="686" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/UAQo3Ca1.png 1084w, https://www.deepdotweb.com/wp-content/uploads/2015/02/UAQo3Ca1-300x190.png 300w, https://www.deepdotweb.com/wp-content/uploads/2015/02/UAQo3Ca1-1024x648.png 1024w" sizes="(max-width: 1084px) 100vw, 1084px" /></a></li>
    <li>Open the file you downloaded, you should see this screen. Double click on &#8216;Install&#8217; <a href="/imgs/2015/02/dV8D0FZ1.png"><img class="aligncenter size-full wp-image-9155" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/dV8D0FZ1.png" alt="dV8D0FZ[1]" width="565" height="383" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/dV8D0FZ1.png 565w, https://www.deepdotweb.com/wp-content/uploads/2015/02/dV8D0FZ1-300x203.png 300w" sizes="(max-width: 565px) 100vw, 565px" /></a></li>
    <li>Follow the installation process. If successful, you should see this screen. You can now close the window <a href="/imgs/2015/02/m8qytPb1.png"><img class="aligncenter size-full wp-image-9156" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/m8qytPb1.png" alt="m8qytPb[1]" width="584" height="400" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/m8qytPb1.png 584w, https://www.deepdotweb.com/wp-content/uploads/2015/02/m8qytPb1-300x205.png 300w" sizes="(max-width: 584px) 100vw, 584px" /></a></li>
    </ol>
    <p><strong>Part 2 – Creating your keypair</strong></p>
    <p>GPG Suite actually makes this a super simple process. Just like the Linux guide, we&#8217;ll be using 4096 bit length for encryption.</p>
    <ol>
    <li>Open up GPG Keychain, you should be greeted by this beautiful window <a href="/imgs/2015/02/1xvho3K1.png"><img class="aligncenter size-full wp-image-9157" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/1xvho3K1.png" alt="1xvho3K[1]" width="871" height="573" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/1xvho3K1.png 871w, https://www.deepdotweb.com/wp-content/uploads/2015/02/1xvho3K1-300x197.png 300w" sizes="(max-width: 871px) 100vw, 871px" /></a></li>
    <li>Click &#8216;New&#8217; at the top left of the window <a href="/imgs/2015/02/JH57cE51.png"><img class="aligncenter size-full wp-image-9158" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/JH57cE51.png" alt="JH57cE5[1]" width="871" height="573" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/JH57cE51.png 871w, https://www.deepdotweb.com/wp-content/uploads/2015/02/JH57cE51-300x197.png 300w" sizes="(max-width: 871px) 100vw, 871px" /></a></li>
    <li>You should see a small popup. Click the arrow beside &#8216;Advanced options&#8217;, make sure the key length is 4096. For our purposes, we&#8217;ll uncheck &#8216;key expires&#8217;. Put your username where it says &#8216;full name&#8217;, fill out what you want for email, and create a secure passphrase. Check the picture for an example on how to fill it out. When complete, click &#8216;Generate key&#8217; <a href="/imgs/2015/02/UPn7xO41.png"><img class="aligncenter size-full wp-image-9159" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/UPn7xO41.png" alt="UPn7xO4[1]" width="871" height="575" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/UPn7xO41.png 871w, https://www.deepdotweb.com/wp-content/uploads/2015/02/UPn7xO41-300x198.png 300w" sizes="(max-width: 871px) 100vw, 871px" /></a></li>
    <li>GPG Keychain will begin generating your key. Move the mouse around, mash keys in a text editor, have something downloading. Do random stuff to create entropy for a secure key. <a href="/imgs/2015/02/1oFPI101.png"><img class="aligncenter size-full wp-image-9160" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/1oFPI101.png" alt="1oFPI10[1]" width="871" height="574" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/1oFPI101.png 871w, https://www.deepdotweb.com/wp-content/uploads/2015/02/1oFPI101-300x198.png 300w" sizes="(max-width: 871px) 100vw, 871px" /></a></li>
    <li>annndddddd we&#8217;re done! <a href="/imgs/2015/02/J0HkvZG1.png"><img class="aligncenter size-full wp-image-9161" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/J0HkvZG1.png" alt="J0HkvZG[1]" width="870" height="573" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/J0HkvZG1.png 870w, https://www.deepdotweb.com/wp-content/uploads/2015/02/J0HkvZG1-300x198.png 300w" sizes="(max-width: 870px) 100vw, 870px" /></a></li>
    </ol>
    <p><strong>Part 3 – Setting up the environment</strong></p>
    <p>This is where OS X differs from other platforms. The suite itself doesn&#8217;t provide a window to encrypt/decrypt messages, so we need to enable some options.</p>
    <ol>
    <li>Go into system preferences, open up &#8216;Keyboard&#8217; <a href="/imgs/2015/02/EYKyVkn1.png"><img class="aligncenter size-full wp-image-9162" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/EYKyVkn1.png" alt="EYKyVkn[1]" width="628" height="577" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/EYKyVkn1.png 628w, https://www.deepdotweb.com/wp-content/uploads/2015/02/EYKyVkn1-300x276.png 300w" sizes="(max-width: 628px) 100vw, 628px" /></a></li>
    <li>You should see this window. Click the &#8216;Keyboard Shortcuts&#8217; tab at the top, then &#8216;Services&#8217; in the left pane. Scroll down in the right pane to the subsection labeled &#8216;Text&#8217;, and to the OpenPGP options. Here you can create keyboard shortcuts. We&#8217;ll uncheck everything OpenPGP that&#8217;s under &#8216;Text&#8217;, and delete their shortcuts. Now we&#8217;ll enable &#8216;Decrypt&#8217;, &#8216;Encrypt&#8217;, and &#8216;Import key&#8217;. Create keyboard shortcuts for these if you wish. Check the picture to make sure you&#8217;re doing everything correctly. You can now close the window. <a href="/imgs/2015/02/2vQlkq81.png"><img class="aligncenter size-full wp-image-9163" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/2vQlkq81.png" alt="2vQlkq8[1]" width="629" height="544" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/2vQlkq81.png 629w, https://www.deepdotweb.com/wp-content/uploads/2015/02/2vQlkq81-300x259.png 300w" sizes="(max-width: 629px) 100vw, 629px" /></a></li>
    </ol>
    <p><strong>Part 4 – Obtaining your public key</strong></p>
    <p>This part is super simple.</p>
    <ol>
    <li>Open up GPG Keychain, select your key</li>
    <li>At the top of the window, click &#8216;Export&#8217; <a href="/imgs/2015/02/pvVfw2V1.png"><img class="aligncenter size-full wp-image-9164" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/pvVfw2V1.png" alt="pvVfw2V[1]" width="871" height="573" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/pvVfw2V1.png 871w, https://www.deepdotweb.com/wp-content/uploads/2015/02/pvVfw2V1-300x197.png 300w" sizes="(max-width: 871px) 100vw, 871px" /></a></li>
    <li>Give it a name, make sure &#8216;include secret key in exported file&#8217; is <strong>unchecked</strong>, and click &#8216;save&#8217; <a href="/imgs/2015/02/xwjzDoI1.png"><img class="aligncenter size-full wp-image-9165" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/xwjzDoI1.png" alt="xwjzDoI[1]" width="871" height="574" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/xwjzDoI1.png 871w, https://www.deepdotweb.com/wp-content/uploads/2015/02/xwjzDoI1-300x198.png 300w" sizes="(max-width: 871px) 100vw, 871px" /></a></li>
    <li>Open your text editor of choice, browse to where you saved the key, open it</li>
    <li>There it is. Copy and paste this on your market profile to make it easier for people to contact you <a href="/imgs/2015/02/RJhHUWx1.png"><img class="aligncenter size-full wp-image-9166" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/RJhHUWx1.png" alt="RJhHUWx[1]" width="552" height="655" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/RJhHUWx1.png 552w, https://www.deepdotweb.com/wp-content/uploads/2015/02/RJhHUWx1-253x300.png 253w" sizes="(max-width: 552px) 100vw, 552px" /></a></li>
    </ol>
    <p><strong>Part 5 – Obtaining your private key</strong></p>
    <p>Again, super simple.</p>
    <ol>
    <li>Open up GPG Keychain, select your key</li>
    <li>At the top of the window, click &#8216;Export&#8217;</li>
    <li>Keep the file name it gives you, <strong>check</strong> &#8216;Include secret key in exported file&#8217;, then click save <a href="/imgs/2015/02/QSLfhqW1.png"><img class="aligncenter size-full wp-image-9167" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/QSLfhqW1.png" alt="QSLfhqW[1]" width="870" height="573" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/QSLfhqW1.png 870w, https://www.deepdotweb.com/wp-content/uploads/2015/02/QSLfhqW1-300x198.png 300w" sizes="(max-width: 870px) 100vw, 870px" /></a></li>
    </ol>
    <p>Keep this file in a safe place, and don&#8217;t forget your passphrase. You&#8217;re fucked without it!</p>
    <p>Part 6 – Importing a public key</p>
    <p>This is really easy.</p>
    <ol>
    <li>Find the key you want to import.</li>
    <li>Copy everything from &#8216;&#8212;&#8211;BEGIN PGP PUBLIC KEY BLOCK&#8212;&#8211;&#8216; to &#8216;&#8212;&#8211;END PGP PUBLIC KEY BLOCK&#8212;&#8211;&#8216; <a href="/imgs/2015/02/nH6MBYc1.png"><img class="aligncenter size-full wp-image-9168" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/nH6MBYc1.png" alt="nH6MBYc[1]" width="532" height="407" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/nH6MBYc1.png 532w, https://www.deepdotweb.com/wp-content/uploads/2015/02/nH6MBYc1-300x230.png 300w" sizes="(max-width: 532px) 100vw, 532px" /></a></li>
    <li>Paste it into your favourite text editor, highlight everything, right click, go to &#8216;Services&#8217;, then &#8216;OpenPGP: Import key&#8217; <a href="/imgs/2015/02/Uq40mv11.png"><img class="aligncenter size-full wp-image-9169" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/Uq40mv11.png" alt="Uq40mv1[1]" width="835" height="668" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/Uq40mv11.png 835w, https://www.deepdotweb.com/wp-content/uploads/2015/02/Uq40mv11-300x240.png 300w" sizes="(max-width: 835px) 100vw, 835px" /></a></li>
    <li>You&#8217;ll see this window pop up confirming the key has been imported, click &#8216;Ok&#8217; <a href="/imgs/2015/02/CWv0ySL1.png"><img class="aligncenter size-full wp-image-9170" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/CWv0ySL1.png" alt="CWv0ySL[1]" width="384" height="153" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/CWv0ySL1.png 384w, https://www.deepdotweb.com/wp-content/uploads/2015/02/CWv0ySL1-300x120.png 300w" sizes="(max-width: 384px) 100vw, 384px" /></a></li>
    <li>Open up GPG Keychain just to confirm the key is there <a href="/imgs/2015/02/zQYRK9c1.png"><img class="aligncenter size-full wp-image-9171" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/zQYRK9c1.png" alt="zQYRK9c[1]" width="842" height="570" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/zQYRK9c1.png 842w, https://www.deepdotweb.com/wp-content/uploads/2015/02/zQYRK9c1-300x203.png 300w, https://www.deepdotweb.com/wp-content/uploads/2015/02/zQYRK9c1-290x195.png 290w" sizes="(max-width: 842px) 100vw, 842px" /></a></li>
    </ol>
    <p><strong>Part 7 – Importing a private key</strong></p>
    <p>Again, really easy.</p>
    <ol>
    <li>Open GPG Keychain, click &#8216;Import&#8217; at the top <a href="/imgs/2015/02/o7XMOBq1.png"><img class="aligncenter size-full wp-image-9172" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/o7XMOBq1.png" alt="o7XMOBq[1]" width="843" height="570" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/o7XMOBq1.png 843w, https://www.deepdotweb.com/wp-content/uploads/2015/02/o7XMOBq1-300x203.png 300w, https://www.deepdotweb.com/wp-content/uploads/2015/02/o7XMOBq1-290x195.png 290w" sizes="(max-width: 843px) 100vw, 843px" /></a></li>
    <li>Browse to where your key is, click it, then click &#8216;Open&#8217;. It should have a .asc file extension <a href="/imgs/2015/02/yUTGU3o1.png"><img class="aligncenter size-full wp-image-9173" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/yUTGU3o1.png" alt="yUTGU3o[1]" width="844" height="570" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/yUTGU3o1.png 844w, https://www.deepdotweb.com/wp-content/uploads/2015/02/yUTGU3o1-300x203.png 300w, https://www.deepdotweb.com/wp-content/uploads/2015/02/yUTGU3o1-290x195.png 290w" sizes="(max-width: 844px) 100vw, 844px" /></a></li>
    <li>You&#8217;ll see this pop up confirming your key has been imported. Click &#8216;Close&#8217; <a href="/imgs/2015/02/5Cadwt81.png"><img class="aligncenter size-full wp-image-9174" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/5Cadwt81.png" alt="5Cadwt8[1]" width="843" height="570" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/5Cadwt81.png 843w, https://www.deepdotweb.com/wp-content/uploads/2015/02/5Cadwt81-300x203.png 300w, https://www.deepdotweb.com/wp-content/uploads/2015/02/5Cadwt81-290x195.png 290w" sizes="(max-width: 843px) 100vw, 843px" /></a></li>
    </ol>
    <p><strong>Part 8 – Encrypting a message</strong></p>
    <ol>
    <li>Open your text editor of choice, write your message</li>
    <li>Highlight the message, right click, &#8216;Services&#8217;, &#8216;OpenPGP: Encrypt&#8217; <a href="/imgs/2015/02/LWjLFfL1.png"><img class="aligncenter size-full wp-image-9175" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/LWjLFfL1.png" alt="LWjLFfL[1]" width="680" height="543" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/LWjLFfL1.png 680w, https://www.deepdotweb.com/wp-content/uploads/2015/02/LWjLFfL1-300x240.png 300w" sizes="(max-width: 680px) 100vw, 680px" /></a></li>
    <li>A window should appear. Select who you&#8217;re sending it to, sign it with your key if you wish, click &#8216;Ok&#8217; <a href="/imgs/2015/02/g4UyC6Y1.png"><img class="aligncenter size-full wp-image-9176" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/g4UyC6Y1.png" alt="g4UyC6Y[1]" width="638" height="287" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/g4UyC6Y1.png 638w, https://www.deepdotweb.com/wp-content/uploads/2015/02/g4UyC6Y1-300x135.png 300w" sizes="(max-width: 638px) 100vw, 638px" /></a></li>
    <li>Copy everything, and send it to the recipient <a href="/imgs/2015/02/AFGqEOx1.png"><img class="aligncenter size-full wp-image-9177" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/AFGqEOx1.png" alt="AFGqEOx[1]" width="679" height="545" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/AFGqEOx1.png 679w, https://www.deepdotweb.com/wp-content/uploads/2015/02/AFGqEOx1-300x241.png 300w" sizes="(max-width: 679px) 100vw, 679px" /></a></li>
    </ol>
    <p><strong>Part 9 – Decrypting a message</strong></p>
    <p>Pretty much the same process as encrypting</p>
    <ol>
    <li>Open your text editor of choice, paste the message</li>
    <li>Highlight everything, right click, &#8216;Services&#8217;, &#8216;OpenPGP: Decrypt&#8217; <a href="/imgs/2015/02/u2wWMtA1.png"><img class="aligncenter size-full wp-image-9178" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/u2wWMtA1.png" alt="u2wWMtA[1]" width="701" height="565" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/u2wWMtA1.png 701w, https://www.deepdotweb.com/wp-content/uploads/2015/02/u2wWMtA1-300x242.png 300w" sizes="(max-width: 701px) 100vw, 701px" /></a></li>
    <li>A window should pop up. Enter your passphrase, then click &#8216;Ok&#8217; <a href="/imgs/2015/02/gL2nnbq1.png"><img class="aligncenter size-full wp-image-9179" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/gL2nnbq1.png" alt="gL2nnbq[1]" width="492" height="183" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/gL2nnbq1.png 492w, https://www.deepdotweb.com/wp-content/uploads/2015/02/gL2nnbq1-300x112.png 300w" sizes="(max-width: 492px) 100vw, 492px" /></a></li>
    <li>aannnddddd there&#8217;s your message <a href="/imgs/2015/02/zNX94M71.png"><img class="aligncenter size-full wp-image-9180" src="https://www.deepdotweb.com/wp-content/uploads/2015/02/zNX94M71.png" alt="zNX94M7[1]" width="680" height="544" srcset="https://www.deepdotweb.com/wp-content/uploads/2015/02/zNX94M71.png 680w, https://www.deepdotweb.com/wp-content/uploads/2015/02/zNX94M71-300x240.png 300w" sizes="(max-width: 680px) 100vw, 680px" /></a></li>
    </ol>
    <p><strong>Part 10 – Conclusion</strong></p>
    <p>That wasn&#8217;t too hard, was it? Like I said in the intro, you shouldn&#8217;t be using OS X for DNM activities due to privacy issues, but I won&#8217;t go into it. This took forever to complete because OS X is a bitch to get running properly in a virtual machine. A guide for Windows will be coming next week!</p>
    </div>
    </div>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/os/" rel="tag">os</a> <a href="https://www.deepdotweb.com/tag/pgp/" rel="tag">pgp</a> <a href="https://www.deepdotweb.com/tag/tutorial/" rel="tag">tutorial</a></span> <span style="display:none" class="updated">2015-02-20</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/admin/" title="Posts by DeepDotWeb" rel="author">DeepDotWeb</a></strong></div>
    </div>
</article>

