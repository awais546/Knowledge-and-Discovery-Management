from pyspark.sql import *
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession

from pyspark.sql import SQLContext
from pyspark.sql.functions import lit, when, col, regexp_extract
from pyspark.sql import functions as F
import pdb
sc = SparkContext('local')
# spark = SparkSession(sc)
sql = SQLContext(sc)

df = sql.read.csv("data.csv", inferSchema = True, header = True)
pdb.set_trace()

#selecting 3 columns and analysing does old people use more fibre optics or yong people
df1 = df.select('gender','SeniorCitizen','InternetService')
df2 = df1.filter((df1['gender'] == 'Male') & (df1['SeniorCitizen']==1) & (df1['InternetService']=='Fiber optic'))
df3 = df1.filter((df1['gender'] == 'Male') & (df1['SeniorCitizen']==0) & (df1['InternetService']=='Fiber optic'))
df2.count()
df3.count()
#df_check_stream = df.withColumn('Any Streaming', when((col("StreamingTV")=='No' and col("StreamingMovies") == 'No'),lit("Use Streaming")))

df_check = df.withColumn('testColumn', lit('this is a test'))

#creating a new column with a multiple conditions
df_check = df.withColumn('No Streaming(Tv and Movies)',when((col('StreamingTV')=='No') & (col('StreamingMovies')=='No'),'No streaming').otherwise('Stream'))

#create dataframe having yearly contractual subscription
df_year = df.filter(df.Contract.like('%year%'))

#take sum of one column
total_charge = df.groupBy().agg(F.sum("TotalCharges")).collect()

#take first 10 rows and convert it into dataframe
df_first = df.take(10)
df_convert = sql.createDataFrame(df_first)