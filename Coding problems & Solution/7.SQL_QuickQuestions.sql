-- Salesperson  

-- +----+-------+------+--------+
-- | ID | Name  | Age  | Salary |
-- +----+-------+------+--------+
-- |  1 | Abe   |   61 | 140000 |
-- |  2 | Bob   |   34 |  44000 |
-- |  5 | Chris |   34 |  40000 |
-- |  7 | Dan   |   41 |  52000 |
-- |  8 | Ken   |   57 | 115000 |
-- | 11 | Joe   |   38 |  38000 |
-- +----+-------+------+--------+

-- Orders
-- +--------+------------+---------+----------------+--------+
-- | Number | order_date | cust_id | salesperson_id | Amount |
-- +--------+------------+---------+----------------+--------+
-- |     10 | 1996-08-02 |       4 |              2 |    540 |
-- |     20 | 1999-01-30 |       4 |              8 |   1800 |
-- |     30 | 1995-07-14 |       9 |              1 |    460 |
-- |     40 | 1998-01-29 |       7 |              2 |   2400 |
-- |     50 | 1998-02-03 |       6 |              7 |    600 |
-- |     60 | 1998-03-02 |       6 |              7 |    720 |
-- |     70 | 1998-05-06 |       9 |              7 |    150 |
-- +--------+------------+---------+----------------+--------+


-- Find the salesperson(s) who have not made any sales in the last 3 months.

Select a.Name
from Salesperson a
left join Orders b
on a.ID=b.salesperson_id
where TO_DATE(b.order_date,'DDDD-MM-DD') >= CURRENT_DATE-50000
and b.salesperson_id is null;


-- Calculate the percentage of total sales contributed by each salesperson.

-- with TotalSales as 
-- (Select Sum(Amount) from Orders)

-- Select Name , (sum(Amount)/Select * from TotalSales)*100
-- from SalesPerson a
-- left join  Orders b
-- on a.ID=b.salesperson_id



-- -- Find the salesperson(s) who have the highest salary but have not made any sales.


-- Select top 1 a.Name, Salary
-- from Salesperson a
-- left join Orders b
-- on a.ID=b.salesperson_id
-- and b.salesperson_id is null
-- order by Salary;

-- -- Determine the month with the highest total sales.

-- Select To_char(order_Date,'MM') Month , sum(Amount)
-- from Orders
-- group by 1 
-- order by 2 desc 
-- limit 1;


-- -- List the salespersons who have made consecutive sales in two or more different months.


-- Select distinct salesperson_id
-- FROM (
-- Select 
-- salesperson_id,
-- order_Date Month , 
-- Lag(order_Date,-1) over(partition by salesperson_id order
-- by order_Date) Prevval,
-- months_between(order_Date-Prevval-order_Date) GAP
-- where 
-- Amount>0
-- order by 1,2 
-- )GAP=1
