---
A Bitcoin Framework For Sending Bitcoins Using Low-end Mobile Phones
---
<article class="post-listing post-18300 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-bitcoin tag-bitcoins tag-framework tag-lowend tag-mobile tag-phones tag-sending">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>February 23, 2017</span>
    <span>in <a href="https://www.deepdotweb.com/category/articles/" rel="category tag">Articles</a>, <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a></span>
    <span><a href="https://www.deepdotweb.com/2017/02/23/bitcoin-framework-sending-bitcoins-using-low-end-mobile-phones/#comments">1 Comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Bitcoin is a decentralized peer-to-peer (P2P) currency that was innovated to provide a payment system that omits the need for banks and third party intermediaries. In some parts of the developing world, bank fees can be unaffordable, especially in poor rural communities. Moreover, access to retail banking services can be limited in such areas, which can lead to imbalances in the costs and standards of living of people who don&#8217;t own bank accounts. Throughout the past few years, <a href="https://www.deepdotweb.com/2016/02/26/africas-frontier-economies-chomp-at-the-bitcoin/">many solutions were presented to use bitcoin in developing parts of the world</a>, including rural communities, to mitigate these problems.</p>
    <p>A group of researchers from University of Fort Hare, South Africa, designed <a href="http://researchspace.csir.co.za/dspace/bitstream/10204/8931/1/Dlamini3_2016.pdf">a bitcoin framework that works on low-end mobile phones</a>, but also functions on any other mobile phone, to serve people in rural African communities. The published paper included a mobile bitcoin wallet system that proved the efficacy of the proposed bitcoin payment framework, as well as use cases of the designed wallet. The results of the framework experiment included the ability to send bitcoin payments via a low-end mobile phone which proved that bitcoin can be an ideal supplement to the current payment system in rural areas. On the other hand, the paper also touched on a number of issues that can hurdle supplementing the financial system, with bitcoin, in developing territories including bitcoin&#8217;s volatility and the need to exchange bitcoin to fiat currency, in some instances, before the money can be actually spent.</p>
    <p><strong>The Architectural Design of the Bitcoin Payment Framework:</strong></p>
    <p>The below figure illustrates the design of the proposed <a href="https://www.deepdotweb.com/2016/01/19/how-bitcoin-could-revolutionize-the-payments-landscape-in-africa/">bitcoin payment framework for rural areas in developing African countries such as South Africa</a>.</p>
    <p><img class="wp-image-18315 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/02/btc-mobile-framework-png.png" alt="BTC mobile framework.PNG" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/02/btc-mobile-framework-png.png 556w, https://www.deepdotweb.com/wp-content/uploads/2017/02/btc-mobile-framework-png-300x247.png 300w" sizes="(max-width: 556px) 100vw, 556px"/></p>
    <p>The following represents the components of the framework:</p>
    <p>Low-end mobile phone: The user will send SMSs, using a low-end mobile phone, to a GSM modem connected to a computer. These SMSs will include commands to operate the system such as Help, Bal, Getwallet, Send and Addr. Whenever a user sends an SMS including a command, he/she will receive a response. The used commands are as follows:</p>
    <p>1. Help: to request a list of all the commands available for usage and their descriptions.</p>
    <p>2. Getwallet: to acquire a bitcoin wallet from the payment framework. When acquired, a user can use this wallet to create a bitcoin address, receive and send bitcoins.</p>
    <p>3. Addr: to generate a bitcoin address from a bitcoin wallet acquired from the payment framework. Whenever a user issues this command in an SMS, he/she will generate a new unused bitcoin address.</p>
    <p>4. Bal: to request the balance of a bitcoin wallet.</p>
    <p>5. Send: to send a bitcoin payment. When the command is issued, a session is opened for the user and the framework will ask for his/her Personal Identification Number (PIN), the amount of bitcoins to be sent and the recipient&#8217;s mobile phone number. Bitcoins can only be sent to a recipient who is recorded on the framework&#8217;s system. Nevertheless, a user can receive bitcoins from a user who isn&#8217;t recorded on the framework&#8217;s system provided that he/she knows the recipient&#8217;s bitcoin address.</p>
    <p>The sent SMSs are charged according to the standard SMS rates of MNO.</p>
    <p>GSM Modem:</p>
    <p>The researchers chose a GSM modem that uses a CELL C MNO SIM card. The modem is connected to a computer which can communicate with various devices subscribed to the MNO.</p>
    <p>SMS Gateway:</p>
    <p>The used SMS gateway is formulated to parse the retrieved SMSs from the GSM modem, then transform the string to lowercase letters while also stripping the spaces from the beginning and end of the string. The yielded message is then processed via the MBWSC, which runs the function of the chosen command.</p>
    <p>ABWM:</p>
    <p>ABWM represents a bitcoin wallet manager that enables the developer to access the blockchain. It is an open source application which is utilized to create encrypted wallets that are stored on the computer&#8217;s storage disc.</p>
    <p>MBWSC:</p>
    <p>The MBWSC represents an application that controls the functions that are executed after receiving the SMS command. In other words, it runs the command e.g. if the command included in the SMS was Addr, the following is executed:</p>
    <p>1. Check whether or not a user&#8217;s record is present in the system.</p>
    <p>2. If the user&#8217;s record is not present in the system, an SMS will be sent to let him/her know that he/she doesn&#8217;t own a bitcoin wallet on the system.</p>
    <p>3. If the user&#8217;s record is present, the next unused address will be extracted from the user&#8217;s wallet.</p>
    <p>4. Send the user the bitcoin address.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/bitcoin/" rel="tag">bitcoin</a> <a href="https://www.deepdotweb.com/tag/bitcoins/" rel="tag">bitcoins</a> <a href="https://www.deepdotweb.com/tag/framework/" rel="tag">framework</a> <a href="https://www.deepdotweb.com/tag/lowend/" rel="tag">lowend</a> <a href="https://www.deepdotweb.com/tag/mobile/" rel="tag">mobile</a> <a href="https://www.deepdotweb.com/tag/phones/" rel="tag">phones</a> <a href="https://www.deepdotweb.com/tag/sending/" rel="tag">sending</a></span> <span style="display:none" class="updated">2017-02-23</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

