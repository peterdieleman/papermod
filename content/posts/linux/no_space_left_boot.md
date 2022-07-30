---
title: "Full boot sector linux"
tags: ["linux"]
date: 2022-05-14
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

- run `uname -r`
- remove older kernels under `/boot/`
- run `sudo apt-get autoremove --purge`

```
E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
peter@peter-UX430UAR:~$ sudo apt --fix-broken install
```

- <https://askubuntu.com/questions/668582/false-disk-full-error-apt-get-unable-to-install-or-remove>