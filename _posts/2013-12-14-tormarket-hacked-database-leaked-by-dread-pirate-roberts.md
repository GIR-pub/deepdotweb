---
title: "Tormarket Hacked &#8211; Database Leaked By&#8230; Dread Pirate Roberts"
---


<span>Posted by: DeepDotWeb </span>
<span>December 14, 2013</span>
<span>in <a href="https://gir.pub/deepdotweb/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://gir.pub/deepdotweb/category/news-updates/" rel="category tag">News Updates</a></span>
<span><a href="https://gir.pub/deepdotweb/2013/12/14/tormarket-hacked-database-leaked-by-dread-pirate-roberts/#comments">3 Comments</a></span>


<p>Following our previous report regarding the mutual <a href="https://gir.pub/deepdotweb/2013/12/13/so-whats-going-on-with-all-these-ddos-attacks/">DDOS attacks of the darknet markets</a>,  the situation has just escalated to a full marketplace Cyberwar as Dread Pirate Roberts posted a proof showing that he has the database of the competing market TOR marketplace (link to the original thread on SR2 Forums: http://silkroad5v7dywlc.onion/index.php?topic=8598.0):</p>
<p>=======================START QUOTE===================</p>
<blockquote><p>To start, I would like to make this clear to everyone involved that Silk Road does not have malicious intentions or an anti-competition attitude, we actually require competition to keep us motivated and for the diversity of the network but in order to fulfill that function the competition must be a safe one which does not put people in harms way or subject to possible exploit. This post I hope will demonstrate to you why claims a market makes does not correlate to the true story and we would like to demonstrate this with Tormarket.</p>
<p>At this moment in time, I also want to clarify in light of recent events the full disclosure everyone deserves to know. This investigation started under the suspicion that Tormarket was behind the ongoing DDOS against Silk Road but has since taken another turn when we looked below the surface a little more. I have no conclusive proof Tormarket did or did not order the DDOS currently hitting us and personally I don&#8217;t believe I ever will so I won&#8217;t go on about this much more as it is actually not something that matters any more since we are definitely en route to fixing it if you have watched our recent developments, but over Tor such attacks are not trivial to correct. All of this is done in the name of safety and I hope the owners of Tormarket can take this seriously, go away and rethink their strategies because as I will discuss later we didn&#8217;t even put much effort in to extracting this data.</p>
<p><strong>What is it I am attempting to prove?</strong></p>
<p>To take it from the home page of Tormarket, I wish to publicly overturn the rumors and falsehoods of some of the below:</p>
<div>
<div>Quote from: TorMarket</div>
</div>
<p>Darknet Market done right</p>
<p>Secure codebase, competent operators, and common sense.</p>
<p>Common sense I will allow that to pass as a subjective matter and how they wish to operate their market is none of my business. Competent operators &#8211; again it would depend on your individual definition of that. Secure codebase &#8211; let us put that to the test.</p>
<p><strong>Let&#8217;s start with the basics</strong></p>
<p>One of the most valuable pieces of any website is the database. It controls so many parts of the site and without it there could be no effective market, so we started trying to extract the information from that. Surprise surprise, it didn&#8217;t take long to grab the structure:</p>
<div>Code: <a>[Select]</a></div>
    
<div id="crayon-581cb69c9ef2d133486314" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    orders table
    - id
    - price
    - status
    - qt
    - address
    - notes
    - crypto_currency_id
    - buyer_id
    - buyer_username
    - vendor_username
    - vendor_id
    
    vendor table
    - id
    - username
    - banned
    - currency
    - location
    - messages_id
    - messages_body</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-581cb69c9ef2d133486314-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef2d133486314-2">2</div><div class="crayon-num" data-line="crayon-581cb69c9ef2d133486314-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef2d133486314-4">4</div><div class="crayon-num" data-line="crayon-581cb69c9ef2d133486314-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef2d133486314-6">6</div><div class="crayon-num" data-line="crayon-581cb69c9ef2d133486314-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef2d133486314-8">8</div><div class="crayon-num" data-line="crayon-581cb69c9ef2d133486314-9">9</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef2d133486314-10">10</div><div class="crayon-num" data-line="crayon-581cb69c9ef2d133486314-11">11</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef2d133486314-12">12</div><div class="crayon-num" data-line="crayon-581cb69c9ef2d133486314-13">13</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef2d133486314-14">14</div><div class="crayon-num" data-line="crayon-581cb69c9ef2d133486314-15">15</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef2d133486314-16">16</div><div class="crayon-num" data-line="crayon-581cb69c9ef2d133486314-17">17</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef2d133486314-18">18</div><div class="crayon-num" data-line="crayon-581cb69c9ef2d133486314-19">19</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef2d133486314-20">20</div><div class="crayon-num" data-line="crayon-581cb69c9ef2d133486314-21">21</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-581cb69c9ef2d133486314-1"><span class="crayon-e">orders </span><span class="crayon-i">table</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef2d133486314-2"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-i">id</span></div><div class="crayon-line" id="crayon-581cb69c9ef2d133486314-3"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-i">price</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef2d133486314-4"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-i">status</span></div><div class="crayon-line" id="crayon-581cb69c9ef2d133486314-5"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-i">qt</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef2d133486314-6"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-i">address</span></div><div class="crayon-line" id="crayon-581cb69c9ef2d133486314-7"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-i">notes</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef2d133486314-8"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-v">crypto_currency</span><span class="crayon-sy">_</span>id<span class="crayon-h"> </span></div><div class="crayon-line" id="crayon-581cb69c9ef2d133486314-9"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-v">buyer</span><span class="crayon-sy">_</span>id</div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef2d133486314-10"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-v">buyer</span><span class="crayon-sy">_</span>username</div><div class="crayon-line" id="crayon-581cb69c9ef2d133486314-11"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-v">vendor</span><span class="crayon-sy">_</span>username</div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef2d133486314-12"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-e">vendor_id</span></div><div class="crayon-line" id="crayon-581cb69c9ef2d133486314-13">&nbsp;</div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef2d133486314-14"><span class="crayon-e">vendor </span><span class="crayon-i">table</span></div><div class="crayon-line" id="crayon-581cb69c9ef2d133486314-15"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-i">id</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef2d133486314-16"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-i">username</span></div><div class="crayon-line" id="crayon-581cb69c9ef2d133486314-17"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-i">banned</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef2d133486314-18"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-i">currency</span></div><div class="crayon-line" id="crayon-581cb69c9ef2d133486314-19"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-i">location</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef2d133486314-20"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-v">messages</span><span class="crayon-sy">_</span>id</div><div class="crayon-line" id="crayon-581cb69c9ef2d133486314-21"> <span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-v">messages_body</span></div></div></td>
</tr>
</table>
</div>
</div>
    
    Now we&#8217;ve had a sneak peak at their table structure, it was decided to have a trawl through the messages that vendors had sent to customers. We will list a little segment below, some vendors here might recognize their own messages with of course sensitive information removed from below.</p>
<div>Code: <a>[Select]</a></div>
    
<div id="crayon-581cb69c9ef3f037753930" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    Paulwalker : thank you.
    S0wl : has been sent.  if?
    17538 : here's a screenshot
    Strings999 : hello,i was sent an invite while
    OGCorleone : hello, thanks for your order :)
    Puntitot1 : has been sent.  if?
    Berndman : hello,  your order is ready to ship.  you have to finalize now.
    Crepuscular : hello,  did you order here or on  heep? what am i missing?
    Jackpot1875 : hello,  your order is ready to ship.  you have to finalize now.
    Spartanec731 : hello to  you as well . indeed it is the original haizenberg , and offence non taken , :)
    Dogtanian : hello my friend good to hear from you,
    Levlvov70 : hehe i was joking, but you seem cool man. i ll send you a sample of one each...
    Az12er34ty56 : hello!  i requiered a seller account here  i am matrixx on bmr with more than 180 positives feedback!
    Strom : hello,  your order is ready to ship.  you have to finalize now.
    MickeyMantle : hi there, when your product has arrived please mark as arrived and set a positive feedback on your experience
    Qwertyqazwsx : haha, won't do so brother... your order will ship asap.
    Toefia : abgemacht. dann sind 7 tage rum und dann kann ich dir reship anbieten.
    Spaniard : always verify identity using pgp key
    Gtiv : allso mit unserem shop werden wir im lauf der nexten woche online gehen. wenn du willst kanst du auch dar ber verkauf n. wegen den geb ren bist du mit 1  einverstanden?  einfach f r hosting arbeit usw. ich werde noch ein paar andere verkaufer fragen ab
    JTLeary : always verify identity using pgp key
    MrTrump : ah yes i just saw it! i think with out 1700 orders and 100  feedback on sheep it will be going strong! -)
    Slappfisk : bare
    Piccolabesti : azi fb
    Mushinmusa : bajs fr n katter?...   </textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-581cb69c9ef3f037753930-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef3f037753930-2">2</div><div class="crayon-num" data-line="crayon-581cb69c9ef3f037753930-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef3f037753930-4">4</div><div class="crayon-num" data-line="crayon-581cb69c9ef3f037753930-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef3f037753930-6">6</div><div class="crayon-num" data-line="crayon-581cb69c9ef3f037753930-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef3f037753930-8">8</div><div class="crayon-num" data-line="crayon-581cb69c9ef3f037753930-9">9</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef3f037753930-10">10</div><div class="crayon-num" data-line="crayon-581cb69c9ef3f037753930-11">11</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef3f037753930-12">12</div><div class="crayon-num" data-line="crayon-581cb69c9ef3f037753930-13">13</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef3f037753930-14">14</div><div class="crayon-num" data-line="crayon-581cb69c9ef3f037753930-15">15</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef3f037753930-16">16</div><div class="crayon-num" data-line="crayon-581cb69c9ef3f037753930-17">17</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef3f037753930-18">18</div><div class="crayon-num" data-line="crayon-581cb69c9ef3f037753930-19">19</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef3f037753930-20">20</div><div class="crayon-num" data-line="crayon-581cb69c9ef3f037753930-21">21</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef3f037753930-22">22</div><div class="crayon-num" data-line="crayon-581cb69c9ef3f037753930-23">23</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef3f037753930-24">24</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-581cb69c9ef3f037753930-1"><span class="crayon-v">Paulwalker</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">thank </span><span class="crayon-v">you</span><span class="crayon-sy">.</span> <span class="crayon-h"> </span> </div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef3f037753930-2"><span class="crayon-v">S0wl</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">has </span><span class="crayon-e">been </span><span class="crayon-v">sent</span><span class="crayon-sy">.</span> <span class="crayon-h"> </span><span class="crayon-st">if</span><span class="crayon-sy">?</span> <span class="crayon-h"> </span> </div><div class="crayon-line" id="crayon-581cb69c9ef3f037753930-3"><span class="crayon-cn">17538</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-i">here</span><span class="crayon-s">'s a screenshot   </span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef3f037753930-4"><span class="crayon-s">Strings999 : hello,i was sent an invite while   </span></div><div class="crayon-line" id="crayon-581cb69c9ef3f037753930-5"><span class="crayon-s">OGCorleone : hello, thanks for your order :)   </span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef3f037753930-6"><span class="crayon-s">Puntitot1 : has been sent.  if?   </span></div><div class="crayon-line" id="crayon-581cb69c9ef3f037753930-7"><span class="crayon-s">Berndman : hello,  your order is ready to ship.  you have to finalize now.   </span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef3f037753930-8"><span class="crayon-s">Crepuscular : hello,  did you order here or on  heep? what am i missing?   </span></div><div class="crayon-line" id="crayon-581cb69c9ef3f037753930-9"><span class="crayon-s">Jackpot1875 : hello,  your order is ready to ship.  you have to finalize now.   </span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef3f037753930-10"><span class="crayon-s">Spartanec731 : hello to  you as well . indeed it is the original haizenberg , and offence non taken , :)   </span></div><div class="crayon-line" id="crayon-581cb69c9ef3f037753930-11"><span class="crayon-s">Dogtanian : hello my friend good to hear from you,   </span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef3f037753930-12"><span class="crayon-s">Levlvov70 : hehe i was joking, but you seem cool man. i ll send you a sample of one each...   </span></div><div class="crayon-line" id="crayon-581cb69c9ef3f037753930-13"><span class="crayon-s">Az12er34ty56 : hello!  i requiered a seller account here  i am matrixx on bmr with more than 180 positives feedback!   </span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef3f037753930-14"><span class="crayon-s">Strom : hello,  your order is ready to ship.  you have to finalize now.   </span></div><div class="crayon-line" id="crayon-581cb69c9ef3f037753930-15"><span class="crayon-s">MickeyMantle : hi there, when your product has arrived please mark as arrived and set a positive feedback on your experience   </span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef3f037753930-16"><span class="crayon-s">Qwertyqazwsx : haha, won'</span><span class="crayon-i">t</span><span class="crayon-h"> </span><span class="crayon-st">do</span><span class="crayon-h"> </span><span class="crayon-e">so </span><span class="crayon-v">brother</span><span class="crayon-sy">.</span><span class="crayon-sy">.</span><span class="crayon-sy">.</span><span class="crayon-h"> </span><span class="crayon-e">your </span><span class="crayon-e">order </span><span class="crayon-e">will </span><span class="crayon-e">ship </span><span class="crayon-v">asap</span><span class="crayon-sy">.</span> <span class="crayon-h"> </span> </div><div class="crayon-line" id="crayon-581cb69c9ef3f037753930-17"><span class="crayon-v">Toefia</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-v">abgemacht</span><span class="crayon-sy">.</span><span class="crayon-h"> </span><span class="crayon-e">dann </span><span class="crayon-i">sind</span><span class="crayon-h"> </span><span class="crayon-cn">7</span><span class="crayon-h"> </span><span class="crayon-e">tage </span><span class="crayon-e">rum </span><span class="crayon-e">und </span><span class="crayon-e">dann </span><span class="crayon-e">kann </span><span class="crayon-e">ich </span><span class="crayon-e">dir </span><span class="crayon-e">reship </span><span class="crayon-v">anbieten</span><span class="crayon-sy">.</span> <span class="crayon-h"> </span> </div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef3f037753930-18"><span class="crayon-v">Spaniard</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">always </span><span class="crayon-e">verify </span><span class="crayon-e">identity </span><span class="crayon-e">using </span><span class="crayon-e">pgp </span><span class="crayon-i">key</span> <span class="crayon-h"> </span> </div><div class="crayon-line" id="crayon-581cb69c9ef3f037753930-19"><span class="crayon-v">Gtiv</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">allso </span><span class="crayon-e">mit </span><span class="crayon-e">unserem </span><span class="crayon-e">shop </span><span class="crayon-e">werden </span><span class="crayon-e">wir </span><span class="crayon-e">im </span><span class="crayon-e">lauf </span><span class="crayon-e">der </span><span class="crayon-e">nexten </span><span class="crayon-e">woche </span><span class="crayon-e">online </span><span class="crayon-v">gehen</span><span class="crayon-sy">.</span><span class="crayon-h"> </span><span class="crayon-e">wenn </span><span class="crayon-e">du </span><span class="crayon-e">willst </span><span class="crayon-e">kanst </span><span class="crayon-e">du </span><span class="crayon-e">auch </span><span class="crayon-e">dar </span><span class="crayon-e">ber </span><span class="crayon-i">verkauf</span><span class="crayon-h"> </span><span class="crayon-v">n</span><span class="crayon-sy">.</span><span class="crayon-h"> </span><span class="crayon-e">wegen </span><span class="crayon-e">den </span><span class="crayon-e">geb </span><span class="crayon-e">ren </span><span class="crayon-e">bist </span><span class="crayon-e">du </span><span class="crayon-i">mit</span><span class="crayon-h"> </span><span class="crayon-cn">1</span> <span class="crayon-h"> </span><span class="crayon-v">einverstanden</span><span class="crayon-sy">?</span> <span class="crayon-h"> </span><span class="crayon-i">einfach</span><span class="crayon-h"> </span><span class="crayon-i">f</span><span class="crayon-h"> </span><span class="crayon-i">r</span><span class="crayon-h"> </span><span class="crayon-e">hosting </span><span class="crayon-e">arbeit </span><span class="crayon-v">usw</span><span class="crayon-sy">.</span><span class="crayon-h"> </span><span class="crayon-e">ich </span><span class="crayon-e">werde </span><span class="crayon-e">noch </span><span class="crayon-e">ein </span><span class="crayon-e">paar </span><span class="crayon-e">andere </span><span class="crayon-e">verkaufer </span><span class="crayon-e">fragen </span><span class="crayon-e">ab</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef3f037753930-20"><span class="crayon-v">JTLeary</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">always </span><span class="crayon-e">verify </span><span class="crayon-e">identity </span><span class="crayon-e">using </span><span class="crayon-e">pgp </span><span class="crayon-e">key</span></div><div class="crayon-line" id="crayon-581cb69c9ef3f037753930-21"><span class="crayon-v">MrTrump</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">ah </span><span class="crayon-i">yes</span><span class="crayon-h"> </span><span class="crayon-i">i</span><span class="crayon-h"> </span><span class="crayon-e">just </span><span class="crayon-e">saw </span><span class="crayon-v">it</span><span class="crayon-o">!</span><span class="crayon-h"> </span><span class="crayon-i">i</span><span class="crayon-h"> </span><span class="crayon-e">think </span><span class="crayon-e">with </span><span class="crayon-i">out</span><span class="crayon-h"> </span><span class="crayon-cn">1700</span><span class="crayon-h"> </span><span class="crayon-e">orders </span><span class="crayon-st">and</span><span class="crayon-h"> </span><span class="crayon-cn">100</span> <span class="crayon-h"> </span><span class="crayon-e">feedback </span><span class="crayon-e">on </span><span class="crayon-e">sheep </span><span class="crayon-e">it </span><span class="crayon-e">will </span><span class="crayon-e">be </span><span class="crayon-e">going </span><span class="crayon-v">strong</span><span class="crayon-o">!</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-sy">)</span><span class="crayon-h"> </span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef3f037753930-22"><span class="crayon-v">Slappfisk</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-i">bare</span> <span class="crayon-h"> </span> </div><div class="crayon-line" id="crayon-581cb69c9ef3f037753930-23"><span class="crayon-v">Piccolabesti</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">azi </span><span class="crayon-i">fb</span> <span class="crayon-h"> </span> </div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef3f037753930-24"><span class="crayon-v">Mushinmusa</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">bajs </span><span class="crayon-i">fr</span><span class="crayon-h"> </span><span class="crayon-i">n</span><span class="crayon-h"> </span><span class="crayon-v">katter</span><span class="crayon-sy">?</span><span class="crayon-sy">.</span><span class="crayon-sy">.</span><span class="crayon-sy">.</span> <span class="crayon-h"> </span> </div></div></td>
