# DevTools Console Tricks

**Purpose:** Console shortcuts for faster debugging and testing.
**Requirements:** Chrome, Edge, or Firefox. Open DevTools with F12, then the Console tab.

## Selecting elements

```js
$0                      // the element currently selected in the Elements tab
$$("a")                 // all matching elements as an array (like querySelectorAll)
$("h1")                 // first match (like querySelector)
$_                      // result of the last expression
```

## Inspecting data

```js
console.table([{a:1,b:2},{a:3,b:4}])   // arrays/objects as a table
copy(JSON.stringify(data, null, 2))    // copy formatted JSON to your clipboard
console.dir(document.body)             // object view instead of HTML view
```

## Editing the page live

```js
document.designMode = "on"             // click and edit any text on the page
$0.style.outline = "2px solid red"     // highlight the selected element
```

## Debugging behavior

```js
getEventListeners($0)                  // list listeners on an element (Chrome)
monitorEvents($0, "click")             // log every click on it
unmonitorEvents($0)                    // stop logging
```

## Timing

```js
console.time("load"); /* run code */ console.timeEnd("load");
```

## Extract all links on a page

```js
copy($$("a").map(a => a.href).join("\n"))
```

Changes made in the console last only until you reload the page.
