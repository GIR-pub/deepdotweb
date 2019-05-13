---
title: "Evolution Market: Now Offering Multisig Transactions!"
---

Posted by: DeepDotWeb
<span>May 6, 2014</span>

<p>We have another market joining the Munmltisig Family, Now evolution, as always, we try to support those market offering multisig transaction so we bring you here the multisig usage guide as its listed on their wiki, this will also be listed on out <a href="http://www.deepdotweb.com/multisig-guides/">multisig guides</a> page and the market will be promoted to the multisig category <a href="/2013/10/28/updated-llist-of-hidden-marketplaces-tor-i2p/">on our list</a>:</p>
<p><a class="sabai-entity-type-content sabai-entity-bundle-name-directory-listing sabai-entity-bundle-type-directory-listing" title="Evolution Marketplace" href="http://www.deepdotweb.com/marketplace-directory/listing/evolution-marketplace">Evolution Marketplace</a> &#8211;  http://k5zq47j6wd3wdvjq.onion</p>
<h2><span id="Introduction" class="mw-headline">Introduction</span></h2>
<p>Using and accepting multi-signature (multisig) transactions on Evolution is pretty straight-forward. The following sections will explain how to obtain bitcoin public-private keypairs (section 1), how to configure your account for multisig (section 2), how to order using multisig (section 3), and finally how to claim funds (section 4).</p>
<p>Keep in mind that this is an advanced feature still. Make sure to know what you&#8217;re doing, or you could lose funds.</p>
<h2><span id="Obtaining_Keypairs" class="mw-headline">Obtaining Keypairs</span></h2>
<p>This section will explain how to obtain a public-private bitcoin keypair using the Bitcoin-QT debug console (Help &gt; Debug Console) or bitcoind. It’s a simple 3-step-process that will provide you with a public and private key. Once inside the console, start by obtaining a new address using the following command:</p>
<div id="crayon-594aa9851b632400786041" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    getnewaddress</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-594aa9851b632400786041-1">1</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-594aa9851b632400786041-1"><span class="crayon-v">getnewaddress</span></div></div></td>
</tr>
</table>
</div>
</div>
    
<p>
    It will output a new bitcoin address, for example &#8216;1LtZhZ8rNcRRqqayUfzUcxywF59MSPHxoV’. To obtain the public key use the following command:</p>
<div id="crayon-594aa9851b63c048560574" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    validateaddress "1LtZhZ8rNcRRqqayUfzUcxywF59MSPHxoV"</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-594aa9851b63c048560574-1">1</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-594aa9851b63c048560574-1"><span class="crayon-i">validateaddress</span><span class="crayon-h"> </span><span class="crayon-s">"1LtZhZ8rNcRRqqayUfzUcxywF59MSPHxoV"</span></div></div></td>
</tr>
</table>
</div>
</div>
    
<p>
    Make sure to replace this example address with the address you just generated yourself. It will output something along the lines of:</p>
<div id="crayon-594aa9851b640851490787" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    {
    "isvalid" : true,
    "address" : "1LtZhZ8rNcRRqqayUfzUcxywF59MSPHxoV",
    "ismine" : true,
    "isscript" : false,
    "pubkey" : "03c756aafb23e6f4fcb9912a2f6bc3785c8ece24ba851058f34dd117903eec52b6",
    "iscompressed" : true,
    }</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-594aa9851b640851490787-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-594aa9851b640851490787-2">2</div><div class="crayon-num" data-line="crayon-594aa9851b640851490787-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-594aa9851b640851490787-4">4</div><div class="crayon-num" data-line="crayon-594aa9851b640851490787-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-594aa9851b640851490787-6">6</div><div class="crayon-num" data-line="crayon-594aa9851b640851490787-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-594aa9851b640851490787-8">8</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-594aa9851b640851490787-1"><span class="crayon-sy">{</span></div><div class="crayon-line crayon-striped-line" id="crayon-594aa9851b640851490787-2"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-s">"isvalid"</span> <span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-t">true</span><span class="crayon-sy">,</span></div><div class="crayon-line" id="crayon-594aa9851b640851490787-3"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-s">"address"</span> <span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-s">"1LtZhZ8rNcRRqqayUfzUcxywF59MSPHxoV"</span><span class="crayon-sy">,</span></div><div class="crayon-line crayon-striped-line" id="crayon-594aa9851b640851490787-4"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-s">"ismine"</span> <span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-t">true</span><span class="crayon-sy">,</span></div><div class="crayon-line" id="crayon-594aa9851b640851490787-5"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-s">"isscript"</span> <span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-t">false</span><span class="crayon-sy">,</span></div><div class="crayon-line crayon-striped-line" id="crayon-594aa9851b640851490787-6"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-s">"pubkey"</span> <span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-s">"03c756aafb23e6f4fcb9912a2f6bc3785c8ece24ba851058f34dd117903eec52b6"</span><span class="crayon-sy">,</span></div><div class="crayon-line" id="crayon-594aa9851b640851490787-7"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-s">"iscompressed"</span> <span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-t">true</span><span class="crayon-sy">,</span></div><div class="crayon-line crayon-striped-line" id="crayon-594aa9851b640851490787-8"><span class="crayon-sy">}</span></div></div></td>
