import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_rows", None)
database = pd.read_feather("database_1")
for i in range(2, 12):
    database = database.append(pd.read_feather(f"database_{i}"), ignore_index=True)
    print(database.shape)
db2 = database[database.duplicated("RS No", keep=False)].sort_values(by="RS No")
print(db2)
print(len(db2))
# plt.hist(db2["RS No"], bins=100)
# plt.show()
clean_db = database.drop_duplicates("RS No", keep=False).reset_index()
print(len(database), "\n", len(clean_db))
clean_db.to_feather("clean_db")
