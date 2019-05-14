---
title: "Darkleaks: Black Market for Secrets"
---
Posted by: DeepDotWeb 

<span>February 4, 2015</span>


<p><iframe width="640" height="360" src="https://vid.me/e/Lfkh" frameborder="0" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen" scrolling="no"></iframe></p>
<div><span style="text-decoration: underline;"> As it was originally published on <a href="https://medium.com/@ZozanCudi/darkleaks-information-blackmarket-1ee5ac28c892">medium.com</a>:</span></div>
<div>
<p id="a776" class="graf--h3"><strong>Sell and buy information anonymously</strong></p>
<p id="d5a1" class="graf--p">Darkleaks is a decentralised blackmarket where you can sell information. It has a mechanism for trustless authentication of documents that are being sold through a novel cryptographic mechanism. The authentication is fair, provably fair. Before paying for the file, a random selection of segments are released chosen by the block chain demonstrating the file’s contents match the leaker’s claim.</p>
<p id="bc69" class="graf--p">The software uses Bitcoin’s block chain to encrypt files which are released when payment is claimed by the leaker. Files are split into segments and encrypted. These segments are unlocked only when the leaker reveals the key by claiming his Bitcoins.</p>
<p id="e761" class="graf--p">There is no identity, no central operator and no interaction between leaker and buyers. We encourage everyone to download Darkleaks now and start building. The code can be <a class="markup--anchor markup--p-anchor" href="https://github.com/darkwallet/darkwallet" target="_blank" rel="nofollow" data-href="https://github.com/darkwallet/darkwallet">found here</a>.</p>
<p class="graf--p"><a href="/imgs/2015/02/1_kz2LBycqsV2PRLwCLFUCUQ1.jpeg"><img class="aligncenter  wp-image-8965" src="/imgs/2015/02/1_kz2LBycqsV2PRLwCLFUCUQ1.jpeg" alt="Darkleaks" width="734" height="459" srcset="/imgs/2015/02/1_kz2LBycqsV2PRLwCLFUCUQ1.jpeg 1120w, /imgs/2015/02/1_kz2LBycqsV2PRLwCLFUCUQ1-300x188.jpeg 300w, /imgs/2015/02/1_kz2LBycqsV2PRLwCLFUCUQ1-1024x640.jpeg 1024w" sizes="(max-width: 734px) 100vw, 734px" /></a></p>
<p id="d866" class="graf--h3"><strong>Unstoppable Leaks</strong></p>
<p id="1626" class="graf--p">We give the world a new scheme for selling information of any type, form or kind. This is a gift for you to stop corruption and challenge power.</p>
<figure id="aebe" class="graf--figure postField--insetLeftImage">
<div class="aspectRatioPlaceholder is-locked">
<div class="aspect-ratio-fill"></div>
<p><img class="graf-image aligncenter" src="https://d262ilb51hltx0.cloudfront.net/max/630/1*FcWO9LXfa6j9JzK3Av40Gg.png" alt="" data-image-id="1*FcWO9LXfa6j9JzK3Av40Gg.png" data-width="630" data-height="249" data-action="zoom" data-action-value="1*FcWO9LXfa6j9JzK3Av40Gg.png" /></div>
</figure>
<p id="390b" class="graf--p">Darkleaks is the best tool to trade any kind of media, information, video, data and documents that have value.</p>
<ul class="postList">
<li id="3c9a" class="graf--li">Hollywood movies</li>
<li id="9574" class="graf--li">Trade secrets</li>
<li id="bd21" class="graf--li">Government secrets</li>
<li id="a309" class="graf--li">Proprietary source code</li>
<li id="afea" class="graf--li">Industrial designs like medicine or defence</li>
<li id="62e9" class="graf--li">Zero day exploits</li>
<li id="e281" class="graf--li">Stolen databases</li>
<li id="c03c" class="graf--li">Proof of tax evasion</li>
<li id="2131" class="graf--li">Military intelligence</li>
<li id="a2da" class="graf--li">Celebrity sex pictures</li>
<li id="a337" class="graf--li">Corruption</li>
</ul>
<p id="e323" class="graf--h3"><strong>Developer Information</strong></p>
<p id="0525" class="graf--h4"><strong>Command line tools</strong></p>
<p id="ab3f" class="graf--p">To get started, install <a class="markup--anchor markup--p-anchor" href="https://github.com/darkwallet/python-obelisk" target="_blank" rel="nofollow" data-href="https://github.com/darkwallet/python-obelisk">python-obelisk</a> and <a class="markup--anchor markup--p-anchor" href="https://github.com/libbitcoin/libbitcoin" target="_blank" rel="nofollow" data-href="https://github.com/libbitcoin/libbitcoin">libbitcoin</a>.</p>
<blockquote id="e053" class="graf--blockquote"><p>git clone <a class="markup--anchor markup--blockquote-anchor" href="https://github.com/darkwallet/darkleaks/" target="_blank" rel="nofollow" data-href="https://github.com/darkwallet/darkleaks/">https://github.com/darkwallet/darkleaks/</a></p></blockquote>
<p id="b7ad" class="graf--p">Follow the instructions in the README.</p>
<p id="8977" class="graf--h4"><strong>Python API</strong></p>
<p id="829a" class="graf--p">The python/ subdirectory contains the Python bindings.</p>
<blockquote id="433a" class="graf--blockquote"><p>import darkleaks</p></blockquote>
<blockquote id="ba12" class="graf--blockquote"><p>source_filename = …</p></blockquote>
<blockquote id="4adf" class="graf--blockquote"><p>number_chunks = 20</p></blockquote>
<blockquote id="ff9e" class="graf--blockquote"><p>release_chunks = 12</p></blockquote>
<blockquote id="9c83" class="graf--blockquote"><p>block_hash = …</p></blockquote>
<blockquote id="64d8" class="graf--blockquote"><p>darkleaks.start(source_filename, “output_segments”, number_chunks)</p></blockquote>
<blockquote id="9009" class="graf--blockquote"><p>proofs = darkleaks.prove(source_filename, number_chunks, block_hash, release_chunks)</p></blockquote>
<blockquote id="5e7a" class="graf--blockquote"><p>secret_keys = darkleaks.secrets(source_filename, number_chunks)</p></blockquote>
<p id="0207" class="graf--p">See the <a class="markup--anchor markup--p-anchor" href="https://github.com/darkwallet/darkleaks/blob/master/python/example.py" target="_blank" rel="nofollow" data-href="https://github.com/darkwallet/darkleaks/blob/master/python/example.py">example.py</a> for more info.</p>
<p id="77c4" class="graf--h4"><strong>How does it work?</strong></p>
<p id="a0fb" class="graf--p">When the leaker selects a document, it is broken up into segments. Each of the segments is hashed, and a Bitcoin address is generated using the hash as the secret key. From this public key, a new key is generated to encrypt the segments. The encrypted segments are released for public download with the list of Bitcoin addresses.</p>
<p class="graf--p"><a href="/imgs/2015/02/1_RTZrHcRj7a_RnfCSWaVlrQ1.jpeg"><img class="aligncenter  wp-image-8966" src="/imgs/2015/02/1_RTZrHcRj7a_RnfCSWaVlrQ1.jpeg" alt="Darkleaks2" width="939" height="704" srcset="/imgs/2015/02/1_RTZrHcRj7a_RnfCSWaVlrQ1.jpeg 1333w, /imgs/2015/02/1_RTZrHcRj7a_RnfCSWaVlrQ1-300x225.jpeg 300w, /imgs/2015/02/1_RTZrHcRj7a_RnfCSWaVlrQ1-1024x767.jpeg 1024w" sizes="(max-width: 939px) 100vw, 939px" /></a></p>
<p id="3a2d" class="graf--p">To prove the authenticity of the document, the system uses a trustless provably fair mechanism. When announcing the leak, the leaker chooses a date and number of the chunks to be released. Based on the Bitcoin block hash at that time, some provably fair random numbers are chosen to select segments to be unlocked. This allows the community to verify the veracity of the file and decide whether they want to pay for the remaining encrypted segments.</p>
<p id="9b55" class="graf--p">The buyers then send Bitcoins to these addresses. When the leaker decides to claim the Bitcoins from the private key, due to how Bitcoin is designed he must release the public key which allows the buyers to decrypt the document.</p>
<p id="ea55" class="graf--p">Because the leaker cannot pre-choose which segments are released, the buyers can verify the addresses are correct, and the segments can be decrypted. This makes for an authenticatable and trustless mechanism for selling information on the decentralised black market.</p>
<p id="e36a" class="graf--h4"><strong>So what’s next?</strong></p>
<p id="aacb" class="graf--p">Don’t be afraid. Come join the revolution and reclaim your freedom.</p>
<p class="graf--p"><strong>Article Source: <a href="https://medium.com/@ZozanCudi/darkleaks-information-blackmarket-1ee5ac28c892" target="_blank">https://medium.com/@ZozanCudi/darkleaks-information-blackmarket-1ee5ac28c892</a></strong></p>
</div>

Updated: 2015-02-04