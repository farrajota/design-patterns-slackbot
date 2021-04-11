# Design And Implementation Patterns

| Pattern | Summary | Implementations |
| --- | --- | --- |
| Ambassador | Create helper services that send network requests on behalf of a consumer service or application. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/ambassador#example) |
| Anti-Corruption Layer | Implement a façade or adapter layer between different subsystems that don't share the same semantics. |  |
| Backends for Frontends | Create separate backend services to be consumed by specific frontend applications or interfaces. |  |
| Command and Query Responsibility Segregation (CQRS) | Segregate operations that read data from operations that update data by using separate interfaces. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/cqrs#example) |
| Compute Resource Consolidation | Consolidate multiple tasks or operations into a single computational unit. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/compute-resource-consolidation#example) |
| External Configuration Store | Move configuration information out of the application deployment package to a centralized location. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/external-configuration-store#example) |
| Gateway Aggregation | Use a gateway to aggregate multiple individual requests into a single request. | [Nginx Conf](https://docs.microsoft.com/en-us/azure/architecture/patterns/gateway-aggregation#example) |
| Gateway Offloading | Offload shared or specialized service functionality to a gateway proxy. | [Nginx Conf](https://docs.microsoft.com/en-us/azure/architecture/patterns/gateway-offloading#example) |
| Gateway Routing | Route requests to multiple services using a single endpoint. | [Nginx Conf](https://docs.microsoft.com/en-us/azure/architecture/patterns/gateway-routing#example) |
| Leader Election | Coordinate the actions performed by a collection of collaborating task instances in a distributed application by electing one instance as the leader that assumes responsibility for managing the other instances. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/leader-election#example) |
| Pipes and Filters | Break down a task that performs complex processing into a series of separate elements that can be reused. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/pipes-and-filters#example) |
