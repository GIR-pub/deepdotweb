---
title: "Cantina Marketplace PWND: Admin Password was: &#8220;Password1&#8221; ?!"
---

Posted by: DeepDotWeb

<span>January 29, 2014</span>
    

<p><span style="color: #ff0000;"><strong>You are not going to believe the horror you are about to witness in this post &#8211; Proceed with caution!</strong></span></p>
<p><span style="text-decoration: underline;"><strong>Our thanks goes to</strong>: <strong><a href="http://www.reddit.com/user/sniok">sniok</a> , <a href="http://www.reddit.com/user/the_avid">The_avid, </a></strong> and everyone else who helped us prove to the users to avoid this miserable failure, while at the same time, keeping everyone amused!</span></p>
<p>It was just last week when we reported here about a market popping up with a design 100% similar to the biggest scam market that ever existed, the &#8220;Sheep Marketplace&#8221;. It is called <a href="https://gir.pub/deepdotweb/2014/01/20/sheep-marketplace-is-that-you-again-cantina-marketplace/">Cantina marketplace</a>. We got a few comments about this market and basically just wrote if off as another scam attempt from the same group the Sheep Marketplace. At the time, we had no idea that this market was about to become the biggest example ever to have every security hole imaginable, and built in a way that made <a href="https://gir.pub/deepdotweb/2014/01/27/the-drugslist-lesson-why-marketplace-security-should-not-be-taken-lightly/">Drugslist</a> (You remember the fiasco that was just couple of days ago, right?) look like the Fort Knox of the deep web marketplaces.</p>
<p>Once again, we will put the things into place in a form of a timeline. Since this party is still going, we will update later if needed:</p>
<p>1. It all started when the user <a href="http://www.reddit.com/user/Cantina_Marketplace">cantina_marketplce</a> started posting threads on Reddit announcing that a new marketplace was opened named Cantina. Now, lets ignore for a second the obvious question: How dumb are you to create a marketplace that looks exactly like Sheep Marketplace? On top of that, make it a normal escrow marketplace and focus on the fact that like most marketplaces, they started making claims about security that they couldn&#8217;t backup. Take for example: &#8220;being the safest marketplace out there ?!&#8221; &#8211; read the <a href="http://www.reddit.com/r/DarkNetMarkets/comments/1wbjzp/introducing_cantina_marketplace/" target="_blank">thread here</a></p>
<img src="https://gir.pub/deepdotweb/imgs/2014/01/cantin_intro.png" />

<p>2. I felt like I just had Déjà vu for the second time in just 2 days! When user called <a href="http://www.reddit.com/user/the_avid" target="_blank">the_avid</a> posted, and told Cantina not to make such claims about being secure unless they are going to back it up with some technical explanations:</p>
<img src="https://gir.pub/deepdotweb/imgs/2014/01/avid1.png" />

<p>3. Once again instead of explaining / admitting, the marketplace admin chooses to argue by posting a bold statement: <strong>&#8220;We have designed the site so it is completely safe from hackers and LE who may try various data extraction techniques to get sensitive data such as order information, user list, messages, etc.&#8221; </strong>Well said Cantina! Market owners should make a short search of the forums / Reddit before making the same dumb mistakes over and over again.</p>
<img src="https://gir.pub/deepdotweb/imgs/2014/01/cantina-secure.png" />

<p>4. Now this is where our story start to get interesting. In the background, a user named <b><a href="http://www.reddit.com/user/sniok">sniok</a></b> found a security hole on the site that lets you place orders without actually depositing any money into the site. This is what he told us: &#8220;The first security hole that i found was just absurd. Simply put negative quantity when ordering stuff and you &#8216;steal&#8217; money from vendor. Withdraws of that money didn&#8217;t come because all withdraw system was completely broken.&#8221; At a later point, he post this in this thread:</p>
<img src="https://gir.pub/deepdotweb/imgs/2014/01/makemoney.png" />

