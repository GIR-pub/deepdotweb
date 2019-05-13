---
QuickNet &#8211; A Faster, More Efficient Deep Web Network Architecture
---
<article class="post-listing post-17870 post type-post status-publish format-standard has-post-thumbnail hentry  tag-architecture tag-deep tag-efficient tag-faster tag-network tag-quicknet tag-web">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    <span>January 31, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/01/31/quicknet-faster-efficient-deep-web-network-architecture/#comments">4 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    <p><a href="https://arxiv.org/abs/1701.02291">QuickNet</a> is a novel deep network architecture that is faster and more efficient than the current &#8220;fast&#8221; deep web network architectures such as SqueezeNet. QuickNet utilizes fewer parameters when compared to previous network architectures. This has been made possible via implementing a couple of pivotal modifications to <a href="https://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_below_the_surface.pdf">the reference &#8220;Darknet&#8221; network architecture model</a>:</p>
    <p>a- Using depth-wise separable convolutions.</p>
    <p>b- Using parametric rectified linear units.</p>
    <p><img class="wp-image-17877 aligncenter" src="/imgs/2017/01/quicknet-jpg.jpeg" alt="quicknet.jpg" width="738" height="387" srcset="/imgs/2017/01/quicknet-jpg.jpeg 1268w, /imgs/2017/01/quicknet-jpg-300x157.jpeg 300w, /imgs/2017/01/quicknet-jpg-1024x536.jpeg 1024w" sizes="(max-width: 738px) 100vw, 738px" /></p>
    <p>The creator of QuickNet proved that leaky rectified linear units at a given test time is equal to, from a computational point of view, parametric rectified linear units. He also observed that separable convolutions can be viewed as a compressed inception network. The <a href="https://www.deepdotweb.com/2015/06/08/the-dark-web-deep-web-and-dark-net-terminology-hell/">deep web network architecture</a>, QuickNet, was inspired by the aforementioned observations, which led to a faster more efficient network architecture model. QuickNet has at least four main advantages:</p>
    <p>1- A smaller sized model, which runs more efficiently on a system with constrained memory resources.</p>
    <p>2- A very fast network that runs more efficiently on a system with constrained processing power.</p>
    <p>3- QuickNet has yielded an accuracy of 95.7% on the CIFAR-10 Dataset. This outperforms results of all previous experiments, except one, yet QuickNet represents a group of orthogonal approaches that could be combined, rather than used individually, to yield even better levels of accuracy.</p>
    <p>4- Orthogonality when compared to previous models of network compression approaches, which permits realization of speed gains.</p>
    <p><strong>The QuickNet Deep Web Network Architecture:</strong></p>
    <p>It is currently widely agreed that memory resources, not computational resources, are the primary power consumers in a <a href="https://www.deepdotweb.com/2014/06/21/how-the-deepweb-helped-and-hindered-net-neutrality-and-online-privacy/">deep neural network ecosystem</a>. Previous researches have shown that along a commercial 40 nm process, the energy intensive of the DRAM access is 200 times higher than 32 bit multiply. Accordingly, it is clear that in order to create a light weighted neural network architecture, which is also energy efficient, the architecture must rely on minimizing parameters. On the other hand, along with minimization of parameters, intermediate layer activation maps also need a large amount of memory resources, even at inference time. The proposed QuickNet architecture minimized the number of parameters to 3.56 million (using less than 14.24 megabytes at 32 bits), and this can be reduced even more to less than 1 megabyte via using Deep Compression. It has been observed that using Deep Compression with a rate of compression of 15x is more reasonable than the reported rate of 50x.</p>
    <p>QuickNet aimed at minimization of parameters due to the fact that the pipeline of Deep Compression already represents an effective, yet simple, pipeline for reducing the model size by 50x via combining quantization with pruning and Huffman coding without sacrificing accuracy. This combination is sufficient, by itself, to significantly reduce the size of the model. Oppositely, working to tame the computational complexity of deep web networks, without sacrificing accuracy, has been significantly lagging behind. Accordingly, QuickNet aims at offering a network with low computational complexity, while maintaining high levels of accuracy.</p>
    <p><strong>Results of Testing of QuickNet:</strong></p>
    <p>The author of the paper stated that he experimented QuickNet on CIFAR-10 along with data augmentation using Keras framework. A dropout with a value of 0.5 was used along with batch normalization. Cross-entropy loss was used as a loss of function. A validation/test set was used with randomly chosen 6000 images, which were never presented to the network. Accuracy was measured using the validation/test set.</p>
    <p>QuickNet testing exhibited an accuracy of 95.7%, which corresponds to an error rate of 4.3%. This is higher than all current deep network architectures, except Fractional Max Pooling. However, the QuickNet approach is orthogonal to that of Fractional Max Pooling and can be used in combination, yet the author of the paper chose to forgo it due to the following reasons:</p>
    <p>1- To promote computational tractability as all the current implementation approaches of Fractional Max Pooling take much longer (reaching 15x in Lasagne) when compared to conventional pooling methods without producing any optimization effects.</p>
    <p>2- To promote memory tractability due to the fact that memory resources consume the most energy and this can increase even more when Fractional Max Pooling is used.</p>
    <p>One of the most interesting features of QuickNet is its significantly fast architecture convergence (within 70 epochs, 80% accuracy). This can open the door to networks&#8217; updating and local training in the near future.</p>
    <p>Even much better results can be yielded with further hyperparameter research along with experimentation using various adaptive optimizers e.g. RMSProp or Adam.</p>
    </div>
    <span style="display:none"><a href="https://www.deepdotweb.com/tag/architecture/" rel="tag">architecture</a> <a href="https://www.deepdotweb.com/tag/deep/" rel="tag">deep</a> <a href="https://www.deepdotweb.com/tag/efficient/" rel="tag">efficient</a> <a href="https://www.deepdotweb.com/tag/faster/" rel="tag">faster</a> <a href="https://www.deepdotweb.com/tag/network/" rel="tag">network</a> <a href="https://www.deepdotweb.com/tag/quicknet/" rel="tag">quicknet</a> <a href="https://www.deepdotweb.com/tag/web/" rel="tag">web</a></span> <span style="display:none" class="updated">2017-01-31</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    </div>
</article>

