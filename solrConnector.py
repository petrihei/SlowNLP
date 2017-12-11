from urllib.request import urlopen

def title_query(word):

    return "(title:" + word + ")"



# how many documents found
# print(response['response']['numFound'], "documents found.")

# Print the name of each document.

def get_results(word):

    # look for the closest matches
    query = word+'~'
    url = 'http://localhost:8983/solr/latin/select?q=title:('+query+')&wt=python'
    connection = urlopen(url)
    response = eval(connection.read())

    results = []
    for document in response['response']['docs']:
        results.append(document['title'])
    return results