</tr>
</table>
</div>
</div>
    
    Then an order note which was from a buyer to a vendor, we&#8217;ll keep this very select for obvious reasons:</p>
<div>Code: <a>[Select]</a></div>
    
<div id="crayon-581cb69c9ef4c500279208" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    From: JackCubrick
    To: GodfatherNL
    Purchase:  *** 1 gram pure uncut cocaine ***
    Message: hey there. please ship asap as i would like to place a large order before christmas once i have confirmed weigh in and quality</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-581cb69c9ef4c500279208-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef4c500279208-2">2</div><div class="crayon-num" data-line="crayon-581cb69c9ef4c500279208-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef4c500279208-4">4</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-581cb69c9ef4c500279208-1"><span class="crayon-v">From</span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">JackCubrick</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef4c500279208-2"><span class="crayon-st">To</span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">GodfatherNL</span></div><div class="crayon-line" id="crayon-581cb69c9ef4c500279208-3"><span class="crayon-v">Purchase</span><span class="crayon-o">:</span> <span class="crayon-h"> </span><span class="crayon-o">*</span><span class="crayon-o">*</span><span class="crayon-o">*</span><span class="crayon-h"> </span><span class="crayon-cn">1</span><span class="crayon-h"> </span><span class="crayon-e">gram </span><span class="crayon-e">pure </span><span class="crayon-e">uncut </span><span class="crayon-e ">cocaine *</span><span class="crayon-o">*</span><span class="crayon-o">*</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef4c500279208-4"><span class="crayon-v">Message</span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">hey </span><span class="crayon-v">there</span><span class="crayon-sy">.</span><span class="crayon-h"> </span><span class="crayon-e">please </span><span class="crayon-e">ship </span><span class="crayon-e">asap </span><span class="crayon-st">as</span><span class="crayon-h"> </span><span class="crayon-i">i</span><span class="crayon-h"> </span><span class="crayon-e">would </span><span class="crayon-e">like </span><span class="crayon-st">to</span><span class="crayon-h"> </span><span class="crayon-i">place</span><span class="crayon-h"> </span><span class="crayon-i">a</span><span class="crayon-h"> </span><span class="crayon-e">large </span><span class="crayon-e">order </span><span class="crayon-e">before </span><span class="crayon-e">christmas </span><span class="crayon-i">once</span><span class="crayon-h"> </span><span class="crayon-i">i</span><span class="crayon-h"> </span><span class="crayon-e">have </span><span class="crayon-e">confirmed </span><span class="crayon-e">weigh </span><span class="crayon-st">in</span><span class="crayon-h"> </span><span class="crayon-st">and</span><span class="crayon-h"> </span><span class="crayon-v">quality</span></div></div></td>
