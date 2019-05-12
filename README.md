# Deep Dot Web Privacy Guides

Archive: Privacy guides, and History from deepdotweb.


![](https://imgur.com/T7QpFTM.png)

I was broken-hearted to recently find out that deepdotweb got seized.

The world should have user-friendly access to the educational materials that were previously available on deepdotweb.com.

It was the best place to find privacy guides, and though I'm grateful for the internet archive, I thought I could do something nice with [Jekyll and Github Pages](https://infominer.id/web-work/github-pages-starter-pack/). 

---

I ran:

`gem install wayback_machine_downloader`   [*](https://superuser.com/questions/828907/how-to-download-a-website-from-the-archive-org-wayback-machine)


and then


`wayback_machine_downloader https://deepdotweb.com`

I'm stripping away all the header material and the comments so I can spin up a simple site, without having to host everything, and really trying to get it done asap because I have other stuff I should be doing.. 

* [https://github.com/Ruined1/HTMLArticleElementStripper](https://github.com/Ruined1/HTMLArticleElementStripper)

This app goes through and strips away everything besides what's between `<article>...</article>`.

From there I had to do a bunch of search and replace so that it was all nice and ready for one of the static site generators.
