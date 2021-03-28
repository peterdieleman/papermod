---
title: "Linux Laptops & Battery Life    "
date: 2021-01-15T11:30:03+00:00
weight: 1
# aliases: ["/first"]
tags: ["Linux","TLP","guide","auto-cpufreq","laptop"]
# author: "Peter Dieleman"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
description: "A guide on extending the battery life of your linux laptop"
# disableHLJS: true # to disable highlightjs
disableShare: false
searchHidden: false
# cover:
#     # image: "<image path/url>" # image path/url
#     alt: "test" # alt text
#     caption: "test" # display caption under cover
#     relative: false # when using page bundles set this to true
#     hidden: false # only hide on current single page

---

Linux can easily be installed on many different types of hardware,
including laptops.
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
In addition, I will also be assuming your laptop either contains an intel,
AMD,
or other x86-64 CPU.

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

### Actions (5 min)

This assumes you are running Kubuntu:

- Navigate to the 'Energy Saving' panel in the 'System Settings'
- Select the 'On Battery' tab, and:
  - enable the 'Screen brightness' option and
  bring the slider down to your desired level,
  - in case your laptop has a keyboard backlight:
  enable the 'Keyboard backlight' option and bring the slider down to your desired level,
  - enable the 'Dim screen' option and
  set a time after which this should take effect,
  - enable the 'Screen Energy Saving' and
  set a time after which the screen should turn off.

## CPU 

Together with your screen,
the CPU (processor) of your laptop can be one of the big consumers of your laptop's battery.
This section describes two tools, 'TLP' and 'auto-cpufreq',
that work in conjunction,
and limit the power consumption of your cpu.

### TLP

TLP[^1] is a command line tool,
and is considered the bread and butter of Linux laptop battery management.
That said,
very few Linux distros install it by default.
The
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
I will focus on 3 or 4 settings that actually yield significant results and
that may benefit from a bit of tuning.

TLP can limit CPU power consumption by limiting the maximum frequency of the CPU.
CPUs can consume a lot of battery when running at 'full power'.
In turn this generates a lot of heat,
which necessitates the use of fan(s).
Together this can rapidly drain your battery.  
By tuning the maximum CPU frequency we can make sure that we limit power consumption
while still having acceptable performance for most tasks.