</tr>
</table>
</div>
</div>
    
    Worried? So were we.</p>
<hr/>
<p>Up to this point we weren&#8217;t looking for any kind of mass data extraction, but in the interest of ensuring the users of Tormarket are safe, we had to do it anyway. The summary of some of the data we went through was to see who the top buyers were, something of equal interest to law enforcement as vendors except it is more likely a buyer will have leaked personal information on the site than a vendor. So who are the top buyers:</p>
<div>Code: <a>[Select]</a></div>
    
<div id="crayon-581cb69c9ef55031949316" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    Top 15 Buyers by number of products purchased
    
    Buyer ID   Buyer Name
    16759      icq
    13621      jackcubrick
    12226      shedrik
    11994      dreamsage
    13100      purpleextreme
    12274      [redacted]
    18634      [redacted]
    10625      sebb66g
    13572      choicethespi
    16611      felsad
    14731      marvel
    11001      madcunt33
    13127      sleep12
    18308      roxas50
    13132      rstevens</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-581cb69c9ef55031949316-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef55031949316-2">2</div><div class="crayon-num" data-line="crayon-581cb69c9ef55031949316-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef55031949316-4">4</div><div class="crayon-num" data-line="crayon-581cb69c9ef55031949316-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef55031949316-6">6</div><div class="crayon-num" data-line="crayon-581cb69c9ef55031949316-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef55031949316-8">8</div><div class="crayon-num" data-line="crayon-581cb69c9ef55031949316-9">9</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef55031949316-10">10</div><div class="crayon-num" data-line="crayon-581cb69c9ef55031949316-11">11</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef55031949316-12">12</div><div class="crayon-num" data-line="crayon-581cb69c9ef55031949316-13">13</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef55031949316-14">14</div><div class="crayon-num" data-line="crayon-581cb69c9ef55031949316-15">15</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef55031949316-16">16</div><div class="crayon-num" data-line="crayon-581cb69c9ef55031949316-17">17</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef55031949316-18">18</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-581cb69c9ef55031949316-1"><span class="crayon-i">Top</span><span class="crayon-h"> </span><span class="crayon-cn">15</span><span class="crayon-h"> </span><span class="crayon-e">Buyers </span><span class="crayon-e">by </span><span class="crayon-e">number </span><span class="crayon-e">of </span><span class="crayon-e">products </span><span class="crayon-e">purchased</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef55031949316-2">&nbsp;</div><div class="crayon-line" id="crayon-581cb69c9ef55031949316-3"><span class="crayon-e">Buyer </span><span class="crayon-i">ID</span> <span class="crayon-h"> </span> <span class="crayon-e">Buyer </span><span class="crayon-i">Name</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef55031949316-4"><span class="crayon-cn">16759</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">icq</span></div><div class="crayon-line" id="crayon-581cb69c9ef55031949316-5"><span class="crayon-cn">13621</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">jackcubrick</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef55031949316-6"><span class="crayon-cn">12226</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">shedrik</span></div><div class="crayon-line" id="crayon-581cb69c9ef55031949316-7"><span class="crayon-cn">11994</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">dreamsage</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef55031949316-8"><span class="crayon-cn">13100</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">purpleextreme</span></div><div class="crayon-line" id="crayon-581cb69c9ef55031949316-9"><span class="crayon-cn">12274</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-sy">[</span><span class="crayon-v">redacted</span><span class="crayon-sy">]</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef55031949316-10"><span class="crayon-cn">18634</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-sy">[</span><span class="crayon-v">redacted</span><span class="crayon-sy">]</span></div><div class="crayon-line" id="crayon-581cb69c9ef55031949316-11"><span class="crayon-cn">10625</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">sebb66g</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef55031949316-12"><span class="crayon-cn">13572</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">choicethespi</span></div><div class="crayon-line" id="crayon-581cb69c9ef55031949316-13"><span class="crayon-cn">16611</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">felsad</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef55031949316-14"><span class="crayon-cn">14731</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">marvel</span></div><div class="crayon-line" id="crayon-581cb69c9ef55031949316-15"><span class="crayon-cn">11001</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">madcunt33</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef55031949316-16"><span class="crayon-cn">13127</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">sleep12</span></div><div class="crayon-line" id="crayon-581cb69c9ef55031949316-17"><span class="crayon-cn">18308</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">roxas50</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef55031949316-18"><span class="crayon-cn">13132</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-v">rstevens</span></div></div></td>
