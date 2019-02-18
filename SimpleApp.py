from pyspark.sql import SparkSession

data_path="README.txt"
spark=SparkSession.builder.appName("SimpleApp").getOrCreate()
data=spark.read.text(data_path).cache()
spark.stop()
