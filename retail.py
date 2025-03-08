import streamlit as st
import pymysql
import pandas as pd
#import re

# database connection

mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="naga",
            database="retail_data",
            autocommit=True
        )
mycursor = mydb.cursor()
#st.success("Connected to the database successfully!")


st.title("RETAIL_ORDERS")
st.header("GIVEN QUERIES:")

mycursor.execute('use retail_data')

if st.button("1"):
     st.markdown(" Find top 10 highest revenue generating products:")
     mycursor.execute('''SELECT order_2.product_id, SUM(order_2.sale_price * order_2.quantity) AS revenue
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_2.product_id
ORDER BY revenue DESC
LIMIT 10;
''')
     st.table(mycursor)


if st.button("2"):
     st.markdown("Find the top 5 cities with the highest profit margins:")
     mycursor.execute('''SELECT order_1.city, SUM(order_2.profit) AS total_profit
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_1.city
ORDER BY total_profit DESC
LIMIT 5;
''')
     st.table(mycursor)


if st.button("3"):
     st.markdown("Calculate the total discount given for each category:")
     mycursor.execute('''SELECT order_1.category, SUM(order_2.discount) AS total_discount
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_1.category;
''' )
     st.table(mycursor)


if st.button("4"):
     st.markdown("Find the average sale price per product category:")
     mycursor.execute('''SELECT order_1.category, AVG(order_2.sale_price) AS avg_sale_price
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_1.category;
''' )
     st.table(mycursor)


if st.button("5"):
     st.markdown("Find the region with the highest average sale price:")
     mycursor.execute('''SELECT order_1.region, AVG(order_2.sale_price) AS avg_sale_price
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_1.region
ORDER BY avg_sale_price DESC
LIMIT 1;
''')
     st.table(mycursor)    


if st.button("6"):
     st.markdown("Find the total profit per category:")
     mycursor.execute('''SELECT order_1.category, SUM(order_2.profit) AS total_profit
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_1.category;
''' )
     st.table(mycursor)  

if st.button("7"):
     st.markdown(" Identify the top 3 segments with the highest quantity of orders:")
     mycursor.execute('''SELECT order_2.segment, SUM(order_2.quantity) AS total_quantity
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_2.segment
ORDER BY total_quantity DESC
LIMIT 3;
 ''')
     st.table(mycursor)  


if st.button("8"):
     st.markdown("Determine the average discount percentage given per region:")
     mycursor.execute('''SELECT order_1.region, AVG(order_2.discount_percent) AS avg_discount_percent
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_1.region;
'''  )
     st.table(mycursor)


if st.button("9"):
     st.markdown("Find the product category with the highest total profit:")
     mycursor.execute('''SELECT order_1.category, SUM(order_2.profit) AS total_profit
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_1.category
ORDER BY total_profit DESC
LIMIT 1;
 ''' )
     st.table(mycursor)


if st.button("10"):
     st.markdown("Calculate the total revenue generated per year:")
     mycursor.execute('''SELECT YEAR(order_1.order_date) AS year, 
       SUM(order_2.sale_price * order_2.quantity) AS total_revenue
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY YEAR(order_1.order_date)
''')
     st.table(mycursor)


st.header("MY OWN GIVEN QUERIES:")

if st.button("11"):
     st.markdown("Find the top 5 lowest revenue generating products:")
     mycursor.execute('''SELECT order_2.product_id, SUM(order_2.sale_price * order_2.quantity) AS revenue
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_2.product_id
ORDER BY revenue ASC
LIMIT 5;
 ''' )
     st.table(mycursor) 


if st.button("12"):
     st.markdown("Find the top 5 cities with the lowest profit margins:")
     mycursor.execute('''
        SELECT order_1.city, SUM(order_2.profit) AS total_profit
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_1.city
ORDER BY total_profit ASC
LIMIT 5;
   '''  )
     st.table(mycursor)

if st.button("13"):
     st.markdown("Calculate the total discount given for each category:")
     mycursor.execute('''
        SELECT order_1.category, SUM(order_2.discount) AS total_discount
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_1.category;
  '''   )
     st.table(mycursor)


if st.button("14"):
     st.markdown("Find the average sale price per product category:")
     mycursor.execute('''
        SELECT order_1.category, AVG(order_2.sale_price) AS avg_sale_price
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_1.category;
''')
     st.table(mycursor)


if st.button("15"):
     st.markdown("Find the region with the lowest average sale price:")
     mycursor.execute('''
        SELECT order_1.region, AVG(order_2.sale_price) AS avg_sale_price
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_1.region
ORDER BY avg_sale_price ASC
LIMIT 1;
''')
     st.table(mycursor)


if st.button("16"):
     st.markdown(" Find the total profit for each category:")
     mycursor.execute('''
        SELECT order_1.category, SUM(order_2.profit) AS total_profit
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_1.category;
'''  )
     st.table(mycursor)


if st.button("17"):
     st.markdown("Identify the top 5 segments with the lowest quantity of orders:")
     mycursor.execute('''
        SELECT order_2.segment, SUM(order_2.quantity) AS total_quantity
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_2.segment
ORDER BY total_quantity ASC
LIMIT 5;
''' )
     st.table(mycursor)


if st.button("18"):
     st.markdown("Determine the average discount percentage given for total revenue:")
     mycursor.execute('''
        SELECT SUM(order_2.sale_price * order_2.quantity) AS total_revenue,
       AVG(order_2.discount_percent) AS avg_discount_percent
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id;
''' )
     st.table(mycursor)


if st.button("19"):
     st.markdown("Find the product category with the lowest total profit:")
     mycursor.execute('''
        SELECT order_1.category, SUM(order_2.profit) AS total_profit
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_1.category
ORDER BY total_profit ASC
LIMIT 1;
''' )
     st.table(mycursor)


if st.button("20"):
     st.markdown(" Calculate the total revenue generated per day:")
     mycursor.execute('''SELECT order_1.order_date, SUM(order_2.sale_price * order_2.quantity) AS total_revenue
FROM order_1
JOIN order_2 ON order_1.order_id = order_2.order_id
GROUP BY order_1.order_date
ORDER BY order_1.order_date;
''' )
     st.table(mycursor)



