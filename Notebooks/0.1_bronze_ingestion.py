from pyspark.sql import functions as F

df_raw = (spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("/Volumes/personal_projects/information_retail_schema/retailtransactions"))

# Clean column names by replacing spaces with underscores
for col in df_raw.columns:
    df_raw = df_raw.withColumnRenamed(col, col.replace(" ", "_"))

df_raw.write.format("delta").mode("overwrite").saveAsTable("personal_projects.information_retail_schema.online_retail_raw")