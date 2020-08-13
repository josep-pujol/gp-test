from psb_tree import PSBTree


def iter_records(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

def parse_sequence(seq):
    return [*map(int, seq.split(' '))]


# File iterator
iter_ln = iter_records('input.txt')
C = int(next(iter_ln))
for _ in range(C):
    sequence = parse_sequence(next(iter_ln))
    # Create Partial Sums Binary Tree Object
    tree = PSBTree(sequence)
    M = int(next(iter_ln))
    for _ in range(M):
        oper, a, b = next(iter_ln).split(' ')
        if oper == 'sum':
            print(tree.nums, sum(tree.nums))
            print(tree.aux)
            print(tree.sum(int(a), int(b)))
        elif oper == 'update':
            tree.update(int(a), int(b))
        else:
            print(f'Unknown operation "{oper}"!')
