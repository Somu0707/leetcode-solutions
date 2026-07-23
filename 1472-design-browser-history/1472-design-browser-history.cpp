class Node {
    public: 
    string url;
    Node* prev;
    Node* next;

    Node(string s){
        url = s;
        prev = NULL;
        next = NULL;
    }
};


class BrowserHistory {
public:
    Node* curr;
    BrowserHistory(string homepage) {
        curr = new Node(homepage);
    }
    
    void visit(string url) {
        Node* temp = curr->next;
        while(temp!=NULL){
            Node* nextnode = temp->next;
            delete temp;
            temp = nextnode;
        }
        curr->next = NULL;
        Node* newNode = new Node(url);
        curr->next = newNode;
        newNode->prev = curr;
        curr = newNode;
    }
    
    string back(int steps) {
        while(steps > 0 && curr->prev != NULL){
            steps--;
            curr = curr->prev;
        }
        return curr->url;
    }
    
    string forward(int steps) {
         while(steps > 0 && curr->next != NULL){
            steps--;
            curr = curr->next;
        }
        return curr->url;
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */