# Databricks notebook source
# MAGIC %md
# MAGIC # Accessing Data via Access Key
# MAGIC
# MAGIC #### Resources:
# MAGIC * https://learn.microsoft.com/en-us/azure/databricks/external-data/azure-storage#--access-azure-data-lake-storage-gen2-or-blob-storage-using-the-account-key
# MAGIC * https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction-abfs-uri

# COMMAND ----------

ACCESS_KEY = ""

# COMMAND ----------

# Paste in your account key in the second argument
spark.conf.set(
    "fs.azure.account.key.demoadls1234.dfs.core.windows.net", ACCESS_KEY
)

# COMMAND ----------

# Reading data from the storage account
countries = spark.read.csv("abfss://bronze@demoadls1234.dfs.core.windows.net/countries.csv", header=True)

# COMMAND ----------

countries.display()