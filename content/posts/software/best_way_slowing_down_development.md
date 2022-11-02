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
 
Assign additional costs/consequences for generating a "bug" type ticket, such users/testers will just have to write them down in the comment section.  This essentially makes them undiscoverable. Having to write them down in a comment also ensures no template (Steps to Reproduce) can be specified. If you happen to remember about this bug, you'll have , and just.  Months later someone will find the comment written on the ticket and spend another 30 minutes to see if it was fixed or not. If 


## Tasks

Distribute tasks by topic rather than by technology.  Enforce everyone to work a full stack developer rather than pick up tasks that play into their strength.  This has the added benefit of minimizing communication between your team-members, decreasing any chances of them developing a common understanding of the solution and goals.  Make sure to extend task definition whenever it is nearly finished.

## Microservices

Don't bother and instead rely on the online test environment. Let every developer on the team find this out for themselves. 

## Unit Tests

Should be as large as possible and take forever to run. 

## Pull Requests

Should be as large as possible and receive constant pressure to merge into master.  These two factors will ensure the details of the implementation will not receive the attention needed. Rather, you will enjoy the fun of asking yourself questions like: "why is this not implemented another way" with respect to your master/main branch.

## Retrospective

Cost time. 

## Daly Standup

Vital for pretending you do agile development, but only in name.  Not used for discussing blockers but daily update round for PM/PO as well as 20 minutes techncial discussions only relevant to some people.

## Solution Architecture

Choose the one that best satisfies the requirements, where the requirement is: curing corporate FOMO.  Add, even if the application will never scale and microservices will be 

## Databases

Must run within K8s.