CREATE TABLE dim_department (
    department_key INT PRIMARY KEY IDENTITY(1,1),
    department_id INT NOT NULL,
    department_name VARCHAR(100) NOT NULL,
    area VARCHAR(100) NOT NULL,
    region VARCHAR(100) NOT NULL
);

INSERT INTO dim_department (department_id, department_name, area, region)
SELECT 
    d.DEPARTMENT_ID,
    d.DEPARTMENT_NAME,
    a.DEPARTMENT_NAME AS area,
    r.DEPARTMENT_NAME AS region
FROM 
    department d
JOIN department a ON d.PARENT_DEPARTMENT_ID = a.DEPARTMENT_ID
JOIN department r ON a.PARENT_DEPARTMENT_ID = r.DEPARTMENT_ID
WHERE 
    d.DEPARTMENT_NAME LIKE '% - SD'
    AND a.DEPARTMENT_NAME LIKE 'Area % - SD'
    AND r.DEPARTMENT_NAME LIKE 'Region % - SD';

CREATE TABLE fact_vacancy (
    vacancy_key INT PRIMARY KEY IDENTITY(1,1),
    requisition_key INT NOT NULL,
    department_key INT NOT NULL,
    recruiter_key INT NOT NULL,
    date_key INT NOT NULL,
    active_vacancies INT NOT NULL,
    time_to_fill DECIMAL(10,2),
    submission_to_interview_rate DECIMAL(10,2),
    interview_to_hire_rate DECIMAL(10,2),
    number_of_openings INT NOT NULL,
    FOREIGN KEY (requisition_key) REFERENCES dim_requisition(requisition_key),
    FOREIGN KEY (department_key) REFERENCES dim_department(department_key),
    FOREIGN KEY (recruiter_key) REFERENCES dim_recruiter(recruiter_key),
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
);