### 🔎 Filtering, Searching, and Ordering

The API supports query parameters for flexible data retrieval:

| Feature | Parameter | Example |
|----------|------------|----------|
| Filter by author | `?author=` | `/api/books/?author=John%20Doe` |
| Search by title or author | `?search=` | `/api/books/?search=python` |
| Order by field | `?ordering=` | `/api/books/?ordering=title` |
| Reverse order | `?ordering=-field` | `/api/books/?ordering=-published_date` |
