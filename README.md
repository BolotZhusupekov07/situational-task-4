# Eco Track

Legend:

EcoTrack develops a platform for monitoring and managing environmental data from various sensors and devices. Currently, the company needs a system to manage data on air quality.


Your task is to develop a RESTful API based on the provided specification to manage a list of air quality sensors. The API should allow sensors to be created, read, updated, and deleted. Provide basic authentication and authorization for API access. The service must be able to process simultaneous requests from multiple clients and ensure high data availability.

Additional requirements:

The API specification should be well documented using tools such as Swagger or OpenAPI.
Provide support for standard HTTP methods (GET, POST, PUT, DELETE) for each resource.
Implement error handling and return appropriate HTTP statuses and messages.
Possible questions and answers:

Question: How will you ensure the security of your API? Answer: We can use Access Tokens to authenticate users and restrict access based on roles and permissions.

Question: What measures will you take to ensure the performance of your API? Answer: We can use data caching and database query optimization to improve performance. Additionally, we can scale the application horizontally to handle large volumes of requests.

Question: How will you test your API? Answer: We can write unit tests using tools like unittest for Python to test the core functionality of the API. Additionally, we can conduct integration testing to check how the API interacts with other system components.

Question: What data formats will you use to pass information through the API? Answer: We can use JSON format to exchange data between client and server as it is easy to read and supported by many programming languages.

Question: How will you ensure data consistency across parallel queries? Answer: We can use transaction mechanisms in a database to ensure data integrity during create, update, and delete operations.

Database details:

Tables:

Sensors: Contains information about each sensor, including unique ID, type, model, installation date, status, etc.
Data: Stores air quality measurements such as PM2.5, PM10, CO2 levels, and other parameters. Each entry is associated with a specific sensor and contains a timestamp and parameter values.
Alerts: Contains information about events that require operator attention, such as high pollution levels. Each alert is associated with a specific sensor and contains a description of the event and a timestamp.
Relations:

The Data and Alerts tables are linked to the Sensors table via a foreign key to provide tracking of data and alerts for specific sensors.
Additional relationships can be added to ensure data integrity and query optimization.


# Screenshots

![Swagger Docs 1](/screenshots/shot_1.png)
![Swagger Docs 2](/screenshots/shot_2.png)
![Swagger Docs 2](/screenshots/shot_3.png)


# Video

Link - https://drive.google.com/file/d/14ns-y5_jcDAhHxpoRmh1mDqLj5wAAeMK/view?usp=sharing