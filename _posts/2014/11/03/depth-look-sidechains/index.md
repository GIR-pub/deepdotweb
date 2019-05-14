---
title: "In-Depth Look Into Sidechains"
---

Posted by:  Zubair Muadh
<span>November 3, 2014</span>
    

<p>Following the proposal for having Bitcoin Sidechains that was <a href="/2014/06/26/sidechains-blockchain-2-0/">discussed earlier in 2014</a> Adam Back, Matt Corallo, Luke Dashjr, Mark Friedenbach, Gregory Maxwell, Andrew Miller, Andrew Poelstra, Jorge Timón, and Pieter Wuille released the first white paper on sidechains titled ‘Enabling Blockchain Innovations with Pegged Sidechains’</p>
<p>A detailed 22 page whitepaper which discuses design rationale, the applications of sidechains, drawbacks and explains two-way pegging.</p>
<p><strong>Symmetric two way pegging</strong></p>
<p><a href="/imgs/2014/10/sidechains.png"><img class="aligncenter size-full wp-image-7486" src="/imgs/2014/10/sidechains.png" alt="sidechains" width="529" height="405" srcset="/imgs/2014/10/sidechains.png 529w, /imgs/2014/10/sidechains-300x230.png 300w" sizes="(max-width: 529px) 100vw, 529px"/></a></p>
<p>We’re introduced to the details of symmetric two-way pegging</p>
<p>SPV is a simplified payment verification proof.</p>
<p>How the protocol works is that you would send your Bitcoins from the Blockchain (which is the parent chain in this case) to an SPV locked output.</p>
<p>It’s locked till a certain number of confirmations are reached (to validate the transaction), once reached then the coins are released. You must however also wait out the contest period this is a duration in which a newly-transferred coin may not be spent on the sidechain. The purpose of a contest period is to prevent double-spending by transferring previously-locked coins during a reorganization.</p>
<p><em>SPV Reorganization:</em></p>
<p><em>If during the delay (contest periods) a new proof is published containing a chain that doesn’t include the block in which your lock output was created your conversion is invalidated. If SPV proof fails and undergoes reorganisation and new proof is submitted to the chain and you wait again for the contest period to clear. </em></p>
<p>When returning back to Bitcoin SPV proof is again submitted beginning the contest period if SPV proof fails, SPV reorganization occurs and then new SPV proof is submitted again.</p>
<p><strong>Asymmetric two-way pegging:</strong></p>
<p>In the whitepaper asymmetric two-way pegging was briefly explained but was not explored due to the sheer complexities involved with its implementation.</p>
<p>In asymmetric two-way peg however users of the sidechain are fully validators of the parent chain, and transfers from parent chain to sidechain do not require SPV proofs, since all validators are aware of the state of the parent chain.</p>
<p>On the other hand, the parentchain is still unaware of the sidechain, so SPV proofs are required to transfer back. This gives a boost in security, since now even a 51% attacker cannot falsely move coins from the parent chain to the sidechain. However, it comes at the expense of forcing sidechain validators to track the parent chain, and also implies that reorganizations on the parent chain may cause reorganizations on the sidechain.</p>
<p><strong>Drawbacks to Sidechains</strong></p>
<p>The sheer complexity on the network level brought about by having multiple independent unsynchronised blockchains supporting transfers between each other is huge. They must support transaction scripts which can be invalidated by a later reorganisation proof.</p>
<p>This calls for a software that would automatically detect misbehaviour and produce and publish proofs.</p>
<p>In addition to this the ‘one chain, one asset’ maxim becomes invalidated as individual chains could be supported by multiple other assets, some assets not even being inexistence when the chain was originally created. Each asset would have to be labelled with the original chain that it came from so transfers can be unwound correctly.</p>
<p>This could cause sidechains as a whole to fail if it becomes difficult to unwind the transfers, which could devalue the particular chain.</p>
<p>Wallet software would also have to be reconfigured to support multiple chains, with the incorporation of some altcoins, it could prove to be difficult since each altcoin has its own wallet software that facilitates transactions in its particular chain.</p>
<p><strong>Fraudulent transfers:</strong></p>
<p>Reorganisations of arbitrary depth are in principle possible, however it could allow an attacker to completely transfer coins between sidechains before causing a reorganization longer than the contest period on the sending chain to undo its half of the transfer. This would result in an imbalance between the number of coins on the recipient chain and the amount of locked output value backing them on the output chain. If the attacker is then capable of returning the transferred coins to the original chain, he’d have more coins in his possession at the expense of other users on the sidechain.</p>
<p>This threat could be mitigated by increasing the duration of the contest periods, what would a be more effective method would be making the contest period a function of the hashing power of both chains.</p>
<p>The recipient chain might only unlock coins given an SPV proof of one day’s worth of its own proof-of-work, which might correspond to several days of the sending chain’s proof-of-work.</p>
<p>What is fundamental is that sidechains do not respond with a catastrophic failure by optimising the security parameters to the functionalities of each sidechain.</p>
<p><strong>Mining</strong></p>
<p>Introducing sidechains with mining fees may place resource pressure on miners which could result in Bitcoin mining centralisation.</p>
<p>Because miners receive compensation from the block subsidy and fees of each chain they provide work for, it is in their economic interest to switch between different similarly-valued blockchains following changes in difficulty and movements in market value.</p>
<p>As miners provide work for more blockchains, more resources are needed to track and validate them all, this would increase the resources that miners would be using up making it unaffordable for smaller-scale miners.</p>
<p>It would be possible for miners to delegate validation and transaction selection however choosing to delegate authority enables miners to avoid almost all of the additional resource requirements, or provide work for blockchains that they are still in the process of validating. However such delegation comes at the cost of centralizing validation and transaction selection for the blockchain, even if the work generation itself remains distributed.</p>

Updated: 2014-11-03    
