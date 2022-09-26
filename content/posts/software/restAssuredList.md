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
- <https://github.com/radarsh/gradle-test-logger-plugin>
- <https://mkyong.com/gradle/gradle-display-test-results-in-console/>
- <https://stackoverflow.com/questions/56436541/assertj-log-all-passing-and-failing-assertions>
- <https://stackoverflow.com/questions/56436541/assertj-log-all-passing-and-failing-assertions>
- <https://github.com/assertj/assertj/issues/1518>
- <https://assertj.github.io/doc/#assertj-core-assertion-description-consumer>
- <https://stackoverflow.com/questions/65113051/junit5-assertj-create-log-entry-on-assertion>
- <https://stackoverflow.com/questions/28994316/can-you-add-a-custom-message-to-assertj-assertthat>
- <https://stackoverflow.com/questions/57334283/is-it-possible-to-log-the-name-and-values-of-fields-being-asserted-along-with-co>
