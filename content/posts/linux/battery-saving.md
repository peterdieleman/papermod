---
title: "Linux Laptops & Battery Life    "
date: 2020-09-15T11:30:03+00:00
weight: 1
# aliases: ["/first"]
tags: ["linux","tlp","guide"]
# author: "Peter Dieleman"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
description: "A guide on extending the battery life of your linux laptop"
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

Developers like to work on Linux, and often install it on their laptops.
Either as a standalone system or alongside Windows in a dual boot setup.
However,
default Linux installations typically do a worse job than Windows
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
Most settings in this guide are configured through the command line or
by editing config files.
This guide should therefore work fairly universally across different linux distros.
However, some settings are more easily configured through the GUI,
and in this I will assume you are running Kubuntu.
However, other popular Linux distros,
such as or Manjaro/Arch,
likely offer very similar settings.

Note:
When you find that info for your Linux installation is missing/incorrect,
please contact me (twitter/github).

# Easy Wins (30 min)
  
The following are easy wins that can significantly extend the total battery life of your laptop and
can be configured in approximately half an hour.
In case you have even less time:
- The guide is ordered following hardware items that consume most battery,
  and likewise,
  offer most room for improvement.
- Each section provides a little bit of context.
  If you want to speedrun this guide, skip ahead to the **Actions** subsections.

## Screen

On a laptop,
the screen is one often one of the biggest consumers of battery.
To prevent the backlight of your laptop screen to consume too much battery,
lots of laptops come with a brightness sensor.
Windows can use this sensor to tune the display brightness depending on lighting conditions.
Most of the time these sensors do not work under Linux due to missing drivers.
Another approach used by Windows is lowering the maximum allowed screen brightness when
running on the battery.

On Linux, neither of these approaches are possible,
or at least not without a lot of hassle.
That said,
simple manually bringing down the
brightness of the screen when possible is often more than sufficient.
In addition,
most Linux distros offer some settings to make sure your laptop's screen does not
inadvertently eat a lot of battery when running from your battery.

### Actions (3 min): 

This assumes you are running Kubuntu:

- Navigate to the `Energy Saving` panel in the `System Settings`
- Select the `On Battery` tab 
  - Enable the `Screen brightness` option and
  bring the slider down to your desired level.
  - Enable the `Keyboard backlight` option and
  bring the slider down to your desired level.
  - Enable the `Dim screen` option and
  set a time after which this should take effect.
  - Enable the `Screen Energy Saving` and
  set a time after which the screen should turn off.

## CPU 

Together with your screen,
the CPU (processor) of your laptop can be one of the big consumers of your laptop's battery. 
This section describes two tools, 'tlp' and 'auto-cpufreq',
that work in conjunction,
and limit the power consumption of your cpu.

### TLP

