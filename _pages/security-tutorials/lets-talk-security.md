---
title: "Let&#8217;s talk about security"
---


</div><span class="wpsr_floatbts_anchor" data-offset="25"></span><p>Post by: astor on August 14, 2013, 03:06 am<br/>
In the wake of the Freedom Hosting exploit, I think we should reevaluate our threat model and update our security to better protect ourselves against the real threats that we face. So I wrote this guide in order to spark a conversation. It is by no means comprehensive. I only focus on technical security. Perhaps others can address shipping and financial security. I welcome feedback and would like these ideas to be critiqued and expanded.</p>
<p>As I was thinking about writing this guide, I decided to take a step back and ask a basic question: what are our goals? I&#8217;ve come up with two basic goals that we want to achieve with our technical security.</p>
<p>1. Avoid being identified.<br/>
2. Minimize the damage when we are identified.</p>
<p>You can think of these as our _guiding security principles_. If you have a technical security question, you may be able to arrive at an answer by asking yourself these questions:</p>
<p>1. Does using this technology increase or decrease the chances that I will be identified?<br/>
2. Does using this technology increase or decrease the damage (eg, the evidence that can be used against me) when I am identified?</p>
<p>Obviously, you will need to understand the underlying technology to answer these questions.</p>
<p>The rest of this guide explains the broad technological features that decrease the chances we are identified and that minimize the damage when we are identified. Towards the end I list specific technologies and evaluate them based on these features.</p>
<p>First, let me list the broad features that I have come up with, then I will explain them.</p>
<p>1. Simplicity<br/>
2. Trustworthiness<br/>
3. Minimal execution of untrusted code<br/>
4. Isolation<br/>
5. Encryption</p>
<p>To some extent, we&#8217;ve been focusing on the wrong things. I&#8217;ve predominantly been concerned with network layer attacks, or &#8220;attacks on the Tor network&#8221;, but it seems clear to me now that application layer attacks are far more likely to identify us. The applications that we run over Tor are a much bigger attack surface than Tor itself. We can minimize our chances of being identified by securing the applications that we run over Tor. This observation informs the first four features that we desire.</p>
<p>===Simplicity===</p>
<p>Short of not using computers at all, we can minimize threats against us by simplifying the technological tools that we use. A smaller code base is less likely to have bugs, including deanonymizing vulnerabilities. A simpler application is less likely to behave in unexpected and unwanted ways.</p>
<p>As an example, when the Tor Project evaluated the traces left behind by the browser bundle, they found 4 traces on Debian Squeeze, which uses the Gnome 2 desktop environment, and 25 traces on Windows 7. It&#8217;s clear that Windows 7 is more complex and behaves in more unexpected ways than Gnome 2. Through its complexity alone, Windows 7 increases your attack surface, exposing  you to more potential threats. (Although there are other ways that Windows 7 makes you more vulnerable, too.) The traces left behind on Gnome 2 are easier to prevent than the traces left behind on Windows 7, so at least with regard to this specific threat, Gnome 2 is desirable over Windows 7.</p>
<p>So, when evaluating a new technological tool for simplicity, ask yourself these questions:</p>
<p>Is it more or less complex than the tool I&#8217;m currently using?<br/>
Does it perform more or fewer (unnecessary) functions than the tool I&#8217;m currently using?</p>
<p>===Trustworthiness===</p>
<p>We should favor technologies that are built by professionals or people with many years of experience rather than newbs. A glaring example of this is CryptoCat, which was developed by a well-intentioned hobbyist programmer, and has suffered severe criticism because of the many vulnerabilities that have been discovered.</p>
<p>We should favor technologies that are open source, have a large user base, and a long history of use, because they will be more thoroughly reviewed.</p>
<p>When evaluating a new technological tool for trustworthiness, ask yourself these questions:</p>
<p>Who wrote or built this tool?<br/>
How much experience do they have?<br/>
Is it open source, and how big is the community of users, reviewers, and contributors?</p>
<p>===Minimal Execution of Untrusted Code===</p>
<p>The first two features assume the code is trusted but has potential unwanted problems. This feature assumes that as part of our routine activities, we may have to run arbitrary untrusted code. This is code that we can&#8217;t evaluate in advance. The main place this happens is in the browser, through plug-ins and scripts.</p>
<p>You should completely avoid running untrusted code, if possible. Ask yourself these questions:</p>
<p>Are the features that it provides absolutely necessary?<br/>
Are there alternatives that provide these features without requiring plug-ins or scripts?</p>
<p>===Isolation===</p>
<p>Isolation is the separation of technological components with barriers. It minimizes the damage incurred by exploits, so if one component is exploited, other components are still protected. It may be your last line of defense against application layer exploits.</p>
<p>The two types of isolation are physical (or hardware based) and virtual (or software based). Physical isolation is more secure than virtual isolation, because software based barriers can themselves be exploited by malicious code. We should prefer physical isolation over virtual isolation over no isolation.</p>
<p>When evaluating virtual isolation tools, ask yourself the same questions about simplicity and trustworthiness. Does this virtualization technology perform unnecessary functions (like providing a shared clipboard)? How long has it been in development, and how thoroughly has it been reviewed? How many exploits have been found?</p>
<p>===Encryption==</p>
<p>Encryption is one of two defenses we have to minimize the damage when we are identified. The more encryption you use, the better off you are. In an ideal world, all of your storage media would be encrypted, along with every email and PM that you send. The reason for this is because, when some emails are encrypted but others are not, an attacker can easily identify the interesting emails. He can learn who the interesting parties are that you communicate with because those will be the ones you send encrypted emails to (this is called metadata leakage). Interesting messages are lost in the noise when everything is encrypted.</p>
<p>The same goes for storage media encryption. If you store an encrypted file on an unencrypted hard drive, an adversary can trivially determine that all the good stuff is in that small file. But when you use full disk encryption, you have more plausible deniability as to whether the drive contains data that would be interesting to that adversary, because there are more reasons to encrypt an entire hard drive than a single file. Also, an adversary who bypasses your encryption would have to cull through more data to find the the stuff that is interesting to him.</p>
<p>Unfortunately, using encryption incurs a cost that the vast majority of people can&#8217;t bare, so at a minimum, sensitive information should be encrypted.</p>
<p>On a related note, the other defense against damage is secure data erasure, but that takes time that you may not have. Encryption is preemptive secure data erasure. It&#8217;s easier to destroy encrypted data, because you only have to destroy the encryption key to prevent an adversary from accessing the data.</p>
<p>Finally, I&#8217;d like to add a related non-technical feature.</p>
<p>===Safe Behavior===</p>
<p>In some cases, the technology we use is only as safe as our behavior. Encryption is useless if your password is &#8220;password&#8221;. Tor is useless if you tell someone your name. It may surprise you how little an adversary needs to know about you in order to uniquely identify you. Here are some basic rules to follow:</p>
<p>Don&#8217;t tell anyone your name. (obv)<br/>
Don&#8217;t describe your appearance, or the appearance of any major possessions (car, house, etc.).<br/>
Don&#8217;t describe your family and friends.<br/>
Don&#8217;t tell anyone your location beyond a broad geographical area.<br/>
Don&#8217;t tell people where you will be traveling in advance (this includes festivals!).<br/>
Don&#8217;t reveal specific times and places where you lived or visited in the past.<br/>
Don&#8217;t discuss specific arrests, detentions, discharges, etc.<br/>
Don&#8217;t talk about your school, job, military service, or any organizations with official memberships.<br/>
Don&#8217;t talk about hospital visits.</p>
<p>In general, don&#8217;t talk about anything that links you to an official record of your identity.</p>
<p>===A List of Somewhat Secure Setups for Silk Road Users===</p>
<p>I should begin by pointing out that the features outlined above are not equally important. Physical isolation is probably the most useful and can protect you even when you run complex and untrusted code. In each of the setups below, I assume a fully updated browser / TBB with scripts and plug-ins disabled. Also, the term &#8220;membership concealment&#8221; means that someone watching your internet connection doesn&#8217;t know you are using Tor. This is especially important for vendors. You can use bridges, but I&#8217;ve included extrajurisdictional VPNs as an added layer of security.</p>
<p>With that in mind, here is a descending list of secure setups for SR users.</p>
<p>Starting off, I present to you the most secure setup!</p>
<p>#1</p>
<p>A router with a VPN + an anonymizing middle box running Tor + a computer running Qubes OS.</p>
<p>Advantages: physical isolation of Tor from applications, virtual isolation of applications from each other, encryption as needed, membership concealment against local observers with VPN</p>
<p>Disadvantages: Qubes OS has a small user base and is not well tested, as far as I know.</p>
<p>#2</p>
<p>Anon middle box (or router with Tor) + Qubes OS</p>
<p>Advantages: physical isolation of Tor from applications, virtual isolation of applications from each other, encryption as needed</p>
<p>Disadvantages: Qubes OS has a small user base and is not well tested, no membership concealment</p>
<p>#3</p>
<p>VPN router + anon middle box + Linux OS</p>
<p>Advantages: physical isolation of Tor from applications, full disk encryption, well tested code base if it&#8217;s a major distro like Ubuntu or Debian</p>
<p>Disadvantages: no virtual isolation of applications from each other</p>
<p>#4</p>
<p>Anon middle box (or router with Tor) + Linux OS</p>
<p>Advantages: physical isolation of Tor from applications, full disk encryption, well tested code base</p>
<p>Disadvantages: no virtual isolation of applications from each other, no membership concealment</p>
<p>#5</p>
<p>Qubes OS by itself.</p>
<p>Advantages: virtual isolation of Tor from applications, virtual isolation of applications from each other, encryption as needed, membership concealment (possible? VPN may be run in VM)</p>
<p>Disadvantages: no physical isolation, not well tested</p>
<p>#6</p>
<p>Whonix on Linux host.</p>
<p>Advantages: virtual isolation of Tor from applications, full disk encryption (possible), membership concealment (possible, VPN can be run on host)</p>
<p>Disadvantages: no physical isolation, no virtual isolation of applications from each other, not well tested</p>
<p>#7</p>
<p>Tails</p>
<p>Advantages: encryption and leaves no trace behind, system level exploits are erased after reboot, relatively well tested</p>
<p>Disadvantages: no physical isolation, no virtual isolation, no membership concealment, no persistent entry guards! (but can manually set bridges)</p>
<p>#8</p>
<p>Whonix on Windows host.</p>
<p>Advantages: virtual isolation, encryption (possible), membership concealment (possible)</p>
<p>Disadvantages: no physical isolation, no virtual isolation of applications from each other, not well tested, VMs are exposed to Windows malware!</p>
<p>#9</p>
<p>Linux OS</p>
<p>Advantages: full disk encryption (possible), membership concealment (possible)</p>
<p>Disadvantages: no physical isolation, no virtual isolation</p>
<p>#10</p>
<p>Windows OS</p>
<p>Advantages: full disk encryption (possible), membership concealment (possible)</p>
<p>Disadvantages: no physical isolation, no virtual isolation, the biggest target of malware and exploits!</p>
<p>Assuming there is general agreement about the order of this list, our goal is to configure our personal setups to be as high up on the list as possible.</p>
<p>Thanks for your attention, and again I welcome comments and criticism.</p>
<h3>Share and Enjoy</h3>




Updated: 2014-05-11


