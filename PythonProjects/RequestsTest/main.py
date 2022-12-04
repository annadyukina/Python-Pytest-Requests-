import requests
import _json
token = '8e1bfe49cbdcdfcb6349eeefc59ebc43'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token},json={
    
    "name": "Squirtle",
    "photo": "https://e7.pngegg.com/pngimages/994/964/png-clipart-pokemon-squirtle-illustration-pokemon-mystery-dungeon-explorers-of-sky-pokemon-go-pikachu-squirtle-mug-pokemon-comics-vertebrate.png"
})

print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token},json={
    "pokemon_id": 1338,
    "name": "Сквиртл",
    "photo": "https://e7.pngegg.com/pngimages/994/964/png-clipart-pokemon-squirtle-illustration-pokemon-mystery-dungeon-explorers-of-sky-pokemon-go-pikachu-squirtle-mug-pokemon-comics-vertebrate.png"

})

print(response_put.text)

response_post = requests.post('https://pokemonbattle.me:5000//trainers/addPokebol', headers={'trainer_token' : token},json={
    "pokemon_id": "1338"})

print(response_post.text)

