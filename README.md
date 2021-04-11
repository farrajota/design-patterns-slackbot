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
| Priority Queue | Prioritize requests sent to services so that requests with a higher priority are received and processed more quickly than those with a lower priority. This pattern is useful in applications that offer different service level guarantees to individual clients. | [Messaging](messaging.md) [Performance Efficiency](performance_efficiency.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/priority-queue#example) |
| Retry | Enable an application to handle transient failures when it tries to connect to a service or network resource, by transparently retrying a failed operation. This can improve the stability of the application. | [Reliability](reliability.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/retry#example) |

## Categories of Design Patterns

- [Data Management](data_management.md)
- [Design And Implementation](design_and_implementation.md)
- [Messaging](messaging.md)
- [Operational Excellence](operational_excellence.md)
- [Performance Efficiency](performance_efficiency.md)
- [Reliability](reliability.md)

# References

- https://docs.microsoft.com/en-us/azure/architecture/patterns/index-patterns

# License

[MIT License](LICENSE)
