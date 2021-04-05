---
title: "Ubuntu 20.04 and slow 5g wifi speed"
date: 2021-04-05T11:38:07+02:00
# weight: 1
# aliases: ["/first"]
tags: ["Linux","wifi","energy saving"]
author: "Peter Dieleman"
# author: ["Me", "You"] # multiple authors
showToc: false
TocOpen: false
draft: false
hidemeta: false
comments: false
description: "When connected to a 5ghz wifi network you may experience slower speeds
            than Windows, or then when connected to a the same router on a 2.4ghz network.
            This may be due to a change in the default wifi power saving mode in Ubuntu 20.04."
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

[This post on askubuntu](https://askubuntu.com/questions/1230525/ubuntu-20-04-network-performance-extremely-slow?newreg=c680273ce1dc4c26841ae12de89b0f7e)
describes limited network speeds when connected to a 5ghz network 
The solution for me seemed to be editing the default Networkmanager powersave mode,
although some people report other fixes. This can be done by running:

```bash
sudo nano /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
```

and changing the value from `3` to a `2`.
Hit `Control+X` and then, `Y` when prompted to save your changes,
and reboot.
This disables the powersave mode for your wifi driver [^1].
To check if this had any effect,
type `iwconfig` and see whether the value after 'Power management:' reads 'off'.

For troubleshooting network speeds I like to use the
[Ookla command line interface](https://www.speedtest.net/apps/cli).

[^1]: For an explanation on the possible values, see
[this gist](https://gist.github.com/jcberthon/ea8cfe278998968ba7c5a95344bc8b55).