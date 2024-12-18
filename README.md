# kubernetes-eks
Apply Kubernetes on AWS EKS

# Using Github Actions
Run the following github actions: <br>
**Terraform Deployment** in order to create the EKS cluster on AWS. <br>
**Kubernetes Deployment** in prder to apply kubernetes pods, services and ingress on the cluster. <br>
**Kubernetes Check** in order to check that the application is active. <br>
Finally you should run **Kubernetes Destry** in prder to delete everything that was applied on AWS. <br>
**Avoiding the destry will increase the AWS costs!** <br>
Please pay attention that a failed Destroy due to a *subnet that has dependencies and cannot be deleted* is temporary considred as satisfying. <br>
The reason is that it cleared all or most of the paid assets.

# Manual deployment
Clone the repository to your own computer. <br>
Do the following steps. <br>
*Prerequisites are not detailed. E.g. installing kubernetes and terraform.*

## Terraform
In directory infrastructure - <br>
`terraform init` <br>
`terraform plan` <br>
`terraform apply` <br>

## Kubernetes

### Initial steps - 

Connect k8s to cluster:
`aws eks update-kubeconfig --region il-central-1 --name main-cluster`

Create namespace:
`kubectl create namespace eks-sample-app`



### HELM -

Add helm chart to my local helm repo (needed once):
`helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx`

Update helm repo:
`helm repo update`

Install nginx-ingress by helm:
`helm install nginx-ingress ingress-nginx/ingress-nginx \
--namespace eks-sample-app \
--set controller.service.type=LoadBalancer`

### Apply - 

In directory k8s - <br>
Apply the deployment and service:
`kubectl apply -f eks-sample-deployment.yaml`

Apply the ingress:
`kubectl apply -f eks-sample-ingress.yaml`

## Checks - 

After apply - get the testing url from the `Address` value: `kubectl describe ingress nginx-ingress -n eks-sample-app`<br>
If Address is empty wait and try again later.<br>
Check the Address in any browser.

