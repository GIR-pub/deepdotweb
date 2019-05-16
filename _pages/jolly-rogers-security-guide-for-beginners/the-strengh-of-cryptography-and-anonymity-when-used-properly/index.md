---
layout: single
title: "THE STRENGH OF CRYPTOGRAPHY AND ANONYMITY WHEN USED PROPERLY"
---

<p>This post is meant to serve as an example of how, when cryptography and anonymity is used properly, you can evade just about anybody including the police.</p>
<p>By now, everyone has likely heard of someone getting locked out of their computer and being forced to pay by the attacker to have it unlocked, this is CryptoLocker. Dell SecureWorks estimates that CryptoLocker has infected 250,000 victims. The average payout is $300 each, and millions in laundered Bitcoin have been tracked and traced to the ransomware&#8217;s money runners.</p>
<p>CryptoLocker is a ransomware trojan which targets computers running Microsoft Windows[1] and first surfaced in September 2013. A CryptoLocker attack may come from various sources; one such is disguised as a legitimate email attachment. A ZIP file attached to an email message contains an executable file with the filename and the icon disguised as a PDF file, taking advantage of Windows&#8217; default behaviour of hiding the extension from file names to disguise the real .EXE extension. When activated, the malware encrypts certain types of files stored on local and mounted network drives using RSA public-key cryptography to generate a 2048-bit RSA key pair, with the private key stored only on the malware&#8217;s control servers.</p>
<p>The malware then displays a message which offers to decrypt the data if a payment (through either Bitcoin or a pre-paid voucher) is made by a stated deadline, and threatens to delete the private key if the deadline passes. If the deadline is not met, the malware offers to decrypt data via an online service provided by the malware&#8217;s operators, for a significantly higher price in Bitcoin.</p>
<p>Dell SecureWorks estimates that CryptoLocker has infected 250,000 victims. The average payout is $300 each, and millions in laundered Bitcoin have been tracked and traced to the ransomware&#8217;s money runners. In November 2013, the operators of CryptoLocker launched an online service which claims to allow users to decrypt their files without the CryptoLocker program, and to purchase the decryption key after the deadline expires; the process involves uploading an encrypted file to the site as a sample, and waiting for the service to find a match, which the site claims would occur within 24 hours. Once a match is found, the user can pay for the key online; if the 72-hour deadline has passed, the cost increases to 10 Bitcoin.</p>
<p>To date, no one has successfully defeated CryptoLocker. The Swansea, Massachusetts police department was hit in November. The officers paid CryptoLocker&#8217;s ransom. Police Lt. Gregory Ryan told press that his department shelled out around $750 for two Bitcoin on November 10. One of the reasons I am posting this, is that CryptoLocker uses 2,048 RSA encryption, and if you remember in the PGP posts earlier in this thread I recommended to use 4096. Even with 2,048 bit encryption, no one has successfully defeated CryptoLocker, and this is the power of properly implemented cryptography.</p>
<p>And, using the proper methods of anonymity, this person or group has managed to acquire, according to research done by ZDNet, around 41,928 BTC.</p>
<p>http://www.zdnet.com/cryptolockers-crimewave-a-trail-of-millions-in-laundered-bitcoin-7000024579/</p>
<div>
<div>Quote</div>
</div>
<blockquote><p>In research for this article ZDnet traced four bitcoin addresses posted (and re-posted) in forums by multiple CryptoLocker victims, showing movement of 41,928 BTC between October 15 and December 18.</p>
<p>Based on the current Bitcoin value of $661, the malware ninjas have moved $27,780,000 through those four addresses alone &#8211; if CryptoLocker cashes out today.</p>
<p>If CryptoLocker&#8217;s supervillans cash out when Bitcoin soars back up to $1000, like it did on November 27&#8230; Well, $41.9 million isn&#8217;t bad for three months of work.</p></blockquote>
<p>As you can see, properly executed cryptography and anonymity allowed this group of people acquire the Bitcoin equivalent of almost $42 million in just now 4 months at the time of this post. I am not recommending or advocating that you do this, but just giving you a perfect example of how powerful the combination of these two very important factors are in protecting anybody online when used properly.</p>

Updated: 2014-02-13

