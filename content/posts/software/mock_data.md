---
title: "Template"
tags: ["postgresql"]
date: 2022-05-05
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

Inefficient, but does the job:

<https://dev.to/antjanus/using-postgres-for-loop-to-generate-data-3mm2>

```SQL
DO $FN$
BEGIN
  FOR counter IN 1..100 LOOP
    RAISE NOTICE 'Counter: %', counter;

    EXECUTE $$ INSERT INTO items(name, active) VALUES ('Test item ' || $1, true) RETURNING id $$ 
      USING counter;
  END LOOP;
END;
$FN$
```

