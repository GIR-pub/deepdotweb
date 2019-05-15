---
title: "Tutorial: XMPP/Jabber OTr"
---

Posted by: Dave 

<span>May 17, 2015</span>
    

<p>Hey guys. Dave here again, back to teach you how to chat safely and securely via the XMPP/Jabber messaging protocol. This tutorial will be done on Windows 7, but the same idea should be transferred across Linux distros and Mac OSX.</p>
<p>The first thing you are going to want to download the XMPP client called Pidgin. This can be downloaded <a href="https://www.pidgin.im/download/" target="_blank">here</a>. Once it is downloaded, go ahead with the install to completion.</p>

<img src="/imgs/2015/02/zIUEdL61.png">

<p>Once it is installed, start up Pidgin. You will be presented with two different Windows. Ignore them for now. We have to first go grab the software that will allow us to chat securely. It is called OTR, which stands for Off-the-Record messaging, and can be downloaded <a href="https://otr.cypherpunks.ca/" target="_blank">here</a>.</p>
<p>Download and install it. Make sure that the Pidgin application is closed out from your screen and taskbar before installing OTR.</p>

<img src="/imgs/2015/02/IJnP5Ue1.png">

<p>Great. OTR and Pidgin are now installed! No more downloads from here out in the tutorial, just a few simple configurations to Pidgin. The first thing we need to do is make the OTR plugin active in Pidgin. Do this by opening Pidgin, going to the &#8220;Tools&#8221; drop down, selecting &#8220;Plugins&#8221;, and clicking on the checkbox next to &#8220;Off-the-Record Messaging&#8221;.</p>

<img src="/imgs/2015/02/XBmu7GP1.png">

<p>Once we are done with that, we can enter our XMPP account details and start chatting, or make a new account if you do not have one. If you need a list of free XMPP service providers, you can get one at <a href="https://list.jabber.at/" target="_blank">this</a> link.</p>
<p>For the example, I will make a new account with the <a href="https://wtfismyip.com/jabber/" target="_blank">wtfismyip.com</a> service. You can register through the client, like I will show you how to do, or you can register online from <a href="https://wtfismyip.com/jabber/register" target="_blank">this</a> link.</p>
<p>The first step to register from the client will be to enter the username, password, and domain. The username and password will be your choosing, but the domain will be &#8220;<a href="http://wtfismyip.com" target="_blank">wtfismyip.com</a>&#8221; without the quotation marks. The &#8220;Resource&#8221; box should be left blank. Next, check the &#8220;Create this new account on the server&#8221; box at the bottom of the screen. It should look something like this.</p>

<img src="/imgs/2015/02/Iu9NwdR1.png">

<p>The next steps, to take one more step to be even more secure, will to set Tor as a SOCKS5 proxy, so that not only are the messages encrypted with OTR, but the traffic is encrypted with Tor. To do that, click on the &#8220;Proxy&#8221; tab, and set your &#8220;Host&#8221; and &#8220;Port&#8221; accordingly. Make sure that Tor is running as well, or you will get connection errors!</p>
<p>
<p>Once this is done, click on the &#8220;Add&#8221; button, go back to the &#8220;Buddy List&#8221;, click on the &#8220;Accounts&#8221; drop down, click on &#8220;Manage Accounts&#8221;, and finally click the checkbox next to your account. This will send the request to the server, and ask you to confirm your new account.</p>

<img src="/imgs/2015/02/pxs6Ocx1.png">

<p>If you get an error that pops up, don&#8217;t be worried. Sometimes, there is an error with the server, and you will have to register online. This has happened to me several times, and is normal. Just register on the website of the XMPP host you are using.</p>
<p>Once you have done all of this, you need to add your buddy and get in a chat with him or her. I will be using a fake account for this example, but the same actions transfer over to when you chat with a real account. All you need to do is click on the &#8220;OTR&#8221; button in the chat room, and click &#8220;Start a Private Conversation&#8221;. Wait a few seconds, and just like that, you are chatting securely via XMPP.</p>

<img src="/imgs/2015/02/snKrfky1.png">

<p>I hope this tutorial has been helpful, and as always, if you have any questions or problems, feel free to post a comment, and I will do my best to help. Thank you so much.</p>

Updated: 2015-05-17

