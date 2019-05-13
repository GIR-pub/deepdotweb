---
APT attacks via the Tor network, “OnionDuke”
---
<article class="post-listing post-8276 post type-post status-publish format-standard has-post-thumbnail hentry  tag-apt tag-attacks tag-network tag-onionduke tag-tor">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/zubairmuadh/" title="">Zubair Muadh </a></span>
    <span>November 20, 2014</span>
    
    <span><a href="https://www.deepdotweb.com/2014/11/20/apt-attacks-via-tor-network-onionduke/#comments">4 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>The Leviathan security group <a href="http://www.f-secure.com/weblog/archives/00002764.html" target="_blank">discovered</a> that malicious Tor exist nodes where wrapping executable windows files (.exe files) with malware. The malware was dubbed “OnionDuke” by F-Secure researchers.</p>
    <p><strong>The MiniDuke Link</strong></p>
    <p>MiniDuke was a highly sophisticated malware that previously infected government agencies and organisations spanning 23 countries. MiniDuke used multiple layers of encryption and clever coding tricks that made the malware difficult to detect and reverse engineer, due to the fact it was written in assembly language most MiniDuke Files where small in size. MiniDuke used certain websites as command &amp; control which is quite similar to the C&amp;C (Command and control) chain that OnionDuke uses.</p>
    <p><strong>How OnionDuke Works</strong></p>
    <p><a href="/imgs/2014/11/onionduke1.jpg"><img class="aligncenter size-full wp-image-8277" src="https://www.deepdotweb.com/wp-content/uploads/2014/11/onionduke1.jpg" alt="onionduke1" width="650" height="365" srcset="https://www.deepdotweb.com/wp-content/uploads/2014/11/onionduke1.jpg 650w, https://www.deepdotweb.com/wp-content/uploads/2014/11/onionduke1-300x168.jpg 300w" sizes="(max-width: 650px) 100vw, 650px"/></a>A victim would use the malicious Tor exit node and would request to download an executable (.exe) file from a site. The file would then be wrapped with a malware dropper called Trojan-Dropper:W32/OnionDuke.A by the malicious node. The Malware Dropper contains what appears at first look to be an embedded GIF image whereas it’s actually a DLL file called Backdoor:W32/OnionDuke.A. The DLL file is written onto the disk and executed. The DLL file then decrypts an embedded configuration file shown here:</p>
    <p><a href="/imgs/2014/11/onionduke2.jpg.png"><img class="aligncenter size-full wp-image-8278" src="https://www.deepdotweb.com/wp-content/uploads/2014/11/onionduke2.jpg.png" alt="onionduke2.jpg" width="650" height="300" srcset="https://www.deepdotweb.com/wp-content/uploads/2014/11/onionduke2.jpg.png 650w, https://www.deepdotweb.com/wp-content/uploads/2014/11/onionduke2.jpg-300x138.png 300w, https://www.deepdotweb.com/wp-content/uploads/2014/11/onionduke2.jpg-272x125.png 272w" sizes="(max-width: 650px) 100vw, 650px"/></a></p>
    <p>The domains where used as command and control sites that the malware would use to receive instructions or download and install additional malicious content. Upon analysis of the websites F-Secure researchers found them to be innocent websites compromised with malware. The domain overpict.com was hardcoded into the C&amp;C domain which could suggest that the malware abused twitter and used it as an addition C&amp;C channel.</p>
    <p><strong>The John Kassai link</strong></p>
    <p>Overpict.com was originally registered in 2011 under the alias “John Kassai”. Within two-weeks “John Kassai” registered the following domains:</p>
    <p>airtravelabroad.com, beijingnewsblog.net, grouptumbler.com, leveldelta.com, nasdaqblog.net, natureinhome.com, nestedmail.com, nostressjob.com, nytunion.com, oilnewsblog.com, sixsquare.net and ustradecomp.com.</p>
    <p>What’s interesting is that the domains leveldata.com and grouptumbler.com where previously used as C&amp;C domains by MiniDuke. This points towards the actors behind MiniDuke and OnionDuke are connected due to the shared use of infrastructure despite the malware being different families.</p>
    <p>OnionDuke also infected executables in .torrent containing pirated software. F-Secure also found strong evidence indicating that the OnionDuke was targeting European government agencies, this suggests two different targeting strategies. The first being the traditional APT surgical targeting the second being the “Shooting a fly with a cannon” approach which basically a mass-infection through modified binaries.</p>
    <p>Whilst case is still shrouded in mystery and speculation you can mitigate this risk by using a VPN that would encrypt your traffic with articles on this <a href="http://www.deepdotweb.com/?s=VPN">found here</a>. In addition to this, <strong>don’t download .exe files over Tor</strong>.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/apt/" rel="tag">apt</a> <a href="https://www.deepdotweb.com/tag/attacks/" rel="tag">attacks</a> <a href="https://www.deepdotweb.com/tag/network/" rel="tag">network</a> <a href="https://www.deepdotweb.com/tag/onionduke/" rel="tag">onionduke</a> <a href="https://www.deepdotweb.com/tag/tor/" rel="tag">tor</a></span> <span style="display:none" class="updated">2014-11-20</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/zubairmuadh/" title="Posts by Zubair Muadh" rel="author">Zubair Muadh</a></strong></div>
    </div>
</article>