</tr>
</table>
</div>
</div>
    
    So user icq has the highest amount of products purchased. We investigated a little further to see precisely what he bought (and we could do this for every buyer I would like to point out):</p>
<div>Code: <a>[Select]</a></div>
    
<div id="crayon-581cb69c9ef5f353367188" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    ID      Buyer      Vendor      Product
    16759      icq      moneysell      Brazzers.com - [LIFETIME PORN PREMIUM ACCOUNT]
    16759      icq      rainbowbear      INTERNATIONAL 100 grams bulk methylone M1 moonrock 99.9% purity
    16759      icq      moneysell      Teenpornopass.com - [LIFETIME PORN PREMIUM ACCOUNT]
    16759      icq      moneysell      PornPros.com - [LIFETIME PORN PREMIUM ACCOUNT]
    16759      icq      moneysell      Asiansexdiary.com - [LIFETIME PORN PREMIUM ACCOUNT]
    16759      icq      moneysell      Babes.com - [LIFETIME PORN PREMIUM ACCOUNT]
    16759      icq      dipsycards      An Idiot's Guide to Fleeing to Mexico
    16759      icq      positive      Xbox One Console!
    16759      icq      moneysell      3dxstar.com - [LIFETIME PORN PREMIUM ACCOUNT]
    16759      icq      moneysell      Sexart.com - [LIFETIME PORN PREMIUM ACCOUNT]</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-581cb69c9ef5f353367188-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef5f353367188-2">2</div><div class="crayon-num" data-line="crayon-581cb69c9ef5f353367188-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef5f353367188-4">4</div><div class="crayon-num" data-line="crayon-581cb69c9ef5f353367188-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef5f353367188-6">6</div><div class="crayon-num" data-line="crayon-581cb69c9ef5f353367188-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef5f353367188-8">8</div><div class="crayon-num" data-line="crayon-581cb69c9ef5f353367188-9">9</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef5f353367188-10">10</div><div class="crayon-num" data-line="crayon-581cb69c9ef5f353367188-11">11</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-581cb69c9ef5f353367188-1"><span class="crayon-i">ID</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">Buyer</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">Vendor</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">Product</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef5f353367188-2"><span class="crayon-cn">16759</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">icq</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">moneysell</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-v">Brazzers</span><span class="crayon-sy">.</span><span class="crayon-v">com</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-sy">[</span><span class="crayon-e">LIFETIME </span><span class="crayon-e">PORN </span><span class="crayon-e">PREMIUM </span><span class="crayon-v">ACCOUNT</span><span class="crayon-sy">]</span></div><div class="crayon-line" id="crayon-581cb69c9ef5f353367188-3"><span class="crayon-cn">16759</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">icq</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">rainbowbear</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">INTERNATIONAL</span><span class="crayon-h"> </span><span class="crayon-cn">100</span><span class="crayon-h"> </span><span class="crayon-e">grams </span><span class="crayon-e">bulk </span><span class="crayon-e">methylone </span><span class="crayon-e">M1 </span><span class="crayon-i">moonrock</span><span class="crayon-h"> </span><span class="crayon-cn">99.9</span><span class="crayon-o">%</span><span class="crayon-h"> </span><span class="crayon-i">purity</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef5f353367188-4"><span class="crayon-cn">16759</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">icq</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">moneysell</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-v">Teenpornopass</span><span class="crayon-sy">.</span><span class="crayon-v">com</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-sy">[</span><span class="crayon-e">LIFETIME </span><span class="crayon-e">PORN </span><span class="crayon-e">PREMIUM </span><span class="crayon-v">ACCOUNT</span><span class="crayon-sy">]</span></div><div class="crayon-line" id="crayon-581cb69c9ef5f353367188-5"><span class="crayon-cn">16759</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">icq</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">moneysell</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-v">PornPros</span><span class="crayon-sy">.</span><span class="crayon-v">com</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-sy">[</span><span class="crayon-e">LIFETIME </span><span class="crayon-e">PORN </span><span class="crayon-e">PREMIUM </span><span class="crayon-v">ACCOUNT</span><span class="crayon-sy">]</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef5f353367188-6"><span class="crayon-cn">16759</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">icq</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">moneysell</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-v">Asiansexdiary</span><span class="crayon-sy">.</span><span class="crayon-v">com</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-sy">[</span><span class="crayon-e">LIFETIME </span><span class="crayon-e">PORN </span><span class="crayon-e">PREMIUM </span><span class="crayon-v">ACCOUNT</span><span class="crayon-sy">]</span></div><div class="crayon-line" id="crayon-581cb69c9ef5f353367188-7"><span class="crayon-cn">16759</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">icq</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">moneysell</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-v">Babes</span><span class="crayon-sy">.</span><span class="crayon-v">com</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-sy">[</span><span class="crayon-e">LIFETIME </span><span class="crayon-e">PORN </span><span class="crayon-e">PREMIUM </span><span class="crayon-v">ACCOUNT</span><span class="crayon-sy">]</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef5f353367188-8"><span class="crayon-cn">16759</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">icq</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">dipsycards</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-e">An </span><span class="crayon-i">Idiot</span>'<span class="crayon-i">s</span><span class="crayon-h"> </span><span class="crayon-e">Guide </span><span class="crayon-st">to</span><span class="crayon-h"> </span><span class="crayon-e">Fleeing </span><span class="crayon-st">to</span><span class="crayon-h"> </span><span class="crayon-i">Mexico</span></div><div class="crayon-line" id="crayon-581cb69c9ef5f353367188-9"><span class="crayon-cn">16759</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">icq</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">positive</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-e">Xbox </span><span class="crayon-e">One </span><span class="crayon-v">Console</span><span class="crayon-o">!</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef5f353367188-10"><span class="crayon-cn">16759</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">icq</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">moneysell</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-cn">3dxstar.com</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-sy">[</span><span class="crayon-e">LIFETIME </span><span class="crayon-e">PORN </span><span class="crayon-e">PREMIUM </span><span class="crayon-v">ACCOUNT</span><span class="crayon-sy">]</span></div><div class="crayon-line" id="crayon-581cb69c9ef5f353367188-11"><span class="crayon-cn">16759</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">icq</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-i">moneysell</span> <span class="crayon-h"> </span> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-v">Sexart</span><span class="crayon-sy">.</span><span class="crayon-v">com</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-sy">[</span><span class="crayon-e">LIFETIME </span><span class="crayon-e">PORN </span><span class="crayon-e">PREMIUM </span><span class="crayon-v">ACCOUNT</span><span class="crayon-sy">]</span></div></div></td>
