CREATE SCHEMA IF NOT EXISTS temp;

CREATE TABLE IF NOT EXISTS temp.data (
    event_date TIMESTAMPTZ NOT NULL DEFAULT now(),
    temperature float,
    humidity smallint,
    heat_index float
    );

GRANT USAGE ON SCHEMA temp TO reader;
GRANT SELECT, INSERT ON ALL TABLES IN SCHEMA temp TO reader;