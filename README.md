# Design Patterns

List fo design patterns I've found that look promising to learn more about / take a look at.

## Catalog of patterns

| Pattern | Summary | Category | Implementations |
| --- | --- | --- | --- |
| Ambassador | Create helper services that send network requests on behalf of a consumer service or application. | [Design And Implementation](design_and_implementation.md) [Operational Excellence](operational_excellence.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/ambassador#example) |
| Anti-Corruption Layer | Implement a façade or adapter layer between different subsystems that don't share the same semantics. | [Design And Implementation](design_and_implementation.md) [Operational Excellence](operational_excellence.md) |  |
| Asynchronous Request-Reply | Decouple backend processing from a frontend host, where backend processing needs to be asynchronous, but the frontend still needs a clear response. | [Messaging](messaging.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/async-request-reply#example) |
| Backends for Frontends | Create separate backend services to be consumed by specific frontend applications or interfaces. | [Design And Implementation](design_and_implementation.md) |  |
| Bulkhead | Isolate elements of an application into pools so that if one fails, the others will continue to function. | [Reliability](reliability.md) | [Yaml](https://docs.microsoft.com/en-us/azure/architecture/patterns/bulkhead#example) |
| Cache-Aside | Load data on demand into a cache from a data store. | [Data Management](data_management.md) [Performance Efficiency](performance_efficiency.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/cache-aside#example) |
| Choreography | Let each service decide when and how a business operation is processed, instead of depending on a central orchestrator. | [Messaging](messaging.md) [Performance Efficiency](performance_efficiency.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/choreography#example) |
| Circuit Breaker | Handle faults that might take a variable amount of time to recover from, when connecting to a remote service or resource. This can improve the stability and resiliency of an application. | [Reliability](reliability.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker#example) |
| Claim Check | Split a large message into a claim check and a payload to avoid overwhelming a message bus. | [Messaging](messaging.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/claim-check#examples) |
| Compensating Transaction | Undo the work performed by a series of steps, which together define an eventually consistent operation. | [Reliability](reliability.md) |  |
| Competing Consumers | Enable multiple concurrent consumers to process messages received on the same messaging channel. | [Messaging](messaging.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/competing-consumers#example) |
| Compute Resource Consolidation | Consolidate multiple tasks or operations into a single computational unit. | [Design And Implementation](design_and_implementation.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/compute-resource-consolidation#example) |
| Command and Query Responsibility Segregation (CQRS) | Segregate operations that read data from operations that update data by using separate interfaces. | [Data Management](data_management.md) [Design And Implementation](design_and_implementation.md) [Performance Efficiency](performance_efficiency.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/cqrs#example) |
| Deployment Stamps | Deploy multiple independent copies of application components, including data stores. | [Reliability](reliability.md) [Performance Efficiency](performance_efficiency.md) |  |
| Event Sourcing | Use an append-only store to record the full series of events that describe actions taken on data in a domain. | [Data Management](data_management.md) [Performance Efficiency](performance_efficiency.md) |  |
| External Configuration Store | Move configuration information out of the application deployment package to a centralized location. | [Design And Implementation](design_and_implementation.md) [Operational Excellence](operational_excellence.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/external-configuration-store#example) |
| Federated Identity | Delegate authentication to an external identity provider. | [Security](security.md) |  |
| Gatekeeper | Protect applications and services by using a dedicated host instance that acts as a broker between clients and the application or service, validates and sanitizes requests, and passes requests and data between them. | [Security](security.md) |  |
| Gateway Aggregation | Use a gateway to aggregate multiple individual requests into a single request. | [Design And Implementation](design_and_implementation.md) [Operational Excellence](operational_excellence.md) | [Nginx Conf](https://docs.microsoft.com/en-us/azure/architecture/patterns/gateway-aggregation#example) |
| Gateway Offloading | Offload shared or specialized service functionality to a gateway proxy. | [Design And Implementation](design_and_implementation.md) [Operational Excellence](operational_excellence.md) | [Nginx Conf](https://docs.microsoft.com/en-us/azure/architecture/patterns/gateway-offloading#example) |
| Gateway Routing | Route requests to multiple services using a single endpoint. | [Design And Implementation](design_and_implementation.md) [Operational Excellence](operational_excellence.md) | [Nginx Conf](https://docs.microsoft.com/en-us/azure/architecture/patterns/gateway-routing#example) |
| Geodes | Deploy backend services into a set of geographical nodes, each of which can service any client request in any region. | [Reliability](reliability.md) [Operational Excellence](operational_excellence.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/retry#example) |
| Health Endpoint Monitoring | Implement functional checks in an application that external tools can access through exposed endpoints at regular intervals. | [Reliability](reliability.md) [Operational Excellence](operational_excellence.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/health-endpoint-monitoring#example) |
| Index Table | Create indexes over the fields in data stores that are frequently referenced by queries. | [Data Management](data_management.md) [Performance Efficiency](performance_efficiency.md) |  |
| Leader Election | Coordinate the actions performed by a collection of collaborating task instances in a distributed application by electing one instance as the leader that assumes responsibility for managing the other instances. | [Design And Implementation](design_and_implementation.md) [Reliability](reliability.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/leader-election#example) |
| Materialized View | Generate prepopulated views over the data in one or more data stores when the data isn't ideally formatted for required query operations. | [Data Management](data_management.md) [Operational Excellence](operational_excellence.md) |  |
| Pipes and Filters | Break down a task that performs complex processing into a series of separate elements that can be reused. | [Design And Implementation](design_and_implementation.md) [Messaging](messaging.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/pipes-and-filters#example) |
| Priority Queue | Prioritize requests sent to services so that requests with a higher priority are received and processed more quickly than those with a lower priority. This pattern is useful in applications that offer different service level guarantees to individual clients. | [Messaging](messaging.md) [Performance Efficiency](performance_efficiency.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/priority-queue#example) |
| Publisher/Subscriber | Enable an application to announce events to multiple interested consumers asynchronously, without coupling the senders to the receivers. | [Messaging](messaging.md) |  |
| Queue-Based Load Leveling | Use a queue that acts as a buffer between a task and a service that it invokes in order to smooth intermittent heavy loads. | [Reliability](reliability.md) [Messaging](messaging.md) [Resiliency](resiliency.md) [Performance Efficiency](performance_efficiency.md) |  |
| Retry | Enable an application to handle transient failures when it tries to connect to a service or network resource, by transparently retrying a failed operation. This can improve the stability of the application. | [Reliability](reliability.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/retry#example) |
| Scheduler Agent Supervisor | Coordinate a set of actions across a distributed set of services and other remote resources. | [Messaging](messaging.md) [Reliability](reliability.md) |  |
| Sequential Convoy | Process a set of related messages in a defined order, without blocking processing of other groups of messages. | [Messaging](messaging.md) |  |
| Sharding | Divide a data store into a set of horizontal partitions or shards. | [Data Management](data_management.md) [Performance Efficiency](performance_efficiency.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/sharding#example) |
| Sidecar | Deploy components of an application into a separate process or container to provide isolation and encapsulation. | [Design And Implementation](design_and_implementation.md) [Operational Excellence](operational_excellence.md) |  |

## Categories of Design Patterns

- [Data Management](data_management.md)
- [Design And Implementation](design_and_implementation.md)
- [Messaging](messaging.md)
- [Operational Excellence](operational_excellence.md)
- [Performance Efficiency](performance_efficiency.md)
- [Reliability](reliability.md)
- [Resiliency](resiliency.md)
- [Security](security.md)

# References

- https://docs.microsoft.com/en-us/azure/architecture/patterns/index-patterns

# License

[MIT License](LICENSE)
