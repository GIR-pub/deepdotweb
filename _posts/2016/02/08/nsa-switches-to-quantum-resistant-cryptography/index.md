---
NSA Switches To Quantum-Resistant Cryptography
---
<article class="post-listing post-13173 post type-post status-publish format-standard has-post-thumbnail hentry  tag-cryptography tag-nsa tag-quantumresistant tag-switches">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/fuzzy/" title="">Fuzzy </a></span>
    <span>February 8, 2016</span>
    <span>in <a href="https://www.deepdotweb.com/category/deepdot-news/" rel="category tag">Featured</a>, <a href="https://www.deepdotweb.com/category/news-updates/" rel="category tag">News Updates</a></span>
    <span><a href="https://www.deepdotweb.com/2016/02/08/nsa-switches-to-quantum-resistant-cryptography/#comments">7 Comments</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>In a recently published <a href="https://www.iad.gov/iad/customcf/openAttachment.cfm?FilePath=/iad/library/ia-guidance/ia-solutions-for-classified/algorithm-guidance/assets/public/upload/CNSA-Suite-and-Quantum-Computing-FAQ.pdf&amp;WpKes=aF6woL7fQp3dJicDQFZVNrsPCxb58LrERpG7tK">FAQ</a>, the NSA outlines the switch for NSS (National Security Systems) from Suite B cryptography to the CNSA (Commercial National Security Algorithm Suite).</p>
    <p>The NSA describes the CNSA as a “suite of algorithms identified in CNSS Advisory Memorandum 02-15 for protecting NSS up to and including TOP SECRET classification. This suite of algorithms will be incorporated in a new version of the National Information Assurance Policy on the Use of Public Standards for the Secure Sharing of Information Among National Security Systems (CNSSP-15 dated October 2012). The Advisory Memorandum and Policy define the set of public cryptographic standards that may be used to protect NSS until acceptable public standards for quantum resistant cryptography exist and are approved for use in NSS by the Committee for National Security Systems (CNSS).”</p>
    <p>Detailing the CNSA&#8217;s algorithms and its usage:</p>
    <table width="643">
    <tbody>
    <tr>
    <td width="321">Algorithm</td>
    <td width="321">Usage</td>
    </tr>
    <tr>
    <td width="321">RSA 3072-bit or larger</td>
    <td width="321">Key Establishment, Digital Signature</td>
    </tr>
    <tr>
    <td width="321">Diffie-Hellman (DH) 3072-bit or larger</td>
    <td width="321">Key Establishment</td>
    </tr>
    <tr>
    <td width="321">ECDH with NIST P-384</td>
    <td width="321">Key Establishment</td>
    </tr>
    <tr>
    <td width="321">ECDSA with NIST P-384</td>
    <td width="321">Digital Signature</td>
    </tr>
    <tr>
    <td width="321">SHA-384</td>
    <td width="321">Integrity</td>
    </tr>
    <tr>
    <td width="321">AES-256</td>
    <td width="321">Confidentiality</td>
    </tr>
    </tbody>
    </table>
    <p>&nbsp;</p>
    <p>The NSA remarked that “The AES-256 and SHA-384 algorithms are symmetric, and believed to be safe from attack by a large quantum computer.”</p>
    <p>According the NSA, the following isn&#8217;t safe to use:</p>
    <ul>
    <li>ECDH and ECDSA with NIST P-256</li>
    <li>SHA-256</li>
    <li>AES-128</li>
    <li>RSA with 2048-bit keys</li>
    <li>Diffie-Hellman with 2048-bit keys</li>
    </ul>
    <p>What provoked this switch was the ever-growing threat of quantum computers breaking encryption.</p>
    <p><em>“</em>&#8230; quantum computers will use “qubits” that behave in surprising ways, efficiently performing selected mathematical algorithms exponentially faster than a classical computer.” The NSA went on to say “A sufficiently large quantum computer, if built, would be capable of undermining all widely-deployed public key algorithms used for key establishment and digital signatures.<em>”</em></p>
    <p>According to the NSA, symmetric algorithms are more quantum-resistant as opposed to public key algorithms.</p>
    <p>“It is generally accepted that quantum computing techniques are much less effective against symmetric algorithms than against current widely used public key algorithms. While public key cryptography requires changes in the fundamental design to protect against a potential future quantum computer, symmetric key algorithms are believed to be secure provided a sufficiently large key size is used.”</p>
    <p>The NSA made sure to note that just because they&#8217;re making this switch doesn&#8217;t mean that a quantum computer exists.</p>
    <p>“NSA does not know if or when a quantum computer of sufficient size to exploit public key cryptography will exist. The cryptographic systems that NSA produces, certifies, and supports often have very long life-cycles. NSA has to produce requirements today for systems that will be used for many decades in the future, and data protected by these systems will still require cryptographic protection for decades after these solutions are replaced. There is growing research in the area of quantum computing, and enough progress is being made that NSA must act now to protect NSS by encouraging the development and adoption of quantum resistant algorithms.”</p>
    <p>Regarding, “why now”, the NSA says “Choosing the right time to champion the development of quantum resistant standards is based on 3 points: forecasts on the future development of a large quantum computer, maturity of quantum resistant algorithms, and an analysis of costs and benefits to NSS owners and stakeholders. NSA believes the time is now right—consistent advances in quantum computing are being made, there are many more proposals for potentially useful quantum resistant algorithms than were available 5 years ago, and the mandatory change to elliptic curves that would have been required in October 2015 presented an opportune time to make an announcement. NSA published the advisory memorandum to move to quantum resistant symmetric key options and to allow additional continued use of older public key options as away to reduce modernization costs in the near term. In the longer term, NSA is looking to all NSS vendors and operators to implement standards-based, quantum resistant cryptography to protect their data and communications.”</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/cryptography/" rel="tag">cryptography</a> <a href="https://www.deepdotweb.com/tag/nsa/" rel="tag">nsa</a> <a href="https://www.deepdotweb.com/tag/quantumresistant/" rel="tag">quantumresistant</a> <a href="https://www.deepdotweb.com/tag/switches/" rel="tag">switches</a></span> <span style="display:none" class="updated">2016-02-08</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/fuzzy/" title="Posts by Fuzzy" rel="author">Fuzzy</a></strong></div>
    
