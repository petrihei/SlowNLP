from urllib.request import urlopen

def title_query(word):

    return "(title:" + word + ")"



# how many documents found
# print(response['response']['numFound'], "documents found.")

# Print the name of each document.

def get_results(word):

    url_start = "http://localhost:8983/solr/latin/select?q="
    url_middle = title_query(word)
    url_end = "&wt=python"

    url = url_start + url_middle + url_end

    connection = urlopen(url)
    response = eval(connection.read())

    results = []
    for document in response['response']['docs']:
        results.append(document['title'])
    return results