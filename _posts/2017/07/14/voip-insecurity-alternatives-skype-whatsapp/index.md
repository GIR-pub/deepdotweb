---
VOIP (IN)SECURITY: ALTERNATIVES TO SKYPE AND WHATSAPP
---
<article class="post-listing post-21233 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-alternatives tag-insecurity tag-skype tag-voip tag-whatsapp">
    <div class="post-inner">
    <p class="post-meta">
    <span>Posted by: <a href="https://www.deepdotweb.com/author/theinnocent/" title="">TheInnocent </a></span>
    <span>July 14, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/07/14/voip-insecurity-alternatives-skype-whatsapp/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>&nbsp;</p>
    <p>Skype was released on August 29, 2003 and was quite a revolution. With Skype the voice and video information was packetized and transmitted over internet protocol networks; people could call for free, using only an internet connection. Skype was then acquired by Microsoft that started to work with NSA in the PRISM surveillance program in order to access private calls and messages from nine big companies including Microsoft, Apple, Google, Facebook.</p>
    <p><img class="wp-image-21243 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/07/word-image-14.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/07/word-image-14.png 700w, https://www.deepdotweb.com/wp-content/uploads/2017/07/word-image-14-300x225.png 300w" sizes="(max-width: 700px) 100vw, 700px" /></p>
    <p>Since this happened, writing the words “<a href="https://www.deepdotweb.com/2016/08/17/morocco-bans-skype-whatsapp-voip-crackdown-state-isp/">skype</a>” and “secure” in the same statement, it has become nonsense.</p>
    <p>Fortunately many protocols help us to secure our conversations in combination with security applications for messaging and video calls.</p>
    <p><a href="https://www.deepdotweb.com/2015/05/17/tutorial-xmppjabber-otr/">OTR</a> (Off the Record messaging) allows us to have private conversations over instant messaging. The key features of OTR are:</p>
    <ul>
    <li>Encryption</li>
    </ul>
    <p>All the communication is strongly encrypted. The content of you messages cannot be seen by the servers.</p>
    <ul>
    <li>Deniability</li>
    </ul>
    <p>The messages you send don’t have any digital signature.</p>
    <ul>
    <li>Authentication</li>
    </ul>
    <p>You can be sure to know who you’re talking to.</p>
    <ul>
    <li>Perfect Forward Secrecy</li>
    </ul>
    <p>No previous conversation is compromised if you lose control of your keys.</p>
    <p>XMPP is Extensible Messaging and Presence Protocol, a secure and decentralized (everyone can run his own XMPP server) protocol for chatting, voice and video calls.</p>
    <p>To create a Jabber (this was the original name of XMPP) account, you can sign up with one of the numerous servers that offer a jabber service, it is not important which one you choose. Once you’re done with that, you can download an instant messaging tool like <a href="http://www.pidgin.im/">pidgin</a>. When pidgin starts, it will ask you to create a new account. Choose XMPP as “protocol”, the username you chose during the account registration as “username”, the name of the server as Domain (e.g. jabber.org), and the password you chose during the account registration as “password”. In “Advanced” set 5222 as the default port and your server’s address. To connect over tor, in “Proxy” set 127.0.0.1 as “host” and 9050 as “port”; click on “save” and you’re done with your account’s creation. Now you can activate <a href="http://www.cypherpunks.ca/otr/">OTR</a> in the plugins menu checking the box which says “Messaging Off The Record”. When you start a conversation with a friend, you’ll see “not private” in the bottom-right corner. Click on it and choose “start private conversation”. If your friend has OTR too, you’ll see “unverified” near his contact. Click on it and choose “authenticate buddy”. There are several ways you can do it, for example you can make him answer to a secret question. Once he’s done with that, you’ll see “private” in the bottom-right corner.</p>
    <p>For what concerns encrypted calls, the ZRTP protocol is what you need. ZRTP stands for Zimmermann Real-Time Transport Protocol and it was developed by Phil Zimmermann, Silent Circle’s owner. From <a href="https://www.silentcircle.com/products-and-solutions/technology/zrtp/">Silent Circle</a>:</p>
    <p><em>“ZRTP is a cryptographic key-agreement protocol to negotiate the keys for encryption between two end points in a Voice over Internet Protocol (VoIP) phone telephony call based on the Real-time Transport Protocol. It uses </em><a href="https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange"><em>Diffie–Hellman key exchange</em></a><em> and the </em><a href="https://en.wikipedia.org/wiki/Secure_Real-time_Transport_Protocol"><em>Secure Real-time Transport</em></a> <a href="https://en.wikipedia.org/wiki/Secure_Real-time_Transport_Protocol"><em>Protocol</em></a><em> (SRTP) for encryption.”</em></p>
    <p>Silent Phone developed by Silent Circle, protects you from MITM attacks using ZRTP for every call. Anyway you don’t need to buy a Silent Phone to use ZRTP, there are numerous applications that use this protocol by default.</p>
    <p>Signal is an open-source application available for android and iOS developed by Open Whisper. It uses ZRTP to allow us to make secure calls. Every time we open a new conversation with a contact we can verify that we’re talking to the right person opening settings and clicking on “verify safety number”. A safety number is a 60-digit number you can compare with the one of your contact to make sure that your conversation is private. You can also use a desktop version with which you can call and text your contacts from your computer.</p>
    <p>Until this point we talked about secure messaging and secure calling but if you also want secure video-calling, you can use Threema.</p>
    <p><img class="wp-image-21245 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/07/word-image-15.png" width="676" height="451" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/07/word-image-15.png 1260w, https://www.deepdotweb.com/wp-content/uploads/2017/07/word-image-15-300x200.png 300w, https://www.deepdotweb.com/wp-content/uploads/2017/07/word-image-15-1024x683.png 1024w" sizes="(max-width: 676px) 100vw, 676px" /></p>
    <p>To use this app, no telephone number is requested, because a Threema id is generated. This grants you full anonymity and also means that you can use Threema also on devices without a SIM. You can verify your contacts scanning a QR-code or comparing some keys and the messages, files and even the status messages are end-to-end encrypted. A desktop version exists also for this app and you’re not forced to use Chrome, you can also use Firefox. Additionally, Threema declares to be an independent and self-financed company based in Switzerland, “<em>a country with some of the most user friendly privacy laws in the world”</em>.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/alternatives/" rel="tag">alternatives</a> <a href="https://www.deepdotweb.com/tag/insecurity/" rel="tag">insecurity</a> <a href="https://www.deepdotweb.com/tag/skype/" rel="tag">skype</a> <a href="https://www.deepdotweb.com/tag/voip/" rel="tag">voip</a> <a href="https://www.deepdotweb.com/tag/whatsapp/" rel="tag">whatsapp</a></span> <span style="display:none" class="updated">2017-07-14</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/theinnocent/" title="Posts by TheInnocent" rel="author">TheInnocent</a></strong></div>
    </div>
</article>

