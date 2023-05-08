# poc-chaos-mesh

## Setup environment and run test
- Install python 3.11
- Install dependencies from requirements.txt
- Set up kubernetes cluster https://kubernetes.io/docs/setup/
- Install chaos mesh in 'chaos-mesh' namespace on your cluster https://chaos-mesh.org/docs/quick-start/
- Create k8s test application using test_app/tutorial.yaml
- Under tests/test_pod_failure_expr.py update the test constants (POD, LABELS, NAMESPACE)
- Run test