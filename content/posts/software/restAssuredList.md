---
title: "Notes on Unit testing using Rest Assured & Junit"
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

# Unpacking a List of results

- <https://stackoverflow.com/questions/43850101/rest-assured-json-body-assertion-for-set-of-values-in-list-regardless-of-posit>
- <https://stackoverflow.com/questions/68794097/how-to-get-list-of-objects-with-restassured-instead-of-array-of-objects>
- <https://stackoverflow.com/questions/15531767/rest-assured-generic-list-deserialization>
- <https://stackoverflow.com/questions/49324680/how-to-verify-that-array-contains-object-with-rest-assured>
- <https://www.james-willett.com/rest-assured-extract-json-response/>
- <https://devqa.io/parse-json-response-rest-assured/>

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

## Further Notes on Logging

How to output of Asserts (expected, actual) to console, for failing _as well as_ succesfull tests?

- <https://stackoverflow.com/questions/3963708/gradle-how-to-display-test-results-in-the-console-in-real-time>
- <https://stackoverflow.com/questions/3963708/gradle-how-to-display-test-results-in-the-console-in-real-time>
- <https://github.com/radarsh/gradle-test-logger-plugin>
