After infra creation run the below code manually. This is required if GHRC private.
kubectl create secret docker-registry ghcr-secret `
  --docker-server=ghcr.io `
  --docker-username=<github username> `
  --docker-password=<github PAT> `
  --docker-email=your-email@example.com `
  --namespace <namespace>