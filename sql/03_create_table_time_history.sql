BEGIN;

CREATE TABLE time_history (
    id SERIAL PRIMARY KEY,
    label VARCHAR(255),
    time1 TIMESTAMP,
    time2 TIMESTAMP
);

COMMIT;