</tr>
</table>
</div>
</div>
    
<p>
    The value identified as pubkey is the public key you’ll need to set-up multisig on your account.</p>
<p>Lastly, we need to obtain the private key associated with public key. To do so, use the following command:</p>
<div id="crayon-594aa9851b644651829567" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    dumpprivkey "1LtZhZ8rNcRRqqayUfzUcxywF59MSPHxoV"</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-594aa9851b644651829567-1">1</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-594aa9851b644651829567-1"><span class="crayon-i">dumpprivkey</span><span class="crayon-h"> </span><span class="crayon-s">"1LtZhZ8rNcRRqqayUfzUcxywF59MSPHxoV"</span></div></div></td>
</tr>
</table>
</div>
</div>
    
<p>
    The output of this command is the private key associated with your public key. You will need this private key in order to sign and release the funds from the multisig address, so make sure to keep it somewhere safe.</p>
<h2><span id="Account_Configuration" class="mw-headline">Account Configuration</span></h2>
<p>Before you’ll be able to accept/use multisig escrow, you’ll have to specify your bitcoin public key and your payment/return bitcoin address. You can do so here: my evolution &gt; settings &gt; multisig.</p>
<p>Note that the payment/return address should be a bitcoin address that belongs to you, i.e. an address in your bitcoin wallet.</p>
<p><b>Vendors</b><br/>
    If you wish to accept multisig escrow transaction, you’ll need to configure so in your store settings (my evolution &gt; store &gt; settings). The default setting is to accept regular escrow only &#8211; change it to ‘multisig only’ or ‘both’ depending on your preference in order to accept multisig escrow for orders.</p>
<h2><span id="Ordering" class="mw-headline">Ordering</span></h2>
<p>Ordering products using multisig escrow isn’t really all too different from using regular escrow. First, deposit the appropriate amount into your evolution wallet using the default procedure. Once the funds have credited to your account balance, order the desired product as you normally would. In Step 3 you will have to option of selecting your preferred method of escrow, select ‘multisig’ to use this form of escrow, and continue to place the order.</p>
<p>Upon placing the order, funds (minus fees) will transfer from your evolution wallet to the multisig address that was generated. You can view the multisig address on the orders detail page.</p>
<h2><span id="Claiming_Funds" class="mw-headline">Claiming Funds</span></h2>
<p>When the order is finalized, canceled, declined or split, the appropriate party (or both parties in case of split) can claim their funds. On the orders/sale details page there will have appeared a button underneath the multisig address reading ‘Claim Funds’. Press this button and follow the instructions on this page.</p>
<p><b>Bitcoin-QT/bitcoind</b><br/>
    Using the same Bitcoin-QT debug console we used to obtain the public-private keypair, we’ll sign the transaction in order to release your funds. On this page you will find a command similar to the following:</p>
