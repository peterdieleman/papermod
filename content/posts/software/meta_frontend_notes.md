---
title: "Study Notes Meta Frontend Coursera"
tags: ["study"]
date: 2022-07-03
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

## HTTP Headers

```
Host: example.com​
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0
Accept: */*
Accept-Language: en​
Content-type: text/json
```

- The`Host` header specifies the host of the server and indicates where the resource is requested from.
- The `User-Agent` header informs the web server of the application that is making the request. It often includes the operating system (Windows, Mac, Linux), version and application vendor.
- The `Accept` header informs the web server what type of content the client will accept as the response.
- The `Accept-Language` header indicates the language and optionally the locale that the client prefers.
- The `Content-type` header indicates the type of content being transmitted in the request body.

## Other Internet Protocols

- Dynamic Host Configuration Protocol (DHCP)
- Domain Name System Protocol (DNS)
- Internet Message Access Protocol (IMAP)
- Simple Mail Transfer Protocol (SMTP)
- Post Office Protocol (POP)
- File Transfer Protocol (FTP)
- Secure Shell Protocol (SSH)
- SSH File Transfer Protocol (SFTP)

## HTTP Overview

<https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview>

## CSS

### Selectors

selector, declaration (value:property)

- Element Selectors
- ID Selectors
- Class Selectors
- Child Selectors
- Element with Class Selector:
- Descendant Selectors: are useful if you need to select HTML elements that are contained within another selector.

```html
<div id="blog">
  <h1>Latest News</h1>
  <div>
    <h1>Today's Weather</h1>
    <p>The weather will be sunny</p>
  </div>
  <p>Subscribe for more news</p>
</div>
<div>
  <h1>Archives</h1>
</div>
```

```css
#blog h1​ {
  color: blue;
}
```

The CSS rule will select all h1 elements that are contained within the element with the ID blog. The CSS rule will not apply to the h1 element containing the text Archives.

### Alignment

"To center align an element, you set a width on the element and push its margins out to fill the remaining available space of the parent element as in the following HTML structure:"

"To be more precise, in CSS you can set only the left and right margins to auto. This allows you to set the top and bottom margins to specific values if needed."

CSS Reference (Mozilla): <https://developer.mozilla.org/en-US/docs/Web/CSS/Reference>

HTML and CSS: Design and build websites by Jon Duckett: <https://www.amazon.com/HTML-CSS-Design-Build-Websites/dp/1118008189/>

CSS Definitive Guide  by Eric Meyer <https://www.amazon.com/CSS-Definitive-Guide-Visual-Presentation/dp/1449393195/>

### Responsive Design

- Flexible grids
- fluid images
- media queries

### bootstrap

