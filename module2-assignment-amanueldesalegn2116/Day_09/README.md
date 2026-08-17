# Day 09 Assignment: Addis Market Shopping List

## Deliverable
A working single-page app: a form adds grocery items, each row can be marked bought or removed, and a counter shows how many items remain — built with the **State → Render** pattern.

## Requirements Checklist
- [x] State stored in `items` array with `{ id, name, done }` objects.
- [x] `render()` function rebuilds `list` from `items` array.
- [x] Elements use `data-id` (`li.dataset.id = item.id`) to connect HTML to JavaScript state.
- [x] Bought items use `.done` CSS class (`text-decoration: line-through`).
- [x] Remove buttons created with `dataset.action = "remove"`.
- [x] Form submission uses `e.preventDefault()`.
- [x] Input validation prevents empty items (`name.trim()`).
- [x] Duplicate item prevention using `.some()` and `.toLowerCase()`.
- [x] State updated before calling `render()`.
- [x] Event delegation used on `<ul>` (`e.target.closest("li")`).
- [x] Remaining item count updated inside `render()`.

## Files
- `index.html`: Contains form (`#form`), input (`#input`), count (`#count`), and list (`#list`).
- `styles.css`: Styles layout and `.done` class.
- `app.js`: Implementation of state-then-render pattern.
