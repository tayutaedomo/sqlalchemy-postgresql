BEGIN;

CREATE TABLE empsalary (
    id SERIAL PRIMARY KEY, -- 自動インクリメントID
    depname VARCHAR(32), -- 部門名
    empno INTEGER,        -- 従業員番号
    salary NUMERIC        -- 給料
);

COMMIT;
