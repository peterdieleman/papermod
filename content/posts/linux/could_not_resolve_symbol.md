---
title: "BIOS ERROR (bug)"
tags: ["linux","kernel"]
date: 2022-08-01
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

`BIOS ERROR (bug): Could not resolve symbol [\_PR.PR00._CPC], AE_NOT_FOUND (2022103730/psargs-330)`

- <https://github.com/intel/linux-intel-lts/issues/22>
- <https://bugzilla.kernel.org/show_bug.cgi?id=213023>

> `The fix was reverted recently in the upstream commit 2ca8e6285250 (which was backported to stable trees, too), hence the problem resurfaced. That said, we came back to square.