---
title: "Persisting ArrayList"
tags: ["java","spring"]
date: 2022-08-03
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

<https://stackoverflow.com/questions/25415738/how-to-persist-arraylist-within-spring-entity-class>

Need: `@ElementCollection` & `@CollectionTable(name="abc")` ?

<https://thorben-janssen.com/hibernate-tips-elementcollection/>

Does this still require a separate table?

<https://stackoverflow.com/questions/26512916/what-column-type-is-required-when-using-elementcollection-with-jpa>


<https://www.postgresql.org/docs/current/arrays.html>

<https://sajithv.medium.com/spring-jpa-data-with-postgres-array-types-a6cc4be421e2>

## Hibernate & Arrays

From: [Vlad Mihalcea](https://vladmihalcea.com/postgresql-array-java-list/)

" Hibernate ORM does not support ARRAY column types"

Also see: <https://stackoverflow.com/questions/1647583/how-to-map-a-postgresql-array-with-hibernate>