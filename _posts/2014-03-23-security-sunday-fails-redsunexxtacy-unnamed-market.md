---
title: "Security Sunday Fail Trio: Redsun,EXXTACY &#038; Unnamed Market"
---

<span>March 23, 2014</span>
    

<p>Are we ever going to have a quiet week? i doubt it. but at least we can thank some of the security guys in Reddit for exposing yet another 3 security hazards in the form of new marketplaces, and this time 3 in one day! (well technically 2 since i kept one of them unnamed since it seem it was not really launched yet, doing the right thing probably)</p>
<p>So here we go:</p>
<p><span style="text-decoration: underline;"><strong>Red Sun Marketplace:</strong></span><br />
<span style="text-decoration: underline;">Problem</span>: SQL injection (among others)<br />
<span style="text-decoration: underline;">Was located at this address</span>: redsun4lvjrxwwuy.onion<br />
<span style="text-decoration: underline;">How it ended?</span> Was at least decent enough to take his marketplace down quickly after this.<br />
<span style="text-decoration: underline;">Original Thread</span>: http://www.reddit.com/r/DarkNetMarkets/comments/214y14/i_made_it_all_pretty_and_stuff/<br />
<span style="text-decoration: underline;">Exposed by:</span> <a href="http://www.reddit.com/user/the_avid">the_avid</a>  (from the epic <a href="https://gir.pub/deepdotweb/2014/01/27/the-drugslist-lesson-why-marketplace-security-should-not-be-taken-lightly/">drugslist lesson</a> , and the <a href="https://gir.pub/deepdotweb/2014/01/29/cantina-marketplace-pwnd-admin-password-was-password1/">cantina</a> fiasco)</p>
<div>
<div>
<blockquote><p><a href="http://prntscr.com/33fiyo">hey adminm, ruh roh<br />
</a>look on the bright side, if you ever lose your database you can email me and get a backup.<br />
    ps. took minutes. I wouldn&#8217;t leave you in charge of watering a plant.</p></blockquote>
</div>
</div>
<img src="https://gir.pub/deepdotweb/imgs/2014/03/VDMpbLU.png" />

<ol>
<li>redsun4lvjrxwwuy.onion/server-status</li>
<li>redsun4lvjrxwwuy.onion/phpinfo.php</li>
</ol>
<p><span style="text-decoration: underline;"><strong>EXXTACY Market:</strong></span><br />
    Located at: j3gwwsnswrg7dtf4.onion  &#8211;  Did not take his marketplace down even tough its pretty clear where this one is heading.<br />
    Presenting the craziest password requirements we have ever seen, and noting them as a &#8220;security feature&#8221;:</p>
<div id="crayon-5bd6e32fbc247334234541" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    Password must contain at least 2 lowercase characters.
    Password must contain at least 2 digits.
    Password must not contain the username.
    Password must contain at least 2 uppercase characters.
    Password must not match last 100 passwords.
    Password may only be changed in 2 hours from the last change.
    Password must be at least 12 characters in length.
    Password must contain at least 2 letters.
    Password must have a minimum of 2 digits in order to place any digits at the start or end of the password.</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5bd6e32fbc247334234541-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5bd6e32fbc247334234541-2">2</div><div class="crayon-num" data-line="crayon-5bd6e32fbc247334234541-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5bd6e32fbc247334234541-4">4</div><div class="crayon-num" data-line="crayon-5bd6e32fbc247334234541-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-5bd6e32fbc247334234541-6">6</div><div class="crayon-num" data-line="crayon-5bd6e32fbc247334234541-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-5bd6e32fbc247334234541-8">8</div><div class="crayon-num" data-line="crayon-5bd6e32fbc247334234541-9">9</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5bd6e32fbc247334234541-1"><span class="crayon-e">Password </span><span class="crayon-e">must </span><span class="crayon-e">contain </span><span class="crayon-e">at </span><span class="crayon-i">least</span><span class="crayon-h"> </span><span class="crayon-cn">2</span><span class="crayon-h"> </span><span class="crayon-e">lowercase </span><span class="crayon-v">characters</span><span class="crayon-sy">.</span></div><div class="crayon-line crayon-striped-line" id="crayon-5bd6e32fbc247334234541-2"><span class="crayon-e">Password </span><span class="crayon-e">must </span><span class="crayon-e">contain </span><span class="crayon-e">at </span><span class="crayon-i">least</span><span class="crayon-h"> </span><span class="crayon-cn">2</span><span class="crayon-h"> </span><span class="crayon-v">digits</span><span class="crayon-sy">.</span></div><div class="crayon-line" id="crayon-5bd6e32fbc247334234541-3"><span class="crayon-e">Password </span><span class="crayon-e">must </span><span class="crayon-st">not</span><span class="crayon-h"> </span><span class="crayon-e">contain </span><span class="crayon-e">the </span><span class="crayon-v">username</span><span class="crayon-sy">.</span></div><div class="crayon-line crayon-striped-line" id="crayon-5bd6e32fbc247334234541-4"><span class="crayon-e">Password </span><span class="crayon-e">must </span><span class="crayon-e">contain </span><span class="crayon-e">at </span><span class="crayon-i">least</span><span class="crayon-h"> </span><span class="crayon-cn">2</span><span class="crayon-h"> </span><span class="crayon-e">uppercase </span><span class="crayon-v">characters</span><span class="crayon-sy">.</span></div><div class="crayon-line" id="crayon-5bd6e32fbc247334234541-5"><span class="crayon-e">Password </span><span class="crayon-e">must </span><span class="crayon-st">not</span><span class="crayon-h"> </span><span class="crayon-e">match </span><span class="crayon-i">last</span><span class="crayon-h"> </span><span class="crayon-cn">100</span><span class="crayon-h"> </span><span class="crayon-v">passwords</span><span class="crayon-sy">.</span></div><div class="crayon-line crayon-striped-line" id="crayon-5bd6e32fbc247334234541-6"><span class="crayon-e">Password </span><span class="crayon-e">may </span><span class="crayon-e">only </span><span class="crayon-e">be </span><span class="crayon-e">changed </span><span class="crayon-st">in</span><span class="crayon-h"> </span><span class="crayon-cn">2</span><span class="crayon-h"> </span><span class="crayon-e">hours </span><span class="crayon-e">from </span><span class="crayon-e">the </span><span class="crayon-e">last </span><span class="crayon-v">change</span><span class="crayon-sy">.</span></div><div class="crayon-line" id="crayon-5bd6e32fbc247334234541-7"><span class="crayon-e">Password </span><span class="crayon-e">must </span><span class="crayon-e">be </span><span class="crayon-e">at </span><span class="crayon-i">least</span><span class="crayon-h"> </span><span class="crayon-cn">12</span><span class="crayon-h"> </span><span class="crayon-e">characters </span><span class="crayon-st">in</span><span class="crayon-h"> </span><span class="crayon-v">length</span><span class="crayon-sy">.</span></div><div class="crayon-line crayon-striped-line" id="crayon-5bd6e32fbc247334234541-8"><span class="crayon-e">Password </span><span class="crayon-e">must </span><span class="crayon-e">contain </span><span class="crayon-e">at </span><span class="crayon-i">least</span><span class="crayon-h"> </span><span class="crayon-cn">2</span><span class="crayon-h"> </span><span class="crayon-v">letters</span><span class="crayon-sy">.</span></div><div class="crayon-line" id="crayon-5bd6e32fbc247334234541-9"><span class="crayon-e">Password </span><span class="crayon-e">must </span><span class="crayon-i">have</span><span class="crayon-h"> </span><span class="crayon-i">a</span><span class="crayon-h"> </span><span class="crayon-e">minimum </span><span class="crayon-i">of</span><span class="crayon-h"> </span><span class="crayon-cn">2</span><span class="crayon-h"> </span><span class="crayon-e">digits </span><span class="crayon-st">in</span><span class="crayon-h"> </span><span class="crayon-e">order </span><span class="crayon-st">to</span><span class="crayon-h"> </span><span class="crayon-e">place </span><span class="crayon-e">any </span><span class="crayon-e">digits </span><span class="crayon-e">at </span><span class="crayon-e">the </span><span class="crayon-e">start </span><span class="crayon-st">or</span><span class="crayon-h"> </span><span class="crayon-st">end</span><span class="crayon-h"> </span><span class="crayon-e">of </span><span class="crayon-e">the </span><span class="crayon-v">password</span><span class="crayon-sy">.</span></div></div></td>
