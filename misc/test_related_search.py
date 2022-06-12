# %%
import pandas as pd

df = pd.read_csv("/tmp/df_magId_field.csv")

res = df["fieldofstudy"].value_counts()

df_fields = df.drop_duplicates(subset=["fieldofstudy"])
df_fields = df_fields.merge(res, left_on="fieldofstudy", right_index=True)


# we sort by level and then by fieldofstudy_y
df_best_fields = df_fields.sort_values(by=["fieldofstudy_y"], ascending=False).head(10)
# %%
df_sorted_level = df_best_fields.sort_values(by=["level"], ascending=True)
# %%
list(df_sorted_level.fieldofstudy)
