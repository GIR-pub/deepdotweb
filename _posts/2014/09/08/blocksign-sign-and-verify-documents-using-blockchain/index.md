---
BlockSign: Sign and Verify Documents Using Blockchain"
---
<article class="post-listing post-6932 post type-post status-publish format-standard has-post-thumbnail hentry  tag-blockchain tag-blocksign tag-documents tag-sign tag-verify">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/zubairmuadh/" title="">Zubair Muadh </a></span>
    <span>September 8, 2014</span>
    
    <span><a href="https://www.deepdotweb.com/2014/09/08/blocksign-sign-and-verify-documents-using-blockchain/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p><strong>What is BlockSign?          </strong></p>
    <p>BlockSign is a platform which runs on the Blockchain that cryptographically signs documents and timestamps them allowing them to be later verified on the internet</p>
    <p><strong>How does it work?</strong></p>
    <p>BlockSign is a web application from the user’s perception as the upload their document add their signature which is their name, email address and time/date of the signature which is added to the document.</p>
    <p>BlockSign works by utilizing a 40-byte slot which exists in every Bitcoin block called OP_RETURN. It’s a slot that’s used to store miscellaneous data as well as messages. BlockSign creates a cryptographic hash of the document and stores it in the OP_RETURN slot.</p>
    <p>With the cryptographic hash logged in the Blockchain and when it’s time to verify the document they search the Blockchain for the string.</p>
    <p>BlockSign store a verification record on behalf their clients and relies on email authentication for users which isn’t very reliable, they plan to move onto private keys on the long term.</p>
    <p>The only the user who uploaded the document can unlock it as it’s tied to the users location</p>
    <p><strong>Bloating the Blockchain?</strong></p>
    <p>BlockSign uses the OP_RETURN slot which has a limit of 40 bytes, when you compare it to the average transaction size of 570 bytes it’s 7% of the average block size. Approximately a quarter of blocks use the OP_RETURN slot when you look at the recent 80 blocks.</p>
    <p>BlockSign also uses only 32-bytes and doesn’t use the entire slot so wouldn’t bloat the Blockchain much.</p>
    <p><strong>Security</strong></p>
    <p>People would be able to verify the document by uploading the document and verifying it or by having the link and verifying it. This enables them to see that the document is verified by they won’t be able to see the contents of the documents. This enables privacy for documents such as life insurance etc. Only email address that you’ve allowed would be able to see the document. Any changes of to the document at a later date will cause a different cryptographic hash of the document to be created and therefore it wouldn’t be able to be verified.</p>
    <p><strong>BlockSign vs Adobe EchoSign</strong></p>
    <p>Adobe’s EchoSign is a platform that allows its clients too electronically sign documents and track any changes to the document and archive them.</p>
    <p>EchoSigns Advantages.</p>
    <ul>
    <li>EchoSign is well established with a good reputation.</li>
    <li>It handles 3 Million signatures a month</li>
    <li>All stored on the cloud, safe from any tampering.</li>
    </ul>
    <ol>
    <li>BlockSign uses the Blockchain and uploads the cryptographic hash of the signed document. This automatically provides protection from any attacks as the Hash is protected by the Bitcoin network.</li>
    <li>Since the Bitcoin network is decentralised this by default protects BlockSign from any attacks as attackers would have to attack the Bitcoin network (Which is protected by over 1 Petahash hashrate) whereas EchoSign relies on the Adobe servers, if they go down then you can’t sign or verify your documents.</li>
    <li>You cannot independently verify documents with EchoSign whereas with BlockSign if you have the cryptographic hash of the document you can search for t on the Blockchain and verify the timestamp and all for yourself.</li>
    </ol>
    <p><strong>Pricing</strong></p>
    <p>Adobe EchoSign: $14.95 per Month for a single user to sign and upload documents.</p>
    <p>BlockSign: First 5 signatures are free, every 50 signatures afterwards are $5.</p>
    <p>BlockSign is providing a cheap alternative to e-signing over the current industry leaders, using Blockchain technology to do so. BlockSign isn’t alone in this, due to the open source nature of the Bitcoin source code other projects are also rising such as Euthereum which uses the Blockchain technology to facilitate the many things including smart contracts providing BlockSign with competition.</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/blockchain/" rel="tag">blockchain</a> <a href="https://www.deepdotweb.com/tag/blocksign/" rel="tag">blocksign</a> <a href="https://www.deepdotweb.com/tag/documents/" rel="tag">documents</a> <a href="https://www.deepdotweb.com/tag/sign/" rel="tag">sign</a> <a href="https://www.deepdotweb.com/tag/verify/" rel="tag">verify</a></span> <span style="display:none" class="updated">2014-09-08</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/zubairmuadh/" title="Posts by Zubair Muadh" rel="author">Zubair Muadh</a></strong></div>
    
