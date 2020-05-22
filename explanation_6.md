# Explanation BlockChain exercise
Union -> just iterate over both list, and add each node to a new LinkedList
Intersection -> Iterate Over List2 1 time per item in list1, check whether or not an item of list 1 exists in list 2, if True -> append to a new linked list
# Time and Space complexity:

Union :
     -> O(n + m) being n list1, m list2
Intersection:    
      -> O (n + m + p) being n list1, m list2, p (append to intersected list)
# Time complexity

The time complexity of the union function is quadratic because for each element in the linked list, 
there is a python in operation, which is O(n) by itself,
 to check if they already exits in the list or not.

But, the time complexity of the union function is O(n^3) because,
 there are two while loops that loop over the elements of the two linked lists,
 plus there is Python in operation that checks for each element if they occur in a temporary list or not.	  
# Space complexity
The space complexity for union (and also for intersection) functions is O(n),
 because for both operations there is a temporary array called tmp_list,
 which can grow upto the size of the two input linked lists.
 Also there are two nodes (i.e. node1 and node2) but these should be O(1).
 So overall the space complexity of union is O(n), and the space complexity of intersection is O(n) too.