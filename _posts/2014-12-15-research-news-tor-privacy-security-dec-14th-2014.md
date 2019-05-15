---
title: "Research &#038; News in Tor, Privacy, &#038; Security – Dec 15th, 2014"
---


Posted by: Kiell

<span>December 15, 2014</span>

<p>Tor Browser 4.0.2 has been <a href="https://blog.torproject.org/blog/tor-browser-402-released">released</a>. The new release fixes compiler bugs in Windows, ensures that cache entires are isolated by domain, and prevents user locale settings from being leaked by the Javascript engine.</p>
<p>Tor Browser 4.5-alpha-2 is now <a href="https://blog.torproject.org/blog/tor-browser-45-alpha-2-released">out</a>. This version includes improvements to Torbutton&#8217;s circuit visualization feature, and removes a custom fix to the POODLE vulnerability, implementing Mozilla&#8217;s fix.</p>
<p>Tails 1.2.1 has been <a href="https://blog.torproject.org/blog/tails-121-out">released</a>. The package contains routine updates to the Tor Browser (4.0.2) and Linux (3.16.7-1). Truecrypt has finally been disabled, and GnuPG is now configured in line with <a href="https://help.riseup.net/en/security/message-security/openpgp/best-practices">accepted best practices</a>.</p>
<p>George Kadianakis has updated his proposal to collect statistics about hidden services from Tor relays. The proposal suggests that collecting these statistics could help us understand hidden service usage across the network, such as how often these services are used and how much load they put on the network. He suggests collecting these statistics by adding some fields to a relay&#8217;s extra-info descriptor, and keeping track of a relay&#8217;s hidden service directory or rendezvous point activities. These extra-info descriptors would then be submitted to directory authorities every 24 hours.</p>
<p><em>This updated proposal was released through the tor-dev mailing list. You can view the original email</em> <a href="https://lists.torproject.org/pipermail/tor-dev/2014-December/007928.html"><em>here</em></a><em>.</em></p>
<p>David Fifield released a report outlining the costs incurred during November by infrastructure for the meek pluggable transport. The results showed a strong increase in the amount of users, with the amount of simultaneous users increasing from 247 to 750. A summary of all costs is as follows:</p>
<p>App Engine + Amazon + Azure = total by month<br />
    February 2014 $0.09 + &#8212; + &#8212; = $0.09<br />
    March 2014 $0.00 + &#8212; + &#8212; = $0.00<br />
    April 2014 $0.73 + &#8212; + &#8212; = $0.73<br />
    May 2014         $0.69 +      &#8212; +    &#8212; =   $0.69<br />
    June 2014        $0.65 +      &#8212; +    &#8212; =   $0.65<br />
    July 2014        $0.56 +   $0.00 +    &#8212; =   $0.56<br />
    August 2014      $1.56 +   $3.10 +    &#8212; =   $4.66<br />
    September 2014   $4.02 +   $4.59 + $0.00 =   $8.61<br />
    October 2014    $40.85 + $130.29 + $0.00 = $171.14<br />
    November 2014  $224.65 + $362.60 + $0.00 = $587.25<br />
    &#8212;<br />
    total by CDN   $273.80 + $500.58 + $0.00 = $774.38 grand total</p>
<p><em>This report was released through the tor-dev mailing list. You can view the original email</em> <a href="https://lists.torproject.org/pipermail/tor-dev/2014-December/007916.html"><em>here</em></a><em>.</em></p>
<p><em>&#8212;</em></p>
<p>Eleven United States senators, ten Democratic and one independent, have called for a review of policies governing use of IMSI-catchers, or “Stingray” devices. In a <a href="https://www.documentcloud.org/documents/1378358-249798493-tester-s-letter-to-attorney-general.html">letter</a> sent to Attorney General Eric Holder and Secretary of Homeland Security Jeh Johnson, the senators aim to clear up any ambiguity about use of the devices. The letter requests information regarding use of the devices, policies governing use of the devices, retention and use of any collected information, and cooperation between state and federal agencies.</p>
<p>The payment service CHARGE Anywhere <a href="https://www.chargeanywhere.com/notice/_defaultmerchant.aspx">announced</a> that they have uncovered an attack against their network. The company discovered the malware on September 22, 2014, and have been taking time to perform a full investigation. The malware targets information that is sent during a payment card authorization request, which may include a cardholder&#8217;s name, account number, expiration date, and card verification code. The company reports that, “the format and method of connection for certain outbound messages enabled the unauthorized person to capture and ultimately then gain access to plain text payment card transaction authorization requests.” Any cards used at relevant merchants between November 5, 2009 and September 24, 2014 may have been affected.</p>
<p>Researchers from Blue Coat Labs have <a href="https://www.bluecoat.com/security-blog/2014-12-09/blue-coat-exposes-">discovered</a> sophisticated malware that they believe was developed by a powerful adversary, possibly a well-resourced nation-state. The malware was first used against targets in Russia and other Eastern European countries, and later targeted “individuals in strategic positions: executives in important businesses such as oil, finance and engineering, military officers, embassy personnel and government officials.” The malware, which has been dubbed “Inception”, is delivered via emails containing infected attachments.</p>
<p>In all attacks observed by Blue Coat, malware components have been embedded in Rich Text Format (RTF) files. The malware exploits two known RTF vulnerabilities, CVE-2014-1761 and CVE-2012-0158. Command and control is done through a Swedish cloud hosting platform (CloudMe.com), and the attackers have also created a proxy network composed of home routers, mostly located in South Korea. Once a machine is infected, the malware collects information about the device, including OS version, computer name, user name, user group membership, the process it is running in, locale ID’s, and system drive and volume information. The attackers also target mobile platforms, including Android, BlackBerry, and iOS. This malware records incoming and outgoing calls, saving them to an mp4 file. This information is then encrypted and sent to cloud storage via the WebDAV protocol.</p>

Updated: 2014-12-15    