</tr>
</table>
</div>
</div>
    
    Somebody tell him you don&#8217;t need to pay these days. Let&#8217;s try another (jackcubrick):</p>
<div>Code: <a>[Select]</a></div>
    
<div id="crayon-581cb69c9ef6a959472083" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    Purchases made by jackcubrick
    Vendor: Product
    
    PureHeaven : 3 Grams of Tested 90% Cocaine...Verified Vendor!
    ozconnection L 1 gram Peru Cocaine Australia
    sunwu : 250mg Pure Alprazolam Powder (Xanax) - USA
    tomorrowman : 3 grams tan mdma crystals 85%+ purity
    demoniak : 2GR PINK Speed (dry)
    sunwu : 250mg Pure Alprazolam Powder (Xanax) - UK
    wilfred : 3.5g Hydroponic BUDS - HIGH THC - New Vendor Special !!
    justincase : 10 regular seeds - Hindu&amp;amp;#39;s Shiva
    uperspeedbros : 2g of Speed -- Amphetamine sulfate
    godfathernl : *** 1 gram pure uncut cocaine  ***</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-581cb69c9ef6a959472083-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef6a959472083-2">2</div><div class="crayon-num" data-line="crayon-581cb69c9ef6a959472083-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef6a959472083-4">4</div><div class="crayon-num" data-line="crayon-581cb69c9ef6a959472083-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef6a959472083-6">6</div><div class="crayon-num" data-line="crayon-581cb69c9ef6a959472083-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef6a959472083-8">8</div><div class="crayon-num" data-line="crayon-581cb69c9ef6a959472083-9">9</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef6a959472083-10">10</div><div class="crayon-num" data-line="crayon-581cb69c9ef6a959472083-11">11</div><div class="crayon-num crayon-striped-num" data-line="crayon-581cb69c9ef6a959472083-12">12</div><div class="crayon-num" data-line="crayon-581cb69c9ef6a959472083-13">13</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-581cb69c9ef6a959472083-1"><span class="crayon-e">Purchases </span><span class="crayon-e">made </span><span class="crayon-e">by </span><span class="crayon-e">jackcubrick</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef6a959472083-2"><span class="crayon-v">Vendor</span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-e">Product</span></div><div class="crayon-line" id="crayon-581cb69c9ef6a959472083-3">&nbsp;</div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef6a959472083-4"><span class="crayon-v">PureHeaven</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-cn">3</span><span class="crayon-h"> </span><span class="crayon-e">Grams </span><span class="crayon-e">of </span><span class="crayon-i">Tested</span><span class="crayon-h"> </span><span class="crayon-cn">90</span><span class="crayon-o">%</span><span class="crayon-h"> </span><span class="crayon-v">Cocaine</span><span class="crayon-sy">.</span><span class="crayon-sy">.</span><span class="crayon-sy">.</span><span class="crayon-e">Verified </span><span class="crayon-v">Vendor</span><span class="crayon-o">!</span></div><div class="crayon-line" id="crayon-581cb69c9ef6a959472083-5"><span class="crayon-i">ozconnection</span><span class="crayon-h"> </span><span class="crayon-i">L</span><span class="crayon-h"> </span><span class="crayon-cn">1</span><span class="crayon-h"> </span><span class="crayon-e">gram </span><span class="crayon-e">Peru </span><span class="crayon-e">Cocaine </span><span class="crayon-e">Australia</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef6a959472083-6"><span class="crayon-v">sunwu</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-cn">250mg</span><span class="crayon-h"> </span><span class="crayon-e">Pure </span><span class="crayon-e">Alprazolam </span><span class="crayon-e">Powder</span><span class="crayon-h"> </span><span class="crayon-sy">(</span><span class="crayon-v">Xanax</span><span class="crayon-sy">)</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-e">USA</span></div><div class="crayon-line" id="crayon-581cb69c9ef6a959472083-7"><span class="crayon-v">tomorrowman</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-cn">3</span><span class="crayon-h"> </span><span class="crayon-e">grams </span><span class="crayon-e">tan </span><span class="crayon-e">mdma </span><span class="crayon-i">crystals</span><span class="crayon-h"> </span><span class="crayon-cn">85</span><span class="crayon-o">%</span><span class="crayon-o">+</span><span class="crayon-h"> </span><span class="crayon-e">purity</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef6a959472083-8"><span class="crayon-v">demoniak</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-cn">2GR</span><span class="crayon-h"> </span><span class="crayon-e">PINK </span><span class="crayon-e">Speed</span><span class="crayon-h"> </span><span class="crayon-sy">(</span><span class="crayon-v">dry</span><span class="crayon-sy">)</span></div><div class="crayon-line" id="crayon-581cb69c9ef6a959472083-9"><span class="crayon-v">sunwu</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-cn">250mg</span><span class="crayon-h"> </span><span class="crayon-e">Pure </span><span class="crayon-e">Alprazolam </span><span class="crayon-e">Powder</span><span class="crayon-h"> </span><span class="crayon-sy">(</span><span class="crayon-v">Xanax</span><span class="crayon-sy">)</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-e">UK</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef6a959472083-10"><span class="crayon-v">wilfred</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-cn">3.5g</span><span class="crayon-h"> </span><span class="crayon-e">Hydroponic </span><span class="crayon-v">BUDS</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-e">HIGH </span><span class="crayon-v">THC</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-r">New</span><span class="crayon-h"> </span><span class="crayon-e">Vendor </span><span class="crayon-v">Special</span><span class="crayon-h"> </span><span class="crayon-o">!</span><span class="crayon-o">!</span></div><div class="crayon-line" id="crayon-581cb69c9ef6a959472083-11"><span class="crayon-v">justincase</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-cn">10</span><span class="crayon-h"> </span><span class="crayon-e">regular </span><span class="crayon-v">seeds</span><span class="crayon-h"> </span><span class="crayon-o">-</span><span class="crayon-h"> </span><span class="crayon-v">Hindu</span><span class="crayon-o">&amp;</span><span class="crayon-v">amp</span><span class="crayon-sy">;</span><span class="crayon-p">#39;s Shiva</span></div><div class="crayon-line crayon-striped-line" id="crayon-581cb69c9ef6a959472083-12"><span class="crayon-v">uperspeedbros</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-cn">2g</span><span class="crayon-h"> </span><span class="crayon-e">of </span><span class="crayon-v">Speed</span><span class="crayon-h"> </span><span class="crayon-o">--</span><span class="crayon-h"> </span><span class="crayon-e">Amphetamine </span><span class="crayon-e">sulfate</span></div><div class="crayon-line" id="crayon-581cb69c9ef6a959472083-13"><span class="crayon-v">godfathernl</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-o">*</span><span class="crayon-o">*</span><span class="crayon-o">*</span><span class="crayon-h"> </span><span class="crayon-cn">1</span><span class="crayon-h"> </span><span class="crayon-e">gram </span><span class="crayon-e">pure </span><span class="crayon-e">uncut </span><span class="crayon-i">cocaine</span> <span class="crayon-h"> </span><span class="crayon-o">*</span><span class="crayon-o">*</span><span class="crayon-o">*</span></div></div></td>
