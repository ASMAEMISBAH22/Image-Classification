
# Image-Classification
![Screenshot 2025-05-15 163018](https://github.com/user-attachments/assets/e8a64936-08bb-460a-b49d-53e4529b82bf)

## Project Overview

This project is an image classification system that utilizes a MobileNet model for image recognition. The application allows users to upload images via a web interface, and the model classifies the image, returning the top prediction and other possible categories.

The app is built with FastAPI for the backend, HTML/CSS/JS for the frontend, and is containerized using Docker. The backend and frontend components are deployed on Minikube using Kubernetes for scalability and management. The system is optimized for performance and scalability, using Kubernetes autoscaling and load management strategies.

## Core Evaluation Metrics

-  AI Understanding → MobileNet Implementation & Inference Optimization:  
  The system uses the MobileNet architecture, a lightweight model ideal for mobile and embedded devices, for image classification. It is optimized for fast inference and accuracy on the target dataset.

-  Containerization & Kubernetes → Deployment Strategy, Minikube Handling:  
  The application is containerized using Docker and deployed on Minikube . Kubernetes handles deployment, scaling, and load balancing across multiple instances of the application to ensure high availability and robustness.

- UI & API Integration → Functional Web Interface for Real-Time Predictions:  
  The frontend UI allows users to upload images, which are processed in real-time by the FastAPI backend. The web interface seamlessly interacts with the backend API to return classification results and display predictions in an intuitive manner.

- Scalability Thinking → Kubernetes Autoscaling & Load Management:  
  The system is designed to scale under high load. Kubernetes autoscaling adjusts the number of replicas in the deployment based on incoming traffic, ensuring that the application performs well during peak usage.

## Technologies Used
- FastAPI– Backend API framework.
- MobileNet – Pre-trained deep learning model for image classification.
- Docker – Containerization of the backend and frontend.
- Minikube – Local Kubernetes environment for deployment and scalability.
- HTML, CSS, JavaScript – Frontend for user interaction.
- Python 3.10– Programming language for backend and model inference.

## Setup

### Docker Setup
1. Clone the Repository
```bash
git clone https://github.com/ASMAEMISBAH22/Image-Classification.git
cd Image-Classification
```
2. Docker Setup
a. Build the Docker Image
```bash
docker build -t image-classification:latest .
```
b. Run the Docker Container
```bash
docker run -d -p 8000:8000 image-classification:latest
```
3. Minikube Setup
a. Start Minikube
```bash
minikube start
```
b. Set Docker Environment for Minikube
```bash
 & minikube -p minikube docker-env | Invoke-Expression
```
c. Deploy the Application on Kubernetes
```bash
kubectl apply -f deployment.yaml
```
d. Access the Application via Minikube
```bash
minikube service classification-api-service --http://192.168.49.2:31260
```
5. Frontend 
```bash
cd app
python -m http.server 8080
```
