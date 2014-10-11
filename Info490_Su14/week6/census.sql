-- Week 6 Problem 1 Template

DROP TABLE IF EXISTS myCensus;
CREATE TABLE myCensus(
id INT PRIMARY KEY,
age INT,
hours_worked INT,
income INT
); -- your code goes here

.separator ,
.import ss12pil_sql.csv myCensus

-- uncomment below to check the first 10 lines
--SELECT * FROM myCensus LIMIT 10;


DROP TABLE IF EXISTS moreCensus;
CREATE TABLE moreCensus(
id INT PRIMARY KEY, 
favorite_number INT
); -- your code goes here


.separator ,
.import ss12pil_favorite_number.csv moreCensus

-- uncomment below to check the first 10 lines
--SELECT * FROM moreCensus LIMIT 10;

DROP TABLE IF EXISTS myMoreCensus;
CREATE TABLE myMoreCensus AS SELECT moreCensus.id,myCensus.age,myCensus.hours_worked,myCensus.income,moreCensus.favorite_number
FROM moreCensus
INNER JOIN myCensus
ON moreCensus.id = myCensus.id; -- your code goes here

-- uncomment below to check the first 10 lines
--SELECT * FROM myMoreCensus LIMIT 10;

INSERT INTO myMoreCensus(id,age,hours_worked,income,favorite_number) VALUES (49001,21,40,1000000,1); -- your code goes here

SELECT * FROM myMoreCensus WHERE myMoreCensus.age >17 AND myMoreCensus.hours_worked >39 AND
myMoreCensus.income > 500000 AND myMoreCensus.favorite_number = 1;
 -- your code goes here


