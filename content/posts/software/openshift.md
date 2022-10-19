---
title: "Openshift Documentation"
tags: ["openshift","docker","k8s"]
date: 2022-02-22
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

## Issues with root

- <https://number1.co.za/openshift-will-not-run-your-container-as-a-root-user/>
- <https://stackoverflow.com/questions/57044509/openshift-use-nginx-official-image-instead-of-one-from-oc-registry>
- <https://stackoverflow.com/questions/38754592/what-is-the-correct-way-to-run-an-nginx-docker-container-in-openshift>
- <https://engineering.bitnami.com/articles/running-non-root-containers-on-openshift.html>
- <https://torstenwalter.de/openshift/nginx/2017/08/04/nginx-on-openshift.html>
- <https://developers.redhat.com/blog/2020/10/26/adapting-docker-and-kubernetes-containers-to-run-on-red-hat-openshift-container-platform>
- <https://developers.redhat.com/blog/2020/10/26/adapting-docker-and-kubernetes-containers-to-run-on-red-hat-openshift-container-platform#how_to_debug_issues>
- <https://stackoverflow.com/questions/42363105/permission-denied-mkdir-in-container-on-openshift>

> Although OpenShift runs containers using an arbitrarily assigned user ID, the group ID must always be set to the root group (0). Therefore, the directories and files that the processes running in the image need to access should have their group ownership set to the root group. They also need to be read/writable by that group as recommended by the OpenShift Container Platform-specific guidelines.

## Install Minishift

- <https://phoenixnap.com/kb/ubuntu-install-kvm>
- <https://docs.okd.io/3.11/minishift/getting-started/preparing-to-install.html>

## Further sources

- <https://docs.openshift.com/online/pro/architecture/core_concepts/pods_and_services.html>
