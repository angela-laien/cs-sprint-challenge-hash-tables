# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # storage = {}
    # result = []
    # for path in files:
    #     file = path.split("/")
    #     target = file[-1]
    #     print(target)
    #     if target in storage:
    #         storage[target].append[path]
    #     for query in queries:
    #         if query in storage:
    #             result.append(path)

    # return result 
   

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
