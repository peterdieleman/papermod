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

From <https://javarevisited.blogspot.com/2016/08/top-10-maven-plugins-every-java-developer-know.html>:

- `maven-compiler-plugin`: This is the most important maven plugin. You almost always use it unknowingly. This plugin compiles your Java code from the standard location Maven specifies e.g. /src/main/java and /src/main/resources.
- `maven-surefire-plugin`: The Maven Surefire plugin is the default plugin for running unit tests. You can also customize the behavior of this plugin by specifying the configuration in pom.xml. The Surefire Plugin has only one goal: surefire:test runs the unit tests of an application.
- `maven-assembly-plugin`: The Maven Assembly plugin is another useful maven plugin that allows you to create your project distribution in zip or tar format, suitable for deployment in the Linux environment.
- `maven-dependency-plugin`: The Maven Dependency Plugin is another mandatory plugin to debug or understand a POM and how you get some dependency (transitively).
- `maven-jar-plugin`: This is the plugin that creates a Java Archive (JAR) file from the compiled project classes and resources.
- `maven-resources-plugin`: This Maven resource plugin is responsible for the copying of Java projects resources to the output directory.
- `spring-boot-maven-plugin`: The Spring Boot maven plugin is one of the useful plugins to develop Java web applications using the Spring Boot library. It collects all the jars on the classpath and builds a single, runnable "über-jar".
- `maven-bundle-plugin`:

### Maven scaffold

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0  https://maven.apache.org/xsd/maven-4.0.0.xsd">
 <modelVersion>4.0.0</modelVersion>

 <groupId>com.thing.stuff</groupId>
 <artifactId>thing-stuff</artifactId>
 <version>${revision}</version>
 <packaging>pom</packaging>
 <!-- <packaging>jar</packaging> -->
 <!-- <packaging>maven-plugin</packaging>  -->
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

### Maven Packaging Types

See [Baeldung](https://www.baeldung.com/maven-packaging-types)

`jar`: Java archive – or jar – is one of the most popular packaging types. Projects with this packaging type produce a compressed zip file with the .jar extension. It may include pure Java classes, interfaces, resources, and metadata files.

`war`: Simply put, a web application archive – or war – contains all files related to a web application. It may include Java servlets, JSPs, HTML pages, a deployment descriptor, and related resources. Overall, war has the same goal bindings as a jar, but with one exception —the package phase of the war has a different goal, which is war.

`ear`: Enterprise application archive – or ear – is a compressed file that contains a J2EE application. It consists of one or more modules that can be either web modules (packaged as a war file) or EJB modules (packaged as a jar file) or both of them.

`pom`: Among all packaging types, pom is the simplest one. It helps to create aggregators and parent projects. [...] An aggregator or multi-module project assembles submodules coming from different sources. These submodules are regular Maven projects and follow their own build lifecycles. The aggregator POM has all the references of submodules under the modules element. [...] Such projects have the simplest lifecycle that consists of only two steps: install and deploy.

`maven-plugin`: Maven offers a variety of useful plugins. However, there might be cases when default plugins are not sufficient enough. In this case, the tool provides the flexibility to create a maven-plugin, according to project needs.

`bundle`:

## Tangents

- Dynamic vs. Transitive dependencies: <http://sorcersoft.org/project/site/gradle/userguide/dependency_management.html>
- Don't use dynamic versions for your dependencies: <https://blog.danlew.net/2015/09/09/dont-use-dynamic-versions-for-your-dependencies/>
