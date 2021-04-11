# Design Patterns

List fo design patterns I've found that look promising to learn more about /take a look.

## Catalog of patterns

| Pattern | Summary | Category | Implementations |
| --- | --- | --- | --- |
| Ambassador | Create helper services that send network requests on behalf of a consumer service or application. | [Design and Implementation](Design_implementation.md), [Operational Excellence](Operational_excellence.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/ambassador#example) |
| Anti-Corruption Layer | Implement a façade or adapter layer between different subsystems that don't share the same semantics. | [Design and Implementation](Design_implementation.md), [Operational Excellence](Operational_excellence.md) | |
| Asynchronous Request-Reply | Decouple backend processing from a frontend host, where backend processing needs to be asynchronous, but the frontend still needs a clear response. | [Messaging](Messaging.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/async-request-reply#example) |
| Backends for Frontends | Create separate backend services to be consumed by specific frontend applications or interfaces. | [Design and Implementation](Design_implementation.md) | |
| Bulkhead | Isolate elements of an application into pools so that if one fails, the others will continue to function. | [Reliability](Reliability.md) | [YAML](https://docs.microsoft.com/en-us/azure/architecture/patterns/bulkhead#example) |
| Cache-Aside | Load data on demand into a cache from a data store. | [Data Management](Data_management.md) [Performance Efficiency](Performance_efficiency.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/cache-aside#example) |
| Choreography | Let each service decide when and how a business operation is processed, instead of depending on a central orchestrator. | [Messaging](Messaging.md) [Performance Efficiency](Performance_efficiency.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/choreography#example) |
| Circuit Breaker | Handle faults that might take a variable amount of time to recover from, when connecting to a remote service or resource. This can improve the stability and resiliency of an application. | [Reliability](Reliability.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker#example) |
| Priority Queue | Prioritize requests sent to services so that requests with a higher priority are received and processed more quickly than those with a lower priority. This pattern is useful in applications that offer different service level guarantees to individual clients. | [Messaging](Messaging.md) [Performance Efficiency](Performance_efficiency.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/priority-queue#example) |
| Retry | Enable an application to handle transient failures when it tries to connect to a service or network resource, by transparently retrying a failed operation. This can improve the stability of the application. | [Reliability](Reliability.md) | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/retry#example) |

# References

- https://docs.microsoft.com/en-us/azure/architecture/patterns/index-patterns

# License

[MIT License](LICENSE)
