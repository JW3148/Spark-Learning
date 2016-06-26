SparkShell

-filepath

local files 'file:///' 
HDFS 'hdfs://' 


Define an RDD by reading a simple text file

-mydata=sc.textFile(FilePath)

-mydata.count()
-mydata.collect()  --use with care
-mydata.take(n)    --first n rows
-mydata.filter(lambda x: '.jpg' in x)
-mydata.map(lambda x: len(x))
-mydata.map(lambda x: s.split()[0]) 

Print data
for x in mydata.take(10): print x