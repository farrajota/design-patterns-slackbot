# Reliability Patterns

| Pattern | Summary | Implementations |
| --- | --- | --- |
| Circuit Breaker | Handle faults that might take a variable amount of time to recover from, when connecting to a remote service or resource. This can improve the stability and resiliency of an application. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker#example) |
| Retry | Enable an application to handle transient failures when it tries to connect to a service or network resource, by transparently retrying a failed operation. This can improve the stability of the application. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/retry#example) | 