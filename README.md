# Waste Wise - Smart Waste Management System

Waste Wise is a smart waste management system designed to streamline and optimize waste collection. It allows users to request pickups via a mobile app, scan their waste for reuse tips, and ensures efficient clustering and assignment of pickup requests to drivers based on location.

## System Overview

![System Diagram](https://github.com/libreprojectss/waste_wise/blob/main/Screenshot%202024-05-28%20002734.png)

### Key Components
1. **Customer and Picker (Driver)**
   - Customers can request waste pickups via the mobile app.
   - Pickers (drivers) receive notifications of assigned pickups, perform the collection, and mark it as completed.

2. **Mobile App**
   - Interfaces with customers and pickers.
   - Allows customers to scan waste for reuse tips using an Object Detection Model.
   - Sends pickup requests to the primary server via REST APIs.

3. **Admin WebApp**
   - Admins can monitor and manage pickup requests.
   - Interacts with the primary server using REST APIs.

4. **Primary Server**
   - Central hub for processing requests and managing data.
   - Interfaces with the Primary Database and various microservices.
   - Use Django and Django Rest Framework
   - Facilitates REST and gRPC communications.

5. **Clustering Microservice**
   - Node.js server that clusters pickup requests for optimized collection routes.
   - Communicates with the primary server via gRPC.
   - Stores cluster data in the Cluster Database.

6. **Prompt Microservice**
   - Generates reuse tips for scanned waste using the Llama LLM (Language Learning Model).
   - Utilizes the Object Detection Model to analyze waste images.

7. **FastAPI Server**
   - Fetches data from the Llama model and stores it in the database for quicker access to similar queries.
   - Ensures efficient retrieval and caching of frequently requested data.

### Technologies Used
- **Mobile App:** Flutter
- **Admin WebApp:** ReactJs
- **Primary Server:** Django
- **Clustering Microservice:** Node.js server with gRPC communication
- **Primary Database:** PostgreSQL
- **Cluster Database:** MongoDB
- **Object Detection Model:** Machine Learning model for waste identification
- **Llama LLM:** Natural Language Processing model for generating reuse tips
- **FastAPI Server:** FastAPI for efficient data retrieval and caching

## Workflow
1. **Customer Interaction:**
   - The customer scans the waste using the mobile app.
   - The Object Detection Model identifies the waste and suggests reuse tips via the Prompt Microservice.
   - The customer requests a pickup through the app.

2. **Pickup Request Handling:**
   - The pickup request is sent to the primary server and recorded in the Primary Database.
   - Admins can view and manage requests through the Admin WebApp.

3. **Clustering and Assignment:**
   - The Clustering Microservice groups pickup requests based on location.
   - Drivers are automatically assigned to clusters using location data.

4. **Driver Notification and Pickup:**
   - The assigned driver receives a notification of the pickup request.
   - The driver completes the pickup and marks it as completed in the system.

5. **Reuse Tips Generation and Caching:**
   - The Prompt Microservice interacts with the Llama LLM to generate reuse tips.
   - The FastAPI Server fetches these tips and stores them in the database for quicker access to similar queries.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/libreprojectss/waste_wise.git
   cd waste-wise
   ```
2. Setup main django server
   ```bash
   cd main_server/ecycle
   python manage.py migrate
   python manage.py runserver
   ```
3. Setup admin server (clustering microservice)
   ```bash
   cd admin_server/
   yarn install
   yarn dev
   ```
4. Setup prompt server (prompt microservice)
   ```bash
   cd admin_server/services
   python main.py
   ```
5. Run the react admin dashboard
   ```bash
   cd admin_web
   yarn install
   yarn dev
   ```

The setup can also be done using docker.
```bash
docker-compose build
docker-compose up
```


   
