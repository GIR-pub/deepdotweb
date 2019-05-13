---
Here’s some tips for using Signal as safely as possible
---
<article class="post-listing post-14751 post type-post status-publish format-standard has-post-thumbnail hentry  tag-signal tag-tips">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/caliens/" title="">C. Aliens </a></span>
    <span>July 7, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/07/07/heres-tips-using-signal-safely-possible/#comments">4 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>A few weeks ago, we <a href="https://www.deepdotweb.com/2016/06/22/brief-comparison-secure-messaging-apps/">wrote</a> about how Signal was one of the better encrypted messaging applications for mobile devices. In the article, it was mentioned that no matter how secure you think your platform is – there’s always a weak link. More often than not, user error plays a major key in how weak that link is. An article was published by <a href="https://theintercept.com/2016/07/02/security-tips-every-signal-user-should-know/">The Intercept</a>_ yesterday that points out a few extra steps one can take to further protect themselves while using Signal. I’ll run through their list briefly. This list is fairly straightforward, and if you’re not a newcomer to operation security or the ins-and-outs of Signal, this write-up probably won’t provide too much insight.</p>
    <p><a href="/imgs/2016/07/signal1.jpg"><img class="aligncenter size-full wp-image-14752" src="/imgs/2016/07/signal1.jpg" alt="signal1" width="540" height="334" srcset="/imgs/2016/07/signal1.jpg 540w, /imgs/2016/07/signal1-300x186.jpg 300w" sizes="(max-width: 540px) 100vw, 540px" /></a></p>
    <p><strong>If you’re on Android: </strong></p>
    <ul>
    <li><strong>Set a passcode. </strong>No need to go into detail on this one. You all know how to set passcodes. The Intercept_ has a great bit on Touch ID/fingerprint sensors that I’ll stick at the bottom of the article, but I would completely avoid using patterns or four digit pin-codes.</li>
    <li><strong>Encrypt your phone’s storage. </strong>It’s default on iOS, but it’s a lot easier to forget about storage encryption as it’s often “hidden” within settings. It’s not really hidden, but it’s nested a little bit. Settings → Security → “Encrypt Phone.” It takes as long as an hour and I believe your phone needs to be plugged into a power source. There’s no reason not to have your phone encrypted if you’re security conscious.</li>
    <li><strong>Install updates promptly. </strong>I can’t entirely agree with this one. Or at least the promptly part. I remember several incremental bug-patching updates that caused more issues than they fixed. I would recommend waiting until someone else is able to test the update.</li>
    </ul>
    <p><strong>If you’re on iOS:</strong></p>
    <ul>
    <li><strong>Set a passcode. </strong>See the Android passcode section. There’s no difference in function. Avoid four digit pins like the plague though. I’ll briefly <em>touch</em> on Touch ID at the bottom of this article.</li>
    <li><strong>Install updates promptly. </strong>Again, see above. I would generally say that iOS is by default somewhat more secure than Android, but when it comes to updates, I’m not so sure.</li>
    </ul>
    <p>The next category is fairly similar to the first one – it helps prevent people who have physical access to you phone, whether innocent or law enforcement, from snooping or extracting data.</p>
    <h3>Hide Signal Messages on Your Lock Screen</h3>
    <p>If you’re using Android:</p>
    <ol>
    <li>Open the Settings app, and under “Device” &gt; “Sound &amp; notification” select “When device is locked.”</li>
    <li>The options are “Show all notification content,” “Hide sensitive notification content,” or “Don’t show notifications at all.” I recommend you choose “Hide sensitive information content” — this way you’ll still be notified when you get a Signal message, but you’ll have to unlock your phone to see who it’s from and what it says.(<a href="https://theintercept.com/2016/07/02/security-tips-every-signal-user-should-know/">source</a>)</li>
    </ol>
    <p>If you’re using an iPhone</p>
    <ol>
    <li>Open the Signal app and click the gear icon in the top-left to get to Signal’s settings. Under “Notifications” &gt; “Background Notifications,” tap “Show.”</li>
    <li>The options are “Sender name &amp; message,” “Sender name only,” or “No name or message.” I recommend you choose “No name or message” — this way you’ll still be notified when you get a Signal message, but you’ll have to unlock your phone to see who it’s from and what it says.</li>
    <li>To completely remove Signal notifications from your iPhone’s lock screen, open the Settings app, tap “Notifications,” scroll down to the list of apps, and tap Signal. From here you can turn off “Show on Lock Screen.”(<a href="https://theintercept.com/2016/07/02/security-tips-every-signal-user-should-know/">source</a>)</li>
    </ol>
    <p>Verifying Identities</p>
    <p>This is my favorite part as it encompasses the entire purpose of having a secure messaging app like Signal. I use Signal with a handful of contacts and one of them is admittedly security naive – he had no idea that man-in-the-middle attacks were still a threat. One of the the key functions of Signal is how easy it is to verify the identity of the party you’re communicating with. Here’s how:</p>
    <p>Verify your phone contacts.</p>
    <blockquote><p><em>“It’s easy to verify the security of phone calls on Signal, but you have to verify every call.</em></p>
    <p><em>For each call, the Signal app displays two words on the callers’ phone screens. In the screen shot below, for example, each screen shows the words “shamrock paragon.” Juliet and Romeo read these words to one another; if the words are the same, and they recognize one another’s voices, the call is secure. If the words are different, someone is attacking the encryption in the call and you should hang up and try calling again, but this time from a different internet connection.</em></p>
    <p><em>It’s not required, but a popular convention is for the receiver to answer the phone by reading the first word, as in, “Shamrock?” And the caller to respond with the second word, as in, “Paragon.”</em></p></blockquote>
    <p><strong>Verify your text contacts.</strong></p>
    <blockquote><p><em>It’s more complicated to verify the security of Signal text chats, but once you’ve verified a text chat correspondent, you won’t have to re-verify them again until they get a new phone or re-install Signal.</em></p>
    <p><em>Each person you text with in Signal has something called an identity key. When Juliet sends Romeo a message for the first time, her Signal app downloads a copy of his identity key and stores it on her phone and visa versa. So long as these identity keys are valid — the key that Juliet has stored for Romeo is actually Romeo’s real key and not some attacker’s key — then the messages they send to each other are secure.</em></p>
    <p><em>Because it’s unlikely that anyone is trying to attack your encrypted messages the <em>very first time</em> you send a contact a message, Signal automatically trusts the identity key that it downloads. This makes Signal easy to use: All you need to do to have an encrypted conversation is send someone a message, and that’s it. But if you discuss anything sensitive, you still might want to confirm.</em></p>
    <p><em>To verify the identity key, you first navigate to the verification screen.</em></p></blockquote>
    <p>If you’re using Android:</p>
    <ul>
    <li>Open the Signal app and tap on a conversation to open it</li>
    <li>Tap the contact’s name and phone number at the top of the screen</li>
    <li>Tap “Verify identity”</li>
    </ul>
    <p>If you’re using an iPhone:</p>
    <ul>
    <li>Open the Signal app and tap on a conversation to open it</li>
    <li>Long-press the contact’s name at the top of the screen until the verification screen appears</li>
    </ul>
    <p><a href="/imgs/2016/07/signal2.png"><img class="aligncenter size-full wp-image-14753" src="/imgs/2016/07/signal2.png" alt="signal2" width="1024" height="911" srcset="/imgs/2016/07/signal2.png 1024w, /imgs/2016/07/signal2-300x267.png 300w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></p>
    <p><strong>Verifying a Text Contact in Person</strong></p>
    <p>If you are using Signal to communicate with someone who you can meet up with in real life, you have another method of verifying a contact’s identity. There’s an automated method of scanning each user’s QR codes and a more painstaking solution where you can compare each key by looking them both over to spot differences. Obviously scanning a QR code is easier. The Intercept_ lays it out in an understandable fashion.</p>
    <p>If you’re using Android:</p>
    <ul>
    <li>To be verified, tap the barcode icon in the top-right of the verification screen and select “Display your QR code” (you may be prompted to install the Barcode Scanner app the first time you do this; it is safe to install).</li>
    <li>To verify someone else, tap the barcode icon on the verification screen and choose “Scan contact’s QR code,” and then point your camera at the contact’s QR code.</li>
    </ul>
    <p>If you’re using an iPhone:</p>
    <ul>
    <li>To be verified, tap the QR code icon on the verification screen.</li>
    <li>To verify someone else, tap the camera icon on the verification screen, and then point the iPhone camera at the person’s QR code.</li>
    </ul>
    <p>When you successfully verify a contact, Signal should pop up a message that says, “Verified!”</p>
    <p><strong>Remotely verifying a contact.</strong></p>
    <p>This is one that people overlook fairly often; if you’re trying to verify your contact is who he or she says they are, sending your key over a Signal text message is not a good idea. Here’s what they wrote:</p>
    <blockquote><p><em>If you can’t meet up in person, you can still verify that you have the right identity key by comparing fingerprints — however, it’s kind of annoying.</em></p>
    <p><em>You need to share your fingerprint with your contact using some out-of-band communication channel — that is, don’t share it in a Signal message. Instead, share it in a Facebook message, Twitter direct message, email, or phone call. You could also choose to share it using some other encrypted messaging app, such as WhatsApp or iMessage. (If you’re feeling paranoid, a phone call is a good option; it would be challenging for an attacker to pretend to be your contact if you recognize their voice.)</em></p>
    <p><em>Once your contact gets your fingerprint, they need to navigate to the verification screen and compare, character by character, what you sent them with what they see. If they match, your conversation is secure.</em></p>
    <p><em>Your contact should share their fingerprint with you in the same way, and you should confirm that what they sent you matches what’s on your verification screen as well.</em></p>
    <p><em>If you’re using Android, unfortunately there’s no way to copy your own fingerprint to your phone’s clipboard to paste into another app. If you want to share it using another app on your phone, you’ll have to manually type it.</em></p>
    <p><em>If you’re using an iPhone, you can copy your own fingerprint to your phone’s clipboard like this: Open the Signal app and click the gear icon in the top-left to get to Signal’s settings. Tap Privacy, then tap Fingerprint.</em></p></blockquote>
    <p><strong>Verify your contact after they get a new phone</strong></p>
    <p>Last but not least, they talk about verifying a user’s identity after they purchase or switch to a new device. This one is fairly important as well and has been an issue in my situation as I switch between Android and iOS fairly often, using the same number. This change shows up to the contact you’ve been conversing with and lets them know that your identity changed. This most likely points to a user getting a new phone or reinstalling the app – but there’s the slight chance it could be law enforcement trying to put their nose where it probably doesn’t belong.</p>
    <p>But when you do see a warning telling you that they keychain of of the person you are communication with has changed, you need to go through the process of verifying a text contact, as detailed in the previous section.</p>
    <p>It’s worth pointing out a bit about passwords that The Intercept_ wrote in an <a href="https://theintercept.com/2016/02/18/passcodes-that-can-defeat-fbi-ios-backdoor/#instructions"><strong>article about the FBI’s back-door strategy</strong></a> in the FBI’s case against Apple.</p>
    <p><em>Don’t use Touch ID to unlock your phone. Your attacker doesn’t need to guess your passcode if she can push your finger onto the home button to unlock it instead. (At least one court has </em><a href="http://jolt.law.harvard.edu/digest/telecommunications/court-rules-police-may-compel-suspects-to-unlock-fingerprint-protected-smartphones"><strong><em>ruled</em></strong></a> <em>that while the police cannot compel you to disclose your passcode, they can compel you to use your fingerprint to unlock your smartphone.)</em></p>
    <p>Source: <a href="https://theintercept.com/2016/07/02/security-tips-every-signal-user-should-know/">The Intercept</a></p>
    <p>Recommended Reading: <a href="https://www.deepdotweb.com/2016/06/22/brief-comparison-secure-messaging-apps/">A Brief Comparison of Secure Messaging Apps</a></p>
    <p>&nbsp;</p>
    </div>
    <span style="display:none"> <a href="https://www.deepdotweb.com/tag/signal/" rel="tag">signal</a> <a href="https://www.deepdotweb.com/tag/tips/" rel="tag">tips</a></span> <span style="display:none" class="updated">2016-07-07</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/caliens/" title="Posts by C. Aliens" rel="author">C. Aliens</a></strong></div>
    </div>
</article>

