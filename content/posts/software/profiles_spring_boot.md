---
title: "Switching Spring Boot Application.yml properties from IntelliJ"
tags: ["Java", "software"]
date: 2022-03-28
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

Use: `--spring.config.name=myproject`,
where `myproject` is the name of the `*.yml` or `*.properties` file that is stored under the default `/config` directory.
The extension is not required.

<https://docs.spring.io/spring-boot/docs/2.1.13.RELEASE/reference/html/boot-features-external-config.html>