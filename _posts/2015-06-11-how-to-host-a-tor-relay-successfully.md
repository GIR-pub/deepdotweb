---
title: "How to Host a Tor Relay Successfully?"
---


Posted by: Dave 

<span>June 11, 2015</span>
    

<p>Hello everyone. My name is Dave, and today I will be teaching you on how to successfully host your own Tor relay on a Ubuntu 14.04 x64 VPS. The general method should be the same across most major Linux distros as well.</p>
<p>I have noticed a distinct lack of simple and clear tutorials on how to do this, so I am hoping that this will be the first mainstream one available.</p>
<p>The first thing you are going to want to do is run &#8220;sudo apt-get update &amp;&amp; sudo apt-get upgrade&#8221; and accept all of the updates to the packages. This just makes sure we have the most up to date software for your systems security.</p>

<img src="https://info-gir.github.io/deepdotweb/imgs/2015/02/2LWOauG1.png">

<p>After this is completed, you are going to want to edit the /etc/apt/sources.list with your favourite editor, and add the following lines.</p>
deb http://deb.torproject.org/torproject.org trusty main
    deb-src http://deb.torproject.org/torproject.org trusty main</textarea></div>

<p>
    After you have added those two lines into the sources list, copy, paste, and run the following two lines separately as two different commands. It&#8217;s very important that you copy and paste each line correctly.</p>
gpg --keyserver keys.gnupg.net --recv 886DDD89
    gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -</textarea></div>

<p>
    Once you have ran those two commands, run one more apt-get update &amp;&amp; apt-get upgrade command, and then finally, we are ready to install the latest stable version of Tor!</p>
sudo apt-get update &amp;amp;&amp;amp; sudo apt-get upgrade
    apt-get install tor deb.torproject.org-keyring</textarea></div>

<p>
    Tor is now installed, and we are ready to get down and dirty with configuring and starting your Tor node. Make sure that Tor is not running before we begin to make any changes to the torrc file, or the changes will not take place. To do this, make sure you run the following command.</p>
sudo service tor stop</textarea></div>

<p>
    Once that is done, we can use our favourite editor to edit the magic file known as &#8220;torrc&#8221;, located in the /etc/tor/ folder on our VPS. This file contains all of the options to run Tor as a hidden service, as a bridge, and for today&#8217;s tutorial, a Tor relay.</p>
<p>We want to scroll down in this file until we see the information stating that the section is just for Tor relays. It will look something like this.</p>

<img src="https://info-gir.github.io/deepdotweb/imgs/2015/02/4kdKUk11.png">

<p>It is also worth noting that I will be going down the list of configuration options out of order, since some of the options are not really needed for this tutorial.</p>
<p>The picture is just the first few settings in the options for our Tor relay, but don&#8217;t get overwhelmed. It&#8217;s really simple when you take your time and read through it.</p>
<p>The first setting we will be dealing with is the &#8220;ORPort&#8221;. This is the port that will accept connections from clients so they can use the Tor network. It is a required option, and the default selection of 9001 is the optimal way to run it. Remove the octothorpe(that is the # sign) from the front of it to make it active. The rest of the options under it can be ignored, as they are used for specific configurations.</p>
<p><a href="httpd://www.deepdotweb.com/wp-content/uploads/2015/02/tJGTxF61.png">

<p>The second setting we will be dealing with is the &#8220;Nickname&#8221; setting. This is only a name for the relay you are making for you to keep track of it, and for other people to know who runs it. It can be anything you want.</p>

<img src="https://info-gir.github.io/deepdotweb/imgs/2015/02/4HMohZX1.png">

<p>The next two settings we will be relating to your bandwidth. These are very important to set correctly, otherwise you may end up in trouble with your hosting provider. Be sure you know your limits before setting up a Tor relay in the first place.</p>
<p>RelayBandwidthRate is the base line of how much bandwidth you want to allow people to use off of your relay. RelayBandwidthBurst is how much bandwidth you want to allow in one quick burst to and from a client. This does not cap the bandwidth you use outside of the Tor applications on your VPS. The default settings for both of these are usually fine. You can adjust them up or down as you need or want though.</p>

<img src="https://info-gir.github.io/deepdotweb/imgs/2015/02/4fdUtWp1.png">

<p>AccountingMax is the total amount of data you want to be sent in a given period of time. This could be 10 gigabytes of data in a 24 hour period, for example. AccountingStart is when that period of time starts for your relay. In the example below, I will set it so that only 10 gigabytes of data can be sent in a 24 hour period. Again, this can be set up or down to your wants or needs.</p>

<img src="https://info-gir.github.io/deepdotweb/imgs/2015/02/4CcGo5r1.png">

<p>The next setting is your contact information. This can be as simple as an email address, or as advanced as your PGP key, but using an email address is absolutely recommended to get you on the Tor mailing list. Usually, people put there email address, followed by their BitCoin address just in case someone wants to donate BitCoins to that relay, as shown in the example below.</p>

<img src="https://info-gir.github.io/deepdotweb/imgs/2015/02/PWHBTf01.png">

<p>The final option is an important option. It is the decision as to if you want to be an exit node or not. Being an exit node is important to the Tor network, as it is where encrypted Tor traffic gets into the internet. For more information, click <a href="http://hackertarget.com/tor-exit-node-visualization/">here</a>.</p>
<p>You don&#8217;t hurt the Tor network by not being an exit node at all, so it is no worry if you want do not want to be. Just uncomment the last ExitPolicy option I did in the picture. If you do want to be an exit node, leave all of them commented just like they are.</p>

<img src="https://info-gir.github.io/deepdotweb/imgs/2015/02/1unQhB51.png">

<p>Once you make sure everything is to your liking, start up Tor again with the command below, viola! You are running your own Tor relay, heloing users around the world have safer and more anonymous internet!</p>
sudo service tor start</textarea></div>

<p>
    A few things to keep in mind that are not really listed in any help file before we end the tutorial. One, is that your relay may not be listed for a few hours on sites like <a href="https://globe.torproject.org/">Globe</a> or <a href="https://atlas.torproject.org/">Atlas</a>. It takes a bit. Don&#8217;t go restarting your VPS or anything.</p>
<p>The second thing is that your bandwidth is going to be really screwy for awhile. It will jump up, it will go down to nothing, it will even out, and even sometimes go <b>COMPLETELY INSANE</b> like it did for me the first time I ran a Tor node. It&#8217;s entirely natural, and I recommend you take a look at <a href="https://blog.torproject.org/blog/lifecycle-of-a-new-relay">this</a> article for more reading on what to expect.</p>
<p>Another thing is that there is a community established that is ready to help you if you have any trouble at all. Stackexchange is a website dedicated to people who are having problems with a wide array of subjects, and Tor is one of them! It can be accessed at <a href="https://tor.stackexchange.com/">this</a> link, 24 hours a day, 7 days a week, 365 days a year.</p>
<p>The last thing I can think of is that logs are your friend. If there is anything going wrong with your relay, it will be located in the log files at /var/log/tor. Read them, find out where the problem is, and fix it. If you need some help, use the Stackexchange link above<br/>
    Well, this about covers the tutorial on how to host your own Tor relay. If you have any questions, feel free to ask them in the comments below.</p>
<p>Thank you all so much, and thank you for your interest in helping the Tor community.</p>
<p><strong>This tutorial is by Dave, who can be reached at tor@8chan.co</strong></p>

Updated: 2015-06-11

