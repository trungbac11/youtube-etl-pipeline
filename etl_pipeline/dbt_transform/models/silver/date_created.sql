select
	youtuber, 
	created_date,
    CASE 
        WHEN created_month = 'Jan' THEN 'January'
        WHEN created_month = 'Feb' THEN 'February'
        WHEN created_month = 'Mar' THEN 'March'
        WHEN created_month = 'Apr' THEN 'April'
        WHEN created_month = 'May' THEN 'May'
        WHEN created_month = 'Jun' THEN 'June'
        WHEN created_month = 'Jul' THEN 'July'
        WHEN created_month = 'Aug' THEN 'August'
        WHEN created_month = 'Sep' THEN 'September'
        WHEN created_month = 'Oct' THEN 'October'
        WHEN created_month = 'Nov' THEN 'November'
        WHEN created_month = 'Dec' THEN 'December'
        ELSE created_month
    END AS created_month,
    created_year 
FROM {{ ref('raw_information') }}
