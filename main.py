import pandas as pd
import matplotlib.pyplot as plt
import re
import xlwt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_rows", None)
# database = pd.read_feather("data/data (1)")
# for i in range(2, 11):
#     database = database.append(pd.read_feather(f"data/data ({i})"), ignore_index=True)
# # print(database.shape)
# # database = database.append(pd.read_feather(f"database_930000-980000"), ignore_index=True)
# # print(database.shape)
# # # print(database[database.duplicated("RS No", keep=False)].sort_values(by="RS No").reset_index())
# clean_db = database.drop_duplicates("RS No", keep="last").reset_index(drop=True)
# print(clean_db.tail())
# print(len(clean_db))
# clean_db.to_feather("data/clean_db.xls")
# # clean_db.to_feather("clean_db")
# # clean_db = pd.read_feather("clean_db")
# # clean_db = clean_db.sort_values("level_0").drop("index", axis=1)
# # clean_db = clean_db.drop(columns="level_0")
# # clean_db = clean_db.reset_index(drop=True)
# # print(len(clean_db))
# # clean_db["Displacement"] = clean_db["Displacement"].fillna(value=0)
# # clean_db["Speed"] = clean_db["Speed"].fillna(value=0)
# print(clean_db[clean_db["Basic type"] == "Research"].sort_values("Displacement"))
# # plt.hist(clean_db["Basic type"], bins=112)
# # plt.show()
# database = pd.read_csv("data/database_0-59000.csv").drop(columns="Unnamed: 0")
# print(database)
# print(len(database))
#
# print(database.shape)
# database = database.append(clean_db, ignore_index=True)
# database["IMO No"] = database["IMO No"].fillna(value=0)
# database["IMO No"] = database["IMO No"].astype(int)
# database = database.astype(str)
# print(database.shape)
# clean_db = database.drop_duplicates("RS No", keep="last").reset_index(drop=True)
# print(database.shape)
# clean_db.to_feather("data/clean_db_30-11-2021")
# # print(database.tail)
# # print(len(database))
# # dataset = pd.concat([clean_db["Name of vessel"], clean_db["Flag"], clean_db["Basic type"], clean_db["Date of build"],
# #                      clean_db["Country of build"], clean_db["Gross tonnage"], clean_db["Tonnage"],
# #                      clean_db["Deadweight"], clean_db["Displacement"], clean_db["Length overall (extreme)"],
# #                      clean_db["Breadth"], clean_db["Depth"], clean_db["Draught"], clean_db["Speed"],
# #                      clean_db["Type of power plant"], clean_db["Main Engine"],
# #                      clean_db["The number and power of propulsion motors"],
# #                      clean_db["Number and power of generators"], clean_db["Number and capacity of cargo holds"],
# #                      clean_db["Refrigerated cargo spaces"], clean_db["Cargo tanks"],
# #                      clean_db["Number and type of containers"], clean_db["Number o bulkheads"], clean_db[""]
#
#
# # clean_db["Displacement, t"] = clean_db["Displacement"].map(lambda element: filter(str.isdigit, element) if not None else 0)
# # plt.hist(clean_db["Displacement"], bins=100)
# # plt.show()
# # clean_db["Index"] = clean_db["index"].map(lambda element: int(element))
database = pd.read_feather("data/clean_db_30-11-2021")
# print(database["Basic type"].value_counts())


database["Gross tonnage"] = database["Gross tonnage"].str.extract("(\d+)")
database["Tonnage"] = database["Tonnage"].str.extract("(\d+)")
database["Deadweight"] = database["Deadweight"].str.extract("(\d+)")
database["Displacement"] = database["Displacement"].str.extract("(\d+)")
database["Length overall (extreme)"] = database["Length overall (extreme)"].str[:-3]
database["Moulded lenght"] = database["Moulded lenght"].str[:-3]
database["Rule length"] = database["Rule length"].str[:-3]
database["Breadth"] = database["Breadth"].str[:-3]
database["Depth"] = database["Depth"].str[:-3]
database["Draught"] = database["Draught"].str[:-3]
database["Water ballast"] = database["Water ballast"].str.extract("(\d+)")
database["Main Engine"] = database["Main Engine"].str.extract("power of ME: ([\d* ]+\*\d+) Mark")
database["Date of build"] = database["Date of build"].str[-4:]
database["Arc-Ice class"] = database["RS Class notation"].str.extract("(Ice\d|Arc\d)")




cargos = database[database["Basic type"] == "General cargo"]
print(cargos["Arc-Ice class"])