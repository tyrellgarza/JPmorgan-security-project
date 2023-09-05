"""
Tyrell Garza

The goal of this coding activity is to design a system that limits the number
of active roles that any given person has. A role gives the user access to
some thing, whether it be a piece of data or an internal system.
The system achieves this requirement by keeping track of the last k roles
that a person has used. If a new role is used, the oldest role is removed
if there are already k active roles for that person. Each role has a name
and a message which contains details about its use by the person. You
only need to store the last message for a role invocation.

Implement the constructor, get, and set methods of RolesCache. Each
instance of the RolesCache corresponds to a single person.

Finally, fill out the runtime complexity for get and set and the overall
space used. Use Big O notation, i.e. O(1), O(N), etc. For a refresher
on Big O notation.

"""

from collections import deque


class RolesCache:
    def __init__(self, capacity):
        self.cache = {}  # Dictionary to store roles and their messages
        self.order = deque()  # Deque to keep track of the order of roles
        self.capacity = capacity

    def get(self, role):
        # Returns the message corresponding to the last invocation of that
        # role, None if the role does not exist in the cache.
        return self.cache.get(role, None)

    def set(self, role, message):
        # If the role already exists, update its message.
        if role in self.cache:
            self.cache[role] = message
        else:
            # If the cache is at capacity, remove the oldest role.
            if len(self.order) == self.capacity:
                oldest_role = self.order.popleft()
                del self.cache[oldest_role]
            # Add the new role to the cache and order.
            self.cache[role] = message
            self.order.append(role)

    def _complexity(self):
        return {"get": "O(1)", "set": "O(1)", "space": "O(k)"}


def test_roles_cache():
    # Initialize a cache with a capacity of 3
    cache = RolesCache(3)

    # Test 1: Basic Functionality
    cache.set("Admin", "Accessed dashboard")
    assert cache.get("Admin") == "Accessed dashboard"

    # Test 2: Update Existing Role
    cache.set("Admin", "Modified user data")
    assert cache.get("Admin") == "Modified user data"

    # Test 3: Exceed Capacity
    cache.set("Editor", "Edited article")
    cache.set("Viewer", "Viewed article")
    # At this point, the cache has "Admin", "Editor", and "Viewer"
    cache.set("Moderator", "Reviewed comments")
    # "Admin" should be evicted since it's the oldest
    assert cache.get("Admin") is None
    assert cache.get("Editor") == "Edited article"
    assert cache.get("Viewer") == "Viewed article"
    assert cache.get("Moderator") == "Reviewed comments"

    # Test 4: Retrieve Non-Existent Role
    assert cache.get("Guest") is None

    # Test 5: Eviction Order
    cache.set("Contributor", "Added a comment")
    # "Editor" should be evicted since it's now the oldest after "Admin"
    assert cache.get("Editor") is None
    assert cache.get("Viewer") == "Viewed article"
    assert cache.get("Moderator") == "Reviewed comments"
    assert cache.get("Contributor") == "Added a comment"

    print("All tests passed!")


if __name__ == "__main__":
    test_roles_cache()
