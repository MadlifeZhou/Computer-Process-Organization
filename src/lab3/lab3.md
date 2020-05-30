## Lab3 
### Variant Description: Variant 4(`concurrent.futures`)
In this variant, we implemented a module just like `concurrent.futures` which is a high level concurrent library to execute programs.
### Work Demonstration
1. `ThreadPoolExecutor` is a global worker pool. Every function will be executed in this pool with fixed number of threads specified by `max_workers` value.  
1.2 `submit()` returns `future` object which can show the different state of this work. Meanwhile, function and `future` will be packed into a single object `_WorkItem` which will be putted into a queue.    
1.3 In `_start_working()` a new thread will be created and execute globla function `_worker()`.  
1.4 In function `_worker()`, every thread fetches a `_WorkItem` from the queue. Please note that it is a infinite `while` loop, `queue.get()` will block itself when the queue is empty. Once there is a new `_WorkItem` putted into this queue, one of these thread will be awaken and execute the corresponding item.
2. `Future` is an object shows different state of a work. There are 4 different states of a `future`.  
2.1 `PENDING`: When a new job has been created.  
2.2 `RUNNING`: When a job is running.  
2.3 `FINISHED`: When a job has been done.  
2.4 `CANCELLED`: When a job was cancelled.