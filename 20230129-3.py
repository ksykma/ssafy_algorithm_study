def is_position_safe(N, M, position):
    if M == 0:
        return bool(position[0])
    elif M == 1:
        return bool(position[0] - N + 1)
    elif M == 2:
        return bool(position[1])
    else:
        return bool(position[1] - N + 1)


if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False