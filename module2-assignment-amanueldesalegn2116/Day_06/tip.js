// Day 06: TeleBirr Tip & Split Calculator

function calculateTipAndSplit(billInput, partySizeInput, paymentMethod = "TeleBirr") {
  // 1. Read bill and partySize; convert the bill with Number()
  const bill = Number(billInput);
  const partySize = Number(partySizeInput);

  // 2. Add a 10% tip when the bill is over 300 ETB, else 5%
  const tipRate = bill > 300 ? 0.10 : 0.05;
  const tipAmount = bill * tipRate;

  // 3. Use a switch to add a TeleBirr / CBE Birr service fee
  let serviceFee = 0;
  switch (paymentMethod) {
    case "TeleBirr":
      serviceFee = 15;
      break;
    case "CBE Birr":
    case "CBEBirr":
      serviceFee = 10;
      break;
    default:
      serviceFee = 0;
      break;
  }

  // 4. Compute total and the per-person amount
  const totalAmount = bill + tipAmount + serviceFee;
  const perPersonAmount = totalAmount / partySize;

  // 5. Print a clear message with a template literal
  const summary = `--- TeleBirr Tip & Split Calculator ---
Bill Amount: ${bill.toFixed(2)} ETB
Party Size: ${partySize} person(s)
Tip Rate: ${(tipRate * 100).toFixed(0)}% (${tipAmount.toFixed(2)} ETB)
Payment Method: ${paymentMethod} (Service Fee: ${serviceFee.toFixed(2)} ETB)
----------------------------------------
Total Amount: ${totalAmount.toFixed(2)} ETB
Amount Per Person: ${perPersonAmount.toFixed(2)} ETB`;

  return summary;
}

// Sample execution with inputs
const billAmount = "450";
const partySize = "3";
const paymentMethod = "TeleBirr";

const output = calculateTipAndSplit(billAmount, partySize, paymentMethod);
console.log(output);
