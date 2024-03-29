---
title: "Hibernate Envers"
tags: ["Java", "Spring Boot"]
date: 2022-01-01
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
## Blog Posts / Documentation

- <https://docs.jboss.org/envers/docs/>
- <https://vladmihalcea.com/the-best-way-to-implement-an-audit-log-using-hibernate-envers/>
- <https://thorben-janssen.com/hibernate-envers-getting-started/>
- <https://sunitc.dev/2020/01/21/spring-boot-how-to-add-jpa-hibernate-envers-auditing/>
- <https://www.bytefish.de/blog/hibernate_envers_versioning_and_auditing.html>
- <https://hibernate.atlassian.net/browse/HHH-10212?attachmentOrder=asc>
- <https://developer.jboss.org/thread/152642>
- <https://developer.jboss.org/thread/166705>
- <https://access.redhat.com/documentation/en-us/red_hat_jboss_enterprise_application_platform/7.4/html/developing_hibernate_applications/hibernate_envers>

## Further Issues @CreatedDate, @CreatedBy, etc. Annotations

- <https://www.baeldung.com/database-auditing-jpa>
- <https://rashidi.github.io/spring-boot-data-audit/>

>> @CreatedDate, @CreatedBy, @LastModifiedDate, and @LastModifiedBy. createdBy and modifiedBy fields will be automatically populated if Spring Security is available in the project path. 

`@CreatedDate` & `@LastModifiedDate`

- <https://stackoverflow.com/questions/49170180/createdby-and-lastmodifieddate-are-no-longer-working-with-zoneddatetime>
- <https://stackoverflow.com/questions/43236431/register-a-new-date-converter-auditable-in-spring-data-mongodb-for-zoneddatetime>
- <https://stackoverflow.com/questions/49170180/createdby-and-lastmodifieddate-are-no-longer-working-with-zoneddatetime>

`java.lang.IllegalArgumentException: Invalid date type for member <MEMBER NAME>! Supported types are [org.joda.time.DateTime, org.joda.time.LocalDateTime, java.util.Date, java.lang.Long, long].`

- <https://github.com/spring-projects/spring-data-commons/issues/880>

Which finally contains this amazing quote:

>> I can't believe that this is still not working in 2021

## Persisting Revision Info into TimestampTz

<https://stackoverflow.com/questions/37748142/how-to-save-utc-instead-of-local-timestamps-for-hibernate-envers-revision-info>

## Behaviour on Inheritance & MappedSuperClass

- <https://stackoverflow.com/questions/41298391/base-model-with-audited>
- <https://developer.jboss.org/thread/171717>

## Native queries bypassing hibernate envers

- <https://stackoverflow.com/questions/12370596/work-around-for-envers-auditing-for-bulk-update>
- <https://stackoverflow.com/questions/14139856/hibernate-envers-doesnt-write-audit-records-for-createquery-executeupdat>
- <https://developer.jboss.org/thread/149545>

Need to trigger lifecycle events. This does not happen when we use:

- Native queries
- Bulk actions (get translated to SQL directly)

## Can we use Native Queries?

No, not be default, need to hook into lifecycle events.

- <https://stackoverflow.com/questions/14139856/hibernate-envers-doesnt-write-audit-records-for-createquery-executeupdat>
- <https://localcoder.org/hibernate-envers-doesnt-write-audit-records-for-createquery-executeupdat>
- <https://stackoverflow.com/questions/12370596/work-around-for-envers-auditing-for-bulk-update>
- <https://stackoverflow.com/questions/14139856/hibernate-envers-doesnt-write-audit-records-for-createquery-executeupdat>
- <https://thorben-janssen.com/use-native-queries-perform-bulk-updates/>
- <https://www.heise.de/hintergrund/Auditierung-mit-Hibernate-Envers-eine-Einfuehrung-3728004.html>

can be done using `createNativeQuery(String sqlString)`?

## Ignoring Inserts / POSTS? (Conditional Auditing)

- <https://vladmihalcea.com/hibernate-event-listeners/>
- <https://thorben-janssen.com/conditional-auditing-hibernate-envers/#Customize_the_Handling_of_EventTypePRE_UPDATE_Events>
- <https://stackoverflow.com/questions/58929502/hibernate-skip-envers-historisation-for-specific-action-or-a-transaction>
- <https://stackoverflow.com/questions/14250612/conditional-envers-auditing>
- <https://www.youtube.com/watch?v=fX0SXEexy_o>
- <https://stackoverflow.com/questions/28118004/implementing-conditional-envers-auditing-hibernate-4-3-7-final>

To do this, the following steps are required:

- Customize listener for `POST_INSERT`
- Custom event listeners
- Overwrite envers integrator
- List FQName of class in `<ETA-INF/services/org.hibernate.integrator.spi.Integrator`
