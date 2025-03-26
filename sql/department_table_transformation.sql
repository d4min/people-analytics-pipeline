WITH hierarchy AS (
    SELECT 
        d_store."DEPARTMENT_ID",
        d_store."DEPARTMENT_NAME",
        d_area."DEPARTMENT_NAME" AS "AREA",
        d_region."DEPARTMENT_NAME" AS "REGION"
    FROM department d_store
    JOIN department d_area ON d_store."PARENT_DEPARTMENT_ID" = d_area."DEPARTMENT_ID"
    JOIN department d_region ON d_area."PARENT_DEPARTMENT_ID" = d_region."DEPARTMENT_ID"
    WHERE d_store."DEPARTMENT_NAME" LIKE '% - SD'
      AND d_area."DEPARTMENT_NAME" LIKE 'Area % - SD'
      AND d_region."DEPARTMENT_NAME" LIKE 'Region % - SD'
)
SELECT * FROM hierarchy
ORDER BY "DEPARTMENT_ID";