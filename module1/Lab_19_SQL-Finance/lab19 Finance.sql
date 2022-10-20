USE `olist`;

1. From the order_items table, find the price of the highest priced order and lowest price order;

select price from order_items
order by price desc
limit 5;

select price from order_items
order by price desc
limit 5;
