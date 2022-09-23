---
title: "Rest Assured List of Items"
tags: ["Java"]
date: 2022-09-22
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

# Info

<https://stackoverflow.com/questions/43850101/rest-assured-json-body-assertion-for-set-of-values-in-list-regardless-of-posit>

<https://stackoverflow.com/questions/68794097/how-to-get-list-of-objects-with-restassured-instead-of-array-of-objects>

<https://stackoverflow.com/questions/15531767/rest-assured-generic-list-deserialization>

```
List<Person> persons = given()
        .when()
        .get("/person")
        .then()
        .extract()
        .body()
        // here's the magic
        .jsonPath().getList(".", Person.class);
```
