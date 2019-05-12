---
HOW TO VERIFY YOUR DOWNLOADED FILES ARE AUTHENTIC
---
4081


<p>I just had a realization about something that is pretty important and I wanted to share it with you, regarding security. <strong>Verifying your downloads</strong></p>
<p>As a general rule of thumb, you should <strong>always</strong> download files from the home pages of their respective developers.</p>
<p>TOR: https://www.torproject.org<br />
Tails: https://www.tails.boum.org<br />
Virtual Box: https://www.virtualbox.org/</p>
<p>The reason this is so important, is that there are people who host maliciously modified versions of these programs and will host legitimate looking sites to try and get you to download their version, which can install things like backdoors into your computers, keyloggers, and all types of nasty surprises. Sometimes developers will offer mirrors for their projects, which are simply just alternative links to download from in case the main server is too slow, or down. Sometimes these mirrors can become compromised without the knowledge of the developers.</p>
<p>Maybe you do not have TOR or Tails on your laptop and you are traveling out of the country and the hotel that you are staying at has TOR&#8217;s homepage blocked. There are times when you may need to find an alternative mirror to download certain things. Then of course there is the infamous <strong>man-in-the-middle</strong> attack where an attacker can inject malicious code into your network traffic and alter the file you are downloading. The TOR developers have even reported that attackers have the capability of tricking your browser into thinking you are visiting the TOR home page when in fact you are not.</p>
<p>So what do you do about it? You can verify that the file you downloaded is in fact legitimate. The best tool for this is <strong>GnuPG</strong>. The TOR developers recommend you get it from the following page (Windows Users).</p>
<p>http://www.gpg4win.org/download.html</p>
<p>You can install this program on your USB drive or on your actual computer, you will hear your actual computer&#8217;s operation system referred to as your Host OS. So download it, run it, install it and we will start showing you how to use GnuPG.</p>
<p>If you remain on the GnuPG download page you will see something under the big green box that is called <strong>OpenPGP signature</strong>. Download that into the same folder as the GnuPG file, this is the file that the download was signed with. Basically someone&#8217;s signature saying, I made this file. And you also need a PGP public key to verify the signature. So to sum it up so far, the signature is created from the PGP private key, and can be verified by the PGP public key. The signature file is used to verify the program itself. So let us grab the PGP public key for GnuPG as well.</p>
<p>If you look on the same download page, under the heading Installation, you will see a link where it says <strong>verify</strong> the integrity of the file. It will lead to you the following page.</p>
<p>http://gpg4win.org/package-integrity.html</p>
<p>Note where it says the following statement. <strong>The signatures have been created with the following OpenPGP certificate Intevation File Distribution Key (Key ID: EC70B1B8)</strong>. This is the link to the page that hosts the PGP public key file that you need to download, go there. On the page we just navgiated to, go to the bottom right where it says <strong>Intevation-Distribution-Key (public OpenPGP key for signing files)</strong> and download that file. This is the PGP public key file, save it to the same place as your signature file for ease of use.</p>
<p>Okay, now that we have both the signature file and the PGP public key, let us now verify our download. First thing you need to do is navigate to the PGP public key file, called <strong>Intervation-Distribution-Key.asc</strong>, right click it and go to <strong>More GpgEX Options</strong> and down to <strong>Import Keys</strong>. This will import the PGP public key into your key ring, and now you can verify the file with the signature.</p>
<p>Right click your actual file you want to verify, in this case <strong>gpg4win-2.2.1.exe</strong> and go to  <strong>More GpgEX Options</strong> and down to <strong>Verify</strong> and it should automatically detect the signature file where it says Input File, but if it does not, navigate to the signature file and make sure the box below it where it says <strong>Input file is a detached signature</strong> is checked. Look at the bottom and click Decrypt/Verify and you will likely get the following message.</p>
<p><strong>Not enough information to check signature validity. Check details</strong>.</p>
<p>Believe it or not, this is completely fine. Click on show details, you are looking for a specific result.</p>
<p><strong>Signed on 2013-10-07 08:31 by <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="07636e7473756e6572736e68692a6c627e476e697362757166736e6869296362">[email&#160;protected]</a> (Key ID: 0xEC70B1B8). The validity of the signature cannot be verified.</strong></p>
<p>If you navigate back to the page from Gpg4Win that says <strong>Check Integrity</strong> where you found the link to the page that contained the PGP public key you will see on that page.</p>
<p><strong>Intevation File Distribution Key (Key ID: EC70B1B8)</strong></p>
<p>Note the key ID from your decrypt result and the key ID from the Check Integrity page and note the email address ending in the same URL that we downloaded the PGP public key from. We have a match! I will explain the reason for this warning message later.</p>
<p>Now that we verified that our verification program is legit. Let us try and verify our Tails ISO file, since if we have a compromised Tails OS, then nothing we do will be anonymous. Let us get right to the Tails download page.</p>
<p>https://tails.boum.org/download/index.en.html</p>
<p>Scroll down to where it says Tails 0.22 signature and download that to your Tails folder where you have the ISO file that we already downloaded. Next scroll down to where it says Tails signing key, this is our PGP public key. Exact same procedure, import the key, then click Verify and specify the signature file if it has not already been specified for you, exact same settings and you will get the same warning message. As explained by Tails</p>
<div>
<div>Quote</div>
</div>
<blockquote><p>If you see the following warning:</p>
<p>Not enough information to check the signature validity.<br />
Signed on &#8230; by <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="1f6b7e76736c5f7d706a7231706d78">[email&#160;protected]</a> (Key ID: 0xBE2CD9C1<br />
The validity of the signature cannot be verified.</p>
<p>Then the ISO image is still correct, and valid according to the Tails signing key that you downloaded. This warning is related to the trust that you put in the Tails signing key. See, Trusting Tails signing key. To remove this warning you would have to personally sign the Tails signing key with your own key.</p></blockquote>
<p>In other words, you need to basically promise that the PGP public key you downloaded is safe by signing the PGP public key with your own private key, but we do not really need to do that and I will not be including a tutorial on how to do that. Tails explains that if you are worried about a compromised PGP public key, just download the key from multiple sources and compare them, if they all match, it is a good chance you are using a legit PGP key. Now let us finally move on to TOR because this one will be a little less straight forward, but once you do this one, you should be able to figure out how to verify anything. Navigate to their download page and find the package that you want.</p>
<p>https://www.torproject.org/download/download.html.en</p>
<p>To keep things simple let us choose Tor Browser Bundle 3.5, and under the orange box you will see a link <strong>(sig)</strong>. This is the link for the signature file, I hope by now you know what to do with it. Next we need the PGP public key right? Well it turns out that with so many developers working on TOR, there are multiple PGP public keys, and certain bundles were signed with different keys than other bundles. So we need to find the PGP public key that belongs to our Tor Browser Bundle. Check out this page.</p>
<p>https://www.torproject.org/docs/signing-keys.html.en</p>
<p>It has a list of all the signing keys that they use and you can certainly use these key IDs to get what we want by simply right clicking on the signature file and click verify. You will get a warning.</p>
<p><strong>Not enough information to check signature validity. Show Details</strong></p>
<p>And in details it will say the following warning.</p>
<p><strong>Signed on 2013-12-19 08:34 with unknown certificate 0x416F061063FEE659</strong></p>
<p>Keep this entire number in mind for later, it is called a fingerprint. But for now if you just compare the last 8 digits to Erinn Clark&#8217;s key ID (<strong>0x63FEE659</strong>) provided on the above page, and since she is the person who signs the Tor Browser Bundles you will see they match. But we want to be a bit more thorough, never settle for mediocrity.</p>
<p>Go to your task bar in Windows, and find the program called <strong>Kleopatra</strong>, it looks like a red circle with a small white square in it. Right click it and go to <strong>Open Certificate Manager</strong>. We are going to import the full keys using this manager. Also note, if you go to the tab that says <strong>Other Ceriticates</strong> you will find the Tails and Intevation (GnuPG) keys we used earlier stored for the future when you need to download a new version of those programs and verify them again.</p>
<p>We are going to be following the instructions from the <strong>verifying signatures</strong> page on the TOR Project website. Feel free to follow along from that page so you know what I am talking about and where I am getting my URL and numbers from.</p>
<p>https://www.torproject.org/docs/verifying-signatures.html.en</p>
<p>In order to import keys, we need to first add an online directory where they are stored. So let us first add the online directory where the PGP public keys are stored according to the TOR website. Click <strong>Settings then Configure Kleopatra</strong>. Next, click New and we are going to enter the following URL which I took right from the page above. <strong>pool.sks-keyservers.net</strong>, and leave everything else as default and click OK.</p>
<p>Finally, click the button that says <strong>Lookup Certificates On Server</strong> and we will be searching for Errin Clark&#8217;s PGP public key by searching for her <strong>fingerprint</strong> provided on the TOR website page called <strong>Verifying Signatures</strong> above, remember, she is the developer who signs the Tor Browser Bundle. The fingerprint we are entering is <strong>0x416F061063FEE659</strong>, does this number look familiar? It should, it is the number we got back the first time we tried verifying but without the actual PGP public key. if you get any warnings that pop up when searching just click OK and it should bring up Errin Clark&#8217;s key, select it and click <strong>Import</strong>. You should now have her key listed under <strong>Imported Certificates</strong>.</p>
<p>Now let us go back and verify that signature one more time and see what happens. You should get something like the following.</p>
<p><strong>Not enough information to check signature validity.</p>
<p>Signed on 201-12-17 12:41 by <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="9bfee9e9f2f5dbeff4e9ebe9f4f1fef8efb5f4e9fc">[email&#160;protected]</a> (Key ID: 0x63FEE659).<br />
The validity of the signature cannot be verified.</strong></p>
<p>TOR also explains this warning message in their words in case you are still not happy with the warning message.</p>
<div>
<div>Quote</div>
</div>
<blockquote><p>Notice that there is a warning because you haven&#8217;t assigned a trust index to this person. This means that GnuPG verified that the key made that signature, but it&#8217;s up to you to decide if that key really belongs to the developer. The best method is to meet the developer in person and exchange key fingerprints.</p></blockquote>
<p>I do not know about you, but I am happy with the result here, and I am certainly not going to track down Erinn Clark to get her key fingerprint, and it looks like our TOR Browser Bundle is legitimate as well! Now you know what to do when the PGP public key file is not directly hosted on the site itself, you have no more excuses to not verify your downloads.</p>

Updated: 2014-02-13

