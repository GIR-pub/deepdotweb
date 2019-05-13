---
Bitwasp &#8211; Now Offering Built in multi-signature Transactions!"
---
<article class="post-listing post-4879 post type-post status-publish format-standard has-post-thumbnail hentry  tag-bitwasp tag-built tag-multisignature tag-offering tag-transactions">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/admin/" title="">DeepDotWeb </a></span>
    <span>April 4, 2014</span>
    <span>in <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://www.deepdotweb.com/category/news-updates/" rel="category tag">News Updates</a></span>
    <span><a href="https://www.deepdotweb.com/2014/04/04/bitwasp-now-offering-built-in-multi-signature-transactions/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Following our recent <a href="http://www.deepdotweb.com/2014/03/25/interview-with-bitwasp-founder-developer/">interview</a> with the founder and developer of the Bitwasp software, we were just told that the new version is now released and is offering built in multisig transactions, this is pretty good news as we know this software is being used from time to time for marketplaces and had some history of getting hacked with all the bitcoins stolen &#8211; so with this new multisig feature we could at least not worry about this part, this is a repost of the announcement from the bitwasp forum  + the guide for using multisig transactions, you can find the original thread here: http://bit-wasp.org/index.php/topic,215.0.html</p>
    <p>(The Guide is after the announcement )</p>
    <p><strong>===Start Quote===</strong></p>
    <p>Folks, it&#8217;s time at last. Announcing Bitwasp, the marketplace that stores no user funds.</p>
    <p>I&#8217;ve spent a lot of my recent time working on this code in the background, not posting to Github. There wasn&#8217;t much I could say, since rebuilding the project was a huge undertaking, it didn&#8217;t justify posting incremental, broken commits to Github. It needed to be fairly well tested, and I&#8217;ve had to work on things like OP_CHECKSIG functionality, rewriting the system so it used a scraper rather than relying in incoming wallet transactions, and refactoring the order system.</p>
    <p>Since most of you are familiar with the live-wallet version, I&#8217;ll describe what&#8217;s new:</p>
    <ol>
    <li>No more &#8216;Bitcoin&#8217; link on the navigation panel.</li>
    <li>Instead of giving funds a regular address to pay to, which enables all sorts of scams, and can lead to theft, multisignature transactions are now standard, for up-front payment or escrow.(***)</li>
    <li>Administrators must enter an electrum master public key(*) to derive addresses for registration fee payment&#8217;s, and keys for multisig addresses. Let me just say now that this is what attackers will be trying to change. Secure your admin account with 2FA.</li>
    <li>Vendors can enter a list of public keys(**) in advance of accepting orders, or will be prompted to enter keys if they have none available when creating an order.</li>
    <li>Buyers must enter public keys on a per-order basis(**).</li>
    <li>The order process in the old version pretty much just moved around magic numbers (user balances) in a database to grant entitlement to coins on the wallet. Now, once funds leave a multisig address, <em>they pay directly to the users key that was used to create the address.</em></li>
    <li> Users need to sign multisignature transactions. I&#8217;ll explain in detail below&#8230;</li>
    </ol>
    <p>* It isn&#8217;t my intention to force people to use a particular client, however electrum is the only deterministic key derivation algorithm that sees mainstream use. (**)<br />
    ** &#8211; Forcing users to enter a list of keys, or individually, or solely from an MPK, sucks. However, this is an acceptable solution until clients adopt BIP32, which will be the case for the next version of electrum, and eventually all the others as well.<br />
    *** &#8211; Since vendors/buyers can go missing during an order, 2 of 3 multisignature addresses are used for escrow and up-front payments, so funds are recoverable.</p>
    <p>I will post the code onto github shortly once I finish a few small bits, and get it presentable.</p>
    <p>Pushing code to github does NOT mean it is a tested, vetted, and definitely working version &#8211; the software really needs to be reevaluated now, since I&#8217;ve recoded a vast amount of it.</p>
    <p><strong>So, whats multisig?</strong><br />
    Multisignature addresses are addresses controlled by more than one person. They are created with a set of requirements, that dictate how the funds in the address can be moved.</p>
    <p>2-of-3 signature addresses are jointly controlled by 3 people, say the site operator, the buyer, and the seller, but funds can only be moved if two people authorize and sign a transaction.</p>
    <p>Users will be expected to sign transactions for themselves. While client&#8217;s leave much to be desired regarding support for multisignature transactions, I believe the best way to increase their adoption is to bring them into day-to-day life, and watch the situation improve from there.</p>
    <p>Currently, the only unmodified client which supports signing multisignature transactions is Bitcoin Core. Otherwise, users can use an offline copy of <a href="https://coinb.in/multisig" target="_blank">https://coinb.in/multisig</a> to sign in their browser.</p>
    <p>It sucks that Bitcoin Core is the only client that lets us do this. I&#8217;m very much looking forward to a light client that supports it out of the box.</p>
    <p><strong>Training users to use multisig</strong><br />
    Multisig can seem complicated, but I&#8217;ve done what I can to make the process as smooth as practicality and security allows me to.</p>
    <p>I have decided against allowing buyers to click to sign with the Administrators key. The reason for this, is that it undermines the assurances that come with multisig. Buyers will be expected to sign</p>
    <p>Completing an order doesn&#8217;t require many complicated steps at once, but rather it is a gradual process where users are guided doing the transaction. If users have any experience with an electrum offline wallet, the process is very similar &#8211; Take unsigned transaction, sign, broadcast. I will create a document later which outlines the process using Bitcoin Core.</p>
    <p><strong>Order process:</strong><br />
    Step 0: Buyer choses their items, as normal. When they&#8217;re ready, they enter a public key, and their address, and confirm their order.</p>
    <p>Step 1: Vendor has a new order, must decide if it&#8217;s escrow, or up-front, based on ratings. The vendor has probably entered public keys in advance, but will be prompted to do so if not.</p>
    <p>Step 2: Awaiting Payment: Once the order is accepted by the vendor, and the terms are selected (up-front or escrow), the multisig address will be created, and available to all users. A redeemScript is given, allowing users to verify that the address is one they have control over (contains their public key). The buyer needs to pay to the address to continue.</p>
    <p>Once Bitwasp has seen enough incoming transactions to this address to cover the order, it will progress the order to the next step, which is signing. First, both users need to import the address to their wallet. A copy/paste command is shown to help them with that.</p>
    <p>Step 3:  Up-front order&#8217;s only &#8211; await buyer signature. If the order is up-front, then the buyer signs the unsigned transaction. They paste the <em>partially signed</em> transaction onto the order page and submit, where it will be verified, and the order progressed to step 4.<br />
    If the order is escrow, then the process skips this step, and the vendor signs/dispatches first.</p>
    <p>Step 4: Waiting for Vendor to deliver goods. The vendor signs to indicate they have dispatched.<br />
    If the order is up-front, then the vendor will now sign, and broadcast the transaction. Once Bitwasp see&#8217;s this transaction in the blockchain, then the order is moved to step 5.<br />
    If the order is escrow, the vendor will add the first signature to the transaction, and paste the partially signed transaction onto the order page.</p>
    <p>Step 5: Order has been dispatched. Await buyer to sign &amp; broadcast (Escrow), or click Received (Up-front).<br />
    If it&#8217;s up-front, the buyer simply clicks the &#8216;Received&#8217; button, and the order is completed (step 7). Otherwise, the buyer can raise a dispute.<br />
    If it&#8217;s escrow, when the goods arrive the buyer signs &amp; broadcasts the transaction paying the vendor, the order is marked as completed (step 7). Otherwise, the buyer or vendor can raise a dispute.</p>
    <p>Step 6: Disputed Order<br />
    If a dispute is raised, and the order was escrow, the administrator will be able to craft a new raw transaction, which pays the buyer/vendor an appropriate amount at their discretion. Ideally, both users should be satisfied with the outcome, but the admin can sign, and wait for the second signature, and the transaction to be broadcast, before the dispute is automatically closed, and the order marked complete (step 7)<br />
    If the transaction was up-front, all the admin can do is close the dispute, and mark the order as complete.</p>
    <p>Step 7: Completed Order<br />
    At this point, the buyer and seller will be asked to leave feedback for the other party.<br />
    A buyer will leave feedback for the vendor, and then the items.<br />
    A vendor will leave feedback for the buyer.<br />
    If the order was disputed, this will mark each review on the page as Disputed, allowing users to read what happened.</p>
    <p><strong>Leaving Feedback:</strong><br />
    Vendors can rate buyers on qualities like Cooperation and Communication, from 1-5. I want feedback on the community on this, and what people should be rating!</p>
    <p>Buyers can rate vendors on qualities like Shipping, and Communication, from 1-5. They also rate the items on an order, on qualities: Item Quality, and if it Matches Description. Again, I need feedback here.<br />
    When buyers leave feedback for an order with more than one item, they can choose to rate all the items with the same score, and comments, or else fill in ratings/comments individually.</p>
    <p>All users can leave comments about the vendor/buyer/item. These can be from a list of prepared statements (to mask people&#8217;s writing styles), or else a bespoke comment can be written. Also, feedback takes on average 12 hours to show up &#8211; All feedback will have a timestamp of 12pm the following day, so they appear in a batch.</p>
    <p><strong>Todo:</strong><br />
    I need to write up an article describing the commands to actually import, sign, and broadcast the transaction.<br />
    Transactions are created by the bitwasp software, so mostly its a case of pasting the unsigned/partially signed transaction into the bitcoin console, taking the output, and pasting to the site/broadcasting it.</p>
    <p>I need to work out the best solution for admins. Keys are generated using an electrum mpk, but electrum can&#8217;t sign transactions it produces.. I think admins will likely need to run Bitcoin Core on their own computer, dump the private key from electrum, import to Bitcoin Core, and then sign. Otherwise, they can use coinb.in.</p>
    <p>Once this gets adequate testing, things will be looking good. The code will start to become mature, and I can mop up the outstanding issues posted on the forum.</p>
    <p>I want to try and remove Bitwasps dependency on BitcoinD. There&#8217;s nothing I can do about the clients users use to sign, however I hope to find a way that allow it to run off an API, if that&#8217;s what people want.</p>
    <p>What I really need now is for developers to set up a copy, test it on the testnet, and work with me to finish the software, and take it to the next level. You all know it&#8217;s just me working on the code, but this project will only reach it&#8217;s true potential with help from the community. It&#8217;s got to be more give and take, so I&#8217;d ask if you&#8217;re considering to use Bitwasp, that you actively participate in it&#8217;s development, or donate to us here: 19EkDTAaGWySZv1QsWxyWwYMZpo7jpvPYe. The project isn&#8217;t ready for mainstream use yet, and we want help to accelerate things.</p>
    <p><strong>===End quote===</strong></p>
    <p>This is a guide to completing an order using Bitcoin Core, via the Help-&gt;Debug-&gt;Console window, or bitcoind using the command line. The commands entered at the bitcoin core console can be run just the same by doing: bitcoind &lt;command&gt; &lt;arguments&gt;</p>
    <p>As a buyer confirms their order, they are asked to enter a new public key, and their order address.<br />
    To generate a new public key using Bitcoin Core, run the following two commands</p>
    <div>Code: <a>[Select]</a></div>
    
    <div id="crayon-5c8bc8fa0507a106439697" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    &amp;gt; getnewaddress
    1HpCq3FVZf4UDvPjFSCz1V4aLMijdfKjfK
    &amp;gt; validateaddress 1HpCq3FVZf4UDvPjFSCz1V4aLMijdfKjfK
    {
    "isvalid" : true,
    "address" : "1HpCq3FVZf4UDvPjFSCz1V4aLMijdfKjfK",
    "ismine" : true,
    "isscript" : false,
    "pubkey" : "03ff0d9f8332ca6261739901fac22b520921ca370d98a354467a2ea6d2c93520cc",
    "iscompressed" : true,
    "account" : ""
    }
    </textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5c8bc8fa0507a106439697-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5c8bc8fa0507a106439697-2">2</div><div class="crayon-num" data-line="crayon-5c8bc8fa0507a106439697-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5c8bc8fa0507a106439697-4">4</div><div class="crayon-num" data-line="crayon-5c8bc8fa0507a106439697-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-5c8bc8fa0507a106439697-6">6</div><div class="crayon-num" data-line="crayon-5c8bc8fa0507a106439697-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-5c8bc8fa0507a106439697-8">8</div><div class="crayon-num" data-line="crayon-5c8bc8fa0507a106439697-9">9</div><div class="crayon-num crayon-striped-num" data-line="crayon-5c8bc8fa0507a106439697-10">10</div><div class="crayon-num" data-line="crayon-5c8bc8fa0507a106439697-11">11</div><div class="crayon-num crayon-striped-num" data-line="crayon-5c8bc8fa0507a106439697-12">12</div><div class="crayon-num" data-line="crayon-5c8bc8fa0507a106439697-13">13</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5c8bc8fa0507a106439697-1"><span class="crayon-o">&amp;</span><span class="crayon-v">gt</span><span class="crayon-sy">;</span><span class="crayon-h"> </span><span class="crayon-i">getnewaddress</span></div><div class="crayon-line crayon-striped-line" id="crayon-5c8bc8fa0507a106439697-2"><span class="crayon-cn">1HpCq3FVZf4UDvPjFSCz1V4aLMijdfKjfK</span></div><div class="crayon-line" id="crayon-5c8bc8fa0507a106439697-3"><span class="crayon-o">&amp;</span><span class="crayon-v">gt</span><span class="crayon-sy">;</span><span class="crayon-h"> </span><span class="crayon-e">validateaddress</span><span class="crayon-h"> </span><span class="crayon-cn">1HpCq3FVZf4UDvPjFSCz1V4aLMijdfKjfK</span></div><div class="crayon-line crayon-striped-line" id="crayon-5c8bc8fa0507a106439697-4"><span class="crayon-sy">{</span></div><div class="crayon-line" id="crayon-5c8bc8fa0507a106439697-5"> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-s">"isvalid"</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-t">true</span><span class="crayon-sy">,</span></div><div class="crayon-line crayon-striped-line" id="crayon-5c8bc8fa0507a106439697-6"> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-s">"address"</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-s">"1HpCq3FVZf4UDvPjFSCz1V4aLMijdfKjfK"</span><span class="crayon-sy">,</span></div><div class="crayon-line" id="crayon-5c8bc8fa0507a106439697-7"> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-s">"ismine"</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-t">true</span><span class="crayon-sy">,</span></div><div class="crayon-line crayon-striped-line" id="crayon-5c8bc8fa0507a106439697-8"> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-s">"isscript"</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-t">false</span><span class="crayon-sy">,</span></div><div class="crayon-line" id="crayon-5c8bc8fa0507a106439697-9"> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-s">"pubkey"</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-s">"03ff0d9f8332ca6261739901fac22b520921ca370d98a354467a2ea6d2c93520cc"</span><span class="crayon-sy">,</span></div><div class="crayon-line crayon-striped-line" id="crayon-5c8bc8fa0507a106439697-10"> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-s">"iscompressed"</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-t">true</span><span class="crayon-sy">,</span></div><div class="crayon-line" id="crayon-5c8bc8fa0507a106439697-11"> <span class="crayon-h"> </span> <span class="crayon-h"> </span><span class="crayon-s">"account"</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-s">""</span></div><div class="crayon-line crayon-striped-line" id="crayon-5c8bc8fa0507a106439697-12"><span class="crayon-sy">}</span></div><div class="crayon-line" id="crayon-5c8bc8fa0507a106439697-13">&nbsp;</div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    The pubkey field is then copied/pasted directly into the page.<br />
    <img alt="" src="http://thelaboratory.tk/buyer_confirm_order.png" width="600" /></p>
    <p>Vendors are able to upload several public keys at a time, by running the above commands several times.<br />
    <img alt="" src="http://thelaboratory.tk/vendor_add_public_keys.png" width="600" /></p>
    <p>If no keys are available in the vendors list, they will be prompted to enter some before they can accept an order. At this time they choose if the order should be escrow or up-front.<br />
    <img alt="" src="http://thelaboratory.tk/vendor_accept_order.png" width="600" /></p>
    <p><img alt="" src="http://thelaboratory.tk/buyer_pay_to_address_prompt.png" width="600" /></p>
    <p>Once the order is accepted, the multisignature address is generated out of the buyer, vendor, and administrators public key. The administrators public key is generated from a master public key.<br />
    The buyer must pay to the order in order to progress to the next step.<br />
    Once the order is paid in full, a raw transaction paying the vendor/admin is created.<br />
    <img alt="" src="http://thelaboratory.tk/buyer_payment_details.png" width="600" /></p>
    <p>(If the order is up-front, the buyer will be asked to sign the transaction first)<br />
    If it&#8217;s escrow, the vendor will sign. Once the vendor signs, they are indicating that they have dispatched the order.<br />
    <img alt="" src="http://thelaboratory.tk/buyer_awaiting_dispatch.png" width="600" /></p>
    <p>In order to sign the transaction, you need to add the multisig address to your wallet. This is done by copy/pasting the command shown on the order page into the Bitcoin Core console:</p>
    <div>Code: <a>[Select]</a></div>
    
    <div id="crayon-5c8bc8fa0508f212601039" class="crayon-syntax crayon-theme-classic crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover" style=" margin-top: 12px; margin-bottom: 12px; font-size: 12px !important; line-height: 15px !important;">
    <div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
    <div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="Toggle Line Numbers"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="Toggle Plain Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="Toggle Line Wrap"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="Expand Code"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="Copy"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="Open Code In New Window"><div class="crayon-button-icon"></div></div></div></div>
    <div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
    <div class="crayon-plain-wrap"><textarea wrap="soft" class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
    addmultisigaddress 2 '["02eec4737ddb62092d8b4834022ae41cf9af4faee9cc25b9b5c553eaa07d98a3dd","026d017c249eae64b039f3cb33c913a6f8762198d998cf03f440b66622bdb2c75c","04eadc08c551774e82a9869dc6279d96d66920a0ccdcd6ac94ebaa11aa33827c21096e2ec974d21411c653d8d60cca06936523fa2774f237a2c347ffdb3b1147aa"]'
    3GmeaSfxFAPbbUrcUojSbkUCGdPXwcm9HZ
    </textarea></div>
    <div class="crayon-main" style="">
    <table class="crayon-table">
    <tr class="crayon-row">
    <td class="crayon-nums " data-settings="show">
    <div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5c8bc8fa0508f212601039-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5c8bc8fa0508f212601039-2">2</div><div class="crayon-num" data-line="crayon-5c8bc8fa0508f212601039-3">3</div></div>
    </td>
    <td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5c8bc8fa0508f212601039-1"><span class="crayon-i">addmultisigaddress</span><span class="crayon-h"> </span><span class="crayon-cn">2</span><span class="crayon-h"> </span><span class="crayon-s">'["02eec4737ddb62092d8b4834022ae41cf9af4faee9cc25b9b5c553eaa07d98a3dd","026d017c249eae64b039f3cb33c913a6f8762198d998cf03f440b66622bdb2c75c","04eadc08c551774e82a9869dc6279d96d66920a0ccdcd6ac94ebaa11aa33827c21096e2ec974d21411c653d8d60cca06936523fa2774f237a2c347ffdb3b1147aa"]'</span></div><div class="crayon-line crayon-striped-line" id="crayon-5c8bc8fa0508f212601039-2"><span class="crayon-cn">3GmeaSfxFAPbbUrcUojSbkUCGdPXwcm9HZ</span></div><div class="crayon-line" id="crayon-5c8bc8fa0508f212601039-3">&nbsp;</div></div></td>
    </tr>
    </table>
    </div>
    </div>
    
    The same address as on the order page should be returned. Users can take this time to check that one of the keys in the address was the one they entered at the start.</p>
    <p>In order to sign the transaction, an extra JSON field is supplied as well as the raw transaction. This is required, but is automatically generated. Whenever a user is asked to sign a transaction, they can copy/paste the transaction into the console, and prefixed by the command &#8216;signrawtransaction&#8217;.<br />
    <img alt="" src="http://thelaboratory.tk/vendor_signing_transaction.png" width="600" /><br />
    Once the transaction is <em>partially</em> signed, it needs to be passed to the other user to add the final signature. Just paste the raw transaction <em>hex</em> back onto the site and submit.<br />
    <img alt="" src="http://thelaboratory.tk/vendor_pasting_partially_signed.png" width="600" /></p>
    <p>Once the buyer receives the goods, they can sign and broadcast the transaction.<br />
    <img alt="" src="http://thelaboratory.tk/buyer_completes_transaction.png" width="600" /></p>
    <p>The entire process guides users towards this final end result: the transaction leaving the multisig address:<br />
    <img alt="" src="http://thelaboratory.tk/blockchain_payment_1configm.png" width="600" /></p>
    <p>If there is ever a dispute along the way, the admin will be notified, and the users will have a chat thread to discuss the situation. If the order was escrow, the admin can create a new transaction. If the order was up-front, there is little the buyer can do unless the seller cooperates.</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/bitwasp/" rel="tag">bitwasp</a> <a href="https://www.deepdotweb.com/tag/built/" rel="tag">built</a> <a href="https://www.deepdotweb.com/tag/multisignature/" rel="tag">multisignature</a> <a href="https://www.deepdotweb.com/tag/offering/" rel="tag">offering</a> <a href="https://www.deepdotweb.com/tag/transactions/" rel="tag">transactions</a></span> <span style="display:none" class="updated">2014-04-04</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name">
    
