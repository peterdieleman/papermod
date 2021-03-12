---
title: "My 1st post"
date: 2020-09-15T11:30:03+00:00
weight: 1
# aliases: ["/first"]
tags: ["first"]
author: "Me"
author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
description: "Desc Text."
disableHLJS: true # to disable highlightjs
disableShare: false
disableHLJS: false
searchHidden: false
cover:
    # image: "<image path/url>" # image path/url
    alt: "test" # alt text
    caption: "test" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page

---
## Background

Developers like to work on Linux, and often install it on their laptops. Either as a standalone system or alongside Windows in a dual boot setup.
However, default Linux installations typically do a worse job than Windows
when it comes to conserving battery power.
This is despite us thinking of Linux as having less 'bloat' and
having an overall smaller footprint.

Linux does have tools to limit battery usage,
and there are guides that explain how to configure Linux on a laptop,
such as
[this one from omgubuntu](https://www.omgubuntu.co.uk/improve-battery-life-linux).
Most of these guides however,
only focus on the basics or
point to a single tool to fix all your problems
(i.e. the very unhelpful: 'just install TLP').
This often leads you to searching the internet for specifics or configurations.

This is an attempt at writing a single 'one-and-done' guide that
can be used to set up Linux on a laptop and
get a battery runtime comparable to that of an equivalent Windows setup.
Here, I will focus on settings that actually yield significant results
and that can be configured without too much hassle.
I will try to use settings are available through the interface when possible.
In this I am assuming you are running a default installation of something like
(K/X)Ubuntu, Manjaro/Arch, or other popular Linux distros for laptop use,
which do have some energy saving settings available in the
system settings interface.
However, some usage of the terminal is required when you want to
run through the whole thing.

Disclaimer: my own installation uses Kubuntu, and I'm not 100% up-to-date with all other Linux distros. When you find info for other distros is missing/incorrect, please contact me (twitter/github).

## Easy Wins
  
The following 
### Screen

In a laptop, the screen is one often one of the biggest consumers of battery.
To prevent the backlight of your laptop screen to consume too much battery,
lots of laptops come with a brightness sensor.
Windows can use this sensor to tune the display brightness depending on lighting conditions.
Most of the time these sensors do not work under Linux due to missing drivers.
Another approach used by Windows is lowering the maximum allowed screen brightness when
running on the battery.

On Linux, neither of these approaches are possible,
or at least not without a lot of hassle.
That said, simple manually bringing down the
brightness of the screen when possible is often more than sufficient.

To make this easier, it is possible to

Actions (5 mins):

- xyz
- xyz
- xyz

### Bluetooth & Wifi

Having your 

Actions  (5 mins):

- xyz
- xyz
- xyz

### CPU frequency scaling

#### tlp

The bread and butter of linux laptop battery management, although not installed 

Actions:

Warning: `powersave` may have some issues, and was switched to `xyz` some time ago.

#### auto-cpufreq

The problem with configuring settings through tlp is that they are static.
This requires finding a sweetspot between battery life and perfomance,
mainly by tuning `max cpu freq` or `pstat param`.
What you really want is a tool that can dynamically .
This kind of CPU throttling is how a default Windows installation is (typically) able to
achieve better battery life than a default linux installation,
while still having decent performance.

This is what [`auto-cpufreq`](https://github.com/AdnanHodzic/auto-cpufreq)

Actions (5 mins):
- xyz 
- xyz

### Video / gpu

#### hardware acceleration (videos)

You don't install linux on a laptop to watch videos all day,
but it's still nice save a little bit of battery when you do.
By default, watching videos through chrome on firefox or chrome can eat quite a bit of battery,
as they don't make use of the GPU (graphics card). 
This means the videos 
This has a variety of reasons:

- h264
- linux being supported, especially when it comes to nvidia

Late 2020, firefox finally gained the, see:

[this post on omgubuntu](https://www.omgubuntu.co.uk/2020/08/firefox-80-release-linux-gpu-acceleration)

Actions (5 mins):
- xyz
- xyz


<!---
TODO: does it even help?
do a few benchmarks on this.
-->

### sleep settings

This is a topic with a long history.

### battery conservation 

limit battery charge to preserve battery life.

## Down The Rabbit Hole

### powertop

Additionally, there is the `powertop` package.
This package was originally developed by intel as
a diagnostic tool for linux distribution developers.
It comes with a host of options,
some of which actually toggle .
However, these settings are quite difficult to get-persistent-on-boot,
and provide little gains over the defaults used by most linux distros.
The most valuable feature is the overview that is provided in the default menu,
which allows you to quickly see what applications are using a lot of battery.
Values are estimates.

`PowerTOP --auto-tune`

### hibernate (aka sleep settings part 2)

Alright

![test](/powertop_overview.png)

![test](/powertop_tunables.png)

### other tips

close apps that you don't nee

### dropbox

dropbox fairly slow to sync (especially when you have many files)
this means it can run for quite a long time
this is no problem on AC, but can drain quite some battery
In KDE it is possible to disable syncing when on battery.
This can be done by running the following script.

dropbox start
dropbox stop