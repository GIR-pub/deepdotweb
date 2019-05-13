---
No Dice: Diceware Passphrase Creation System
---
<article class="post-listing post-15243 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-creation tag-dice tag-diceware tag-passphrase tag-system">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/ciphas/" title="">Ciphas </a></span>
    <span>August 24, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/08/24/no-dice-diceware-passphrase-creation-system/#comments">6 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Not long ago, I was browsing the Tor network and came across several doxing sites.  One of them in particular struck me because it was a list of social media accounts, including usernames and passwords.  The passwords were what stood out the most, because they often looked like this:</p>
    <ul>
    <li>123456</li>
    <li>password</li>
    <li>bob123456</li>
    <li>12345678</li>
    <li>Letmein</li>
    <li>batman</li>
    </ul>
    <p>After seeing that, I thought, “No wonder people get their passwords stolen so easily!”  This was one of the things that led me to seek out a more secure password system, and one of the ones that I came across was the Diceware Passphrase System.</p>
    <p>Diceware is a system used to create passphrases based on random rolls of <em>physical</em> dice.  The dice rolls correspond to a long word list, wherein the outcomes of five dice rolls each stand for a single word, number, or letter combination.  Here’s an example:</p>
    <p>21526 crab</p>
    <p>32264 haley</p>
    <p>52346 rst</p>
    <p>12654 avail</p>
    <p>54322 slake</p>
    <p>The words that the dice rolls represent (in this case) are taken from the <a href="http://world.std.com/~reinhold/diceware.wordlist.asc">official Diceware word list</a>, which contains 7776 short words, abbreviations, and easy to remember character strings (in theory).  Beyond the official list, there are alternate ones, such as the <a href="http://world.std.com/~reinhold/beale.wordlist.asc">Beale Wordlist</a>, as well.  If you mix and match the different word lists, this improves the security.  Some people may find them harder to remember than others, so you may initially have to store your password somewhere offline.  Eventually you’ll memorize them!</p>
    <p><strong>Warning:</strong> although there are online sites such as <a href="https://entima.net/diceware/">Entima.net: Diceware Passphrase Generator</a> where you can generate Diceware passphrases without going through the process of physically rolling dice, these are significantly weaker than the offline versions.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2016/08/1-6.png"><img class="aligncenter size-full wp-image-15244" src="https://www.deepdotweb.com/wp-content/uploads/2016/08/1-6.png" alt="1" width="1616" height="876" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/08/1-6.png 1616w, https://www.deepdotweb.com/wp-content/uploads/2016/08/1-6-300x163.png 300w, https://www.deepdotweb.com/wp-content/uploads/2016/08/1-6-1024x555.png 1024w" sizes="(max-width: 1616px) 100vw, 1616px" /></a></p>
    <p>In fact, the site specifically mentions this:  “This passphrase is too weak to resist an offline attack where the password hashes are available to the attacker.”</p>
    <p>Beyond just using the word lists, however, you can generate random passwords and characters using the same method (although it takes a little longer and therefore, more patience). On the last page of the official list is a system of dice tables you can use to generate passwords and random characters (which is even more secure, in theory).</p>
    <p>With the dice tables, you would roll a die three times for each character, and then select one of three tables, based on what comes up on the first roll.  Here’s a good link that explains how that works: <a href="http://world.std.com/~reinhold/dicewarefaq.html">Diceware Passphrase FAQ</a></p>
    <p>Just for fun, to test out the security of one of the Diceware passphrases, I used this example (which is <em>not</em> one of my real passphrases!):</p>
    <p>13236 baku</p>
    <p>53352 sepoy</p>
    <p>42625 rilly</p>
    <p>42662 moyer</p>
    <p>53643 shrug</p>
    <p>64134 white</p>
    <p>53234 scuba</p>
    <p>65152 yodel</p>
    <p>At the end of the list of words, I added a randomly generated set of characters from the dice: $f!{  Also, in between each word, I added a period (which you can choose to do or not).  Here was the result, according to <a href="https://www.grc.com/haystack.htm">GRC&#8217;s Brute Force Password Search Space Calculator</a>.</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2016/08/2-6.png"><img class="aligncenter size-full wp-image-15245" src="https://www.deepdotweb.com/wp-content/uploads/2016/08/2-6.png" alt="2" width="1248" height="732" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/08/2-6.png 1248w, https://www.deepdotweb.com/wp-content/uploads/2016/08/2-6-300x176.png 300w, https://www.deepdotweb.com/wp-content/uploads/2016/08/2-6-1024x601.png 1024w" sizes="(max-width: 1248px) 100vw, 1248px" /></a></p>
    <p>Can you read that?  The Search Space Size (as a power of 10) = 1.51 x 10<sup>73 </sup>According to the “Time Required to Exhaustively Search this Password’s Space:</p>
    <ul>
    <li>Online Attack Scenario (assuming 1000 guesses per second): “4.76 hundred trillion (x7) centuries.”</li>
    <li>Offline Fast Attack Scenario (assuming 100 billion guesses per second): “4.76 million trillion(x6) centuries.”</li>
    <li>Massive Cracking Array Scenario (assuming 100 trillion guesses per second): “4.76 thousand trillion(x6) centuries.”</li>
    </ul>
    <p>I don’t know about you guys, but I find that very reassuring!  Contrast that with one of the common passwords, like “password.”  According to the same site:</p>
    <p><a href="https://www.deepdotweb.com/wp-content/uploads/2016/08/3-5.png"><img class="aligncenter size-full wp-image-15246" src="https://www.deepdotweb.com/wp-content/uploads/2016/08/3-5.png" alt="3" width="1250" height="632" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/08/3-5.png 1250w, https://www.deepdotweb.com/wp-content/uploads/2016/08/3-5-300x152.png 300w, https://www.deepdotweb.com/wp-content/uploads/2016/08/3-5-1024x518.png 1024w" sizes="(max-width: 1250px) 100vw, 1250px" /></a></p>
    <ul>
    <li>Online Attack Scenario: “6.91 years”</li>
    <li>Offline Fast Attack Scenario: “2.17 seconds”</li>
    <li>Massive Cracking Array Scenario: “0.00217 seconds”</li>
    </ul>
    <p>That’s not even taking into account that something like “password” is so common that an attacker might try that first.  So, what’s the conclusion?  Although it may take a bit more time and effort, the offline randomly generated passphrases are significantly stronger than many of the most common passwords.</p>
    <p>Granted, nothing is unhackable, but even when using a brute force attack, it would still take significantly longer to crack a Diceware passphrase, as opposed to your average, everyday password.</p>
    <p>If you ask me, “Is it worth the effort?”  I’d say yes.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/creation/" rel="tag">creation</a> <a href="https://www.deepdotweb.com/tag/dice/" rel="tag">dice</a> <a href="https://www.deepdotweb.com/tag/diceware/" rel="tag">diceware</a> <a href="https://www.deepdotweb.com/tag/passphrase/" rel="tag">passphrase</a> <a href="https://www.deepdotweb.com/tag/system/" rel="tag">system</a></span> <span style="display:none" class="updated">2016-08-24</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/ciphas/" title="Posts by Ciphas" rel="author">Ciphas</a></strong></div>
    </div>
</article>

