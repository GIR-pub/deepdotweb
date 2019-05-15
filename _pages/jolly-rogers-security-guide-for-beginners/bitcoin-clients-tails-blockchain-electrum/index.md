---
title: "BITCOIN CLIENTS IN TAILS &#8211; BLOCKCHAIN AND ELECTRUm"
sidebar:
  - title: "Jolly Rogers Security Guide"
    nav: "jolly"
  - title: "Security Tutorials"
    nav: "security"
  - title: "Blog Archive"
    nav: "blognav"
---


<p>In this post I want to talk about 2 options for trading your Bitcoins.<br/>
#1 &#8211; Blockchain<br/>
#2 &#8211; Electrum</p>
<p>By now, hopefully you know how to use BlockChain. If not, you simply go to http://blockchain.info and press the button &#8220;Wallet&#8221; and you can open up your existing wallet or create a new account. Very straight forward and can be done all from your web browser.</p>
<p>But what about Electrum? Electrum is an easy to use Bitcoin client. It protects you from losing coins in a backup mistake or computer failure, because your wallet can be recovered from a secret phrase that you can write on paper or learn by heart. There is no waiting time when you start the client, because it does not download the Bitcoin blockchain. If you use the normal Bitcoin client from https://bitcoin.org then you would need to download the entire blockchain, which is several GB of data. In Tails, we are trying not to download too much to our computers. Downloading the entire BlockChain can take over 24 hours.</p>
<p>So how do we set up Electrum in Tails? First thing we need to do is download it.</p>
<p><strong>https://download.electrum.org/Electrum-1.9.7.tar.gz</strong></p>
<p>Now extract it (right click -&gt; Extract here) and rename the folder to electrum to make things easier. (Right click -&gt; Rename). You might also want to move the folder to the <strong>tmp</strong> directory so it is easier to find. (Places -&gt; Computer -&gt; File System -&gt; tmp)</p>
<p>Next open up a terminal and type the following command</p>
<p><strong>cd /tmp/electrum </strong></p>
<p>You can replace /tmp/electrum with whatever directory electrum is currently in, but this is why we put it in tmp, to make things easier for us. Next type the following command.</p>
<p><strong>./electrum -s 56ckl5obj37gypcu.onion:50001:t -p socks5:localhost:9050</strong></p>
<p>This will allow your electrum to connect through Tor, to make sure it does not connect over clearnet. You will get a warning when you do this that electrum is attempting to connect in an unsafe manner, but this is expected, and do not worry, it is safe to do this. This step was recommended on the Tails web page at the following URL.</p>
<p><strong>https://tails.boum.org/forum/Report:_the_electrum_bitcoin_client_in_tails/</strong></p>
<p>Since you are likely going to want to reuse your wallet that is generated in Electrum, you can specify where your wallet is kept by replacing the above command with the following command.</p>
<p><strong>./electrum -s 56ckl5obj37gypcu.onion:50001:t -p socks5:localhost:9050 -w /tmp/electrum.dat</strong></p>
<p>You would replace /tmp/electrum.dat with whatever the path to your wallet is, and you can rename <strong>electrum.dat</strong> to whatever you want to call your wallet, like <strong>srwallet.dat</strong> or whatever you want. Or leave it the way that it is. Then each time you want to start up electrum, reuse the same command, and make sure you copy electrum.dat into <strong>/tmp</strong> or whatever directory you wish to use. Then when you are finished, make sure to back up electrum.dat onto your USB drive or SD card, especially if you do not have Tails persistence. This way you can reuse the same wallet and you will not lose your balance.</p>
<p>Electrum is likely going to be the Bitcoin client of choice for Tails users. And you can read more about how to use Electrum by visiting the home page at the following link.</p>
<p>https://electrum.org</p>

Updated: 2014-02-22

