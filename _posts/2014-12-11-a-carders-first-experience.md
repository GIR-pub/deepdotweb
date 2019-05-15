---
title: "A Carder&#8217;s First Experience"
---

Posted by: Kiell

<span>December 11, 2014</span>

<p><em><span style="text-decoration: underline;">We do not support carding</span>! This is for educational purposes only &#8211; and reflect the author&#8217;s own experience and views only.</em></p>
<p>At the time of this story, I was new to carding. Saying that I was “new” is a bit of an understatement. I had never used any Darknet markets, and I had barely any experience with Bitcoin. I had a lot to learn. This was my experience.</p>
<p>There are currently few major carding forums such as – Tor Carding Forums (TCF) and Rescator for example. Since Tor Carding Forums had a fee for registration, I decided to use Rescator. The website requires an account to access any listings or to make purchases, but it does not require any payment for registration.</p>
<p>There are two things that are unique about Rescator: first, it is centralized. As the rumor goes, Rescator was a reputable user from a now-defunct Russian forum. After this forum was infiltrated by law enforcement, he decided to open his own dedicated shop. Many of the recent security breaches, including Target and J.P. Morgan, can be traced back to a small group of people who include Rescator. Second, there is no escrow system. Once you release funds, there is very little you can dispute. The site&#8217;s only dispute resolution is in the form of tickets. I had to put a lot of trust in a single person.</p>
<p>There is also some terminology that is pretty exclusively used on carding forums. “Dumps” are the collections of data that are being sold. These are exactly what they sound like – disorganized dumps of all data that was collected. A “base” is a collection of dumps that were all skimmed from the same source. The data from the Target hack would be a base, while the data from the Home Depot hack would be another base. The names of these bases vary, ranging from names like, “Ronald Reagan” to “Beaver Cage”. The amount of data that you can expect to still be usable and valid is called the “validity rate”.</p>
<p>In order to purchase a dump, I had to transfer money into an on-site account. This is where Bitcoin came into the picture. I decided not to tumble my Bitcoins. Many people advocate that you must tumble your Bitcoins. The issue, however, is that tumbling Bitcoins does not make them impossible to trace – it just makes them difficult to trace. This is what we call, “security through obscurity”. I decided that, to be safe, I had to make my Bitcoins <em>impossible</em> to trace. Here was my plan: All Bitcoin transactions are publicly recorded on the blockchain. As long as you are trading on the blockchain, all transactions are connected. Therefore, I had to break the chain of transactions. To do this, I used a normal Bitcoin exchange. I converted my Bitcoin to Litecoin, then back into Bitcoin.</p>
<p><a href="/imgs/2014/10/listings.jpg"/>
<p>The act of purchasing was fairly straightforward. The website itself was very user-friendly. There was a basic filter that could be used to sort by base, country of origin, type of card, among other criteria. When I decided on the card information I wanted to purchase, I added it to my cart. At this point, in order to release funds and receive the dump, I simply clicked a “purchase” button. From the time a base is released, the validity rate will gradually decrease. After a security breach is discovered, companies and account holders begin to close accounts, and the data quickly becomes useless. Therefore, I chose a recent base: American Sanctions, information collected during the recent Home Depot breach.</p>
<p><a href="/imgs/2014/10/order1.jpg"/>
<p><a href="/imgs/2014/10/track1-track2.jpg"/>
<p>This is what I got once I received my order. This, at first, was a bit confusing.</p>
<p>Here&#8217;s how card technology works: There are two to three tracks on the magnetic strip of a credit or debit card. Track 3 is sometimes not even present on cards, and most major networks only use tracks 1 and 2.</p>
<p>This is the format for Track 1: account number^Lastname/Firstname^expiration date(YY/MM)::bank key(3 numbers)::discretionary data or security key(in this case it was a CVC code &#8211; 3 numbers)::Longitudinal Redundancy Check.</p>
<p>This is the format for Track 2:</p>
<p>account number=expiration date(YY/MM)::service code(3 numbers)::discretionary data or security key (3 numbers)::Longitudinal Redundancy Check</p>
<p>A lot of the information from Track 1 is repeated on Track 2.</p>
<p>Now we can make my example meaningful:</p>
<p>Lets divide Track 1: 4631588<strong>xxxxx//&lt;</strong>lastname&gt;,&lt;firstname&gt;.//1601//101//163//03100495000000</p>
<p>Our primary account number is: 4631588<strong>xxxxx</strong></p>
<p>Our account holder is: &lt;lastname&gt;&lt;firstname&gt;</p>
<p>Our Expiration date is: 01/16</p>
<p>Our service code is: 101</p>
<p>Our CVC code is: 163</p>
<p>Once I had organized this information, it became a matter of cashing out the card.</p>
<p>The difficulty of actually using this information is figuring out how to use it anonymously. I decided that once again, I would turn to Bitcoin. There are several things a website asks you for when you use a debit or credit card: the primary account number, the expiration date, and the security (CVC) code. Since all of this was included in the dump, I could use the card online without any problems. I decided to purchase gift cards, which I would then sell for Bitcoins. After doing my Bitcoin &gt; Litecoin &gt; Bitcoin tumbling scheme mentioned earlier, I could deposit these into my wallet. However, I never got that far. My plan would have been successful&#8230;had the card holder&#8217;s account not been closed.</p>
<p>Overall, my experience was very positive. At first, I was just happy that I hadn&#8217;t gotten scammed; and after banging my head over my desk a few times, I ended up not being too upset over the card&#8217;s failure. After all, if I had purchased a card with an option for a refund, I would have been successful. Using the information, while an extensive process, was definitely doable. It worked very much like any market, with many helpful and honest members.. The people involved were not just criminals looking for easy money; they were interested in the technology and were more than willing to help me. The carding community was just as diverse as any community, and I discovered it was just as tight knit.</p>

Updated: 2014-12-11    
