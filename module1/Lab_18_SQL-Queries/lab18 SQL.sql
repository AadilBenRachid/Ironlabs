create database if not exists applestore;
use applestore;

select * from applestore;
select prime_genre from applestore
group by prime_genre;

select * from applestore;
select prime_genre from applestore 
group by prime_genre
order by rating_count_tot desc;

select prime_genre from applestore
group by prime_genre
order by prime_genre desc;

select prime_genre from applestore
group by prime_genre
order by prime_genre asc;

select prime_genre from applestore
group by prime_genre 
order by rating_count_tot desc
limit 10;

select prime_genre from applestore
group by prime_genre 
order by rating_count_tot desc
limit 10;

select track_name, user_rating, rating_count_tot from applestore 
order by user_rating desc, rating_count_tot desc
limit 10;

select track_name, user_rating, rating_count_tot, price from applestore 
order by user_rating desc, rating_count_tot desc, price desc;


