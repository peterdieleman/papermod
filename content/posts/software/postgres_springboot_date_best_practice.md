---
title: "PostgreSQL & Spring Boot Dates"
tags: ["Java"]
date: 2022-02-18
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

## Notes

The SQL standard requires that writing just
`timestamp` be equivalent to
`timestamp without time zone`,
and PostgreSQL honors that behavior.
`timestamptz` is accepted as an abbreviation for
`timestamp with time zone`;
this is a PostgreSQL extension.

```text
Precision can be specified for time, timestamp, and interval types, and can range from 0 to 6. 
If no precision is specified in a constant specification, 
it defaults to the precision of the literal value (but not more than 6 digits).
```

```text
ISO 8601 specifies the use of uppercase letter T to separate the date and time.
PostgreSQL accepts that format on input, but on output it uses a space rather than T, as shown above. 
This is for readability and for consistency with RFC 3339 as well as some other database systems.
```

## Mapping

`Date` columm can be mapped by:

- `java.sql.Date`
- `java.util.Date`
- `LocalDate`

`Timestamp` column can be mapped by:

- `java.sql.Timestamp`
- `java.util.Date`
- `LocalDateTime`
- `OffsetDateTime`
- `ZonedDateTime`

## Best Practice?

- Use ISO-8601 where possible
- Save date in UTC timestamp, only make zoned when displaying to the user (convert at application layer)
- Use `timestamptz`?
- Use classes in the [`java.time package`](https://thorben-janssen.com/hibernate-jpa-date-and-time/)

## Sources

- <https://vladmihalcea.com/how-to-store-date-time-and-timestamps-in-utc-time-zone-with-jdbc-and-hibernate/>
- <https://www.postgresql.org/docs/current/datatype-datetime.html#DATATYPE-DATETIME-INPUT>
- <https://stackoverflow.com/questions/43476364/hibernate-with-java-8-localdate-localdatetime-in-database>
- <https://medium.com/building-the-system/how-to-store-dates-and-times-in-postgresql-269bda8d6403>
- <https://thorben-janssen.com/hibernate-jpa-date-and-time/>
- <>
- <>
- <>
