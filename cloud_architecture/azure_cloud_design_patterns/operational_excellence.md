# Operational Excellence Patterns

| Pattern | Summary | Examples |
| --- | --- | --- |
| [Ambassador](https://docs.microsoft.com/en-us/azure/architecture/patterns/ambassador) | Create helper services that send network requests on behalf of a consumer service or application. |  |
| [Anti-Corruption Layer](https://docs.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) | Implement a façade or adapter layer between different subsystems that don't share the same semantics. |  |
| [External Configuration Store](https://docs.microsoft.com/en-us/azure/architecture/patterns/external-configuration-store) | Move configuration information out of the application deployment package to a centralized location. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/external-configuration-store#example) |
| [Gateway Aggregation](https://docs.microsoft.com/en-us/azure/architecture/patterns/gateway-aggregation) | Use a gateway to aggregate multiple individual requests into a single request. | [Nginx Conf](https://docs.microsoft.com/en-us/azure/architecture/patterns/gateway-aggregation#example) |
| [Gateway Offloading](https://docs.microsoft.com/en-us/azure/architecture/patterns/gateway-offloading) | Offload shared or specialized service functionality to a gateway proxy. | [Nginx Conf](https://docs.microsoft.com/en-us/azure/architecture/patterns/gateway-offloading#example) |
| [Gateway Routing](https://docs.microsoft.com/en-us/azure/architecture/patterns/gateway-routing) | Route requests to multiple services using a single endpoint. | [Nginx Conf](https://docs.microsoft.com/en-us/azure/architecture/patterns/gateway-routing#example) |
| [Geodes](https://docs.microsoft.com/en-us/azure/architecture/patterns/geodes) | Deploy backend services into a set of geographical nodes, each of which can service any client request in any region. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/retry#example) |
| [Health Endpoint Monitoring](https://docs.microsoft.com/en-us/azure/architecture/patterns/health-endpoint-monitoring) | Implement functional checks in an application that external tools can access through exposed endpoints at regular intervals. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/health-endpoint-monitoring#example) |
| [Materialized View](https://docs.microsoft.com/en-us/azure/architecture/patterns/materialized-view) | Generate prepopulated views over the data in one or more data stores when the data isn't ideally formatted for required query operations. |  |
| [Sidecar](https://docs.microsoft.com/en-us/azure/architecture/patterns/sidecar) | Deploy components of an application into a separate process or container to provide isolation and encapsulation. |  |
| [Strangler Fig](https://docs.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) | Incrementally migrate a legacy system by gradually replacing specific pieces of functionality with new applications and services. |  |
