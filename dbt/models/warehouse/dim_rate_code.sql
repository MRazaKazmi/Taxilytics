{{ config(materialized='table') }}

select
    rate_code_id,
    rate_code
from {{ ref('stg_rate_code') }}