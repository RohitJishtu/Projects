import random

ListofPlayers=[
   "Virat", "Phil", "Devdutt", "Rajat",
    "Liam", "Jitesh", "Tim", "Krunal",
    "Bhuvneshwar", "Josh", "Yash",
    "Sunil", "Quinton", "Venkatesh", "Ajinkya",
    "Rinku", "Ramandeep", "Andre", "Harshit",
    "Varun", "Spencer", "Chetan"]

# Given data
PossibleCaptain = ['Kohli', 'Phil', 'Sunil', 'Andre','Rajat','Varun']
PossibleViceCaptain = ['Kohli', 'Phil', 'Sunil', 'Andre','Rajat','Varun']
CombinationSize = 11  # Number of players in a team
NumTeams = 5  # Number of teams to generate

# List to store all generated teams
teams = []

# Function to generate a team with a specific captain and vice captain
def generate_team(captain, available_players):
    # Remove captain from available players
    remaining_players = [p for p in available_players if p != captain]
    
    # Choose vice captain from possible vice captains that are still available
    available_vice_captains = [p for p in remaining_players if p in PossibleViceCaptain]
    
    if not available_vice_captains:
        # If no designated vice captains are available, choose from remaining players
        vice_captain = random.choice(remaining_players)
    else:
        vice_captain = random.choice(available_vice_captains)
    
    # Remove vice captain from available players
    remaining_players = [p for p in remaining_players if p != vice_captain]
    
    # We need (CombinationSize - 2) more players to complete the team
    needed_players = CombinationSize - 2
    
    # Check if we have enough remaining players
    if len(remaining_players) < needed_players:
        return None  # Not enough players to form a team
    
    # Randomly select the remaining players
    other_players = random.sample(remaining_players, needed_players)
    
    # Complete team
    team = {
        'captain': captain,
        'vice_captain': vice_captain,
        'team': [captain, vice_captain] + other_players
    }
    
    return team

# Rotate through possible captains to create teams
captain_idx = 0
for _ in range(NumTeams):
    # Get the next captain in the rotation
    captain = PossibleCaptain[captain_idx % len(PossibleCaptain)]
    captain_idx += 1
    
    # Generate a team with this captain
    team = generate_team(captain, ListofPlayers)
    
    if team:
        teams.append(team)
    else:
        break  # Break if we can't form more teams

print(f"Generated {len(teams)} teams with rotating captains")

# Print the generated teams
for i, team in enumerate(teams):
    print(f"\nTeam {i+1}:")
    print(f"Captain: {team['captain']}")
    print(f"Vice Captain: {team['vice_captain']}")
    print(f"Team: {', '.join(team['team'])}")