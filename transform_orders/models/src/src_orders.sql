WITH raw_orders as (
    SELECT * 
    FROM BRONZE.ORDERS.RAW_ORDERS)

SELECT 
    DOC_NUMBER as order_id, 
    DOC_DATE as order_creation_date, 
    ORDER_QTY_NEW as order_qty, 
    BILLING_QTY billing_qty, 
    SHIP_TO__0INDUSTRY___T as shipping_location, 
    GC_KUNNR__0SALES_DIST___T as sales_location, 
    COUNTRY as country
FROM raw_orders