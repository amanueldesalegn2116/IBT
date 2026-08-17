// Day 09: Addis Market Shopping List (State -> Render Pattern)

// 1. Initial State
let items = [
  { id: 1, name: "Milk", done: false },
  { id: 2, name: "Bread", done: true }
];

// DOM references
const form = document.getElementById("form");
const input = document.getElementById("input");
const count = document.getElementById("count");
const list = document.getElementById("list");

// 2. Render function (State -> View)
function render() {
  list.innerHTML = "";

  items.forEach((item) => {
    const li = document.createElement("li");
    li.dataset.id = item.id;

    if (item.done) {
      li.classList.add("done");
    }

    const span = document.createElement("span");
    span.textContent = item.name;

    const button = document.createElement("button");
    button.textContent = "Remove";
    button.dataset.action = "remove";

    li.appendChild(span);
    li.appendChild(button);
    list.appendChild(li);
  });

  // Update remaining count inside render()
  const remaining = items.filter((item) => !item.done).length;
  count.textContent = `${remaining} items remaining`;
}

// 3. Form submission & validation
form.addEventListener("submit", (e) => {
  e.preventDefault();

  const name = input.value.trim();

  // Validate empty input
  if (!name) {
    return;
  }

  // Prevent duplicate items (case-insensitive)
  const alreadyExists = items.some(
    (item) => item.name.toLowerCase() === name.toLowerCase()
  );

  if (alreadyExists) {
    alert("This item is already on your list.");
    return;
  }

  // Add new item to state
  items.push({
    id: Date.now(),
    name: name,
    done: false
  });

  // Re-render UI and reset input
  render();
  input.value = "";
});

// 4. Event Delegation on <ul>
list.addEventListener("click", (e) => {
  const li = e.target.closest("li");
  if (!li) return;

  const id = Number(li.dataset.id);

  // If Remove button clicked, filter out item
  if (e.target.dataset.action === "remove") {
    items = items.filter((item) => item.id !== id);
    render();
    return;
  }

  // Otherwise, toggle done state
  const item = items.find((item) => item.id === id);
  if (item) {
    item.done = !item.done;
    render();
  }
});

// Initial Render
render();
