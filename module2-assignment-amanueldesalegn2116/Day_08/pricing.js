// Pricing helper functions for Addis Market

const VAT_RATE = 0.15; // 15% VAT

// Applies 15% VAT to a subtotal
export function withVat(amount) {
  return amount * (1 + VAT_RATE);
}

// Formats an amount into ETB currency string
export function format(amount) {
  return `${amount.toFixed(2)} ETB`;
}
