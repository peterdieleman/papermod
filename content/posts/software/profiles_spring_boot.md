---
title: "Switching Spring Boot Application.yml properties from IntelliJ"
tags: ["java", "spring-boot", "intellij"]
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

## Further Documentation

<https://www.baeldung.com/spring-yaml>
<https://baeldung-cn.com/spring-yaml-vs-properties>

<https://docs.spring.io/spring-boot/docs/1.0.1.RELEASE/reference/html/howto-properties-and-configuration.html>

<https://docs.spring.io/spring-boot/docs/1.0.1.RELEASE/reference/html/howto-properties-and-configuration.html#howto-change-configuration-depending-on-the-environment>

need:

spring.config.activate.on-profile: "profile_name"

example:

```yaml
spring: # default config without profile name
.
.
.

---

spring:
    config:
        activate:
            on-profile: "profile name"
```

In conjunction with: `./gradlew run --args='--spring.profiles.active=profile_name'`

Can make this even more complicated when activating multiple profiles at once with overlapping properties, in that case the precedence order of profiles needs to be defined.

## From IntelliJ

Add the following as an environment variable when right clicking on the configuration in the top-left corner: `spring.profiles.active=profile_name`
