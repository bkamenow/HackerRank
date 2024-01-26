SELECT
  ROUND(ABS(MIN(lat_n) + MIN(long_w) - (MAX(lat_n) + MAX(long_w))), 4) AS distance
FROM station;
