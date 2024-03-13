from scholarly import scholarly, ProxyGenerator
from combo import generate_combinations
import typer


app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")

@app.command()
def keyword_report(query: str, start_year: int, end_year: int, proxy: bool = False):
    keywords = generate_combinations(query)
    if proxy:
        # Set the proxy generator
        pg = ProxyGenerator()
        success = pg.FreeProxies()
        scholarly.use_proxy(pg)
    
    for kw in keywords:
        if start_year and end_year:
            search_query = scholarly.search_pubs(f'allintitle: {kw}', patents=False, citations=True, year_low=start_year, year_high=end_year)
        elif start_year:
            search_query = scholarly.search_pubs(f'allintitle: {kw}', patents=False, citations=True, year_low=start_year)
        elif end_year:
            search_query = scholarly.search_pubs(f'allintitle: {kw}', patents=False, citations=True, year_high=end_year)
        else:
            search_query = scholarly.search_pubs(f'allintitle: {kw}', patents=False, citations=True)
        
    print(f"{generate_combinations(query)}")


if __name__ == "__main__":
    app()