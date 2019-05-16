---
title: "In-depth Guide to Tails + Persistence"
---

Posted by: DeepDotWeb 

<span>June 5, 2015</span>
    

<p>Here&#8217;s an easy to follow noobs guide to Tails. Tails is by no means just a noobs OS, it does a lot of the hard work for you and makes connecting to and browsing the .onion network easy as hell. <strong><a href="http://www.wired.com/2014/04/tails/">Edward Snowden used it</a></strong> to help stay anonymous during the initial NSA spying leaks. We&#8217;ll go over verifying the ISO, installing to USB, setting up persistence, and setting up the environment. For this guide we&#8217;ll be using Linux Mint as our operating system. Most steps will be the same across operating systems.</p>
<p><strong>#What we&#8217;ll need</strong></p>
<ul>
<li>Flash drive, minimum of 4GB</li>
<li>Host OS (your computer)</li>
<li>Guest OS (Tails .iso file)</li>
<li>Virtualbox and Virtualbox Extensions</li>
<li>PGP knowledge</li>
</ul>
<p><strong>Part 1 – Installing Virtualbox and Extensions</strong></p>
<p>Unlike the other methods this one only requires one flash drive. We&#8217;ll be booting the live Tails system on Virtualbox, and installing it to the USB stick from there. The interface in the pictures may look a little different from what you see, but all of the options are in the same places.</p>
<p><strong>#Virtualbox</strong></p>
<p>Virtualbox allows you to run other operating systems on top of your current one, kind of like an emulator. This is what we&#8217;ll be using to boot Tails so we wont have to reboot during the install. Head over to the <strong><a href="http://www.oracle.com/technetwork/server-storage/virtualbox/downloads/index.html#vbox">download page</a></strong> and select the download appropriate for your current OS.</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails002.png">

<p>After downloading, install it like you would any other program. Open it up and you should see the following screen.</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails003.png">

<p><strong>#Virtualbox Extensions</strong></p>
<p>This is what will allow the USB stick to communicate with our guest OS, which will allow us to install the live system without needing to reboot. Go to the <strong><a href="http://www.oracle.com/technetwork/server-storage/virtualbox/downloads/index.html#extpack">download page</a></strong>, and download the extension pack for the most recent version. When it&#8217;s finished downloading, double click it to open it with Virtualbox.</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails004.png">

<p>The above should appear. Click install, follow through with the install process. If successful you should see the following window appear.</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails005.png">

<p>We&#8217;re done with Virtualbox for now. We&#8217;ll come back to it later when setting up the virtual machine.</p>
<p><strong>Part 2 – Downloading and verifying Tails</strong></p>
<p>We need to download the Tails .iso file, and verify that it&#8217;s authentic. Tails, or The Amnesic Incognito Live System, is a GNU/Linux distro with a focus on anonymity and privacy. It does this by routing all traffic through the Tor network, deletes all files on shutdown unless explicitly asked not to (persistence storage), and comes with all the other tools you need. Persistant storage will be needed for saving our wallet and keypairs.</p>
<p>If you want to know more check out the <strong><a href="https://tails.boum.org/about/index.en.html">&#8216;About&#8217; page</a></strong>, and it would also be a good idea to read over the <strong><a href="https://tails.boum.org/doc/about/warning/index.en.html">&#8216;Warning&#8217; page</a></strong> to get a better idea about what Tails can and cannot do.</p>
<p><strong>#Downloading</strong></p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails006.png">

<p>Next you&#8217;re going to want to download the &#8216;signing key&#8217; from <strong><a href="https://tails.boum.org/download/index.en.html#verify">this link</a></strong>. Import the key into your PGP program of choice. We&#8217;ll be verifying the .iso by checking the PGP signature. If you don&#8217;t know how to use PGP, check out the guides we have for <strong><a href="/2015/02/17/basic-guide-pgp-linux/">GNU/Linux</a></strong>, <strong><a href="/2015/02/20/pgp-tutorial-os-x/">OS X</a></strong>, and <strong><a href="/2015/02/21/pgp-tutorial-for-windows-kleopatra-gpg4win/">Windows</a></strong>.</p>
<p><strong>#Verifying</strong></p>
<p>Verifying the ISO is an important step. We want to make sure what we&#8217;re getting is actually from the Tails project. Like the intro said, we&#8217;ll be using the command line in Linux Mint . If you&#8217;re using Windows or OS X check out <strong><a href="https://tails.boum.org/download/index.en.html#index3h1">this link for instructions</a></strong>.</p>
<p>First we need to import the Tails signing key. Change into the directory where you saved it, then import the key into GPG. Once it&#8217;s imported, the output from gpg should reflect that. Take a look at the below picture to make sure you did this step right. If you get an error saying “gpg: no ultimately trusted keys found” this means that you haven&#8217;t created your own keypair yet. This is fine just for verifying the .iso file, you can ignore it.</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails009.png">


<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails010.png">

