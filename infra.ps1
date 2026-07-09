$rg = "mlDemo-rg"
$region = "southindia"
$AKS_NAME = "mlDemo-AKS"
$identity = "github-oidc-identity"
# az login

# az group create `
#     --name $rg `
#     --location $region

# az aks create `
#     --resource-group $rg `
#     --name $AKS_NAME `
#     --tier free `
#     --node-count 1 `
#     --node-vm-size Standard_B2ms `
#     --generate-ssh-keys

# az aks get-credentials `
#     --resource-group $rg `
#     --name $AKS_NAME `
#     --overwrite-existing

# az identity create `
#     --resource-group $rg `
#     --name $identity

# $AKS_ID = az aks show `
#     --resource-group $rg `
#     --name $AKS_NAME `
#     --query id `
#     --output tsv
# az role assignment create `
#     --assignee 9040dbef-782b-4c9d-9944-d2cb61d9bca4 `
#     --role "Azure Kubernetes Service Cluster User Role" `
#     --scope $AKS_ID

# az identity federated-credential create `
#     --resource-group $rg `
#     --identity-name $identity `
#     --name github-main `
#     --issuer "https://token.actions.githubusercontent.com" `
#     --subject "repo:naveenatnew/azure-ai-mlops-demo:ref:refs/heads/main" `
#     --audiences "api://AzureADTokenExchange"

# kubectl create secret docker-registry ghcr-secret `
#   --docker-server=ghcr.io `
#   --docker-username=naveenatnew `
#
#   --docker-email=your-email@example.com `
#   --namespace ai-mlops