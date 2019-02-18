# Import SparkSession to create python app
from pyspark.sql import SparkSession
from sklearn.linear_model import LinearRegression

# Load data data_path
data_path="shuttle.trn"

#Crete SparkSession
spark=SparkSession.builder.appName("Space shuttle").getOrCreate()

# Load data in spark
data=spark.read.load(data_path,format="csv",sep=",",header="false",inferSchema="true")
print(data.shape())
