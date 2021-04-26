# Messaging Patterns

| Pattern | Summary | Implementations |
| --- | --- | --- |
| Asynchronous Request-Reply | Decouple backend processing from a frontend host, where backend processing needs to be asynchronous, but the frontend still needs a clear response. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/async-request-reply#example) |
| Choreography | Let each service decide when and how a business operation is processed, instead of depending on a central orchestrator. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/choreography#example) |
| Claim Check | Split a large message into a claim check and a payload to avoid overwhelming a message bus. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/claim-check#examples) |
| Competing Consumers | Enable multiple concurrent consumers to process messages received on the same messaging channel. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/competing-consumers#example) |
| Pipes and Filters | Break down a task that performs complex processing into a series of separate elements that can be reused. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/pipes-and-filters#example) |
| Priority Queue | Prioritize requests sent to services so that requests with a higher priority are received and processed more quickly than those with a lower priority. This pattern is useful in applications that offer different service level guarantees to individual clients. | [C#](https://docs.microsoft.com/en-us/azure/architecture/patterns/priority-queue#example) |
| Publisher/Subscriber | Enable an application to announce events to multiple interested consumers asynchronously, without coupling the senders to the receivers. |  |
| Queue-Based Load Leveling | Use a queue that acts as a buffer between a task and a service that it invokes in order to smooth intermittent heavy loads. |  |
| Scheduler Agent Supervisor | Coordinate a set of actions across a distributed set of services and other remote resources. |  |
| Sequential Convoy | Process a set of related messages in a defined order, without blocking processing of other groups of messages. |  |