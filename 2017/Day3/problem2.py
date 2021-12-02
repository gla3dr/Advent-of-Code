def get_next_ring(prev_ring):
    prev_ring_index = len(prev_ring) - 1
    next_ring_len = len(prev_ring) + 8
    next_ring = []
    for i in range(next_ring_len):
        if i == 0:
            next_ring.append(prev_ring[prev_ring_index] + prev_ring[0])
            prev_ring_index = 0
        elif i == next_ring_len - 2:
            next_ring.append(next_ring[i - 1] + prev_ring[prev_ring_index - 1] + prev_ring[prev_ring_index] + next_ring[0])
        elif i == next_ring_len - 1:
            next_ring.append(next_ring[i - 1] + prev_ring[prev_ring_index] + next_ring[0])
        elif i % (next_ring_len / 4) == next_ring_len / 4 - 2:
            next_ring.append(next_ring[i - 1] + prev_ring[prev_ring_index - 1] + prev_ring[prev_ring_index])
        elif i % (next_ring_len / 4) == next_ring_len / 4 - 1:
            next_ring.append(next_ring[i - 1] + prev_ring[prev_ring_index])
        elif i % (next_ring_len / 4) == 0:
            next_ring.append(next_ring[i - 1] + next_ring[i - 2] + prev_ring[prev_ring_index] + prev_ring[prev_ring_index + 1])
            prev_ring_index = prev_ring_index + 1
        else:
            next_ring.append(next_ring[i - 1] + prev_ring[prev_ring_index - 1] + prev_ring[prev_ring_index] + prev_ring[prev_ring_index + 1])
            prev_ring_index = prev_ring_index + 1
    return next_ring

def spiral_generator():
    current_ring = [1, 2, 4, 5, 10, 11, 23, 25]
    while True:
        copy = current_ring[:]
        while copy:
            yield copy.pop(0)
        current_ring = get_next_ring(current_ring)

def first_number_larger_than(input):
    return next(n for n in spiral_generator() if n > input)

if __name__ == "__main__":
    print(first_number_larger_than(325489))
