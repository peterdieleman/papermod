---
title: "Asus 430 Charging issues"
tags: ["linux"]
date: 2022-02-04
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

## Charging issue

Asus 430 models running linux sometimes suffer from charging issues while suspended, see:
[this issue](https://forums.tomsguide.com/threads/computer-doesnt-charge-when-on-suspend.439594/).
Charging while turned off or turned on works without any issues.

For me, this was resolved by adding
 `mem_sleep_default=deep`
 to the kernel command line.
This can be done by going to
`sudo nano /etc/default/grub`
and change the line:

`GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"`

to

`GRUB_CMDLINE_LINUX_DEFAULT="quiet splash mem_sleep_default=deep"`.

Not only does this enable charging while your laptop is suspended,
it should also
[lower the amount of battery drain](https://wiki.archlinux.org/title/ASUS_Zenbook_UX430/UX530#Suspend).
