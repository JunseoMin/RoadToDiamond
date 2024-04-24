SELECT p.product_code,sum(price * sales_amount) as sales
from PRODUCT p
inner join OFFLINE_SALE o
on p.product_id = o.product_id
group by p.product_code
order by sales desc, p.product_code