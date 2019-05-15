---
title: "Alphabay Updates UI, Introduce New Onion Cloner Countermeasure"
---

Posted by: DeepDotWeb 

<span>November 18, 2015</span>



<p><a href="#">onion cloner phishing scams</a> (common phishing scam sites which proxy markets on the fly while replacing deposit addresses to their own addresses in order to scam users into sending their BTC to the phishers instead of the market).</p>
<p>New users are advised to verify the PGP signature of their deposit address against the market pgp key located in its &#8220;contact&#8221; page.</p>

<img src="/imgs/2015/11/deposit.png">

<p>This is how it looks:</p>

<img src="/imgs/2015/11/pgpsigned.png">

<p>You can learn more about PGP signatures <a href="/jolly-rogers-security-guide-for-beginners/verifying-signed-messages-with-signatures-and-signing-your-own-messages/">here</a>.</p>
<p>This is the original update posted by the market admins:</p>

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA512
    
    We just finished redesigning the market's place UI in order to improve
    it and make it look more modern. We hope you enjoy the new clean
    and responsive UI. In addition to that, we made a few additional changes.
    (if you use a VERY outdated browser and for some reason the new skin
    does not display correctly, you can add "/old" to the URL to use the old
    interface)
    
    - -- Orders &amp; Sales --
    All orders and sales will be purged securely from the list 30 days after finalization.
    For security reasons, and in case the account gets compromised, this was the
    best option to do.
    
    - -- User List --
    The user.php page no longer accepts a numeric parameter. The username must
    now be supplied. This will prevent phishers from iterating through the user IDs
    and messaging new members with phishing links. Also, some people were
    suspecting us of inflating the user count. We don't, but to solve the problem, we
    completely removed the user count.
    
    - -- Messages --
    The user title is now made more clear in the messages page. This is done in an
    effort to prevent impersonation and make the user's ranking more clear.
    
    - -- Deposit Address PGP Proof --
    We added a feature where users can get a PGP-signed proof of deposit address.
    The helpdesk was filled with "missing deposits" requests where the answer was
    "this isn't an Alphabay address". Many phishing pages make a few customization,
    for example displaying an address of their own, so you send coins directly to the
    attackers. You now can have a proof that your deposit address is authentic.
    
    Enjoy!
    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v1
    
    iQEcBAEBCgAGBQJWS1S2AAoJEOAZpE/dncxmpR0IAK81sEn7h9ga3MDlZsiFYstQ
    /2DCJouk5vU289hQUNpzJQ+NXBDI/LPniL6SLHTEzyGCuMZ2i5avOMXx75TCufsE
    PgcmZxPVxLZoOcUvXxDUfWNFcS1/MY3zlhm3KFrm+QDO+gViVlXh7zogamMwU0WD
    Bxo6PKNcHqPxIfS6J5lE7m1gYoHQwwn981VJFinjmu+QMpwOH5xisBYcELppg+8z
    YgbTmttQ4D7yumDYt2MfDct7WBYJaxfunqeN2MJwhnb2qVwP3PdTPR90OU4tQhoC
    KXPxIFdAVtMqx/pXNUB1eIJ/dva2hYyblD7QFyiWttOhS50L3MzROFH1JeDfG4A=
    =uv7e
    -----END PGP SIGNATURE-----

<p>
    Reminder: Use market links obtained from <a href="/2013/10/28/updated-llist-of-hidden-marketplaces-tor-i2p/">trusted</a> <a href="/dark-net-market-comparison-chart/">sources</a> only and encourage the use of <a href="/2015/11/12/reminder-reduce-exit-scams-by-supporting-multisig-markets/">multisg transactions</a>.</p>

Updated: 2015-11-18

