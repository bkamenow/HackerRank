class QueueUsingTwoStacks:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, element):
        self.stack_enqueue.append(element)

    def dequeue(self):
        if not self.stack_dequeue:
            self.move_elements_to_dequeue()

        if self.stack_dequeue:
            return self.stack_dequeue.pop()

        return None

    def front(self):
        if not self.stack_dequeue:
            self.move_elements_to_dequeue()

        return self.stack_dequeue[-1] if self.stack_dequeue else None

    def move_elements_to_dequeue(self):
        while self.stack_enqueue:
            self.stack_dequeue.append(self.stack_enqueue.pop())


def process_queries(queries):
    queue = QueueUsingTwoStacks()

    for query in queries:
        query_type = query[0]

        if query_type == 1:
            element = query[1]
            queue.enqueue(element)
        elif query_type == 2:
            queue.dequeue()
        elif query_type == 3:
            print(queue.front())


if __name__ == "__main__":
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    process_queries(queries)
