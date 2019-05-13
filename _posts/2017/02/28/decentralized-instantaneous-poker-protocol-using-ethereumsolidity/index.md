---
Decentralized Instantaneous Poker Protocol Using Ethereum/Solidity
---
<article class="post-listing post-18375 post type-post status-publish format-standard has-post-thumbnail hentry  tag-decentralized tag-ethereumsolidity tag-instantaneous tag-poker tag-protocol">
    
<div class="post-inner">
    
    
        
<span>Posted by: <a href="https://www.deepdotweb.com/author/tamersameeh/" title="">Tamer Sameeh </a></span>
    
    
<span>February 28, 2017</span>
    
    
<span><a href="https://www.deepdotweb.com/2017/02/28/decentralized-instantaneous-poker-protocol-using-ethereumsolidity/#comments">1 Comment</a></span>
</p>
<div class="clear"></div>
    
    
    
<p>Today&#8217;s standard model of communication renders it impossible to establish a fair multiparty computation model, if an honest majority of participants cannot be guaranteed. This represents a big problem when it comes to designing a 100% fair, secure, decentralized poker platform. Accordingly, the past couple of decades have witnessed numerous research attempts to bypass this hypothetical impossibility mainly via implementing techniques such as optimistic fair exchange and gradual release. With the advent of bitcoin, a line of research, which emerged from cryptocurrency experimental studies, sought establishing fairness within <a href="https://www.deepdotweb.com/2017/01/05/secure-multi-party-computing-using-bitcoins-blockchain/">secure multiparty computation (MPC) models</a> via implementation of monetary penalties.</p>
<p>A group of researchers recently published <a href="https://arxiv.org/pdf/1701.06726.pdf">a paper that included a framework for a decentralized poker platform</a> that relies on a protocol for amortized MPC with monetary penalties and a highly secure method for cash distribution. The protocol includes an initial phase during which parties communicate with a cryptocurrency network; this would then enable them to interact exclusively among themselves along one or more poker games during which money changes hands.</p>
<p><img class="wp-image-18380 aligncenter" src="/imgs/2017/02/poker-jpg.jpeg" alt="Poker.jpg" srcset="/imgs/2017/02/poker-jpg.jpeg 940w, /imgs/2017/02/poker-jpg-300x139.jpeg 300w, /imgs/2017/02/poker-jpg-272x125.jpeg 272w" sizes="(max-width: 940px) 100vw, 940px" /></p>
<p>The proposed protocol harnesses the power of stateful contracts which maximizes its efficiency. When compared to bitcoin scripts&#8217; limited expressive power, stateful contracts promote extensive functionality that provide richer ways for interaction between cryptocurrency blockchains and standard secure multiparty computation. The paper included a formal stateful contract model and the security characteristics of the proposed protocol. It also provided an experimental implementation via Ethereum/Solidity, for the stateful contracts utilized in the protocol. The protocol adopts an off-chain system for cash distribution using stateful duplex micropayment channels. When compared to payment channels based on bitcoin, the proposed duplex micropyamet channels have been proven to be not only more efficient, but also of greater functionality.</p>
<p><strong>An Overview of the Proposed Poker Protocol:</strong></p>
<p>Unlike previous protocols, the proposed protocol is based on secure cash distribution with penalties SCD, rather than using fair MPC with penalties. The difference between SCD and fair MPC with penalties is that in SCD, the inputs and outputs of participants include both money and data, while fair MPC with penalties include only data in both inputs and outputs of participants, yet it rewards honest parties, who didn&#8217;t known the output, with money in the form of cryptocurrency.</p>
<p>A mental poker game represents an example of SCD, where the computation&#8217;s outcome is not intrinsically useful, yet it determines the way money changes hands. SCD was presented via on-chain protocols which require the sent messages, during execution of SCD, to have proof-of-work PoW confirmations. Oppositely, the newly proposed poker platform relies on stateful SCD protocols that are executed off-chain. Accordingly, following the initial on-chain setup phase, the players can play an endless number of instantaneous poker games, so long as neither player runs out of money.</p>
<p>The protocol has three phases:</p>
<p>1. Setting up contract parameters:</p>
<p>This is the phase when the players communicate with the stateful contract on the blockchain (on-chain). Players will agree on setting parameters for the contract including number of players, the allowed state for contract&#8217;s transition, the time-out and the amount of compensation paid to players in case the game(s) are aborted.</p>
<p>2.Local executions:</p>
<p>This is when actual computation takes place off the blockchain (off-chain) via local MPC executions which also provide hooks to the stateful on-chain contract.</p>
<p>3. Handling aborts:</p>
<p>This is the phase that includes the process used by honest players whenever an off-chain local execution is aborted. This is phase during which players will interact with the on-chain stateful contract to either claim their compensation or continue the aborted local execution.</p>
<p>The poker platform is dependent on off-chain cash distribution system which can be also used for stateful duplex payment channels. Although this use case doesn&#8217;t need secure computation processes, it is rather important. This is due to the fact that micropayment channels can be utilized to reduce the volume of transaction data maintained by a cryptocurrency&#8217;s blockchain. As such, scalability issues, which represent one of the major obstacles hindering the adoption of cryptocurrencies, can be mitigated efficiently via using such off-chain payment channels. The authors of the paper compared their proposed stateful duplex payment channels to <a href="https://www.deepdotweb.com/2017/01/11/teechan-improving-bitcoins-scalability-via-creation-off-chain-payment-channels/">off-chain payment channels</a> that are bitcoin based and proved that stateful duplex payment channels are more efficient and provide better functionality. They presented a self-contained implementation model of stateful duplex off-chain payment channels.</p>
    
    
</div><!-- .entry /-->
<a href="https://www.deepdotweb.com/tag/decentralized/" rel="tag">decentralized</a> <a href="https://www.deepdotweb.com/tag/ethereumsolidity/" rel="tag">ethereumsolidity</a> <a href="https://www.deepdotweb.com/tag/instantaneous/" rel="tag">instantaneous</a> <a href="https://www.deepdotweb.com/tag/poker/" rel="tag">poker</a> <a href="https://www.deepdotweb.com/tag/protocol/" rel="tag">protocol</a></span>				<span style="display:none" class="updated">2017-02-28</span>
<div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/tamersameeh/" title="Posts by Tamer Sameeh" rel="author">Tamer Sameeh</a></strong></div>
    
    
</div><!-- .post-inner -->
</article><!-- .post-listing -->

