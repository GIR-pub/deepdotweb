---
title: "Veracrypt Tutorial: How To Encrypt A USB Drive?"
---

Posted by: DeepDotWeb 

<span>February 9, 2015</span>

<div class="elgg-output blog-post">
<p>A simple tutorial explaining how to install VeraCrypt &#8211; The tutorial was created and contributed by Ping (Blog: http://w363zoq3ylux5rf5.onion/blog/owner/ping).</p>
<p>Lets start &#8211; First, go to the link <a href="https://veracrypt.codeplex.com/releases/view/565079" rel="nofollow">here</a> and select the version you want to use and download it. Now open a terminal and go to the directory where you downloaded the file and extract it:</p>
<p><em>tar -xzvf veracrypt-1.0f.1-setup.tar.gz</em></p>
<p>(Note: Navigate to the folder where you saved the tar.gz file)</p>
<p>Next, run the following command to install Veracrypt: <em>sh veracrypt-1.0f.1-setup.tar.gz</em></p>
<p>Or double click on the file.</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/02/1.png">

<p>Now enter 1 and press enter and say yes to the user agreement, once finished you will should find Veracrypt in your menu &#8211; if not you may run it by entering veracrypt in the command line.</p>
<p>In the window that will appear click on the option &#8220;Create Volume&#8221;:</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/02/2.png">

<p>To the next image, select &#8220;Create a volume within a partition / drive &#8221; and click &#8220;Next&#8221;:</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/02/3.png">

<p>At this point we will select the first choice &#8220;Standard VeraCrypt volume&#8221;, to create a normal volume. So we click &#8220;Next&#8221;</p>
<p>(i will cover making a hidden volume in another tutorial.)</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/02/4.png">

<p>In the next step click on &#8220;Select Device&#8221;. In this part we will choose a USB device that you have plugged in to your computer. After that click on &#8220;Next&#8221;.</p>
<p>(Note: all the data on the USB will be destroyed so make sure you don&#8217;t have any information on it!)</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/02/5.png">

<p>Make sure &#8220;Never save history&#8221; is checked:</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/02/6.png">

<p>In this step we must choose the encryption algorithm and the hash algorithm. We can choose between AES, Serpent, Twofish etc. So, we can leave the default options and we click &#8220;Next&#8221;. For more info on algorithms and hash algorithm you may look at the documentation <a href="https://veracrypt.codeplex.com/documentation%20 " target="_blank">here</a>.</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/02/7.png">

    Next, it will ask you for the password, this should be between 40-60 characters long. I am not going to go into depth because you can easily find a lot of info about how to create strong passwords. So just enter your password and click next:</p>
<p><strong>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/02/8.png">

<p>Next, we will select our file system. We can leave the recommend option (Filesystem type: FAT) as it is readable in all major operating systems:</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/02/9.png">

<p>On the Volume Format screen, you’ll need to move your mouse around to generate some random data, i recommend doing that for about 30 seconds. While just moving your mouse is sufficient you could always use a Wacom tablet and draw a lot of dicks everywhere. Once you’ve generated enough random data, hit the Format button:</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/02/10.png">

<p>Now, it might take a while for the process to finish so please be patient:</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/02/11.png">

<p>When its done, you will see this screen letting you know that the volume creation has been successfully created:</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/02/12.png">

<p>Next, click Ok and exit the wizard. Now choose one of the slots and click &#8220;select drive&#8221; at the bottom and choose the USB you just formatted:</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/02/13.png">

<p>Next, click mount and type in your password as well and your veracrypt admin password. Once you have entered everything in you will see it in your file manager or double click on the volume:</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/02/14.png">


<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/02/15.png">

<p>That&#8217;s it! You have now encrypted a USB drive using Veracrypt. All you have to do now is wait for the feds to arrest you and see if it works!</p>
<p>This tutorial is listed in the <a href="/security-tutorials/">Security Tutorials</a> section.</p>
<p>&nbsp;</p>

Updated: 2015-02-09