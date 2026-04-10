from collections import deque


def process_jobs(jobs: list[str]) -> list[str]:
    queue = deque(jobs)
    done: list[str] = []
    while queue:
        done.append(queue.popleft())
    return done



def round_robin_once(players: list[str]) -> list[str]:
    queue = deque(players)
    if queue:
        queue.append(queue.popleft())
    return list(queue)


if __name__ == "__main__":
    print(process_jobs(["job-1", "job-2", "job-3"]))
    print(round_robin_once(["A", "B", "C", "D"]))
