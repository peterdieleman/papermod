---
title: "Empty Hash MSAL React"
tags: ["template"]
date: 2022-03-21
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

`BrowserAuthError: hash_empty_error: Hash value cannot be processed because it is empty. Please verify that your redirectUri is not clearing the hash. Given Url: ...`

- <https://github.com/AzureAD/microsoft-authentication-library-for-js/issues/3638>
- <https://stackoverflow.com/questions/67788651/microsoft-authentication-react-hash-empty-error-when-using-loginpopup>
- <https://github.com/AzureAD/microsoft-authentication-library-for-js/issues/4573>

> We've resolved this in our application. For us, we had our redirect URL as the home page of our application. This caused an issue where our router (in Next.js) took over the routing in the popup, stripping the hash and redirecting it to the login page - before the window that launched the popup had time to extract it. Redirecting to a blank page allowed consistent logins.
