---
layout: single
title: "VERIFYING SIGNED MESSAGES WITH SIGNATURES AND SIGNING YOUR OWN MESSAGES"
sidebar:
  nav: "jolly"
permalink: "jolly-rogers-security-guide-for-beginners/verifying-signed-messages-with-signatures-and-signing-your-own-messages/"
redirect_from: "jolly-rogers-security-guide-for-beginners/verifying-signed-messages-with-signatures-and-signing-your-own-messages"
---


<p>Since we just finished a section on verifying downloads with signatures and public keys, I figured we should do a quick post on verifying messages by using the same two things, signatures and public keys.</p>
<p>Now for those of you who are members of the Silk Road Forums, you will notice that some people, mainly Moderators like to sign their messages with signatures. Let us look at an example of a signed message from Dread Pirate Roberts. The last message he left before going on his leave of absence.</p>
<div>
<div>Quote</div>
</div>
<blockquote><p>&#8212;&#8211;BEGIN PGP SIGNED MESSAGE&#8212;&#8211;<br/>
Hash: SHA512</p>
<p>Silk Road has not been compromised even if the allegations are true. Neither had access to sensitive material. I will make an announcement later to address the concerns this has raised.<br/>
&#8212;&#8211;BEGIN PGP SIGNATURE&#8212;&#8211;</p>
<p>iQIcBAEBCgAGBQJStEgqAAoJEMyyOOR8/t+867AP/RpjCq1B3WSYgnscbZU+UZOy<br/>
K0AGMM7tmu1DV1pr2S379YjVxQeUWeTbwDYhaYcWkDBDshnlpSd97fwAL1YVrBQx<br/>
jWE08tyo1sd1v5F/HajCx0DC2L5NeqD4UTDd6Dl2AOeBI4pZ+Ah/Q4VoB9cOBQGw<br/>
lSbjBY2U4redqBeRd1mFR8N+f3XmxYXzmB4Mf8ddvQkl62HmkwRwA27uUExt73uj<br/>
f3/EYVc/XjPgKG345S8yUwcGxLQcfoRM7UosbSGeEaDvvWjfZ6qQw4p7CbqIimHu<br/>
IOT6dhFcPmoVdiZGDvjtM3jXfF2sTi5mclGp/4axsrvOWZlCbrobE9EuJnGvscU4<br/>
ekU90vtcviES9XEJAr9XGOGgzY/OBf1xpj0iRY7rBDHUqA/FjfSULxqanZYhh0Wn<br/>
webHldrjylBRKM0PsnQdPn1CVGj8ThwB6SLfd0WEN1FEQt0hXP3uK1zDOri/fIcJ<br/>
Pnvf3jxYNcw9Q+2OW6QpZ/7t+S2E0yiifbNCobAMI18mrynuw3pk/xumg6t2WF/j<br/>
YHRpbTfFCCsbiPwR8P9CcUNQ5Iqcc2ewq4GOPx053aL/Vo/nfPdu/9hrRpfF3U5E<br/>
J7rFvAStaejxH7/vNxZRrTTiwrrc6njsFJHXWVAJjd+fHLI1efptbc8Kzwms9Yl0<br/>
0nzLjAJPFZOv6y7gP8tG<br/>
=lDZd<br/>
&#8212;&#8211;END PGP SIGNATURE&#8212;&#8211;</p></blockquote>
<p>So why should you care about this? What is the significance of signing a message? The reason is, in case somebody were to compromise DPR&#8217;s account, due to having a weak password or possibly an exploit in the forum&#8217;s coding, then the person would not be able to sign the messages without access to DPR&#8217;s private key. So let us look at how we can verify this message left by DPR. First of all you need to visit Dread Pirate Roberts&#8217; profile page and grab his PGP public key. I am not going to post the key here for space reasons, but just visit his page at the following URL and import that key into your keyring.</p>
<p>http://silkroad5v7dywlc.onion/index.php?action=profile;u=1</p>
<p>Next, highlight the entire PGP signed message from top to bottom and copy it to your clipboard (Right click, Copy). You will see your little Clipboard icon in the top right of Tails turn red. Click on that clipboard and select <strong>Decrypt/Verify</strong>. You should get the following results. One in the window on top and the other on the bottom.</p>
<div>
<div>Quote</div>
</div>
<blockquote><p>Silk Road has not been compromised even if the allegations are true. Neither had access to sensitive material. I will make an announcement later to address the concerns this has raised.</p>
<p>gpg: Signature made Fri 20 Dec 2013 01:37:46 PM UTC using RSA key ID 7CFEDFBC<br/>
gpg: Good signature from &#8220;Dread Pirate Roberts &lt;silkroad6ownowfk.onion&gt;&#8221;<br/>
gpg: WARNING: This key is not certified with a trusted signature!<br/>
gpg:          There is no indication that the signature belongs to the owner.<br/>
Primary key fingerprint: 5A48 F5D0 50E9 9052 62B4  799D CCB2 38E4 7CFE DFBC</p></blockquote>
<p>Again we get the same warning we did when verifying our downloads, saying we have not verified that the PGP public key is authentic. We can see the signature name was made by Dread Pirate Roberts and the comment section has the Silk Road URL, so far so good. Now remember when we verified TOR? We wanted to check out the fingerprints to see if they matched. We do this by going to our key ring (Manage Keys), and selecting DPR&#8217;s key, right clicking it and going to properties. Now move to the tab <strong>Details</strong> and look under where it says Fingerprint: and compare the numbers in there to the numbers we got when we verified the signature. They should be the following.</p>
<p><strong>5A48 F5D0 50E9 9052 62B4<br/>
799D CCB2 38E4 7CFE DFBC</strong></p>
<p>We have ourselves a match! So unless DPR&#8217;s private key was compromised, we know that he himself was the one who wrote that message. So now you see why some people decide to sign their messages. It is a way of verifying that their account has not been compromised by verifying that the person in control of the account is the same person that is in control of the PGP private key.</p>
<p>Do you want to learn how to sign a message? It is very easy. Open up gedit Text Editor and type in a message. Next, select the message and copy it to your clipboard (Right Click &#8211; Copy) and then click on your clipboard icon up top and choose <strong>Sign/Encrypt Clipboard with Public Keys</strong>. Do not choose a key from your list of PGP public keys unless you want to encrypt the message. If you want to encrypt the message to send to somebody&#8217;s inbox or so that only one person can view it, then select their name and it will encrypt it with their PGP public key. In our case, we just want to sign the message without encrypting it, but you can certainly do both at the same time if you wanted to.</p>
<p>If you look down near the bottom you will see where it says <strong>Sign message as:</strong> click on this and select your personal key. It will ask you for your passphrase because remember you are signing this with your private key. Once you enter it correctly, the PGP signed message will be copied to your clipboard and you can paste it anywhere (Right Click &#8211; Paste) that you want to. Here it what mine looked like.</p>
<p>&#8212;&#8211;BEGIN PGP SIGNED MESSAGE&#8212;&#8211;<br/>
Hash: SHA512</p>
<p>This is my PGP signed message for demonstration purposes.<br/>
&#8212;&#8211;BEGIN PGP SIGNATURE&#8212;&#8211;</p>
<p>iQIcBAEBCgAGBQJS0GiWAAoJEPuh6tSg81nyqXAP/2mEqvk9RP0FEHZi3edH9faV<br/>
OmDoOostmzm90nGMGOOu4cuG0M6jgl7R3hfUZBE6zCh59MG8a9EDuUzpIT3U5nfd<br/>
zS0GWtzUQKGXPXfJ1OvWlsA6Sm7TsEsviBBz5DJxyVLcJGNU6OLUVm7onxBLwfTq<br/>
D1jAATIB43WJbDrq3XY9MF9GCoOLlcLeKNVa4m0JF582IvQJ05mSZXeXCueImvol<br/>
FaflpLW5MKyJJ92a8uheB0pLHUQTLr6jZn6TcfKY9dK8puOam5k2TGut/Sm47uqc<br/>
aMA1trXw4xntww/8X4QyL5SbSN7QVOFsy/g0b3Grp5OrConsfnsUoeRH5ArnxY0W<br/>
ijPl92aTbZazvXspW2REkJ3yq+fWjuGrYHw8m7/YVBig+OSMuBUXhSE5Pjq95fyM<br/>
bA1P7rF2fi7eRsl1z0qyETV3Bs1RltwvBUVIwj3SZNeVVoG5cHgpiPgGFq4S9Qke<br/>
unIFeHy3YpBk90kLA1n8n61VnkKAUy0Dt9AoTJloeOqPtcgeKHVsFzxdPCBcSwqd<br/>
XYnIx4lNeaw4OvHYgZsCMvFlUItSBGnFWLN9foQ8UybAUPGI9Z4sK2WmtyWK4fLl<br/>
cXnYY9zt56Ji4DiVsQrEUamNTQEDGxpvBL/kQKRMKN6HviEXW+qr57LAo6t6sTQw<br/>
KTV4uJkH1JxuOOhN9tIe<br/>
=Nkox<br/>
&#8212;&#8211;END PGP SIGNATURE&#8212;&#8211;</p>
<p>And if you want to verify it, check out my PGP public key in my profile and verify my PGP signature against my key! It is really that simple. But you might be asking, cannot somebody just change the message and copy the signature? No, changing the message will change the signature because the signature depends on both the message and the PGP private key. So if you change one single character of my signed message you will get the following error.</p>
<p><strong>gpg: Signature made Fri 10 Jan 2014 09:39:34 PM UTC using RSA key ID A0F359F2<br/>
gpg: BAD signature from &#8220;Jolly Roger (They would live and die under it)&#8221;</strong></p>
<p>So when should you sign a message? And when should you not sign a message? Great question. The majority of users should probably not sign messages unless they have to because it gives you plausible deniability. It is easier to deny posting certain things or certain communications you may have had with vendors or other people including law enforcement if you do not sign your messages, because you can always claim somebody else gained access to your account. It is harder to do this if you signed the message with your PGP private key. If you are dealing with somebody who wants to verify your identity and make sure that your current signature matches the public key they had on file for you from 6 months ago, then maybe they might get you to send a signed message. But again, all they really need to do is send you an encrypted message with your PGP public key they had on file, and if you cannot decrypt it, you are not who you say you are.</p>
<p>In real world application, developers can use PGP signed messages in News Announcements or perhaps new releases of their programs providing a download URL so that users can be sure the developer is the one posting the URL and not some malicious attacker who compromised the forum account of the developer and so forth. So for the average Silk Road forum user there really is not a lot of times when you should be signing messages unless you are a moderator or making a public announcement and so forth, but it is an option you now have in your arsenal, and now you can start verifying the signatures of the Administrators and Moderators in case you believe their accounts may have been compromised.</p>

Updated: 2014-02-13

