from kubernetes import client, config
import sys

def main():
    config.load_incluster_config()

    v1 = client.CoreV1Api()
    namespace = sys.argv[1]
    print("Listing pods with their IPs:")
    ret = v1.list_namespaced_pod(namespace, watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


if __name__ == '__main__':
    main()
