-- 코드를 입력하세요
SELECT ROUND(avg(daily_fee)) as average_fee
FROM CAR_RENTAL_COMPANY_CAR
where car_type = 'SUV'
group by car_type
