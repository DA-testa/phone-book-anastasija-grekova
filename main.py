class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep dictionary of all existing contacts.
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # Add or update contact's name
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            # Remove contact, if it exists
            contacts.pop(cur_query.number, None)
        else:
            # Look up contact by number
            response = contacts.get(cur_query.number, 'not found')
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
