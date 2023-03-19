from queue import PriorityQueue

def parallel_processing(n, m, data):
    output = []
    pq = PriorityQueue()   # initialize a priority queue to store workers

    for i in range(n):
        pq.put((0, i))   # add workers to the priority queue with start time 0

    for i in range(m):
        job_time = data[i]
        start_time, worker_id = pq.get()   # get the worker with minimum start time
        output.append((worker_id, start_time))   # add the worker to output
        end_time = start_time + job_time   # calculate the end time
        pq.put((end_time, worker_id))   # add the worker back to priority queue with new end time

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for worker_id, start_time in result:
        print(worker_id, start_time)

if __name__ == "__main__":
    main()
