---
Tutorial &#8211; How To Start a Full Bitcoin Node On Windows
---
<article class="post-listing post-19632 post type-post status-publish format-standard has-post-thumbnail hentry  tag-bitcoin tag-full tag-node tag-start tag-tutorial tag-windows">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>May 5, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/05/05/tutorial-start-full-bitcoin-node-windows/#comments">4 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    <p>As the present happenings seem to be taking us to an almost inevitable bitcoin hard fork, it is pivotal now to point out to bitcoin enthusiasts, that running a full node today will have positive influence on the bitcoin ecosystem during the upcoming critical period in the history of bitcoin.</p>
    <p>As an experienced bitcoiner, I would recommend starting a full bitcoin node via running the traditional Bitcoin Core Client. Keep away from Bitcoin Unlimited (BU), if you plan on running a full node, as until now, two major bugs have been discovered in its code; <a href="https://twitter.com/juscamarena/status/841798037252919296">one of them was exploited by a malicious user</a> which allowed him to take down a large number of Bitcoin Unlimited (BU) nodes. Another bug was discovered which led to mining of an <a href="https://live.blockcypher.com/btc/block/000000000000000000cf208f521de0424677f7a87f2f278a1042f38d159565f5/">invalid block</a> whose size was larger than 1 MB. Moreover, I would not trust any solution that receives support from <a href="https://bitcointalk.org/?topic=6652.0">Gavin Andersen; the guy who helped seed the bitcoin community with birdwatchers</a>.</p>
    <p>The number of Bitcoin Core full nodes and that of Bitcoin Unlimited will determine the outcome of the hard fork, if it ever happens, and will also dictate the percentage of coins on each of the yielded child chains. After the recent discovery of the Bitcoin Unlimited bugs, the number of BU full nodes declined dramatically and today, more than 85% of all full nodes on the bitcoin network are Bitcoin Core nodes.</p>
    <p>Throughout this tutorial, I will show you how to setup a full bitcoin node on Windows, but let&#8217;s start by understanding what a full node is:</p>
    <p><strong>What is a Full Bitcoin Node?</strong></p>
    <p>A full bitcoin node is a piece of software that validates generated blocks and transactions. Full nodes also support the network via verifying blocks and transactions from other full nodes, validating these blocks and transactions, and then relaying, or routing, them to other full nodes across the network.</p>
    <p>On the other hand, the greater portion of full nodes acts as lightweight bitcoin clients which enable users to broadcast their transactions to the network and also notify them when transactions are sent to their wallets. If there is no sufficient number of full nodes to play this role, clients would not have the ability to connect via the peer-to-peer (P2P) network; they will have to rely on centralized wallet services instead.</p>
    <p>Many bitcoin enthusiasts donate their spare computing power and bandwidths to run full nodes, yet more nodes are still indispensable if bitcoin is to be adopted on a massive global scale.</p>
    <p><strong>Minimum system requirements:</strong></p>
    <p>There are minimum requirements for running a Bitcoin Core full node. If you attempt running your node using weaker hardware, it might work, but it will be rather slow. The following are the minimum system requirements for running a Bitcoin Core full node, according to info from Bitcoin.org:</p>
    <ul>
    <li>A Windows 7 OS or later versions.</li>
    <li>125 GB of free hard disk space.</li>
    <li>2 GB of RAM.</li>
    <li>An internet connection with an upload speed of at least 400 kilobits/second.</li>
    <li>An internet connection with unrestricted uploads. Usually, full nodes run using high speed internet connections, upload around 200 GB of data per month, yet download usage is usually around 20 GB per month, in addition to around 100 GB the first time you run your node (this amount represents the whole blockchain).</li>
    <li>You have to leave your full node running for at least 6 hours per day, yet more time is always better and best of all is to keep it running 24/7.</li>
    </ul>
    <p>&nbsp;</p>
    <p><strong>Installing Bitcoin Core:</strong></p>
    <p>This will explain how to install Bitcoin Core 0.13.1 on Windows 8.</p>
    <p>1. Point your browser to the <a href="https://bitcoin.org/en/download">official page for downloading Bitcoin Core</a> and verify that your connection is secure (via seeing a padlock on the left side of the address bar).</p>
    <p><img class="wp-image-19640 aligncenter" src="/imgs/2017/05/word-image-6.png" srcset="/imgs/2017/05/word-image-6.png 413w, /imgs/2017/05/word-image-6-300x214.png 300w" sizes="(max-width: 413px) 100vw, 413px" /></p>
    <p>2. Click the blue &#8220;Download Bitcoin Core&#8221; button to start downloading the installer.</p>
    <p>3. After the download if complete, run it as the system&#8217;s administrator, by right clicking the installer&#8217;s icon and choosing the &#8220;run as administrator&#8221; option. The installer will ask you about your destination installation folder, I recommend using the default destination folder.</p>
    <p><img class="wp-image-19641 aligncenter" src="/imgs/2017/05/word-image-7.png" srcset="/imgs/2017/05/word-image-7.png 502w, /imgs/2017/05/word-image-7-300x232.png 300w" sizes="(max-width: 502px) 100vw, 502px" /></p>
    <p>4. To continue on, you will have to choose one of two options:</p>
    <p>i. Use the Bitcoin Core Graphical User Interface (GUI).</p>
    <p>ii. Use the Bitcoin Core daemon (bitcoind), which would be an ideal option, especially if you are an advanced user or a coder.</p>
    <p>For the sake of this tutorial, I will show you only how to set up a full node via installing the Bitcoin Core GUI.</p>
    <p>Installing the Bitcoin Core GUI:</p>
    <p>1. Press the Windows button, on the bottom right corner of your Windows 8 desktop screen and then type &#8220;bitcoin&#8221; in the search box. The Bitcoin Core icon will show up, so click on it.</p>
    <p>2. A prompt screen will appear asking you to select a directory for storing bitcoin&#8217;s blockchain and your wallet&#8217;s data. I recommend using the default destination folder, but you can store both wherever you want on your machine&#8217;s hard disk.</p>
    <p>3. Occasionally, your Windows firewall will block Bitcoin Core from creating outbound connections. Allow the client to communicate on all networks; it is safe. Note that you still need to set configurations for inbound connections, as we will explain later on.</p>
    <p><img class="wp-image-19642 aligncenter" src="/imgs/2017/05/word-image-8.png" srcset="/imgs/2017/05/word-image-8.png 540w, /imgs/2017/05/word-image-8-300x215.png 300w" sizes="(max-width: 540px) 100vw, 540px" /></p>
    <p>4. The Bitcoin Core GUI will now start downloading the blockchain. This will usually take a few days, yet it may take much more time if you are using a slow internet connection or a slow machine. The client will use the most of your connection&#8217;s bandwidth during the download process, yet you can stop it at any time by closing it; it will continue on the download process from where it stopped the next time you run it.</p>
    <p><img class="wp-image-19643 aligncenter" src="/imgs/2017/05/word-image-9.png" srcset="/imgs/2017/05/word-image-9.png 623w, /imgs/2017/05/word-image-9-300x204.png 300w" sizes="(max-width: 623px) 100vw, 623px" /></p>
    <p>5. After the whole blockchain is downloaded successfully, you can use it as your bitcoin wallet, or just leave it running to support the bitcoin network. Congratulations, you are now running a full bitcoin node.</p>
    <p>6. Optionally, you can set your node to start automatically each time you start your computer, which renders it easy to start supporting the bitcoin network. After running the Bitcoin Core GUI, click on the &#8220;Settings&#8221; button on the top bar and then choose &#8220;Options&#8221;. As shown on the below screenshot, click on the &#8220;Main&#8221; tab and then click the checkbox marked &#8220;Start Bitcoin on system login&#8221;, then click the Ok button in order to save your new settings. Now, the next time you start Windows, the client will automatically run minimized in your desktop&#8217;s task bar.</p>
    <p><img class="wp-image-19644 aligncenter" src="/imgs/2017/05/word-image-10.png" srcset="/imgs/2017/05/word-image-10.png 574w, /imgs/2017/05/word-image-10-300x228.png 300w" sizes="(max-width: 574px) 100vw, 574px" /></p>
    <p><strong>Important Note: </strong>To prevent data loss or corruption, never force system shutdown via the Windows shutdown screen, whenever the Bitcoin Core GUI client is running.</p>
    <p><strong>Network Configuration:</strong></p>
    <p>To support bitcoin&#8217;s network, you have to allow inbound connections. When Bitcoin Core GUI runs, it creates 8 outbound connections with other full nodes, in order to download the latest transactions and blocks. If you want to just use your full node as a bitcoin wallet, you needn&#8217;t more than these 8 connections, yet if you aim at supporting other full nodes and lightweight clients across the network, you have to allow inbound connections.</p>
    <p>Servers with direct connections to the internet won&#8217;t usually need any special network configurations. You can just refer to the testing instructions below to make sure that your server based full node allows inbound connections. On the other hand, home connections usually have connection restrictions via a modem or a router. Bitcoin Core GUI will require your router to configure itself automatically to allow inbound internet connections on port 8333; bitcoin&#8217;s port. However, some routers don&#8217;t permit automatic configuration, so you have to manually allow inbound connections to port 8333 on your router and firewall.</p>
    <p><strong>Testing Connections:</strong></p>
    <p>BitNodes offers an online tool that allows you to test whether or not your full node allows inbound connections. To use this tool, run the Bitcoin Core GUI client, leave it running for 10 minutes, then visit <a href="https://bitnodes.21.co/#join-the-network">the service&#8217;s page</a>. The tool will try to automatically detect your IP address, yet if it can&#8217;t guess it, you will need to enter it manually., as shown on the below screenshot.</p>
    <p><img class="wp-image-19645 aligncenter" src="/imgs/2017/05/word-image-11.png" srcset="/imgs/2017/05/word-image-11.png 637w, /imgs/2017/05/word-image-11-300x84.png 300w" sizes="(max-width: 637px) 100vw, 637px" /></p>
    <p>Now, press the &#8220;Check Node&#8221; button and the tool will prompt you whether the tested port is open (green box) or closed (red box). If you are prompted with a green box, you are set and you have confirmed that you are accepting inbound connections. If you are prompted with a red box, then you have to recheck your router&#8217;s and firewall&#8217;s settings.</p>
    <p>You can use Bitcoin Core GUI to confirm that you are actively accepting inbound connections. Bitcoin Core GUI cannot inform you directly whether or not you are accepting inbound connections, yet it can inform you whether or not you have any active inbound connections in real time. If your full node has been running for at least 30 minutes, then it will definitely have established inbound connections.</p>
    <p>This was a concise tutorial that will help you start a full bitcoin node. I will be glad to answer your questions, if you have any. Just add them in the comments&#8217; section below.</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/bitcoin/" rel="tag">bitcoin</a> <a href="https://www.deepdotweb.com/tag/full/" rel="tag">full</a> <a href="https://www.deepdotweb.com/tag/node/" rel="tag">node</a> <a href="https://www.deepdotweb.com/tag/start/" rel="tag">start</a> <a href="https://www.deepdotweb.com/tag/tutorial/" rel="tag">tutorial</a> <a href="https://www.deepdotweb.com/tag/windows/" rel="tag">windows</a></span> <span style="display:none" class="updated">2017-05-05</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    