TLP[^1] is a command line tool,
and is considered the bread and butter of Linux laptop battery management.
That said,
very few Linux distros install it by default and the 
[actions section below](#actions-tlp)
will therefore also describe installation instructions.
In addition to settings that control your CPU,
TLP has a lot of configurable settings that control other pieces of hardware,
such as your bluetooth and wifi.
All these settings are configured by editing the config file,
which lives under `/etc/tlp.conf`.
It is easy to lose yourself in this sea of config
and ~~spend~~ waste a lot of time.[^2]
In this guide,
I'll focus on 3 or 4 settings that actually yield significant results and
that may benefit from a bit of tuning.

TLP can limit CPU power consumption by limiting the maximum frequency of the CPU.
CPUs can consume a lot of battery when running at 'full power'.
In turn this generates a lot of heat, 
which necessitates the use of fan(s).
Together this can rapidly drain your battery.
By tuning the maximum CPU frequency we can make sure that we limit power consumption
while still having acceptable perfomance for most tasks.

[^1]: [TLP project on github](https://github.com/linrunner/TLP)
[^2]: [Dedoimedo: Don't go chasing power management](https://www.dedoimedo.com/computers/linux-power-management-tlp.html)

### auto-cpufreq

Simply limiting the maximum frequency of your CPU helps improving the battery life of your laptop.
However, this is approach is still fairly static[^3]
Additional benefits can be gained by 'throttling' your CPU.
Basically, scaling up the maximum frequency of the CPU when necessary,
but scaling
This is where [`auto-cpufreq`](https://github.com/AdnanHodzic/auto-cpufreq) comes in. 

A more extensive explanation of what `auto-cpufreq` offers over TLP can be found
[here](https://github.com/AdnanHodzic/auto-cpufreq#why-do-i-need-auto-cpufreq).
is one approach to extend battery life.
configuring settings through tlp is that they are static.
This requires finding a sweetspot between battery life and perfomance,
mainly by tuning `max cpu freq` or `pstat param`
(if suppored by your cpu).
What you really want is a tool that can dynamically .
This kind of CPU throttling is how a default Windows installation is (typically) able to
achieve better battery life than a default linux installation,
while still having decent performance.

Some guidelines:

- tune 
- Otherwise play around with p=0.25, p=0.5, p=0.8
- 

This is what 

[^3]: This is an oversimplification.
TLP also offers the ability to change the
'CPU frequency scaling governor' from
'performance' to
'powersave.
However, 


### Actions (10 mins): {#actions-tlp}

1. xyz.
2. xyz.
3. xyz.
4. xyz.

## Bluetooth & Wifi

Although the amount of battery bluetooth/wifi chips consume when
you are not connected to anything is typically relatively modest,
it's still a waste to have these turned on when you do not
intend to connect to any devices/networks.
Most Linux distros offer options through the GUI that disable
wifi and/or bluetooth when disconnecting from AC.
This is a somewhat blunt instrument that can interfere with work,
e.g. when you're in the middle of a Google Meet call using your 
bluetooth headphones and running to a more quiet room. 
TLP offers a slightly more refined option that only disables
bluetooth/wifi when you are not connected to any devices/networks.
The [actions](tlp-radio-actions) below result in the following behaviour:

- Disconnecting from AC:
  - disable bluetooth when you are not connected to any devices,
  - disable wifi when you are not connected to any networks.
- Connecting to AC:
  - Enable bluetooth and wifi.

### Actions (2 min) {#tlp-radio-actions}

- Follow steps **TODO** in the [tlp & auto-cpufreq instructions above](#actions-tlp).
- `sudo nano etc/tlp.conf`
- Uncomment `DEVICES_TO_DISABLE_ON_BAT_NOT_IN_USE = "bluetooth wifi wwan"`.
- Uncomment `DEVICES_TO_ENABLE_ON_AC" = "bluetooth wifi wwan"`.
- Hit `control-X` and hit `Y` when prompted for `Save modified buffer?`.


## Video / gpu

### hardware acceleration (videos)

You don't install linux on a laptop to watch videos all day,
but it's still nice save a little bit of battery when you do.
By default, watching videos through chrome on firefox or chrome can eat quite a bit of battery,
as they don't make use of the GPU (graphics card). 
This means the videos 
This has a variety of reasons:

- h264
- linux being supported, especially when it comes to nvidia

Late 2020, firefox finally gained the, see:

[this post on omgubuntu]
(https://www.omgubuntu.co.uk/2020/08/firefox-80-release-linux-gpu-acceleration)

Actions (5 mins):
- xyz
- xyz


<!---
TODO: does it even help?
do a few benchmarks on this.
-->

## sleep settings

This is a topic with a long history.

# Diminishing Returns

This is the 

## battery conservation 

limit battery charge to preserve battery life.

## powertop

Additionally, there is the `powertop` package.
This package was originally developed by intel as
a diagnostic tool for linux distribution developers.
It comes with a host of options,
some of which actually toggle .
However, these settings are quite difficult to get-persistent-on-boot,
and provide little gains over the defaults used by most linux distros.
The most valuable feature is the overview that is provided in the default menu,
which allows you to quickly see what applications are using a lot of battery.
Values are estimates.[^1]

[^1]: To say down here.

`PowerTOP --auto-tune`

## hibernate (aka sleep settings part 2)

Alright

Logo: ![alt](/powertop_overview.png#center "Title")

Test: ![alt](/powertop_tunables.png#center "Title")

## other tips

close apps that you don't nee

## dropbox

dropbox fairly slow to sync (especially when you have many files)
this means it can run for quite a long time
this is no problem on AC, but can drain quite some battery
In KDE it is possible to disable syncing when on battery.
This can be done by running the following script.

dropbox start
dropbox stop


### Undervolting

### darkmode

A lot of developers have darkmode enabled by default. A lot of people have darkmode enabled. 

# Further info

[An extensive guide to optimizing a linux battery for battery life and performance](https://amanusk.medium.com/an-extensive-guide-to-optimizing-a-linux-laptop-for-battery-life-and-performance-27a7d853856c)