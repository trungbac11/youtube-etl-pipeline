LOAD DATA LOCAL INFILE '/tmp/youtube_channels/youtube_information.csv' 
INTO TABLE youtube_information 
CHARACTER SET latin1 FIELDS TERMINATED 
BY ',' ENCLOSED 
BY '"' LINES TERMINATED 
BY '\n' IGNORE 1 ROWS;