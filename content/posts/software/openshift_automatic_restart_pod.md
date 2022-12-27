---
title: "Automatically restart pods Openshift"
tags: ["openshift","k8s"]
date: 2022-07-12
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

## Problem

Seperately deployed pods are linked up in openshift using [automatically generated variables](https://docs.openshift.com/container-platform/3.11/dev_guide/environment_variables.html). 

To access the solution single route is allowed in from the outside to an nginx container. 

Pod restart policy: <https://docs.openshift.com/container-platform/3.11/architecture/core_concepts/pods_and_services.html>

## Threads

<https://stackoverflow.com/questions/37317003/restart-pods-when-configmap-updates-in-kubernetes>

## Solutions

- Restartpolicy?
- Reloader?

## Tangents:

- <https://www.hava.io/blog/cattle-vs-pets-devops-explained>

