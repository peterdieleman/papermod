---
title: "The Cheatsheet"
# tags: ["software"]
date: 2023-03-06
aliases: ["/cheatsheet"]
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

## macOS, ip-address

- `ipconfig getifaddr en0`

## kubectl

- `kubectl logs --namespace name_space svc_name -f`
- `kubectl set env deployment/name_of_service ENV_VAR="value" --namespace=the_best`
- `delete --all deployments --namespace=defaul`

## minikube

- `minikube service`

## chmod

- `chmod -R 701 ./*` (add all permissions to all files)

## Docker

- `DOCKER_BUILDKIT=0  docker build .` ([stackoverflow](https://stackoverflow.com/questions/64221861/an-error-failed-to-solve-with-frontend-dockerfile-v0))
- `docker run -it --entrypoint /bin/bash [docker_image]` (overwrite entrypoint of the docker file, rn container interactively)
- `docker build -f sub/directory/Dockerfile . -t "image_name"`

## iTerm / Bash

- `cat .bash_history`
- `ctrl + r`

## Helm

- `helm upgrade chart_name chart_dir/ --install`

## pip

- `pip show <package_name>` to let pip show you where a package is installed

## brew

- `brew list --formula | xargs brew info | egrep --color '\d*\.\d*(KB|MB|GB)'` ([stackoverflow](https://stackoverflow.com/questions/40065188/get-size-of-each-installed-formula-in-homebrew))