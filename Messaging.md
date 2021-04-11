# Messaging Patterns

| Pattern | Summary  | Implementations |
| --- | --- | --- |
| Priority Queue | Prioritize requests sent to services so that requests with a higher priority are received and processed more quickly than those with a lower priority. This pattern is useful in applications that offer different service level guarantees to individual clients. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/priority-queue#example) |
| Asynchronous Request-Reply | Decouple backend processing from a frontend host, where backend processing needs to be asynchronous, but the frontend still needs a clear response. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/async-request-reply#example) |
| Choreography | Let each service decide when and how a business operation is processed, instead of depending on a central orchestrator. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/choreography#example) |
