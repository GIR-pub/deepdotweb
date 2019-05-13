---
Should We Encourage Bug Discovery And Neglect Pen Testing ?
---
<article class="post-listing post-13413 post type-post status-publish format-standard has-post-thumbnail hentry  tag-bug tag-discovery tag-encourage tag-neglect tag-pen tag-testing">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/michaelatobraaboagye/" title="">Michael Atobra Aboagye </a></span>
    <span>March 10, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/03/10/should-we-encourage-bug-discovery-and-neglect-pen-testing/#comments">1 Comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>You’ve probably heard the term “bug” used many times in movies and TV shows (in the technological sense). Technically a bug simply refers to an error or flaw in a software program.</p>
    <p>Even in in programming languages (as well as scripting languages like bash, pdksh, csh, and so on), an interpreter designates a block of code or script/cmdlets as an error if it is written outside, or is not in line with standard programming/scripting language syntax.</p>
    <p>This is what is commonly referred to as a syntax error; these specific errors are often made by inexperienced programmers.</p>
    <p><strong>In Context</strong></p>
    <p>Here’s an example: an information security engineer may want to write an interactive program to test the minds of pupils below age 14. Students would be asked to reply to each question accordingly.</p>
    <p>In theory, an information security engineer or developer should be aware of the subtle differences between Python 2 and Python 3; the interpretation lies in its syntax.</p>
    <p><strong>Note: there are various ways to check the Python version you have installed, but you can usually do so from the shell. In Kali Linux, for example, use the “python –version” command, or “python” then “import sys” “sys.version”.</strong></p>
    <p>Both programs were written in python, but the interpreter version differs.</p>
    <p>* A <strong>function</strong> is kind of like a mini-program within a program.</p>
    <p>Python 2.7.11 [Program: Students were asked to choose between Yale University and Stanford University.]
    <blockquote><p>1. #This program says hello and asks for a student&#8217;s preference of Ivy League schools.</p>
    <p>2. print(&#8216;Hello world!&#8217;)</p>
    <p>3. print(&#8216;Which do you prefer: Yale or Stanford?&#8217;)</p>
    <p>4. mySchool = input()</p>
    <p>5. print(&#8216;Okay. Thanks a lot!&#8217;)</p></blockquote>
    <p><strong>Python 3</strong></p>
    <blockquote><p>1. #This program says hello and asks for a student&#8217;s preference of Ivy League schools.</p>
    <p>2. print (&#8216;Hello world!&#8217;)</p>
    <p>3. print(&#8216;Which do you prefer: Yale or Stanford?&#8217;)</p>
    <p>4. mySchool = input()</p>
    <p>5. print(&#8216;Okay. Thanks a lot!&#8217;)</p></blockquote>
    <p>The source code of both programs is the same. However, it seems that Python 3&#8217;s syntax differs a lot from Python 2&#8217;s in terms of the input() function call. Python 3&#8217;s input() function call has different results than that of Python 2. This is only one example of where a syntax error can occur.</p>
    <p><strong>Zero-Day Attacks</strong></p>
    <p>Zero-day attacks are borne of unnoticed bugs written into code by software developers. Some of these bugs are too subtle to detect. Is pen testing effective enough to take care of these errors, or do you need to hire the services of black hat hackers specifically to deal with software errors?</p>
    <p>The reason for this is that most white-hat hackers tend to use traditional methods of pen testing. Black hats, on the other hand, are more likely to try unorthodox methods, such as modifying blocks of code just to divert the original purpose of a program.</p>
    <p>For instance, on the Tor network, there are many clone sites of legitimate .onion sites. Malicious code written into a clone site may attempt to steal login details from users or victimize them in other ways. A black hat hacker would be more knowledgeable about methods to expose and shut down such sites (and even retaliate against those who set them up), based on experience.</p>
    <p>(So I would rather recommend a black hat hacker than a white hat hacker for such tasks.)</p>
    <p><strong>Art of Penetration</strong></p>
    <p>The art of penetration testing is applied when the owner(s) of a webpage or software application have been assured of total security. The mission of pen testing is not to avail all attack vectors or open ports, which could give access to the internal network or system. Just a single open port (which should have been closed in the first place) could make things work for pen tester(s). Or just a single mistake within a module could enable a zero-day attack.</p>
    <p>Bug discovery, on the other hand, refers to in-depth scientific investigation of a software application or web server; it operates more thoroughly than pen testing.</p>
    <p>A pen tester would not, in theory, bother to excavate the nitty-gritty of a web server (i.e. there is no need to check out the database engine of web servers based on JSON). Other techniques of modern day attacks like man-in-the-middle attacks (MitM), distributed denial of service (DDoS), ARP poisoning, or even social engineering could aid a pen tester in accomplishing her mission. Other attack vectors won&#8217;t be needed if these forms of cyber-attacks could launch him into the integral part of the server.</p>
    <p><strong>We&#8217;ve Been Compromised!</strong></p>
    <p>A couple of years ago, bugs like the infamous Heartbleed affected many software vendors. Heartbleed compromised the transport layer security (TLS) which secures communication between two parties; a Heartbleed attack is somewhat like an MitM attack. Because of this, OpenSSL was compromised.</p>
    <p>The bug discovered in the OpenSSL not only affected protected data, but also allowed hackers to access web pages with ease, until it was discovered that Heartbleed was the main cause.</p>
    <p>The difference between bug discovery and pen testing lies in using &#8220;in-depth&#8221; methods. In this context, &#8220;in-depth&#8221; defines bug discovery and pen testing altogether. Bug discovery depends on pen testing to maintain security awareness, whilst pen testing depends on bug discovery to ensure that all open ports (which need to be closed) are dealt with efficiently.</p>
    <p><strong>Know Your Role&#8230;And Shut Your Mouth!</strong></p>
    <p>Initially, I explain that penetration testing does not excavate the nitty-gritty of a software product or a web page. The chief advantage of pen testing is to test whether a software product or a webpage is secure enough against attacks from external networks. Vulnerability auditing is the closest to bug discovery (because it does more in-depth checking than pen testing, but is ineffective when compared to the latter).</p>
    <p>Unit and system testing are the best potential candidates to work in tandem with these other methods. Unit testing tends to focus on the correctness of a single product, whilst system testing is primarily concerned with the correct operation of the entire system.</p>
    <p>So, the coupling of both unit and system testing is about as close as you can get to bug discovery. Although both modes of testing differ in terms of jurisdiction, efficiency is achieved.</p>
    <p>Whether developers should rely on pen testing, unit testing, or system testing to prevent a zero-day attack launch, the bottom line is efficiency.</p>
    <p>The final question remains: are any of them efficient enough? Or will the attackers always be one step ahead?</p>
    <p>&nbsp;</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/bug/" rel="tag">bug</a> <a href="https://www.deepdotweb.com/tag/discovery/" rel="tag">discovery</a> <a href="https://www.deepdotweb.com/tag/encourage/" rel="tag">encourage</a> <a href="https://www.deepdotweb.com/tag/neglect/" rel="tag">neglect</a> <a href="https://www.deepdotweb.com/tag/pen/" rel="tag">pen</a> <a href="https://www.deepdotweb.com/tag/testing/" rel="tag">testing</a></span> <span style="display:none" class="updated">2016-03-10</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/michaelatobraaboagye/" title="Posts by Michael Atobra Aboagye" rel="author">Michael Atobra Aboagye</a></strong></div>
    </div>
</article>

