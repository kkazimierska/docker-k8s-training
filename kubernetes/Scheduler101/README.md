## What is Kubernetes Scheduling?

- The Kubernetes Scheduler is a core component of Kubernetes: After a user or a controller creates a Pod, the Kubernetes Scheduler, monitoring the Object Store for unassigned Pods, will assign the Pod to a Node. Then, the Kubelet, monitoring the Object Store for assigned Pods, will execute the Pod.

## what is the scheduler for?

![](https://raw.githubusercontent.com/collabnix/dockerlabs/master/kubernetes/workshop/Scheduler101/schedulerhow.png)

The Kubernetes scheduler is in charge of scheduling pods onto nodes. Basically it works like this:

   1. You create a pod
   2. The scheduler notices that the new pod you created doesn’t have a node assigned to it
   3. The scheduler assigns a node to the pod

It’s not responsible for actually running the pod – that’s the kubelet’s job. So it basically just needs to make sure every pod has a node assigned to it. Easy, right?

Kubernetes in general has this idea of a “controller”. A controller’s job is to:

  - look at the state of the system
  - notice ways in which the actual state does not match the desired state (like “this pod needs to be assigned a node”)
  - repeat

The scheduler is a kind of controller. There are lots of different controllers and they all have different jobs and operate independently.


## How Kubernetes Selects The Right node?


- This part takes the most work as there are several algorithms that the Scheduler must use to make this decision. Some of those algorithms depend on user-supplied options, while Kubernetes itself calculates others.
- In simple world we can explain in simple questions - just assume schduler ask these questions to nodes-

### Do You Have What it Takes To Run This Pod?

- A node may be overloaded with so many busy pods consuming most of its CPU and memory. So, when the scheduler has a Pod to deploy, it determines whether or not the node has the necessary resources.
- If a Pod deploy to node that doesnot have enough memory(just an example ) that pod has requesting that hosted appliction might behave unexpectedly or even crash.

### Are You a Better Candidate For Having This Pod ?

- In addition to true/false decisions a.k.a predicates, the scheduler executes some calculations (or functions) to determine which node is more suited to be hosting the pod in question.
- For example, a node where the pod image is already present (like it’s been pulled before in a previous deployment) has a better chance of having the pod scheduled to it because no time will be wasted downloading the image again.
- Another example is when the scheduler favors a node that does not include other pods of the same Service. This algorithm helps spread the Service pods on multiple nodes as much as possible so that one node failure does not cause the entire Service to go down. Such a decision-making method is called the spreading function.
- Several decisions, like the above examples, are grouped, and weight is calculated for each node based on the final decision. The node with the highest priority wins the pod deployment.
### The Final Decision

- The scheduler determines all the nodes that it knows they exist and are healthy.
- The scheduler runs the  tests to filter out nodes that are not suitable. The rest of the nodes form a group of possible nodes.
- The scheduler runs priority tests against the possible nodes. Candidates are ordered by their score with the highest ones on the top. At this point, the highest-scoring possible node gets chosen. But sometimes there may be more than one node with the same score.
- If nodes have the same score, they are moved to the final list. The Kubernetes Scheduler selects the winning node in a round-robin fashion to ensure that it equally spreads the load among the machines.