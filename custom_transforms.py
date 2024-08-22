from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def normalize_column(df: DataFrame, column: str) -> DataFrame:
    max_value = df.agg({column: "max"}).collect()[0][0]
    min_value = df.agg({column: "min"}).collect()[0][0]
    return df.withColumn(column, (col(column) - min_value) / (max_value - min_value))
