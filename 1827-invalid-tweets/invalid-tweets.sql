# Write your MySQL query statement below

-- Using LENGTH()
select tweet_id from Tweets 
where length(content)>15;