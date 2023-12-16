{{ config(materialized='table') }}

select
    payment_type,
    payment_type_desc
from {{ ref('seed_payment_type') }}