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
<p><a href="/imgs/2015/02/1.png"><img class="aligncenter size-full wp-image-8997" src="/imgs/2015/02/1.png" alt="1" width="1187" height="692" srcset="/imgs/2015/02/1.png 1187w, /imgs/2015/02/1-300x175.png 300w, /imgs/2015/02/1-1024x597.png 1024w" sizes="(max-width: 1187px) 100vw, 1187px" /></a></p>
<p>Now enter 1 and press enter and say yes to the user agreement, once finished you will should find Veracrypt in your menu &#8211; if not you may run it by entering veracrypt in the command line.</p>
<p>In the window that will appear click on the option &#8220;Create Volume&#8221;:</p>
<p><a href="/imgs/2015/02/2.png"><img class="aligncenter size-full wp-image-8998" src="/imgs/2015/02/2.png" alt="2" width="612" height="553" srcset="/imgs/2015/02/2.png 612w, /imgs/2015/02/2-300x271.png 300w" sizes="(max-width: 612px) 100vw, 612px" /></a></p>
<p>To the next image, select &#8220;Create a volume within a partition / drive &#8221; and click &#8220;Next&#8221;:</p>
<p><a href="/imgs/2015/02/3.png"><img class="aligncenter size-full wp-image-8999" src="/imgs/2015/02/3.png" alt="3" width="747" height="445" srcset="/imgs/2015/02/3.png 747w, /imgs/2015/02/3-300x179.png 300w" sizes="(max-width: 747px) 100vw, 747px" /></a></p>
<p>At this point we will select the first choice &#8220;Standard VeraCrypt volume&#8221;, to create a normal volume. So we click &#8220;Next&#8221;</p>
<p>(i will cover making a hidden volume in another tutorial.)</p>
<p><a href="/imgs/2015/02/4.png"><img class="aligncenter size-full wp-image-9000" src="/imgs/2015/02/4.png" alt="4" width="745" height="447" srcset="/imgs/2015/02/4.png 745w, /imgs/2015/02/4-300x180.png 300w" sizes="(max-width: 745px) 100vw, 745px" /></a></p>
<p>In the next step click on &#8220;Select Device&#8221;. In this part we will choose a USB device that you have plugged in to your computer. After that click on &#8220;Next&#8221;.</p>
<p>(Note: all the data on the USB will be destroyed so make sure you don&#8217;t have any information on it!)</p>
<p><a href="/imgs/2015/02/5.png"><img class="aligncenter size-full wp-image-9001" src="/imgs/2015/02/5.png" alt="5" width="606" height="446" srcset="/imgs/2015/02/5.png 606w, /imgs/2015/02/5-300x221.png 300w" sizes="(max-width: 606px) 100vw, 606px" /></a></p>
<p>Make sure &#8220;Never save history&#8221; is checked:</p>
<p><a href="/imgs/2015/02/6.png"><img class="aligncenter size-full wp-image-9002" src="/imgs/2015/02/6.png" alt="6" width="740" height="436" srcset="/imgs/2015/02/6.png 740w, /imgs/2015/02/6-300x177.png 300w" sizes="(max-width: 740px) 100vw, 740px" /></a></p>
<p>In this step we must choose the encryption algorithm and the hash algorithm. We can choose between AES, Serpent, Twofish etc. So, we can leave the default options and we click &#8220;Next&#8221;. For more info on algorithms and hash algorithm you may look at the documentation <a href="https://veracrypt.codeplex.com/documentation%20 " target="_blank">here</a>.</p>
<p><a href="/imgs/2015/02/7.png"><img class="aligncenter size-full wp-image-9003" src="/imgs/2015/02/7.png" alt="7" width="746" height="448" srcset="/imgs/2015/02/7.png 746w, /imgs/2015/02/7-300x180.png 300w" sizes="(max-width: 746px) 100vw, 746px" /></a><br />
    Next, it will ask you for the password, this should be between 40-60 characters long. I am not going to go into depth because you can easily find a lot of info about how to create strong passwords. So just enter your password and click next:</p>
<p><strong><a href="/imgs/2015/02/8.png"><img class="aligncenter size-full wp-image-9004" src="/imgs/2015/02/8.png" alt="8" width="747" height="450" srcset="/imgs/2015/02/8.png 747w, /imgs/2015/02/8-300x181.png 300w" sizes="(max-width: 747px) 100vw, 747px" /></a></strong></p>
<p>Next, we will select our file system. We can leave the recommend option (Filesystem type: FAT) as it is readable in all major operating systems:</p>
<p><a href="/imgs/2015/02/9.png"><img class="aligncenter size-full wp-image-9005" src="/imgs/2015/02/9.png" alt="9" width="748" height="446" srcset="/imgs/2015/02/9.png 748w, /imgs/2015/02/9-300x179.png 300w" sizes="(max-width: 748px) 100vw, 748px" /></a></p>
<p>On the Volume Format screen, you’ll need to move your mouse around to generate some random data, i recommend doing that for about 30 seconds. While just moving your mouse is sufficient you could always use a Wacom tablet and draw a lot of dicks everywhere. Once you’ve generated enough random data, hit the Format button:</p>
<p><a href="/imgs/2015/02/10.png"><img class="aligncenter size-full wp-image-9006" src="/imgs/2015/02/10.png" alt="10" width="744" height="450" srcset="/imgs/2015/02/10.png 744w, /imgs/2015/02/10-300x181.png 300w" sizes="(max-width: 744px) 100vw, 744px" /></a></p>
<p>Now, it might take a while for the process to finish so please be patient:</p>
<p><a href="/imgs/2015/02/11.png"><img class="aligncenter size-full wp-image-9007" src="/imgs/2015/02/11.png" alt="11" width="743" height="447" srcset="/imgs/2015/02/11.png 743w, /imgs/2015/02/11-300x180.png 300w" sizes="(max-width: 743px) 100vw, 743px" /></a></p>
<p>When its done, you will see this screen letting you know that the volume creation has been successfully created:</p>
<p><a href="/imgs/2015/02/12.png"><img class="aligncenter size-full wp-image-9008" src="/imgs/2015/02/12.png" alt="12" width="748" height="450" srcset="/imgs/2015/02/12.png 748w, /imgs/2015/02/12-300x180.png 300w" sizes="(max-width: 748px) 100vw, 748px" /></a></p>
<p>Next, click Ok and exit the wizard. Now choose one of the slots and click &#8220;select drive&#8221; at the bottom and choose the USB you just formatted:</p>
<p><a href="/imgs/2015/02/13.png"><img class="aligncenter size-full wp-image-9009" src="/imgs/2015/02/13.png" alt="13" width="1220" height="555" srcset="/imgs/2015/02/13.png 1220w, /imgs/2015/02/13-300x136.png 300w, /imgs/2015/02/13-1024x466.png 1024w, /imgs/2015/02/13-272x125.png 272w" sizes="(max-width: 1220px) 100vw, 1220px" /></a></p>
<p>Next, click mount and type in your password as well and your veracrypt admin password. Once you have entered everything in you will see it in your file manager or double click on the volume:</p>
<p><a href="/imgs/2015/02/14.png"><img class="aligncenter size-full wp-image-9010" src="/imgs/2015/02/14.png" alt="14" width="608" height="555" srcset="/imgs/2015/02/14.png 608w, /imgs/2015/02/14-300x274.png 300w" sizes="(max-width: 608px) 100vw, 608px" /></a></p>
<p><a href="/imgs/2015/02/15.png"><img class="aligncenter  wp-image-9011" src="/imgs/2015/02/15.png" alt="15" width="754" height="407" srcset="/imgs/2015/02/15.png 1274w, /imgs/2015/02/15-300x162.png 300w, /imgs/2015/02/15-1024x553.png 1024w" sizes="(max-width: 754px) 100vw, 754px" /></a></p>
<p>That&#8217;s it! You have now encrypted a USB drive using Veracrypt. All you have to do now is wait for the feds to arrest you and see if it works!</p>
<p>This tutorial is listed in the <a href="http://www.deepdotweb.com/security-tutorials/">Security Tutorials</a> section.</p>
<p>&nbsp;</p>

Updated: 2015-02-09