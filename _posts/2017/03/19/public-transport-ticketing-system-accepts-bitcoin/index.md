---
A Public Transport Ticketing System That Accepts Bitcoin"
---
<article class="post-listing post-18686 post type-post status-publish format-standard has-post-thumbnail hentry 
tag-accepts tag-bitcoin tag-public tag-system tag-ticketing tag-transport">
<div class="post-inner">
<span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
<span>March 19, 2017</span>

<span><a href="https://www.deepdotweb.com/2017/03/19/public-transport-ticketing-system-accepts-bitcoin/#respond">Leave a comment</a></span>


<p>In many parts of the world today, public transportation is faced by the problem of seemingly inconvenient ticketing processes. Bitcoin is a decentralized currency that can easily solve such problem. <a href="https://www.researchgate.net/profile/Nian_Xue/publication/311789715_Enable_Bitcoin_Transcation_in_Public_Transport_Ticketing_System/links/585a95f508ae3852d2571eb9/Enable-Bitcoin-Transcation-in-Public-Transport-Ticketing-System.pdf">A group of developers from Liverpool University proposed a novel ticketing system for public transportation</a>, which is comprised of an automatic ticketing vending machine that supports bitcoin payments. An essential part of this ticketing system is a <a href="https://www.deepdotweb.com/2017/01/05/hardware-wallets-keep-friends-close-bitcoins-closer-kptx/">bitcoin hardware wallet</a>, which records private keys and their matching public keys throughout bitcoin transaction processes. The developers created a demo ticketing vending machine and experimented it to prove the performance and feasibility of the ticketing system.</p>
<p><strong>System Architecture:</strong></p>
<p>As shown in the below figure, the proposed ticketing system is divided into two parts: the main processor and the bitcoin transaction module:</p>
<p>1. The main processor is comprised of modules to manage fiat money payments and deliver tickets, in addition to a user interface module.</p>
<p>2. The bitcoin transaction module enables bitcoin payments and is comprised of a bitcoin wallet, an ECC chip and a secondary processor.</p>
<p>3. ECC chip represents an encryption chip of the Atmel ATECC108 model, that is utilized to manage bitcoin transactions.</p>
<p>4. The secondary processor is controlled by the primary processor and handles the process of tickets&#8217; delivery.</p>
<p><img class="wp-image-18690 aligncenter" src="/imgs/2017/03/public-1-png.png" alt="Public 1.PNG" srcset="/imgs/2017/03/public-1-png.png 614w, /imgs/2017/03/public-1-png-300x243.png 300w" sizes="(max-width: 614px) 100vw, 614px" /></p>
<p><strong>Wallet Generation:</strong></p>
<p>Throughout the transaction process, the ticketing vending machine firstly creates pairs of public keys and their matching private keys. One of those is the RSA algorithm to cipher and decipher transaction related data. The private key is used to digitally sign transaction related info, while the public key acts as an account address that allow others to send their bitcoins.</p>
<p>Throughout the wallet generation process, initially, a random number is picked up to act as the private key for the ECC algorithm. Afterwards, the private key will be encrypted via the AES algorithm, before being stored onto the chip&#8217;s configuration area. Thereafter, the crypto chip can use the NIST standard P256 along with the private key to formulating the public key in the form of a 32 byte X coordinate, in addition to a 32-byte Y coordinate. Following this process, the public key is firstly hashed via SHA256. The results of this last step will also act as the RIPEMD-160 algorithm to formulate the final address.</p>
<p>When a user chooses the destination and the number of tickets wanted, the ticketing vending machine will show a QR code that includes its account address. The user is then required to provide his/her signature formulated by ECDSA algorithm to validate ownership of the coins. After the ticketing machine communicates with the bitcoin network and receives a response, it will deliver tickets.</p>
<p><strong>Performance Analysis:</strong></p>
<p>To evaluate the performance of the process of wallet generation, Arduino board is used along with a crypto shield to stimulate the bitcoin module of the ticketing vending machine to measure the overall performance of the ticketing system. The developers measure the following parameters:</p>
<p>1. Key generation time for the ECC algorithm. For hardware implementation, the crypto chip will set its private keys once the personalization process is finished. Thereafter, it will generate a public key that matches the generated private key and specific NIST standard P256 elliptic curve.</p>
<p>2. AES encryption time to cipher the private keys.</p>
<p>3. SHA256 hash function time.</p>
<p>The Arduino board was connected to the crypto shield via the ATECC108 chip to perform the ECC key generation processes. Both hardware and software implementation times were measured along these two processes. Moreover, other algorithm&#8217;s time durations are also demonstrated in the below table:</p>
<p><img class="wp-image-18691 aligncenter" src="/imgs/2017/03/public-2-png.png" alt="Public 2.PNG" srcset="/imgs/2017/03/public-2-png.png 618w, /imgs/2017/03/public-2-png-300x101.png 300w" sizes="(max-width: 618px) 100vw, 618px" /></p>
<p>According to the table, the ECC key pair generation is the most crucial factor determining the overall performance of the system. When comparing this with the software library approach, the process&#8217;s time duration decreased sharply. Accordingly, hardware represents a better approach due to the fact that it decreases the duration time of the process of key pair generation, which represents more in all software library algorithms. As such, we can safely say that the bitcoin model&#8217;s crypto chip is the most important element that affects the overall performance of the proposed ticketing system.</p>
</div>
<a href="https://www.deepdotweb.com/tag/accepts/" rel="tag">accepts</a> <a href="https://www.deepdotweb.com/tag/bitcoin/" rel="tag">bitcoin</a> <a href="https://www.deepdotweb.com/tag/public/" rel="tag">public</a> <a href="https://www.deepdotweb.com/tag/system/" rel="tag">system</a> <a href="https://www.deepdotweb.com/tag/ticketing/" rel="tag">ticketing</a> <a href="https://www.deepdotweb.com/tag/transport/" rel="tag">transport</a></span> <span style="display:none" class="updated">2017-03-19<a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>

