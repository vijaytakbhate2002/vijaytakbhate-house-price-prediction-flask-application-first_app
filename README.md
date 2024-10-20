# House Price Prediction Flask Application

## Overview
This repository contains a Machine Learning application built using Python and Flask for predicting house prices. The application takes input as house area and predicts the corresponding house price. This data is stored in a SQL server for future reference.

## Features
- User-friendly interface for interacting with the house price prediction model.
- Input house area to receive real-time predictions.
- Data storage in SQL server with three columns: id, area, and predicted_price.
- Users can view the model's prediction output by clicking the submit button.

## Getting Started
### Clone the Repository
```bash
git clone https://github.com/vijaytakbhate2002/vijaytakbhate-house-price-prediction-flask-application-first_app.git
cd vijaytakbhate-house-price-prediction-flask-application-first_app
```

### Build the Docker Image
To build the Docker image for the application, run:
```bash
docker build -t ml_app:first .
```

### Run the Docker Container
Run the Docker container with:
```bash
docker run -d -p 8000:8000 ml_app:first
```

### Access the Application
Visit `http://localhost:8000` in your web browser.

## Important Note
You should run the GitHub repository to create the Docker image before executing the Docker Hub instructions.

## Usage
- Enter the house area in the input field and click the submit button to see the predicted house price.

## Contributing
Contributions are welcome! Fork the repository and submit a pull request.

## License
This project is licensed under the MIT License 

## Acknowledgements
- I used a SQL server for storing information in three columns: id, area, and predicted_price.
```
