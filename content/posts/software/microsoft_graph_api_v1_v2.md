---
title: "MS Graph API v1 vs. v2"
tags: ["azure"]
date: 2022-03-09
# weight: 1
# author: "Peter Dieleman"
# showToc: false
# TocOpen: false
draft: true
# hidemeta: false
# comments: false
# description: "A guide on extending the battery life of your linux laptop"
# disableShare: false
# searchHidden: false
---

## Compatible?


>  If you ask for an ID token from the V1 endpoint, you get a V1 ID token. If you ask for an ID token from the V2 endpoint you get a V2 ID token. 

> As a starting point you should always aim to smallest tokens as possible.

<https://matthijs.hoekstraonline.net/2020/04/27/v1-and-v2-identity-and-access-tokens-with-azure-active-directory/>

## How to Change it?

> The version of your Azure AD application depends on what portal was used to register it,
>
> If in the Azure Portal, then it's a v1 application
> If in the App Registration Portal then it's a v2 app.

<https://stackoverflow.com/questions/45987516/how-do-i-check-to-see-if-my-azuread-version-is-v1-or-v2>