# Performance Efficiency Patterns

| Pattern | Summary | Implementations |
| --- | --- | --- |
| Cache-Aside | Load data on demand into a cache from a data store. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/cache-aside#example) |
| Choreography | Let each service decide when and how a business operation is processed, instead of depending on a central orchestrator. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/choreography#example) |
| Command and Query Responsibility Segregation (CQRS) | Segregate operations that read data from operations that update data by using separate interfaces. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/cqrs#example) |
| Deployment Stamps | Deploy multiple independent copies of application components, including data stores. |  |
| Event Sourcing | Use an append-only store to record the full series of events that describe actions taken on data in a domain. |  |
| Index Table | Create indexes over the fields in data stores that are frequently referenced by queries. |  |
| Priority Queue | Prioritize requests sent to services so that requests with a higher priority are received and processed more quickly than those with a lower priority. This pattern is useful in applications that offer different service level guarantees to individual clients. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/priority-queue#example) |
| Queue-Based Load Leveling | Use a queue that acts as a buffer between a task and a service that it invokes in order to smooth intermittent heavy loads. |  |
| Sharding | Divide a data store into a set of horizontal partitions or shards. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/sharding#example) |
| Static Content Hosting | Deploy static content to a cloud-based storage service that can deliver them directly to the client. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/static-content-hosting#example) |
| Throttling | Control the consumption of resources used by an instance of an application, an individual tenant, or an entire service. |  |
