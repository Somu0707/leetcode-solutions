class MyCircularQueue {

    int queue[];
    int front;
    int rear;
    int maxS;
    int curS;

    public MyCircularQueue(int k) {
        queue = new int[k];
        front = 0;
        rear = -1;
        maxS = k;
        curS = 0;
    }

    public boolean enQueue(int value) {
        if (isFull())
            return false;

        rear = (rear + 1) % maxS;
        queue[rear] = value;
        curS++;
        return true;
    }

    public boolean deQueue() {
        if (isEmpty())
            return false;

        front = (front + 1) % maxS;
        curS--;
        return true;
    }

    public int Front() {
        if (isEmpty())
            return -1;

        return queue[front];
    }

    public int Rear() {
        if (isEmpty())
            return -1;

        return queue[rear];
    }

    public boolean isEmpty() {
        return curS == 0;
    }

    public boolean isFull() {
        return curS == maxS;
    }
}