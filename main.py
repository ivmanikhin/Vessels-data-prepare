import pandas as pd
import matplotlib.pyplot as plt
import re

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_rows", None)
# database = pd.read_feather("clean_db_old")
# database = database.append(pd.read_feather(f"database_870000-930000"), ignore_index=True)
# print(database.shape)
# database = database.append(pd.read_feather(f"database_930000-980000"), ignore_index=True)
# print(database.shape)
# # print(database[database.duplicated("RS No", keep=False)].sort_values(by="RS No").reset_index())
# clean_db = database.drop_duplicates("RS No", keep=False).sort_values(by="RS No").reset_index()
# print(len(database) - len(clean_db))
# clean_db.to_feather("clean_db")
clean_db = pd.read_feather("clean_db")
clean_db = clean_db.sort_values("level_0").drop("index", axis=1)
clean_db = clean_db.drop(columns="level_0")
clean_db = clean_db.reset_index(drop=True)
print(len(clean_db))
clean_db["Displacement"] = clean_db["Displacement"].fillna(value=0)
clean_db["Speed"] = clean_db["Speed"].fillna(value=0)
print(clean_db["Basic type"].value_counts())
# plt.hist(clean_db["Basic type"], bins=112)
# plt.show()

# dataset = pd.concat([clean_db["Name of vessel"], clean_db["Flag"], clean_db["Basic type"], clean_db["Date of build"],
#                      clean_db["Country of build"], clean_db["Gross tonnage"], clean_db["Tonnage"],
#                      clean_db["Deadweight"], clean_db["Displacement"], clean_db["Length overall (extreme)"],
#                      clean_db["Breadth"], clean_db["Depth"], clean_db["Draught"], clean_db["Speed"],
#                      clean_db["Type of power plant"], clean_db["Main Engine"],
#                      clean_db["The number and power of propulsion motors"],
#                      clean_db["Number and power of generators"], clean_db["Number and capacity of cargo holds"],
#                      clean_db["Refrigerated cargo spaces"], clean_db["Cargo tanks"],
#                      clean_db["Number and type of containers"], clean_db["Number o bulkheads"], clean_db[""]


# clean_db["Displacement, t"] = clean_db["Displacement"].map(lambda element: filter(str.isdigit, element) if not None else 0)
# plt.hist(clean_db["Displacement"], bins=100)
# plt.show()
# clean_db["Index"] = clean_db["index"].map(lambda element: int(element))