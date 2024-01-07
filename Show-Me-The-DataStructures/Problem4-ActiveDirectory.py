class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def search(self, user, group):
        # first check in users of that group itself
        users = group.get_users()
        if user in users:
            return True

        for group in group.get_groups():
            # second check in groups of the group as well
            return self.search(user, group)

        return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
no_user_group = Group("no_user_group")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test Case 1: User is added into the sub_child group but if checked against parent it should exists because of heirarchy
print(parent.search(sub_child_user, parent))

# Test Case 2: User is added to another group but checked against another group
print(parent.search(sub_child_user, no_user_group))

testparent = Group("testparent")
testchild = Group("testchild")
testparent.add_group(testchild)
test_users  = Group("test_users")
test_users.add_user("john doe")
# Test Case 3: User is not part of any group and checked in the groups
print(parent.search("john doe", testparent))

# Now adding the test_users group to the testchild group and checking against testparent parent
testchild.add_group(test_users)
print(parent.search("john doe", testparent))


# Test Case 4: User is not part of any group and checked in the groups
print(parent.search("no_user", parent))
