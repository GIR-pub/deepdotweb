---
All You Need To Know About Passwords
---
<article class="post-listing post-16395 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-passwords">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/filipjelic/" title="">Filip Jelic </a></span>
    <span>November 12, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/11/12/need-know-passwords/#comments">4 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Choosing and managing passwords is the fundamental security measure in client&#8217;s control. Even if the application and it&#8217;s server is impenetrable, it means absolutely nothing if your password can be cracked by an average Joe.</p>
    <p>You would think that all security conscious people would know how to protect themselves, but I frequently see cases like this:</p>
    <p>CaliConnect’s Private PGP Key &amp; Account Password Was “<a href="https://www.deepdotweb.com/2016/08/13/caliconnects-private-pgp-key-account-password-asshole209/">asshole209</a>”</p>
    <p>Twittor – Launched &amp; Hacked in 2 Hours (Password was: <a href="https://www.deepdotweb.com/2014/02/22/twittor-launched-hacked-2-hours/">123123123</a>…)</p>
    <p>Cantina Marketplace PWND: Admin Password was: “<a href="https://www.deepdotweb.com/2014/01/29/cantina-marketplace-pwnd-admin-password-was-password1/">Password1</a>” ?!</p>
    <p>This tutorial contains explanations of password cracking when the server and client side are protected. These methods&#8217; effectiveness highly depend on attacker&#8217;s processing power which we&#8217;ll analyze after attack methods.</p>
    <p>If you just want to know easy way to be safe, jump to the &#8216;Easy way to manage strong passwords&#8217;.</p>
    <p><strong>Brute Force Attack</strong></p>
    <p>Brute-force attack is a technique of enumerating all possible password candidates and checking each one. This is no elegant attacking method, but sometimes it&#8217;s all that&#8217;s needed. This attack is feasible only for very weak passwords.</p>
    <p><strong>Dictionary Attack</strong></p>
    <p>Dictionary attack is a variant of brute force attack in which the attacker gathers all information about targeted password(s) and creates a &#8216;dictionary&#8217;. Dictionary is a customized list of password candidates, typically including a list of most common passwords first, dictionary words that are frequently used and some combinations. Next, the dictionary often contains all those words with common prefixes and suffixes such as numbers and punctuation signs.</p>
    <p>Dictionary attacks are relatively easy to defeat by choosing a password that is not a simple variant of a word found in any dictionary. Many password cracking tools have built-in dictionaries. <a href="https://wiki.skullsecurity.org/Passwords">This page</a> contains information on most popular tools, their dictionaries and collections of leaked password for analysis in one place.</p>
    <p>fQnT1d0c{E}+p[;</p>
    <p><strong>Rainbow Tables </strong></p>
    <p>This attack is used when attacker owns the password database. It&#8217;s worth mentioning here because the complexity of your password will protect you even if the server is compromised. Protection wise, it&#8217;s enough to know that a strong password will do the trick here as well.</p>
    <p>Skip this part if you just want to secure yourself without bothering with hashing, rainbow tables and salting.</p>
    <p>Databases don&#8217;t contain plaintext passwords, but password hashes. Hash is the result of time-consuming function that obfuscates the input. When you enter your password, server calculates the hash of the entered value and compares it to the one stored in the database for the confirmation.</p>
    <p>Very simple hash function example: take number 4 as the input: square it (16), take natural log (2.7725), multiply by pi (8.7103) and take factorial (gamma function) -&gt; 189843.119. Now ask your friend how is 189843.119 related to 4. Chances are, no one can figure it out.</p>
    <p>Password hashes often look like this one: qiyh4XPJGsOZ2MEAyLkfWqeQ</p>
    <p>So, when an attacker compromises the password database he won&#8217;t be able to figure out your password (or will he?, read on). Here&#8217;s when rainbow table comes in – it&#8217;s a pre-computed table of passwords and their hashes. Attacker then compares the rainbow table hashes to those in the database. If hashes match, the password is discovered. Here&#8217;s a short exampe:</p>
    <p>This is what we can find in a database:</p>
    <table>
    <tbody>
    <tr>
    <td>User</td>
    <td>Password</td>
    </tr>
    <tr>
    <td>RegularUser1</td>
    <td>HgkHJgKHgKhKGhjfhgKvkGjKG</td>
    </tr>
    <tr>
    <td>Administrator</td>
    <td>qiyh4XPJGsOZ2MEAyLkfWqeQ</td>
    </tr>
    <tr>
    <td>&#8230;</td>
    <td>&#8230;</td>
    </tr>
    </tbody>
    </table>
    <p>Lets try to find this hash in the rainbow table:</p>
    <table>
    <tbody>
    <tr>
    <td>Password</td>
    <td>Hash</td>
    </tr>
    <tr>
    <td>password</td>
    <td>asdh4DFGsOZ2MEAyLkfWqES</td>
    </tr>
    <tr>
    <td>qwerty</td>
    <td>qi8H8R7OM4xMfdMPuRAZxlY</td>
    </tr>
    <tr>
    <td>pass1234</td>
    <td>GsOZ2MEAM4xPuRAZxlqiyAFiy</td>
    </tr>
    <tr>
    <td>passw0rd</td>
    <td>qiyh4XPJGsOZ2MEAyLkfWqeQ</td>
    </tr>
    <tr>
    <td>abcdefgh</td>
    <td>nKv3LvrdAVtOcE5EcsGIpYBtniN</td>
    </tr>
    <tr>
    <td>&#8230;</td>
    <td>&#8230;</td>
    </tr>
    </tbody>
    </table>
    <p>That&#8217;s why some servers &#8216;salt&#8217; the hash by adding random value into the equation so the attacker can&#8217;t just download finished rainbow table, he needs to create a custom one for that salt and that requires a lot of time because hash functions are time-consuming. If different salt is used for each password, attacker needs to create a custom table for each password which is not feasible. Salt is stored next to the password, it&#8217;s no secret since it&#8217;s just making the attacker&#8217;s computer do a lot of &#8216;work&#8217;.</p>
    <p>There&#8217;s only that much server side can do for you, it&#8217;s up to you to choose a strong password. If the attacker targets you specifically, he may create a rainbow table for your salt. It&#8217;s up to you to have a password that will not be in his table.</p>
    <p>I&#8217;m surprised how many sensitive web services allow having weak password.</p>
    <p><strong>Practical analysis of these attacks</strong></p>
    <p>Analyzed time represents <strong>offline attack speed</strong>, online attacks are much slower than this, but it&#8217;s logical to seek for a password strong enough for offline attacks because it&#8217;s the maximum speed and it&#8217;s just a few characters away.</p>
    <p>Password complexity depends on 2 characteristics: length and number of different characters. For example, if you use 8 digit password (only numbers – 10 characters): _ _ _ _ _ _ _ _ each field can contain 10 different characters, so there are 10*10*10*10*10*10*10*10 = 10<sup>8</sup> possible combinations. If attacker has a Pentium 4D, 3.2 Ghz processor he can try 2 million passwords per second. That means the password can be broken in 10<sup>8</sup> / (2*10<sup>6</sup>) = 50 seconds.</p>
    <p>Formula for the number of combinations the attacker need to try:</p>
    <p>A<sup>B </sup>where: A – number of different possible characters</p>
    <p>B – password length</p>
    <p>If password length is unknown, the attacker will usually try only the shortest ones. Let&#8217;s say he wants to try all 8,9,10 characters long passwords, the number of combinations is: A<sup>8 </sup>+ A<sup>9</sup> + A<sup>10 </sup>.</p>
    <p><strong>Exponential growth</strong></p>
    <p>Luckily for us, password complexity rises exponentially when length increases. In the example above (only 10 digits) each extra character adds 10 times more possible combinations.</p>
    <p>Here&#8217;s a table for passwords that contain only lower-case letters from English alphabet and digits – 36 different characters (Combinations = 36 ^ length):</p>
    <table>
    <tbody>
    <tr>
    <td>Length (B)</td>
    <td>Combinations (36<sup>B</sup>)</td>
    <td>Individual capability</td>
    <td>5000x individual</td>
    </tr>
    <tr>
    <td>1</td>
    <td>34</td>
    <td>&lt; 1 second</td>
    <td>&lt; 1 second</td>
    </tr>
    <tr>
    <td>2</td>
    <td>1 296</td>
    <td>&lt; 1 second</td>
    <td>&lt; 1 second</td>
    </tr>
    <tr>
    <td>3</td>
    <td>46 656</td>
    <td>&lt; 1 second</td>
    <td>&lt; 1 second</td>
    </tr>
    <tr>
    <td>4</td>
    <td>1 679 616</td>
    <td>&lt; 1 second</td>
    <td>&lt; 1 second</td>
    </tr>
    <tr>
    <td>5</td>
    <td>60 466 176</td>
    <td>30 seconds</td>
    <td>&lt; 1 second</td>
    </tr>
    <tr>
    <td>6</td>
    <td>21 76 782 336</td>
    <td>18 minutes</td>
    <td>1 second</td>
    </tr>
    <tr>
    <td>7</td>
    <td>78 364 164 096</td>
    <td>10 hours</td>
    <td>55 seconds</td>
    </tr>
    <tr>
    <td>8</td>
    <td>2 821 109 907 456</td>
    <td>16 days</td>
    <td>33 minutes</td>
    </tr>
    <tr>
    <td>9</td>
    <td>101 559 956 668 416</td>
    <td>1 year</td>
    <td>20 hours</td>
    </tr>
    <tr>
    <td>10</td>
    <td>3 656 158 440 062 976</td>
    <td>60 years</td>
    <td>30 days</td>
    </tr>
    <tr>
    <td>11</td>
    <td>131 621 703 842 267 136</td>
    <td>2140 years</td>
    <td>3 years</td>
    </tr>
    <tr>
    <td>12</td>
    <td>4 738 381 338 321 616 896</td>
    <td>77025 years</td>
    <td>110 years</td>
    </tr>
    </tbody>
    </table>
    <p>X axis &#8211; password length in for 36 charset (letters and numbers)</p>
    <p>Y axis &#8211; days to crack</p>
    <p><img class="wp-image-16406" src="https://www.deepdotweb.com/wp-content/uploads/2016/11/word-image-20.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/11/word-image-20.png 850w, https://www.deepdotweb.com/wp-content/uploads/2016/11/word-image-20-300x185.png 300w" sizes="(max-width: 850px) 100vw, 850px" /></p>
    <p>Blue &#8211; Time in the first case was an experiment with previously mentioned Pentum 4D, 3.2 Ghz processor, affordable processing power for an individual.</p>
    <p>Red &#8211; Time in the second case represents someone that can use 5 000 such processors.</p>
    <p>We can see length 12 is sweet, it&#8217;s even more safe if we expand the character set to uppercase and lowercase letters, numbers and punctuation signs. Number of possible characters is 126:</p>
    <table>
    <tbody>
    <tr>
    <td>Length (B)</td>
    <td>Combinations (126<sup>B</sup>)</td>
    <td>Individual capability</td>
    <td>5000x individual</td>
    </tr>
    <tr>
    <td>1</td>
    <td>126</td>
    <td>&lt; 1 second</td>
    <td>&lt; 1 second</td>
    </tr>
    <tr>
    <td>2</td>
    <td>15 876</td>
    <td>&lt; 1 second</td>
    <td>&lt; 1 second</td>
    </tr>
    <tr>
    <td>3</td>
    <td>20 00 376</td>
    <td>1 second</td>
    <td>&lt; 1 second</td>
    </tr>
    <tr>
    <td>4</td>
    <td>252 047 376</td>
    <td>2 minutes</td>
    <td>&lt; 1 second</td>
    </tr>
    <tr>
    <td>5</td>
    <td>31 757 969 376</td>
    <td>4 hours</td>
    <td>22 seconds</td>
    </tr>
    <tr>
    <td>6</td>
    <td>4 001 504 141 376</td>
    <td>23 days</td>
    <td>47 minutes</td>
    </tr>
    <tr>
    <td>7</td>
    <td>504 189 521 813 376</td>
    <td>8 years</td>
    <td>4 days</td>
    </tr>
    <tr>
    <td>8</td>
    <td>63 527 879 748 485 376</td>
    <td>1 032 years</td>
    <td>2 years</td>
    </tr>
    <tr>
    <td>9</td>
    <td>8 004 512 848 309 157 376</td>
    <td>130 000+years</td>
    <td>184 years</td>
    </tr>
    </tbody>
    </table>
    <p>X axis – password length in 126 charset</p>
    <p>Y axis – days to crack</p>
    <p><img class="wp-image-16407" src="https://www.deepdotweb.com/wp-content/uploads/2016/11/word-image-21.png" srcset="https://www.deepdotweb.com/wp-content/uploads/2016/11/word-image-21.png 850w, https://www.deepdotweb.com/wp-content/uploads/2016/11/word-image-21-300x185.png 300w" sizes="(max-width: 850px) 100vw, 850px" /></p>
    <p>Blue &#8211; Time in the first case was an experiment with previously mentioned Pentum 4D, 3.2 Ghz processor, affordable processing power for an individual.</p>
    <p>Red &#8211; Time in the second case represents someone that can use 5 000 such processors.</p>
    <p><strong>Conclusion</strong></p>
    <p>Using only lowercase or only uppercase letters and numbers, you need 11 characters long password.</p>
    <p>If you&#8217;re using both lowercase and uppercase letters, numbers and punctuation signs you need 8 characters long password.</p>
    <p>Neither should be predictable enough to be part of a dictionary attack list. I would recommend using 12 characters long password and wide charset.</p>
    <p><strong>Easy way to Manage Strong Passwords</strong></p>
    <p>Different password should be used for each sensitive account because attackers often check all your accounts for password they compromised.</p>
    <p>Password should be at least 12 characters long and include uppercase and lowercase letter, number and a punctuation sign. You can easily meet those requirements by rambling on the keyboard, but it would be difficult to remember passwords.</p>
    <p><strong>Password Manager</strong></p>
    <p>Password manager allows the user to use hundreds of different passwords, and only have to remember a single password, the one which opens the encrypted password database. Needless to say, this single password should be strong and well-protected (not recorded anywhere).</p>
    <p>Most password managers can automatically create strong passwords using a cryptographically secure random password generator, as well as calculating the entropy of the generated password. A good password manager will provide resistance against attacks such as key logging, clipboard logging and various other memory spying techniques.</p>
    <p>To generate 1 strong password that&#8217;s easy to remember you can use a great source of entropy &#8211; your mind. Think of a sentence or two. Something like: &#8216;any sentence will do the trick, Just Make Sure It&#8217;s Over 12 Words&#8217;. Password would be: aswdtt,JMSIO12W (first letters in each word). You can remember the sentence easily and recreate the password later. Ideally, the sentence would include a sign and number.</p>
    <p>There are many similar tricks out there if you don&#8217;t like this one.</p>
    <p><strong>Pattern</strong></p>
    <p>So you don&#8217;t like installing a manager? Think of a good pattern that will not be obvious. An example would be: pick 2 numbers: 6,7 and surround your password with 67 and shift+6 = &amp;, shift+7 = /. Also, uppercase 6<sup>th</sup> and 7<sup>th</sup> letter. If your password right now is password -&gt; 67passwORd&amp;/ is easy to remember and strong. The word can be something you can remember for each site, but stay away from obvious like domain name.</p>
    <p>Avoid common letter-number substitutions like o – 0, I &#8211; 1. Here&#8217;s the same link once again, I highly recommend taking a look at <a href="https://wiki.skullsecurity.org/Passwords">common dictionaries</a> and tools attackers may try to use against you.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/passwords/" rel="tag">passwords</a></span> <span style="display:none" class="updated">2016-11-12</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/filipjelic/" title="Posts by Filip Jelic" rel="author">Filip Jelic</a></strong></div>
    </div>
</article>

