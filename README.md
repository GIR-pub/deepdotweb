# dotweb-archive.github.io

Archive: Privacy guides, and History from deepdotweb.

The world should have user-friendly access to the educational materials that were previously available on deepdotweb.com.

## This is an unofficial archive

This isn't anything to do with the market, but only educational material.

You can argue that the market is educational.. and sure that's fine, but that's not the part i'm interested in preserving. You can follow these instructions and do it your own way, and\or clean-up parts of it you'd like to preserve, and submit a pull-request.

There is way more content than I realized before I began.. so I'm making some arbitrary decisions, such as eliminating 50x50 images, and "shit posting" memes, etc.  


![](https://imgur.com/T7QpFTM.png)


I ran:

`gem install wayback_machine_downloader`   [*](https://superuser.com/questions/828907/how-to-download-a-website-from-the-archive-org-wayback-machine)


and then


`wayback_machine_downloader https://deepdotweb.com`

I'm stripping away all the header material and the comments so I can spin up a simple site, without having to host everything, and really trying to get it done asap because I have other stuff I should be doing.. 

* [https://github.com/Ruined1/HTMLArticleElementStripper](https://github.com/Ruined1/HTMLArticleElementStripper)

This app goes through and strips away everything besides what's between `<article>...</article>`.

---

for my purposes, It's important to have all the security guides saved and easily accessible, and keeping a bunch of the old posts too for history\educational purposes.

ultimately will link back to archived links of the pages so people can dig in if they like.

I'll be using github pages\ jekyll static site generator, once I have the files cleaned up it will publish easily (maybe tonight).

Not sure what I'll use, but there are a number of good resources for publishing on GitHub here:

* [GitHub Pages Starter Pack](https://infominer.id/web-work/github-pages-starter-pack/)