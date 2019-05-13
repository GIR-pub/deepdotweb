---
title: How to Safely Host Your Own TOR Hidden Service
---
573 


<span>Posted by: <a href="https://www.deepdotweb.com/author/admin/" title="">DeepDotWeb </a></span>
<span>October 19, 2013</span>


<div class="box  warning"><div class="box-inner-block"><i class="tieicon-boxicon"></i>
<h2><span style="text-decoration: underline; color: #ff0000;">This Tutorial Is OUTDATED</span></h2>
<h2><span style="text-decoration: underline; color: #ff0000;">&#8211; DO NOT USE IT &#8211; YOU WILL BE DE-ANOYNMIZED AND BUSTED!</span></h2>
</div></div>
<p><sup>you</sup> <sup>have</sup> <sup>the</sup> <sup>knowledge</sup> <sup>and</sup> <sup>ability</sup> <sup>to</sup> <sup>host</sup> <sup>on</sup> <sup>a</sup> <sup>Linux</sup> <sup>Based</sup> <sup>system,</sup> <sup>that</sup> <sup>is</sup> <sup>a</sup> <sup>preferable</sup> <sup>alternative.</sup> <sup>However,</sup> <sup>the</sup> <sup>majority</sup> <sup>of</sup> <sup>users</sup> <sup>will</sup> <sup>have</sup> <sup>a</sup> <sup>Windows</sup> <sup>Based</sup> <sup>PC</sup> <sup>at</sup> <sup>their</sup> <sup>disposal</sup> <sup>or</sup> <sup>are</sup> <sup>more</sup> <sup>comfortable</sup> <sup>with</sup> <sup>Windows.</sup><br/>
<sup>There</sup> <sup>are</sup> <sup>plenty</sup> <sup>of</sup> <sup>complete</sup> <sup>Linux</sup> <sup>mainly <sup>Debian</sup></sup> <sup>guides</sup> <sup>to</sup> <sup>this,</sup> <sup>but</sup> <sup>a</sup> <sup>complete</sup> <sup>Windows</sup> <sup>guide</sup> <sup>was</sup> <sup>not</sup> <sup>found.</sup></p>
<hr/>
<p>What You&#8217;ll Need:</p>
<ul>
<li>Dedicated Box [Free to $200] &#8211; <sup>At</sup> <sup>least</sup> <sup>1Ghz</sup> <sup>Dual</sup> <sup>Core,</sup> <sup>1GB</sup> <sup>RAM,</sup> <sup>30GB</sup> <sup>HD,</sup> <sup>and</sup> <sup>Windows</sup> <sup>XP</sup> <sup>Windows <sup>7</sup> <sup>&amp;</sup> <sup>8</sup> <sup>Not</sup> <sup>Advisable</sup></sup></li>
<li>Anonymous VPN Account [$3 to $12 Monthly] &#8211; <sup>Allows</sup> <sup>you</sup> <sup>to</sup> <sup>further</sup> <sup>mask</sup> <sup>your</sup> <sup>identity</sup> <sup>in</sup> <sup>the</sup> <sup>event</sup> <sup>of</sup> <sup>errors</sup> <sup>or</sup> <sup>exploits</sup> <sup>to</sup> <sup>your</sup> <sup>site</sup></li>
<li>Tor Browser Bundle [<a href="http://www.torproject.org">www.torproject.org</a>] &#8211; <sup>The</sup> <sup>same</sup> <sup>bundle</sup> <sup>you</sup> <sup>already</sup> <sup>use</sup> <sup>to</sup> <sup>browse</sup> <sup>.onion</sup> <sup>sites</sup> <sup>and</sup> <sup><a href="http://www.reddit.com/r/silkroad">/r/silkroad</a></sup></li>
<li>Apache, MySQL, PHP package [<a href="http://www.uniformserver.com/">http://www.uniformserver.com/</a>] &#8211; <sup>We</sup> <sup>recommend</sup> <sup>you</sup> <sup>use</sup> <sup>The</sup> <sup>Uniform</sup> <sup>Server,</sup> <sup>but</sup> <sup>you</sup> <sup>are</sup> <sup>free</sup> <sup>to</sup> <sup>use</sup> <sup>any</sup> <sup>package</sup> <sup>that</sup> <sup>includes</sup> <sup>PHP</sup> <sup>support,</sup> <sup>MySQL</sup> <sup>backend,</sup> <sup>and</sup> <sup>has</sup> <sup>Apache.</sup> <sup>Xampp</sup> <sup>is</sup> <sup>very</sup> <sup>insecure,</sup> <sup>and</sup> <sup>EasyPHP</sup> <sup>has</sup> <sup>many</sup> <sup>items</sup> <sup>you</sup> <sup>do</sup> <sup>not</sup> <sup>need</sup> <sup>in</sup> <sup>a</sup> <sup>TOR</sup> <sup>server.</sup></li>
</ul>
<hr/>
<p><strong>Building the Box</strong></p>
<p>First you need to make sure your Windows OS is not registered to you and it is preferable that you find a PC that is not registered to you (such as at yard sales, friends, auctions, ebay without Serial, ect).<br/>
    Since most don&#8217;t just have a spare Windows disc lying around, you should visit the Pirate Bay or similar torrent sites and download a Windows XP SP3 (with matching architecture &#8211; x86 is 32 Bit, x64 is 64 Bit).<br/>
    Always make sure to source reliable torrents, and to make sure they don&#8217;t have any backdoors or embedded malicious software. This can be done by monitoring your network activity from the machine for a few days to make sure no activity that&#8217;s odd occurs.</p>
<p>Make sure you name your PC a obscure name, such as PC or DIR &#8211; never anything that can be linked to you. Server errors can sometime link to the servers name, and if this is JohnSmithsPC then that&#8217;s not very good for John Smith.</p>
<p>The same thing goes with your admin account &#8211; something obscure. Occasionally the users name is displayed in errors (along with or instead of the PC name).</p>
<hr/>
<p><strong>Building the System</strong></p>
<p>Uninstall Everything. Well, nearly everything.<br/>
    No updater, no antivirus, no firewall, no software &#8211; nothing but the basic requirements for your PC to operate.<br/>
    You also need to go to Control Panel &gt; Uninstall Program &gt; Uninstall Windows Service<br/>
    Remove games, fax, and any other tools that you do not need. Keep any networking tools that are already checked.</p>
<p>Windows Defender is good enough since you are not going to be on the clearnet, and unless you are browsing with this PC you will not encounter any issues with downloading malicious software from the web.</p>
<p>If you don&#8217;t trust Defender, any free AV is acceptable. Same with the firewall.</p>
<hr/>
<p><strong>Adding Security</strong></p>
<p>Download Truecrypt and install it.<br/>
    At the very least you want to make sure your containers for your hostname and your web directory are encrypted.<br/>
    This will require you to login to the container to decrypt it after each restart, but this also prevents any information to be recovered as long as the PC is shut down before any security breaches occur.</p>
<p>This will require you to monitor the server, and if remote you will have to use a remote login to decrypt the container each restart.</p>
<div class="box  warning"><div class="box-inner-block"><i class="tieicon-boxicon"></i>
<h2><span style="text-decoration: underline; color: #ff0000;">This Tutorial Is OUTDATED</span></h2>
<h2><span style="text-decoration: underline; color: #ff0000;">&#8211; DO NOT USE IT &#8211; YOU WILL BE DE-ANOYNMIZED AND BUSTED!</span></h2>
</div></div>
<p>&nbsp;</p>
<hr/>
<p><strong>The Software</strong></p>
<p>Okay, so you have a barebones system.</p>
<p>Install your VPN first, and always have it on. Routinely change it (or enable auto change) to further mask your identity/location.</p>
<p>NEVER USE THIS PC WITHOUT THE VPN ENABLED.</p>
<p>Extract TOR to a directory under C (Such as C:\TOR) and add the Videlia.exe to your startup folder in your start menu so TOR starts whenever your OS loads up.</p>
<p>Open Tor Browser, and the Videlia GUI appears.</p>
<p>Click Settings &gt; Services and you will see a blank table. Click the green &#8220;+&#8221; and a new service is added.<br/>
    Click the appropriate box to change or add a value.</p>
<ul>
<li>Set Virtual Port to 80</li>
<li>Set Target to 127.0.0.1:420 &#8211; Replace 420 with whatever port number you wish</li>
<li>Set Directory Path to (preferably) a separate storage container. This could be a partition, a external HD, a SD card, a Flash Drive.</li>
</ul>
<p>Just remember the drive must NOT be named anything revealing.</p>
<p>Restart TOR and go to your directory path that you entered.<br/>
    Open the &#8220;HOSTNAME&#8221; file with notepad and you will find your unique .onion address.</p>
<p>If you know how to generate a unique .onion address using Scallion, these are the two files you will replace to have a custom .onion address.</p>
<div class="box  warning"><div class="box-inner-block"><i class="tieicon-boxicon"></i>
<h2><span style="text-decoration: underline; color: #ff0000;">This Tutorial Is OUTDATED</span></h2>
<h2><span style="text-decoration: underline; color: #ff0000;">&#8211; DO NOT USE IT &#8211; YOU WILL BE DE-ANOYNMIZED AND BUSTED!</span></h2>
</div></div>
<p>&nbsp;</p>
<p>As a reference, this is how long it takes to generate a custom address:</p>
<ul>
<li>4 Characters &#8211; 10 seconds</li>
<li>5 Characters &#8211; 29 Seconds</li>
<li>6 Characters &#8211; 1 Minute</li>
<li>7 Characters &#8211; 5 to 10 Minutes</li>
<li>8 Characters &#8211; 20 Minutes to 1 hour</li>
<li>9 Characters &#8211; 2 to 10 Hours</li>
<li>10 Characters &#8211; 5 to 10 days</li>
</ul>
<p>Now, you need to install your Web Server. We recommend The Uniform Server, but you are free to use any web server package you want. Just remember some are much less secure than others.</p>
<p>Make sure your web directory is a separate container than your operating system. This can be a separate partition, hard drive, external drive, SD card, or flash drive. This will be the drive to destroy in the event of an emergency.</p>
<p>After you get everything installed, you will have to customize your httpd.config file.</p>
<p>Scroll down to Listen 80<br/>
    Change this to Listen 127.0.0.1:80<br/>
    Add the following line below this one: Listen 127.0.0.1:420 (if you changed the Port Number, make sure this line matches what you put in the &#8220;Target&#8221; box in your TOR service).</p>
<p>Scroll down to ServerName<br/>
    Change this to ServerName 1qw23er45ty67ui8.onion, where 1qw23er45ty67ui8.onion is your hidden service .onion hostname.</p>
<p>Make sure you disable any features that you do not need to prevent security issues.</p>
<p>As per the BMR mistake, make sure your index.html or index.php is just a redirect.</p>
<p>Create a subfolder to keep your site at (this will be displayed in the URL, so instead of mysite.com/index.html being your home page, it should be a redirect to another directory and your real index should be at mysite.com/hidden/index.html or something similar).</p>
<div class="box  warning"><div class="box-inner-block"><i class="tieicon-boxicon"></i>
<h2><span style="text-decoration: underline; color: #ff0000;">This Tutorial Is OUTDATED</span></h2>
<h2><span style="text-decoration: underline; color: #ff0000;">&#8211; DO NOT USE IT &#8211; YOU WILL BE DE-ANOYNMIZED AND BUSTED!</span></h2>
</div></div>
<p>&nbsp;</p>
<p>Some errors result in your index page being offered for download, so make sure you don&#8217;t have any identifying information in it. Also, ASCII art being placed in index pages is a long time tradition, try that.</p>
<p>You site will be available at localhost, but it is not recommended that you use this to setup scripts since some will take localhost as your hostname, and not your .onion address.<br/>
    You do have to use TOR Browser to access your .onion site address to setup some scripts. Some have the option to change your hostname in the settings, and others have documentation on how to manually change it, but ultimately it is much easier to go to your .onion site and set it up since you are making a client connection so you also are making sure the site and scripts will work for your customers, visitors, ect.</p>
<p>You should also find your intranet IP and see if you can connect to your site using that IP and the port you set. If you can, you need to change Listen 80 to Listen 127.0.0.1:80<br/>
    If you can see your website from, say, 192.168.1.20 then anyone that is on your network can, and anyone that has your outside IP address (even through VPN) can see your site on clearnet. You MUST have 127.0.0.1:80 listed.</p>
<hr/>
<p><strong>Running Multiple TOR Sites</strong></p>
<p>1) Create your hidden services manually in your torrc configuration file as normal e.g. :</p>
<div id="crayon-594fbabaeb74a509563427" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    HiddenServiceDir /path/to/my/site/keys/service1
    HiddenServicePort 80 127.0.0.1:8082
    HiddenServiceDir /path/to/my/site/keys/service2
    HiddenServicePort 80 127.0.0.1:8083
</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-594fbabaeb74a509563427-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-594fbabaeb74a509563427-2">2</div><div class="crayon-num" data-line="crayon-594fbabaeb74a509563427-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-594fbabaeb74a509563427-4">4</div><div class="crayon-num" data-line="crayon-594fbabaeb74a509563427-5">5</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-594fbabaeb74a509563427-1"><span class="crayon-v">HiddenServiceDir</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">path</span><span class="crayon-o">/</span><span class="crayon-st">to</span><span class="crayon-o">/</span><span class="crayon-v">my</span><span class="crayon-o">/</span><span class="crayon-v">site</span><span class="crayon-o">/</span><span class="crayon-v">keys</span><span class="crayon-o">/</span><span class="crayon-e">service1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></div><div class="crayon-line crayon-striped-line" id="crayon-594fbabaeb74a509563427-2"><span class="crayon-i">HiddenServicePort</span><span class="crayon-h"> </span><span class="crayon-cn">80</span><span class="crayon-h"> </span><span class="crayon-cn">127.0.0.1</span><span class="crayon-o">:</span><span class="crayon-cn">8082</span><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></div><div class="crayon-line" id="crayon-594fbabaeb74a509563427-3"><span class="crayon-v">HiddenServiceDir</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">path</span><span class="crayon-o">/</span><span class="crayon-st">to</span><span class="crayon-o">/</span><span class="crayon-v">my</span><span class="crayon-o">/</span><span class="crayon-v">site</span><span class="crayon-o">/</span><span class="crayon-v">keys</span><span class="crayon-o">/</span><span class="crayon-e">service2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></div><div class="crayon-line crayon-striped-line" id="crayon-594fbabaeb74a509563427-4"><span class="crayon-i">HiddenServicePort</span><span class="crayon-h"> </span><span class="crayon-cn">80</span><span class="crayon-h"> </span><span class="crayon-cn">127.0.0.1</span><span class="crayon-o">:</span><span class="crayon-cn">8083</span><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></div><div class="crayon-line" id="crayon-594fbabaeb74a509563427-5">&nbsp;</div></div></td>
</tr>
</table>
</div>
</div>
    
<p>
    2) Start Tor to generate your services&#8217; host names. For vanity .onion names, see <a href="https://github.com/lachesis/scallion">Scallion</a>.</p>
