# Flask API Project

## Overview
This repository contains a **Flask API project** deployed on Kubernetes with monitoring using Prometheus and Grafana.

## Project Structure

flask-kubernetes-api/
- app/
  - static/        (Static files)
  - templates/     (HTML templates)
- docker/          (Dockerfile and related files)
- k8s/             (Kubernetes manifests: Deployment, Service, HPA, etc.)
- prometheus/    (Prometheus & Grafana dashboards and configs)
- README.md

## Notes
- Future updates will include:
  - Flask API endpoints
  - Dockerfile and Docker images
  - Kubernetes deployment and service files
  - Monitoring with Prometheus and Grafana

## Quick Start

### Clone the project
```bash
git clone https://github.com/victornaya-dev/flask-kubernetes-api
```
Apply all Kubernetes manifests

```bash
kubectl apply -f flask-kubernetes-api/k8s -R
```

Note: This assumes Prometheus Operator is installed.

Check if Prometheus Operator is installed

```bash
kubectl get pods --all-namespaces | grep operator
```

If there is a pod with a name similar to kube-prometheus-stack-operator-xxxx, the operator is installed.

Access the Flask API
Open the API in your browser or via curl at:

```bash
http://<node-ip>:30008
```

For local clusters (like Minikube), you can use:

```bash
http://localhost:30008
```

Import Grafana Dashboard
Import the dashboard JSON located at:

```bash
k8s/prometheus/grafana-dashboard.json
```

### Monitoring & Metrics

Prometheus scrapes metrics from the Flask app using the /metrics endpoint.
The Grafana dashboard includes:
- CPU usage per container
- Memory usage per container
- Requests per second
- Average latency
- Pod status (Running / Pending)

  Docker Image (Local Build)

####  If you want to build and run the Docker image locally:

Build the image:

```bash
docker build -t myapp_flask_v003:latest .
```

(Optional) Tag it if you want to push later:
```bash
docker tag myapp_flask_v003:latest victordock218/myapp_flask_v003:tagname
```

Run the container locally:
```bash
docker run -p 80:80 myapp_flask_v003:latest
```

You can now access the Flask API at:
```bash
http://localhost:80
```

## TEST
Once your Flask app is running (for example, via Docker, Kubernetes, or directly with python app.py), you can test it with:
```bash
curl http://localhost:30008/api/data
```

Expected response:
```bash
{"message": "Hello from flask API!", "status": "success"}
```

### Notes

- Future updates will include:
- Additional Flask API endpoints
- Extended Kubernetes manifests (ConfigMaps, Secrets, etc.)
- Advanced Prometheus alerts and Grafana dashboards
