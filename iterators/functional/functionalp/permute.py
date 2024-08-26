def permute(lst):
    def _permute_helper(current, remaining):
        if not remaining:
            yield current
        else:
            for i in range(len(remaining)):
                next_current = current + [remaining[i]]
                next_remaining = remaining[:i] + remaining[i+1:]
                yield from _permute_helper(next_current, next_remaining)

    return list(_permute_helper([], lst))

lst = [1, 2, 3]
print(permute(lst))
