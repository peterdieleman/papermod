---
title: "Jenkins being a Jenkin"
tags: ["jenkins"]
date: 2022-07-08
# weight: 1
# author: "Peter Dieleman"
# showToc: false
# TocOpen: false
draft: true
# hidemeta: false
# comments: false
# description: "A guide on extending the battery life of your linux laptop"
# disableShare: false
# searchHidden: false
---

## Executing a shell script

- <https://serverfault.com/questions/654498/can-jenkins-run-a-shell-script-located-outside-of-the-jenkins-workspace>
- <https://stackoverflow.com/questions/44950361/unable-to-run-sh-steps-inside-docker-agent-script-sh-not-found>
- <https://stackoverflow.com/questions/38143485/how-do-i-make-jenkins-2-0-execute-a-sh-command-in-the-same-directory-as-the-chec>
- <https://serverfault.com/questions/654498/can-jenkins-run-a-shell-script-located-outside-of-the-jenkins-workspace>

These should run on the host:
`sh 'sh ./yourscript.sh'`
`sh './yourscript.sh'`

This should run on the target:
`sh 'script.sh'`

>>> The reason that your script doesn't work is because build.sh is not in your PATH. The Jenkinsfile is running a "sh" script, whose entire contents is the string build.sh. The parent script is in the "@tmp" directory and will always be there - the "@tmp" directory is where Jenkins keeps the Jenkinsfile, essentially, during a run.

