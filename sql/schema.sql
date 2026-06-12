CREATE DATABASE IF NOT EXISTS analytics;

CREATE TABLE analytics.orders
(
    order_id UInt64,
    user_id UInt64,
    amount Float64,
    country String,
    event_time DateTime
)
ENGINE = MergeTree()
ORDER BY order_id;
