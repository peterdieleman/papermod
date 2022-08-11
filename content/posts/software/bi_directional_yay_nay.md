---
title: "Spring Data: bi-directional relationships"
tags: ["java","spring"]
date: 2022-08-10
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

## Should we map both sides?

- <https://stackoverflow.com/questions/30464782/how-to-maintain-bi-directional-relationships-with-spring-data-rest-and-jpa/30474303#30474303>

> It usually simplifies the matter if you try not to use bi-directional relationship whenever possible and rather fall back to a repository to obtain all the entities that make up the backside of the association.

- <https://thorben-janssen.com/best-practices-many-one-one-many-associations-mappings/>
- <https://twitter.com/odrotbohm/status/603247455094841344>
- <https://stackoverflow.com/questions/48754783/do-i-have-to-set-both-sides-for-a-bidirectional-relationship>

## If Yes - Do we have to manually update both sides?

- <https://stackoverflow.com/questions/7546161/update-bidirectional-manytomany-from-both-sides>
- <https://stackoverflow.com/questions/20068742/jpa-updating-bidirectional-association>
- <https://hellokoding.com/jpa-one-to-many-relationship-mapping-example-with-spring-boot-maven-and-mysql/>

> CascadeType.ALL is for propagating the CRUD operations on the parent entity to the child entities. CascadeType.ALL should be used for small child collection only as it can cause performance issue, we will dig more into this in the later part

- <https://vladmihalcea.com/jpa-hibernate-synchronize-bidirectional-entity-associations/>
- <https://stackoverflow.com/questions/5360795/what-is-the-difference-between-unidirectional-and-bidirectional-jpa-and-hibernat/48681422#48681422>

> First, the @ManyToOne association uses the FetchType.LAZY strategy because by default @ManyToOne and @OneToOne associations use the FetchType.EAGER strategy which is bad for performance.

## Common (recursion) problems

- <https://www.baeldung.com/jackson-bidirectional-relationships-and-infinite-recursion>


## Spring Data Jpa Repository

<https://www.baeldung.com/spring-data-crud-repository-save>