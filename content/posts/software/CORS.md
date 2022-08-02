---
title: "Disabling CORS in local development"
tags: ["java","javascript","spring-boot"]
date: 2022-08-02
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

## Problem

> Access to the XMLHttpRequest at 'http://localhost:8084' from origin 'http://localhost:3000' has been blocked by CORS policy: response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource.

## Frontend side Disabling CORS in 

- <https://stackoverflow.com/questions/46337471/how-to-allow-cors-in-react-js>
- <https://nabil6391.medium.com/avoid-cors-requests-for-a-react-app-2988e0061c1a>
- <https://reactjs.org/docs/cross-origin-errors.html>
- <>

## Backend side

- <https://howtodoinjava.com/spring-boot2/spring-cors-configuration/>


## Should we be doing this in prod?

- <https://zetcode.com/springboot/cors/>
- <https://www.baeldung.com/spring-cors>
- <https://www.baeldung.com/spring-security-cors-preflight>

> If we use Spring Security in our project, we must take an extra step to make sure it plays well with CORS. That's because CORS needs to be processed first. Otherwise, Spring Security will reject the request before it reaches Spring MVC. Luckily, Spring Security provides an out-of-the-box solution:"