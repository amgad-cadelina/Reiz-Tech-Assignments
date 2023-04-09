class Branch:
    def __init__(self, name):

        self.name = name
        self.branches = []

def calculate_depth(branch, current_depth):

    if not branch.branches:

        return current_depth
    
    else:

        max_depth = current_depth

        for b in branch.branches:

            depth = calculate_depth(b, current_depth+1)

            if depth > max_depth:

                max_depth = depth

        return max_depth


root = Branch("Root")

branch1 = Branch("Branch 1")
branch2 = Branch("Branch 2")
branch3 = Branch("Branch 3")
branch4 = Branch("Branch 4")
branch5 = Branch("Branch 5")

root.branches.append(branch1)
root.branches.append(branch2)

branch1.branches.append(branch3)
branch1.branches.append(branch4)
branch3.branches.append(branch5)


depth = calculate_depth(root, 1)

print("Depth of the structure is", depth)
