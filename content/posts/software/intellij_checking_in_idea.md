---
title: "Commiting .idea folder to repository"
tags: ["intellij", "java"]
date: 2022-07-28
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

## How to share config between developers?

Q: Can we check in (parts of) the .idea folder as in VS Code?

<https://intellij-support.jetbrains.com/hc/en-us/articles/206544839>

- All files under the .idea directory in the project root except the items that store user-specific settings:
    - workspace.xml
    - usage.statistics.xml
    - shelf directory
    - All the .iml module files (can be located in different module directories) -> applies to IntelliJ IDEA


<https://www.jetbrains.com/help/idea/creating-and-managing-projects.html#share-project-through-vcs>

## SO says...

<https://stackoverflow.com/questions/43198273/which-files-in-idea-folder-should-be-tracked-by-git?r=SearchResults&s=1%7C91.0115>


## Jetbrains official gitignore

https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore

## But but I just want to set required plugin for the whole team...

- <https://www.jetbrains.com/help/idea/sharing-your-ide-settings.html>
- <https://www.jetbrains.com/help/idea/configure-project-settings.html#share-project-through-vcs>
- <https://stackoverflow.com/questions/39875823/how-to-share-installed-plugins-in-intellij-with-team>
- <https://youtrack.jetbrains.com/issue/IDEA-35331>

We need to specify "required plugins" (`(Preferences | Build, Execution, Deployment | Required Plugins)`).