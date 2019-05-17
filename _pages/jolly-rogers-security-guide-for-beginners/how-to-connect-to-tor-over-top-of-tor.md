---
layout: single
title: "HOW TO CONNECT TO TOR OVER TOP OF TOR"
sidebar:
  nav: "jolly"
permalink: "jolly-rogers-security-guide-for-beginners/how-to-connect-tor-over-top-of-tor/"
redirect_from: "jolly-rogers-security-guide-for-beginners/how-to-connect-tor-over-top-of-tor"
---


<p>Here is another fun tip that may or may not interest you, but I figured I would throw it in for you anyways.</p>
<p style="text-align: center;"><a href="/vpn-comparison-chart/">&gt;&gt;&gt;Attention: Use VPN with Tor! Click here to see the best VPN’s&lt;&lt;&lt;</a></p>
<p>I figured this out while trying to figure out an effective way to do a TOR -&gt; VPN connection. You can do TOR -&gt; TOR connection with Tails by using a program called <strong>Tortilla</strong>, thus adding another layer for your adversaries to crack. Whether or not this is worth it, is completely up to you, but I am sharing in case it is something you want to do. This however currently only works for those using Windows because it was designed to be used by Windows users. Please note as well that this will noticeably slow down your connection since you are going through TOR twice. Here is the official homepage of Tortilla.</p>
<p>https://github.com/CrowdStrike/Tortilla</p>
<p>And the official download page for the prebuilt standalone exe below. There is a link to it on the home page if you do not trust me.</p>
<p>http://www.crowdstrike.com/community-tools/</p>
<p>The way you do this is very simple actually. You need to first download <strong>TOR Expert Bundle</strong> from the TOR Project download page and install it on your computer or better yet your USB drive.</p>
<p>https://www.torproject.org/download/download.html.en</p>
<p>Next open the <strong>tor.exe</strong> and just let it run until it says <strong>Bootstrapped 100% Done</strong>. Next you want to run the tortilla.exe file and make sure you run it with Administrator privileges. Also, if you are running Windows Vista or later, you will likely get an error that this program does not have a valid certificate, because it is actually signed with something called a test-signed ceritifcate. In this case you need to allow test-signed drivers to run on your computer.</p>
<p>To do this, simply go to your Start Menu and type in the search box &#8220;command&#8221;. When command comes up, you right click it, and click run as Administrator and it will open up a command prompt. Next type in the following command. <strong>Bcdedit.exe -set TESTSIGNING ON</strong> and this will allow Windows to install test-signed drivers. Restart your computer and you will see in the bottom right hand corner after you restart <strong>Test Mode Windows</strong>. Now you can run Tortilla. And let it connect to TOR. Remember to have <strong>tor.exe</strong> from TOR Expert Bundle open first.</p>
<p>Finally, you open up Virtual Box or whatever Virtual Machine software you are using and click <strong>Settings</strong> on the Tails virtual machine. Click on the <strong>Network</strong> tab and change the drop down menu where it says <strong>Attached To</strong>: to <strong>Bridged Adapter</strong> and in the drop down menu below it called Name: Select Tortilla Adapter. Now your Virtual Machine, in this case Tails, will always connect to the internet <strong>through Tortilla</strong>, which connects through TOR. And since Tails establishes its own connection to TOR, you will be running TOR over top of TOR. Again, you may or may not want to do this, but I am giving you the option should you want to.</p>
<p>If anyone is interested in learning more about the creator of Tortilla, he did a PowerPoint presentation at the 2013 Black Hat USA conference. Feel free to watch his talk at the YouTube link below. Please note however that YouTube is owned by Google and there are only about 57 views on the video, so the government will likely correlate users who watch that video with users from this forum. Make sure you do not watch the video on YouTube with your real IP address. At the very least use a VPN or find another site that has it hosted. Always be extra paranoid.</p>

{% include video id="G_jDPQU-8YQ" provider="youtube" %}


Updated: 2014-02-12

