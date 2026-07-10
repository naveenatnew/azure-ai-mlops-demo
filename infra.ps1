# Run az login manually before running this script


$rg = "mlDemo-rg"
$region = "southindia"
$aks = "mlDemo-AKS"
$identity = "github-oidc-identity"
$repo = "repo:naveenatnew/azure-ai-mlops-demo:ref:refs/heads/main"

az group create `
    --name $rg `
    --location $region

az aks create `
    --resource-group $rg `
    --name $aks `
    --tier free `
    --node-count 1 `
    --node-vm-size Standard_B2ms `
    --generate-ssh-keys

az aks get-credentials `
    --resource-group $rg `
    --name $aks `
    --overwrite-existing

az identity create `
    --resource-group $rg `
    --name $identity

$aksId = az aks show `
    --resource-group $rg `
    --name $AKS_NAME `
    --query id `
    --output tsv

$principalId =az identity show `
    --name $identity `
    --resource-group $rg `
    --query principalId

az role assignment create `
    --assignee $principalId `
    --role "Azure Kubernetes Service Cluster User Role" `
    --scope $aksId

az identity federated-credential create `
    --resource-group $rg `
    --identity-name $identity `
    --name github-main `
    --issuer "https://token.actions.githubusercontent.com" `
    --subject $repo `
    --audiences "api://AzureADTokenExchange"

