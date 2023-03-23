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

- `maven-compiler-plugin`: This is the most important maven plugin. You almost always use it unknowingly. This plugin compiles your Java code from the standard location Maven specifies e.g. /src/main/java and /src/main/resources.
- `maven-surefire-plugin`: The Maven Surefire plugin is the default plugin for running unit tests. You can also customize the behavior of this plugin by specifying the configuration in pom.xml. The Surefire Plugin has only one goal: surefire:test runs the unit tests of an application.
- `maven-assembly-plugin`: The Maven Assembly plugin is another useful maven plugin that allows you to create your project distribution in zip or tar format, suitable for deployment in the Linux environment.
- `maven-dependency-plugin`: The Maven Dependency Plugin is another mandatory plugin to debug or understand a POM and how you get some dependency (transitively).
- `maven-jar-plugin`: This is the plugin that creates a Java Archive (JAR) file from the compiled project classes and resources.
- `maven-resources-plugin`: This Maven resource plugin is responsible for the copying of Java projects resources to the output directory.
- `spring-boot-maven-plugin`: The Spring Boot maven plugin is one of the useful plugins to develop Java web applications using the Spring Boot library. It collects all the jars on the classpath and builds a single, runnable "über-jar".

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
