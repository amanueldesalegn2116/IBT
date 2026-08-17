// Day 20 Assignment: Fetch & Display Live Data
const API_URL = "https://jsonplaceholder.typicode.com/posts?_limit=10";

// Async function to load posts from the API and update the DOM
async function load() {
  const list = document.getElementById("list");
  const status = document.getElementById("status");

  if (!list) return;

  // 1. Show "Loading…" first
  list.innerHTML = "";
  if (status) {
    status.textContent = "Loading…";
    status.className = "status-msg loading";
  }

  try {
    // 2. Fetch the API
    const res = await fetch(API_URL);

    // 3. Check for errors
    if (!res.ok) {
      throw new Error("Request failed");
    }

    // 4. Get the JSON
    const data = await res.json();

    // 5. Display the data by creating <li> elements
    list.innerHTML = "";
    data.forEach(item => {
      const li = document.createElement("li");
      li.textContent = item.title;
      list.appendChild(li);
    });
  } catch (error) {
    // 6. Handle errors and show a friendly message
    list.innerHTML = "";
    if (status) {
      status.textContent = "Unable to load data. Please try again later.";
      status.className = "status-msg error";
    }
  } finally {
    // 7. Clear loading message using finally
    if (status && status.classList.contains("loading")) {
      status.textContent = "";
      status.className = "status-msg";
    }
  }
}

// Initial load and button setup when DOM is ready
document.addEventListener("DOMContentLoaded", () => {
  load();

  const refreshBtn = document.getElementById("refresh-btn");
  if (refreshBtn) {
    refreshBtn.addEventListener("click", load);
  }
});