<p>3) Stop Apache if it is running and edit your virtual host file(s) &#8211; specifically, add an entry for each host, where ServerName is the name from your Tor service&#8217;s &#8216;hostname&#8217; file:</p>
<div id="crayon-594fbabaeb756617203681" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    &amp;lt;VirtualHost 127.0.0.1:8082&amp;gt;
    ServerName site1example8nbp.onion
    DocumentRoot /path/to/my/tor/www/root/site1
    &amp;lt;/VirtualHost&amp;gt;
    
    &amp;lt;VirtualHost 127.0.0.1:8083&amp;gt;
    ServerName site2example6pqr.onion
    DocumentRoot /path/to/my/tor/www/root/site2
    &amp;lt;/VirtualHost&amp;gt;
</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-594fbabaeb756617203681-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-594fbabaeb756617203681-2">2</div><div class="crayon-num" data-line="crayon-594fbabaeb756617203681-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-594fbabaeb756617203681-4">4</div><div class="crayon-num" data-line="crayon-594fbabaeb756617203681-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-594fbabaeb756617203681-6">6</div><div class="crayon-num" data-line="crayon-594fbabaeb756617203681-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-594fbabaeb756617203681-8">8</div><div class="crayon-num" data-line="crayon-594fbabaeb756617203681-9">9</div><div class="crayon-num crayon-striped-num" data-line="crayon-594fbabaeb756617203681-10">10</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-594fbabaeb756617203681-1"><span class="crayon-o">&amp;</span><span class="crayon-v">lt</span><span class="crayon-sy">;</span><span class="crayon-i">VirtualHost</span><span class="crayon-h"> </span><span class="crayon-cn">127.0.0.1</span><span class="crayon-o">:</span><span class="crayon-cn">8082</span><span class="crayon-o">&amp;</span><span class="crayon-v">gt</span><span class="crayon-sy">;</span></div><div class="crayon-line crayon-striped-line" id="crayon-594fbabaeb756617203681-2"><span class="crayon-h">&nbsp;&nbsp; </span><span class="crayon-e">ServerName </span><span class="crayon-v">site1example8nbp</span><span class="crayon-sy">.</span><span class="crayon-e">onion</span></div><div class="crayon-line" id="crayon-594fbabaeb756617203681-3"><span class="crayon-e">&nbsp;&nbsp; </span><span class="crayon-v">DocumentRoot</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">path</span><span class="crayon-o">/</span><span class="crayon-st">to</span><span class="crayon-o">/</span><span class="crayon-v">my</span><span class="crayon-o">/</span><span class="crayon-v">tor</span><span class="crayon-o">/</span><span class="crayon-v">www</span><span class="crayon-o">/</span><span class="crayon-v">root</span><span class="crayon-o">/</span><span class="crayon-v">site1</span></div><div class="crayon-line crayon-striped-line" id="crayon-594fbabaeb756617203681-4"><span class="crayon-o">&amp;</span><span class="crayon-v">lt</span><span class="crayon-sy">;</span><span class="crayon-o">/</span><span class="crayon-v">VirtualHost</span><span class="crayon-o">&amp;</span><span class="crayon-v">gt</span><span class="crayon-sy">;</span></div><div class="crayon-line" id="crayon-594fbabaeb756617203681-5">&nbsp;</div><div class="crayon-line crayon-striped-line" id="crayon-594fbabaeb756617203681-6"><span class="crayon-o">&amp;</span><span class="crayon-v">lt</span><span class="crayon-sy">;</span><span class="crayon-i">VirtualHost</span><span class="crayon-h"> </span><span class="crayon-cn">127.0.0.1</span><span class="crayon-o">:</span><span class="crayon-cn">8083</span><span class="crayon-o">&amp;</span><span class="crayon-v">gt</span><span class="crayon-sy">;</span></div><div class="crayon-line" id="crayon-594fbabaeb756617203681-7"><span class="crayon-h">&nbsp;&nbsp;</span><span class="crayon-e">ServerName </span><span class="crayon-v">site2example6pqr</span><span class="crayon-sy">.</span><span class="crayon-e">onion</span></div><div class="crayon-line crayon-striped-line" id="crayon-594fbabaeb756617203681-8"><span class="crayon-e">&nbsp;&nbsp;</span><span class="crayon-v">DocumentRoot</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-v">path</span><span class="crayon-o">/</span><span class="crayon-st">to</span><span class="crayon-o">/</span><span class="crayon-v">my</span><span class="crayon-o">/</span><span class="crayon-v">tor</span><span class="crayon-o">/</span><span class="crayon-v">www</span><span class="crayon-o">/</span><span class="crayon-v">root</span><span class="crayon-o">/</span><span class="crayon-v">site2</span></div><div class="crayon-line" id="crayon-594fbabaeb756617203681-9"><span class="crayon-o">&amp;</span><span class="crayon-v">lt</span><span class="crayon-sy">;</span><span class="crayon-o">/</span><span class="crayon-v">VirtualHost</span><span class="crayon-o">&amp;</span><span class="crayon-v">gt</span><span class="crayon-sy">;</span></div><div class="crayon-line crayon-striped-line" id="crayon-594fbabaeb756617203681-10">&nbsp;</div></div></td>
</tr>
</table>
</div>
</div>
    
