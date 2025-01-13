minikube start

# Előkészületek
## Docker imagek letöltése\létrehozása
`docker save postgres:15 -o C:\dev\k8\images\postgres.img`
`docker build -t python-web .`
`docker save python-web -o C:\dev\k8\images\python-web.img`

## Docker imagek betöltése a kubernetesbe
`minikube image load C:\dev\k8\images\postgres.img`
`minikube image load C:\dev\k8\images\python-web.img`

# Kubernetes parancsok
## Konfigurációk betöltése
`kubectl apply -f secret.yaml`
`kubectl apply -f config.yaml`
`kubectl get configmaps`
`kubectl describe configmaps <ConfigMap name>`

## Adatbázis podok\deployment\service
`cd db`
`kubectl apply -f db_deployment.yaml`
`kubectl get pods`
`kubectl describe pod <Pod name>`
`kubectl describe deployments`
`kubectl logs webapp-deployment-585dd5675-pxxdw`
`kubectl apply -f db_internal_service.yaml`

## Python podok\deployment\service
`cd ..`
`cd app`
`kubectl apply -f app_deployment.yaml`
`kubectl apply -f app_external_service.yaml`

## Ellenörzés
`minikube service app-external-service --url`

## Exec
`kubectl exec -it <db-pod-name>`
