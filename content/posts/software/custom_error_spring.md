---
title: "Customize error message Spring Boot"
tags: ["spring-boot", "java", "error"]
date: 2022-04-12
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

- <https://stackoverflow.com/questions/62561211/spring-responsestatusexception-does-not-return-reason>
- <https://www.baeldung.com/global-error-handler-in-a-spring-rest-api>
- <https://www.amitph.com/spring-rest-api-custom-error-messages/>
- <https://auth0.com/blog/get-started-with-custom-error-handling-in-spring-boot-java/>
- <https://stackoverflow.com/questions/45317638/how-to-catch-accessdeniedexception-in-spring-boot-rest-api>
- <https://stackoverflow.com/questions/59302621/custom-message-in-spring-accessdeniedexception>
- <https://dzone.com/articles/best-practice-for-exception-handling-in-spring-boo>

- `@ControllerAdvice` annotation

## Note

- AccessDeniedException needs to be taken care of in filter chain
