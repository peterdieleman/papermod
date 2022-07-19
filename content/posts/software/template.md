---
title: "Binding @RequestParam through a POJO"
tags: ["java"]
date: 2022-07-18
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

## Long List of Query params / request parameters

<http://dolszewski.com/spring/how-to-bind-requestparam-to-object/>

"You also need to mark the POJO parameter in controller’s method with the @Valid annotation. This way you inform Spring that it should execute validation on the binding step."

Downsides: are not able to map query param to a nice variable name in case the ones in URL are shortened  (`q` instead of `query`), unless you specify a different getter.

## Note

> In many cases, it makes much more sense to use @NotBlack instead @NotNull as it also covers the undesired empty string problem (a string with the length of zero).