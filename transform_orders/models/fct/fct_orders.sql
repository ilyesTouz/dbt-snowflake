{{
    config(
    materialized = 'incremental',
    on_schema_change='fail'
    )
}}

SELECT
    ORDER_ID, 
    CAST(ORDER_CREATION_DATE as timestamp) as ORDER_CREATION_DATE, 
    CASE WHEN ORDER_QTY < 0 THEN 0 ELSE ORDER_QTY END AS ORDER_QTY, 
    CASE WHEN BILLING_QTY < 0 THEN 0 ELSE BILLING_QTY END AS BILLING_QTY,
    SHIPPING_LOCATION, 
    SALES_LOCATION,
    COUNTRY
FROM src_orders
WHERE 
ORDER_ID IS NOT NULL

{% if is_incremental() %}
AND ORDER_CREATION_DATE > (select max(ORDER_CREATION_DATE) from {{ this }})
{% endif %}