---
title: "70 Malicious Tor Exit Nodes Exposed By Siganit.org"
---

Posted by: DeepDotWeb 

<span>April 26, 2015</span>



<p>If you are a Sigaint email user you probably received this email last week:</p>

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA1
    
    Hello SIGAINT user,
    
    We have recently found out that over 70 Tor exit nodes have been rewriting
    the
    cleartext page on sigaint.org.
    
    We have reported the bad exit nodes to the Tor Project and they have been
    removed. We are actively coordinating with them to keep bad exit nodes off of
    the Tor network.
    
    If you have ever browsed to sigaint.org to find our onion address, your
    account
    may be at risk.
    
    We ask that our users change their password as a precaution if you feel you
    might have done the above.
    
    You can change your password by following this link:
    http://sigaintevyh2rzvw.onion/chpass.php
    
    This message is PGP signed so you can verify that it is authentic.
    
    Thank you,
    The Cats at SIGAINT
    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG
    
    iQIcBAEBAgAGBQJVOFSNAAoJEM1IOzMPil9PD5MP/RQTnI7bhTeODxxYCfNNAPkp
    Q37cRp13vuOejN7ow+3FD9SjUf4IH8ACQmYbWDD2o1rbFZemK6QWLwTEe1/BqorG
    q1qFR4c+gpJDdp6IcppMFN1qRkxiuMeIxII0+i7Uv9z9rlMZCwiook5yHQ3TmOd7
    8o8RxXg+H6UT6xJHWtvaUSTncEC2QLcgeCGXDisPrUs3bSxPGs34Oq9jdbl46/4d
    nz0Tg8QpsMjefJ3i2AveQlosnrwP8CidU2xR2frwLfaxemd1122415HFBmGj5ohx
    3Q7mcT1boGHq9mccRFm1ojNFLas6WRQHyJcZ4CfLPuiS7fQbculUE1f+rZx5DFMo
    WfiQR0zjSklp2vYqUbW3bpZapSDaw334FKCJvwdKtmfz8eE9Ccy83gdhrwc9IO0D
    y8eHz+1ERDm4uWJVUetPt6lJb0X5Hc05+HxCcxQzpZLbvAcKAr2i346Ce+54aVlJ
    +l+c/BLznNIymF5hF+WFAjWRq+ijuGnXU4a3xbbVMGiLAvJWgrFkWXsyjd+GHSx4
    76MQfsW2zd9c9B+lC3lb1jIVllob4SeK8dQ7teC+hX+xZVIWEZRnB/EsqRpNJXsi
    QhQ3ciq41XpQeyCpRoAZP1hZI3FXaETsoU5PTXvaSHOx+yJAdDBmA4uLGbhiMWlh
    4iFX6Vw0IXgjPZcYVZti
    =Fkou
    -----END PGP SIGNATURE-----

<p>
<span style="text-decoration: underline;"><strong> And this is the story behind it as it was shared with us by the owner of <a href="/2015/02/16/interview-sigaint-darknet-email-admin/">sigaint darknet email</a> service:</strong></span></p>
<p>We started noticing some strange circumstances. We usually get a few complaints from law enforcement per week regarding abusive users of the service.</p>
<p>After the month of March had passed and we hadn&#8217;t had a single complaint we figured something strange was going on.</p>
<p>About a week ago someone started trying to break into the servers that warehouse user data. The attacks were relentless. After a full audit we realized that the attacker didn&#8217;t get in. (We employ extensive exploit mitigations that deflect even worst 0day exploits.)</p>
<p>Around the same time we received a complaint from a user that noticed that he had logged into an onion address that just didn&#8217;t look right after clicking the link from our clearnet abuse page on <a href="http://sigaint.org" target="_blank">sigaint.org</a>.</p>
<p>This got our attention so we started scanning our abuse page from every single Tor exit node. We found 58 of them and reported them to the Tor Project privately using PGP. (We didn&#8217;t want to alert the attacker, and we wanted the results we were seeing to be reproducible on their end.)</p>
<p>A member of the Tor Project wrote a plugin for the scanner they use and found even more exits. Some of them had literally just started the attack hours after we reported the first 58. We ended up with a total count of 71 bad Tor exit nodes. They have all since been blocked. The search for more of them continues.</p>
<p>Our users were alerted as soon as we had confirmation that the nodes were on the BadExit list. Any one who had been using our abuse page to find the darknet onion URL was advised to change their password immediately.</p>
<p>We think it could be a government that one or more of our users have angered in the past. The time line above could suggest this. Of course, there is no way for us to be sure and this is just speculation.</p>
<p>In hindsight, we figure because they couldn&#8217;t just break in and spy they resorted to running 71 bad Tor exit nodes to alter the abuse page on <a href="http://sigaint.org" target="_blank">sigaint.org</a>.</p>
<p><strong> Explanation of the attack:</strong></p>
<p>SIGAINT lives inside of the darknet. This means that the entire service is hosted on &#8220;<strong>sigaintevyh2rzvw.onion</strong>&#8220;.</p>
<p>We do operate a custom mail exit so our users can email people who have a regular clearnet email address. Sometimes users generate complaints. In order to ensure that the SIGAINT admins handle the clearnet complaints in a timely fashion we have an abuse page on <a href="http://sigaint.org" target="_blank">sigaint.org</a>. The <a href="http://sigaint.org" target="_blank">sigaint.org</a> abuse page has a link to the onion address.</p>
<p>Initially <a href="http://sigaint.org" target="_blank">sigaint.org</a> was behind Cloudflare and had SSL capability, but as the months went by Cloudflare started loading captchas to those who were viewing the <a href="http://sigaint.org" target="_blank">sigaint.org</a> page from Tor. We started to get complaints mostly from people who use TAILS. We realized that people using TAILS without persistent storage (they can&#8217;t save bookmarks between reboots) were using the abuse page as a bootstrapping point to get at their email.</p>
<p>In response to the captcha complaints, we turned Cloudflare off. (We still use them for DNS, but that&#8217;s all.) This happened months ago. The attack we witnessed followed.</p>
<p>The attackers were altering the onion address on our clearnet abuse page. They were changing it to an onion address that they control. Initially, we thought it was to steal user credentials. Our support email history statistics told us that this simply wasn&#8217;t the case.</p>
<p>After more investigation we realized that it was a sophisticated Man-In-The-Middle (MITM) attack. The bad onion address would sit in the middle between the user and the real site. It would read their email as they typed it and harvest any new emails that came in.</p>
<p><strong>Why would they do this?</strong> A lot of darknet email doesn&#8217;t even leave the darknet anymore. Lots of users of SIGAINT email each other and other Tor-enabled mail services. There is no way to spy on email that doesn&#8217;t leave the darknet without spying on the mail service itself.</p>
<p>For now, we are still using the clearnet abuse page for testing so we have not changed it yet. We are debating either putting TLS on the page or removing the onion link all together. We will probably do the latter, and routinely patrol the page from each exit node looking for rewrite attacks.</p>
<p><strong>We still advocate that users keep browser bookmarks, or simply write the correct onion address on a piece of paper.<br/>
</strong></p>
<p>&#8220;<strong>sigaintevyh2rzvw.onion</strong>&#8220;.</p>

Updated: 2015-04-26

