import uuid

POD = 'tutorial-7d4cb66fd8-t87gx'
LABELS = {"com.docker.project": "tutorial"}
NAMESPACE = 'default'

def test_pod_failure_ch_mesh_lib(app, ch_mesh_cl, k8s_cl):
    app.healthcheck()
    expr_name = f'poc-test-{str(uuid.uuid4())}'
    ch_mesh_cl.start_pod_failure(
        labels=LABELS,
        ns=[NAMESPACE],
        expr_name=expr_name
    )
    ch_mesh_cl.delete_pod_failure(expr_name=expr_name)
    k8s_cl.wait_pods_up(POD, NAMESPACE)
    k8s_cl.wait_containers_ready(POD, NAMESPACE)
    app.healthcheck()

