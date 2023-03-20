---
title: "Configuring zsh"
tags: ["zsh"]
date: 2023-03-05
# aliases: ["/first"]
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

Some basic zsh stuff.

### Alias

- <https://linuxhint.com/configure-use-aliases-zsh/>

### CLI tools

- <https://dev.to/stuartcreed/how-to-add-aliases-to-your-terminal-on-mac-os-53dl>

### zsh color

- <https://scriptingosx.com/2019/07/moving-to-zsh-06-customizing-the-zsh-prompt/>

### Simple Cron (type) job

`export VISUAL=nano` or `export EDITOR=nano` for noob-mode, and don't forget to `chmod +x` your files.

Example: `43 * * * * ~/scripts/notes.sh >/tmp/stdout.log 2>/tmp/stderr.log`

- <https://www.geekbitzone.com/posts/macos/crontab/macos-schedule-tasks-with-crontab/>
- <https://towardsdatascience.com/a-step-by-step-guide-to-scheduling-tasks-for-your-data-science-project-d7df4531fc41>
- <https://serverfault.com/questions/332255/how-to-backup-crontab-e-files>
- <https://apple.stackexchange.com/questions/38861/where-is-the-cron-log-file-in-macosx-lion>

### Preferred Shebang Line?

User preferred shell: `#!/usr/bin/env bash`

Source: <https://scriptingosx.com/2017/10/on-the-shebang/>

### zsh vs. bash differences

Q: is zsh a superset of bash?

A: not a strict superset, be aware of:

- Arrays (zsh arrays start at 1, not at 0)
- Wildcard expansion

Extra info:

- <https://linuxhint.com/differences_between_bash_zsh/>
- <https://apple.stackexchange.com/questions/361870/what-are-the-practical-differences-between-bash-and-zsh>
- <https://www.educative.io/answers/what-is-the-difference-between-zsh-and-bash>

### Themes

- [oh-my-zsh](https://ohmyz.sh/#install)
- [smashing magazine post](https://www.smashingmagazine.com/2015/07/become-command-line-power-user-oh-my-zsh-z/)

### Videos

- <https://commandlinepoweruser.com/>
