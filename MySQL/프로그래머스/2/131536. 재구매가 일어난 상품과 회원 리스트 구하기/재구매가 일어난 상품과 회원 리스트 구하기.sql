select distinct T.user_id,T.product_id
from(
    SELECT user_id, product_id,count(user_id) as cnt
    FROM ONLINE_SALE
    group by user_id,product_id
) as T
where cnt > 1
order by T.user_id, T.product_id desc