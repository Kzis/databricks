# Databricks notebook source
# MAGIC %md
# MAGIC # Mounting ADLS to DBFS
# MAGIC
# MAGIC #### Resources:
# MAGIC * https://learn.microsoft.com/en-us/azure/databricks/dbfs/mounts

# COMMAND ----------

APPLICATION_ID = ""
TENANT_ID = ""
SECRET = ""

# COMMAND ----------

# syntax for configs and mount methods
configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": APPLICATION_ID,
          "fs.azure.account.oauth2.client.secret": SECRET,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://bronze@demoadls1234.dfs.core.windows.net/",
  mount_point = "/mnt/bronze_demo",
  extra_configs = configs)