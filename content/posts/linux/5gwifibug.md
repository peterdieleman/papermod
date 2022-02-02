---
title: "Ubuntu 20.04 and slow 5g wifi speed"
date: 2021-04-05T11:38:07+02:00
# weight: 1
# aliases: ["/first"]
tags: ["Linux"]
author: "Peter Dieleman"
# author: ["Me", "You"] # multiple authors
showToc: false
TocOpen: false
draft: true
hidemeta: false
comments: false
description: "When connected to a 5ghz wifi network you may experience slow network speeds under 
Ubuntu 20.04. This may be due to a change in the default wifi power saving mode in Ubuntu 20.04."
disableHLJS: false # to disable highlightjs
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
describes limited network speeds when connected to a 5ghz network.
This bottleneck only appears as a problem for those people that are lucky enough to
have fast enough broadband.
For example, on my Zenbook I obtained average download speeds no greater than 25Mpbs,
while easily obtaining 250Mpbs/25Mpbs Up/Down on my Macbook,
which hits the capped speed of my IP.
This is on the the exact same 5g network and from the exact same location in the house.
On top of this the speed is not only slower, but also jump all over the place.

The solution for me was to change the default Networkmanager powersave mode,
although some people in the thread above report other fixes.
This can be done by running:

```bash
sudo nano /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
```

and changing the value from `3` to a `2`.
Hit `Control+X` and `Y` when prompted to save your changes. Reboot.
This disables the powersave mode for your wifi driver [^1].
To check if this had any effect,
type `iwconfig` and see whether the value after 'Power management:' reads 'off'.

In the case it still reads 'on', your tlp configuration might be to blame.
Check that the power saving mode is disabled in the tlp config file,
by opening a terminal and typing
`sudo nano /etc/tlp.conf`.
Look for the following lines:

```bash
# WiFi power saving mode: on=enable, off=disable; not supported by all adapters.
WIFI_PWR_ON_AC=off
WIFI_PWR_ON_BAT=on
```

check that at least the 'AC' setting is set to 'off'.
Hit `Control+X` and `Y` when prompted to save your changes.
Reboot.
Consider turning your 'BAT' setting to 'off' as well in the case you experience 
very low or inconsistent 5g wifi speeds.

For troubleshooting network speeds I like to use the
[Ookla command line interface](https://www.speedtest.net/apps/cli).
This can be used to check whether your changes have actual effect.

[^1]: For an explanation on the possible values, see
[this gist](https://gist.github.com/jcberthon/ea8cfe278998968ba7c5a95344bc8b55).