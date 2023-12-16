{{ config(materialized='table') }}

select
    trip_type,
    trip_type_desc
from {{ ref('stg_trip_type') }}