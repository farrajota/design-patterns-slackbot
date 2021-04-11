# Reliability Patterns

| Pattern | Summary | Implementations |
| --- | --- | --- |
| Bulkhead | Isolate elements of an application into pools so that if one fails, the others will continue to function. | [Yaml](https://docs.microsoft.com/en-us/azure/architecture/patterns/bulkhead#example) |
| Circuit Breaker | Handle faults that might take a variable amount of time to recover from, when connecting to a remote service or resource. This can improve the stability and resiliency of an application. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker#example) |
| Compensating Transaction | Undo the work performed by a series of steps, which together define an eventually consistent operation. |  |
| Deployment Stamps | Deploy multiple independent copies of application components, including data stores. |  |
| Geodes | Deploy backend services into a set of geographical nodes, each of which can service any client request in any region. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/retry#example) |
| Health Endpoint Monitoring | Implement functional checks in an application that external tools can access through exposed endpoints at regular intervals. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/health-endpoint-monitoring#example) |
| Leader Election | Coordinate the actions performed by a collection of collaborating task instances in a distributed application by electing one instance as the leader that assumes responsibility for managing the other instances. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/leader-election#example) |
| Queue-Based Load Leveling | Use a queue that acts as a buffer between a task and a service that it invokes in order to smooth intermittent heavy loads. |  |
| Retry | Enable an application to handle transient failures when it tries to connect to a service or network resource, by transparently retrying a failed operation. This can improve the stability of the application. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/retry#example) |
| Scheduler Agent Supervisor | Coordinate a set of actions across a distributed set of services and other remote resources. |  |
