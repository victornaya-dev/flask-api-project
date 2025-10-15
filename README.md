# Flask API Project

## Overview
This repository contains a **Flask API project** deployed on Kubernetes with monitoring using Prometheus and Grafana.

## Project Structure

flask-api-project/
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

## Status
**In progress** – The project structure is ready; main features will be implemented soon.
## Quick Start

### Clone the project
```bash
git clone https://github.com/victornaya-dev/flask-api-project
```
Apply all Kubernetes manifests

```bash
kubectl apply -f flask-api-project/k8s -R
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
