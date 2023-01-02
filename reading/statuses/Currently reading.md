## Books that I'm currently reading
```dataview
TABLE 
	title as "Title",
	genre_1 as "Genre 1",
	rating AS "Rating"
FROM "reading/books"
WHERE status = [[Currently reading]]
SORT rating DESC
```
