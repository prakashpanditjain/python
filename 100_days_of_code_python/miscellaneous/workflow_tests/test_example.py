from pyspark.sql import SparkSession

def test_count():
    spark = SparkSession.builder.master("local[*]").appName("Test").getOrCreate()
    df = spark.createDataFrame([(1,), (2,), (3,)], ["numbers"])
    assert df.count() == 3
    spark.stop()