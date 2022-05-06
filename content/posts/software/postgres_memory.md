---
title: "Postgres Memory Error"
tags: ["postgresql"]
date: 2022-05-06
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
 
- <https://www.postgresql.org/docs/current/runtime-config-resource.html>
- <https://dba.stackexchange.com/questions/64570/postgresql-error-out-of-memory>
- <>

`SQL Error: 0, SQLState: 53200 out of memory`
`Could not extract ResultSet, nested exception is org.hibernate.exception.GenericJDBCException: could not extract ResultSet`

<https://stackoverflow.com/questions/70158261/postgresql-14-2-out-of-memory-failed-on-request-of-size-24576-in-memory-conte>

`Failed on request of size 24576 in memory context "TupleSort main"`

<https://postgrespro.com/list/thread-id/2437174>

`SQL Error: 0, SQLState: 53200`
`ERROR: out of memory Detail: Failed on request of size 152 in memory context "ExecutorState"`