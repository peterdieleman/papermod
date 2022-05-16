---
title: "Jackson exclude null values"
tags: ["template"]
date: 2022-05-16
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

## Sources

- <https://stackoverflow.com/questions/64868946/how-to-not-return-null-value-in-responseentity>
- <https://www.baeldung.com/jackson-ignore-null-fields>
- <https://stackoverflow.com/questions/11757487/how-to-tell-jackson-to-ignore-a-field-during-serialization-if-its-value-is-null>

## Issue

We have the following setting in the `application.yml` file, but it is ignored:

```yml
spring:
    jackson:
        default-property-inclusion: non_null
```

Manually annotating the classes with 
`@JsonInclude(JsonInclude.Include.NON_NULL)`
 did reinstate the wanted behaviour. However, this is painful for classes that are pulled from libraries.

Root cause seems to be related to the following: <https://stackoverflow.com/questions/62819472/spring-jackson-default-property-inclusion-ignored>.