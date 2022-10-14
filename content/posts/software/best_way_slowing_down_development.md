---
title: "Effective ways of slowing down development"
tags: ["java","spring"]
date: 2022-08-14
# weight: 1
# author: "Peter Dieleman"
# showToc: false
# TocOpen: false
draft: true
# hidemeta: false
# comments: false
# description: "A guide on extending the battery life of your linux laptop"
# disableShare: false
# searchHidden: false
---

## Jira
 
- Assign additional costs/consequences for generating a "bug" type ticket, such users/testers will just have to write them down in the comment section.  This essentially makes them undiscoverable.  Even when you remember the about the bug, you'll have no idea, and just.  Months later someone will find the comment written on the ticket and spend another 30 minutes to see if it was fixed or not.

## Microservices

- Don't bother and instead rely on the online test environment. Let every developer on the team find this out for themselves.

## Unit Tests

- Should be as large as possible and take forever to run. 

## Pull Requests

- Should be as large as possible.