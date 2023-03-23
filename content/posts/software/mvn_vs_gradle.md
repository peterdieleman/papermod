---
title: "Mvn vs. Gradle"
tags: ["java"]
date: 2022-07-14
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

## Comparisons

- <https://phauer.com/2018/moving-back-from-gradle-to-maven/>
- <https://gradle.org/gradle-vs-maven-performance/>
- <https://dzone.com/articles/gradle-vs-maven>
- <https://www.baeldung.com/ant-maven-gradle>

## Further Gradle Info

- <https://tomgregory.com/5-reasons-to-switch-to-the-gradle-kotlin-dsl/>
- <https://www.oreilly.com/library/view/gradle-beyond-the/9781449373801/ch04.html>

## Further Maven Info

### Essential Maven Plugins

From: <https://javarevisited.blogspot.com/2016/08/top-10-maven-plugins-every-java-developer-know.html>:

- maven-compiler-plugin

### Maven scaffold

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0  https://maven.apache.org/xsd/maven-4.0.0.xsd">
 <modelVersion>4.0.0</modelVersion>

 <groupId>com.thing.stuff</groupId>
 <artifactId>thing-stuff</artifactId>
 <version>${revision}</version>
 <packaging>pom</packaging>

 <modules>
  ...
 </modules>

 <distributionManagement>
  ...
 </distributionManagement>

 <properties>
  ...
 </properties>

 <dependencies>
  ...
 </dependencies>

 <build>
  ...
 </build>

 <profiles>
  ...
 </profiles>

</project>
```

## Tangents

- Dynamic vs. Transitive dependencies: <http://sorcersoft.org/project/site/gradle/userguide/dependency_management.html>
- Don't use dynamic versions for your dependencies: <https://blog.danlew.net/2015/09/09/dont-use-dynamic-versions-for-your-dependencies/>