<p>
    4) Assuming Apache is still stopped, edit your httpd.conf file to listen on the ports you specified above (near the top):</p>
<div id="crayon-594fbabaeb75a952340346" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    #Listen 12.34.56.78:80
    Listen 80
    # Listen for Tor services
    Listen 127.0.0.1:8082
    Listen 127.0.0.1:8083
</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-594fbabaeb75a952340346-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-594fbabaeb75a952340346-2">2</div><div class="crayon-num" data-line="crayon-594fbabaeb75a952340346-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-594fbabaeb75a952340346-4">4</div><div class="crayon-num" data-line="crayon-594fbabaeb75a952340346-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-594fbabaeb75a952340346-6">6</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-594fbabaeb75a952340346-1"><span class="crayon-p">#Listen 12.34.56.78:80</span></div><div class="crayon-line crayon-striped-line" id="crayon-594fbabaeb75a952340346-2"><span class="crayon-i">Listen</span><span class="crayon-h"> </span><span class="crayon-cn">80</span></div><div class="crayon-line" id="crayon-594fbabaeb75a952340346-3"><span class="crayon-p"># Listen for Tor services</span></div><div class="crayon-line crayon-striped-line" id="crayon-594fbabaeb75a952340346-4"><span class="crayon-i">Listen</span><span class="crayon-h"> </span><span class="crayon-cn">127.0.0.1</span><span class="crayon-o">:</span><span class="crayon-cn">8082</span></div><div class="crayon-line" id="crayon-594fbabaeb75a952340346-5"><span class="crayon-i">Listen</span><span class="crayon-h"> </span><span class="crayon-cn">127.0.0.1</span><span class="crayon-o">:</span><span class="crayon-cn">8083</span></div><div class="crayon-line crayon-striped-line" id="crayon-594fbabaeb75a952340346-6">&nbsp;</div></div></td>
</tr>
</table>
</div>
</div>
    
