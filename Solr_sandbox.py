import pysolr

# Setup a Solr instance. The timeout is optional.
solr = pysolr.Solr('http://localhost:8983/solr/latin', timeout=10)


# Later, searching is easy. In the simple case, just a plain Lucene-style
# query is fine.
results = solr.search(' title:"gener*"')
# results = solr.search('generatio', search_handler="title")

# The ``Results`` object stores total results found, by default the top
# ten most relevant results and any additional data like
# facets/highlighting/spelling/etc.
print("Saw {0} result(s).".format(len(results)))
for o in results:
    print(o['title'])