<div id="crayon-594aa9851b64d238125646" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    signrawtransaction '01000000016023e7ff9ca73c79dc995187b272d50bb2297c087c5cf86069b6f33719
    a3740e0100000000ffffffff0110270000000000001976a914bd7e6d9e780f3547c595b9813966d4d1f0634b
    2d88ac00000000' '[{"txid":"0e74a31937f3b66960f85c7c087c29b20bd572b2875199dc793ca79cffe7
    2360","vout":1,"scriptPubKey":"a9142aec2eeae61f77201c9e102c240ac8e7ebe416ad87",
    "redeemScript":"524104b082afa304cc17fc2acb95543cca28d9c1dfad7929bedc3973162e16b3f64568888
    94297a0ede3cf3779c9873e5a2bf8a9cc3a4bdc0a9c25b17cb7ef5a0b20d8410415cff57483456ffccb17b597
    ab57a3e6e37be4d3b366062b1fb9b8d7120a355154e41143a1f2fb9b395196be3ab00d3a87a1b4ca4ab013122
    4373602dd63bf8721033bd6e9038a9ee0763ad8129729d4afc4d77bdbcf12e9dcabbee3d7e2887c844c53ae"}]'
    '["YOUR_PRIVATE_KEY"]'</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-594aa9851b64d238125646-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-594aa9851b64d238125646-2">2</div><div class="crayon-num" data-line="crayon-594aa9851b64d238125646-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-594aa9851b64d238125646-4">4</div><div class="crayon-num" data-line="crayon-594aa9851b64d238125646-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-594aa9851b64d238125646-6">6</div><div class="crayon-num" data-line="crayon-594aa9851b64d238125646-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-594aa9851b64d238125646-8">8</div><div class="crayon-num" data-line="crayon-594aa9851b64d238125646-9">9</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-594aa9851b64d238125646-1"><span class="crayon-i">signrawtransaction</span><span class="crayon-h"> </span><span class="crayon-s">'01000000016023e7ff9ca73c79dc995187b272d50bb2297c087c5cf86069b6f33719</span></div><div class="crayon-line crayon-striped-line" id="crayon-594aa9851b64d238125646-2"><span class="crayon-s">a3740e0100000000ffffffff0110270000000000001976a914bd7e6d9e780f3547c595b9813966d4d1f0634b</span></div><div class="crayon-line" id="crayon-594aa9851b64d238125646-3"><span class="crayon-s">2d88ac00000000'</span><span class="crayon-h"> </span><span class="crayon-s">'[{"txid":"0e74a31937f3b66960f85c7c087c29b20bd572b2875199dc793ca79cffe7</span></div><div class="crayon-line crayon-striped-line" id="crayon-594aa9851b64d238125646-4"><span class="crayon-s">2360","vout":1,"scriptPubKey":"a9142aec2eeae61f77201c9e102c240ac8e7ebe416ad87",</span></div><div class="crayon-line" id="crayon-594aa9851b64d238125646-5"><span class="crayon-s">"redeemScript":"524104b082afa304cc17fc2acb95543cca28d9c1dfad7929bedc3973162e16b3f64568888</span></div><div class="crayon-line crayon-striped-line" id="crayon-594aa9851b64d238125646-6"><span class="crayon-s">94297a0ede3cf3779c9873e5a2bf8a9cc3a4bdc0a9c25b17cb7ef5a0b20d8410415cff57483456ffccb17b597</span></div><div class="crayon-line" id="crayon-594aa9851b64d238125646-7"><span class="crayon-s">ab57a3e6e37be4d3b366062b1fb9b8d7120a355154e41143a1f2fb9b395196be3ab00d3a87a1b4ca4ab013122</span></div><div class="crayon-line crayon-striped-line" id="crayon-594aa9851b64d238125646-8"><span class="crayon-s">4373602dd63bf8721033bd6e9038a9ee0763ad8129729d4afc4d77bdbcf12e9dcabbee3d7e2887c844c53ae"}]'</span><span class="crayon-h"> </span></div><div class="crayon-line" id="crayon-594aa9851b64d238125646-9"><span class="crayon-s">'["YOUR_PRIVATE_KEY"]'</span></div></div></td>
</tr>
</table>
</div>
</div>
    
<p>
    Replace YOUR_PRIVATE_KEY with the private key we obtained in section 1 and copy the entire command into the debug log. Upon submitting it will output something along the lines of this:</p>
<div id="crayon-594aa9851b652404486632" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
<div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    {
    "hex" : "01000000016023e7ff9ca73c79dc995187b272d50bb2297c087c5cf86069b6f33719a3740e03c
    756aafb23e6f4fcb9912a2f6bc3785c8ece24ba851058f34dd117903eec52b600001976a914bd7e6d9e780f354
    7c595b9813966d4d1f0634b2d88ac00000000",
    "complete" : false,
    }</textarea></div>
<div class="crayon-main" style="">
<table class="crayon-table">
<tr class="crayon-row">
<td class="crayon-nums " data-settings="show">
<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-594aa9851b652404486632-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-594aa9851b652404486632-2">2</div><div class="crayon-num" data-line="crayon-594aa9851b652404486632-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-594aa9851b652404486632-4">4</div><div class="crayon-num" data-line="crayon-594aa9851b652404486632-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-594aa9851b652404486632-6">6</div></div>
</td>
<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-594aa9851b652404486632-1"><span class="crayon-sy">{</span></div><div class="crayon-line crayon-striped-line" id="crayon-594aa9851b652404486632-2"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-s">"hex"</span> <span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-s">"01000000016023e7ff9ca73c79dc995187b272d50bb2297c087c5cf86069b6f33719a3740e03c</span></div><div class="crayon-line" id="crayon-594aa9851b652404486632-3"><span class="crayon-s">756aafb23e6f4fcb9912a2f6bc3785c8ece24ba851058f34dd117903eec52b600001976a914bd7e6d9e780f354</span></div><div class="crayon-line crayon-striped-line" id="crayon-594aa9851b652404486632-4"><span class="crayon-s">7c595b9813966d4d1f0634b2d88ac00000000"</span><span class="crayon-sy">,</span></div><div class="crayon-line" id="crayon-594aa9851b652404486632-5"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-s">"complete"</span> <span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-t">false</span><span class="crayon-sy">,</span></div><div class="crayon-line crayon-striped-line" id="crayon-594aa9851b652404486632-6"><span class="crayon-sy">}</span></div></div></td>
</tr>
</table>
</div>
</div>
    
<p>
    Copy the value identified as hex and paste it in the appropriate form on the ‘Claim Funds’ page on evolution. After submitting, the transaction will also be signed by evolution and the funds will be transferred to the address you specified as your return/refund address.</p>
<p>&#8212;-</p>
<p>Thanks to the evolution staff taking another step to reduce marketplace scams!</p>
</div>

Updated: 2014-05-06
    
