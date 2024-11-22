# ETL Pipeline Development using Employee Data
**Project Overview:**<br>
This project focuses on creating a fully automated ETL (Extract, Transform, Load) pipeline that processes fake employee data for analytical and visualization purposes. The entire pipeline is orchestrated using Google Cloud services, ensuring seamless data extraction, transformation which includes masking and encoding of sensitive information, and loading into a cloud-based environment. Data is processed using a combination of Python scripting, cloud storage, data integration, and orchestration tools. The project culminates in interactive data visualisations using Power BI for real-time insights.

## Technologies Used: ##
- **Python:** Used for scripting and data transformation with the Faker library to generate synthetic employee data.
- **Google Cloud Storage:** Data storage for the raw and transformed datasets.
- **Google Cloud Data Fusion:** Data integration tool for transforming and managing the ETL pipeline.
- **Apache Airflow (via Cloud Composer):** Orchestrating the ETL pipeline to ensure the seamless movement and processing of data.
- **BigQuery:** Cloud-based data warehouse used for storing and querying the transformed data.
- **Power BI:** Data visualisation tool used for presenting the employee data insights.

## Project Objectives: ##
- Generate synthetic employee data using Python’s Faker library.
- Store the raw and processed data in Google Cloud Storage.
- Transform and integrate data using Google Cloud Data Fusion for analytics-ready formats.
- Orchestrate the ETL pipeline using Apache Airflow via Cloud Composer.
- Load the transformed data into BigQuery for efficient querying.
- Visualise key insights from the data using Power BI.

## Data Architecture: ##


![diagram-export-20-11-2024-08_42_47](https://github.com/user-attachments/assets/85664443-787f-49ce-8e99-84344c320390)

## Data Flow and Process: ##
The project follows a structured flow from data generation to visualization:

**Data Generation:**
Using the Python Faker library, synthetic employee data is generated. The data is created for a large number of fake employees to simulate a real-world employee database.

**Data Storage:**
The generated data is stored in Google Cloud Storage in a structured file format (e.g., CSV or JSON) for further processing.

**Data Transformation:**
Google Cloud Data Fusion is used to transform the raw employee data, including tasks like cleaning, reshaping, and aggregating the data for analysis. This ensures that the data is ready for querying and analysis.

**Data Orchestration:**
The entire ETL pipeline is orchestrated using Apache Airflow through Cloud Composer. Airflow ensures that tasks like data extraction, transformation, and loading are executed in a sequence, and dependencies are correctly handled.

**Data Loading:**
The processed data is loaded into BigQuery, where it is stored in optimized tables that are ready for analysis. BigQuery’s fast querying capabilities ensure that users can query large datasets efficiently.

**Data Visualisation:**
The data stored in BigQuery is connected to Power BI, where various reports and dashboards are created to present key employee metrics. 


## Insights: ## 
Breakdown of employee distribution across various departments: <br>


![Screenshot 2024-11-20 084905](https://github.com/user-attachments/assets/fe4a3665-b17f-4010-875b-d5a787ec891c)






