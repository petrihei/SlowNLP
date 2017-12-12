from urllib.request import urlopen

def title_query(word):

    return "(title:" + word + ")"


def get_results(word):

    # look for the closest matches

    query = word+'~'
    url = 'http://localhost:8983/solr/latin/select?q=title:('+query+')&rows=1&wt=python'
    connection = urlopen(url)
    response = eval(connection.read())

    results = []
    for document in response['response']['docs']:
        results.append(document['title'])
    return results