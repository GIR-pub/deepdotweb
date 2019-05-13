---
Tutorial &#8211; How To Host Your Own DNS Website Domain On Ethereum&#8217;s Blockchain
---
<article class="post-listing post-22422 post type-post status-publish format-standard has-post-thumbnail hentry 
tag-blockchain tag-dns tag-domain tag-ethereums tag-tutorial tag-website">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>September 7, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/09/07/tutorial-host-dns-website-domain-ethereums-blockchain/#comments">1 Comment</a></span>
    </p>
    <div class="clear"></div>
    <div class="entry">
    <p>You can now host DNS domains on Ethereum&#8217;s blockchain through ENS, which is short for Ethereum Name Service, a distributed, extensible domain naming system that relies on Ethereum&#8217;s blockchain. This is possible via adjusting the domain name server settings to point to gateway DNS servers, which resolve lookups through checking an ENS registry that points to resolvers including the zone data for the domain in question.</p>
    <p>Throughout this tutorial, I will present you with a simple guide to help you host your DNS domain on the blockchain.</p>
    <p><strong>Note: You have to be running a full Ethereum node on your machine to be able to follow through this tutorial. We have </strong><a href="https://www.deepdotweb.com/2017/05/25/tutorial-run-full-ethereum-node-windows/"><strong>a detailed tutorial on how to run a full Ethereum node</strong></a><strong> that will help you run yours, even if you are a total newbie. </strong></p>
    <p><img class="wp-image-22427 aligncenter" src="/imgs/2017/09/word-image-16.png" srcset="/imgs/2017/09/word-image-16.png 539w, /imgs/2017/09/word-image-16-276x300.png 276w" sizes="(max-width: 539px) 100vw, 539px" /></p>
    <p><strong>1. Implementing your own ENS registry:</strong></p>
    <p>First, you will have to implement ENS central component, i.e. &#8220;the registry&#8221;. To do so, run the following code into an Ethereum console (via your Ethereum client):</p>
    <p><img class="wp-image-22428" src="/imgs/2017/09/word-image-17.png" /></p>
    <p>Once this contract is successfully mined, you will have a fresh new ENS registry, whose root is controlled by the account that created the contract, i.e. the transaction. As such, this account will have total control over the registry, as it can add or remove nodes along the entire tree.</p>
    <p><strong>2. Implementing a registrar:</strong></p>
    <p>A registrar represents a contract that controls a node, i.e. a name, within the ENS registry, and provides a special user interface for participants to register subnodes, i.e. subdomains. A registrar can be implemented on any domain name. Throughout the following example, we will implement a basic first-in-first-served registrar via the root node.</p>
    <p>To implement a first-in-first-served registrar via the root node of your ENS registry, run the following code in an Ethereum console.</p>
    <p>Once this contract is successfully mined, as owner of the ENS registry, you can transfer the ownership of the root node to the new registrar that has been created via executing the following code in an Ethereum console: <img class="wp-image-22430" src="/imgs/2017/09/word-image-19.png" /></p>
    <p>Now, users can register names, i.e. nodes, with the registrar. You can <a href="http://docs.ens.domains/en/latest/userguide.html#fifs">register the names you desire with the FIFS registrar</a>. Users can now register domain names via two top level domains:</p>
    <ul>
    <li><strong><em>.eth</em></strong>: this top level domain uses an auction registrar that has the same functionality of the main network and permits users, registering domain names, to own them indefinitely. Visit this <a href="http://docs.ens.domains/en/latest/userguide.html#auctions">link</a> for registering a domain name with the auction registrar.</li>
    <li><strong><em>.test:</em></strong> this top level domain allows any user to claim any unused domain name for test purposes. Domain names expire automatically after 28 days.</li>
    </ul>
    <p><strong>3. Implementing a DNSResolver instance:</strong></p>
    <p>To implement an instance of the DNSResolver, run the following code in an Ethereum console.</p>
    <p><strong>4. Setting DNSResolver as the domain name&#8217;s resolver:</strong></p>
    <p>The ENS registry has to be modified so that the newly implemented DNSResolver acts as the resolver of your domain name. This can be done by using the <strong><em>setResolver </em></strong>function, as in the following code example: <img class="wp-image-22431" src="/imgs/2017/09/word-image-20.png" /></p>
    <p>So, in the previous example, we set DNSResolver to be the resolver of the domain name <strong><em>deepdotweb.eth</em></strong>.</p>
    <p>The ENS blog has a <a href="http://docs.ens.domains/en/latest/userguide.html#interacting">useful guide that includes details of how to interact with the ENS registry</a> e.g. registering a name, transferring name ownership, creating subdomains&#8230;..etc.</p>
    <p><strong>5. Writing a Zonefile:</strong></p>
    <p>You have to write a zonefile that includes an NS record of your domain name that specifies <strong><em>address.ns1.ens.domains </em></strong> as the resolver, but don&#8217;t forget to replace <strong><em>address</em></strong> with the address of your ENS registry that you implemented in step 1, but omit the &#8220;Ox&#8221; in the beginning. The following is an example code for a zonefile.</p>
    <p><strong>6. Cloning and Building ensdns:</strong></p>
    <p>Clone and build <a href="https://github.com/arachnid/ensdns/">ensdns</a>. Now, start your node and then run the following code in an Ethereum console:</p>
    <p>This will upload the zonefile to the blockchain.</p>
    <p><strong>7. Finally, Updating Your NS Records:</strong></p>
    <p>The final step is to update your NS records with your registrar to point to the domain you used above which is in the format:</p>
    <p><strong>address<em>.ns1.ens.domains</em></strong></p>
    <p>So, if we chose a domain name e.g. <strong><em>deepdotweb.eth </em></strong>it will be hosted on the blockchain, i.e. resolve to something like:</p>
    <p><strong><em>397437541a757880eCC5d26606624F4FC8958Cb5.ns1.ens.domains</em></strong></p>
    <p>Here you go, you now have an ENS domain hosted on Ethereum&#8217;s blockchain. In the end, it is worth mentioning that ENS hosting is an experimental feature that is still in its infancy, so you should not use it for any critical domains. The DNS gateway still has not been extensively tested and presently, only a single instance is working, so there is no backup or any mitigation strategies in case of server failure. Also note that the configuration and API can be changed in backwards-incompatible ways, which can break your nameserver. This should only be used for experimental and research purposes.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/blockchain/" rel="tag">blockchain</a> <a href="https://www.deepdotweb.com/tag/dns/" rel="tag">dns</a> <a href="https://www.deepdotweb.com/tag/domain/" rel="tag">domain</a> <a href="https://www.deepdotweb.com/tag/ethereums/" rel="tag">ethereums</a> <a href="https://www.deepdotweb.com/tag/host/" rel="tag">host</a> <a href="https://www.deepdotweb.com/tag/tutorial/" rel="tag">tutorial</a> <a href="https://www.deepdotweb.com/tag/website/" rel="tag">website</a></span> <span style="display:none" class="updated">2017-09-07</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

