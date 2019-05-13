---
Security Sunday Fail Trio: Redsun,EXXTACY &#038; Unnamed Market
---
<article class="post-listing post-4768 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-fail tag-market tag-redsunexxtacy tag-security tag-sunday tag-trio tag-unnamed">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/admin/" title="">DeepDotWeb </a></span>
    <span>March 23, 2014</span>
    <span>in <a href="https://www.deepdotweb.com/category/articles/" rel="category tag">Articles</a>, <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a></span>
    <span><a href="https://www.deepdotweb.com/2014/03/23/security-sunday-fails-redsunexxtacy-unnamed-market/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Are we ever going to have a quiet week? i doubt it. but at least we can thank some of the security guys in Reddit for exposing yet another 3 security hazards in the form of new marketplaces, and this time 3 in one day! (well technically 2 since i kept one of them unnamed since it seem it was not really launched yet, doing the right thing probably)</p>
    <p>So here we go:</p>
    <p><span style="text-decoration: underline;"><strong>Red Sun Marketplace:</strong></span><br />
    <span style="text-decoration: underline;">Problem</span>: SQL injection (among others)<br />
    <span style="text-decoration: underline;">Was located at this address</span>: redsun4lvjrxwwuy.onion<br />
    <span style="text-decoration: underline;">How it ended?</span> Was at least decent enough to take his marketplace down quickly after this.<br />
    <span style="text-decoration: underline;">Original Thread</span>: http://www.reddit.com/r/DarkNetMarkets/comments/214y14/i_made_it_all_pretty_and_stuff/<br />
    <span style="text-decoration: underline;">Exposed by:</span> <a href="http://www.reddit.com/user/the_avid">the_avid</a>  (from the epic <a href="http://www.deepdotweb.com/2014/01/27/the-drugslist-lesson-why-marketplace-security-should-not-be-taken-lightly/">drugslist lesson</a> , and the <a href="http://www.deepdotweb.com/2014/01/29/cantina-marketplace-pwnd-admin-password-was-password1/">cantina</a> fiasco)</p>
    <div>
    <div>
    <blockquote><p><a href="http://prntscr.com/33fiyo">hey adminm, ruh roh<br />
    </a>look on the bright side, if you ever lose your database you can email me and get a backup.<br />
    ps. took minutes. I wouldn&#8217;t leave you in charge of watering a plant.</p></blockquote>
    </div>
    </div>
    <p><a href="/imgs/2014/03/VDMpbLU.png"><img class="aligncenter  wp-image-4769" alt="VDMpbLU" src="https://www.deepdotweb.com/wp-content/uploads/2014/03/VDMpbLU.png" width="779" height="277" srcset="https://www.deepdotweb.com/wp-content/uploads/2014/03/VDMpbLU.png 969w, https://www.deepdotweb.com/wp-content/uploads/2014/03/VDMpbLU-300x107.png 300w" sizes="(max-width: 779px) 100vw, 779px" /></a>And just to add by another user, <a href="http://www.reddit.com/user/luftwaffle8">luftwaffle8</a>, that he was also leaking Server info and Phpinfo:</p>
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
    <a href="/imgs/2014/03/Exxcay.png"><img class="aligncenter size-full wp-image-4771" alt="Exxcay" src="https://www.deepdotweb.com/wp-content/uploads/2014/03/Exxcay.png" width="937" height="186" srcset="https://www.deepdotweb.com/wp-content/uploads/2014/03/Exxcay.png 937w, https://www.deepdotweb.com/wp-content/uploads/2014/03/Exxcay-300x60.png 300w" sizes="(max-width: 937px) 100vw, 937px" /></a></p>
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
    <p>One of them was listed in our <a href="http://www.deepdotweb.com/2013/10/28/updated-llist-of-hidden-marketplaces-tor-i2p/">list of hidden</a> marketplaces but will be removed now</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/fail/" rel="tag">fail</a> <a href="https://www.deepdotweb.com/tag/market/" rel="tag">market</a> <a href="https://www.deepdotweb.com/tag/redsunexxtacy/" rel="tag">redsunexxtacy</a> <a href="https://www.deepdotweb.com/tag/security/" rel="tag">security</a> <a href="https://www.deepdotweb.com/tag/sunday/" rel="tag">sunday</a> <a href="https://www.deepdotweb.com/tag/trio/" rel="tag">trio</a> <a href="https://www.deepdotweb.com/tag/unnamed/" rel="tag">unnamed</a></span> <span style="display:none" class="updated">2014-03-23</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/admin/" title="Posts by DeepDotWeb" rel="author">DeepDotWeb</a></strong></div>
    </div>
</article>

