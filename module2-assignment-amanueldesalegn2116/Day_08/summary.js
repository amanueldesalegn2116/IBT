import { orders } from "./orders.js";
import { withVat, format } from "./pricing.js";

// Process orders: reduce item totals with destructuring { price, qty }, map + spread total
const ordersWithTotals = orders.map((order) => {
  const subtotal = order.items.reduce((sum, { price, qty }) => sum + price * qty, 0);
  const total = withVat(subtotal);
  return { ...order, subtotal, total };
});

// Filter orders over 500 ETB
const highValueOrders = ordersWithTotals.filter((order) => order.total > 500);

// Calculate grand total using reduce
const grandTotal = ordersWithTotals.reduce((sum, { total }) => sum + total, 0);

// Output formatted summary
console.log("==========================================");
console.log("       ADDIS MARKET ORDER SUMMARY        ");
console.log("==========================================");

ordersWithTotals.forEach(({ id, customer, subtotal, total }) => {
  console.log(`Order ${id} - ${customer}`);
  console.log(`  Subtotal : ${format(subtotal)}`);
  console.log(`  Total    : ${format(total)} (incl. 15% VAT)`);
  console.log("------------------------------------------");
});

console.log("\nOrders Over 500 ETB:");
highValueOrders.forEach(({ id, customer, total }) => {
  console.log(`  - ${id} (${customer}): ${format(total)}`);
});

console.log("\n==========================================");
console.log(`GRAND TOTAL: ${format(grandTotal)}`);
console.log("==========================================");
