
# Ques 2 
# 1321. Restaurant Growth

# . 

# Table: Customer

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | customer_id   | int     |
# | name          | varchar |
# | visited_on    | date    |
# | amount        | int     |
# +---------------+---------+
# In SQL,(customer_id, visited_on) is the primary key for this table.
# This table contains data about customer transactions in a restaurant.
# visited_on is the date on which the customer with ID (customer_id) has visited the restaurant.
# amount is the total paid by a customer.
 

# You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

# Compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). 
# average_amount should be rounded to two decimal places.

# Return the result table ordered by visited_on in ascending order.

# The result format is in the following example.

 

# Example 1:

-- # Input: 
-- # Customer table:
-- # +-------------+--------------+--------------+-------------+
-- # | customer_id | name         | visited_on   | amount      |
-- # +-------------+--------------+--------------+-------------+
-- # | 1           | Jhon         | 2019-01-01   | 100         |
-- # | 2           | Daniel       | 2019-01-02   | 110         |
-- # | 3           | Jade         | 2019-01-03   | 120         |
-- # | 4           | Khaled       | 2019-01-04   | 130         |
-- # | 5           | Winston      | 2019-01-05   | 110         | 
-- # | 6           | Elvis        | 2019-01-06   | 140         | 
-- # | 7           | Anna         | 2019-01-07   | 150         |
-- # | 8           | Maria        | 2019-01-08   | 80          |
-- # | 9           | Jaze         | 2019-01-09   | 110         | 
-- # | 1           | Jhon         | 2019-01-10   | 130         | 
-- # | 3           | Jade         | 2019-01-10   | 150         | 
-- # +-------------+--------------+--------------+-------------+



# Output: 
# +--------------+--------------+----------------+
# | visited_on   | amount       | average_amount |
# +--------------+--------------+----------------+
# | 2019-01-07   | 860          | 122.86         |
# | 2019-01-08   | 840          | 120            |
# | 2019-01-09   | 840          | 120            |
# | 2019-01-10   | 1000         | 142.86         |
# +--------------+--------------+----------------+
# Explanation: 
# 1st moving average from 2019-01-01 to 2019-01-07 has an average_amount of (100 + 110 + 120 + 130 + 110 + 140 + 150)/7 = 122.86
# 2nd moving average from 2019-01-02 to 2019-01-08 has an average_amount of (110 + 120 + 130 + 110 + 140 + 150 + 80)/7 = 120
# 3rd moving average from 2019-01-03 to 2019-01-09 has an average_amount of (120 + 130 + 110 + 140 + 150 + 80 + 110)/7 = 120
# 4th moving average from 2019-01-04 to 2019-01-10 has an average_amount of (130 + 110 + 140 + 150 + 80 + 110 + 130 + 150)/7 = 142.86



--------------------------------------------------------------------------------------------------------
--QUES 1
--------------------------------------------------------------------------------------------------------
# Approach 
# Approach 

# Select 
# visited_on,
# Sum(b.amount)TotaAmount ,
# Sum(b.amount)/7
# from Customer a 
# left join Customer b 
# a.visited_on > b.dateadd(d,b.visited_on,-7)
# and a.visited_on <= b.visited_on
# order by 1 




# Approach 
SELECT 
  visited_on,
  SUM(SUM(b.amount)) OVER (ORDER BY visited_on ROWS BETWEEN 7 PRECEDING AND CURRENT ROW) AS SumUpToDate
FROM Customer a
GROUP BY visited_on
ORDER BY visited_on;





--------------------------------------------------------------------------------------------------------
Question 3: Unique Patterns
Find patterns where three consecutive customers have visited on three consecutive days. Display the customer names and the corresponding visit dates.

--------------------------------------------------------------------------------------------------------


# Select name,visited_on,NextVisit,NextToNextVisit
# from 
# (
# Select 
# customer_id,
# name,
# visited_on,
# lead(visited_on,1) over(partition by customer_id order by visited_on) NextVisit ,
# lead(visited_on,2) over(partition by customer_id order by visited_on) NextToNextVisit ,
# from Customer
# order by visited_on
# ) where NextVisit-visited_on=1
# and NextToNextVisit-visited_on=1

--------------------------------------------------------------------------------------------------------

Question 4: Monthly Variance
Calculate the percentage variance in the total amount spent from one month to the next, considering only the last day of each month.
--------------------------------------------------------------------------------------------------------


# Select 
# Month,
# (lead(Amount,1) over(partition by order by Month ) - Amount)/Amount NextAmountVariation%
# from (
# Select 
# Month(visited_on) , 
# Sum(amount) Amount, 
# from datedim a 
# inner join Customer b 
# on a.visited_on=b.DimDate
# and a.visited_on=b.LastDayOfMonth
# group by all 
# order by 1 
# )

--------------------------------------------------------------------------------------------------------

Question 5: Peak Spending Days
Identify the top 3 days with the highest total amount spent and find the customer(s) who spent the most on each of those days.
--------------------------------------------------------------------------------------------------------


# Select top 3 customer_id,sum(Amount)
# from Customer
# where visited_on=
# Select visited_on from (
# Select visited_on,sum(Amount)
# from Customer 
# order by 2 desc 
# limit 3)
# order by 2 desc 

--------------------------------------------------------------------------------------------------------

Question 1: Rolling Average
Calculate the 3-day rolling average of the total amount spent by all customers, ordered by the visit date.
--------------------------------------------------------------------------------------------------------


# Select 
# visited_on,
# avg(amount) over( between 3 preeding row and current row order by visited_on)
# from Customer;


--Syntax Correction 

# SELECT
#   visited_on,
#   AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_average
# FROM
#   Customer
# ORDER BY
#   visited_on;
--------------------------------------------------------------------------------------------------------
Question 2: Customer Loyalty
Identify customers who have visited on consecutive days and calculate the total amount spent by each such customer.
--------------------------------------------------------------------------------------------------------



# Select name , sum(amount)
# from Customer a 
# where customer_id in (  Select customer_id from (
#     Select customer_id,
#     dateadd(d,visited_on,lag(visited_on,-1) over(partition by customer_id order by visited_on) GAP 
#     from Customer
#     ) where GAP=1


--You Can use CTEs as well
