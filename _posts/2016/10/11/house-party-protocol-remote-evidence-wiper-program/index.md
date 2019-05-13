---
House Party Protocol &#8211; remote evidence wiper program
---
<article class="post-listing post-15747 post type-post status-publish format-standard has-post-thumbnail hentry  tag-evidence tag-house tag-party tag-program tag-protocol tag-remote tag-wiper">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/filipjelic/" title="">Filip Jelic </a></span>
    <span>October 11, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/10/11/house-party-protocol-remote-evidence-wiper-program/#comments">14 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Implementing this will make you feel that fuzzy feeling of being extra safe. House Party Protocol is a program that you control remotely and when activated, it encrypts all confidential data on your computer. It&#8217;s a life saver in case of police seizure or theft by criminals.</p>
    <p>One might suggest deleting instead of encrypting those files, but the encryption is actually safer. This is beyond the scope of this tutorial, but you will probably find all answers on this topic <a href="http://www.howtogeek.com/125521/htg-explains-why-deleted-files-can-be-recovered-and-how-you-can-prevent-it/">here</a>. Extra point goes to encrypting for being the same for every system while irreversibly deleting files is system and hard drive dependent.</p>
    <p>The name was inspired by a scene from Iron Man 3 movie in which Tony Stark activates the &#8220;House Party Protocol&#8221; when his house is destroyed. A guy named Utku Sen wrote 2 versions</p>
    <p>and uploaded them to github:</p>
    <p><a href="https://github.com/utkusen/house-party-py">python version</a> (recommended and featured in this tutorial)</p>
    <p><a href="https://github.com/utkusen/house-party-protocol">C# version</a></p>
    <p><strong>How it works?</strong></p>
    <p>There are 3 files in the process:</p>
    <p><span style="text-decoration: underline;">hpp.py</span> &#8211; Python program that reads an uploaded text file (command.txt) every 60 seconds (adjustable) to check for the start command. If the permission is given, the &#8220;party&#8221; starts which means the program encrypts all files in chosen location with AES algorithm with unique random key for each encryption process. It also encrypts all files in all subdirectories.</p>
    <p><span style="text-decoration: underline;">bust.php</span> &#8211; Minimalistic HTML and PHP website that writes &#8220;1&#8221; to commands.txt if you submit the correct password signaling that the &#8220;party&#8221; should start. This is a public website that can be reached from any device with internet access.</p>
    <p><span style="text-decoration: underline;">command.txt</span> &#8211; The file hpp.py periodically reads to know when to start the action.</p>
    <p>I used Kali Linux (Debian based), but it should work like this for any Linux environment. If you would like me to make a tutorial for Windows or any other OS, let me know in the comments section.</p>
    <p>First, you need to have a hosting account which can run php scripts. Many websites offer that service for free, I used <a href="https://www.000webhost.com/">000webhost</a>.</p>
    <p>Next, copy the HTML and PHP code from Utku’s <a href="https://github.com/utkusen/house-party-py">github</a> and save it as a PHP file (.php). Then upload it along with empty command.txt file so they are both accessible from any internet browser. You should be able to open the page that prompts you the password at <a href="http://www.yoursite.com/bust.php">www.yoursite.com/bust.php</a> :</p>
    <p><img class="wp-image-15748 aligncenter" src="/imgs/2016/10/word-image-16.png" srcset="/imgs/2016/10/word-image-16.png 291w, /imgs/2016/10/word-image-16-290x56.png 290w" sizes="(max-width: 291px) 100vw, 291px"/></p>
    <p>The password can (should) be set in bust.php line 3:</p>
    <div id="crayon-5964018c7310d903758585" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    $password = "utku123"; // Change it</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5964018c7310d903758585-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5964018c7310d903758585-1"><span class="crayon-sy">$</span><span class="crayon-v">password</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-s">"utku123"</span><span class="crayon-sy">;</span><span class="crayon-h"> </span><span class="crayon-c">// Change it</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    Also make sure that you can access command.txt file at www.yoursite.com/command.txt It should display an empty file until you submit your password to bust.php.</p>
    <p>You should have your python program starting and silently running by default every time you start your PC so the listener (method in hpp.py that periodically checks for the start command) is always ready! You can do this by adding a bash (.sh) script to your startup processes. Alternative option is to use SSH to run the command. SSH can actually be used to implement the whole protocol without using the hosting service.</p>
    <p>Terminal command that starts it should look like this:</p>
    <div id="crayon-5964018c73118822513388" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    # python3 hpp.py -d /home/SuperSecretFolder -u http://yourwebsite.com/command.txt -i 60</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5964018c73118822513388-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5964018c73118822513388-1"><span class="crayon-p"># python3 hpp.py -d /home/SuperSecretFolder -u http://yourwebsite.com/command.txt -i 60</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    python3 is the version of python being usedhpp.py is name of the python program -d /path specifies path to the folder that you want encrypted (all files in all subdirectories will be encrypted too); you have to keep all your confidential data in 1 folder -u URL specifies URL to be checked -i integer is the checking time period in seconds Running that command will start the listener:</p>
    <div id="crayon-5964018c7311d485367252" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    def listener(url,interval): #arguments are given when starting the program
    
    while True: #repeat
    
    if finish_control == 1:
    
    break #stop listening if the encryption is done
    
    check_url(url) #checks for the start command and act accordingly
    
    sleep(interval) #wait for specified time amount</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5964018c7311d485367252-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5964018c7311d485367252-2">2</div><div class="crayon-num" data-line="crayon-5964018c7311d485367252-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5964018c7311d485367252-4">4</div><div class="crayon-num" data-line="crayon-5964018c7311d485367252-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-5964018c7311d485367252-6">6</div><div class="crayon-num" data-line="crayon-5964018c7311d485367252-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-5964018c7311d485367252-8">8</div><div class="crayon-num" data-line="crayon-5964018c7311d485367252-9">9</div><div class="crayon-num crayon-striped-num" data-line="crayon-5964018c7311d485367252-10">10</div><div class="crayon-num" data-line="crayon-5964018c7311d485367252-11">11</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5964018c7311d485367252-1"><span class="crayon-e">def </span><span class="crayon-e">listener</span><span class="crayon-sy">(</span><span class="crayon-v">url</span><span class="crayon-sy">,</span><span class="crayon-v">interval</span><span class="crayon-sy">)</span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-p">#arguments are given when starting the program</span></div><div class="crayon-line crayon-striped-line" id="crayon-5964018c7311d485367252-2">&nbsp;</div><div class="crayon-line" id="crayon-5964018c7311d485367252-3"><span class="crayon-st">while</span><span class="crayon-h"> </span><span class="crayon-t">True</span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-p">#repeat</span></div><div class="crayon-line crayon-striped-line" id="crayon-5964018c7311d485367252-4">&nbsp;</div><div class="crayon-line" id="crayon-5964018c7311d485367252-5"><span class="crayon-st">if</span><span class="crayon-h"> </span><span class="crayon-v">finish_control</span><span class="crayon-h"> </span><span class="crayon-o">==</span><span class="crayon-h"> </span><span class="crayon-cn">1</span><span class="crayon-o">:</span></div><div class="crayon-line crayon-striped-line" id="crayon-5964018c7311d485367252-6">&nbsp;</div><div class="crayon-line" id="crayon-5964018c7311d485367252-7"><span class="crayon-st">break</span><span class="crayon-h"> </span><span class="crayon-p">#stop listening if the encryption is done</span></div><div class="crayon-line crayon-striped-line" id="crayon-5964018c7311d485367252-8">&nbsp;</div><div class="crayon-line" id="crayon-5964018c7311d485367252-9"><span class="crayon-e">check_url</span><span class="crayon-sy">(</span><span class="crayon-v">url</span><span class="crayon-sy">)</span><span class="crayon-h"> </span><span class="crayon-p">#checks for the start command and act accordingly</span></div><div class="crayon-line crayon-striped-line" id="crayon-5964018c7311d485367252-10">&nbsp;</div><div class="crayon-line" id="crayon-5964018c7311d485367252-11"><span class="crayon-e">sleep</span><span class="crayon-sy">(</span><span class="crayon-v">interval</span><span class="crayon-sy">)</span><span class="crayon-h"> </span><span class="crayon-p">#wait for specified time amount</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    Once the correct password is submitted, PHP script will write &#8220;1&#8221; to command.txt file and respond with a message &#8220;1Completed&#8221;. If the response is “0Completed” that means that there was an error writing to the command.txt file.</p>
    <p>Next time the listener checks that file, it will start the encryption and your files will be safe! Remember that the program doesn&#8217;t save used encryption keys so not even you will be able to get your files back. This is good because it eliminates the possibility of blackmailing you into decrypting the files.</p>
    <p>This is what should happen if someone tries to open an encrypted file when the job is done:</p>
    <p><img class="wp-image-15749 aligncenter" src="/imgs/2016/10/word-image-17.png" srcset="/imgs/2016/10/word-image-17.png 834w, /imgs/2016/10/word-image-17-300x182.png 300w" sizes="(max-width: 834px) 100vw, 834px"/></p>
    </div>
    <a href="https://www.deepdotweb.com/tag/evidence/" rel="tag">evidence</a> <a href="https://www.deepdotweb.com/tag/house/" rel="tag">house</a> <a href="https://www.deepdotweb.com/tag/party/" rel="tag">party</a> <a href="https://www.deepdotweb.com/tag/program/" rel="tag">program</a> <a href="https://www.deepdotweb.com/tag/protocol/" rel="tag">protocol</a> <a href="https://www.deepdotweb.com/tag/remote/" rel="tag">remote</a> <a href="https://www.deepdotweb.com/tag/wiper/" rel="tag">wiper</a></span> <span style="display:none" class="updated">2016-10-11</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/filipjelic/" title="Posts by Filip Jelic" rel="author">Filip Jelic</a></strong></div>
    
