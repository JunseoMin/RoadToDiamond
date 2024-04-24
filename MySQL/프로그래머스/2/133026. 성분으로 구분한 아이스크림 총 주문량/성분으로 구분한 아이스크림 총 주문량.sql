SELECT INGREDIENT_TYPE,sum(TOTAL_ORDER) as TOTAL_ORDER
FROM FIRST_HALF F
join ICECREAM_INFO I
on F.FLAVOR = I.FLAVOR
group by I.INGREDIENT_TYPE
order by total_order

