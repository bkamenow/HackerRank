SELECT ROUND(lat_N, 4)
FROM station
WHERE lat_n = (SELECT MIN(lat_N) FROM station WHERE lat_n > 38.7780);