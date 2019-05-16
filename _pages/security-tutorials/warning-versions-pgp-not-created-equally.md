---
layout: single
title: "Word of Warning &#8212; All versions of PGP are NOT created equally!"
sidebar:
  - title: "Security Tutorials"
    nav: "security"
  - title: "Jolly Rogers Security Guide"
    nav: "jolly"
  - title: "Blog Archive"
    nav: "blognav"
permalink: "security-tutorials/warning-versions-pgp-not-created-equally/"
redirect_from: 
  - "security-tutorials/word-warning-versions-pgp-created-equally"
  - "security-tutorials/warning-versions-pgp-not-created-equally"
---

<p>The version lines that are usually shown by default in PGP keys and PGP signature blocks, often reveal which OS the person is using.</p>
<p><strong><span class="bbc_u">PGP/GPG Version strings:</span></strong></p>
<p>You can tell a fair bit about a user&#8217;s PGP/GPG setup from their Version: string. Here are some typical examples:</p>
<p>Version: GnuPG v1.4.11 (GNU/Linux)</p>
<p>This key belongs to a Linux user.</p>
<p>Version: GnuPG v2.0.19 (MingW32)</p>
<p>This key belongs to a Windows user.</p>
<p>Version: GnuPG/MacGPG2 v2.0.17 (Darwin)</p>
<p>This key belongs to a Mac OS X user.</p>
<p><strong><span class="bbc_u">Versions that should make you nervous:</span></strong></p>
<p>Version: 9.9.0.397</p>
<p>This person is using the official PGP version, as published by Symantec. I&#8217;ve read statements by Kevin Mitnick that he no longer trusts PGP, since it was acquired by Symantec.   In his post, Mitnick refers to the case of Diskreet, which back in the early days, was an encryption package sold by Symantec. This software purported to use the full 56-bit DES cipher algorithm, which was quite strong for its day. Mitnick stated that he acquired a copy of the Diskreet source code, and discovered that the actual key was nowhere near 56-bits, but was incredibly weak. He went on to say that based on his experience, he would not trust any version of PGP published by Symantec.</p>
<p>His caution is only underscored by the Snowden revelations earlier this Summer, which set out the NSA&#8217;s campaign of attempting to weaken or backdoor crypto.<br/>
I, for one, would not trust any closed-source crypto software published by an American company &#8212; that goes double for companies with a history like Symantec.</p>
<p>To the best of my knowledge, Symantec does not publish PGP source code, and as an American company, their crypto software is now suspect.</p>
<p><strong><span class="bbc_u">Versions of PGP  that should make you run away screaming: </span></strong></p>
<p>Versions of PGP with these Version: strings are based on the BouncyCastle Java crypto libraries. They should be avoided like the plague.</p>
<p>Version: BCPG v1.45<br/>
Version: BCPG v1.47</p>
<p><strong><em>These versions of PGP are absolutely NOTORIOUS for generating MASSIVELY UNSAFE PGP keys by default.</em></strong> These versions typically generate DSS/Elgamal keys<br/>
with signing keys with a size of 1024-bits, and an encryption sub-key of as little as 512-bits.<br/>
By: Nightcrawler</p>
<p>512-bit keys are so unsafe, that they were being broken by hobbyists on spare hardware a dozen years ago. 1024-bit keys were deprecated by NIST more than 3 years ago.</p>
<p>Version: BCPG C# v1.6.1.0</p>
<p>This version of PGP generates by default a PGP key of 1024-bits, with NO encryption sub-key. Again, these keys are unsafe/obsolete.</p>
<p><strong><span class="bbc_u">Recommendations: </span></strong></p>
<p>Any software that uses the Java Bouncycastle crypto libraries (like PortablePGP) should be avoided like the plague. These typically contain BCPG in the Version: string.</p>
<p>GPG4Win/Kleopatra/GPA are also deprecated &#8212; Kleopatra generates RSA keys <em>without</em> an encryption sub-key. Dual RSA keys, with one RSA key for signing, and the other exclusively for encryption have been standard since the Fall of 2009.<br/>
GPA will not generate keys over 3072-bits in length.</p>
<p>GPG4USB or Gnu Privacy Tray (GnuPT) are recommended, as they are:</p>
<p>* Easy to use</p>
<p>* Standards compliant</p>
<p>GnuPT, in particular, is frequently updated. Usually, when there is a new GPG version (e.g. 1.4.15), the GnuPT developers issue an update with a day or two, reflecting the change.</p>
<p>Download links:</p>
<p>GPG4USB: http://gpg4usb.cpunk.de/index.html</p>
<p>GnuPT: http://www.gnupt.de/ (Site is in German)</p>

Updated: 2014-05-11

