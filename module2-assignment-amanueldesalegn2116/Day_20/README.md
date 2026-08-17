# Day 20 Assignment: Fetch & Display Live Data

## API URL
- API used: `https://jsonplaceholder.typicode.com/posts?_limit=10`

## Requirements Checklist
- [x] **Create async load()**: Created `load()` to handle fetching and updating the page.
- [x] **Show "Loading…" first**: Displayed "Loading…" status message before sending the fetch request.
- [x] **Fetch the API**: Used `const res = await fetch(API_URL)`.
- [x] **Check for errors**: Added `if (!res.ok) throw new Error("Request failed")`.
- [x] **Get the JSON**: Parsed JSON response using `await res.json()`.
- [x] **Display the data**: Looped over the returned posts, created `<li>` elements, and added them to `<ul id="list">`.
- [x] **Handle errors**: Used `try...catch` block to catch network errors and display a friendly message.
- [x] **Clear loading**: Used `finally` to remove the "Loading…" message after fetch completes.
- [x] **Bonus - Refresh Button**: Added a Refresh button that calls `load()` on click.

## File Overview
- `index.html` - Main HTML layout with heading, `#refresh-btn`, `#status`, and empty `<ul id="list">`.
- `app.js` - JavaScript file with `API_URL`, `load()` function, async/await logic, and error handling.
- `styles.css` - Custom styling for page layout, posts list, refresh button, loading state, and error message.
- `README.md` - Summary of project features and API URL.
- `Day_20_Assignment_Answers.txt` - Written answers for Day 20 theory and practical exercises.
