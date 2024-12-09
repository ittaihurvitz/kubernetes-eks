# kubernetes-eks
apply Kubernetes on AWS EKS

*Prerequisites are not detailed. E.g. installing kubernetes and terraform.*

# Terraform
`terraform init` <br>
`terraform plan` <br>
`terraform apply` <br>

# Kubernetes

## Initial steps - 

Connect k8s to cluster:
`aws eks update-kubeconfig --region il-central-1 --name main-cluster`

Create namespace:
`kubectl create namespace eks-sample-app`



## HELM -

Add helm chart to my local helm repo (needed once):
`helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx`

Update helm repo:
`helm repo update`

Install nginx-ingress by helm:
`helm install nginx-ingress ingress-nginx/ingress-nginx \
--namespace eks-sample-app \
--set controller.service.type=LoadBalancer`

## Apply - 

Apply the deployment and service:
`kubectl apply -f eks-sample-deployment.yaml`

Apply the ingress:
`kubectl apply -f eks-sample-ingress.yaml`

# Checks - 

After apply - get the testing url from the `Address` value: `kubectl describe ingress nginx-ingress -n eks-sample-app`<br>
If Address is empty wait and try again later.

