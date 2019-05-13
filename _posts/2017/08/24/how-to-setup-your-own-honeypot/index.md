---
How To Setup Your Own Honeypot?
---
<article class="post-listing post-22141 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-honeypot tag-setup">
    
    <div class="post-inner">
    
    
    <p class="post-meta">
    
    <span>Posted by: <a href="https://www.deepdotweb.com/author/theinnocent/" title="">TheInnocent </a></span>
    
    
    <span>August 24, 2017</span>
    <span>in <a href="https://www.deepdotweb.com/category/articles/" rel="category tag">Articles</a>, <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a></span>
    
    <span><a href="https://www.deepdotweb.com/2017/08/24/how-to-setup-your-own-honeypot/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    
    <div class="entry">
    
    <p>A honeypot is a system designed to appear vulnerable to <a href="https://www.deepdotweb.com/2017/05/27/types-cyberattacks-hitting-dark-web-research-paper/">attackers</a>. The goal of a honeypot is to log all the attackers’ activities to study their behaviour, log their Ips, track their location, collect zero-days. The idea of “honeypot” is nothing but a server that offers any kind of services to the attacker, from SSH to telnet, showing several well known exploitable ports opened like 22, 23, 445, 135, 139 and so on. The server appears to have critical vulnerabilities but it actually rejects connections so it is not really exploitable. It could happen that a honeypot is really compromised but this would be the case of a bad configured honeypot and this argument goes beyond the scope of this article. Keep also in mind that your honeypot can be configured to emulate all possible systems from Apache servers to Windows XP machines, appearing to run all possible softwares and services. In this article we will start implementing a rudimental honeypot on your linux machine that logs all unwanted <a href="https://www.deepdotweb.com/2017/06/01/trends-cyberattacks-2016/">activities </a>performed against your personal computer, to finally create different kinds of honeypot servers with complicated configurations to catch hackers all over the internet. Dealing with such configurations would be a pain for most of us, so we’ll find a workaround to pre-install default configurations.</p>
    <p><img class="wp-image-22145 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-16.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-16.png 460w, https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-16-300x76.png 300w" sizes="(max-width: 460px) 100vw, 460px" /></p>
    <h2>Pentbox: Your Personal Honeypot</h2>
    <p>Pentbox is a little piece of software that allows you to open a port on your host and listen for incoming connections (eventually refused) from outside.</p>
    <p>1 &#8211; Download Pentbox:</p>
    <p>wget <a href="http://downloads.sourceforge.net/project/pentbox18realised/pentbox-1.8.tar.gz">http://downloads.sourceforge.net/project/pentbox18realised/pentbox-1.8.tar.gz</a></p>
    <p>2 – Unpack</p>
    <p>tar -zxvf pentbox-1.8.tar.gz</p>
    <p>3 – Move to the Pentbox’s directory</p>
    <p>cd pentbox-1.8/</p>
    <p>4 – Run Pentbox</p>
    <p>./pentbox.rb</p>
    <p>Now you should see an introductive message like this:</p>
    <p><img class="wp-image-22146 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-17.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-17.png 755w, https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-17-300x219.png 300w" sizes="(max-width: 755px) 100vw, 755px" /></p>
    <p>Select 2, then you’ll see the subsequent menu:</p>
    <p><img class="wp-image-22147 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-18.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-18.png 917w, https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-18-300x178.png 300w" sizes="(max-width: 917px) 100vw, 917px" /></p>
    <p>Select 3 and fast auto configuration:</p>
    <p><img class="wp-image-22148 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-19.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-19.png 925w, https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-19-300x71.png 300w" sizes="(max-width: 925px) 100vw, 925px" /></p>
    <p>Then you’ll see “honeypot activated on port 80”. Just open your browser, connect to your VM’s IP and you’ll see an “access denied message”, while in your Pentbox terminal you’ll see the attack has been logged successfully! You can also choose to open different ports, in this case select the manual configuration and enable port forwarding on your router to make the external connections to those ports redirected to your honeypot.</p>
    <h2>HoneyDrive: The Honeypot Paradise</h2>
    <p>HoneyDrive is the honeypot paradise. HoneyDrive is a linux distribution that comes with 15 different honeypots preconfigured for you and a set of more than 30 forensic tools. Exploring the world of honeypots you will see that a lot of varieties exist. Honeyd, Kippo and Dionaea are only few of them. To install and configure each of these servers would be a chaos and it would require a lifetime to you. HoneyDrive, starting from a Xubuntu Desktop 12.04.4, installs and configures all these honeypots for you so you only have to become familiar with them without worrying about messing arround with incomprehensible “.config” files. Nevertheless it is highly recommended that you become familiar with these kind of files and how they are built in order to better understand what you are really doing.</p>
    <p>1 – Download HoneyDrive <a href="https://sourceforge.net/projects/honeydrive/">here</a>.</p>
    <p>2 – Double click on the .ova file.</p>
    <p>3 – Now your VirtualBox (yes I suppose you have one) will start and will automatically install the new virtual machine with the pre-built guest additions.</p>
    <p>4 – Once the installation process is finished, you will have your HoneyDrive up and running ! The desktop should look like this:</p>
    <p><img class="wp-image-22149 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-20.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-20.png 1357w, https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-20-300x149.png 300w, https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-20-1024x509.png 1024w" sizes="(max-width: 1357px) 100vw, 1357px" /></p>
    <p>The interesting thing you should worry about is the readme file, a simple text file in which are saved the file paths and commands of the several honeypots installed; the portion for Kippo should look like this:</p>
    <p><img class="wp-image-22150 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-21.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-21.png 923w, https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-21-300x208.png 300w" sizes="(max-width: 923px) 100vw, 923px" /></p>
    <p>Before starting to play with our new honeypots, keep in mind that you should really spend some time to update your system to a new Xubuntu release.</p>
    <h2>Setting Up Kippo</h2>
    <p>You can find all the subsequent instructions in the readme file but I will enlighten the most important:</p>
    <p>1 – cd /honeydrive/kippo/</p>
    <p>2 &#8211; /honeydrive/kippo/start.sh</p>
    <p>3 – ifconfig (to find the ip of the virtual honeypot)</p>
    <p>4 – load this IP in your browser and you will see this page:</p>
    <p>Now that your server works correctly, you can enable port-forwarding navigating to your router page so that the incoming traffic is redirected to your honeypot. After that you can go to http://yourip/kippo-graph/ to watch some interesting graphics about password attempted by the attackers, usernames, IPs, and other awesome stuff. <img class="wp-image-22151 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-22.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-22.png 647w, https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-22-300x109.png 300w" sizes="(max-width: 647px) 100vw, 647px" /></p>
    <p><img class="wp-image-22152 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-23.png" width="785" height="310" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-23.png 1351w, https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-23-300x118.png 300w, https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-23-1024x404.png 1024w" sizes="(max-width: 785px) 100vw, 785px" /></p>
    <p><img class="wp-image-22153 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-24.png" width="845" height="349" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-24.png 1351w, https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-24-300x124.png 300w, https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-24-1024x423.png 1024w" sizes="(max-width: 845px) 100vw, 845px" /></p>
    <h2>Setting Up Dionaea</h2>
    <p>From the developers’ <a href="https://www.edgis-security.org/honeypot/dionaea/">site</a>:</p>
    <p><em>Dionaea “the Nepenthes successor” is a malware capturing honeypot initially developed under The Honeynet Project’s 2009 Google Summer of Code (GSoC). Dionaea aims to trap malware exploiting vulnerabilities exposed by services offered over a network, and ultimately obtain a copy of the malware.</em></p>
    <p><em>Dionaea features a modular architecture, embedding Python as its scripting language in order to emulate protocols. Much superior to its predecessor (Nepenthes), it is able to detect shellcodes using LibEmu and supports IPv6 and TLS.</em></p>
    <p>1) start Dionaea</p>
    <p>/opt/dionaea/bin/dionaea</p>
    <p>2) in another terminal</p>
    <p>cd /honeydrive/DionaeaFR/</p>
    <p>3) Tell Dionaea to collect data</p>
    <p>python manage.py collectstatic</p>
    <p>4) python manage.py runserver honeypotip:8000</p>
    <p>where honeypotip is the ip of your honeypot that you can find using ifconfig</p>
    <p>now go to your honeypotip:8000 in your browser and you will see this page:</p>
    <p><img class="wp-image-22154" src="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-25.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-25.png 1347w, https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-25-300x126.png 300w, https://www.deepdotweb.com/wp-content/uploads/2017/08/word-image-25-1024x430.png 1024w" sizes="(max-width: 1347px) 100vw, 1347px" /></p>
    <p>Dionaea has really awesome features: if you look at the panel, it will show you the IPs of the attackers, their location in the world, the services and ports attacked, the malwares uploaded and other interesting things.</p>
    <h2>Conclusions</h2>
    <p>Now that you have an idea of what a honeypot is and how to install one, try to take a look to the other honeypots developed in honeydrive, take some time to play with them and try to change the configurations’ files assigning to your servers different features, services and opened ports. Playing with honeypots can be very instructive but pay attention, cause it’s not actually a game.</p>
    
    
    </div><!-- .entry /-->
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/honeypot/" rel="tag">honeypot</a> <a href="https://www.deepdotweb.com/tag/setup/" rel="tag">setup</a></span>				<span style="display:none" class="updated">2017-08-24</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/theinnocent/" title="Posts by TheInnocent" rel="author">TheInnocent</a></strong></div>
    
    
    </div><!-- .post-inner -->
</article><!-- .post-listing -->

