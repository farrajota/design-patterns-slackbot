# Operational Excellence Patterns

| Pattern | Summary | Implementations |
| --- | --- | --- |
| Ambassador | Create helper services that send network requests on behalf of a consumer service or application. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/ambassador#example) |
| Anti-Corruption Layer | Implement a façade or adapter layer between different subsystems that don't share the same semantics. |  |
| External Configuration Store | Move configuration information out of the application deployment package to a centralized location. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/external-configuration-store#example) |
| Gateway Aggregation | Use a gateway to aggregate multiple individual requests into a single request. | [Conf](https://docs.microsoft.com/en-us/azure/architecture/patterns/gateway-aggregation#example) |
| Gateway Offloading | Offload shared or specialized service functionality to a gateway proxy. | [Conf](https://docs.microsoft.com/en-us/azure/architecture/patterns/gateway-offloading#example) |
| Gateway Routing | Route requests to multiple services using a single endpoint. | [Conf](https://docs.microsoft.com/en-us/azure/architecture/patterns/gateway-routing#example) |
| Geodes | Deploy backend services into a set of geographical nodes, each of which can service any client request in any region. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/retry#example) |
| Health Endpoint Monitoring | Implement functional checks in an application that external tools can access through exposed endpoints at regular intervals. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/health-endpoint-monitoring#example) |
