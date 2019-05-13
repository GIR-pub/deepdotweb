---
Wireshark Tutorial
---
<article class="post-listing post-23615 post type-post status-publish format-standard has-post-thumbnail hentry  tag-tutorial tag-wireshark">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/theinnocent/" title="">TheInnocent </a></span>
    <span>November 21, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/11/21/wireshark-tutorial/#comments">3 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    <p>The following tutorial is intended as a brief introduction to the most famous packet sniffer in the world, Wireshark. The most complete guide you can find, is the <a href="https://www.wireshark.org/download/docs/user-guide-a4.pdf">user-guide-wireshark.pdf</a>, that counts 192 pages. Anyway if you don’t want to read all those pages, you can find few easier tutorials on the <a href="https://www.deepdotweb.com/2017/09/19/art-google-hacking/">web</a>. This is one of them, and it will guide you from the theoretical basis to a “hands-on” approach for the graphical interface.</p>
    <h2>Introduction</h2>
    <p>The data that you send and receive with your computer, are encapsulated following the ISO/OSI model or the TCP/IP architecture. In the following images you can see how the ISO/OSI model and the TCP/IP architecture are built and how they deal with each other.</p>
    <p><img class="wp-image-23618 aligncenter" src="/imgs/2017/11/word-image-22.png" srcset="/imgs/2017/11/word-image-22.png 390w, /imgs/2017/11/word-image-22-300x235.png 300w" sizes="(max-width: 390px) 100vw, 390px" /> <img class="wp-image-23619 aligncenter" src="/imgs/2017/11/word-image-23.png" srcset="/imgs/2017/11/word-image-23.png 463w, /imgs/2017/11/word-image-23-300x207.png 300w" sizes="(max-width: 463px) 100vw, 463px" /></p>
    <p>Starting from the application level, data are encapsulated through 7 different levels. Every level adds a header. Look at the following image; when it comes to transport level, we refer to data as “segments”, when it comes to network level we say “packets”, speaking of data-link level we say “frames” and referring to physical level, “bits”.</p>
    <p><img class="wp-image-23620 aligncenter" src="/imgs/2017/11/word-image-24.png" srcset="/imgs/2017/11/word-image-24.png 700w, /imgs/2017/11/word-image-24-300x116.png 300w" sizes="(max-width: 700px) 100vw, 700px" /></p>
    <p>Wireshark is a powerful (efficient) packet sniffer. Although we say <strong>packet</strong> sniffer, Wireshark captures <strong>frames </strong>at the data-link layer. Wireshark is passive. It does not send frames, nor it receives them. Wireshark receives a copy of all the frames exchanged between two machines, then, sniffing at the data-link level, it is able to read information at all the higher levels (network, transport, session, presentation, application), storing the data and displaying the various protocol fields and their content.</p>
    <p>Wireshark is essentially composed of two parts: the packet-capturing library that allows Wireshark to sniff the packets and the packet-analyzer that allows Wireshark to distinguish, for example, an HTTP POST method from an HTTP GET method.</p>
    <h2>A Simple Graphical Interface</h2>
    <p><img class="wp-image-23621 aligncenter" src="/imgs/2017/11/word-image-25.png" srcset="/imgs/2017/11/word-image-25.png 1074w, /imgs/2017/11/word-image-25-300x157.png 300w, /imgs/2017/11/word-image-25-1024x537.png 1024w" sizes="(max-width: 1074px) 100vw, 1074px" /></p>
    <p>The graphical interface of Wireshark shows the subsequent parts:</p>
    <ul>
    <li>command menus</li>
    <li>packet display filter field</li>
    <li>packet-listing window</li>
    <li>packet-header details window</li>
    <li>packet-contents window</li>
    </ul>
    <p><strong>Command Menus</strong></p>
    <ul>
    <li>The File Menu allows us to import capture files, export them, save the capture and exit from Wireshark.</li>
    <li>The Edit Menu helps us to search a particular packet between the multitude of the packets captured.</li>
    <li>The Capture Menu permits us to start or stop a capture and to refine the capture options. It also presents a list of preconfigured research filters.</li>
    <li>The Analyze Menu shows other filters’ options.</li>
    </ul>
    <p><strong>The Packet Display Filter Field</strong></p>
    <p>Here you can enter a word (e.g. a protocol name) to hide all the packets that do not present that name.</p>
    <p><strong>The Packet-Listing Window</strong></p>
    <p>Here we can see a list of all the captured packets. Please note that the packet number is assigned by Wireshark for reasons of clarity and readability but it has nothing to do with the packet itself. In this list, you can also find the source and destination address, the time at which the packet was captured and the protocol type.</p>
    <p><strong>The Packet-Header Details Window </strong></p>
    <p>The genre of details that you can find here, include the details about the source or the ultimate destination of the packet selected, Ethernet and IP-layer details and so on.</p>
    <p><strong>The Packet-Contents Window</strong></p>
    <p>Displays the content of the selected packet in both hexadecimal and ASCII.</p>
    <h2>The Installation Process</h2>
    <p>Note that the non-root users won’t automatically have the permission to perform captures. To solve this problem please read the readme document (/usr/share/doc/wireshark-common/README.Debian) that says:</p>
    <p><em>“Only root user will be able to capture packets. It is advised to capture</em></p>
    <p><em>packets with the bundled dumpcap program as root and then run</em></p>
    <p><em>Wireshark/Tshark as an ordinary user to analyze the captured logs. This is the default on Debian systems.”</em></p>
    <p>Another possibility is to use Wireshark to both capture and analyze the packets, in this case the root user has to add the guest users to the Wireshark group in order to make them be able to capture.</p>
    <h2>Navigation Keystrokes</h2>
    <p>All the possible actions in Wireshark, can be performed through the usage of the keyboard. The following is a list of all the fundamental keystrokes that you can use to move through a capture file.</p>
    <p><img class="wp-image-23624 aligncenter" src="/imgs/2017/11/word-image-28.png" srcset="/imgs/2017/11/word-image-28.png 871w, /imgs/2017/11/word-image-28-300x186.png 300w" sizes="(max-width: 871px) 100vw, 871px" /></p>
    <h2>A Capturing Test</h2>
    <p>To perform a capturing test, simply open your favourite browser. Then you can start Wireshark and you will see the main window where still no packet information is present. Go to “interfaces” and select you favourite one. Wireshark can use a great variety of different interfaces. Under Linux:</p>
    <ul>
    <li>&#8220;any&#8221; : virtual interface, captures from all available (even hidden!) interfaces at once</li>
    <li>&#8220;lo&#8221;: virtual loopback interface</li>
    <li>&#8220;eth0&#8221;, &#8220;eth1&#8221;, &#8230;: Ethernet interfaces</li>
    <li>&#8220;ppp0&#8221;, &#8220;ppp1&#8221;, &#8230;: PPP interfaces</li>
    <li>&#8220;wlan0&#8221;, &#8220;wlan1&#8221;, &#8230;: Wireless LAN</li>
    <li>&#8220;team0&#8221;, &#8220;bond0&#8221;: Combined interfaces (i.e. NIC teaming or bonding)</li>
    <li>&#8220;br0&#8221;, &#8220;br1&#8221;, &#8230;: Bridged Ethernet</li>
    <li>&#8220;tunl0&#8221;, &#8220;tunl1&#8221;: IP in IP tunneling</li>
    <li>&#8220;gre0&#8221;, &#8220;gre1&#8221;: GRE tunneling (Cisco)</li>
    <li>&#8220;ipsec0&#8221;, &#8220;ipsec1&#8221;: IPsec (VPN)</li>
    <li>&#8220;nas0&#8221;, &#8220;nas1&#8221;: ATM bridging as in RFC 2684 (used e.g. for xDSL connections)</li>
    <li>&#8220;usb0&#8221;, &#8220;usb1&#8221;, &#8230;: USB interfaces</li>
    </ul>
    <p>To discover the supported interfaces for the other operating systems, you can consult the <a href="https://wiki.wireshark.org/CaptureSetup/NetworkInterfaces">Wireshark Wiki</a>. Note that if you put your interface in monitor mode, you will be able to capture not only the copy of the packets sent to you and from you but also the copy of all the packets that travel in your <a href="https://www.deepdotweb.com/2017/08/14/report-calls-sec-vulnerable-computer-network-systems/">network</a> ! Keep attention in this case, because the .pcap file could rapidly become very heavy.</p>
    <p>Once you have selected the capture interface, click start and the capturing process will begin for the selected interface. While you surf the web, you will see the list of all the packets and once you will be satisfied, thus once you’ll think you have enough packets, you can stop the capturing process. Now go to the File Menu and click on “save as”. You can save the captured packets in several formats, the following is a list of the supported formats from the <a href="https://www.wireshark.org/docs/">Wireshark’s site</a>:</p>
    <ul>
    <li>pcapng (*.pcapng). A flexible, etensible successor to the libpcap format. Wireshark 1.8 and later save files as pcapng by default. Versions prior to 1.8 used libpcap.</li>
    <li>libpcap, tcpdump and various other tools using tcpdump’s capture format (*.pcap,*.cap,*.dmp)</li>
    <li>Accellent 5Views (*.5vw)</li>
    <li>HP-UX’s nettl (*.TRC0,*.TRC1)</li>
    <li>Microsoft Network Monitor &#8211; NetMon (*.cap)</li>
    <li>Network Associates Sniffer &#8211; DOS (*.cap,*.enc,*.trc,*fdc,*.syc)</li>
    <li>Network Associates Sniffer &#8211; Windows (*.cap)</li>
    <li>Network Instruments Observer version 9 (*.bfr)</li>
    <li>Novell LANalyzer (*.tr1)</li>
    <li>Oracle (previously Sun) snoop (*.snoop,*.cap)</li>
    <li>Visual Networks Visual UpTime traffic (*.*)</li>
    </ul>
    <p>The final part is the analysis of the captured packets. To perform a good analysis, you must have solid a <a href="https://www.deepdotweb.com/2017/01/18/wireless-hacking-1/">networking</a> base but this argument is not object of this tutorial that only explains how to use Wireshark to capture juicy information. For further study:</p>
    <ul>
    <li><a href="https://wiki.wireshark.org/">Wireshark’s Wiki</a></li>
    <li><a href="https://www.wireshark.org/download/docs/user-guide-a4.pdf">User’s Guide</a></li>
    </ul>
    </div>
    <a href="https://www.deepdotweb.com/tag/tutorial/" rel="tag">tutorial</a> <a href="https://www.deepdotweb.com/tag/wireshark/" rel="tag">wireshark</a></span> <span style="display:none" class="updated">2017-11-21</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/theinnocent/" title="Posts by TheInnocent" rel="author">TheInnocent</a></strong></div>
    </div>
</article>

