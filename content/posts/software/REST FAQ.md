---
title: "REST FAQ"
tags: ["REST"]
date: 2022-10-17
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

# PUT Request: ID in body or URI?

- <https://stackoverflow.com/questions/27900041/rest-put-ids-in-body-or-not>
- <https://restfulapi.net/rest-put-vs-post/>
- <https://softwareengineering.stackexchange.com/questions/263925/to-include-a-resource-id-in-the-payload-or-to-derive-from-uri>

In general: PUT should be idempotent and mirror behavior of GET 