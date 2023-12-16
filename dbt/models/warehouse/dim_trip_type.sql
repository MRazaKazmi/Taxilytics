{{ config(materialized='table') }}

select
    trip_type,
    trip_type_desc
from {{ ref('seed_trip_type') }}