</tr>
</table>
</div>
</div>
    
    So can this extraction be scaled up to getting entire lists of users? Well we found out:</p>
<div>Code: <a>[Select]</a></div>
    
<div id="crayon-581cb69c9ef73564270716" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    BuyerID,BuyerUsername
    10011,giveemhere
    10037,brian146
    10039,jayjay
    10042,downlowfunk
    10046,torrex
    10061,minimilk
    10066,mightymax
    10067,screwtape
    10069,datamatrix
    10072,shlooky
    10073,okipoki
    10078,brithney85w
    10081,greenjoker
    10082,odyssey47
    10086,magmush
    10090,mxwssh
    10095,gaviboy
    10100,milky
    10106,timtimebomb
    10107,slappfisk
    10108,brainman123
    10113,creepers1
    10127,ronaldo72
    10130,ch0sen
    10134,4corner
    10136,posrednik
    10146,lulz87
    10156,cweistein
    10158,afiddlerfair
    10171,frankiemachi
    10185,2q2
    10186,skizzdaghost
    10190,waltermichae
    10200,violetraindr
    10203,raeuberhotze
    10213,parleybowl84
    10215,boogersugar3
    10218,reiji
    10226,tjebbe
    10254,quiziti_
    10259,xylitol
    10268,bugnine9
    10282,skobeywan
    10296,muggle
    10298,melvvinn_
    10299,hdth
    10302,treemonk
    10310,silvercarrot
    10312,blaster2438
    10313,agape
    10316,gzo_
    10318,crevtiae
    10321,hitman
    10324,bigstoners
    10330,gigglebox
    10370,irishjunkie4
    10371,dimitriglitc
    10372,factory9
    10389,arya420
    10399,az12er34ty56
    10402,theroland
    10413,meggymix
    10418,monkeydust
    10418,m_
    10431,flipit
    10433,mrviking
    10437,h4rdc0r3
    10453,mcg324
    10455,loffer
    10455,_
    10461,thecrazyman1
    10467,pallymally
    10474,thayle
    10476,twistedrx
    10477,olddetleff
    10496,bigone77
    10498,groovetime79
    10511,dimetho
    10512,beardofneptune
    10518,unahmedishe
    10534,pretzelmaste
    10554,krick75
    10555,haremmac
    10558,stupid123
    10560,keeker34
    10562,angeldemom
    10567,fevolution
    10593,cocacoca
    10595,jackpot1875
    10610,hatchet13a
    10623,stimpackuser
    10624,lemon714
    10625,sebb66g
    10627,horstschorst
    10643,c17h21no4
    10648,rekt
    10649,snicker
    10653,eltorrelo
    10665,g0awayb4t1ng
    10671,cilius
    10704,mango420
    10706,depre553
    10708,hohoho
    10709,sulph84
    10732,davidian
    10733,renniemint
    10753,marcotb1287
    10756,neilarmstron
    10757,weedplease
    10758,acid420
    10769,skinnymalink
    10799,sternkraft
    10812,elesdee
    10819,graves
    10827,toplessmind
    10835,peterborough
    10841,bbb2
    10861,slapchop
    10885,needthatnow
    10892,nanonyymi
    10907,rator93
    10908,jumboballs7
    10909,gimmeabreak
    10921,planb
    10928,trevelyan
    10947,kappagrande
    10963,joe121
    10967,canesnake
    10968,monkey18
    10976,mr2happy
    10981,godsnameissm
    10982,raresh
    11001,madcunt33
    11012,stankydanky
    11016,1bigdog
    11038,d1rkd1g1tal
    11046,gyste1
    11053,johns282
    11071,trailertrash
    11078,masterblaste
    11100,lastresort
    11102,thcbuds
    11104,jeffhawkins
    11114,thelionshare
    11116,sournycd
    11120,hobbes
    11123,jameson
    11126,strom
    11137,ruffiee
    11147,jenslover
    11160,tiririca
    11162,blentron
    11168,5orlorn
    11170,jonnoj
    11175,mrmonster123
    11180,sillysally
    11182,deepelmo
    11188,panlanwan
    11200,scolopax
    11204,wikid50
    11222,thall
    11245,methy
    11256,jb299999
    11262,dendrix
    11268,westhebeast
    11271,docbenway71
    11274,moi_
    11280,pinecone25
    11288,phoon
    11293,damane033
    11296,jaystiles
    11317,gagao
    11320,spoot36
    11352,sloppyjoe
    11367,toomertoo
    11369,robertfr
    11377,rollin
    11381,carlitolegen
    11388,dogtanian
    11405,catlessrugged
    11413,kelevrahz
    11427,mmmesopus101
    11429,bubi
    11452,candles
    11453,goldbond
    11464,blustik
    11465,ballsacker
    11480,thetonik
    11484,boc
    11498,mrmagoo
    11499,tap
    11500,vaan1
    11508,zounce
    11511,bikerbum
    11524,acidroom123
    11533,zeek01
    11541,valueadded
    11545,50fifty
    11549,lionfish37
    11550,trent
    11564,sonicdeathmo
    11566,i7847463846
    11588,dr67p
    11595,wingotodman
    11597,brookey
    11601,motibiti
    11625,dack
    11647,poundtownher
    11651,luckycampbel
    11667,vidali_
    11683,potatobread
    11687,shaveandahai
    11693,heavyduty744
    11695,fpm10
    11708,rucksichlos
    11710,pinkpowerran
    11732,belzhikr
    11736,oogaboogagoo
    11737,seek3r00
    11746,boringgirl
    11773,jakndex
    11811,bitcoinbitco
    11818,red99
    11819,holyghost
    11820,amesghali
    11821,principalway
    11829,mrm
    11835,dagger
    11842,anonlifestyle
    11848,demoniakk
    11849,mortondumal
    11865,dakeera
    11866,xxxxman
    11879,blahblah1
    11886,atouttsmanne
    11891,bluebossa
    11905,nsimeh417
    11915,hofsdiufwebk
    11917,z0rfire
    11918,mynameishate_
    11921,elegantfile
    11923,blimpy22
    11924,athomebomb
    11930,clobro1
    11932,bluester
    11939,irishaustral
    11963,gentoo
    11967,newchanges
    11972,danimus
    11973,spaniard
    11980,djevans71
    11985,mrsmith
    11994,dreamsage
    12010,soylentgreen
    12016,ellisdee3
    12044,testeraccount90
    12048,dshas
    12049,improbable
    12053,h20
    12078,pedro21
    12085,phoenixender
    12100,nickyblades
    12101,getupped
    12116,vbh
    12128,oubaya
    12133,canda
    12145,tk005
    12164,pipwalker
    12173,namename
    12176,aslanchik
    12180,datz
    12214,mhitchens42
    12215,brownevo
    12224,fts123
    12226,shedrik
    12240,khanbongo
    12245,jinkz
    12247,glycerat100
    12254,dadinio3213
    12264,cumknot
    12269,d8jd8jd8j
    12275,psytranceg
    12287,swissprog
    12289,ohmathea
    12290,ctrlalth
    12304,zeeozwei
    12306,sophocles
    12318,bluefox
    12337,shamus68
    12338,bealzebobs
    12340,jeanlefebvre
    12348,lostinspace
    12373,herpmcderp
    12382,unknown555
    12388,shaft
    12424,leirbag
    12444,snorro119
    12454,piratecannon
    12457,mrtrump
    12463,niall2012
    12468,rossisucht
    12472,stlbigkahu_
    12475,hurstwok
    12484,plitzein
    12491,fireflyx
    12499,swizzlestick
    12503,kindle
    12509,sourmonkey
    12524,qwertyqazwsx
    12543,balanter
    12549,forellebabbe
    12554,buffalos
    12558,ctrlctrl
    12566,freeparking
    12570,brbdriver
    12584,keneeth
    12603,spaceminers6
    12605,topsecnick
    12606,ilovepnr
    12613,dotdash
    12628,rambo512
    12631,herhim2009
    12634,shingles
    12650,headspace123
    12655,fiskar
    12675,boybreathran
    12696,kerin28
    12706,phishfan
    12717,redman
    12735,jellyrajah
    12736,theargonaut
    12748,spartanec731
    12751,44xseba
    12764,rs6k
    12782,moz
    12791,squirrelmast
    12797,diddlerizzle
    12824,theendall
    12826,anto6901
    12829,r3aliize
    12834,psychonaut123
    12836,django13
    12838,scunkysmerf
    12843,finearts
    12863,casanostra25
    12866,overc375
    12869,byron2013
    12876,nighthawk
    12888,filonxhp3k59
    12889,speedweed
    12895,dreamfox
    12903,brick888
    12932,trippinf0x
    12953,piccolabesti
    12956,untergrundsz
    12971,tmko
    12985,jflynn
    12986,alienthc
    12991,cbozwiek22
    12995,berndman
    13000,traderbtc
    13001,ne0ngirl
    13007,nestea01
    13009,johnmiller
    13019,tberry
    13028,778dexter778
    13031,zaklinaczcip
    13033,coolethan
    13035,onionsoup
    13050,wilbert89
    13057,surfer
    13070,tsm123
    13073,jla
    13085,whiteflight
    13088,superskunk79
    13090,facemelt
    13093,nurse80
    13100,purpleextreme
    13111,dracula
    13116,unknown79
    13119,asdfuiops
    13124,mikenewbit
    13125,mtothex
    13127,sleep12
    13130,scunnered
    13132,rstevens
    13147,komaschaedel
    13148,granville999
    13149,levlvov70
    13150,libertas1234
    13154,heimderdokto
    13162,akafreak
    13166,svenzzon
    13173,relaxedsoup
    13178,mssdark
    13180,fla_
    13195,ahdls
    13199,astrid
    13208,m911j
    13219,guple520
    13226,wwmjax
    13240,jollyrogers
    13266,thisaintme89
    13272,cannsument
    13284,tambour
    13286,dextermorgan
    13294,rubberducklo
    13298,turner13
    13303,mrkobayashi
    13312,foxcloud
    13319,alligatorsmi
    13324,dandan
    13326,gizdog
    13333,aurai
    13343,rayray60
    13354,zapzarap
    13361,gmtmaster
    13362,bluegoat
    13408,whitesferry
    13409,hexdebt
    13411,pebbles200
    13424,wiecz
    13450,alfr40jd
    13455,epicdick
    13463,rotrier
    13467,xteb112
    13472,pryzak
    13473,the70th
    13483,stonedude
    13487,happyguy72
    13494,rasputin
    13495,xk5910
    13548,starshiptent
    13571,justmarried
    13572,choicethespi
    13574,merlo
    13583,jacofaco11
    13597,aussiehq
    13612,fearlessfred
    13619,kronhjorten1
    13621,jackcubrick
    13625,uhr
    13633,cloudso_
    13637,pablo6666
    13645,roth
    13652,anonym254
    13673,bushmans
    13688,doctorgig
    13690,following
    13698,celvin
    13706,gazer
    13724,re3r25rw1
    13725,jtleary
    13733,flex
    13740,guanaci
    13742,redtree13
    13743,annonnymous
    13764,sanctiman
    13795,billy1234
    13819,immortalis66
    13819,immortalis666
    13828,frink
    13829,donaldtruck
    13830,toefia
    13832,dizzydinosaur
    13834,mott
    13837,testingdis
    13838,normannormal
    13852,nextlegacy
    13858,bool
    13862,digitalluv3r
    13869,rufio
    13875,icho
    13894,blackburn74
    13897,zaszax
    13901,franco21
    13903,spookeemeeto
    13918,lacticacid
    13920,jabato
    13925,tootelage
    13933,spsp
    13938,nickbla
    13940,cuco
    13944,mrmustard
    13949,mariejuana
    13951,tranquil
    13965,lordbonk
    13967,findingsolac
    13974,uberstat1
    13977,fooney
    13980,care696
    13982,a845631
    13990,mongoose88
    13997,scotty1278
    14000,griselda
    14008,vad0r
    14010,barepiff
    14019,googleplus
    14022,suppertime
    14025,snoffle
    14032,fox0r
    14038,lemonhaze
    14047,niwatat
    14075,catlicker420
    14081,dimwizzle
    14084,verde
    14089,lovechild96
    14092,mileycyrus21
    14093,intothemist
    14128,0verlord
    14130,bigplateofcr
    14134,hapticreel
    14138,vermithrax
    14140,cabbagetree
    14143,snowflake91
    14150,tvizzle88
    14166,smilebob
    14169,punisher
    14173,virt4321
    14185,meow
    14202,bunnyrabbit3
    14204,fatarcher
    14210,mavlito
    14215,darthvader
    14217,kanets2
    14232,spliffy420
    14245,neb11
    14247,zidane99
    14278,esc0bare
    14284,mrsimmer100
    14287,coffeeblack
    14292,redone1
    14296,joejackson19
    14300,mybuyguy2
    14305,scootie2
    14313,jezisjevzkri
    14315,pollyanna99
    14326,ata100t
    14366,trampdyna
    14398,atxrebel
    14400,twilightprin
    14403,quedlo
    14411,traumarked
    14415,spyguymarket
    14417,ganjaman
    14437,tkolts
    14446,bowser
    14456,shablam123
    14475,bigrat2
    14486,d537719
    14509,icarus212121
    14512,dabbb1
    14525,bobdylan21
    14541,sdfseg32tg2
    14543,saber45
    14554,diminion
    14562,matix22
    14566,millionaires
    14567,markymark102
    14576,dimon114
    14580,pillpig
    14585,aznlova
    14587,qstrong
    14596,junipergreen
    14601,bruda372_
    14604,mikejonas
    14605,omega06
    14617,jimmybuffet
    14625,shrodinger
    14629,gratuity
    14653,davematthews
    14655,jonesy63au
    14661,jimbojones29
    14662,4ncb
    14667,arthur
    14678,greengo420
    14699,heaviside
    14702,jabb3rwock
    14716,trainwreck
    14724,blackcodedog
    14725,colin1
    14730,yellow43
    14731,marvel
    14759,theheard
    14762,dudeguymanpe
    14769,sdgsdf
    14770,paulwalker
    14804,helper77777
    14818,stinkybudz
    14820,rexthecat
    14821,jblaze
    14837,badpacers
    14841,mediamonkey
    14844,rogalach
    14845,calvin
    14853,hell0
    14860,shakur6pack
    14875,ace619
    14877,l2h2k
    14883,1surg
    14889,quakez
    14891,lanochen
    14896,silentworker
    14898,grineflip
    14902,luxornight
    14920,krauch
    14926,iknes
    14985,zazoo
    14986,olpalk
    14990,georgeb
    15002,marketman1
    15005,anon7869
    15011,hubihubsn
    15020,septaflyer
    15023,ogcorleone
    15027,puntitot1
    15034,harbinger168
    15041,psytrance
    15048,eris
    15093,b13q7tey6qe3
    15095,waid123
    15099,pedroc5123
    15112,holygrail
    15121,goliat
    15143,nyymi
    15158,federalhero
    15168,undecylic
    15169,salimmk
    15171,ninjadab
    15182,king2000
    15186,mrp
    15191,strainhunter
    15206,e0n
    15222,senior
    15237,boxn2
    15255,majschmidt
    15256,yuyi
    15270,dreamchild
    15274,dutchy
    15280,mangohedgeho
    15295,rezin
    15296,q77uvctj
    15298,smartbuyer
    15317,wesmantoothh
    15322,qplabr
    15323,hakunamatada
    15324,undergroundd
    15325,ljqaq
    15342,dmad
    15384,qwerty123
    15395,thebear
    15398,formula22
    15425,quickben
    15426,wahamann
    15439,somethingveg
    15446,blkmn
    15457,pinotgrigio
    15472,captainpanic
    15476,pineapples
    15489,notrelluf
    15490,ragnar
    15493,wonkachole
    15501,demeter
    15525,neversummer
    15529,lilbooseyfan
    15533,h3xagon
    15547,mindbender
    15576,papabear
    15584,1berty
    15590,dickvanhinte
    15594,freed
    15600,walterwhitej
    15613,darkdweller
    15616,greatbig
    15642,fiatxu454
    15650,snoww
    15653,craftypie
    15683,cornelius23
    15690,thesumofallb
    15712,dolby23
    15714,blank2052
    15722,theaaaconnec
    15739,rawrang
    15747,gundy0101
    15748,tracy
    15755,beams
    15758,bigenus
    15759,zany88
    15763,givemeoil420
    15772,yimmy
    15799,chopinnuun1
    15804,happymerry
    15818,looksaround
    15832,hellojava
    15836,smackdown
    15853,liquid
    15864,thefist
    15867,wickedwitch6
    15890,drhellokitty
    15910,maryann
    15920,viciousbiscuit
    15951,auston
    15953,crazyb
    15955,charlesfarle
    15961,laksmi
    15984,9bibby
    15986,wuzups
    15995,ryobie9
    15997,stickyman
    16001,trainmaster
    16035,bilb0
    16047,st00sh1e
    16054,djaybjay
    16055,neverbeenbetter
    16057,ronfuckingsw
    16075,wanteddetnaw
    16080,baang
    16082,gr_
    16084,seziertier
    16095,seadragon
    16098,g_
    16098,god
    16111,namekevo
    16119,keram
    16123,raigen
    16126,carlex
    16152,brudes1
    16158,rhodjab
    16160,mrx8552
    16168,mrinnocent
    16174,trancemaster
    16175,sweatywookie
    16183,arjuna
    16204,charvo95
    16206,caraboulou
    16216,penguin1
    16218,importsbrasi
    16224,james69
    16225,inspectahdeck
    16235,stevo1234
    16237,poizulimo
    16250,hansopel
    16257,herbalking
    16279,kbdhro
    16280,sleesh
    16282,whitefish000
    16288,arraki_
    16294,muffyduffy1984
    16303,ericcartman
    16322,acervol
    16331,farmhand
    16343,mushinmusa
    16369,alliwantisso
    16377,nfw91
    16397,wholebuy
    16401,ezio14
    16417,icansee
    16429,feodorbelved
    16466,pilotflying
    16470,ooopdcbza
    16473,boboav
    16474,ggl3000
    16477,misfits69
    16485,rodneybusine
    16490,nope
    16492,3zero
    16512,jonathanpric
    16525,theotherguy
    16528,trit
    16536,gjchjr
    16551,ab_
    16557,snaprabbit
    16579,jdjdjd
    16587,jeffast
    16589,libertadhoy
    16603,fermion
    16610,mickeymantle
    16611,felsad
    16643,flip36
    16689,style2121
    16700,taronga
    16704,voracious
    16718,youngmorpheu
    16720,salvo77
    16721,dosethrasher612
    16724,upthecreek
    16759,icq
    16771,circussam
    16792,caloway
    16794,buxton
    16830,livefree
    16839,o0rainman0o
    16858,darkstar7736
    16867,paploo07
    16878,kinghappy
    16884,niggaz
    16884,_
    16892,sonabe
    16908,coffeetime04
    16931,sugarfree
    16934,gesundheit
    16938,beerman
    16986,strings999
    16994,dima88
    16998,tampico
    16999,carlosbrindi
    17034,spider
    17057,nickel
    17064,lojin99
    17066,sottodue
    17095,ch3dd3rdr4g0
    17100,jdobie
    17106,barry21
    17111,salma6
    17122,transactor
    17145,antoine
    17146,bobtastic
    17150,heroin666
    17166,sennzy
    17167,chickenwings
    17172,raskolnikov
    17175,tedblanders
    17212,thedude
    17214,thefunkybunc
    17233,marketface20
    17237,thewineohs
    17251,ketchup1000
    17254,soulpatch141
    17265,skzap
    17270,senordingdon
    17277,m4lk4v14n
    17288,zhangxuelian
    17308,fostershome4
    17319,larsiboy13
    17330,glowtape
    17343,supertramp
    17352,ableapp1
    17367,kermitthetoad
    17371,dadieoo
    17396,smokedoutsun
    17415,ilovewater
    17424,inri1010
    17435,kak1828
    17440,happyhippy
    17446,trip78
    17463,crummytits
    17472,ninjaslipper
    17474,rockybalboa7
    17479,whowhatwhere
    17491,sargas93
    17494,joshdavey
    17496,eric2267
    17517,zeq8nxwn
    17536,iigivegoodre
    17574,coreyi7
    17603,brucious
    17613,eaststand
    17621,mrbojangles
    17631,rachet
    17638,pansymansy
    17639,jumpinforseals
    17664,lazerbeam
    17687,iaminnocent
    17692,chattylego
    17697,whitewallet
    17709,cheego
    17719,inpetus
    17725,6singfried6
    17751,xotillweover
    17761,gardenhose
    17773,tolly37
    17781,lake1212
    17786,nanjazz25
    17812,sunshadow4
    17815,3juanvaldez
    17829,fishscale
    17831,kollasx
    17843,endymion
    17851,fnordle
    17862,s0wl
    17863,81kaisa81
    17879,oaxacan
    17881,lakshmi
    17883,memorylane
    17884,usserioummer
    17887,desnudito
    17887,d_
    17893,toxinld
    17899,moosdagoose
    17902,bobby178
    17917,oklol
    17971,lakomka
    17983,marley91
    17984,cogeneration
    17989,mightyreal
    18017,funkytown7
    18022,xtcking
    18026,singularity
    18033,toxicmadhatt
    18034,cloudsof
    18047,colforbin
    18048,dmtbliss
    18073,soupsuser
    18113,pingpong99
    18152,medibird
    18157,pooter
    18171,wvwnl
    18189,lawnmower
    18190,h0ll0wfry
    18210,multitox
    18232,unn4m3d
    18245,sanostrike
    18256,gotfried
    18274,killareese1
    18285,mrmutto
    18292,gameristo
    18307,liveaction86
    18308,roxas50
    18336,sunflowersin
    18356,shineforever
    18373,finite
    18419,marialionza
    18425,rainbain
    18426,d4fre2fmxn
    18441,dah38esi
    18461,tkkg
    18466,physicalhatr
    18521,rackyrule
    18547,bum85
    18560,_
    18578,xyz001
    18585,itistruth
    18613,gunakiktomar
    18620,xelab2
    18627,aliasof1
    18636,bitcoinsboi
    18650,mdfrankie
    18655,wooly8
    18661,mx876
    18666,bobdavis33
    18669,sampson
    18674,adamaisha
    18703,grungygringo
    18712,iqvirus
    18719,larrythefalc
    18730,jk4477
    18739,thefinn
    18754,weedman2013
    18763,rezat
    18785,greenfish
    18795,james546
    18824,suavalava
    18844,happywanderi
    18845,rline
    18870,yp1445
    18908,bee
    18909,alibrite
    18914,bigbee69
    18918,toeknee
    18934,teeveestar
    18935,beaconofgod
    18969,trachta
    18987,dexguy20
    19016,milton
    19020,cain1919
    19037,manasek
    19046,crazybobmarley
    19058,ketaminekier
    19075,poiuytrewq
    19079,berrabus
    19080,gtiv
    19082,elephant
    19091,kingsizesilv
    19124,derekderek
    19137,mensget
    19139,grasssea
    19151,rgodo26
    19152,b5x44
    19153,bertandernie
    19194,spacetravele
    19204,fannybaws11
    19206,sh0p
    19218,crepuscular
    19240,noly
    19246,anaccount
    19253,highasakite
    19255,martinus91
    19285,betelgeidze</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">


Updated: 2013-12-14
    
