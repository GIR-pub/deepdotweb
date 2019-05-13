---
BIX Certificates &#8211; Cryptographic Tokens Promoting Anonymity For Blockchain Transactions
---
<article class="post-listing post-17326 post type-post status-publish format-standard has-post-thumbnail hentry category-deepdot-news tag-anonymity tag-bix tag-blockchain tag-certificates tag-cryptographic tag-promoting tag-tokens tag-transactions">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>January 5, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/01/05/bix-certificates-cryptographic-tokens-promoting-anonymity-blockchain-transactions/#respond">Leave a comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>With the advent of the blockchain technology and the use of the internet along with mobile technologies, a brand new group of transactions and applications, which <a href="https://www.deepdotweb.com/2015/06/15/guide-anonymity-and-privacy-for-advanced-linux-users/">rely on anonymity</a>, is increasingly gaining interest and acceptance. Ingenious payment systems, blockchain based voting, digital notaries, medical services and electronic auctions represent examples of these new applications.</p>
    <p>Beside anonymity, such transactions and applications will also have to offer traditional security services including identification, authentication, users&#8217; authorization and transaction protection. Effective provision of these services in means that promote anonymity represents a tough challenge, due to the fact that all security services depend on an explicit process of identification and authentication of users. To overcome this challenge and offer web applications that promote security as well as anonymity, <a href="http://ledger.pitt.edu/ojs/index.php/ledger/article/view/27/52">a group of researchers published a paper</a> a few days ago that introduced an innovative cryptographic token, which they named &#8220;BIX certificates&#8221;.</p>
    <p>&#8220;BIX&#8221; stands for &#8220;Blockchain Information Exchange&#8221;. The purpose of BIX certificates is similar to that of X.509 certificates; to offer secure applications and transactions that provide high levels of anonymity.</p>
    <p><strong>The Components and Structure of BIX Certificates:</strong></p>
    <p>According to the below diagram, a BIX certificate is formed of the following components:</p>
    <p><img class="wp-image-17331 aligncenter" src="https://www.deepdotweb.com/wp-content/uploads/2017/01/bix-certificates-png.png" alt="BIX certificates.PNG" srcset="https://www.deepdotweb.com/wp-content/uploads/2017/01/bix-certificates-png.png 483w, https://www.deepdotweb.com/wp-content/uploads/2017/01/bix-certificates-png-300x272.png 300w" sizes="(max-width: 483px) 100vw, 483px"/></p>
    <p><strong>1- <em>Header:</em></strong> is composed of 3 attributes:</p>
    <p>&#8211; <em>Sequence number: </em>it corresponds to the certificate&#8217;s serial number and denotes its relative position with respect to other BIX certificates within the context of a BCL instance.</p>
    <p>&#8211; Version: It includes the piece of code that determines the type of a given BIX certificate.</p>
    <p>&#8211; Date/time: It denotes the date and time stamp of the issuing of the certificate. It marks the start of the validity period of the certificate.</p>
    <p><strong>2- Subject:</strong> is comprised of 4 attributes:</p>
    <p>&#8211; Subject BIX ID: a global identifier that is unique for each owner of a certificate.</p>
    <p>&#8211; Date/time: it denotes the date and time stamp of creation of the public key and its corresponding private key.</p>
    <p>&#8211; Algorithm identifier: it is an attribute that determines the <a href="https://www.deepdotweb.com/2016/07/03/introduction-cryptography-part-3/">cryptographic algorithm</a> that was used with the corresponding public key.</p>
    <p>&#8211; Public key: this is the public key that corresponds to the owner of the certificate.</p>
    <p><strong>3- Subject Signature: </strong></p>
    <p>it includes the signature over the &#8220;Subject&#8217;s&#8221; attributes using the certificate&#8217;s private key.</p>
    <p><strong>4- Issuer:</strong></p>
    <p>It includes the same attributes of the &#8220;Subject&#8221; but they point to the BIX user who issued the certificate.</p>
    <p><strong>5- Issuer signature:</strong></p>
    <p>This is a self-signed form of digital signature over the attributes of the issuer.</p>
    <p><strong>6- Backward cross-signature:</strong></p>
    <p>This attribute is comprised of 2 signatures; one for the Issuer and the other for the &#8220;Subject&#8221; over the 3 attributes of the &#8220;Header&#8221; concatenated with the &#8220;Subject&#8217;s&#8221; hash and the &#8220;Issuer&#8217;s&#8221; hash.</p>
    <p><strong>7- Next subject:</strong></p>
    <p>These are the same as the 4 &#8220;Subject&#8217;s&#8221; attributes but correspond to the BIX user who was certified by the BIX user who issued the certificate.</p>
    <p><strong>8- Next subject signature:</strong></p>
    <p>This represents the same attribute as the Subject signature, but it is created by the certificate&#8217;s issuer over the data of the Next subject</p>
    <p><strong>9- Forward cross-signature:</strong></p>
    <p>This contains 2 signatures, one corresponding to the Issuer and the other to the Next subject, over the 3 attributes of the &#8220;Header&#8221; concatenated with the hashes of both the Issuer and the Next subject.</p>
    <p><strong>10- Extensions: </strong></p>
    <p>This attribute has ObjectID which includes additional attributes that could be utilized in other applications of BIX certificates.</p>
    <p><strong>Difference between X.509 and BIX certificates:</strong></p>
    <p>One of the main goals of BIX certificates is to provide users with anonymous identities and corresponding public keys that allow users to be verified for correctness and/or ownership. These also represent the main goals of X.509 certificates. Accordingly, we can assume that BIX certificates are quite similar to X.509 certificates. There are two main differences between BIX certificates and X.509 certificates:</p>
    <p>&#8211; User credentials that are included in BIX certificates are totally anonymous.</p>
    <p>&#8211; BIX certificates are not issuable by any form of intermediary or third parties.</p>
    <p>Although an X.509 certificate has a &#8220;serial number&#8221; attribute that refers to a specific X.509 certificate among those issued by a given &#8220;certification authority&#8221;, BIX certificates are only issued by members of a BIX community and collectively aggregated in a blockchain that represents a certificates&#8217; ledger, so there is no need for a serial number to categorize certificates on issuer basis. Nevertheless, BIX certificates have a &#8220;Sequence Number&#8221; attribute that aids in referencing and other purposes.</p>
    <p>A BIX certificates has a &#8220;Subject&#8221; component which includes identification attributes in the form of a personal identification number known as &#8220;BIX Identifier&#8221; which is an anonymous, globally unique, publically available random number within the BIX system. BIX identifiers are used to conveniently reference individuals within the BIX system. The &#8220;subject&#8221; component has 4 attributes: Personal ID number, Date/Time, Subject Public Key Info and Algorithm Identifier. Due to the fact that a BIX certificate is generated by its owner, a private key, linked to its corresponding public key, is used to &#8220;self-sign&#8221; the &#8220;Subject&#8221; component of the certificate.</p>
    <p>BIX certificates represent an innovation that adds an element of anonymity to bitcoin and other similar cryptographic protocols and can open the door to the formulation of a myriad of secure applications during the next few years.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/anonymity/" rel="tag">anonymity</a> <a href="https://www.deepdotweb.com/tag/bix/" rel="tag">bix</a> <a href="https://www.deepdotweb.com/tag/blockchain/" rel="tag">blockchain</a> <a href="https://www.deepdotweb.com/tag/certificates/" rel="tag">certificates</a> <a href="https://www.deepdotweb.com/tag/cryptographic/" rel="tag">cryptographic</a> <a href="https://www.deepdotweb.com/tag/promoting/" rel="tag">promoting</a> <a href="https://www.deepdotweb.com/tag/tokens/" rel="tag">tokens</a> <a href="https://www.deepdotweb.com/tag/transactions/" rel="tag">transactions</a></span> <span style="display:none" class="updated">2017-01-05</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

