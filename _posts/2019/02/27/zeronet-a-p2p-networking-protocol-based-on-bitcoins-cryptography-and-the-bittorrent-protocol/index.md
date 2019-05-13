---
ZeroNet &#8211; A P2P networking protocol based on Bitcoin&#8217;s cryptography and the BitTorrent protocol
---
<article class="post-listing post-28464 post type-post status-publish format-standard has-post-thumbnail hentry  tag-based tag-bittorrent tag-cryptography tag-networking tag-p2p tag-protocol tag-zeronet">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>February 27, 2019</span>
    
    <span><a href="https://www.deepdotweb.com/2019/02/27/zeronet-a-p2p-networking-protocol-based-on-bitcoins-cryptography-and-the-bittorrent-protocol/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Anonymous networking has been gaining massive popularity during the past few years. More and more users are relying on <a href="https://www.deepdotweb.com/2017/03/30/tor-browser-fully-anonymous-myth-reality/">network protocols such as Tor</a> in order to be able to browse the internet anonymously. Zeronet is a new distributed, censorship resistant networking protocol that is based on Bitcoin&#8217;s cryptography and BitTorrent&#8217;s technology, which has massive potential to grow in popularity during the next few years. Throughout this article, we will overview Zeronet and its applications.</p>
    <p><img class="wp-image-28468" src="/imgs/2019/02/zeronett-png.png" alt="zeronett.png" srcset="/imgs/2019/02/zeronett-png.png 220w, /imgs/2019/02/zeronett-png-212x300.png 212w" sizes="(max-width: 220px) 100vw, 220px" /></p>
    <p><strong>What is ZeroNet?</strong></p>
    <p>ZeroNet is decentralized P2P network initially introduced in 2015 by Tamas Kocsis. The network&#8217;s code is open source and is programmed using Python. On ZeroNet, a website is identified by a unique public key of a bitcoin address, rather than by an IP address. The site&#8217;s private key enables its owner to publish content and sign it, which will thereafter propagate throughout the network.</p>
    <p>Websites are accessed via a usual internet browser after running the ZeroNet application, which serves as a local webhost for web pages hosted on ZeroNet. Additionally to relying on <a href="https://www.deepdotweb.com/2019/01/26/research-a-modern-look-into-bitcoins-advantages-and-usage-risks/">Bitcoin&#8217;s cryptography</a>, ZeroNet utilizes <a href="https://www.deepdotweb.com/2016/12/31/torrenting-dark-net/">BitTorrent network&#8217;s</a> trackers for negotiation of connections taking place between network peers. By default, ZeroNet does not support anonymity, yet it supports routing of network traffic via the Tor network. ZeroNet&#8217;s website, as well as the bittorrent tracker, are both blocked in China.</p>
    <p>The idea of P2P internet websites was suggested a while ago, as The Pirate Bay proposed building a P2P network a few years ago. Moreover, the BitTorrent Inc developed Project Malestrom, which is a closed source P2P networking framework. Another similar idea is represented by the SAFE Network which has been developed by MaidSafe, yet it is still not widely popular and is mainly focused on file storage.</p>
    <p>Breaker Browser is another similar application that utilizes the P2P DAT file protocol to enable the development, hosting, and serving of internet sites without having to rely on any servers.</p>
    <p>There is no way whatsoever to take down a page hosted on ZeroNet, so long as it has seeders, which renders these pages resistant to third party methods of censoring websites such as DMCA takedowns. By default, ZeroNet websites are limited to a size of 10 MBs, yet a user may request permission to use a bigger storage space, whenever needed.</p>
    <p><strong>Building sites on ZeroNet:</strong></p>
    <p>On ZeroNet, websites are named &#8220;zites&#8221;. ZeroNet is compliant with CSS, HTML, and JavaScript. Website developers can also design websites using CoffeeScript instead of JavaScript, yet the .coffee files will have to be compiled. In development mode, ZeroNet is capable of compiling to JavaScript, so .coffee files are compiled and stored onto .js files. The system also allows compiling of .sass files to CSS.</p>
    <p>Unfortunately, ZeroNet does not support server side programming languages such as PHP. However, ZeroNet supports sign up and log in to MySQL databases that are of P2P nature. Via the ZeroFrame API and certain plugins, websites can interact with ZeroNet via calling Python using JavaScript.</p>
    <p>Domains can be registered on ZeroNet with .bit domains via Namecoin. Domains can be managed via the command line prompt or the client&#8217;s GUI.</p>
    <p><strong>Important &#8220;Zites&#8221; on ZeroNet:</strong></p>
    <p>The Play website, owned by BitTorrent, has a magnet link to a ZeroNet website, which includes copyrighted movies.</p>
    <p>ZeroMe is a ZeroNet based social network which has been launched in August 2016. ZeroMe is based on twitter. Via the merger site option, users&#8217; data on ZeroMe is secured on multiple hubs, which represent merged websites from ZeroMe.</p>
    <p>KopyKate Big was the first ever YouTube alternative service on ZeroNet, which was launched in November 2017. KopyKate Big makes use of ZeroNet&#8217;s Big File option.</p>
    <p>Git Center is a GitHub alternative which was launched in 2017 on ZeroNet, following Microsoft&#8217;s acquisition of GitHub. Git Center supports issues, clones, stars, comment reactions, and pull requests, in a decentralized P2P means.</p>
    <p>In 2018, development started on the first ever internet browser dedicated to ZeroNet&#8217;s websites, which was named the ZeroNet Browser.</p>
    <p>The first ever click-to-begin internet framework on ZeroNet was introduced in December 2018. The Framework.JS has been developed on ZeroNet on the basis of its theming and cloning features.</p>
    <p><strong>Accessing a website on ZeroNet:</strong></p>
    <p>When a user wishes to access a website on ZeroNet, it will request their IP address via the BitTorrent trackers. Firstly, a file named content.json file will be downloaded, which includes all other file names, hashes, and the cryptographic signature of the site owner.</p>
    <p>Then, the downloaded content.json file will be verified via the website&#8217;s address and the site owner&#8217;s cryptographic signature obtained from the file. Other files of the website (css, html, css, etc) will then be downloaded and authenticated via their size and unique SHA512 hash obtained from the content.json file. Each visited website will then be also served by the user visiting it.</p>
    <p>If the owner of the website, who owns the site&#8217;s private key, modifies the content of the website, they will then sign the modified content.json file and broadcast it to the network peers. After the network&#8217;s peers verify the integrity of the file via means of the signature, they will download the modified content and serve it to other peers across the network.</p>
    <p><strong>How to use Tor with ZeroNet?</strong></p>
    <p>If a user wishes to hide their IP address, they will have to download and install the most recent version of ZeroNet and then select Tor and Enable Tor for every outgoing connection on ZeroHello.</p>
    <p>For Windows OS, Tor is by default bundled with ZeroNet. On its first ever run on the installed machine, ZeroNet will download and install Tor. If for whatever reason, this fails, it can be manually installed.</p>
    <p>ZeroNet does not come with Tor pluggable transports. The simplest way to use Tor in a censored country is to run the Tor browser, configure it to use pluggable transports to connect to the Tor network, and then modify ZeroNet&#8217;s configuration to use the proxy of the Tor browser and control port via starting ZeroNet with the following command:</p>
    <p>&#8211;tor_controller 127.0.0.1:9151 &#8211;tor_proxy 127.0.0.1:9150</p>
    <p>Alternatively, the following parameters can be added to the zeronet.conf file:</p>
    [global]
    <p>tor_controller = 127.0.0.1:9151</p>
    <p>tor_proxy = 127.0.0.1:9150</p>
    <p><strong>Final thoughts:</strong></p>
    <p>ZeroNet is an attempt to decentralize the internet and render it totally resistant to censorship via means of Bitcoin&#8217;s cryptography and BitTorrent&#8217;s technology. Even though the project is still in its infancy, it has massive potential to grow and increase in popularity during the next few years.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/based/" rel="tag">based</a> <a href="https://www.deepdotweb.com/tag/bittorrent/" rel="tag">bittorrent</a> <a href="https://www.deepdotweb.com/tag/cryptography/" rel="tag">cryptography</a> <a href="https://www.deepdotweb.com/tag/networking/" rel="tag">networking</a> <a href="https://www.deepdotweb.com/tag/p2p/" rel="tag">p2p</a> <a href="https://www.deepdotweb.com/tag/protocol/" rel="tag">protocol</a> <a href="https://www.deepdotweb.com/tag/zeronet/" rel="tag">zeronet</a></span> <span style="display:none" class="updated">2019-02-27</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

