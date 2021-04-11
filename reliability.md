# Reliability Patterns

| Pattern | Summary | Implementations |
| --- | --- | --- |
| Bulkhead | Isolate elements of an application into pools so that if one fails, the others will continue to function. | [Yaml](https://docs.microsoft.com/en-us/azure/architecture/patterns/bulkhead#example) |
| Circuit Breaker | Handle faults that might take a variable amount of time to recover from, when connecting to a remote service or resource. This can improve the stability and resiliency of an application. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker#example) |
| Compensating Transaction | Undo the work performed by a series of steps, which together define an eventually consistent operation. |  |
| Retry | Enable an application to handle transient failures when it tries to connect to a service or network resource, by transparently retrying a failed operation. This can improve the stability of the application. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/retry#example) |
