{{ config(materialized='table') }}

select
    rate_code_id,
    rate_code
from {{ ref('seed_rate_code') }}