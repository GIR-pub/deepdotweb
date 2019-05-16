---
title: "New Multisig Marketplace: Hydra market"
---

<span>April 12, 2014</span>
    
<a href="/2014/04/12/new-multisig-marketplace-hydra-market/#comments">13 Comments</a></span>
</p>
<p style="text-align: center;"><span style="color: #ff0000;"><strong>&gt;&gt; <a style="color: #ff0000;" href="tag/silkroad2bust/">HYDRA Market Was Seized During Operation Onymous &#8211; Learn More about Operation Onymous Here</a> &lt;&lt;</strong></span></p>
<p>As part of our efforts to support marketplaces that are offering multisig transactions, like we did before with TMP, Blackbank market &amp; Drugslist (before the other issues) we are happy to post about this new market offering multisig transactions, and by this lowering the risk for both users and vendors, this is the instructions for using their multisig transaction system as it appears on their site, with the images included.</p>
<p>This is the hydra marketplace url: <strong>http://hydrampvvnunildl.onion/register/ktgvv60br5et</strong><br/>
    (this is a referral only market &#8211; the link above includes a ref link)</p>
<p><span style="text-decoration: underline;"><strong>Multisig</strong>:</span></p>
<div>
<div>
<dl>
<dt>Bitcoin/Litecoin multisig transactions on HYDRA</dt>
<dd>
<ul>
<li>Customer deposits coins into HYDRA account, if vendor also set up their pubkey and address, customer can make purchase with multisig escrow.</li>
<li>Don&#8217;t need to enter your pubkey/address on every purchase (You can use it like PGP).</li>
<li>Hydra automatically will generate our own public key, charge fee, create a multisig address and send fund to this address</li>
<li>You can track multisig transactions on btclook.com</li>
<li>2 of 3 Private keys required to access the funds (e.g. Customer + Hydra -&gt; refund, Vendor + Hydra -&gt; finalize, Vendor + Customer -&gt; finalize/refund/etc).</li>
<li>When customer will have finalize multisig order, we sign it with our key and send message to vendor with transaction details.</li>
<li>Nobody will be able to steal your money ever.</li>
</ul>
</dd>
<dt>Create your Public and Private Key with your bitcoin/litecoin client</dt>
<dd>Open your bitcoin/litecoin clients debug console and type the following commands:getaccountaddress HYDRA_KEYCopy the address from output and add to next command.validateaddress [PASTE_THE_PREVIOUSLY_GENERATED_ADDRESS]It will return with address details. You&#8217;ll find your public under &#8220;pubkey&#8221; section.Get your private key.dumpprivkey [PASTE_THE_PREVIOUSLY_GENERATED_ADDRESS]</dd>
<dt>Create your Public and Private Key online</dt>
<dd>You will need to use Javascript, clearnet site.<a href="http://brainwallet.org/#generator">brainwallet.org</a>Save your newly generated Private and Public key.</dd>
<dt>Set up your HYDRA account to use multisig</dt>
<dd>Bitcoin address: Bitcoin refund address if you&#8217;re customer and payment address if you&#8217;re vendorBitcoin pubkey: We&#8217;ll use this key to lock the fundsLitecoin address: Litecoin refund address if you&#8217;re customer and payment address if you&#8217;re vendorLitcoin pubkey: We&#8217;ll use this key to lock the funds</dd>
</dl>
</div>
</div>
<p><span style="text-decoration: underline;"><strong>Guide in screenshots:</strong></span></p>
<img src="https://G-I-R.github.io/deepdotweb/imgs/2014/04/msguide_page_001.jpg" />


Updated: 2014-04-12
    