[^1]: [TLP project on github](https://github.com/linrunner/TLP)
[^2]: [Dedoimedo: Don't go chasing power management](https://www.dedoimedo.com/computers/linux-power-management-tlp.html)

### auto-cpufreq

Simply limiting the maximum frequency of your CPU helps improving
the battery life of your laptop.
However, this is approach is still fairly static[^3]
Additional benefits can be gained by 'throttling' your CPU.
Basically this means scaling up the maximum frequency of the CPU when
processing power is required,
but also scaling it down to preserve power whenever possible.
This practice can significantly extend your battery life when
running typical intermittent workloads,
such as a combination of text editing and web browsing.

[^3]: This is an oversimplification.
TLP also offers the ability to change the
'CPU frequency scaling governor' from
'performance' to
'powersave.
However, auto-cpufreq is more extensive in its approach.

Of course you don't want to do constantly change your CPUs frequency by hand,
which is where ['auto-cpufreq'](https://github.com/AdnanHodzic/auto-cpufreq) comes in.[^4]
In the
[actions section below](#actions-TLP)
I will explain how to install & configure TLP and auto-cpufreq alongside each other.

[^4]: A more extensive explanation of what auto-cpufreq offers over TLP can be found
[here](https://github.com/AdnanHodzic/auto-cpufreq#why-do-i-need-auto-cpufreq)

### Actions (20 mins) {#actions-tlp}

1. Open a terminal.
2. Run `sudo apt install tlp`.
3. To install auto-cpufreq, type in `sudo snap install auto-cpufreq`.
   Alternatively,
   follow the instructions
   [here](https://github.com/AdnanHodzic/auto-cpufreq#installing-auto-cpufreq).
4. Run `sudo auto-cpufreq --install`
5. Back-up your TLP configuration by running:\
   `cp /etc/tlp.conf ~/tlp.conf`.[^5]
6. Check that both TLP and auto-cpufreq are installed correctly.
   1. Restart your laptop. Open a terminal.
   2. Check that TLP is enabled by running:\
      `tlp-stat -c`.\
      The very first line should contain:\
      `TLP_ENABLE="1"`.\
      In case it does not, go in and edit the file as in **step 7** below,
      and change the parameter.
   3. Check that auto-cpufreq is activated by typing:\
      `systemctl status snap.auto-cpufreq.service.service`,\
      when you have installed the package using snap, or:\
      `systemctl status auto-cpufreq`,\
      when you went the other route.
      This should display some information telling `auto-cpufreq` is activated.
7. Run `sudo nano /etc/tlp.conf` to open the TLP config file in nano.
8. In the config file,
   make sure the following lines are commented out,
   by making sure they start with a `#`:
   - `#CPU_SCALING_GOVERNOR_ON_BAT`
   - `#CPU_SCALING_MIN_FREQ_ON_BAT`
   - `#CPU_SCALING_MAX_FREQ_ON_BAT`
   - `#CPU_HWP_ON_BAT`
   - `#CPU_MIN_PERF_ON_BAT`
9. This enables TLP and auto-cpufreq on your machine,
   which should already significantly improve the battery life of your laptop.
   In my case,
   I found it beneficial to tune the CPU frequency limit to further increase battery life.
   This may require a bit of tuning.
   Don't fret!
   You only need to adjust a single parameter:
   exactly which one depends on your system.
10. In case your laptop has an intel CPU, follow the steps below:
    1. Double check whether your CPU is indeed supported, by running:\
      `sudo tlp-stat --processor`.\
      If the resulting output looks something like this:\
      `/sys/.../scaling_driver = intel_pstate`,\
      it means your CPU is using `intel_pstate` scaling driver,
      and you can proceed to **to step 10.2 below**.
      Otherwise, proceed **to step 11 below.** 
    2. Type: `sudo nano /etc/tlp.conf` to edit your TLP config file.
      Uncomment the `CPU_MIN_PERF_ON_BAT = XX` parameter,
      and replace `XX` with a number between 0 and 100.
      Lower values mean longer battery life, but also slower performance.
      Suggested values for experimenting are 25, 50, or 75.
      Enter a value, hit `control-X` and `Y` when prompted for
      `Save modified buffer?`
      See how you like the responsiveness of your system when operating from battery,
      and either increase or decrease the `XX` value until you are satisfied.
11. In case your laptop has an AMD, or an older intel CPU,
    follow the steps below.
    1. Open a terminal and type `sudo tlp-stat -p`,
    2. Note down the values for 'scaling_min_freq' and 'scaling_max_freq'.
    3. Type: `sudo nano /etc/tlp.conf` to edit your TLP config file.
    4. Find the line containing:\
       `CPU_SCALING_MAX_FREQ_ON_BAT =  YY`,\
       and uncomment it
       (i.e. remove the leading `#`).
       To reduce the frequency on battery,
       enter a value lower than the maximum value.[^6]
       Hit `control-X` and `Y` when prompted for
      `Save modified buffer?`
       See how you like the responsiveness of your system when operating from battery,
       and either increase or decrease the `YY` value until you are satisfied.

[^5]: This isn't absolutely necessary, but doesn't hurt either.
A default configuration is also stored in `etc/default/tlp.conf`,
or `/usr/share/tlp/defaults.conf`,
depending on your installation. 
To restore, run the command in reverse:\
`sudo cp ~/tlp.conf /etc/tlp.conf`,
where the sudo is necessary to copy into the `/etc/` directory.

[^6]: The official TLP guide notes  that:\
_'Lowering the max frequency on battery power does not conserve power; 
best results are achieved by the ondemand governor without frequency limits'._
This statement is either lacking in nuance or outdated.
It is certainly the case that setting this limit too low
will unnecessarily cripple your system
and indeed may even reduce your battery life,
as certain tasks will run over a longer time.
However, higher CPU frequencies may result in:\
(1) higher temperatures, requiring active cooling with a fan,\
(2) an exponentially higher power consumption, see:
[this medium post](https://amanusk.medium.com/an-extensive-guide-to-optimizing-a-linux-laptop-for-battery-life-and-performance-27a7d853856c).\
These issues are no problem when running running on AC,
but on battery we can find a sweetspot between performance and battery life.
 
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

### Actions (5 min) {#tlp-radio-actions}

- Make sure that TLP is installed on your system by following
  **steps 1, 2, 6.1, 6.2**
  in
  [TLP & auto-cpufreq instructions above](#actions-tlp).
- Edit your TLP configuration by typing `sudo nano etc/tlp.conf`
- Uncomment
  (remove the leading `#`)
  the following line:\
  `DEVICES_TO_DISABLE_ON_BAT_NOT_IN_USE = "bluetooth wifi wwan"`.
- Uncomment
  (remove the leading `#`)
  the following line:\
  `DEVICES_TO_ENABLE_ON_AC" = "bluetooth wifi wwan"`.
- Hit `control-X` and hit `Y` when prompted for `Save modified buffer?`.

# Future Topics

- Undervolting
- Sleep and hibernate settings
- Battery conservation
- Hardware acceleration for video (Chrome / Firefox)
- Powertop
- Darkmode
- An easy way to measure real life battery time