<p>
    5) Save all your configuration changes and restart Apache. Assuming everything went well, all of your hidden services should be available as separate .onion addresses.</p>
<p>Please note there are more secure way to set things up and the above is just to show how the basic directives work.</p>
<ul>
<li>127.0.0.1 is used to help restrict access to &#8220;localhost only&#8221; for the Listen directive.</li>
<li>Ports are just examples &#8211; you can use any ports you like as long as they match. Ports listed were not forwarded (other than 80).</li>
<li>.onion domains in step 3 are (obviously) examples and should match whatever Tor generates for the actual service name. Note that if you want REAL vanity .onion addresses, check out <a href="https://github.com/lachesis/scallion">Scallion</a> for Windows and Linux. There is a <a href="https://github.com/lachesis/scallion/blob/binaries/scallion-v1.0.zip?raw=true">pre-built Windows binary here</a>.</li>
</ul>
<p>More information here</p>
<ul>
<li>You should drop in your Scallion-made &#8216;private_key'(s) into the appropriates folders listed in Step 1 before starting Tor in Step 2. Otherwise, Tor will auto-generate your services &#8216;private_key&#8217; and &#8216;hostname&#8217; files in the appropriately selected folders. You can delete these and start over if you wish, just update your virtual host entries.</li>
<li>Step 4 is VERY important, otherwise the services will be unavailable even from localhost (e.g. if you just did steps 2 and 3).</li>
<li>For Linux, you might need to add the .onions to your /etc/hosts/ file, but I haven&#8217;t verified this. No host file alterations needed for Windows, for certain.</li>
</ul>
<hr/>
<p><strong>Extra Steps</strong></p>
<p><strong>Email</strong></p>
<p>If you wish, you can enter your email in httpd.config. Make sure you use anonymous email services, we like safe-mail.net but there are several alternatives.</p>
<p>This is also useful for people contacting you. Customers, bug reports, or just to chat about the site or content an email is always a good resource to take advantage of.</p>
<p><strong>PGP Encryption</strong></p>
<p>PGP is also very useful, and with the current situations with marketplaces being shut down and messages intercepted, it is highly recommended.</p>
<p>PGP is free, and consists of the following:</p>
<ul>
<li>Your Public Key, which you give people to encrypt messages that only you can decrypt.</li>
<li>Your Private Key, which is used to decrypt messages by you. NEVER GIVE YOUR PRIVATE KEY OUT.</li>
</ul>
<p>When a person wants to send you a message, then take your public key and save it to their PGP client. Then then type their message any encrypt it.<br/>
    After they encrypt it, not even the person who wrote/sends it can read it again. Only the person that has the matching private key can decrypt it.</p>
