-- =====================================
-- USE DATABASE
-- =====================================

USE ai_sql_project;

-- =====================================
-- VIEW SAMPLE DATA
-- =====================================

SELECT * FROM customers LIMIT 5;

SELECT * FROM orders LIMIT 5;

SELECT * FROM products LIMIT 5;

SELECT * FROM order_items LIMIT 5;

-- =====================================
-- TOP 10 CITIES BY ORDERS
-- =====================================

SELECT 
    c.location,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.location
ORDER BY total_orders DESC
LIMIT 10;

-- =====================================
-- TOP 10 CUSTOMERS BY REVENUE
-- =====================================

SELECT 
    c.customer_id,
    SUM(oi.price * oi.quantity) AS total_revenue
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY c.customer_id
ORDER BY total_revenue DESC
LIMIT 10;

-- =====================================
-- UPDATE TOTAL ORDER AMOUNT
-- =====================================

UPDATE orders o
JOIN (
    SELECT
        order_id,
        SUM(price * quantity) AS total
    FROM order_items
    GROUP BY order_id
) t
ON o.order_id = t.order_id
SET o.total_amount = t.total;

-- =====================================
-- MONTHLY REVENUE TREND
-- =====================================

SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    SUM(total_amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;

-- =====================================
-- TOP PRODUCT CATEGORIES
-- =====================================

SELECT
    p.category,
    SUM(oi.price * oi.quantity) AS revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY revenue DESC
LIMIT 10;

-- =====================================
-- CUSTOMER RANKING (WINDOW FUNCTION)
-- =====================================

SELECT
    customer_id,
    total_revenue,
    RANK() OVER (ORDER BY total_revenue DESC) AS customer_rank
FROM (
    SELECT
        c.customer_id,
        SUM(oi.price * oi.quantity) AS total_revenue
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY c.customer_id
) t;