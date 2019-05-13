---
Tutorial &#8211; How To Run a Full Ethereum Node On Windows
---
<article class="post-listing post-20103 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-ethereum tag-full tag-node tag-run tag-tutorial tag-windows">
    
    <div class="post-inner">
    
    
    <p class="post-meta">
    
    <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    
    
    <span>May 25, 2017</span>
    <span>in <a href="https://www.deepdotweb.com/category/articles/" rel="category tag">Articles</a>, <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a></span>
    
    <span><a href="https://www.deepdotweb.com/2017/05/25/tutorial-run-full-ethereum-node-windows/#comments">6 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    <div class="entry">
    
    <p>Ethereum is one of the most important blockchains present today, not only because it represents another cryptocurrency, but also because Ethereum is technically a &#8220;world computer&#8221; that unifies the processing power of the network&#8217;s public nodes. Ethereum&#8217;s &#8220;world computer&#8221;, or the Ethereum virtual machine (EVM), can be used by peers across the network to execute smart contracts.</p>
    <p>Ethereum&#8217;s platform was launched in 2016, so it is literally still in its infancy. In my opinion, ethereum is currently undervalued and I won&#8217;t be surprised if Ethereum&#8217;s price surpassed that of bitcoin during the upcoming few years.</p>
    <p>Throughout this article, I will present you with an easy-to-follow guide to help you set up an ethereum node.</p>
    <p><strong>Geth and Eth:</strong></p>
    <p>Before setting up your Ethereum node, there are two important pieces of software that you have to know about; Geth and Eth.</p>
    <p>Geth and Eth are two separate command line tools that can run a full Ethereum , public or private, node. Both software provide multiple user interfaces; the command line interface, an interactive console and a JSON-RPC server.</p>
    <p><strong>Running Ethereum Node via Installing and Running Geth:</strong></p>
    <p>When you install and run geth, you can participate in ethereum&#8217;s frontier live network:</p>
    <ul>
    <li>Mine ether</li>
    <li>Initiate ether transactions from an address to the other</li>
    <li>Create and execute smart contracts</li>
    <li>Monitor block history</li>
    </ul>
    <p>1. All Geth&#8217;s versions are available for download at: https://geth.ethereum.org/downloads/</p>
    <p>For every version, an archive (.zip file) as well as an installer (.exe) package are available for download. The installer package will put geth automatically into your PATH, while the archive includes the command .exe files, so that they can be used without installation.</p>
    <p>For the purpose of this tutorial, we will install the Geth 1.6.1 release. Press on the Geth 1.6.1 installer link, as shown on the below screenshot and download the .exe file.</p>
    <p><img class="wp-image-20116 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-89.png" width="719" height="369" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-89.png 1365w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-89-300x154.png 300w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-89-1024x526.png 1024w" sizes="(max-width: 719px) 100vw, 719px" /></p>
    <p>2. Press &#8220;I Agree&#8221; to accept the license agreement and start the installation process.</p>
    <p><img class="wp-image-20117 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-90.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-90.png 436w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-90-300x205.png 300w" sizes="(max-width: 436px) 100vw, 436px" /></p>
    <p>3. You will be prompted to choose whether or not to install Ethereum&#8217;s development tools in addition to Geth. For the purpose of this tutorial, we will install only Geth, so keep the box of &#8220;Development tools&#8221; unchecked.</p>
    <p><img class="wp-image-20118 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-91.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-91.png 434w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-91-300x208.png 300w" sizes="(max-width: 434px) 100vw, 434px" /></p>
    <p>4. You will then be prompted to choose the destination folder for your installation. By default, the program will be installed under C:\Program Files\Geth</p>
    <p><img class="wp-image-20119 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-92.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-92.png 431w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-92-300x207.png 300w" sizes="(max-width: 431px) 100vw, 431px" /></p>
    <p>5. The installation process will be completed, press &#8220;close&#8221; to exit the installation window.</p>
    <p><img class="wp-image-20120 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-93.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-93.png 434w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-93-300x207.png 300w" sizes="(max-width: 434px) 100vw, 434px" /></p>
    <p>6. Now, open a &#8220;command prompt&#8221; instance, via pressing the Windows button and typing &#8220;command prompt&#8221;. Press on the program&#8217;s icon that will appear.</p>
    <p>7. Now, change the directory to the directory where Geth is installed , via the &#8220;chdir&#8221; command, so as we installed Geth onto the &#8220;Program Files&#8221; directory, we will type the following onto the command prompt&#8217;s instance:</p>
    <p>Chdir C:\Program Files\Geth</p>
    <p>8. Now, type Geth onto the command prompt instance, after changing the directory and the client will start up and begin connecting to peers, as shown on the below screenshot:</p>
    <p><img class="wp-image-20121 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-94.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-94.png 675w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-94-300x152.png 300w" sizes="(max-width: 675px) 100vw, 675px" /></p>
    <p>Congratulations, you are now running a full ethereum node, and receiving blocks as shown on the above screenshot.</p>
    <p><strong>Running an Ethereum Node via Installing and Running Ethereum&#8217;s Mist Wallet:</strong></p>
    <p>You can also run a full ethereum node via installing and running ethereum&#8217;s mist wallet client, which will also help you create addresses, send and receive transactions in a simple way. Here is how:</p>
    <p>1. Browse to the <a href="https://github.com/ethereum/mist/releases">download page of the latest release of the mist wallet</a>. For this tutorial, we will download and install the 0.8.10 version, which is the most stable version and has the following features:</p>
    <ul>
    <li>It features a brand new sidebar that gives users more room to browse and presents Dapps in an attractive, simple to use way.</li>
    <li>An annoying bug that made tabs vanish for some users is successfully fixed.</li>
    <li>Better validation for password strengths when users create their accounts. As per this version, passwords should at least have 8 characters.</li>
    <li>Fixed problems associated with wallet importing.</li>
    </ul>
    <p>2. After downloading mist&#8217;s archive, unzip it and then double click on the mist .exe file to start the installation procedure.</p>
    <p>3. Accept the license agreement by clicking &#8220;I agree&#8221; to start the installation procedure.</p>
    <p><img class="wp-image-20122 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-95.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-95.png 431w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-95-300x207.png 300w" sizes="(max-width: 431px) 100vw, 431px" /></p>
    <p>4. You will now be prompted to choose the destination folder for installation of the mist wallet and downloading the blockchain. Note that the blockchain is now almost 30 GB in size, so I recommend using a folder with at least 35 GB of free space.</p>
    <p><img class="wp-image-20123 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-96.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-96.png 430w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-96-300x209.png 300w" sizes="(max-width: 430px) 100vw, 430px" /></p>
    <p>5. When installation is complete, press the &#8220;close&#8221; button to exit the installation wizard, as shown on the below screenshot.</p>
    <p><img class="wp-image-20124 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-97.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-97.png 430w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-97-300x207.png 300w" sizes="(max-width: 430px) 100vw, 430px" /></p>
    <p>6. After completion of installation, double click the &#8220;mist&#8221; icon in your installation folder to launch the wallet. You will be prompted to choose one of two options:</p>
    <p>a. Use the test network:</p>
    <p>If you choose this option, you will not connect to ethereum&#8217;s network. Instead, you can connect to a sandboxed test network to try the technology without using real ethereum.</p>
    <p>b. Use the main network:</p>
    <p>By choosing this option, you will connect to ethereum&#8217;s network and be able to run a full node, send and receive ethereum payments.</p>
    <p>So, to run a full ethereum node, choose the &#8220;use the main network&#8221; option.</p>
    <p><img class="wp-image-20125 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-98.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-98.png 590w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-98-300x244.png 300w" sizes="(max-width: 590px) 100vw, 590px" /></p>
    <p>7. You will now be prompted, to choose whether or not to import a wallet that you have created before, as shown on the below screenshot. Press &#8220;skip&#8221; to move on to the next steps.</p>
    <p><img class="wp-image-20126 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-99.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-99.png 589w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-99-300x242.png 300w" sizes="(max-width: 589px) 100vw, 589px" /></p>
    <p>8. Now, you will be asked to create a password for your account to secure it. By default, you will have to create a password of at least 8 characters. I recommend using at least 16 characters for your password, especially if you intend to use your ethereum node to send and receive transactions. Use a mixture of uppercase letters, lowercase letters, special characters and numbers. Even better, use a randomly generated password using services like passwordsgenerator.net.</p>
    <p>After creating your password, you will reminded to save your password and keyfiles, before moving on to the next steps. Save your keyfiles, which are present in the &#8220;keystore&#8221; folder (under the installation directory), in a safe place e.g. USB drive, cloud drive&#8230;.etc. The &#8220;keyfiles&#8221; folder can be found by pressing main menu -&gt; backup -&gt; accounts on the wallet&#8217;s main interface.</p>
    <p><img class="wp-image-20127 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-100.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-100.png 585w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-100-300x242.png 300w" sizes="(max-width: 585px) 100vw, 585px" /></p>
    <p>9. Now, your wallet is ready to start, press the &#8220;Launch the Application&#8221; button on the window that will appear and the wallet &#8216;s interface will show up. Note, that the blockchain will continue downloading in the background.</p>
    <p>The below screenshot shows how the wallet&#8217;s overview window looks like</p>
    <p><img class="wp-image-20128 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-101.png" width="674" height="394" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-101.png 1227w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-101-300x175.png 300w, https://www.deepdotweb.com/wp-content/uploads/2017/05/word-image-101-1024x598.png 1024w" sizes="(max-width: 674px) 100vw, 674px" /></p>
    <p>On the top of the wallet&#8217;s overview window, you will be able to see information related to the synchronization status of your ethereum node. Whenever the node stops synchronizing (e.g. no peers, or the number of blocks doesn&#8217;t change), try to exit and then restart your wallet or just wait for a few minutes.</p>
    <p>As shown on the above screenshot, you can see your wallet&#8217;s main address under the &#8220;main account&#8221; (etherbase) section. You can also use your wallet to create smart contracts, but you will have to have at least one ether to be able to do that. Note that wallets represent a form of a basic smart contract, that allows your coins to be controlled by more than one account and can optionally enable you to put a limit on daily withdrawals, to maximize security. You can create your very own customized smart contracts via the &#8220;contracts&#8221; tab.</p>
    <p>This was a concise tutorial to guide you through running a full ethereum node using Geth or the Mist wallet. Running an ethereum node will be a good way to introduce you to the world of ethereum and smart contracts. If you have any questions, I will be glad to answer them; just post them in the comments&#8217; section below and I will answer them right away.</p>
    
    
    </div><!-- .entry /-->
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/ethereum/" rel="tag">Ethereum</a> <a href="https://www.deepdotweb.com/tag/full/" rel="tag">full</a> <a href="https://www.deepdotweb.com/tag/node/" rel="tag">node</a> <a href="https://www.deepdotweb.com/tag/run/" rel="tag">run</a> <a href="https://www.deepdotweb.com/tag/tutorial/" rel="tag">tutorial</a> <a href="https://www.deepdotweb.com/tag/windows/" rel="tag">windows</a></span>				<span style="display:none" class="updated">2017-05-25</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    
    
    </div><!-- .post-inner -->
</article><!-- .post-listing -->

