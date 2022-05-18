---
title: "React Select / Randomness "
tags: ["JS","mui"]
date: 2022-05-16
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

- <https://mui.com/material-ui/react-select/>
- <https://v3.mui.com/demos/selects/>


`Solve - No overload matches this call error in TypeScript #`

- <https://bobbyhadz.com/blog/typescript-no-overload-matches-this-call>

- <https://stackoverflow.com/questions/71499278/error-no-overload-matches-this-call-on-component-menuitem>

```
This is because of the MenuItem value. It is LiHTMLAttributes prop, and it only allows string | string[] | number. You can change the true/false values to yes/no and can easily convert into boolean.
```