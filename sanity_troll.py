import json
import requests
  
# Load trolls.json
with open('trolls.json', 'r') as file:
      trolls = json.load(file)
  
updated = False
# Loop through each entry and verify name
for troll in trolls:
    response = requests.get(f"https://api.tibiadata.com/v4/character/{troll}")
    data = response.json()
    correct_name = data["character"]["character"]["name"]
    if troll != correct_name:
        print(f"Correcting name: {troll['name']} to {correct_name}")
        troll['name'] = correct_name
        updated = True

# Write the updated list back if changes were made
if updated:
    with open('trolls.json', 'w') as file:
        json.dump(trolls, file, indent=4)
    # Commit and push changes
    print("Committing and pushing the updated trolls list.")
    run: |
      git config --global user.name 'github-actions[bot]'
      git config --global user.email 'github-actions[bot]@users.noreply.github.com'
      git add trolls.json
      git commit -m "Sanity check corrections for trolls list"
      git push
else:
    print("No changes made.")
