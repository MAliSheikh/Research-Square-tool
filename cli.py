from scholarly import scholarly, ProxyGenerator
from combo import generate_combinations
import typer
from pprint import pprint
import json
import csv

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")

@app.command()
def keyword_report(query: str, start_year: int = None, end_year: int = None, proxy: bool = False):
    keywords = generate_combinations(query, min_words=2)
    pprint(keywords)
    if proxy:
        # Set the proxy generator
        pg = ProxyGenerator()
        success = pg.FreeProxies()
        scholarly.use_proxy(pg)
    
    data = {}
    
    for kw in keywords:
        try:
            if start_year and end_year:
                search_query = scholarly.search_pubs(f'allintitle: {kw}', patents=False, citations=True, year_low=start_year, year_high=end_year)
            elif start_year:
                search_query = scholarly.search_pubs(f'allintitle: {kw}', patents=False, citations=True, year_low=start_year)
            elif end_year:
                search_query = scholarly.search_pubs(f'allintitle: {kw}', patents=False, citations=True, year_high=end_year)
            else:
                search_query = scholarly.search_pubs(f'allintitle: {kw}', patents=False, citations=True)
            data[kw] = search_query.total_results
            print(f'{kw}: {search_query.total_results}')
        except:
            data[kw] = 'Error'
    print('Done!')
    # json into csv file
    with open('data.csv', 'w') as f:
        for key in data.keys():
            f.write("%s,%s\n"%(key,data[key]))
    print('Data saved to data.csv')
    pprint(data)


if __name__ == "__main__":
    app()