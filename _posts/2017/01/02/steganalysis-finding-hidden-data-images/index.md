---
Steganalysis: finding hidden data in Images
---
<article class="post-listing post-17272 post type-post status-publish format-standard has-post-thumbnail hentry  tag-data tag-finding tag-images tag-steganalysis">
    
    <div class="post-inner">
    
    
        
    <span>Posted by: <a href="https://www.deepdotweb.com/author/babysnoop/" title="">babysnoop </a></span>
    
    
    <span>January 2, 2017</span>
    
    
    <span><a href="https://www.deepdotweb.com/2017/01/02/steganalysis-finding-hidden-data-images/#comments">3 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    
    
    <p>The art of hiding secret messages in innocuous looking objects, known as steganography was introduced in a <a href="https://www.deepdotweb.com/2016/11/13/steganography-hiding-data-images/">DDW article</a> last month, featuring a tutorial on a useful tool that embeds data (usually text messages) into JPEG images – without making it obvious to the naked eye.</p>
    <p>Today I would like to discuss steganography&#8217;s counterparty, namely steganalysis – the art of uncovering hidden communication and exposing the use of steganography. Steganalysis is not to be confused with the more well known cryptanalysis which focuses on decrypting a message that has already been intercepted. When performing Steganalysis you do not know where to look, you can&#8217;t identify the channel of communication which could be a stego image (image carrying a hidden message) uploaded onto facebook, a torrent of a star wars flick (which could carry a massive amount of hidden data – even a small video) &#8230; the possibilities are endless.</p>
    <p>In 2001, well known security researchers <a href="https://twitter.com/NielsProvos">Niels Provos</a> and Peter Honeyman released a <a href="http://www.citi.umich.edu/u/provos/papers/detecting.pdf">study</a> whereby a distributed computing framework was used to analyse two million images uploaded to eBay and one million from USENET archives. Sadly no hidden messages were found – however, this study was made 15 years ago and the availability of steganography tools has increased and steganalysis methods have become a lot more sophisticated.</p>
    <p>It is important to note that steganalysis merely constitutes the decision on whether or not a particular object contains a payload i.e. hidden information. A particular steganography tool or method is know to be broken, if it can be steganalysed with a success rate higher that 50% i.e. better than random guessing. Of course researchers are trying to push detection performance far beyond 50%! Rémi Cogranne from UTT published a <a href="http://remi.cogranne.pagesperso-orange.fr/papiers/THT_WIFS_2014_JPEG_Model_OutGuess.pdf">research paper</a> in 2014 claiming to achieve a detection performance of JPEG image steganography between 80 and 93 percent, depending on the amount of data hidden in the image. Just like at an airport security screening, it is easier to detect someone trying to smuggle a machete as opposed to a pen knife.</p>
    <p>Remi and Niels are by far not the only researchers focusing on steganalysis and new white papers are published constantly on not only image but also video and audio steganalysis. Unfortunately easy to use steganalysis tools seem quite hard to come by or are out of date. A search for <a href="https://github.com/search?utf8=✓&amp;q=steganalysis">&#8216;steganalysis&#8217; on Github.com</a> currently returns a dire list of 38 projects. This being said, there is no need to loose hope, because if we look at the steganography world, there are lots of high quality tools available that are easy to use such as <a href="http://steghide.sourceforge.net/">Steghide</a>, <a href="https://zooid.org/~paul/crypto/jsteg/">JSteg</a> and <a href="http://linux01.gwdg.de/~alatham/stego.html">JPHS</a> to name a few that specialize on JPEG embedding alone.</p>
    <p>Now that we have a better understanding of steganalysis lets look at how we might go about actually finding some hidden data in images.</p>
    <ol>
    <li><strong>Choosing where to look</strong></li>
    </ol>
    <p>In order to steganalyse images, we need to first get our hands on them. People using steganography will try to make it hard for outsiders to find out exactly who they are communicating with. To achieve this, they would upload a stego image to a public social network or image sharing site. Lets choose twitter.com as our target.</p>
    <ol>
    <li><strong>Crawling the target</strong></li>
    </ol>
    <p>Because browsing Twitter and downloading random images by hand will take forever, we employ something called a web crawler (otherwise known as scraper), a computer program that browses or &#8216;crawls&#8217; through web pages systematically. Usually this is performed by search engines for web indexing purposes, but anyone can create their own crawler that performs some custom task. We could create a crawler using the Ruby programming language in combination with a HTML library such as <a href="http://www.nokogiri.org/">Nokogiri</a> to crawl Twitter and download any JPEG image files encountered. Of course we could target our crawler to say all followers of <a href="https://twitter.com/torproject">@torproject</a> because we think those people are likely to use steganography. Our crawler should have no problem downloading all these peoples image uploads, which could easily go into the millions of images.</p>
    <ol>
    <li><strong>Running steganalysis tool</strong></li>
    </ol>
    <p>Once the crawler has finished its job, it is time to find a suitable steganalysis tool. As most images on the web are in JPEG format, we are going to choose a tool that specializes on JPEG&#8217;s. It is always a good idea to use multiple tools that use different steganalysis techniques and combine the output to give a more objective result. Binghamton University&#8217;s Digital Data Embedding Laboratory has published state of the art <a href="http://dde.binghamton.edu/download/feature_extractors/">JPEG steganalysis tools</a>, however they need to be combined with an AI framework and the ones we have tested unfortunately only work on greyscale images.</p>
    <p>An up to date and ready to use JPEG steganalysis tool would surely be very much welcomed by many enthusiasts. <img class="wp-image-17276 aligncenter" src="/imgs/2016/12/word-image-137.png" srcset="/imgs/2016/12/word-image-137.png 800w, /imgs/2016/12/word-image-137-300x51.png 300w" sizes="(max-width: 800px) 100vw, 800px" /></p>
    <ol>
    <li><strong>Extract hidden messages from suspicious images</strong></li>
    </ol>
    <p>Once we have identified the images that are likely to have hidden information (know as stego images), we will try to extract the hidden message. Because there are different mechanisms used to embed a message into an image, we need to try out all of them (or at least the most popular embedding techniques). Additionally it is likely that we will discover an encrypted message that will need to be hacked via dictionary attack (script that tries out millions of likely passwords) for example.</p>
    <p>The art of steganography is far from mature and most people haven’t even heard of it. However the number of monthly downloads of Steghide (arguably the most popular tool for image steganography) has <a href="https://sourceforge.net/projects/steghide/files/stats/timeline?dates=2015-08-14+to+2016-11-30">doubled from 3,237 to 7,479 between October and November 2016</a> possibly due to increase fear of surveillance following Americas election results (37% of downloads originate from the US according to sourceforge.net). Naturally an increase in steganography activity will spark further interest in steganalysis, so we can look forward to more developments and stego tools in the near future.</p>
    <p><img class="wp-image-17277 aligncenter" src="/imgs/2016/12/word-image-138.png" srcset="/imgs/2016/12/word-image-138.png 974w, /imgs/2016/12/word-image-138-300x127.png 300w" sizes="(max-width: 974px) 100vw, 974px" /></p>
    <p>babysnoop &#8211; @<a href="https://twitter.com/babysn00p">babysn00p</a></p>
    
    
    </div><!-- .entry /-->
    <a href="https://www.deepdotweb.com/tag/data/" rel="tag">data</a> <a href="https://www.deepdotweb.com/tag/finding/" rel="tag">finding</a>  <a href="https://www.deepdotweb.com/tag/images/" rel="tag">images</a> <a href="https://www.deepdotweb.com/tag/steganalysis/" rel="tag">steganalysis</a></span>				<span style="display:none" class="updated">2017-01-02</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/babysnoop/" title="Posts by babysnoop" rel="author">babysnoop</a></strong></div>
    
    
    </div><!-- .post-inner -->
</article><!-- .post-listing -->

