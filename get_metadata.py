import glob

import frontmatter
import pandas as pd

reading_dir = "./notes/reading"

books = [filename for filename in glob.iglob(f"{reading_dir}/books/*.md")]

frontmatter_data = []
for book in books:
    with open(book) as f:
        fm, content = frontmatter.parse(f.read())
        frontmatter_data.append(fm)

datafm = pd.DataFrame.from_dict(frontmatter_data)
datafm.to_csv("./data/books.csv", index=False)
datafm.to_json("./data/books.json")
