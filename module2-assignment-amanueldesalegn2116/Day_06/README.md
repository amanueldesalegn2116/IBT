# Day 06 Assignment: Build a TeleBirr tip & split calculator

## Deliverable
A script (`tip.js`) that takes a bill amount and party size, adds a tiered tip, adds a payment method service fee, and prints the total and the amount per person in ETB.

## Steps Completed
- [x] Read bill and partySize; convert the bill with `Number()`.
- [x] Add a 10% tip when the bill is over 300 ETB, else 5%.
- [x] Compute the total and the per-person amount.
- [x] Print a clear message with a template literal.
- [x] Use a `switch` statement to add a TeleBirr / CBE Birr service fee.
- [x] Verified by running `node tip.js` against `expected.txt`.

## How to Run
```bash
node Day_06/tip.js
```
