---
title: "Replicating this website"
date: 2021-04-05T16:17:51+02:00
# weight: 1
# aliases: ["/first"]
tags: ["Hugo"]
author: "Peter Dieleman"
# author: ["Me", "You"] # multiple authors
showToc: false
TocOpen: false
draft: false
hidemeta: false
comments: false
description: "Steps to replicate this website"
disableHLJS: true # to disable highlightjs
disableShare: false
disableHLJS: false
searchHidden: false
# cover:
#     image: "<image path/url>" # image path/url
#     alt: "<alt text>" # alt text
#     caption: "<text>" # display caption under cover
#     relative: false # when using page bundles set this to true
#     hidden: true # only hide on current single page

---

# On macOS

## Cloning the Repository

1. Create a [Github](http://github.com/) account.
2. Open a terminal.
3. Make sure that you have installed 'brew' by 
   following [the installation instructions](https://brew.sh/).
4. Install git by running `brew install git`.
5. Install hugo by running `brew install hugo`.
6. We're going to duplicate a repository by using the steps described
   [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository).
   Follow the steps below:
   1. On github.com, create a new repository with your desired `newname`.
   2. Open a terminal.
   3. Navigate to a suitable directory to clone into by making use of the `cd` command.
   4. Type `git clone --bare https://github.com/peterdieleman/papermod.git && cd papermod`.
   5. Type `git push --mirror https://github.com/yourusername/newname.git`,
      where `yourusername` is your github username,
      and where `newname` is the repository name above.
   6. Type `cd .. && rm -rf papermod` to remove the original repository.
   7. Type 
      `git clone https://github.com/yourusername/newname.git`
      to clone your copy of this repository.
   8. Type `cd newname` to move into your newly cloned repo.
   9. Type `git submodule update --init --recursive`
      to make sure the submodules are cloned correctly.
7. Make sure you are on the 'master' branch by running `git checkout master`.
8. Within this folder, run `hugo server -D` and navigate to
   [http://localhost:1313/](http://localhost:1313/)
   to look at the website.

## Deploying to Netlify

1. Sign up for a [netlify account](https://www.netlify.com/).
2. Navigate to the [main settings page](https://app.netlify.com/).
3. Click on `New site from Git`.
4. Select 'Github'.
5. Select the repository that you want to build the site from.
6. Navigate to the bottom and hit 'Deploy site'.

Your site should now be deployed to a randomly generated `*.netlify.com` address.
To view the configuration of your site,
navigate to
[app.netlify.com](https://app.netlify.com/)
and click on 'Sites'.

## To come: Connecting your custom domain