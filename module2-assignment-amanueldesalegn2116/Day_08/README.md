# Day 08 Assignment: Build an Addis Market order summary

## Deliverable
A pricing module plus a script that takes an array of orders and produces a per-order total and a grand total in ETB, using `map`, `filter`, `reduce`, destructuring, and spread.

## Requirements & Self-Check List
- [x] Export `withVat` and `format` from `pricing.js`.
- [x] Import them into `summary.js`.
- [x] Use `reduce` to total each order's items (destructuring `{ price, qty }`).
- [x] Use `map` + spread (`...order`) to attach a `total` field to each order.
- [x] Use `filter` to list only orders over 500 ETB.
- [x] Print a formatted summary and the grand total in ETB.

## How to Run
```bash
node Day_08/summary.js
```