<p>I wanted to show a screenshot, but at this point, all listings were deleted from the market.</p>
<p>5. Then in another thread posted in Silk Road sub Reddit, another user found some SQL injection in the site code:</p>
<img src="https://gir.pub/deepdotweb/imgs/2014/01/not-worthy.png" />

<p>6. You would think that the <a href="https://gir.pub/deepdotweb/2014/01/27/the-drugslist-lesson-why-marketplace-security-should-not-be-taken-lightly/" target="_blank">Drugslist lesson</a> was learned, but nope. <strong>AGAIN, </strong>instead of taking responsibility and trying to fix the problem by contacting the user in private and asking for details, the owner offers a <strong>5BTC bounty</strong> to anyone who can find security vulnerabilities on the market. They make a bold statement that the marketplace is 100% secure and deny the SQLI injection problem:</p>
<img src="https://gir.pub/deepdotweb/imgs/2014/01/100secured.png" />

<p>7. From now on there is no clear timeline since everything happens around the same time. First, we received the following mail:</p>
<blockquote><p>You are wrong about Cantina (<strong>note: meaning our accusation that they are the same as Sheep)</strong>. The backend codebase is absolutely different.<br/>
    They just implemented fronted same as SMP. That kid thinks it could attract people somehow.</p>
<p>Anyway, I am applying for 5BTC bounty for pentesting Cantina. That site is absolutely amateur unsecure php-newbie project. I would bring you some exclusive report, when admin will reply and do his word about bounty.</p></blockquote>
<p>8. Five minutes later we find these unrelated posts from <a href="http://www.reddit.com/user/the_avid">The_avid</a> and <a href="http://www.reddit.com/user/sniok">sniok</a> on the same bounty thread<a href="http://www.reddit.com/user/sniok">:</a></p>
<img src="https://gir.pub/deepdotweb/imgs/2014/01/Hackers.png" />

    Now you would think that this is where the story ends, right? No.</p>
<p>I will make a long story short. The_avid starts dumping the Cantina marketplace DB. So do sniok and who knows how many more people at the time of the post. There were about 5 different threads on the Darknetmarket sub from people who hacked Cantina. All were claiming the 5BTC prize that they will probably never receive. I can only guess because the admin is hours away from shutting down the market (I also smell a doxx?). This is not before sniok posts that the passwords from the marketplace are in MD5 form, and the pin numbers are not encrypted at all. It was posted in this thread:</p>
<img src="https://gir.pub/deepdotweb/imgs/2014/01/password.png" />

<p>The last treat is brought to you by <b><a href="http://www.reddit.com/user/sniok">sniok</a></b> as he described how it went:</p>
<p>&#8220;I don&#8217;t really try that before because it is such basic security thing. Almost every form was able to be injected. In a couple minutes I had access to database. Passwords were stored in md5 hash. I tried to crack admin&#8217;s password with online md5 cracker and result was <strong>&#8220;Password1&#8221;</strong>. Very strong password :D I logged in admin control panel and there was nothing interesting. About 680 users and 60 vendors registered. Zero withdraws and a lot of empty wallets. Can&#8217;t open them though, system is completely broken.&#8221;</p>
<div>
<p>There are two admin accounts. 1 for market and 1 for control panel. Market- <strong>admin:Password1</strong> , Panel &#8211; <strong>admincantina:AAAaaa111</strong></p>
<p>Here is the site users list that was posted by the_avid: https://gist.github.com/anonymous/f9f58b21d370a5564f6d</p>
<p>Here is a screenshot of the admin inbox sniok provided to us while he was logged in as the admin user:</p>

<img src="https://gir.pub/deepdotweb/imgs/2014/01/cantina_admin.jpg"/>
<p>High Quality Screenshot &#8211; note the PM&#8217;s claiming the 5BTC bounty and the fact that known vendors are trying to get verified on this marketplace:</p>
<img src="https://gir.pub/deepdotweb/imgs/2014/01/admin2.png" />

<p>Cantina, you should thank them. They did you a favor. At least you were not hacked by LE.</p>
</div>

Updated: 2014-01-29
    
