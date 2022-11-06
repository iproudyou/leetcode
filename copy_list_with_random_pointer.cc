#include <iostream>
#include <map>
using namespace std;

class Solution {
private:
    map<Node *, Node *> mapping;

public:
    Node* copyRandomList(Node* head) {
        Node *start = head;

        while (start) {
            mapping[start] = new Node{start->val};
            start = start->next;
        }

        start = head;

        while (start) {
            mapping[start]->next = mapping[start->next];
            mapping[start]->random = mapping[start->random];
            start = start->next;
        }

        return mapping[head];
    }
};
