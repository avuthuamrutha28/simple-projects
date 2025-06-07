import json
from collections import Counter, defaultdict


def load_data(filename='players.json'):
    with open(filename, 'r') as f:
        return json.load(f)


def basic_analysis(players):
    print("\n Hey Amrutha here is your ipl analysis")
    print("Total players:", len(players))
    avg_price = sum(p["price"] for p in players) / len(players)
    print("Average player price:", avg_price)

# Team Analysis
def team_analysis(players):
    team_counts = Counter(p['team'] for p in players)
    print("\nTeam Analysis")
    print("\nPlayers in each team:", dict(team_counts))
    most_players_team = team_counts.most_common(1)[0]
    print("Team with most players:", most_players_team)

    team_values = defaultdict(int)
    for p in players:
        team_values[p['team']] += p['price']
    print("Total team values:", dict(team_values))
    most_expensive_team = max(team_values.items(), key=lambda x: x[1])
    print("Most expensive team:", most_expensive_team)

# Role Analysis
def role_analysis(players):
    role_counts = Counter(p['role'] for p in players)
    print("\nRole Analysis:")
    print("\nPlayers in each role:", dict(role_counts))
    common_role = role_counts.most_common(1)[0]
    print("Most common role:", common_role)

    role_prices = defaultdict(list)
    for p in players:
        role_prices[p['role']].append(p['price'])

    avg_role_price = {role: sum(prices)/len(prices) for role, prices in role_prices.items()}
    print("Average price per role:", avg_role_price)

    most_expensive_role = max(avg_role_price.items(), key=lambda x: x[1])
    print("Most expensive role:", most_expensive_role)

# Country Analysis
def country_analysis(players):
    country_counts = Counter(p['country'] for p in players)
    print("\nCountry Analysis:")
    print("\nPlayers by country:", dict(country_counts))
    most_players_country = country_counts.most_common(1)[0]
    print("Country with most players:", most_players_country)

    country_prices = defaultdict(list)
    for p in players:
        country_prices[p['country']].append(p['price'])
    avg_country_price = {c: sum(prices)/len(prices) for c, prices in country_prices.items()}
    print("Average price by country:", avg_country_price)

    expensive_player_by_country = {}
    for p in players:
        if p['country'] not in expensive_player_by_country or p['price'] > expensive_player_by_country[p['country']]['price']:
            expensive_player_by_country[p['country']] = p
    print("Most expensive player by country:")
    for c, p in expensive_player_by_country.items():
        print(f"{c}: {p['name']} - ₹{p['price']}")

# Advanced Analysis
def advanced_analysis(players):
    print("\nAdvanced Analysis:")
    print("\nTop 5 most expensive players:")
    top_players = sorted(players, key=lambda x: x['price'], reverse=True)[:5]
    for p in top_players:
        print(f"{p['name']} ({p['team']}) - ₹{p['price']}")

    # By role
    print("\nTop 5 expensive players in each role:")
    roles = set(p['role'] for p in players)
    for role in roles:
        top = sorted([p for p in players if p['role'] == role], key=lambda x: x['price'], reverse=True)[:5]
        print(f"\n{role}:")
        for p in top:
            print(f"{p['name']} - ₹{p['price']}")

    # By team
    print("\nTop 5 expensive players in each team:")
    teams = set(p['team'] for p in players)
    for team in teams:
        top = sorted([p for p in players if p['team'] == team], key=lambda x: x['price'], reverse=True)[:5]
        print(f"\n{team}:")
        for p in top:
            print(f"{p['name']} - ₹{p['price']}")

    # By country
    print("\nTop 5 expensive players from each country:")
    countries = set(p['country'] for p in players)
    for country in countries:
        top = sorted([p for p in players if p['country'] == country], key=lambda x: x['price'], reverse=True)[:5]
        print(f"\n{country}:")
        for p in top:
            print(f"{p['name']} - ₹{p['price']}")

# Main
if __name__ == "__main__":
    players = load_data()
    basic_analysis(players)
    team_analysis(players)
    role_analysis(players)
    country_analysis(players)
    advanced_analysis(players)
