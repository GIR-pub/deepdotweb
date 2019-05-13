---
PGP Tutorial For Newbs Gpg4usb"
---
<article class="post-listing post-9525 post type-post status-publish format-standard has-post-thumbnail hentry  tag-gpg4usb tag-newbs tag-pgp tag-tutorial">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/admin/" title="">DeepDotWeb </a></span>
    <span>June 21, 2015</span>
    
    <span><a href="https://www.deepdotweb.com/2015/06/21/pgp-tutorial-for-newbs-gpg4usb/#comments">31 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>To wrap up the last of the PGP guides we&#8217;ll be covering gpg4usb. Gpg4usb is a PGP tool that can be ran off of a USB drive and works on both Windows and GNU/Linux, with OS X support planned. It features a very intuitive user interface, portability so it can be used on multiple devices, and is of course open source. It uses GnuPG as the backend, like most PGP methods. The operating system used in this tutorial will be Linux Mint, but the UI will be the same across GNU/Linux distros and Windows versions.</p>
    <p style="text-align: center;"><a href="https://www.deepdotweb.com/vpn-comparison-chart/">&gt;&gt;&gt;Add A Layer Of Encryption: Click For The Best VPN Services&lt;&lt;&lt;</a></p>
    <p>Please keep in mind that <a href="http://www.deepdotweb.com/security-tutorials/word-warning-versions-pgp-created-equally/">not all versions of PGP are created equally</a>, some PGP programs use an insecure or unsafe version of PGP that could comprimise the encrypted message. Others &#8212; namely PGP4Win, Kleopatra, and GPA – use depreciated versions of GnuPG. This means that they aren&#8217;t up to date with the latest version of GnuPG or meet modern PGP standards. This can be dagerous as, for example, Kleopatra doesn&#8217;t generate subkeys. Subkeys are important as they can be revoked to minimize damage from a comprimised key. You&#8217;ll also want to keep in mind not to use online PGP methods like iGolder. You don&#8217;t own the keys, so you can&#8217;t be 100% sure they aren&#8217;t encrypting/decrypting messages that are meant for your eyes only.</p>
    <p><strong>Why use gpg4usb over other PGP methods?</strong></p>
    <ol>
    <li>gpg4usb creates RSA keys with an encryption subkey and a master key. Your master key is used for signing other keys, creating subkeys, and revoking subkeys. Having subkeys is very important since if it becomes compromised, you can revoke it with the master key and create a new secure subkey.</li>
    </ol>
    <ol start="2">
    <li>Like stated above, gpg4usb is cross-platform. If you decide to switch from Windows to GNU/Linux you can still have the same keys and a familiar interface to work with. With OS X support planned this only gives another reason why you should use gpg4usb over other programs.</li>
    </ol>
    <ol start="3">
    <li>gpg4usb is portable. This means that you can bring your keys and PGP program with you wherever you go without needing to import your keys into another program. If you plan on doing this though it&#8217;s a good idea to encrypt you USB drive. <a href="https://wiki.archlinux.org/index.php/disk_encryption#Preparation">This page</a> over at the ArchLinux wiki explains how you can do this on GNU/Linux any why you should encrypt your USB drive, or read <a href="https://technet.microsoft.com/en-us/magazine/ff404223.aspx">this page</a> if you&#8217;re using a Windows computer.</li>
    </ol>
    <ol start="4">
    <li>The interface for gpg4usb is the most intuitive out of all other PGP front-ends. The UI is laid out in an easy to understand manner and options are clearly defined.</li>
    </ol>
    <ol start="5">
    <li>You can encrypt messages created in gpg4usb with multiple keys. This means that you can have multiple recipients for a message, and you can even encrypt it with your own key. Nobody decrypting a message encrypted with multiple keys can see that it was meant for anyone other than them. This is good if you get scammed on the DNM since you can now have proof to back up any claims you have.</li>
    </ol>
    <p><strong>Part 1 – Installing the software</strong></p>
    <p>Since gpg4usb is a portable program, it&#8217;s not really installed per se. It&#8217;s a bunch of files that will be extracted from a .zip archive, and copied onto the USB drive. Head on over to the <strong><a href="http://www.gpg4usb.org/about.html">gpg4usb website</a></strong> and click on the green download button, and save the file. If you want to check out the source code you can visit their development page <strong><a href="http://www.gpg4usb.org/development.html">here</a></strong>.</p>
    <p>Note: gpg4usb will not run on GNU/Linux distributions on USB drives formatted as FAT. If you&#8217;re only using it on GNU/Linux operating systems then ext4 would be best, otherwise format it to NTFS.</p>
    <p><a href="/imgs/2015/03/g4u02.png"><img class="aligncenter size-full wp-image-9527" src="/imgs/2015/03/g4u02.png" alt="g4u02" width="859" height="287" srcset="/imgs/2015/03/g4u02.png 859w, /imgs/2015/03/g4u02-300x100.png 300w" sizes="(max-width: 859px) 100vw, 859px" /></a></p>
    <p>After the download has finished open up the .zip file with your archive manager of choice, you should be able to just double-click on it. You should see a folder named &#8216;gpg4win&#8217;, with all the files needed contained within that folder. Copy that folder over to your USB drive, open it, and it should look similar to the below picture.</p>
    <p><a href="/imgs/2015/03/g4u03.png"><img class="aligncenter size-full wp-image-9528" src="/imgs/2015/03/g4u03.png" alt="g4u03" width="721" height="524" srcset="/imgs/2015/03/g4u03.png 721w, /imgs/2015/03/g4u03-300x218.png 300w" sizes="(max-width: 721px) 100vw, 721px" /></a></p>
    <p>That was pretty simple right? Check out the README file if you want to know more about gpg4usb. To open it, all you have to do is double-click &#8216;start_windows.exe&#8217; if you&#8217;re on Windows, or &#8216;start_linux_xxbit&#8217; where &#8216;xx&#8217; is your CPU architecture. For the majority of users this will be the 64bit version.</p>
    <p><strong>Part 2 – Generating your keypair</strong></p>
    <p>This is the very first thing you should do. Without your own keypair, it will be impossible to receive and decrypt messages. Open up gpg4usb and you&#8217;ll be greeted by the &#8216;First Start Wizard&#8217;. This will walk you through the steps of creating your keypair.</p>
    <p><a href="/imgs/2015/03/g4u04.png"><img class="aligncenter size-full wp-image-9529" src="/imgs/2015/03/g4u04.png" alt="g4u04" width="801" height="477" srcset="/imgs/2015/03/g4u04.png 801w, /imgs/2015/03/g4u04-300x179.png 300w" sizes="(max-width: 801px) 100vw, 801px" /></a></p>
    <p>Choose your language then click &#8216;Next&#8217;. It will now ask you if you want to create a new keypair, import keys from GnuPG, or import settings/keys from an older version of gng4usb. Click on &#8216;create a new keypair&#8217;, then click the button that says &#8216;Create New Key&#8217;. You should see a window with the title &#8216;Generate Key&#8217;. Fill out the information, fill out a fake email if you don&#8217;t want to use one, select if you want it to expire or not, choose the KeySize, then create a strong password. A 2048 bit keypair will <a href="http://danielpocock.com/rsa-key-sizes-2048-or-4096-bits">do fine until 2030</a>, but it&#8217;s recommended to use a 4096 bit key. If you want to know more about how the keysize affects your security, check out <a href="https://www.gnupg.org/(en)/faq/gnupg-faq.html#advanced_topics">this link</a> over at the GnuPG website.</p>
    <p>If filled out correctly your window should look something similar to below.</p>
    <p><a href="/imgs/2015/03/g4u05.png"><img class="aligncenter size-full wp-image-9530" src="/imgs/2015/03/g4u05.png" alt="g4u05" width="422" height="311" srcset="/imgs/2015/03/g4u05.png 422w, /imgs/2015/03/g4u05-300x221.png 300w" sizes="(max-width: 422px) 100vw, 422px" /></a></p>
    <p>You can now click &#8216;Ok&#8217;, and your keypair will be generated. This may take some time depending on what you&#8217;re doing on your computer. Watch some porn, torrent some GNU/Linux ISOs, type up that essay you were supposed to have done last week. If all went well a window will pop up saying your keypair has been created.</p>
    <p><a href="/imgs/2015/03/g4u06.png"><img class="aligncenter size-full wp-image-9531" src="/imgs/2015/03/g4u06.png" alt="g4u06" width="175" height="114" /></a></p>
    <p>You can now close out of the wizard, and select if you want to see the offline help or show the wizard again next time you start up. You&#8217;ll be brought to the main gpg4usb window and will see your keypair on the right, along with gpg4usb&#8217;s keypair.</p>
    <p><a href="/imgs/2015/03/g4u07.png"><img class="aligncenter size-full wp-image-9532" src="/imgs/2015/03/g4u07.png" alt="g4u07" width="802" height="477" srcset="/imgs/2015/03/g4u07.png 802w, /imgs/2015/03/g4u07-300x178.png 300w" sizes="(max-width: 802px) 100vw, 802px" /></a></p>
    <p><strong>Part 3 – Obtaining your public key</strong></p>
    <p>To receive messages you&#8217;ll need your public key posted somewhere. This is really easy in gpg4usb as you don&#8217;t need to save it to a file first.</p>
    <p>With gpg4usb open, click &#8216;Manage Keys&#8217; at the top. A window titles &#8216;Keymanagement&#8217; should appear. Check off the box beside your keypair name, and click &#8216;Export to Clipboard&#8217; at the top. You can now paste your public key somewhere people can access it so they can send you messages. If you want a backup of your public key you can also click &#8216;Export To File&#8217; and save it somewhere.</p>
    <p><a href="/imgs/2015/03/g4u08.png"><img class="aligncenter size-full wp-image-9533" src="/imgs/2015/03/g4u08.png" alt="g4u08" width="802" height="427" srcset="/imgs/2015/03/g4u08.png 802w, /imgs/2015/03/g4u08-300x160.png 300w" sizes="(max-width: 802px) 100vw, 802px" /></a></p>
    <p><strong>Part 4 – Obtaining your private key</strong></p>
    <p>It&#8217;s a good idea to back up your private key somewhere safe in case of computer failure. Although rare, things do happen and you don&#8217;t want to be stuck not being able to decrypt that very important message your mother sent you.</p>
    <p>From the main window right click on your key on the right, and click &#8216;Show Key Details&#8217;.</p>
    <p><a href="/imgs/2015/03/g4u09.png"><img class="aligncenter size-full wp-image-9534" src="/imgs/2015/03/g4u09.png" alt="g4u09" width="376" height="163" srcset="/imgs/2015/03/g4u09.png 376w, /imgs/2015/03/g4u09-300x130.png 300w" sizes="(max-width: 376px) 100vw, 376px" /></a></p>
    <p>From here you can see the details of your key, it&#8217;s fingerprint, and export your private key. Click the button that says &#8216;Export Private Key&#8217; and it will warn you that this is sensitive information that is not to be shared. Select somewhere to save it and keep the filename it gives. A good idea is to save it to a microSD card and hide it somewhere. You don&#8217;t want anyone other than you to get a hold of your private key.</p>
    <p>Again, it is <strong>very important</strong> that you keep this file somewhere secure.</p>
    <p><strong>Part 5 – Importing a public key</strong></p>
    <p>gpg4win makes this just as easy as exporting your public key. Highlight everything in the public key, including &#8216;&#8212;&#8211; BEGIN PGP PUBLIC KEY BLOCK&#8212;&#8211;&#8216; and &#8216;&#8212;&#8211; END PGP PUBLIC KEY BLOCK&#8217;, and copy it. In the main gpg4usb window click &#8216;Import Key&#8217; at the top, then &#8216;Clipboard&#8217;. You&#8217;ll see a window pop up with the imported key&#8217;s details.</p>
    <p><a href="/imgs/2015/03/g4u10.png"><img class="aligncenter size-full wp-image-9535" src="/imgs/2015/03/g4u10.png" alt="g4u10" width="602" height="327" srcset="/imgs/2015/03/g4u10.png 602w, /imgs/2015/03/g4u10-300x163.png 300w" sizes="(max-width: 602px) 100vw, 602px" /></a></p>
    <p>Close out of the window and you&#8217;ll see the public key has been imported.</p>
    <p><strong>Part 6 – Importing a private key</strong></p>
    <p>This is just as easy as importing a public key. In the main gpg4usb window click &#8216;Import Key&#8217;, then &#8216;File&#8217;. Browse to where you saved your private key and open it. You should see a window pop up confirming that it&#8217;s been imported. Click &#8216;Ok&#8217; and you&#8217;ll see your keypair in the right part of gpg4win.</p>
    <p><a href="/imgs/2015/03/g4u11.png"><img class="aligncenter size-full wp-image-9536" src="/imgs/2015/03/g4u11.png" alt="g4u11" width="602" height="348" srcset="/imgs/2015/03/g4u11.png 602w, /imgs/2015/03/g4u11-300x173.png 300w" sizes="(max-width: 602px) 100vw, 602px" /></a></p>
    <p><strong>Part 7 – Encrypting a message</strong></p>
    <p>Encrypting a message in gpg4usb is super simple. In the main window for gpg4usb there will be a text box. Type in your message, click the checkbox for the recipient on the right, and click &#8216;Encrypt&#8217; up at the top. Your encrypted message will now take the place of the unencrypted one. Copy and paste this and send it to the recipient.</p>
    <p><a href="/imgs/2015/03/g4u12.png"><img class="aligncenter size-full wp-image-9537" src="/imgs/2015/03/g4u12.png" alt="g4u12" width="802" height="540" srcset="/imgs/2015/03/g4u12.png 802w, /imgs/2015/03/g4u12-300x202.png 300w, /imgs/2015/03/g4u12-290x195.png 290w" sizes="(max-width: 802px) 100vw, 802px" /></a></p>
    <p><strong>Part 8 – Decrypting a message</strong></p>
    <p>Once again, gpg4usb makes this really easy. Just paste the message you received into the textbox and click &#8216;Decrypt&#8217; up at the top. Enter your password and your decrypted message will take the place of the encrypted one.</p>
    <p><a href="/imgs/2015/03/g4u13.png"><img class="aligncenter size-full wp-image-9538" src="/imgs/2015/03/g4u13.png" alt="g4u13" width="802" height="541" srcset="/imgs/2015/03/g4u13.png 802w, /imgs/2015/03/g4u13-300x202.png 300w, /imgs/2015/03/g4u13-290x195.png 290w" sizes="(max-width: 802px) 100vw, 802px" /></a></p>
    <p><strong>Part 9 – Conclusion</strong></p>
    <p>If you&#8217;ve followed the above steps and understood each one you&#8217;re on your way to increased privacy in a world that wants to invade it. PGP can seem complicated at first, but once you learn it you&#8217;ll laugh at yourself for thinking it was so hard. Even if you still think it&#8217;s complicated or a waste of time, just keep in mind that taking an extra 60 seconds out of your day could possible save you from serving 5+ years in prison.</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/gpg4usb/" rel="tag">gpg4usb</a> <a href="https://www.deepdotweb.com/tag/newbs/" rel="tag">newbs</a> <a href="https://www.deepdotweb.com/tag/pgp/" rel="tag">pgp</a> <a href="https://www.deepdotweb.com/tag/tutorial/" rel="tag">tutorial</a></span> <span style="display:none" class="updated">2015-06-21</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name">
    
