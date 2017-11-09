import pysolr

# Setup a Solr instance. The timeout is optional.
solr = pysolr.Solr('http://localhost:8983/solr/techproducts', timeout=10)


# Later, searching is easy. In the simple case, just a plain Lucene-style
# query is fine.
results = solr.search('Maxtor DiamondMax')

# The ``Results`` object stores total results found, by default the top
# ten most relevant results and any additional data like
# facets/highlighting/spelling/etc.
print("Saw {0} result(s).".format(len(results)))