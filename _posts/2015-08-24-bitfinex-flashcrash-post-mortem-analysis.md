---
title: "BitFinex FlashCrash &#8211; Post-Mortem Analysis"
---

Posted by: pesa_mic 

<span>August 24, 2015</span>

<p>On August 16th, just before midnight (UTC), Bitcoin markets were in a moment of temporary panic, about 30 minutes after a flash crash incidence on one of the world’s largest exchange (by liquidity) BitFinex. Wikipedia describes it as</p>
<p><em>“A <strong>flash crash</strong> is a very rapid, deep, and volatile fall in security prices occurring within an extremely short time period.”</em></p>
<p>A common phenomena in mainstream financial markets and even previously on XBT markets. As XBT asset prices are closely matched around the world, but on silod exchanges in different regions, its effects naturally spilled over into other exchanges completely separated from the epicentre. In a period of 8 minutes, price plummeted from $230 to $ 160!</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/08/13.jpg">

<p><strong><u>What happened? </u></strong></p>
<p>Phase 1 &#8211; Pre-crash:</p>
<p>Earlier that evening, besides all the debate around Bitcoin XT hard fork, all was relatively normal on exchanges. Price had been gradually drifting lower from $260 levels towards strongly supported $ 250. There was reason to believe XT debate would creep into prices, as market exhibited weakness since failure of a double at $ 298.</p>
<p>The first scare, a precursor to the flash crash, came in early at around 8pm UTC. BItfinex orderbook was heavy thick on the bid sides, and attempts came in to test $ 250. Large movements of coins were noticeable on the orderbook, characterized as ‘<em>Megadump on BFX</em>’</p>
<p><em>“Break through attempt on finex in the making&#8230;~4800coins so far…”</em></p>
<p>Minutes later, pace picked up after 15,000 coins were dumped, setting off traders on lower price speculation to the $228 &#8211; $230 zone. By 8.15pm, the bid side was down to a thin stack of 5k coins to $200. It had the makings of a bear trap, and with it, BFX swap activity.</p>
<p><em>‘Margin longs are going down, not up. $300,000 in dollar swaps closed.’Looks like we won&#8217;t get another crash. Just more $220-$320 range trading.’</em></p>
<p>$ 2 million worth in longs were closed and 10k shorts were opened simultaneously. This first scare could be attributed to 20,000 btc sell consisting of roughly 10,000 btc short and 8,000 btc long positions being closed. This was a glimpse of BFX swap charts at 10.00pm</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/08/2.png">

<p>Gradually, price drifted back to normal levels at $250, in sync with other exchanges after an hour of hysteria. This marked the end of the precursor to the main flash event.</p>
<p>Phase 2: Main crash</p>
<p>The main flash crash picked up speed later at about 11.36 pm when, dumping picked up at an accelerated speed. It was an amazing event to behold, as other exchanges maintained their trading range, wobbling from being dragged down by events at BFX. On low volumes, price oscillated between $ 220 and $ 240.</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/08/3.png">

<p>Within minutes, 11.38 pm, price cascaded into free fall, plummeting $ 30,evident from a visibly large red candle on BFX charts. Nothing could stop this, even 600 coins to $199. Chinese exchanges, which typically lead prices, sat on the bylines as spectators, observing a $45 price differential between their exchanges and Bitfinex.</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/08/4.png">

<p>Shortly thereafter, at 11.48pm, price broke below $ 200 &#8211; a level not seen since January and a minute later, $ 162 was officially breached; an opportune time to have been in fiat, as the price presented a lucrative buying opportunity. In hindsight, what resembled a huge margin call cascade looked like it would drag down prices to the $100 level. At 11.50pm, price at $186 ranged between this level and $162 as buy and sell orders came in and got executed.</p>
<p><em>“Weird movement..it literally goes 180-230-160-22x in seconds up and down on Finex. Is that even real data??”</em></p>
<p>The rest of the exchanges weren’t spared. At this time,Bitstamp and Coinbase were at $222 while Finex struggled right above $175. This is a glimpse of the order book at this time</p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/08/54.jpg">

<p>Market Calms down</p>
<p>At 11.57, the madness relented, and traders stepped in to take advantage of the obvious buying opportunities. The rest of the exchanges also began picking up to higher levels. By 12.01am, price had gone up from $175 to $220 in under 2 minutes. Around this time, some bitfinex users reported malfunction glitches with their trading interfaces</p>
<p><em>‘$191.2598468 is not valid on Bitfinex’</em></p>
<p>Users reported experiencing trouble filling up their orders as price retraced &#8211; $220, $230, $235. By 12.05am, price was back again at $255 with volume back to normal levels</p>
<p><em>“Perhaps the biggest change In price ever down and back in bitcoin history! It seems like 10+ million got liquidated but in the same time over 10 million went long again approx how many coins were insta-dumped?”</em></p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/08/6.png">

<p><strong><u>Aftermath &#8211; Connecting the dots, Piecing together events</u></strong></p>

<img src="https://G-I-R.github.io/deepdotweb/imgs/2015/08/71.jpg">

<p>This event naturally called for a post analysis to try figure out why it unfolded as it did. Right after these events, members of <a href="https://twitter.com/btcWhaleclub">Whale Club</a> held an online audio session with BitFinex’s CSO Phil G. Potter, directing questions at him on some of the events witnessed. In his own words, part of the event was escalated by technical glitches in their system &#8211; such as a lag in their live engine that functions to update positions. This explains why some users reported trouble executing their orders when using the main trading platform. From the <a href="https://t.co/ACvfhInTam">audio recording on soundcloud</a>, Potter also added that part of the flash crash was triggered by a bunch of leveraged positions that forcibly had to be closed and happened to be in close proximity to each other.</p>
<p><em>“When the price shifts suddenly, as it did yesterday, &#8216;long&#8217; users who have borrowed funds may see their account equity drop to zero – at which point Bitfinex will automatically liquidate their positions.</em></p>
<p><em>This can exacerbate price movement, as these positions add to sell-side pressure on an already crashing market.” &#8211; </em><a href="http://www.coindesk.com/bitcoin-price-falls-14-following-bitfinex-flash-crash/"><em>Coindesk</em></a></p>
<p>Under normal circumstances, circuit breakers are enforced to limit market movements over 10%, however, this measure is triggered in cases of single manipulated order events. This was not the case on this day, hence why the triggers did not kick in despite the huge swing.</p>
<p>Trader’s Block conducted their own <a href="https://tradeblock.com/blog/bitfinex-flash-crash-analysis">post-event analysis</a>, which seemed to back up Potter assertions.</p>
<p><em>“Over the one-hour trading period highlighted above, ~70k bitcoin changed hands at Bitfinex; this compares with an average daily volume of 20k bitcoin at Bitfinex over the past month. Bitfinex was not only trading in excess of 10% away from the rest of the market, but also with a multi-point bid/ask spread, leading to significant jumps between ticks”</em> &#8211; Trader’s Block</p>

Updated: 2015-08-24

