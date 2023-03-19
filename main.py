from queue import PriorityQueue

def parallel_processing(n, m, data):
    output = []
    pq = PriorityQueue()

    for i in range(n):
        pq.put((0, i))

    for i in range(m):
        job_time = data[i]
        start_time, worker_id = pq.get()
        output.append((worker_id, start_time))
        end_time = start_time + job_time
        pq.put((end_time, worker_id))

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for worker_id, start_time in result:
        print(worker_id, start_time)

if __name__ == "__main__":
    main()
