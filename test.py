def double_list(l):
    return [d * 2 for d in l]


def say_hello():
    print('Hello')


def main():
    l = [1, 2, 3, 4, 5]
    l = double_list(l)
    print(l)
    say_hello()


if __name__ == '__main__':
    main()
