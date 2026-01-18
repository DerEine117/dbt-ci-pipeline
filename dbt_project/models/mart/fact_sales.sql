select
  customer,
  sum(amount) as total_amount
from {{ ref('stg_sales') }}
group by customer