<p><strong>Virtual Machine</strong></p>
<p>Some wish to install the entire system inside a Virtual Machine, in which you will have to install windows again as well as follow all the previous instructions, but the advantage is you can run a VPN on the host (outside the VM) and you will be able to bounce off of 2 separate IP addresses.</p>
<p>Experienced users can also forward everything on the host trough TOR, so a native connection on the VM will actually be masked by TOR.<br/>
    Using this you will be able to use 2 separate TOR instances along with 2 different masking IP&#8217;s.</p>
<p><strong>Escrow</strong></p>
<p>You need to sell stuff, people need t buy stuff, and people are looking to steal stuff.<br/>
    So, use escrow.<br/>
<a href="http://www.reddit.com/r/bitcoin">/r/bitcoin</a>&#8216;s sidebar and Bitcoin Trade Wiki has several Escrow services, although some are not geared towards illegal activity.<br/>
<a href="http://www.bitescrow.org/">http://www.bitescrow.org/</a> is a decent escrow site that accommodates several (private) marketplaces already, and so far looks to be a reliable resource.<br/>
    It is also open source.<br/>
    Budster recently created a brainwallet that utilized P2P escrow, but has yet to release it for open source. When they do, it will be a valuable tool for the BTC community.</p>
<div class="box  warning"><div class="box-inner-block"><i class="tieicon-boxicon"></i>
<h2><span style="text-decoration: underline; color: #ff0000;">This Tutorial Is OUTDATED</span></h2>
<h2><span style="text-decoration: underline; color: #ff0000;">&#8211; DO NOT USE IT &#8211; YOU WILL BE DE-ANOYNMIZED AND BUSTED!</span></h2>
</div></div>
<p>&nbsp;</p>
</div>
 

Updated: 2013-10-19