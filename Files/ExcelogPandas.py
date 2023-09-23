# import pandas as p

# df = pd.read_excel('ExcelogPandas.xlsx')

# markdown_tabell = df.to_markdown()

# print(markdown_tabell)

import pandas as pd

df = pd.read_excel('ExcelogPandas.xlsx')
df = df[["Student Name", "Subject", "Grade"]]

markdown_tabell = df.to_markdown(index=False)
print(markdown_tabell)