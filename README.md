## About the Project

![Image of CSV File](https://www.gooddata.com/img/blog/_1200x630/cover_csv-files-in-analytics-taming-the-variability.jpg.webp)

This project is a simple Python script that reads sales data from a CSV file, cleans the data, enriches it with product information from a JSON file, and generates an aggregated report in CSV format.

## Built With

![Python](https://skillicons.dev/icons?i=py)

## Overall Approach

Since the use of third-party libraries is discouraged, this project uses built-in Python modules to read and manipulate the data. The csv module is used to read/write the CSV file, the json module is used to read the JSON file, and the datetime module is used to parse the date format. This is basically all we need to write the required script.

I decided to use two library modules along with my main script to handle the data processing: 

1. The first library module will be responsible for reading the CSV file and normalizing the date format. It will also read the JSON file and create a dictionary indexed by product_id for easy lookup later on.
2. The second library module will be responsible for cleaning the sales data and then enriching it with product category information.
3. The main script will leverage our two previous modules to generate the aggregated report and save it to a CSV file.

## Getting Started

To use this script, follow these steps:

1. Clone the repository to your local machine.
2. Locally navigate to the src directory within the main project folder.
3. Run the process_data.py script (make sure you are in the src directory) to generate the aggregated report.
    ```
    python3 scripts/process_data.py
    ```
4. The aggregated report will be saved to the <mark>data directory</mark>.
5. To run unit tests, navigate to the src directory and run the following commands:
    ```
    python3 tests/test_data_ingestion.py
    python3 tests/test_data_enrichment.py
    python3 tests/test_process_data.py
    ```

## Future Improvements

- Add ability to handle missing product_id in sales data. Currently, the script will skip over any sales data with missing product_id.
- Add error handling for invalid date formats in the CSV file. Currently, the script will raise a ValueError if the date format does not match the two expected formats.

## Contact

Baylee Kimmel - [Software Portfolio](https://bayleekimmel.com/) - bkimmel1226@gmail.com

Project Link: [https://github.com/bkimmelv2/Data-Processing-Project](https://github.com/bkimmelv2/Data-Processing-Project)