</tr>
</table>
</div>
</div>
    
<p>
    While on the other hand used Google to load scripts into the marketplace! Thank to the_avid again, for pointing this out, i was a bit busy and forgot to take a screenshot of this before it was patched (and i mean patched, not fixed):<br />


<img src="https://gir.pub/deepdotweb/imgs/2014/03/Exxcay.png"/>
<p>Even leaving the Generator tag in place:</p>
<div id="crayon-5bd6e32fbc254584406626" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    &amp;lt;meta name="&lt;a&gt;Generator&lt;/a&gt;" content="&lt;a&gt;Drupal 7 (http://drupal.org)&lt;/a&gt;" /&amp;gt;</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5bd6e32fbc254584406626-1">1</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5bd6e32fbc254584406626-1"><span class="crayon-o">&amp;</span><span class="crayon-v">lt</span><span class="crayon-sy">;</span><span class="crayon-e">meta </span><span class="crayon-v">name</span><span class="crayon-o">=</span><span class="crayon-s">"&lt;a&gt;Generator&lt;/a&gt;"</span><span class="crayon-h"> </span><span class="crayon-v">content</span><span class="crayon-o">=</span><span class="crayon-s">"&lt;a&gt;Drupal 7 (http://drupal.org)&lt;/a&gt;"</span><span class="crayon-h"> </span><span class="crayon-o">/</span><span class="crayon-o">&amp;</span><span class="crayon-v">gt</span><span class="crayon-sy">;</span></div></div></td>
</tr>
</table>
</div>
</div>
    
<p>
    You can read the original thread here: http://www.reddit.com/r/DarkNetMarkets/comments/215161/new_market_exxtacy/</p>
<p><span style="text-decoration: underline;"><strong>{Unnamed} marketplace:</strong></span><br />
    I will not name this marketplace since it was not made public so far<br />
    But it seems that this one was also leaking server info among some other issues that were not specified.<br />
    Currently at this address: {Hidden}  &#8211; This one is still active technically, but we will not post his address here unless he will decide to launch the marketplace before addressing these issues.<br />
    Another one of the markets to offer Innovative Security in his front page, just to leak the PHPinfo and some other server details:<br />
    Exposed by: {Hidden at this time}</p>
<p><strong>{Screenshot Hidden For Privacy reasons}</strong></p>
<p>We have no idea how this will end up for these markets, but we urge all users to do their research before using any of these markets (or any other market)</p>
<p>One of them was listed in our <a href="https://gir.pub/deepdotweb/2013/10/28/updated-llist-of-hidden-marketplaces-tor-i2p/">list of hidden</a> marketplaces but will be removed now</p>

Updated: 2014-03-23
    
