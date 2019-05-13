---
Why CSRF Is Not The Same As XSs"
---
<article class="post-listing post-14564 post type-post status-publish format-standard has-post-thumbnail hentry  tag-csrf tag-xss">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/vb/" title="">V.B </a></span>
    <span>June 23, 2016</span>
    
    <span><a href="https://www.deepdotweb.com/2016/06/23/csrf-not-xss/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    
    <p>Since <a href="https://hackerone.com/">HackerOne</a> came into the system to create close connection between white hats and tech. companies (primarily for security reasons), we have come across terminologies like <strong>CSRF</strong>, <strong>XSS</strong>, <strong>SQLi </strong>and the <strong>Poisoned null byte</strong>. These terminologies are part of today’s most common, harmful vulnerabilities affecting web applications.  Major tech. companies (<strong>Google</strong>, <strong>PayPal</strong>, <strong>Uber</strong>, and <strong>Twitter</strong>) have benefited from white hats or security researchers like <a href="https://twitter.com/rafaybaloch">@Rafaybaloch</a><strong>,  </strong><a href="https://hackerone.com/filedescriptor">filedescriptor </a>, and <strong>Egor Hakimov’s </strong> willingness to help detect hidden bugs or technical mistakes yet unknown to  developers and programmers.</p>
    <p>However, it seems outsiders still find it difficult to differentiate between XSS and CSRF.  We should not interchange XSS with CSRF.  <strong>XSS and CSRF</strong> don’t apply to each other.</p>
    <p><strong>Definition of XSS</strong></p>
    <p>XSS simply means cross site scripting.  XSS is a code attack method used by hackers to inject malicious script.</p>
    <p>In XSS attack, attackers exploit the trust the user has for a particular webiste. Generally like all injection attacks, XSS takes advantage of the fact that browser’s can’t tell a valid markup. The attackers do not directly target their victims. They look for vulnerability in a website to inject and deliver malicious scripts for users.</p>
    <p>Attackers inject malicious javascript into one of the pages that users download from the website. This is very possible if the website allows user inputs. A malicious Javascript can reveal users sensitive information because Javascript has access to some of the user’s information, such as cookies.</p>
    <p>An attacker can access  users cookies associated with the website via <strong>document.cookie</strong>,  post them to his own server and use them to extract and access sensitive information like session ID’s.  Attackers can also steal credit card details, bypass restriction in websites and perform denial of service attacks.</p>
    <p>Therefore in XSS attack, attackers look out for vulnerability in a website to inject malicious Javascript and also exploit the trust the user has for a particular website.</p>
    <p><strong>Definition Of CSRF </strong></p>
    <p>CSRF simply means Cross Site Request Forgery. In a CSRF attack, an attacker exploits a website’s assumption that all requests originate from a user’s   browser.  Logically, a website assumes that all requests that originate from the browser are those of the user.</p>
    <p>The attack is possible when the targeted application does not verify and validate the origin of the request. A website relies only on the existence of a valid session between the user’s browser and the application server.</p>
    <p>Attackers depend on <strong>active sessions</strong> to implement CSRF attack successfully.  An attacker can use a user’s browser session to send valid report (via <strong>GET method</strong> or even a <strong>POST method</strong> occasionally) to a web server to perform certain actions in a user’s account in favour of the attacker.</p>
    <p>Facebook, Twitter, and slack have created ‘my<strong> account page’</strong>, or ‘<strong>payment settings’</strong> for users on their platform to store as well as change their details – <strong>Password</strong>, <strong>Age, Email address</strong>, and <strong>Credit card</strong> <strong>credentials</strong>.</p>
    <p>If users can change information on a webpage via both <strong>GET </strong>and <strong>POST</strong> method, then it is extremely possible for an attacker to forge request of a user’s mail address.  In a CSRF attack, attackers take advantage of or abuse a website’s zero intelligence to forge a request. CSRF attack entails forgery.</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/csrf/" rel="tag">csrf</a> <a href="https://www.deepdotweb.com/tag/xss/" rel="tag">xss</a></span> <span style="display:none" class="updated">2016-06-23</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/vb/" title="Posts by V.B" rel="author">V.B</a></strong></div>
    
