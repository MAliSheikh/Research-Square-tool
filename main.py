import json
from scholarly import scholarly, ProxyGenerator

# Set the proxy generator
# pg = ProxyGenerator()
# success = pg.FreeProxies()
# scholarly.use_proxy(pg)


query = 'supply chain'
start_year = 2019
# end_year = 2020


search_query = scholarly.search_pubs(f'allintitle: {query}', patents=False, citations=True, year_low=start_year)

search_query.total_results

# Retrieve the first result from the iterator
first_result = next(search_query)
scholarly.pprint(first_result)

# Retrieve all the details for the pbublication
publications = scholarly.fill(first_result)
scholarly.pprint(publications)

# Save the author dictionary into a JSON file
with open('publications.json', 'w') as json_file:
    json.dump(publications, json_file)

# Take a closer look at the first publication
# first_publication = author['publications'][0]
# first_publication_filled = scholarly.fill(first_publication)
# scholarly.pprint(first_publication_filled)

# Print the titles of the author's publications
# publication_titles = [pub['bib']['title'] for pub in author['publications']]
# print(publication_titles)

# Which papers cited that publication?
# citations = [citation['bib']['title'] for citation in scholarly.citedby(first_publication_filled)]
# print(citations)