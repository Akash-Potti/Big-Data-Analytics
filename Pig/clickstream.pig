clicks = LOAD 'file:///home/cloudera/clickstream.csv' USING PigStorage(',') AS (uid:chararray,pid:chararray,action:chararray,timestamp:chararray);

products = LOAD 'file:///home/cloudera/products.csv' USING PigStorage(',') AS (pid:chararray,price:float,category:chararray);

purchases = FILTER clicks BY LOWER(action) == 'purchase';

views = FILTER clicks BY LOWER(action) == 'view';
views_grouped = GROUP views BY pid;
view_counts = FOREACH views_grouped GENERATE group AS pid, COUNT(views) AS view_count;

joined = JOIN view_counts BY pid, products BY pid;

sorted_views = ORDER joined BY view_count DESC;

STORE purchases INTO 'file:///home/cloudera/purchases' USING PigStorage(',');
STORE purchases INTO 'file:///home/cloudera/views' USING PigStorage(',');
