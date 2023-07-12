---
title: "Ports, Websockets and K8s"
tags: ["k8s"]
date: 2023-01-01
# aliases: ["/first"]
# weight: 1
# author: "Peter Dieleman"
# showToc: false
# TocOpen: false
draft: false
# hidemeta: false
# comments: false
# description: "A guide on extending the battery life of your linux laptop"
# disableShare: false
# searchHidden: false
---

Considerations when deploying app relying on web sockets on kubernetes.

- [post](https://medium.com/k8scaleio/running-websocket-app-on-kubernetes-2e13eabb4c4f)

## TargetPorts, Ports & Nodeports

These two concepts govern ingress at the `Service` & `Pod` level:

- `port`: port that corresponding `Service` is listening on
- `targetPort`: port to which traffic is directed _inside_ the container

These two concepts govern ingress at the `Service` & `Cluster` level:

- `ClusterIP`: This is the default type for service in Kubernetes; an address that can be used inside the cluster. Can be used in conjunction with a Load balancer/ingress controller to redirect outside traffic to Services.
- `NodePort`:
  - "A NodePort is an open port on every node of your cluster. Kubernetes transparently routes incoming traffic on the NodePort to your service, even if your application is running on a different node."
  - "A NodePort service has two differences from a normal “ClusterIP” service. First, the type is “NodePort.” There is also an additional port called the nodePort that specifies which port to open on the nodes. If you don’t specify this port, it will pick a random port".

## Sources

- <https://ashwin.cloud/blog/port-vs-targetport-in-kubernetes-service/>
- <https://www.tkng.io/services/nodeport/#:~:text=NodePort%20builds%20on%20top%20of,values%20can%20remain%20the%20same.>
- <https://sysdig.com/blog/kubernetes-services-clusterip-nodeport-loadbalancer/>
- <https://www.getambassador.io/learn/kubernetes-ingress/kubernetes-ingress-nodeport-load-balancers-and-ingress-controllers>
- <https://medium.com/google-cloud/kubernetes-nodeport-vs-loadbalancer-vs-ingress-when-should-i-use-what-922f010849e0>
