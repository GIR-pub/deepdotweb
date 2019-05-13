---
Bitcoin Brain Wallets : Hackers&#8217; Heaven!
---
<article class="post-listing post-20486 post type-post status-publish format-standard has-post-thumbnail hentry  tag-bitcoin tag-brain tag-hackers tag-heaven tag-wallets">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>June 9, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/06/09/bitcoin-brain-wallets-hackers-heaven/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>Since its launch in 2009, Bitcoin has by far been the most successful cryptocurrency, attracting a considerable magnitude of research during the past few years. Just like every other cryptocurrency, authorization of transfer of bitcoins from an account to the other relies on ECDSA digital signatures. The rising popularity of bitcoin, especially among non-tech savvy individuals and populations who have no experience with cryptography based applications, have yielded a substantial number of users struggling to deal with private keys.</p>
    <p>Brain wallets refer to private cryptographic keys that are despotically derived from passwords. Alternatively to other means for managing bitcoin&#8217;s cryptographic keys, such as <a href="https://www.deepdotweb.com/2017/05/12/tutorial-store-bitcoins-securely-using-cold-storage/">securing them on a PC</a>, or hardware wallets, brain wallets are much more convenient to users who can spend their coins via simply entering their passwords. Due to the fact that they don&#8217;t involve permanent storage of their private keys on a device, brain wallets cannot be phished by malware. However, <a href="https://www.deepdotweb.com/2016/02/18/hackers-make-103000-cracking-bitcoin-wallets/">a brain wallet is a very insecure way to store bitcoins</a>, as an attacker who can successfully guess a user&#8217;s password, can steal them instantly.</p>
    <p><img class="wp-image-20496 aligncenter" src="/imgs/2017/06/word-image-32.jpeg" srcset="/imgs/2017/06/word-image-32.jpeg 470w, /imgs/2017/06/word-image-32-209x300.jpeg 209w" sizes="(max-width: 470px) 100vw, 470px" /></p>
    <p>Attackers successfully guessing a password can test if it matches any brain wallet via searching for usage of the derived public key on the blockchain, which records all transactions. <a href="https://link.springer.com/chapter/10.1007%2F978-3-662-54970-4_36">A recently published paper</a> presented the first large scale analysis of brain wallet usage among bitcoin users. The researchers replicated the password guessing attack via testing candidate passwords non-invasively to detect the ones that have been historically used as a brain wallet bitcoin addresses.</p>
    <p>Let&#8217;s summarize this study, which includes some interesting results:</p>
    <p><strong>How were candidate passwords picked up and used?</strong></p>
    <p>The researchers built an enormous group of passwords, which were derived from various online sources. They included previous password leaks, including Yahoo!, Rockyou and LinkedIn; words and derived phrase lists, including Wikiquote and the English Wikipedia; and information derived from bitcoin community forums mainly Bitcointalk.org. Collectively, an average of 300 billion passwords were used in guessing bitcoin&#8217;s brain wallets. The used word lists were derived from:</p>
    <p>1. Lists of English words packaged with Ubuntu 12.04.</p>
    <p>2. Urban Dictionary: Phrases and terms derived from The online <a href="http://www.urbandictionary.com/">Urban Dictionary</a> via <a href="https://github.com/inieves/urban-dictionary-scraper/blob/4a86fd9ef4c2f8812dc78f5862c327912213436a/dict/UrbanDictionary.txt">the Urban Dictionary Scrapper</a>. All pairs of terms were checked using the &#8220;combinator&#8221; tool.</p>
    <p>3. Combination of 2 words; 2 English words, or 1 English word plus 1 Slang/Urban word via the &#8220;combinator&#8221; tool.</p>
    <p>4. WikiQuotes: English, Russian, German and Spanish quotes from April, 2013.</p>
    <p>5. Song titles and lyrics bought from Andymoore.info</p>
    <p>6. <a href="https://xkpasswd.net/s/">xkcd</a>: Lists were retrieved on July 10th, 2014</p>
    <p>Additionally, the researchers used brute force attack and also tried modified passwords of previously cracked bitcoin brain wallets.</p>
    <p>Afterwards, the SHA256 password hash was used as the private key and the matching public key was generated using speedups to the secp256k1 curve library. Then, all unique bitcoin addresses were extracted via znort987&#8217;s block parser. All found addresses were then added to a bloom filter for lookup and a list for false positive detection was created. All bitcoin addresses, which were generated from cracked passwords, were compared to the boom filter and positive results were confirmed against the sorted list. After detecting all used bitcoin brain wallet addresses, this information was supplemented by querying these addresses using the blockchain.info API to retrieve accurate timestamps for all transactions.</p>
    <p><strong>Results:</strong></p>
    <p>The researchers discovered 884 different brain wallets with 845 different passwords beginning from the launch of bitcoin all the way down to August, 2015. Totally, these wallets had 1,806 BTC. Even though most of these brain wallets had small amounts of money (6% of them had what is worth around $100), 10 brain wallets had what is equal to 85% of the total amount.</p>
    <p>As a brain wallet&#8217;s address is formulated from the password, an attacker could possibly crack the password and drain the wallet of its coins. Interestingly enough, 863 of the found 884 brain wallets were drained by attackers (97.6%) which reflects the insecurity of brain wallets. 50% of the hacked wallets were drained within less than 21 minutes, but almost all wallets were drained within less than 24 hours.</p>
    <p>98% of the undermined brain wallets were drained at least once. Precisely, the researchers detected 1,895 separate draining events that hit 863 wallets; 69% were drained only once, 19% were drained twice and 1.9% were drained at least ten times. Drains occur rapidly due to the use of bots, by attackers, to monitor new coins deposited into previously known brain wallets. Also, the attacker will instantly send the coins to his/her address, after finding a vulnerable brain wallet, often with high miners&#8217; fees to tempt them to confirm the transaction quickly.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/bitcoin/" rel="tag">bitcoin</a> <a href="https://www.deepdotweb.com/tag/brain/" rel="tag">brain</a> <a href="https://www.deepdotweb.com/tag/hackers/" rel="tag">hackers</a> <a href="https://www.deepdotweb.com/tag/heaven/" rel="tag">heaven</a> <a href="https://www.deepdotweb.com/tag/wallets/" rel="tag">wallets</a></span> <span style="display:none" class="updated">2017-06-09</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

