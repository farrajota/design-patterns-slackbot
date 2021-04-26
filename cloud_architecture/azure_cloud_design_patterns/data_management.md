# Data Management Patterns

| Pattern | Summary | Implementations |
| --- | --- | --- |
| Cache-Aside | Load data on demand into a cache from a data store. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/cache-aside#example) |
| Command and Query Responsibility Segregation (CQRS) | Segregate operations that read data from operations that update data by using separate interfaces. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/cqrs#example) |
| Event Sourcing | Use an append-only store to record the full series of events that describe actions taken on data in a domain. |  |
| Index Table | Create indexes over the fields in data stores that are frequently referenced by queries. |  |
| Materialized View | Generate prepopulated views over the data in one or more data stores when the data isn't ideally formatted for required query operations. |  |
| Sharding | Divide a data store into a set of horizontal partitions or shards. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/sharding#example) |
| Static Content Hosting | Deploy static content to a cloud-based storage service that can deliver them directly to the client. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/static-content-hosting#example) |
| Valet Key | Use a token or key that provides clients with restricted direct access to a specific resource or service. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/valet-key#example) |
