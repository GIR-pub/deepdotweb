---
title: "TOR CHAT"
---
4090


<p>By now if you have been following this thread, you should know that any type of messaging system is likely compromised or storing your data for an unknown period of time, and if you ever become a person of interest can be looked back upon for 5+ years.</p>
<p>This means things like Gmail, Hotmail, Yahoo Mail, Skype Messaging, Facebook Instant/Private Message, Text Messages, and other forms of communication are all likely being monitored to some degree, at the very least logging the meta data. But you should always treat everything as if those who are monitoring it can read the content of the email as well.</p>
<p>We have talked about communicating with PGP, we have talked about using TOR and hidden services, and we have talked about good practices of OpSec. But some of us want to be able to instant message somebody else. The good news is, you can do this with something called <strong>TorChat</strong>.</p>
<p>TorChat is a decentralized anonymous instant messenger that uses Tor hidden services as its underlying Network, in other words it communicates over the Tor network through the .onion URL protocol. This provides <strong>end to end encryption</strong> that we talked about in previous posts. It provides cryptographically secure text messaging and file transfers for business dealings, and confidential communication between two people. The best news, is that you can use TorChat on your Windows, Linux and your smart phones. A French developer released a version for MAC users, but it still in beta and should be used at your own risk. You can get TorChat for the iPhone in the Apple store, you can get TorChat in the Android Market as well, so you can even use it as a means of text messaging somebody else who also has TorChat.</p>
<p>In TorChat, every user has a unique alphanumeric ID consisting of 16 characters. This ID will be randomly created by Tor when the client is started the first time, it is basically the .onion address of a hidden service. TorChat clients communicate with each other by using Tor to contact the other&#8217;s hidden service. For example, the first time you open TorChat your computer might generate <strong>d0dj309jfj94jfgf.onion</strong> and from here on out, <strong>d0dj309jfj94jfgf</strong> will be your TorChat ID that you give out to people that you want to be able to message you. Here is the home page of TorChat.</p>
<p><strong>https://github.com/prof7bit/TorChat</strong><br/>
<strong>http://www.sourcemac.com/?page=torchat</strong> &#8211; MAC users</p>
<p>Unfortunately at this time, TorChat does not run properly in Tails, so you will either need to run it on your Windows, Linux or MAC system. It is pretty straight forward, download it, unpack it and run it and everything else should happen automatically for you. Once the avatar beside your TorChat ID turns green, you are online and same with your contacts. You can add contains by right clicking and choosing Add Contact and just enter their TorChat ID.</p>
<p>At this time there is some people debate as to whether or not TorChat is completely safe, and I would say that TorChat is about as safe as Tor is, just make sure you practice the same good practices you are used to. Do not give out personal information, if you are sending sensitive information use PGP encryption and so forth.</p>
<p>Here is another article on how TorChat works going into a little bit more detail. You can access it over the onion network.</p>
<p><strong>http://kpvz7ki2v5agwt35.onion/wiki/index.php/Hacking_TorChat</strong></p>
<p><strong>UPDATE</strong><br/>
Another user had some additional input that I overlooked when writing this post that you should be aware of.</p>
<div>
<div><a href="http://thehub7dnl5nmcz5.onion/index.php?topic=14555.msg327104#msg327104">Quote from: ldopa on January 13, 2014, 08:43:25 am</a></div>
</div>
<blockquote><p>
Torchat&#8217;s security is unknown. It has not undergone a proper security audit, professional or otherwise, that I know of. It creates a hidden service on your computer leaving you vulnerable to deanonymization attacks that apply to all hidden services. It also seems to be a very basic protocol that looks like netcat over Tor. There is no way to decline a file transfer. It automatically starts the transfer, writing the file to /tmp which is a RAM-mounted tmpfs on Linux. Then you are supposed to save the file somewhere. Theoretically an attacker could transfer /dev/urandom while you are away from your computer until it fills up your RAM and crashes your computer. This would be great for inducing intersection attacks. Not sure though. If the kernel is managing the system correctly, it may just stop the transfer when you run out of RAM.</p>
<p>Another thing is that once someone learns your Torchat ID there is no way to prevent them from knowing you are online, even if you remove them from your buddy list. The reason is because your Torchat instance is a hidden service that publishes a normal hidden service descriptor which anyone can download. There&#8217;s no way to stop that. If you want to cut off contact with someone, you have to get a new Torchat ID. <strong>So you should be very conservative about handing out your Torchat ID and only give it to extremely trusted</strong> associates.</p></blockquote>

Updated: 2014-02-13

