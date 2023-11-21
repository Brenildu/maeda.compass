# Importar as bibliotecas necessárias

from pyspark import SparkContext, SparkConf

from pyspark.sql import SparkSession



# Configurar o Spark

conf = SparkConf().setAppName("ContaPalavras")

sc = SparkContext.getOrCreate(conf=conf) 

spark = SparkSession(sc)

# docker exec -it 23f0c2314945 pyspark

# Ler o arquivo README.md 
df_readme = spark.read.text("README.md") 

# Remover símbolos 
df_semSimbolos = df_readme.withColumn("value", regexp_replace(col("value"), "[^a-zA-Z0-9\\s]", " ")) 

# Separar as palavras 
df_palavras = df_semSimbolos.select(explode(split(col("value"), "\\s+")).alias("word")) 

# Contar as palavras
df_contador = df_palavras.groupBy("word").count().orderBy(F.desc("count")) 

# Mostrar o resultado 
df_contador.show()