<p><strong>Part 3 – Booting the .iso</strong></p>
<p>Now that we&#8217;ve confirmed the .iso is genuine we can install it on the USB stick.</p>
<p><strong>#Creating the virtual machine</strong></p>
<p>Open up VirtualBox and plug in your USB stick. The first thing you&#8217;re going to do is click where it says &#8216;New&#8217; in the top left corner, which should open a window titled &#8216;Create Virtual Machine&#8217;. Create a name, select &#8216;Linux&#8217; as type, and version as &#8216;Linux 2.6 / 3.x (32 bit). See picture for an example.</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails011.png">

<p>The next screen will ask if you want to reate a virtual hard drive. Since we&#8217;ll be booting the .iso directly, there&#8217;s no need to create a hard drive. So click &#8216;Do not add virtual hard drive&#8217;, then click &#8216;Create&#8217;.</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails012.png">


<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails013.png">

<p>In order for Tails to boot properly and recognize the USB stick we need to edit some settings. Click on the virtual machine, then click &#8216;Settings&#8217; up at the top. The following window should appear.</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails014.png">


<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails015.png">


<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails016.png">


<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails017.png">


<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails018.png">

<p><strong>Part 4 – Tails on USB</strong></p>
<p><strong>#Installing</strong></p>
<p>I hope you aren&#8217;t bored yet, we&#8217;re almost done. Click on &#8216;Applications&#8217;, then &#8216;Tails&#8217;, then &#8216;Tails Installer&#8217;. You&#8217;ll see the following window. Click on &#8216;Clone &amp; Install&#8217;, and you should see something like the second picture.</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails019.png">

<p>Your USB drive should already be selected for the &#8216;Target Device&#8217;, if not do so. Then click &#8216;Install Tails&#8217;. It will confirm that you want to install Tails on the USB drive. Do so, then click &#8216;Yes&#8217;. This will take several minutes, and you&#8217;ll be able to see what part the installer is at during the process. Once finished, a pop up will appear reflecting such. Click &#8216;OK&#8217; to close the installer.</p>
<p>Tails is now installed on the USB drive. The last thing we need to do is configure it.</p>
<p><strong>#Configuring</strong></p>
<p>In order to do this you&#8217;ll need to boot your computer from USB. Close the virtual machine, and reboot your computer. You&#8217;ll need to change the boot order of the connected devices, the key that needs to be pressed on boot will be different across manufacturers. It&#8217;s usually listed on the BIOS splash screen on reboot. If not, consult your computers manual or do a search for which key needs to be pressed on boot. You may also need to disable Secure Boot if you&#8217;re using Win8, 8.1, or 10. Check out <strong><a href="http://www.maketecheasier.com/disable-secure-boot-in-windows-8/">this link</a></strong> for more info on that.</p>
<p>Follow the same steps as above. Select &#8216;Live System&#8217;, then keep &#8216;No&#8217; highlighted and click &#8216;Login&#8217;. You&#8217;ll now be at the Tails desktop.</p>
<p>The first thing we&#8217;ll do is set up persistent storage. This will take up the rest of the free space on your USB drive. Go to &#8216;Applications&#8217;, &#8216;Tails&#8217;, then click &#8216;Configure persistent volume&#8217;. The following window should appear. You&#8217;ll want to create a strong password, confirm it, then click &#8216;Create&#8217;. This will take several minutes.</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails021.png">


<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails022.png">


<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails023.png">


<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/03/tails024.png">

<p>To access the internet through the Tor network, just click on the green globe icon on the left of the system tray. You will also want to disable scripts globally, which you can do by clicking on the NoScript icon to the left of the URL bar. There is also a so-called &#8216;Unsafe Web Browser&#8217; which you can use if you need to get on a website that doesn&#8217;t allow Tor connections. You can find that by going to &#8216;Applications&#8217; then &#8216;Internet&#8217;.</p>
<p><strong>#Bitcoin Wallet</strong></p>
<p>Tails uses Electrum as the default wallet, this can be found under &#8216;Internet&#8217; in the &#8216;Applications&#8217; menu. When creating the wallet make sure to back up your seed in a safe place, this is the only way you can recover a lost wallet. Writing it down on a piece of paper is a good idea.</p>
<p><strong>#PGP</strong></p>
<p>Tails uses GnuPG for PGP, and Seahorse as a graphical front-end. This can be found by going to &#8216;Applications&#8217;, &#8216;System Tools&#8217;, &#8216;Preferences&#8217;, then &#8216;Passwords and Keys&#8217;. It will also work just fine from the command line.</p>
<p><strong>Part 5 – Conclusion</strong></p>
<p>Congratulations! If you&#8217;ve followed this guide you now have an anonymous and secure operating system for browsing the dark web. There are a few more things to Tails such as Pidgin+OTR messaging, Claws Mail, and a metadata anonymization toolkit, but those are beyond the basics. If you want to learn more check out the documentation at <strong><a href="https://tails.boum.org/doc/index.en.html">https://tails.boum.org/doc/index.en.html</a></strong>.</p>
<p>Thanks to our skilled tutorials master <a href="http://www.reddit.com/user/MLP_is_my_OPSEC">@MLP_is_my_OPSEC</a> :)</p>

Updated: 2015-06-05

