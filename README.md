# OPC UA Client Development and Data Logging

## Project Overview
### This project demonstrates the development of an OPC UA Client that connects to an OPC UA Server (simulated locally), reads 10 dummy tags at regular intervals, and logs the data into hourly CSV files with accurate timestamps.

## Installation
- pip install opcua

## Steps to Run the Project
### Step 1: Start the OPC UA Server
- python server.py
### Step 2: Start the OPC UA Client
- python logger.py
### Step 3: Generate Hourly Logs
- Let the client run across an hour change
- The system will automatically create a new CSV file for the next hour
### Step 4: Stop the Application
- Stop the client terminal: Ctrl + c
- Stop the server terminal: Ctrl + c
