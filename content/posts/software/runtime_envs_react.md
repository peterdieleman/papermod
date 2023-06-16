---
title: "Runtime environment variables in React + nginx"
tags: ["react", "docker", "nginx", "javascript"]
date: 2022-05-06
# weight: 1
# author: "Peter Dieleman"
# showToc: false
# TocOpen: false
draft: false
# hidemeta: false
# comments: false
# description: "A guide on extending the battery life of your linux laptop"
# disableShare: false
# searchHidden: false
---


## Injecting Variables Through (b)ash

- <https://github.com/facebook/create-react-app/issues/2353>
- <https://www.freecodecamp.org/news/how-to-implement-runtime-environment-variables-with-create-react-app-docker-and-nginx-7f9d42a91d70/>
- <https://medium.com/free-code-camp/how-to-implement-runtime-environment-variables-with-create-react-app-docker-and-nginx-7f9d42a91d70>
- <https://www.bencode.net/posts/react-build/> <-- check
- <https://sinclert.github.io/react-env-vars/>
- <https://gist.github.com/lezhkin11/d6b0a14127b4920feaece278e5323ee1>

## Using a Multi-stage Dockerfile

Another option is to use a multi-stage Docker file, where the first stage is still using nodeJS,
[like this](https://dev.to/bahachammakhi/dockerizing-a-react-app-with-nginx-using-multi-stage-builds-1nfm).  This way node can still parse the environment variables as you would during local development, and the final deployed image is.  However, in large organizations deploying such a multistage container in a production environment may irk some SecOps people. See: [earthly.dev/blog/docker-multistage/](https://earthly.dev/blog/docker-multistage/) for some explanation about security concerns.
