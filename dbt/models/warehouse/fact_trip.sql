{{ config(materialized='table') }}

with green_data as (
    select *, 
        'Green' as service_type 
    from {{ ref('stg_green_tripdata') }}
), 

dim_zone as (
    select * from {{ ref('dim_zone') }}
    where borough != 'Unknown'
),

dim_date as (
    select * from {{ ref('dim_date') }}
)

select 
    green_data.tripid, 
    green_data.vendorid, 
    green_data.service_type,
    green_data.ratecodeid, 
    green_data.pickup_locationid, 
    pickup_zone.borough as pickup_borough, 
    pickup_zone.zone as pickup_zone, 
    green_data.dropoff_locationid,
    dropoff_zone.borough as dropoff_borough, 
    dropoff_zone.zone as dropoff_zone,  
    green_data.pickup_datetime, 
    pickup_date.month_of_year as pickup_moy,
    green_data.dropoff_datetime, 
    dropoff_date.month_of_year as dropoff_moy,
    green_data.store_and_fwd_flag, 
    green_data.passenger_count, 
    green_data.trip_distance, 
    green_data.trip_type, 
    green_data.fare_amount, 
    green_data.extra, 
    green_data.mta_tax, 
    green_data.tip_amount, 
    green_data.tolls_amount, 
    green_data.ehail_fee, 
    green_data.improvement_surcharge, 
    green_data.total_amount, 
    green_data.payment_type,  
    green_data.congestion_surcharge
from green_data
inner join dim_zone as pickup_zone
on green_data.pickup_locationid = pickup_zone.locationid
inner join dim_zone as dropoff_zone
on green_data.dropoff_locationid = dropoff_zone.locationid
inner join dim_date as pickup_date
on EXTRACT(DATE FROM green_data.pickup_datetime) = pickup_date.date_day
inner join dim_date as dropoff_date
on EXTRACT(DATE FROM green_data.dropoff_datetime) = dropoff_date.date_day