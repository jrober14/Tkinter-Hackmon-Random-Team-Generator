#Hello. This is the code to my program, thank  you for viewing it
#This is here to convince you that this it not a virus
#Everything is red is a comment that I have added just for that purpose
#Thank you for downloading and reading my code, and I hope you don't think this is a virus
#Also "\n" mean the enter key
#The program my lag if you keep here, so I suggest you scroll down when you run the program


#importing lets me access code from libaries so I don't have to code very hard parts to a program for no reason

from tkinter import filedialog #Lets me access file directory, i.e. saving menu
from tkinter import ttk        #Lets me add tabs to my program
from tkinter import *          #Lets me add graphics to my program so it does not look like you are talking to the command prompt
import random                  #Should be obvious, but this lets my pick random numbers, and items from a list

#List of all Pokemon
p = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Venusaur-Mega', 'Charmander', 'Charmeleon', 'Charizard', 'Charizard-Mega-X', 'Charizard-Mega-Y', 'Squirtle', 'Wartortle', 'Blastoise', 'Blastoise-Mega', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Beedrill-Mega', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Pidgeot-Mega', 'Rattata', 'Rattata-Alola', 'Raticate', 'Raticate-Alola', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Raichu-Alola', 'Sandshrew', 'Sandshrew-Alola', 'Sandslash', 'Sandslash-Alola', 'Nidoran-F', 'Nidorina', 'Nidoqueen', 'Nidoran-M', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Vulpix-Alola', 'Ninetales', 'Ninetales-Alola', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Diglett-Alola', 'Dugtrio', 'Dugtrio-Alola', 'Meowth', 'Meowth-Alola', 'Persian', 'Persian-Alola', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Alakazam-Mega', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Geodude-Alola', 'Graveler', 'Graveler-Alola', 'Golem', 'Golem-Alola', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Slowbro-Mega', 'Magnemite', 'Magneton', "Farfetch'd", 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Grimer-Alola', 'Muk', 'Muk-Alola', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Gengar-Mega', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Exeggutor-Alola', 'Cubone', 'Marowak', 'Marowak-Alola', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Kangaskhan-Mega', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr. Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Pinsir-Mega', 'Tauros', 'Magikarp', 'Gyarados', 'Gyarados-Mega', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Aerodactyl-Mega', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mewtwo-Mega-X', 'Mewtwo-Mega-Y', 'Mew', 'Chikorita', 'Bayleef', 'Meganium', 'Cyndaquil', 'Quilava', 'Typhlosion', 'Totodile', 'Croconaw', 'Feraligatr', 'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Ledyba', 'Ledian', 'Spinarak', 'Ariados', 'Crobat', 'Chinchou', 'Lanturn', 'Pichu', 'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Natu', 'Xatu', 'Mareep', 'Flaaffy', 'Ampharos', 'Ampharos-Mega', 'Bellossom', 'Marill', 'Azumarill', 'Sudowoodo', 'Politoed', 'Hoppip', 'Skiploom', 'Jumpluff', 'Aipom', 'Sunkern', 'Sunflora', 'Yanma', 'Wooper', 'Quagsire', 'Espeon', 'Umbreon', 'Murkrow', 'Slowking', 'Misdreavus', 'Unown', 'Wobbuffet', 'Girafarig', 'Pineco', 'Forretress', 'Dunsparce', 'Gligar', 'Steelix', 'Steelix-Mega', 'Snubbull', 'Granbull', 'Qwilfish', 'Scizor', 'Scizor-Mega', 'Shuckle', 'Heracross', 'Heracross-Mega', 'Sneasel', 'Teddiursa', 'Ursaring', 'Slugma', 'Magcargo', 'Swinub', 'Piloswine', 'Corsola', 'Remoraid', 'Octillery', 'Delibird', 'Mantine', 'Skarmory', 'Houndour', 'Houndoom', 'Houndoom-Mega', 'Kingdra', 'Phanpy', 'Donphan', 'Porygon2', 'Stantler', 'Smeargle', 'Tyrogue', 'Hitmontop', 'Smoochum', 'Elekid', 'Magby', 'Miltank', 'Blissey', 'Raikou', 'Entei', 'Suicune', 'Larvitar', 'Pupitar', 'Tyranitar', 'Tyranitar-Mega', 'Lugia', 'Ho-Oh', 'Celebi', 'Treecko', 'Grovyle', 'Sceptile', 'Sceptile-Mega', 'Torchic', 'Combusken', 'Blaziken', 'Blaziken-Mega', 'Mudkip', 'Marshtomp', 'Swampert', 'Swampert-Mega', 'Poochyena', 'Mightyena', 'Zigzagoon', 'Linoone', 'Wurmple', 'Silcoon', 'Beautifly', 'Cascoon', 'Dustox', 'Lotad', 'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Taillow', 'Swellow', 'Wingull', 'Pelipper', 'Ralts', 'Kirlia', 'Gardevoir', 'Gardevoir-Mega', 'Surskit', 'Masquerain', 'Shroomish', 'Breloom', 'Slakoth', 'Vigoroth', 'Slaking', 'Nincada', 'Ninjask', 'Shedinja', 'Whismur', 'Loudred', 'Exploud', 'Makuhita', 'Hariyama', 'Azurill', 'Nosepass', 'Skitty', 'Delcatty', 'Sableye', 'Sableye-Mega', 'Mawile', 'Mawile-Mega', 'Aron', 'Lairon', 'Aggron', 'Aggron-Mega', 'Meditite', 'Medicham', 'Medicham-Mega', 'Electrike', 'Manectric', 'Manectric-Mega', 'Plusle', 'Minun', 'Volbeat', 'Illumise', 'Roselia', 'Gulpin', 'Swalot', 'Carvanha', 'Sharpedo', 'Sharpedo-Mega', 'Wailmer', 'Wailord', 'Numel', 'Camerupt', 'Camerupt-Mega', 'Torkoal', 'Spoink', 'Grumpig', 'Spinda', 'Trapinch', 'Vibrava', 'Flygon', 'Cacnea', 'Cacturne', 'Swablu', 'Altaria', 'Altaria-Mega', 'Zangoose', 'Seviper', 'Lunatone', 'Solrock', 'Barboach', 'Whiscash', 'Corphish', 'Crawdaunt', 'Baltoy', 'Claydol', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Feebas', 'Milotic', 'Castform', 'Kecleon', 'Shuppet', 'Banette', 'Banette-Mega', 'Duskull', 'Dusclops', 'Tropius', 'Chimecho', 'Absol', 'Absol-Mega', 'Wynaut', 'Snorunt', 'Glalie', 'Glalie-Mega', 'Spheal', 'Sealeo', 'Walrein', 'Clamperl', 'Huntail', 'Gorebyss', 'Relicanth', 'Luvdisc', 'Bagon', 'Shelgon', 'Salamence', 'Salamence-Mega', 'Beldum', 'Metang', 'Metagross', 'Metagross-Mega', 'Regirock', 'Regice', 'Registeel', 'Latias', 'Latias-Mega', 'Latios', 'Latios-Mega', 'Kyogre', 'Kyogre-Primal', 'Groudon', 'Groudon-Primal', 'Rayquaza', 'Rayquaza-Mega', 'Jirachi', 'Deoxys', 'Deoxys-Attack', 'Deoxys-Defense', 'Deoxys-Speed', 'Turtwig', 'Grotle', 'Torterra', 'Chimchar', 'Monferno', 'Infernape', 'Piplup', 'Prinplup', 'Empoleon', 'Starly', 'Staravia', 'Staraptor', 'Bidoof', 'Bibarel', 'Kricketot', 'Kricketune', 'Shinx', 'Luxio', 'Luxray', 'Budew', 'Roserade', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon', 'Burmy', 'Wormadam', 'Wormadam-Sandy', 'Wormadam-Trash', 'Mothim', 'Combee', 'Vespiquen', 'Pachirisu', 'Buizel', 'Floatzel', 'Cherubi', 'Cherrim', 'Shellos', 'Gastrodon', 'Ambipom', 'Drifloon', 'Drifblim', 'Buneary', 'Lopunny', 'Lopunny-Mega', 'Mismagius', 'Honchkrow', 'Glameow', 'Purugly', 'Chingling', 'Stunky', 'Skuntank', 'Bronzor', 'Bronzong', 'Bonsly', 'Mime Jr.', 'Happiny', 'Chatot', 'Spiritomb', 'Gible', 'Gabite', 'Garchomp', 'Garchomp-Mega', 'Munchlax', 'Riolu', 'Lucario', 'Lucario-Mega', 'Hippopotas', 'Hippowdon', 'Skorupi', 'Drapion', 'Croagunk', 'Toxicroak', 'Carnivine', 'Finneon', 'Lumineon', 'Mantyke', 'Snover', 'Abomasnow', 'Abomasnow-Mega', 'Weavile', 'Magnezone', 'Lickilicky', 'Rhyperior', 'Tangrowth', 'Electivire', 'Magmortar', 'Togekiss', 'Yanmega', 'Leafeon', 'Glaceon', 'Gliscor', 'Mamoswine', 'Porygon-Z', 'Gallade', 'Gallade-Mega', 'Probopass', 'Dusknoir', 'Froslass', 'Rotom', 'Rotom-Heat', 'Rotom-Wash', 'Rotom-Frost', 'Rotom-Fan', 'Rotom-Mow', 'Uxie', 'Mesprit', 'Azelf', 'Dialga', 'Palkia', 'Heatran', 'Regigigas', 'Giratina', 'Giratina-Origin', 'Cresselia', 'Phione', 'Manaphy', 'Darkrai', 'Shaymin', 'Shaymin-Sky', 'Arceus', 'Arceus-Bug', 'Arceus-Dark', 'Arceus-Dragon', 'Arceus-Electric', 'Arceus-Fairy', 'Arceus-Fighting', 'Arceus-Fire', 'Arceus-Flying', 'Arceus-Ghost', 'Arceus-Grass', 'Arceus-Ground', 'Arceus-Ice', 'Arceus-Poison', 'Arceus-Psychic', 'Arceus-Rock', 'Arceus-Steel', 'Arceus-Water', 'Victini', 'Snivy', 'Servine', 'Serperior', 'Tepig', 'Pignite', 'Emboar', 'Oshawott', 'Dewott', 'Samurott', 'Patrat', 'Watchog', 'Lillipup', 'Herdier', 'Stoutland', 'Purrloin', 'Liepard', 'Pansage', 'Simisage', 'Pansear', 'Simisear', 'Panpour', 'Simipour', 'Munna', 'Musharna', 'Pidove', 'Tranquill', 'Unfezant', 'Blitzle', 'Zebstrika', 'Roggenrola', 'Boldore', 'Gigalith', 'Woobat', 'Swoobat', 'Drilbur', 'Excadrill', 'Audino', 'Audino-Mega', 'Timburr', 'Gurdurr', 'Conkeldurr', 'Tympole', 'Palpitoad', 'Seismitoad', 'Throh', 'Sawk', 'Sewaddle', 'Swadloon', 'Leavanny', 'Venipede', 'Whirlipede', 'Scolipede', 'Cottonee', 'Whimsicott', 'Petilil', 'Lilligant', 'Basculin', 'Basculin-Blue-Striped', 'Sandile', 'Krokorok', 'Krookodile', 'Darumaka', 'Darmanitan', 'Maractus', 'Dwebble', 'Crustle', 'Scraggy', 'Scrafty', 'Sigilyph', 'Yamask', 'Cofagrigus', 'Tirtouga', 'Carracosta', 'Archen', 'Archeops', 'Trubbish', 'Garbodor', 'Zorua', 'Zoroark', 'Minccino', 'Cinccino', 'Gothita', 'Gothorita', 'Gothitelle', 'Solosis', 'Duosion', 'Reuniclus', 'Ducklett', 'Swanna', 'Vanillite', 'Vanillish', 'Vanilluxe', 'Deerling', 'Sawsbuck', 'Emolga', 'Karrablast', 'Escavalier', 'Foongus', 'Amoonguss', 'Frillish', 'Jellicent', 'Alomomola', 'Joltik', 'Galvantula', 'Ferroseed', 'Ferrothorn', 'Klink', 'Klang', 'Klinklang', 'Tynamo', 'Eelektrik', 'Eelektross', 'Elgyem', 'Beheeyem', 'Litwick', 'Lampent', 'Chandelure', 'Axew', 'Fraxure', 'Haxorus', 'Cubchoo', 'Beartic', 'Cryogonal', 'Shelmet', 'Accelgor', 'Stunfisk', 'Mienfoo', 'Mienshao', 'Druddigon', 'Golett', 'Golurk', 'Pawniard', 'Bisharp', 'Bouffalant', 'Rufflet', 'Braviary', 'Vullaby', 'Mandibuzz', 'Heatmor', 'Durant', 'Deino', 'Zweilous', 'Hydreigon', 'Larvesta', 'Volcarona', 'Cobalion', 'Terrakion', 'Virizion', 'Tornadus', 'Tornadus-Therian', 'Thundurus', 'Thundurus-Therian', 'Reshiram', 'Zekrom', 'Landorus', 'Landorus-Therian', 'Kyurem', 'Kyurem-Black', 'Kyurem-White', 'Keldeo', 'Meloetta', 'Genesect', 'Genesect-Douse', 'Genesect-Shock', 'Genesect-Burn', 'Genesect-Chill', 'Chespin', 'Quilladin', 'Chesnaught', 'Fennekin', 'Braixen', 'Delphox', 'Froakie', 'Frogadier', 'Greninja', 'Greninja-Ash', 'Bunnelby', 'Diggersby', 'Fletchling', 'Fletchinder', 'Talonflame', 'Scatterbug', 'Spewpa', 'Vivillon', 'Vivillon-Fancy', 'Vivillon-Pokeball', 'Litleo', 'Pyroar', 'Flabebe', 'Flabebe-Blue', 'Flabebe-Orange', 'Flabebe-White', 'Flabebe-Yellow', 'Floette', 'Floette-Blue', 'Floette-Orange', 'Floette-White', 'Floette-Yellow', 'Floette-Eternal', 'Florges', 'Florges-Blue', 'Florges-Orange', 'Florges-White', 'Florges-Yellow', 'Skiddo', 'Gogoat', 'Pancham', 'Pangoro', 'Furfrou', 'Espurr', 'Meowstic', 'Meowstic-F', 'Honedge', 'Doublade', 'Aegislash', 'Spritzee', 'Aromatisse', 'Swirlix', 'Slurpuff', 'Inkay', 'Malamar', 'Binacle', 'Barbaracle', 'Skrelp', 'Dragalge', 'Clauncher', 'Clawitzer', 'Helioptile', 'Heliolisk', 'Tyrunt', 'Tyrantrum', 'Amaura', 'Aurorus', 'Sylveon', 'Hawlucha', 'Dedenne', 'Carbink', 'Goomy', 'Sliggoo', 'Goodra', 'Klefki', 'Phantump', 'Trevenant', 'Pumpkaboo', 'Pumpkaboo-Small', 'Pumpkaboo-Large', 'Pumpkaboo-Super', 'Gourgeist', 'Gourgeist-Small', 'Gourgeist-Large', 'Gourgeist-Super', 'Bergmite', 'Avalugg', 'Noibat', 'Noivern', 'Xerneas', 'Yveltal', 'Zygarde', 'Zygarde-10%', 'Zygarde-Complete', 'Diancie', 'Diancie-Mega', 'Hoopa', 'Hoopa-Unbound', 'Volcanion', 'Rowlet', 'Dartrix', 'Decidueye', 'Litten', 'Torracat', 'Incineroar', 'Popplio', 'Brionne', 'Primarina', 'Pikipek', 'Trumbeak', 'Toucannon', 'Yungoos', 'Gumshoos', 'Grubbin', 'Charjabug', 'Vikavolt', 'Crabrawler', 'Crabominable', 'Oricorio', 'Oricorio-Pom-Pom', "Oricorio-Pa'u", 'Oricorio-Sensu', 'Cutiefly', 'Ribombee', 'Rockruff', 'Lycanroc', 'Lycanroc-Midnight', 'Lycanroc-Dusk', 'Wishiwashi', 'Mareanie', 'Toxapex', 'Mudbray', 'Mudsdale', 'Dewpider', 'Araquanid', 'Fomantis', 'Lurantis', 'Morelull', 'Shiinotic', 'Salandit', 'Salazzle', 'Stufful', 'Bewear', 'Bounsweet', 'Steenee', 'Tsareena', 'Comfey', 'Oranguru', 'Passimian', 'Wimpod', 'Golisopod', 'Sandygast', 'Palossand', 'Pyukumuku', 'Type: Null', 'Silvally', 'Silvally-Bug', 'Silvally-Dark', 'Silvally-Dragon', 'Silvally-Electric', 'Silvally-Fairy', 'Silvally-Fighting', 'Silvally-Fire', 'Silvally-Flying', 'Silvally-Ghost', 'Silvally-Grass', 'Silvally-Ground', 'Silvally-Ice', 'Silvally-Poison', 'Silvally-Psychic', 'Silvally-Rock', 'Silvally-Steel', 'Silvally-Water', 'Minior', 'Minior-Orange', 'Minior-Yellow', 'Minior-Green', 'Minior-Blue', 'Minior-Indigo', 'Minior-Violet', 'Minior-Meteor', 'Komala', 'Turtonator', 'Togedemaru', 'Mimikyu', 'Bruxish', 'Drampa', 'Dhelmise', 'Jangmo-o', 'Hakamo-o', 'Kommo-o', 'Tapu Koko', 'Tapu Lele', 'Tapu Bulu', 'Tapu Fini', 'Cosmog', 'Cosmoem', 'Solgaleo', 'Lunala', 'Nihilego', 'Buzzwole', 'Pheromosa', 'Xurkitree', 'Celesteela', 'Kartana', 'Guzzlord', 'Necrozma', 'Necrozma-Dusk-Mane', 'Necrozma-Dawn-Wings', 'Necrozma-Ultra', 'Magearna', 'Marshadow', 'Poipole', 'Naganadel', 'Stakataka', 'Blacephalon', 'Zeraora']
#List of Genders
gend = ["M", "F"]
#List of all moves
moves = ["Absorb", "Accelerock", "Acid", "Acid Armor", "Acid Spray", "Acrobatics", "Acupressure", "Aerial Ace", "Aeroblast", "After You", "Agility", "Air Cutter", "Air Slash", "Ally Switch", "Amnesia", "Anchor Shot", "Ancient Power", "Aqua Jet", "Aqua Ring", "Aqua Tail", "Arm Thrust", "Aromatherapy", "Aromatic Mist", "Assist", "Assurance", "Astonish", "Attack Order", "Attract", "Aura Sphere", "Aurora Beam", "Aurora Veil", "Autotomize", "Avalanche", "Baby-Doll Eyes", "Baneful Bunker", "Barrage", "Barrier", "Baton Pass", "Beak Blast", "Beat Up", "Belch", "Belly Drum", "Bestow", "Bide", "Bind", "Bite", "Blast Burn", "Blaze Kick", "Blizzard", "Block", "Blue Flare", "Body Slam", "Bolt Strike", "Bone Club", "Bone Rush", "Bonemerang", "Boomburst", "Bounce", "Brave Bird", "Brick Break", "Brine", "Brutal Swing", "Bubble", "Bubble Beam", "Bug Bite", "Bug Buzz", "Bulk Up", "Bulldoze", "Bullet Punch", "Bullet Seed", "Burn Up", "Calm Mind", "Camouflage", "Captivate", "Celebrate", "Charge", "Charge Beam", "Charm", "Chatter", "Chip Away", "Circle Throw", "Clamp", "Clanging Scales", "Clear Smog", "Close Combat", "Coil", "Comet Punch", "Confide", "Confuse Ray", "Confusion", "Constrict", "Conversion", "Conversion 2", "Copycat", "Core Enforcer", "Cosmic Power", "Cotton Guard", "Cotton Spore", "Counter", "Covet", "Crabhammer", "Crafty Shield", "Cross Chop", "Cross Poison", "Crunch", "Crush Claw", "Crush Grip", "Curse", "Cut", "Dark Pulse", "Dark Void", "Darkest Lariat", "Dazzling Gleam", "Defend Order", "Defense Curl", "Defog", "Destiny Bond", "Detect", "Diamond Storm", "Dig", "Disable", "Disarming Voice", "Discharge", "Dive", "Dizzy Punch", "Doom Desire", "Double-Edge", "Double Hit", "Double Kick", "Double Slap", "Double Team", "Draco Meteor", "Dragon Ascent", "Dragon Breath", "Dragon Claw", "Dragon Dance", "Dragon Hammer", "Dragon Pulse", "Dragon Rage", "Dragon Rush", "Dragon Tail", "Draining Kiss", "Drain Punch", "Dream Eater", "Drill Peck", "Drill Run", "Dual Chop", "Dynamic Punch", "Earth Power", "Earthquake", "Echoed Voice", "Eerie Impulse", "Egg Bomb", "Electric Terrain", "Electrify", "Electro Ball", "Electroweb", "Embargo", "Ember", "Encore", "Endeavor", "Endure", "Energy Ball", "Entrainment", "Eruption", "Explosion", "Extrasensory", "Extreme Speed", "Facade", "Feint Attack", "Fairy Lock", "Fairy Wind", "Fake Out", "Fake Tears", "False Swipe", "Feather Dance", "Feint", "Fell Stinger", "Fiery Dance", "Final Gambit", "Fire Blast", "Fire Fang", "Fire Lash", "Fire Pledge", "Fire Punch", "Fire Spin", "First Impression", "Fissure", "Flail", "Flame Burst", "Flame Charge", "Flame Wheel", "Flamethrower", "Flare Blitz", "Flash", "Flash Cannon", "Flatter", "Fleur Cannon", "Fling", "Floral Healing", "Flower Shield", "Fly", "Flying Press", "Focus Blast", "Focus Energy", "Focus Punch", "Follow Me", "Force Palm", "Foresight", "Forest's Curse", "Foul Play", "Freeze-Dry", "Freeze Shock", "Frenzy Plant", "Frost Breath", "Frustration", "Fury Attack", "Fury Cutter", "Fury Swipes", "Fusion Bolt", "Fusion Flare", "Future Sight", "Gastro Acid", "Gear Grind", "Gear Up", "Geomancy", "Giga Drain", "Giga Impact", "Glaciate", "Glare", "Grass Knot", "Grass Pledge", "Grass Whistle", "Grassy Terrain", "Gravity", "Growl", "Growth", "Grudge", "Guard Split", "Guard Swap", "Guillotine", "Gunk Shot", "Gust", "Gyro Ball", "Hail", "Hammer Arm", "Happy Hour", "Harden", "Haze", "Head Charge", "Head Smash", "Headbutt", "Heal Bell", "Heal Block", "Heal Order", "Heal Pulse", "Healing Wish", "Heart Stamp", "Heart Swap", "Heat Crash", "Heat Wave", "Heavy Slam", "Helping Hand", "Hex", "Hidden Power", "Hidden Power Bug", "Hidden Power Dark", "Hidden Power Dragon", "Hidden Power Electric", "Hidden Power Fighting", "Hidden Power Fire", "Hidden Power Flying", "Hidden Power Ghost", "Hidden Power Grass", "Hidden Power Ground", "Hidden Power Ice", "Hidden Power Poison", "Hidden Power Psychic", "Hidden Power Rock", "Hidden Power Steel", "Hidden Power Water", "High Horsepower", "High Jump Kick", "Hold Back", "Hold Hands", "Hone Claws", "Horn Attack", "Horn Drill", "Horn Leech", "Howl", "Hurricane", "Hydro Cannon", "Hydro Pump", "Hyper Beam", "Hyper Fang", "Hyperspace Fury", "Hyperspace Hole", "Hyper Voice", "Hypnosis", "Ice Ball", "Ice Beam", "Ice Burn", "Ice Fang", "Ice Hammer", "Ice Punch", "Ice Shard", "Icicle Crash", "Icicle Spear", "Icy Wind", "Imprison", "Incinerate", "Inferno", "Infestation", "Ingrain", "Instruct", "Ion Deluge", "Iron Defense", "Iron Head", "Iron Tail", "Judgment", "Jump Kick", "Karate Chop", "Kinesis", "King's Shield", "Knock Off", "Land's Wrath", "Laser Focus", "Last Resort", "Lava Plume", "Leaf Blade", "Leaf Storm", "Leaf Tornado", "Leafage", "Leech Life", "Leech Seed", "Leer", "Lick", "Light of Ruin", "Light Screen", "Liquidation", "Lock-On", "Lovely Kiss", "Low Kick", "Low Sweep", "Lucky Chant", "Lunar Dance", "Lunge", "Luster Purge", "Mach Punch", "Magic Coat", "Magic Room", "Magical Leaf", "Magma Storm", "Magnet Bomb", "Magnetic Flux", "Magnet Rise", "Magnitude", "Mat Block", "Me First", "Mean Look", "Meditate", "Mega Drain", "Mega Kick", "Mega Punch", "Megahorn", "Memento", "Metal Burst", "Metal Claw", "Metal Sound", "Meteor Mash", "Metronome", "Milk Drink", "Mimic", "Mind Blown", "Mind Reader", "Minimize", "Miracle Eye", "Mirror Coat", "Mirror Move", "Mirror Shot", "Mist", "Mist Ball", "Misty Terrain", "Moonblast", "Moongeist Beam", "Moonlight", "Morning Sun", "Mud-Slap", "Mud Bomb", "Mud Shot", "Mud Sport", "Muddy Water", "Multi-Attack", "Mystical Fire", "Nasty Plot", "Natural Gift", "Nature Power", "Nature's Madness", "Needle Arm", "Night Daze", "Night Shade", "Night Slash", "Nightmare", "Noble Roar", "Nuzzle", "Oblivion Wing", "Octazooka", "Odor Sleuth", "Ominous Wind", "Origin Pulse", "Outrage", "Overheat", "Pain Split", "Parabolic Charge", "Parting Shot", "Pay Day", "Payback", "Peck", "Perish Song", "Petal Blizzard", "Petal Dance", "Phantom Force", "Photon Geyser", "Pin Missile", "Plasma Fists", "Play Nice", "Play Rough", "Pluck", "Poison Fang", "Poison Gas", "Poison Jab", "Poison Powder", "Poison Sting", "Poison Tail", "Pollen Puff", "Pound", "Powder", "Powder Snow", "Power Gem", "Power Split", "Power Swap", "Power Trick", "Power Trip", "Power-Up Punch", "Power Whip", "Precipice Blades", "Present", "Prismatic Laser", "Protect", "Psybeam", "Psych Up", "Psychic", "Psychic Fangs", "Psychic Terrain", "Psycho Boost", "Psycho Cut", "Psycho Shift", "Psyshock", "Psystrike", "Psywave", "Punishment", "Purify", "Pursuit", "Quash", "Quick Attack", "Quick Guard", "Quiver Dance", "Rage", "Rage Powder", "Rain Dance", "Rapid Spin", "Razor Leaf", "Razor Shell", "Razor Wind", "Recover", "Recycle", "Reflect", "Reflect Type", "Refresh", "Relic Song", "Rest", "Retaliate", "Return", "Revelation Dance", "Revenge", "Reversal", "Roar", "Roar of Time", "Rock Blast", "Rock Climb", "Rock Polish", "Rock Slide", "Rock Smash", "Rock Throw", "Rock Tomb", "Rock Wrecker", "Role Play", "Rolling Kick", "Rollout", "Roost", "Rototiller", "Round", "Sacred Fire", "Sacred Sword", "Safeguard", "Sand Attack", "Sand Tomb", "Sandstorm", "Scald", "Scary Face", "Scratch", "Screech", "Searing Shot", "Secret Power", "Secret Sword", "Seed Bomb", "Seed Flare", "Seismic Toss", "Self-Destruct", "Shadow Ball", "Shadow Bone", "Shadow Claw", "Shadow Force", "Shadow Punch", "Shadow Sneak", "Sharpen", "Sheer Cold", "Shell Smash", "Shell Trap", "Shift Gear", "Shock Wave", "Shore Up", "Signal Beam", "Silver Wind", "Simple Beam", "Sing", "Sketch", "Skill Swap", "Skull Bash", "Sky Attack", "Sky Drop", "Sky Uppercut", "Slack Off", "Slam", "Slash", "Sleep Powder", "Sleep Talk", "Sludge", "Sludge Bomb", "Sludge Wave", "Smack Down", "Smart Strike", "Smelling Salts", "Smog", "Smokescreen", "Snarl", "Snatch", "Snore", "Spectral Thief", "Speed Swap", "Spiky Shield", "Spirit Shackle", "Soak", "Soft-Boiled", "Solar Beam", "Solar Blade", "Sonic Boom", "Spacial Rend", "Spark", "Sparkling Aria", "Spider Web", "Spike Cannon", "Spikes", "Spit Up", "Spite", "Splash", "Spore", "Spotlight", "Stealth Rock", "Steam Eruption", "Steel Wing", "Sticky Web", "Stockpile", "Stomp", "Stomping Tantrum", "Stone Edge", "Stored Power", "Storm Throw", "Steamroller", "Strength", "Strength Sap", "String Shot", "Struggle", "Struggle Bug", "Stun Spore", "Submission", "Substitute", "Sucker Punch", "Sunny Day", "Sunsteel Strike", "Super Fang", "Superpower", "Supersonic", "Surf", "Swagger", "Swallow", "Sweet Kiss", "Sweet Scent", "Swift", "Switcheroo", "Swords Dance", "Synchronoise", "Synthesis", "Tackle", "Tail Glow", "Tail Slap", "Tail Whip", "Tailwind", "Take Down", "Taunt", "Tearful Look", "Techno Blast", "Teeter Dance", "Telekinesis", "Teleport", "Thief", "Thousand Arrows", "Thousand Waves", "Thrash", "Throat Chop", "Thunder", "Thunder Fang", "Thunder Punch", "Thunder Shock", "Thunder Wave", "Thunderbolt", "Tickle", "Topsy-Turvy", "Torment", "Toxic", "Toxic Spikes", "Toxic Thread", "Transform", "Tri Attack", "Trick", "Trick-or-Treat", "Trick Room", "Triple Kick", "Trop Kick", "Trump Card", "Twineedle", "Twister", "U-turn", "Uproar", "V-create", "Vacuum Wave", "Venom Drench", "Venoshock", "Vice Grip", "Vine Whip", "Vital Throw", "Volt Switch", "Volt Tackle", "Wake-Up Slap", "Water Gun", "Water Pledge", "Water Pulse", "Water Sport", "Water Spout", "Waterfall", "Water Shuriken", "Weather Ball", "Whirlpool", "Whirlwind", "Wide Guard", "Wild Charge", "Will-O-Wisp", "Wing Attack", "Wish", "Withdraw", "Wonder Room", "Wood Hammer", "Work Up", "Worry Seed", "Wrap", "Wring Out", "X-Scissor", "Yawn", "Zap Cannon", "Zen Headbutt", "Zing Zap"]
#List of all natures
natures = ['Hardy', 'Lonely', 'Brave', 'Adamant', 'Naughty', 'Bold', 'Docile', 'Relaxed', 'Impish', 'Lax', 'Timid', 'Hasty', 'Serious', 'Jolly', 'Naive', 'Modest', 'Mild', 'Quiet', 'Bashful', 'Rash', 'Calm', 'Gentle', 'Sassy', 'Careful', 'Quirky']
#List of shiny options
shinys = ["Yes", "No"]
#List of all items
items = ["Abomasite", "Absolite", "Absorb Bulb", "Adamant Orb", "Adrenaline Orb", "Aerodactylite", "Aggronite", "Aguav Berry", "Air Balloon", "Alakazite", "Aloraichium Z", "Altarianite", "Ampharosite", "Apicot Berry", "Armor Fossil", "Aspear Berry", "Assault Vest", "Audinite", "Babiri Berry", "Banettite", "Beast Ball", "Beedrillite", "Belue Berry", "Berry Juice", "Big Root", "Binding Band", "Black Belt", "Black Sludge", "Black Glasses", "Blastoisinite", "Blazikenite", "Blue Orb", "Bluk Berry", "BrightPowder", "Bug Memory", "Buginium Z", "Burn Drive", "Cameruptite", "Cell Battery", "Charcoal", "Charizardite X", "Charizardite Y", "Charti Berry", "Cheri Berry", "Cherish Ball", "Chesto Berry", "Chilan Berry", "Chill Drive", "Choice Band", "Choice Scarf", "Choice Specs", "Chople Berry", "Claw Fossil", "Coba Berry", "Colbur Berry", "Cornn Berry", "Cover Fossil", "Custap Berry", "Damp Rock", "Dark Memory", "Darkinium Z", "Decidium Z", "Deep Sea Scale", "Deep Sea Tooth", "Destiny Knot", "Diancite", "Dive Ball", "Dome Fossil", "Douse Drive", "Draco Plate", "Dragon Fang", "Dragon Memory", "Dragonium Z", "Dread Plate", "Dream Ball", "Durin Berry", "Dusk Ball", "Earth Plate", "Eevium Z", "Eject Button", "Electirizer", "Electric Memory", "Electric Seed", "Electrium Z", "Energy Powder", "Enigma Berry", "Eviolite", "Expert Belt", "Fairium Z", "Fairy Memory", "Fast Ball", "Fighting Memory", "Fightinium Z", "Figy Berry", "Fire Memory", "Firium Z", "Fist Plate", "Flame Orb", "Flame Plate", "Float Stone", "Flying Memory", "Flyinium Z", "Focus Band", "Focus Sash", "Friend Ball", "Full Incense", "Galladite", "Ganlon Berry", "Garchompite", "Gardevoirite", "Gengarite", "Ghost Memory", "Ghostium Z", "Glalitite", "Grass ", "Grass Memory", "Grassium Z", "Grassy Seed", "Great Ball", "Grepa Berry", "Grip Claw", "Griseous Orb", "Ground Memory", "Groundium Z", "Gyaradosite", "Haban Berry", "Hard Stone", "Heal Ball", "Heat Rock", "Heavy Ball", "Helix Fossil", "Heracronite", "Hondew Berry", "Houndoominite", "Iapapa Berry", "Ice Memory", "Icicle Plate", "Icium Z", "Icy Rock", "Incinium Z", "Insect Plate", "Iron Ball", "Iron Plate", "Jaboca Berry", "Kasib Berry", "Kebia Berry", "Kee Berry", "Kelpsy Berry", "Kangaskhanite", "King's Rock", "Kommonium Z", "Lagging Tail", "Lansat Berry", "Latiasite", "Latiosite", "Lax Incense", "Leftovers", "Leppa Berry", "Level Ball", "Liechi Berry", "Life Orb", "Light Ball", "Light Clay", "Lopunnite", "Love Ball", "Lucarionite", "Lucky Punch", "Lum Berry", "Luminous Moss", "Lunalium Z", "Lure Ball", "Lustrous Orb", "Luxury Ball", "Lycanium Z", "Macho Brace", "Magnet", "Mago Berry", "Magost Berry", "Mail", "Manectite", "Maranga Berry", "Marshadium Z", "Master Ball", "Mawilite", "Meadow Plate", "Medichamite", "Mental Herb", "Metagrossite", "Metal Coat", "Metal Powder", "Metronome", "Mewnium Z", "Mewtwonite X", "Mewtwonite Y", "Micle Berry", "Mimikium Z", "Mind Plate", "Miracle Seed", "Misty Seed", "Moon Ball", "Muscle Band", "Mystic Water", "Nanab Berry", "Nest Ball", "Net Ball", "Never-Melt Ice", "Nomel Berry", "Normalium Z", "Occa Berry", "Odd Incense", "Old Amber", "Oran Berry", "Pamtre Berry", "Park Ball", "Passho Berry", "Payapa Berry", "Pecha Berry", "Persim Berry", "Petaya Berry", "Pidgeotite", "Pikanium Z", "Pikashunium Z", "Pinap Berry", "Pinsirite", "Pixie Plate", "Plume Fossil", "Poison Barb", "Poison Memory", "Poisonium Z", "Poke Ball", "Pomeg Berry", "Power Anklet", "Power Band", "Power Belt", "Power Bracer", "Power Herb", "Power Lens", "Power Weight", "Premier Ball", "Primarium Z", "Protective Pads", "Psychic Memory", "Psychic Seed", "Psychium Z", "Qualot Berry", "Quick Ball", "Quick Claw", "Quick Powder", "Rabuta Berry", "Rare Bone", "Rawst Berry", "Razor Claw", "Razor Fang", "Razz Berry", "Red Card", "Red Orb", "Repeat Ball", "Rindo Berry", "Ring Target", "Rock Incense", "Rock Memory", "Rockium Z", "Rocky Helmet", "Root Fossil", "Rose Incense", "Roseli Berry", "Rowap Berry", "Sablenite", "Safari Ball", "Safety Goggles", "Salac Berry", "Salamencite", "Sceptilite", "Scizorite", "Scope Lens", "Sea Incense", "Sharp Beak", "Sharpedonite", "Shed Shell", "Shell Bell", "Shock Drive", "Shuca Berry", "Silk Scarf", "SilverPowder", "Sitrus Berry", "Skull Fossil", "Sky Plate", "Slowbronite", "Smooth Rock", "Snorlium Z", "Snowball", "Soft Sand", "Solganium Z", "Soul Dew", "Spell Tag", "Spelon Berry", "Splash Plate", "Spooky Plate", "Sport Ball", "Starf Berry", "Steelixite", "Steel Memory", "Steelium Z", "Stick", "Sticky Barb", "Stone Plate", "Swampertite", "Tamato Berry", "Tanga Berry", "Tapunium Z", "Terrain Extender", "Thick Club", "Timer Ball", "Toxic Orb", "Toxic Plate", "Twisted Spoon", "Tyranitarite", "Ultra Ball", "Ultranecrozium Z", "Venusaurite", "Wacan Berry", "Water Memory", "Waterium Z", "Watmel Berry", "Wave Incense", "Weakness Policy", "Wepear Berry", "White Herb", "Wide Lens", "Wiki Berry", "Wise Glasses", "Yache Berry", "Zap Plate", "Zoom Lens", 'Dawn Stone', 'Dragon Scale', 'Dubious Disc', 'Dusk Stone', 'Fire Stone', 'Ice Stone', 'Jaw Fossil', 'Leaf Stone', 'Magmarizer', 'Moon Stone', 'Oval Stone', 'Prism Scale', 'Protector', 'Reaper Cloth', 'Sachet', 'Sail Fossil', 'Shiny Stone', 'Sun Stone', 'Thunder Stone', 'Up-Grade', 'Water Stone', 'Whipped Dream']
#List of all abilities
abils = ["Neuroforce", "Adaptability", "Aftermath", "Aerilate", "Air Lock", "Analytic", "Anger Point", "Anticipation", "Arena Trap", "Aroma Veil", "Aura Break", "Bad Dreams", "Battery", "Battle Armor", "Battle Bond", "Beast Boost", "Berserk", "Big Pecks", "Blaze", "Bulletproof", "Cheek Pouch", "Chlorophyll", "Clear Body", "Cloud Nine", "Color Change", "Comatose", "Competitive", "Compound Eyes", "Contrary", "Corrosion", "Cursed Body", "Cute Charm", "Damp", "Dancer", "Dark Aura", "Dazzling", "Defeatist", "Defiant", "Delta Stream", "Desolate Land", "Disguise", "Download", "Drizzle", "Drought", "Dry Skin", "Early Bird", "Effect Spore", "Electric Surge", "Emergency Exit", "Fairy Aura", "Filter", "Flame Body", "Flare Boost", "Flash Fire", "Flower Gift", "Flower Veil", "Fluffy", "Forecast", "Forewarn", "Friend Guard", "Frisk", "Full Metal Body", "Fur Coat", "Gale Wings", "Galvanize", "Gluttony", "Gooey", "Grass Pelt", "Grassy Surge", "Guts", "Harvest", "Healer", "Heatproof", "Heavy Metal", "Honey Gather", "Huge Power", "Hustle", "Hydration", "Hyper Cutter", "Ice Body", "Illuminate", "Illusion", "Immunity", "Imposter", "Infiltrator", "Innards Out", "Inner Focus", "Insomnia", "Intimidate", "Iron Barbs", "Iron Fist", "Justified", "Keen Eye", "Klutz", "Leaf Guard", "Levitate", "Light Metal", "Lightning Rod", "Limber", "Liquid Ooze", "Liquid Voice", "Long Reach", "Magic Bounce", "Magic Guard", "Magician", "Magma Armor", "Magnet Pull", "Marvel Scale", "Mega Launcher", "Merciless", "Minus", "Misty Surge", "Mold Breaker", "Moody", "Motor Drive", "Moxie", "Multiscale", "Multitype", "Mummy", "Natural Cure", "No Guard", "Normalize", "Oblivious", "Overcoat", "Overgrow", "Own Tempo", "Parental Bond", "Pickup", "Pickpocket", "Pixilate", "Plus", "Poison Heal", "Poison Point", "Poison Touch", "Power Construct", "Power of Alchemy", "Prankster", "Pressure", "Primordial Sea", "Prism Armor", "Protean", "Psychic Surge", "Pure Power", "Queenly Majesty", "Quick Feet", "Rain Dish", "Rattled", "Receiver", "Reckless", "Refrigerate", "Regenerator", "Rivalry", "RKS System", "Rock Head", "Rough Skin", "Run Away", "Sand Force", "Sand Rush", "Sand Stream", "Sand Veil", "Sap Sipper", "Schooling", "Scrappy", "Serene Grace", "Shadow Shield", "Shadow Tag", "Shed Skin", "Sheer Force", "Shell Armor", "Shield Dust", "Shields Down", "Simple", "Skill Link", "Slow Start", "Slush Rush", "Sniper", "Snow Cloak", "Snow Warning", "Solar Power", "Solid Rock", "Soul-Heart", "Soundproof", "Speed Boost", "Stakeout", "Stall", "Stamina", "Stance Change", "Static", "Steadfast", "Steelworker", "Stench", "Sticky Hold", "Storm Drain", "Strong Jaw", "Sturdy", "Suction Cups", "Super Luck", "Surge Surfer", "Swarm", "Sweet Veil", "Swift Swim", "Symbiosis", "Synchronize", "Tangled Feet", "Tangling Hair", "Technician", "Telepathy", "Teravolt", "Thick Fat", "Tinted Lens", "Torrent", "Toxic Boost", "Tough Claws", "Trace", "Triage", "Truant", "Turboblaze", "Unaware", "Unburden", "Unnerve", "Victory Star", "Vital Spirit", "Volt Absorb", "Water Absorb", "Water Bubble", "Water Compaction", "Water Veil", "Weak Armor", "White Smoke", "Wimp Out", "Wonder Guard", "Wonder Skin", "Zen Mode"]

#List of Pokemon in each type for Mono-type
Grassm = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Venusaur-Mega', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Exeggcute', 'Exeggutor', 'Exeggutor-Alola', 'Tangela', 'Chikorita', 'Bayleef', 'Meganium', 'Bellossom', 'Hoppip', 'Skiploom', 'Jumpluff', 'Sunkern', 'Sunflora', 'Celebi', 'Treecko', 'Grovyle', 'Sceptile', 'Sceptile-Mega', 'Lotad', 'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Shroomish', 'Breloom', 'Roselia', 'Cacnea', 'Cacturne', 'Lileep', 'Cradily', 'Tropius', 'Turtwig', 'Grotle', 'Torterra', 'Budew', 'Roserade', 'Wormadam', 'Cherubi', 'Cherrim', 'Carnivine', 'Snover', 'Abomasnow', 'Abomasnow-Mega', 'Tangrowth', 'Leafeon', 'Rotom-Mow', 'Shaymin', 'Shaymin-Sky', 'Arceus-Grass', 'Snivy', 'Servine', 'Serperior', 'Pansage', 'Simisage', 'Sewaddle', 'Swadloon', 'Leavanny', 'Cottonee', 'Whimsicott', 'Petilil', 'Lilligant', 'Maractus', 'Deerling', 'Sawsbuck', 'Foongus', 'Amoonguss', 'Ferroseed', 'Ferrothorn', 'Virizion', 'Chespin', 'Quilladin', 'Chesnaught', 'Skiddo', 'Gogoat', 'Phantump', 'Trevenant', 'Pumpkaboo', 'Pumpkaboo-Small', 'Pumpkaboo-Large', 'Pumpkaboo-Super', 'Gourgeist', 'Gourgeist-Small', 'Gourgeist-Large', 'Gourgeist-Super', 'Rowlet', 'Dartrix', 'Decidueye', 'Fomantis', 'Lurantis', 'Morelull', 'Shiinotic', 'Bounsweet', 'Steenee', 'Tsareena', 'Silvally-Grass', 'Dhelmise', 'Tapu Bulu', 'Kartana']
Firem = ['Charmander', 'Charmeleon', 'Charizard', 'Charizard-Mega-X', 'Charizard-Mega-Y', 'Vulpix', 'Ninetales', 'Growlithe', 'Arcanine', 'Ponyta', 'Rapidash', 'Marowak-Alola', 'Magmar', 'Flareon', 'Moltres', 'Cyndaquil', 'Quilava', 'Typhlosion', 'Slugma', 'Magcargo', 'Houndour', 'Houndoom', 'Houndoom-Mega', 'Magby', 'Entei', 'Ho-Oh', 'Torchic', 'Combusken', 'Blaziken', 'Blaziken-Mega', 'Numel', 'Camerupt', 'Camerupt-Mega', 'Torkoal', 'Groudon-Primal', 'Chimchar', 'Monferno', 'Infernape', 'Magmortar', 'Rotom-Heat', 'Heatran', 'Arceus-Fire', 'Victini', 'Tepig', 'Pignite', 'Emboar', 'Pansear', 'Simisear', 'Darumaka', 'Darmanitan', 'Litwick', 'Lampent', 'Chandelure', 'Heatmor', 'Larvesta', 'Volcarona', 'Reshiram', 'Fennekin', 'Braixen', 'Delphox', 'Fletchinder', 'Talonflame', 'Litleo', 'Pyroar', 'Volcanion', 'Litten', 'Torracat', 'Incineroar', 'Oricorio', 'Salandit', 'Salazzle', 'Silvally-Fire', 'Turtonator', 'Blacephalon']
Waterm = ['Squirtle', 'Wartortle', 'Blastoise', 'Blastoise-Mega', 'Psyduck', 'Golduck', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Tentacool', 'Tentacruel', 'Slowpoke', 'Slowbro', 'Slowbro-Mega', 'Seel', 'Dewgong', 'Shellder', 'Cloyster', 'Krabby', 'Kingler', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Magikarp', 'Gyarados', 'Gyarados-Mega', 'Lapras', 'Vaporeon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Totodile', 'Croconaw', 'Feraligatr', 'Chinchou', 'Lanturn', 'Marill', 'Azumarill', 'Politoed', 'Wooper', 'Quagsire', 'Slowking', 'Qwilfish', 'Corsola', 'Remoraid', 'Octillery', 'Mantine', 'Kingdra', 'Suicune', 'Mudkip', 'Marshtomp', 'Swampert', 'Swampert-Mega', 'Lotad', 'Lombre', 'Ludicolo', 'Wingull', 'Pelipper', 'Surskit', 'Carvanha', 'Sharpedo', 'Sharpedo-Mega', 'Wailmer', 'Wailord', 'Barboach', 'Whiscash', 'Corphish', 'Crawdaunt', 'Feebas', 'Milotic', 'Spheal', 'Sealeo', 'Walrein', 'Clamperl', 'Huntail', 'Gorebyss', 'Relicanth', 'Luvdisc', 'Kyogre', 'Kyogre-Primal', 'Piplup', 'Prinplup', 'Empoleon', 'Bibarel', 'Buizel', 'Floatzel', 'Shellos', 'Gastrodon', 'Finneon', 'Lumineon', 'Mantyke', 'Rotom-Wash', 'Palkia', 'Phione', 'Manaphy', 'Arceus-Water', 'Oshawott', 'Dewott', 'Samurott', 'Panpour', 'Simipour', 'Tympole', 'Palpitoad', 'Seismitoad', 'Basculin', 'Basculin-Blue-Striped', 'Tirtouga', 'Carracosta', 'Ducklett', 'Swanna', 'Frillish', 'Jellicent', 'Alomomola', 'Keldeo', 'Froakie', 'Frogadier', 'Greninja', 'Greninja-Ash', 'Binacle', 'Barbaracle', 'Skrelp', 'Clauncher', 'Clawitzer', 'Volcanion', 'Popplio', 'Brionne', 'Primarina', 'Wishiwashi', 'Mareanie', 'Toxapex', 'Dewpider', 'Araquanid', 'Wimpod', 'Golisopod', 'Pyukumuku', 'Silvally-Water', 'Bruxish', 'Tapu Fini']
Bugm = ['Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Beedrill-Mega', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Scyther', 'Pinsir', 'Pinsir-Mega', 'Ledyba', 'Ledian', 'Spinarak', 'Ariados', 'Yanma', 'Pineco', 'Forretress', 'Scizor', 'Scizor-Mega', 'Shuckle', 'Heracross', 'Heracross-Mega', 'Wurmple', 'Silcoon', 'Beautifly', 'Cascoon', 'Dustox', 'Surskit', 'Masquerain', 'Nincada', 'Ninjask', 'Shedinja', 'Volbeat', 'Illumise', 'Anorith', 'Armaldo', 'Kricketot', 'Kricketune', 'Burmy', 'Wormadam', 'Wormadam-Sandy', 'Wormadam-Trash', 'Mothim', 'Combee', 'Vespiquen', 'Skorupi', 'Yanmega', 'Arceus-Bug', 'Sewaddle', 'Swadloon', 'Leavanny', 'Venipede', 'Whirlipede', 'Scolipede', 'Dwebble', 'Crustle', 'Karrablast', 'Escavalier', 'Joltik', 'Galvantula', 'Shelmet', 'Accelgor', 'Durant', 'Larvesta', 'Volcarona', 'Genesect', 'Genesect-Douse', 'Genesect-Shock', 'Genesect-Burn', 'Genesect-Chill', 'Scatterbug', 'Spewpa', 'Vivillon', 'Vivillon-Fancy', 'Vivillon-Pokeball', 'Grubbin', 'Charjabug', 'Vikavolt', 'Cutiefly', 'Ribombee', 'Dewpider', 'Araquanid', 'Wimpod', 'Golisopod', 'Silvally-Bug', 'Buzzwole', 'Pheromosa']
Normalm = ['Pidgey', 'Pidgeotto', 'Pidgeot', 'Pidgeot-Mega', 'Rattata', 'Rattata-Alola', 'Raticate', 'Raticate-Alola', 'Spearow', 'Fearow', 'Jigglypuff', 'Wigglytuff', 'Meowth', 'Persian', "Farfetch\\'d", 'Doduo', 'Dodrio', 'Lickitung', 'Chansey', 'Kangaskhan', 'Kangaskhan-Mega', 'Tauros', 'Ditto', 'Eevee', 'Porygon', 'Snorlax', 'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Igglybuff', 'Aipom', 'Girafarig', 'Dunsparce', 'Teddiursa', 'Ursaring', 'Porygon2', 'Stantler', 'Smeargle', 'Miltank', 'Blissey', 'Zigzagoon', 'Linoone', 'Taillow', 'Swellow', 'Slakoth', 'Vigoroth', 'Slaking', 'Whismur', 'Loudred', 'Exploud', 'Azurill', 'Skitty', 'Delcatty', 'Spinda', 'Swablu', 'Zangoose', 'Castform', 'Kecleon', 'Starly', 'Staravia', 'Staraptor', 'Bidoof', 'Bibarel', 'Ambipom', 'Buneary', 'Lopunny', 'Lopunny-Mega', 'Glameow', 'Purugly', 'Happiny', 'Chatot', 'Munchlax', 'Lickilicky', 'Porygon-Z', 'Regigigas', 'Arceus', 'Patrat', 'Watchog', 'Lillipup', 'Herdier', 'Stoutland', 'Pidove', 'Tranquill', 'Unfezant', 'Audino', 'Audino-Mega', 'Minccino', 'Cinccino', 'Deerling', 'Sawsbuck', 'Bouffalant', 'Rufflet', 'Braviary', 'Meloetta', 'Bunnelby', 'Diggersby', 'Fletchling', 'Litleo', 'Pyroar', 'Furfrou', 'Helioptile', 'Heliolisk', 'Pikipek', 'Trumbeak', 'Toucannon', 'Yungoos', 'Gumshoos', 'Stufful', 'Bewear', 'Oranguru', 'Type: Null', 'Silvally', 'Komala', 'Drampa']
Darkm = ['Rattata-Alola', 'Raticate-Alola', 'Meowth-Alola', 'Persian-Alola', 'Grimer-Alola', 'Muk-Alola', 'Gyarados-Mega', 'Umbreon', 'Murkrow', 'Sneasel', 'Houndour', 'Houndoom', 'Houndoom-Mega', 'Tyranitar', 'Tyranitar-Mega', 'Poochyena', 'Mightyena', 'Nuzleaf', 'Shiftry', 'Sableye', 'Sableye-Mega', 'Carvanha', 'Sharpedo', 'Sharpedo-Mega', 'Cacturne', 'Crawdaunt', 'Absol', 'Absol-Mega', 'Honchkrow', 'Stunky', 'Skuntank', 'Spiritomb', 'Drapion', 'Weavile', 'Darkrai', 'Arceus-Dark', 'Purrloin', 'Liepard', 'Sandile', 'Krokorok', 'Krookodile', 'Scraggy', 'Scrafty', 'Zorua', 'Zoroark', 'Pawniard', 'Bisharp', 'Vullaby', 'Mandibuzz', 'Deino', 'Zweilous', 'Hydreigon', 'Greninja', 'Greninja-Ash', 'Pangoro', 'Inkay', 'Malamar', 'Yveltal', 'Hoopa-Unbound', 'Incineroar', 'Silvally-Dark', 'Guzzlord']
Poisonm = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Venusaur-Mega', 'Weedle', 'Kakuna', 'Beedrill', 'Beedrill-Mega', 'Ekans', 'Arbok', 'Nidoran-F', 'Nidorina', 'Nidoqueen', 'Nidoran-M', 'Nidorino', 'Nidoking', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Venonat', 'Venomoth', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Grimer', 'Grimer-Alola', 'Muk', 'Muk-Alola', 'Gastly', 'Haunter', 'Gengar', 'Gengar-Mega', 'Koffing', 'Weezing', 'Spinarak', 'Ariados', 'Crobat', 'Qwilfish', 'Dustox', 'Roselia', 'Gulpin', 'Swalot', 'Seviper', 'Budew', 'Roserade', 'Stunky', 'Skuntank', 'Skorupi', 'Drapion', 'Croagunk', 'Toxicroak', 'Arceus-Poison', 'Venipede', 'Whirlipede', 'Scolipede', 'Trubbish', 'Garbodor', 'Foongus', 'Amoonguss', 'Skrelp', 'Dragalge', 'Mareanie', 'Toxapex', 'Salandit', 'Salazzle', 'Silvally-Poison', 'Nihilego', 'Poipole', 'Naganadel']
Electricm = ['Pikachu', 'Raichu', 'Raichu-Alola', 'Geodude-Alola', 'Graveler-Alola', 'Golem-Alola', 'Magnemite', 'Magneton', 'Voltorb', 'Electrode', 'Electabuzz', 'Jolteon', 'Zapdos', 'Chinchou', 'Lanturn', 'Pichu', 'Mareep', 'Flaaffy', 'Ampharos', 'Ampharos-Mega', 'Elekid', 'Raikou', 'Electrike', 'Manectric', 'Manectric-Mega', 'Plusle', 'Minun', 'Shinx', 'Luxio', 'Luxray', 'Pachirisu', 'Magnezone', 'Electivire', 'Rotom', 'Rotom-Heat', 'Rotom-Wash', 'Rotom-Frost', 'Rotom-Fan', 'Rotom-Mow', 'Arceus-Electric', 'Blitzle', 'Zebstrika', 'Emolga', 'Joltik', 'Galvantula', 'Tynamo', 'Eelektrik', 'Eelektross', 'Stunfisk', 'Thundurus', 'Thundurus-Therian', 'Zekrom', 'Helioptile', 'Heliolisk', 'Dedenne', 'Charjabug', 'Vikavolt', 'Oricorio-Pom-Pom', 'Silvally-Electric', 'Togedemaru', 'Tapu Koko', 'Xurkitree', 'Zeraora']
Groundm = ['Sandshrew', 'Sandslash', 'Nidoqueen', 'Nidoking', 'Diglett', 'Diglett-Alola', 'Dugtrio', 'Dugtrio-Alola', 'Geodude', 'Graveler', 'Golem', 'Onix', 'Cubone', 'Marowak', 'Rhyhorn', 'Rhydon', 'Wooper', 'Quagsire', 'Gligar', 'Steelix', 'Steelix-Mega', 'Swinub', 'Piloswine', 'Phanpy', 'Donphan', 'Larvitar', 'Pupitar', 'Marshtomp', 'Swampert', 'Swampert-Mega', 'Nincada', 'Numel', 'Camerupt', 'Camerupt-Mega', 'Trapinch', 'Vibrava', 'Flygon', 'Barboach', 'Whiscash', 'Baltoy', 'Claydol', 'Groudon', 'Groudon-Primal', 'Torterra', 'Wormadam-Sandy', 'Gastrodon', 'Gible', 'Gabite', 'Garchomp', 'Garchomp-Mega', 'Hippopotas', 'Hippowdon', 'Rhyperior', 'Gliscor', 'Mamoswine', 'Arceus-Ground', 'Drilbur', 'Excadrill', 'Palpitoad', 'Seismitoad', 'Sandile', 'Krokorok', 'Krookodile', 'Stunfisk', 'Golett', 'Golurk', 'Landorus', 'Landorus-Therian', 'Diggersby', 'Zygarde', 'Zygarde-10%', 'Zygarde-Complete', 'Mudbray', 'Mudsdale', 'Sandygast', 'Palossand', 'Silvally-Ground']
Icem = ['Sandshrew-Alola', 'Sandslash-Alola', 'Vulpix-Alola', 'Ninetales-Alola', 'Dewgong', 'Cloyster', 'Jynx', 'Lapras', 'Articuno', 'Sneasel', 'Swinub', 'Piloswine', 'Delibird', 'Smoochum', 'Snorunt', 'Glalie', 'Glalie-Mega', 'Spheal', 'Sealeo', 'Walrein', 'Regice', 'Snover', 'Abomasnow', 'Abomasnow-Mega', 'Weavile', 'Glaceon', 'Mamoswine', 'Froslass', 'Rotom-Frost', 'Arceus-Ice', 'Vanillite', 'Vanillish', 'Vanilluxe', 'Cubchoo', 'Beartic', 'Cryogonal', 'Kyurem', 'Kyurem-Black', 'Kyurem-White', 'Amaura', 'Aurorus', 'Bergmite', 'Avalugg', 'Crabominable', 'Silvally-Ice']
Fairym = ['Clefairy', 'Clefable', 'Ninetales-Alola', 'Jigglypuff', 'Wigglytuff', 'Mr. Mime', 'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Marill', 'Azumarill', 'Snubbull', 'Granbull', 'Ralts', 'Kirlia', 'Gardevoir', 'Gardevoir-Mega', 'Azurill', 'Mawile', 'Mawile-Mega', 'Altaria-Mega', 'Mime Jr', 'Togekiss', 'Arceus-Fairy', 'Audino-Mega', 'Cottonee', 'Whimsicott', 'Flabebe', 'Flabebe-Blue', 'Flabebe-Orange', 'Flabebe-White', 'Flabebe-Yellow', 'Floette', 'Floette-Blue', 'Floette-Orange', 'Floette-White', 'Floette-Yellow', 'Floette-Eternal', 'Florges', 'Florges-Blue', 'Florges-Orange', 'Florges-White', 'Florges-Yellow', 'Spritzee', 'Aromatisse', 'Swirlix', 'Slurpuff', 'Sylveon', 'Dedenne', 'Carbink', 'Klefki', 'Xerneas', 'Diancie', 'Diancie-Mega', 'Primarina', 'Cutiefly', 'Ribombee', 'Morelull', 'Shiinotic', 'Comfey', 'Silvally-Fairy', 'Mimikyu', 'Tapu Koko', 'Tapu Lele', 'Tapu Bulu', 'Tapu Fini', 'Magearna']
Fightingm = ['Mankey', 'Primeape', 'Poliwrath', 'Machop', 'Machoke', 'Machamp', 'Hitmonlee', 'Hitmonchan', 'Mewtwo-Mega-X', 'Heracross', 'Heracross-Mega', 'Tyrogue', 'Hitmontop', 'Combusken', 'Blaziken', 'Blaziken-Mega', 'Breloom', 'Makuhita', 'Hariyama', 'Meditite', 'Medicham', 'Medicham-Mega', 'Monferno', 'Infernape', 'Lopunny-Mega', 'Riolu', 'Lucario', 'Lucario-Mega', 'Croagunk', 'Toxicroak', 'Gallade', 'Gallade-Mega', 'Arceus-Fighting', 'Pignite', 'Emboar', 'Timburr', 'Gurdurr', 'Conkeldurr', 'Throh', 'Sawk', 'Scraggy', 'Scrafty', 'Mienfoo', 'Mienshao', 'Cobalion', 'Terrakion', 'Virizion', 'Keldeo', 'Chesnaught', 'Pancham', 'Pangoro', 'Hawlucha', 'Crabrawler', 'Crabominable', 'Stufful', 'Bewear', 'Passimian', 'Silvally-Fighting', 'Hakamo-o', 'Kommo-o', 'Buzzwole', 'Pheromosa', 'Marshadow']
Psychicm = ['Raichu-Alola', 'Abra', 'Kadabra', 'Alakazam', 'Alakazam-Mega', 'Slowpoke', 'Slowbro', 'Slowbro-Mega', 'Drowzee', 'Hypno', 'Exeggcute', 'Exeggutor', 'Starmie', 'Mr. Mime', 'Jynx', 'Mewtwo', 'Mewtwo-Mega-X', 'Mewtwo-Mega-Y', 'Mew', 'Natu', 'Xatu', 'Espeon', 'Slowking', 'Unown', 'Wobbuffet', 'Girafarig', 'Smoochum', 'Lugia', 'Celebi', 'Ralts', 'Kirlia', 'Gardevoir', 'Gardevoir-Mega', 'Meditite', 'Medicham', 'Medicham-Mega', 'Spoink', 'Grumpig', 'Lunatone', 'Solrock', 'Baltoy', 'Claydol', 'Chimecho', 'Wynaut', 'Beldum', 'Metang', 'Metagross', 'Metagross-Mega', 'Latias', 'Latias-Mega', 'Latios', 'Latios-Mega', 'Jirachi', 'Deoxys', 'Deoxys-Attack', 'Deoxys-Defense', 'Deoxys-Speed', 'Chingling', 'Bronzor', 'Bronzong', 'Mime Jr', 'Gallade', 'Gallade-Mega', 'Uxie', 'Mesprit', 'Azelf', 'Cresselia', 'Arceus-Psychic', 'Victini', 'Munna', 'Musharna', 'Woobat', 'Swoobat', 'Sigilyph', 'Gothita', 'Gothorita', 'Gothitelle', 'Solosis', 'Duosion', 'Reuniclus', 'Elgyem', 'Beheeyem', 'Meloetta', 'Delphox', 'Espurr', 'Meowstic', 'Meowstic-F', 'Inkay', 'Malamar', 'Hoopa', 'Hoopa-Unbound', "Oricorio-Pa\\'u", 'Oranguru', 'Silvally-Psychic', 'Bruxish', 'Tapu Lele', 'Cosmog', 'Cosmoem', 'Solgaleo', 'Lunala', 'Necrozma', 'Necrozma-Dusk-Mane', 'Necrozma-Dawn-Wings', 'Necrozma-Ultra']
Rockm = ['Geodude', 'Geodude-Alola', 'Graveler', 'Graveler-Alola', 'Golem', 'Golem-Alola', 'Onix', 'Rhyhorn', 'Rhydon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Aerodactyl-Mega', 'Sudowoodo', 'Shuckle', 'Magcargo', 'Corsola', 'Larvitar', 'Pupitar', 'Tyranitar', 'Tyranitar-Mega', 'Nosepass', 'Aron', 'Lairon', 'Aggron', 'Lunatone', 'Solrock', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Relicanth', 'Regirock', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon', 'Bonsly', 'Rhyperior', 'Probopass', 'Arceus-Rock', 'Roggenrola', 'Boldore', 'Gigalith', 'Dwebble', 'Crustle', 'Tirtouga', 'Carracosta', 'Archen', 'Archeops', 'Terrakion', 'Binacle', 'Barbaracle', 'Tyrunt', 'Tyrantrum', 'Amaura', 'Aurorus', 'Carbink', 'Diancie', 'Diancie-Mega', 'Rockruff', 'Lycanroc', 'Lycanroc-Midnight', 'Lycanroc-Dusk', 'Silvally-Rock', 'Minior', 'Minior-Orange', 'Minior-Yellow', 'Minior-Green', 'Minior-Blue', 'Minior-Indigo', 'Minior-Violet', 'Minior-Meteor', 'Nihilego', 'Stakataka']
Ghostm = ['Gastly', 'Haunter', 'Gengar', 'Gengar-Mega', 'Marowak-Alola', 'Misdreavus', 'Shedinja', 'Sableye', 'Sableye-Mega', 'Shuppet', 'Banette', 'Banette-Mega', 'Duskull', 'Dusclops', 'Drifloon', 'Drifblim', 'Mismagius', 'Spiritomb', 'Dusknoir', 'Froslass', 'Rotom', 'Giratina', 'Giratina-Origin', 'Arceus-Ghost', 'Yamask', 'Cofagrigus', 'Frillish', 'Jellicent', 'Litwick', 'Lampent', 'Chandelure', 'Golett', 'Golurk', 'Honedge', 'Doublade', 'Aegislash', 'Phantump', 'Trevenant', 'Pumpkaboo', 'Pumpkaboo-Small', 'Pumpkaboo-Large', 'Pumpkaboo-Super', 'Gourgeist', 'Gourgeist-Small', 'Gourgeist-Large', 'Gourgeist-Super', 'Hoopa', 'Decidueye', 'Oricorio-Sensu', 'Sandygast', 'Palossand', 'Silvally-Ghost', 'Mimikyu', 'Dhelmise', 'Lunala', 'Necrozma-Dawn-Wings', 'Marshadow', 'Blacephalon']
Dragonm = ['Charizard-Mega-X', 'Exeggutor-Alola', 'Dratini', 'Dragonair', 'Dragonite', 'Ampharos-Mega', 'Kingdra', 'Sceptile-Mega', 'Vibrava', 'Flygon', 'Altaria', 'Altaria-Mega', 'Bagon', 'Shelgon', 'Salamence', 'Salamence-Mega', 'Latias', 'Latias-Mega', 'Latios', 'Latios-Mega', 'Rayquaza', 'Rayquaza-Mega', 'Gible', 'Gabite', 'Garchomp', 'Garchomp-Mega', 'Dialga', 'Palkia', 'Giratina', 'Giratina-Origin', 'Arceus-Dragon', 'Axew', 'Fraxure', 'Haxorus', 'Druddigon', 'Deino', 'Zweilous', 'Hydreigon', 'Reshiram', 'Zekrom', 'Kyurem', 'Kyurem-Black', 'Kyurem-White', 'Dragalge', 'Tyrunt', 'Tyrantrum', 'Goomy', 'Sliggoo', 'Goodra', 'Noibat', 'Noivern', 'Zygarde', 'Zygarde-10%', 'Zygarde-Complete', 'Silvally-Dragon', 'Turtonator', 'Drampa', 'Jangmo-o', 'Hakamo-o', 'Kommo-o', 'Guzzlord', 'Necrozma-Ultra', 'Naganadel']
Steelm = ['Sandshrew-Alola', 'Sandslash-Alola', 'Diglett-Alola', 'Dugtrio-Alola', 'Magnemite', 'Magneton', 'Forretress', 'Steelix', 'Steelix-Mega', 'Scizor', 'Scizor-Mega', 'Skarmory', 'Mawile', 'Mawile-Mega', 'Aron', 'Lairon', 'Aggron', 'Aggron-Mega', 'Beldum', 'Metang', 'Metagross', 'Metagross-Mega', 'Registeel', 'Jirachi', 'Empoleon', 'Shieldon', 'Bastiodon', 'Wormadam-Trash', 'Bronzor', 'Bronzong', 'Lucario', 'Lucario-Mega', 'Magnezone', 'Probopass', 'Dialga', 'Heatran', 'Arceus-Steel', 'Excadrill', 'Escavalier', 'Ferroseed', 'Ferrothorn', 'Klink', 'Klang', 'Klinklang', 'Pawniard', 'Bisharp', 'Durant', 'Cobalion', 'Genesect', 'Genesect-Douse', 'Genesect-Shock', 'Genesect-Burn', 'Genesect-Chill', 'Honedge', 'Doublade', 'Aegislash', 'Klefki', 'Silvally-Steel', 'Togedemaru', 'Solgaleo', 'Celesteela', 'Kartana', 'Necrozma-Dusk-Mane', 'Magearna', 'Stakataka']
Flyingm = ['Charizard', 'Charizard-Mega-Y', 'Butterfree', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Pidgeot-Mega', 'Spearow', 'Fearow', 'Zubat', 'Golbat', "Farfetch\\'d", 'Doduo', 'Dodrio', 'Scyther', 'Pinsir-Mega', 'Gyarados', 'Aerodactyl', 'Aerodactyl-Mega', 'Articuno', 'Zapdos', 'Moltres', 'Dragonite', 'Hoothoot', 'Noctowl', 'Ledyba', 'Ledian', 'Crobat', 'Togetic', 'Natu', 'Xatu', 'Hoppip', 'Skiploom', 'Jumpluff', 'Yanma', 'Murkrow', 'Gligar', 'Delibird', 'Mantine', 'Skarmory', 'Lugia', 'Ho-Oh', 'Beautifly', 'Taillow', 'Swellow', 'Wingull', 'Pelipper', 'Masquerain', 'Ninjask', 'Swablu', 'Altaria', 'Tropius', 'Salamence', 'Salamence-Mega', 'Rayquaza', 'Rayquaza-Mega', 'Starly', 'Staravia', 'Staraptor', 'Mothim', 'Combee', 'Vespiquen', 'Drifloon', 'Drifblim', 'Honchkrow', 'Chatot', 'Mantyke', 'Togekiss', 'Yanmega', 'Gliscor', 'Rotom-Fan', 'Shaymin-Sky', 'Arceus-Flying', 'Pidove', 'Tranquill', 'Unfezant', 'Woobat', 'Swoobat', 'Sigilyph', 'Archen', 'Archeops', 'Ducklett', 'Swanna', 'Emolga', 'Rufflet', 'Braviary', 'Vullaby', 'Mandibuzz', 'Tornadus', 'Tornadus-Therian', 'Thundurus', 'Thundurus-Therian', 'Landorus', 'Landorus-Therian', 'Fletchling', 'Fletchinder', 'Talonflame', 'Vivillon', 'Vivillon-Fancy', 'Vivillon-Pokeball', 'Hawlucha', 'Noibat', 'Noivern', 'Yveltal', 'Rowlet', 'Dartrix', 'Pikipek', 'Trumbeak', 'Toucannon', 'Oricorio', 'Oricorio-Pom-Pom', "Oricorio-Pa\\'u", 'Oricorio-Sensu', 'Silvally-Flying', 'Minior', 'Minior-Orange', 'Minior-Yellow', 'Minior-Green', 'Minior-Blue', 'Minior-Indigo', 'Minior-Violet', 'Minior-Meteor', 'Celesteela']

#List of Pokemon by colour for Mono-Colour
Green = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Venusaur-Mega', 'Caterpie', 'Metapod', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Grimer-Alola', 'Muk-Alola', 'Scyther', 'Chikorita', 'Bayleef', 'Meganium', 'Spinarak', 'Natu', 'Xatu', 'Bellossom', 'Politoed', 'Skiploom', 'Larvitar', 'Tyranitar', 'Tyranitar-Mega', 'Celebi', 'Treecko', 'Grovyle', 'Sceptile', 'Sceptile-Mega', 'Dustox', 'Lotad', 'Lombre', 'Ludicolo', 'Breloom', 'Electrike', 'Roselia', 'Gulpin', 'Vibrava', 'Flygon', 'Cacnea', 'Cacturne', 'Cradily', 'Kecleon', 'Tropius', 'Rayquaza', 'Rayquaza-Mega', 'Turtwig', 'Grotle', 'Torterra', 'Budew', 'Roserade', 'Burmy', 'Wormadam', 'Bronzor', 'Bronzong', 'Carnivine', 'Yanmega', 'Leafeon', 'Shaymin', 'Shaymin-Sky', 'Snivy', 'Servine', 'Serperior', 'Pansage', 'Simisage', 'Swadloon', 'Cottonee', 'Whimsicott', 'Petilil', 'Lilligant', 'Basculin', 'Basculin-Blue-Striped', 'Maractus', 'Trubbish', 'Garbodor', 'Solosis', 'Duosion', 'Reuniclus', 'Axew', 'Fraxure', 'Golett', 'Golurk', 'Virizion', 'Tornadus', 'Tornadus-Therian', 'Chespin', 'Quilladin', 'Chesnaught', 'Hawlucha', 'Zygarde', 'Zygarde-10%', 'Zygarde-Complete', 'Charjabug', 'Dewpider', 'Araquanid', 'Comfey', 'Dhelmise', 'Celesteela']
Red = ['Charmander', 'Charmeleon', 'Charizard', 'Charizard-Mega-Y', 'Vileplume', 'Paras', 'Parasect', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Goldeen', 'Seaking', 'Jynx', 'Magmar', 'Magikarp', 'Flareon', 'Ledyba', 'Ledian', 'Ariados', 'Yanma', 'Scizor', 'Scizor-Mega', 'Slugma', 'Magcargo', 'Octillery', 'Delibird', 'Porygon2', 'Magby', 'Ho-Oh', 'Torchic', 'Combusken', 'Blaziken', 'Blaziken-Mega', 'Wurmple', 'Medicham', 'Medicham-Mega', 'Carvanha', 'Camerupt', 'Camerupt-Mega', 'Solrock', 'Corphish', 'Crawdaunt', 'Latias', 'Groudon', 'Groudon-Primal', 'Deoxys', 'Deoxys-Attack', 'Deoxys-Defense', 'Deoxys-Speed', 'Kricketot', 'Kricketune', 'Wormadam-Trash', 'Magmortar', 'Porygon-Z', 'Rotom', 'Rotom-Heat', 'Rotom-Wash', 'Rotom-Frost', 'Rotom-Fan', 'Rotom-Mow', 'Tepig', 'Pignite', 'Emboar', 'Pansear', 'Simisear', 'Throh', 'Venipede', 'Scolipede', 'Krookodile', 'Darumaka', 'Darmanitan', 'Dwebble', 'Crustle', 'Scrafty', 'Shelmet', 'Accelgor', 'Druddigon', 'Pawniard', 'Bisharp', 'Braviary', 'Heatmor', 'Fennekin', 'Braixen', 'Delphox', 'Fletchling', 'Fletchinder', 'Talonflame', 'Tyrantrum', 'Yveltal', 'Litten', 'Torracat', 'Incineroar', 'Oricorio', 'Lycanroc-Midnight', 'Minior', 'Minior-Orange', 'Minior-Yellow', 'Minior-Green', 'Minior-Blue', 'Minior-Indigo', 'Minior-Violet', 'Turtonator', 'Tapu Bulu', 'Buzzwole']
Black = ['Charizard-Mega-X', 'Rattata-Alola', 'Raticate-Alola', 'Snorlax', 'Umbreon', 'Murkrow', 'Unown', 'Sneasel', 'Houndour', 'Houndoom', 'Houndoom-Mega', 'Mawile', 'Mawile-Mega', 'Spoink', 'Seviper', 'Claydol', 'Shuppet', 'Banette', 'Banette-Mega', 'Duskull', 'Dusclops', 'Honchkrow', 'Chatot', 'Munchlax', 'Weavile', 'Dusknoir', 'Giratina', 'Giratina-Origin', 'Darkrai', 'Blitzle', 'Zebstrika', 'Sigilyph', 'Yamask', 'Lampent', 'Chandelure', 'Zekrom', 'Scatterbug', 'Spewpa', 'Vivillon-Fancy', 'Vivillon-Pokeball', 'Pikipek', 'Trumbeak', 'Toucannon', 'Salandit', 'Salazzle', 'Pyukumuku', 'Xurkitree', 'Guzzlord', 'Necrozma']
Blue = ['Squirtle', 'Wartortle', 'Blastoise', 'Blastoise-Mega', 'Sandslash-Alola', 'Nidoran-F', 'Nidorina', 'Nidoqueen', 'Ninetales-Alola', 'Oddish', 'Gloom', 'Meowth-Alola', 'Persian-Alola', 'Golduck', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Tentacool', 'Tentacruel', 'Tangela', 'Horsea', 'Seadra', 'Gyarados', 'Gyarados-Mega', 'Lapras', 'Vaporeon', 'Omanyte', 'Omastar', 'Articuno', 'Dratini', 'Dragonair', 'Totodile', 'Croconaw', 'Feraligatr', 'Chinchou', 'Lanturn', 'Marill', 'Azumarill', 'Jumpluff', 'Wooper', 'Quagsire', 'Wobbuffet', 'Heracross', 'Heracross-Mega', 'Kingdra', 'Phanpy', 'Suicune', 'Mudkip', 'Marshtomp', 'Swampert', 'Swampert-Mega', 'Taillow', 'Swellow', 'Surskit', 'Masquerain', 'Loudred', 'Exploud', 'Azurill', 'Meditite', 'Sharpedo', 'Sharpedo-Mega', 'Wailmer', 'Wailord', 'Swablu', 'Altaria', 'Altaria-Mega', 'Whiscash', 'Chimecho', 'Wynaut', 'Spheal', 'Sealeo', 'Walrein', 'Clamperl', 'Huntail', 'Bagon', 'Salamence', 'Salamence-Mega', 'Beldum', 'Metang', 'Metagross', 'Metagross-Mega', 'Regice', 'Latios', 'Kyogre', 'Kyogre-Primal', 'Piplup', 'Prinplup', 'Empoleon', 'Shinx', 'Luxio', 'Luxray', 'Cranidos', 'Rampardos', 'Gible', 'Gabite', 'Garchomp', 'Garchomp-Mega', 'Riolu', 'Lucario', 'Lucario-Mega', 'Croagunk', 'Toxicroak', 'Finneon', 'Lumineon', 'Mantyke', 'Tangrowth', 'Glaceon', 'Azelf', 'Phione', 'Manaphy', 'Oshawott', 'Dewott', 'Samurott', 'Panpour', 'Simipour', 'Roggenrola', 'Boldore', 'Gigalith', 'Woobat', 'Swoobat', 'Tympole', 'Palpitoad', 'Seismitoad', 'Sawk', 'Tirtouga', 'Carracosta', 'Ducklett', 'Karrablast', 'Eelektrik', 'Eelektross', 'Elgyem', 'Cryogonal', 'Deino', 'Zweilous', 'Hydreigon', 'Cobalion', 'Thundurus', 'Thundurus-Therian', 'Froakie', 'Frogadier', 'Greninja', 'Greninja-Ash', 'Meowstic', 'Inkay', 'Malamar', 'Clauncher', 'Clawitzer', 'Amaura', 'Aurorus', 'Bergmite', 'Avalugg', 'Xerneas', 'Popplio', 'Brionne', 'Primarina', 'Vikavolt', 'Wishiwashi', 'Mareanie', 'Toxapex', 'Komala', 'Cosmog', 'Cosmoem', 'Necrozma-Dawn-Wings', 'Necrozma-Ultra']
White = ['Butterfree', 'Sandshrew-Alola', 'Vulpix-Alola', 'Seel', 'Dewgong', 'Togepi', 'Togetic', 'Mareep', 'Smeargle', 'Lugia', 'Linoone', 'Silcoon', 'Wingull', 'Ralts', 'Kirlia', 'Gardevoir', 'Gardevoir-Mega', 'Vigoroth', 'Zangoose', 'Absol', 'Absol-Mega', 'Shelgon', 'Pachirisu', 'Snover', 'Abomasnow', 'Abomasnow-Mega', 'Togekiss', 'Gallade', 'Gallade-Mega', 'Froslass', 'Dialga', 'Regigigas', 'Arceus', 'Audino-Mega', 'Swanna', 'Vanillite', 'Vanillish', 'Vanilluxe', 'Emolga', 'Foongus', 'Amoonguss', 'Frillish', 'Jellicent', 'Tynamo', 'Litwick', 'Cubchoo', 'Beartic', 'Rufflet', 'Larvesta', 'Volcarona', 'Reshiram', 'Meloetta', 'Vivillon', 'Flabebe', 'Flabebe-Blue', 'Flabebe-Orange', 'Flabebe-White', 'Flabebe-Yellow', 'Floette', 'Floette-Blue', 'Floette-Orange', 'Floette-White', 'Floette-Yellow', 'Floette-Eternal', 'Florges', 'Florges-Blue', 'Florges-Orange', 'Florges-White', 'Florges-Yellow', 'Pancham', 'Pangoro', 'Furfrou', 'Meowstic-F', 'Swirlix', 'Slurpuff', 'Crabominable', 'Oranguru', 'Passimian', 'Drampa', 'Solgaleo', 'Nihilego', 'Pheromosa', 'Kartana', 'Blacephalon']
Brown = ['Weedle', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Pidgeot-Mega', 'Raticate', 'Spearow', 'Fearow', 'Raichu-Alola', 'Vulpix', 'Diglett', 'Diglett-Alola', 'Dugtrio', 'Dugtrio-Alola', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Abra', 'Kadabra', 'Alakazam', 'Alakazam-Mega', 'Geodude', 'Graveler', 'Golem', "Farfetch'd", 'Doduo', 'Dodrio', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Kangaskhan', 'Kangaskhan-Mega', 'Staryu', 'Pinsir', 'Pinsir-Mega', 'Tauros', 'Eevee', 'Kabuto', 'Kabutops', 'Dragonite', 'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Sudowoodo', 'Teddiursa', 'Ursaring', 'Swinub', 'Piloswine', 'Stantler', 'Hitmontop', 'Entei', 'Zigzagoon', 'Seedot', 'Nuzleaf', 'Shiftry', 'Shroomish', 'Slakoth', 'Slaking', 'Shedinja', 'Hariyama', 'Torkoal', 'Spinda', 'Trapinch', 'Baltoy', 'Feebas', 'Regirock', 'Chimchar', 'Monferno', 'Infernape', 'Starly', 'Staravia', 'Staraptor', 'Bidoof', 'Bibarel', 'Wormadam-Sandy', 'Buizel', 'Floatzel', 'Buneary', 'Lopunny', 'Lopunny-Mega', 'Bonsly', 'Hippopotas', 'Hippowdon', 'Mamoswine', 'Heatran', 'Patrat', 'Watchog', 'Lillipup', 'Conkeldurr', 'Sandile', 'Krokorok', 'Sawsbuck', 'Beheeyem', 'Stunfisk', 'Bouffalant', 'Vullaby', 'Mandibuzz', 'Landorus', 'Landorus-Therian', 'Bunnelby', 'Diggersby', 'Litleo', 'Pyroar', 'Skiddo', 'Gogoat', 'Honedge', 'Doublade', 'Aegislash', 'Binacle', 'Barbaracle', 'Skrelp', 'Dragalge', 'Tyrunt', 'Phantump', 'Trevenant', 'Pumpkaboo', 'Pumpkaboo-Small', 'Pumpkaboo-Large', 'Pumpkaboo-Super', 'Gourgeist', 'Gourgeist-Small', 'Gourgeist-Large', 'Gourgeist-Super', 'Volcanion', 'Rowlet', 'Dartrix', 'Decidueye', 'Yungoos', 'Gumshoos', 'Rockruff', 'Lycanroc', 'Lycanroc-Dusk', 'Mudbray', 'Mudsdale', 'Sandygast', 'Palossand', 'Minior-Meteor']
Yellow = ['Kakuna', 'Beedrill', 'Beedrill-Mega', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Ninetales', 'Meowth', 'Persian', 'Psyduck', 'Ponyta', 'Rapidash', 'Drowzee', 'Hypno', 'Exeggutor', 'Exeggutor-Alola', 'Electabuzz', 'Jolteon', 'Zapdos', 'Moltres', 'Cyndaquil', 'Quilava', 'Typhlosion', 'Pichu', 'Ampharos', 'Ampharos-Mega', 'Sunkern', 'Sunflora', 'Girafarig', 'Dunsparce', 'Shuckle', 'Elekid', 'Raikou', 'Beautifly', 'Pelipper', 'Ninjask', 'Makuhita', 'Manectric', 'Manectric-Mega', 'Plusle', 'Minun', 'Numel', 'Lunatone', 'Jirachi', 'Mothim', 'Combee', 'Vespiquen', 'Chingling', 'Electivire', 'Uxie', 'Cresselia', 'Victini', 'Sewaddle', 'Leavanny', 'Scraggy', 'Cofagrigus', 'Archen', 'Archeops', 'Joltik', 'Galvantula', 'Haxorus', 'Mienfoo', 'Keldeo', 'Helioptile', 'Heliolisk', 'Dedenne', 'Oricorio-Pom-Pom', 'Cutiefly', 'Ribombee', 'Mimikyu', 'Tapu Koko', 'Necrozma-Dusk-Mane', 'Zeraora']
Purple = ['Rattata', 'Ekans', 'Arbok', 'Nidoran-M', 'Nidorino', 'Nidoking', 'Zubat', 'Golbat', 'Venonat', 'Venomoth', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Gengar-Mega', 'Marowak-Alola', 'Koffing', 'Weezing', 'Starmie', 'Ditto', 'Aerodactyl', 'Aerodactyl-Mega', 'Mewtwo', 'Mewtwo-Mega-X', 'Mewtwo-Mega-Y', 'Crobat', 'Aipom', 'Espeon', 'Forretress', 'Gligar', 'Granbull', 'Mantine', 'Tyrogue', 'Cascoon', 'Delcatty', 'Sableye', 'Sableye-Mega', 'Illumise', 'Swalot', 'Grumpig', 'Lileep', 'Latias-Mega', 'Latios-Mega', 'Cherrim', 'Shellos', 'Gastrodon', 'Ambipom', 'Drifloon', 'Drifblim', 'Mismagius', 'Stunky', 'Skuntank', 'Spiritomb', 'Skorupi', 'Drapion', 'Gliscor', 'Palkia', 'Purrloin', 'Liepard', 'Gothita', 'Gothorita', 'Gothitelle', 'Mienshao', 'Genesect', 'Genesect-Douse', 'Genesect-Shock', 'Genesect-Burn', 'Genesect-Chill', 'Goomy', 'Sliggoo', 'Goodra', 'Noibat', 'Noivern', 'Hoopa', 'Hoopa-Unbound', 'Crabrawler', 'Oricorio-Sensu', 'Morelull', 'Shiinotic', 'Bounsweet', 'Steenee', 'Tsareena', 'Tapu Fini', 'Lunala', 'Poipole', 'Naganadel']
Pink = ['Clefairy', 'Clefable', 'Jigglypuff', 'Wigglytuff', 'Slowpoke', 'Slowbro', 'Slowbro-Mega', 'Exeggcute', 'Lickitung', 'Chansey', 'Mr. Mime', 'Porygon', 'Mew', 'Cleffa', 'Igglybuff', 'Flaaffy', 'Hoppip', 'Slowking', 'Snubbull', 'Corsola', 'Smoochum', 'Miltank', 'Blissey', 'Whismur', 'Skitty', 'Milotic', 'Gorebyss', 'Luvdisc', 'Cherubi', 'Mime Jr.', 'Happiny', 'Lickilicky', 'Mesprit', 'Munna', 'Musharna', 'Audino', 'Deerling', 'Alomomola', 'Spritzee', 'Aromatisse', 'Sylveon', 'Diancie', 'Diancie-Mega', "Oricorio-Pa'u", 'Fomantis', 'Lurantis', 'Stufful', 'Bewear', 'Bruxish', 'Tapu Lele']
Grey = ['Machop', 'Machoke', 'Machamp', 'Geodude-Alola', 'Graveler-Alola', 'Golem-Alola', 'Magnemite', 'Magneton', 'Onix', 'Rhyhorn', 'Rhydon', 'Misdreavus', 'Pineco', 'Steelix', 'Steelix-Mega', 'Qwilfish', 'Remoraid', 'Skarmory', 'Donphan', 'Pupitar', 'Poochyena', 'Mightyena', 'Nincada', 'Nosepass', 'Aron', 'Lairon', 'Aggron', 'Aggron-Mega', 'Volbeat', 'Barboach', 'Anorith', 'Armaldo', 'Castform', 'Snorunt', 'Glalie', 'Glalie-Mega', 'Relicanth', 'Registeel', 'Shieldon', 'Bastiodon', 'Glameow', 'Purugly', 'Magnezone', 'Rhyperior', 'Probopass', 'Arceus-Bug', 'Arceus-Dark', 'Arceus-Dragon', 'Arceus-Electric', 'Arceus-Fairy', 'Arceus-Fighting', 'Arceus-Fire', 'Arceus-Flying', 'Arceus-Ghost', 'Arceus-Grass', 'Arceus-Ground', 'Arceus-Ice', 'Arceus-Poison', 'Arceus-Psychic', 'Arceus-Rock', 'Arceus-Steel', 'Arceus-Water', 'Herdier', 'Stoutland', 'Pidove', 'Tranquill', 'Unfezant', 'Drilbur', 'Excadrill', 'Timburr', 'Gurdurr', 'Whirlipede', 'Zorua', 'Zoroark', 'Minccino', 'Cinccino', 'Escavalier', 'Ferroseed', 'Ferrothorn', 'Klink', 'Klang', 'Klinklang', 'Durant', 'Terrakion', 'Kyurem', 'Kyurem-Black', 'Kyurem-White', 'Espurr', 'Carbink', 'Klefki', 'Grubbin', 'Wimpod', 'Golisopod', 'Type: Null', 'Silvally', 'Silvally-Bug', 'Silvally-Dark', 'Silvally-Dragon', 'Silvally-Electric', 'Silvally-Fairy', 'Silvally-Fighting', 'Silvally-Fire', 'Silvally-Flying', 'Silvally-Ghost', 'Silvally-Grass', 'Silvally-Ground', 'Silvally-Ice', 'Silvally-Poison', 'Silvally-Psychic', 'Silvally-Rock', 'Silvally-Steel', 'Silvally-Water', 'Togedemaru', 'Jangmo-o', 'Hakamo-o', 'Kommo-o', 'Magearna', 'Marshadow', 'Stakataka']

#List I used for checking which Pokemon had multiple forms
form_mons = ['Venusaur-Mega', 'Charizard-Mega-X', 'Charizard-Mega-Y', 'Blastoise-Mega', 'Beedrill-Mega', 'Pidgeot-Mega', 'Rattata-Alola', 'Raticate-Alola', 'Raichu-Alola', 'Sandshrew-Alola', 'Sandslash-Alola', 'Nidoran-F', 'Nidoran-M', 'Vulpix-Alola', 'Ninetales-Alola', 'Diglett-Alola', 'Dugtrio-Alola', 'Meowth-Alola', 'Persian-Alola', 'Alakazam-Mega', 'Geodude-Alola', 'Graveler-Alola', 'Golem-Alola', 'Slowbro-Mega', 'Grimer-Alola', 'Muk-Alola', 'Gengar-Mega', 'Exeggutor-Alola', 'Marowak-Alola', 'Kangaskhan-Mega', 'Pinsir-Mega', 'Gyarados-Mega', 'Aerodactyl-Mega', 'Mewtwo-Mega-X', 'Mewtwo-Mega-Y', 'Ampharos-Mega', 'Steelix-Mega', 'Scizor-Mega', 'Heracross-Mega', 'Houndoom-Mega', 'Tyranitar-Mega', 'Sceptile-Mega', 'Blaziken-Mega', 'Swampert-Mega', 'Gardevoir-Mega', 'Sableye-Mega', 'Mawile-Mega', 'Aggron-Mega', 'Medicham-Mega', 'Manectric-Mega', 'Sharpedo-Mega', 'Camerupt-Mega', 'Altaria-Mega', 'Banette-Mega', 'Absol-Mega', 'Glalie-Mega', 'Salamence-Mega', 'Metagross-Mega', 'Latias-Mega', 'Latios-Mega', 'Kyogre-Primal', 'Groudon-Primal', 'Rayquaza-Mega', 'Deoxys-Attack', 'Deoxys-Defense', 'Deoxys-Speed', 'Wormadam-Sandy', 'Wormadam-Trash', 'Lopunny-Mega', 'Garchomp-Mega', 'Lucario-Mega', 'Abomasnow-Mega', 'Gallade-Mega', 'Rotom-Heat', 'Rotom-Wash', 'Rotom-Frost', 'Rotom-Fan', 'Rotom-Mow', 'Giratina-Origin', 'Shaymin-Sky', 'Arceus-Bug', 'Arceus-Dark', 'Arceus-Dragon', 'Arceus-Electric', 'Arceus-Fairy', 'Arceus-Fighting', 'Arceus-Fire', 'Arceus-Flying', 'Arceus-Ghost', 'Arceus-Grass', 'Arceus-Ground', 'Arceus-Ice', 'Arceus-Poison', 'Arceus-Psychic', 'Arceus-Rock', 'Arceus-Steel', 'Arceus-Water', 'Audino-Mega', 'Basculin-Blue-Striped', 'Tornadus-Therian', 'Thundurus-Therian', 'Landorus-Therian', 'Kyurem-Black', 'Kyurem-White', 'Genesect-Douse', 'Genesect-Shock', 'Genesect-Burn', 'Genesect-Chill', 'Greninja-Ash', 'Vivillon-Fancy', 'Vivillon-Pokeball', 'Flabebe-Blue', 'Flabebe-Orange', 'Flabebe-White', 'Flabebe-Yellow', 'Floette-Blue', 'Floette-Orange', 'Floette-White', 'Floette-Yellow', 'Floette-Eternal', 'Florges-Blue', 'Florges-Orange', 'Florges-White', 'Florges-Yellow', 'Meowstic-F', 'Pumpkaboo-Small', 'Pumpkaboo-Large', 'Pumpkaboo-Super', 'Gourgeist-Small', 'Gourgeist-Large', 'Gourgeist-Super', 'Zygarde-10%', 'Zygarde-Complete', 'Diancie-Mega', 'Hoopa-Unbound', 'Oricorio-Pom-Pom', "Oricorio-Pa'u", 'Oricorio-Sensu', 'Lycanroc-Midnight', 'Lycanroc-Dusk', 'Silvally-Bug', 'Silvally-Dark', 'Silvally-Dragon', 'Silvally-Electric', 'Silvally-Fairy', 'Silvally-Fighting', 'Silvally-Fire', 'Silvally-Flying', 'Silvally-Ghost', 'Silvally-Grass', 'Silvally-Ground', 'Silvally-Ice', 'Silvally-Poison', 'Silvally-Psychic', 'Silvally-Rock', 'Silvally-Steel', 'Silvally-Water', 'Minior-Orange', 'Minior-Yellow', 'Minior-Green', 'Minior-Blue', 'Minior-Indigo', 'Minior-Violet', 'Minior-Meteor', 'Necrozma-Dusk-Mane', 'Necrozma-Dawn-Wings', 'Necrozma-Ultra']

#List of items by tier
tier1 = ['Assault Vest', 'Choice Band', 'Choice Scarf', 'Choice Specs', 'Eviolite', 'Focus Sash', 'Leftovers', 'Life Orb', 'Lum Berry', 'Mental Herb', 'Power Herb', 'Rocky Helmet', 'Sitrus Berry']
tier2 = ['Absorb Bulb', 'Adrenaline Orb', 'Air Balloon',  'Apicot Berry', 'Babiri Berry', 'Berry Juice', 'Big Root', 'Black Belt', 'Black Glasses', 'Black Sludge', 'BrightPowder', 'Buginium Z', 'Cell Battery', 'Charcoal', 'Charti Berry', 'Chesto Berry', 'Chilan Berry', 'Chople Berry', 'Coba Berry', 'Colbur Berry', 'Custap Berry', 'Damp Rock', 'Darkinium Z', 'Draco Plate', 'Dragon Fang', 'Dragonium Z', 'Dread Plate', 'Earth Plate', 'Eject Button', 'Electric Seed', 'Electrium Z', 'Expert Belt', 'Fairium Z', 'Fightinium Z', 'Firium Z', 'Fist Plate', 'Flame Orb', 'Flame Plate', 'Flyinium Z', 'Focus Band', 'Full Incense', 'Ganlon Berry', 'Ghostium Z', 'Grassium Z', 'Grassy Seed', 'Grepa Berry', 'Grip Claw', 'Groundium Z', 'Haban Berry', 'Hard Stone', 'Heat Rock', 'Iapapa Berry', 'Icicle Plate', 'Icium Z', 'Icy Rock', 'Insect Plate', 'Iron Plate', 'Kasib Berry', 'Kebia Berry', 'Kee Berry', 'Kelpsy Berry', "King's Rock", 'Lagging Tail', 'Lansat Berry', 'Lax Incense', 'Leppa Berry', 'Liechi Berry', 'Light Clay', 'Luminous Moss', 'Magnet', 'Mail', 'Maranga Berry', 'Meadow Plate', 'Metal Coat', 'Metronome', 'Micle Berry', 'Mind Plate', 'Miracle Seed', 'Misty Seed', 'Muscle Band', 'Mystic Water', 'Never-Melt Ice', 'Normal Gem', 'Normalium Z', 'Occa Berry', 'Odd Incense', 'Passho Berry', 'Payapa Berry', 'Petaya Berry', 'Pixie Plate', 'Poison Barb', 'Poisonium Z', 'Protective Pads', 'Psychic Seed', 'Psychium Z', 'Quick Claw', 'Razor Claw', 'Razor Fang', 'Red Card', 'Rindo Berry', 'Rock Incense', 'Rockium Z', 'Rose Incense', 'Roseli Berry', 'Safety Goggles', 'Salac Berry', 'Scope Lens', 'Sea Incense', 'Sharp Beak', 'Shed Shell', 'Shell Bell', 'Shuca Berry', 'Silk Scarf', 'SilverPowder', 'Sky Plate', 'Smooth Rock', 'Snowball', 'Soft Sand', 'Spell Tag', 'Splash Plate', 'Spooky Plate', 'Starf Berry', 'Steelium Z', 'Sticky Barb', 'Stone Plate', 'Tanga Berry', 'Terrain Extender', 'Toxic Orb', 'Toxic Plate', 'Twisted Spoon', 'Wacan Berry', 'Waterium Z', 'Wave Incense', 'Weakness Policy', 'White Herb', 'Wide Lens', 'Wise Glasses', 'Yache Berry', 'Zap Plate', 'Zoom Lens']
pokespec = ['Kommonium Z', 'Marshadium Z', 'Ultranecrozium Z', 'Lunalium Z', 'Solganium Z', 'Tapunium Z', 'Mimikium Z', 'Lycanium Z', 'Primarium Z', 'Incinium Z', 'Decidium Z', 'Mewnium Z', 'Snorlium Z', 'Pikanium Z', 'Pikashunium Z', 'Aloraichium Z', 'Eevium Z', 'Abomasite', 'Absolite', 'Adamant Orb', 'Aerodactylite', 'Aggronite', 'Alakazite', 'Altarianite', 'Ampharosite', 'Audinite', 'Banettite', 'Beedrillite', 'Blastoisinite', 'Blazikenite', 'Blue Orb', 'Burn Drive', 'Cameruptite', 'Charizardite X', 'Charizardite Y', 'Chill Drive', 'Deep Sea Scale', 'Deep Sea Tooth', 'Diancite', 'Douse Drive', 'Galladite', 'Garchompite', 'Gardevoirite', 'Gengarite', 'Glalitite', 'Griseous Orb', 'Gyaradosite', 'Heracronite', 'Houndoominite', 'Kangaskhanite', 'Latiasite', 'Latiosite', 'Light Ball', 'Lopunnite', 'Lucarionite', 'Lucky Punch', 'Lustrous Orb', 'Manectite', 'Mawilite', 'Medichamite', 'Metagrossite', 'Metal Powder', 'Mewtwonite X', 'Mewtwonite Y', 'Pidgeotite', 'Pinsirite', 'Quick Powder', 'Red Orb', 'Sablenite', 'Salamencite', 'Sceptilite', 'Scizorite', 'Sharpedonite', 'Shock Drive', 'Slowbronite', 'Soul Dew', 'Steelixite', 'Stick', 'Swampertite', 'Thick Club', 'Tyranitarite', 'Venusaurite', 'Bug Memory', 'Dark Memory', 'Dragon Memory', 'Electric Memory', 'Fairy Memory', 'Fire Memory', 'Flying Memory', 'Ghost Memory', 'Grass Memory', 'Ground Memory', 'Ice Memory', 'Poison Memory', 'Psychic Memory', 'Rock Memory', 'Steel Memory', 'Water Memory']
tier3 = ['Aguav Berry', 'Aspear Berry', 'Binding Band', 'Cheri Berry', 'Destiny Knot', 'Enigma Berry', 'Figy Berry', 'Float Stone', 'Iron Ball', 'Jaboca Berry', 'Macho Brace', 'Mago Berry', 'Oran Berry', 'Pecha Berry', 'Persim Berry', 'Power Anklet', 'Power Band', 'Power Belt', 'Power Bracer', 'Power Lens', 'Power Weight', 'Rawst Berry', 'Ring Target', 'Rowap Berry', 'Wiki Berry']

#List of moves by tier
tieroneab = ['Adaptability', 'Adaptability', 'Aerilate', 'Arena Trap', 'Battle Bond', 'Beast Boost', 'Bulletproof', 'Chlorophyll', 'Comatose', 'Compound Eyes', 'Contrary', 'Dark Aura', 'Dazzling', 'Delta Stream', 'Desolate Land', 'Disguise', 'Download', 'Drizzle', 'Drought', 'Dry Skin', 'Electric Surge', 'Fairy Aura', 'Filter', 'Flash Fire', 'Forecast', 'Fur Coat', 'Gale Wings', 'Galvanize', 'Grassy Surge', 'Guts', 'Huge Power', 'Hustle', 'Illusion', 'Imposter', 'Infiltrator', 'Intimidate', 'Iron Barbs', 'Iron Fist', 'Levitate', 'Lightning Rod', 'Magic Bounce', 'Magic Guard', 'Magnet Pull', 'Mega Launcher', 'Misty Surge', 'Mold Breaker', 'Moody', 'Motor Drive', 'Moxie', 'Multiscale', 'Multitype', 'Natural Cure', 'Neuroforce', 'No Guard', 'Normalize', 'Parental Bond', 'Pixilate', 'Poison Heal', 'Power Construct', 'Prankster', 'Primordial Sea', 'Prism Armor', 'Protean', 'Psychic Surge', 'Pure Power', 'Queenly Majesty', 'Reckless', 'Refrigerate', 'Regenerator', 'RKS System', 'Rough Skin', 'Sand Rush', 'Sand Stream', 'Sap Sipper', 'Schooling', 'Scrappy', 'Serene Grace', 'Shadow Shield', 'Shadow Tag', 'Shed Skin', 'Sheer Force', 'Shields Down', 'Simple', 'Skill Link', 'Snow Warning', 'Solid Rock', 'Soul-Heart', 'Speed Boost', 'Stamina', 'Stance Change', 'Steelworker', 'Storm Drain', 'Strong Jaw', 'Sturdy', 'Swift Swim', 'Technician', 'Teravolt', 'Thick Fat', 'Tinted Lens', 'Tough Claws', 'Toxic Boost', 'Trace', 'Triage', 'Turboblaze', 'Unaware', 'Unburden', 'Victory Star', 'Volt Absorb', 'Water Absorb', 'Water Bubble', 'Wonder Guard']
tiertwoab = ['Aftermath', 'Air Lock', 'Analytic', 'Anger Point', 'Bad Dreams', 'Berserk', 'Blaze', 'Cheek Pouch', 'Clear Body', 'Cloud Nine', 'Competitive', 'Corrosion', 'Cursed Body', 'Dancer', 'Defiant', 'Early Bird', 'Effect Spore', 'Emergency Exit', 'Flame Body', 'Flare Boost', 'Flower Gift', 'Fluffy', 'Full Metal Body', 'Gooey', 'Harvest', 'Heatproof', 'Hydration', 'Immunity', 'Innards Out', 'Insomnia', 'Justified', 'Liquid Voice', 'Marvel Scale', 'Merciless', 'Mummy', 'Overcoat', 'Overgrow', 'Poison Point', 'Poison Touch', 'Pressure', 'Quick Feet', 'Rock Head', 'Sand Force', 'Shield Dust', 'Slush Rush', 'Soundproof', 'Stakeout', 'Static', 'Surge Surfer', 'Swarm', 'Sweet Veil', 'Synchronize', 'Tangling Hair', 'Torrent', 'Vital Spirit', 'Water Compaction', 'Water Veil', 'White Smoke', 'Wimp Out', 'Wonder Skin']
tierthreeab = ['Anticipation', 'Aroma Veil', 'Aura Break', 'Battery', 'Battle Armor', 'Big Pecks', 'Color Change', 'Cute Charm', 'Damp', 'Defeatist', 'Flower Veil', 'Forewarn', 'Friend Guard', 'Frisk', 'Gluttony', 'Grass Pelt', 'Healer', 'Heavy Metal', 'Honey Gather', 'Hyper Cutter', 'Ice Body', 'Illuminate', 'Inner Focus', 'Keen Eye', 'Klutz', 'Leaf Guard', 'Light Metal', 'Limber', 'Liquid Ooze', 'Long Reach', 'Magician', 'Magma Armor', 'Minus', 'Oblivious', 'Own Tempo', 'Pickpocket', 'Pickup', 'Plus', 'Power of Alchemy', 'Rain Dish', 'Rattled', 'Receiver', 'Rivalry', 'Run Away', 'Sand Veil', 'Shell Armor', 'Slow Start', 'Sniper', 'Snow Cloak', 'Solar Power', 'Stall', 'Steadfast', 'Stench', 'Sticky Hold', 'Suction Cups', 'Super Luck', 'Symbiosis', 'Tangled Feet', 'Telepathy', 'Truant', 'Unnerve', 'Weak Armor', 'Zen Mode']


#List of moves by type to force Z-Crystals to be useful
bug = ['Bug Bite', 'Bug Buzz', 'Defend Order', 'Fell Stinger', 'First Impression', 'Fury Cutter', 'Heal Order', 'Hidden Power Bug', 'Infestation', 'Leech Life', 'Lunge', 'Megahorn', 'Pin Missile', 'Pollen Puff', 'Powder', 'Quiver Dance', 'Rage Powder', 'Signal Beam', 'Silver Wind', 'Spider Web', 'Sticky Web', 'Steamroller', 'String Shot', 'Struggle Bug', 'Tail Glow', 'Twineedle', 'U-turn', 'X-Scissor']
dark = ['Assurance', 'Beat Up', 'Bite', 'Brutal Swing', 'Crunch', 'Dark Pulse', 'Dark Void', 'Darkest Lariat', 'Embargo', 'Feint Attack', 'Fake Tears', 'Flatter', 'Fling', 'Foul Play', 'Hidden Power Dark', 'Hone Claws', 'Hyperspace Fury', 'Knock Off', 'Memento', 'Nasty Plot', 'Night Daze', 'Night Slash', 'Parting Shot', 'Payback', 'Power Trip', 'Punishment', 'Pursuit', 'Quash', 'Snarl', 'Snatch', 'Sucker Punch', 'Switcheroo', 'Taunt', 'Thief', 'Throat Chop', 'Topsy-Turvy', 'Torment']
dragon = ['Clanging Scales', 'Core Enforcer', 'Draco Meteor', 'Dragon Breath', 'Dragon Claw', 'Dragon Dance', 'Dragon Hammer', 'Dragon Pulse', 'Dragon Rage', 'Dragon Rush', 'Dragon Tail', 'Dual Chop', 'Hidden Power Dragon', 'Outrage', 'Roar of Time', 'Spacial Rend', 'Twister']
elec = ['Bolt Strike', 'Charge', 'Charge Beam', 'Discharge', 'Eerie Impulse', 'Electric Terrain', 'Electrify', 'Electro Ball', 'Electroweb', 'Fusion Bolt', 'Hidden Power Electric', 'Ion Deluge', 'Magnetic Flux', 'Magnet Rise', 'Nuzzle', 'Parabolic Charge', 'Plasma Fists', 'Shock Wave', 'Spark', 'Thunder', 'Thunder Fang', 'Thunder Punch', 'Thunder Shock', 'Thunder Wave', 'Thunderbolt', 'Volt Switch', 'Volt Tackle', 'Wild Charge', 'Zap Cannon', 'Zing Zap']
fai = ['Aromatic Mist', 'Baby-Doll Eyes', 'Charm', 'Crafty Shield', 'Dazzling Gleam', 'Disarming Voice', 'Draining Kiss', 'Fairy Lock', 'Fairy Wind', 'Fleur Cannon', 'Floral Healing', 'Flower Shield', 'Geomancy', 'Light of Ruin', 'Misty Terrain', 'Moonblast', 'Moonlight', "Nature's Madness", 'Play Rough', 'Sweet Kiss']
fight = ['Arm Thrust', 'Aura Sphere', 'Brick Break', 'Bulk Up', 'Circle Throw', 'Close Combat', 'Counter', 'Cross Chop', 'Detect', 'Double Kick', 'Drain Punch', 'Dynamic Punch', 'Final Gambit', 'Flying Press', 'Focus Blast', 'Focus Punch', 'Force Palm', 'Hammer Arm', 'Hidden Power Fighting', 'High Jump Kick', 'Jump Kick', 'Karate Chop', 'Low Kick', 'Low Sweep', 'Mach Punch', 'Mat Block', 'Power-Up Punch', 'Quick Guard', 'Revenge', 'Reversal', 'Rock Smash', 'Rolling Kick', 'Sacred Sword', 'Secret Sword', 'Seismic Toss', 'Sky Uppercut', 'Storm Throw', 'Submission', 'Superpower', 'Triple Kick', 'Vacuum Wave', 'Vital Throw', 'Wake-Up Slap']
fire = ['Blast Burn', 'Blaze Kick', 'Blue Flare', 'Burn Up', 'Ember', 'Eruption', 'Fiery Dance', 'Fire Blast', 'Fire Fang', 'Fire Lash', 'Fire Pledge', 'Fire Punch', 'Fire Spin', 'Flame Burst', 'Flame Charge', 'Flame Wheel', 'Flamethrower', 'Flare Blitz', 'Fusion Flare', 'Heat Crash', 'Heat Wave', 'Hidden Power Fire', 'Incinerate', 'Inferno', 'Lava Plume', 'Magma Storm', 'Mind Blown', 'Mystical Fire', 'Overheat', 'Sacred Fire', 'Searing Shot', 'Shell Trap', 'Sunny Day', 'V-create', 'Will-O-Wisp']
fly = ['Acrobatics', 'Aerial Ace', 'Aeroblast', 'Air Cutter', 'Air Slash', 'Beak Blast', 'Bounce', 'Brave Bird', 'Chatter', 'Defog', 'Dragon Ascent', 'Drill Peck', 'Feather Dance', 'Fly', 'Gust', 'Hidden Power Flying', 'Hurricane', 'Mirror Move', 'Oblivion Wing', 'Peck', 'Pluck', 'Roost', 'Sky Attack', 'Sky Drop', 'Tailwind', 'Wing Attack']
ghost = ['Astonish', 'Confuse Ray', 'Curse', 'Destiny Bond', 'Grudge', 'Hex', 'Hidden Power Ghost', 'Lick', 'Moongeist Beam', 'Night Shade', 'Nightmare', 'Ominous Wind', 'Phantom Force', 'Shadow Ball', 'Shadow Bone', 'Shadow Claw', 'Shadow Force', 'Shadow Punch', 'Shadow Sneak', 'Spectral Thief', 'Spirit Shackle', 'Spite', 'Trick-or-Treat']
grass = ['Absorb', 'Aromatherapy', 'Bullet Seed', 'Cotton Guard', 'Cotton Spore', 'Energy Ball', "Forest's Curse", 'Frenzy Plant', 'Giga Drain', 'Grass Knot', 'Grass Pledge', 'Grass Whistle', 'Grassy Terrain', 'Hidden Power Grass', 'Horn Leech', 'Ingrain', 'Leaf Blade', 'Leaf Storm', 'Leaf Tornado', 'Leafage', 'Leech Seed', 'Magical Leaf', 'Mega Drain', 'Needle Arm', 'Petal Blizzard', 'Petal Dance', 'Power Whip', 'Razor Leaf', 'Seed Bomb', 'Seed Flare', 'Sleep Powder', 'Spiky Shield', 'Solar Beam', 'Solar Blade', 'Spore', 'Strength Sap', 'Stun Spore', 'Synthesis', 'Trop Kick', 'Vine Whip', 'Wood Hammer', 'Worry Seed']
ground = ['Bone Club', 'Bone Rush', 'Bonemerang', 'Bulldoze', 'Dig', 'Drill Run', 'Earth Power', 'Earthquake', 'Fissure', 'Hidden Power Ground', 'High Horsepower', "Land's Wrath", 'Magnitude', 'Mud-Slap', 'Mud Bomb', 'Mud Shot', 'Mud Sport', 'Precipice Blades', 'Rototiller', 'Sand Attack', 'Sand Tomb', 'Shore Up', 'Spikes', 'Stomping Tantrum', 'Thousand Arrows', 'Thousand Waves']
ic = ['Aurora Beam', 'Aurora Veil', 'Avalanche', 'Blizzard', 'Freeze-Dry', 'Freeze Shock', 'Frost Breath', 'Glaciate', 'Hail', 'Haze', 'Hidden Power Ice', 'Ice Ball', 'Ice Beam', 'Ice Burn', 'Ice Fang', 'Ice Hammer', 'Ice Punch', 'Ice Shard', 'Icicle Crash', 'Icicle Spear', 'Icy Wind', 'Mist', 'Powder Snow', 'Sheer Cold']
norm = ['Acupressure', 'After You', 'Assist', 'Attract', 'Barrage', 'Baton Pass', 'Belly Drum', 'Bestow', 'Bide', 'Bind', 'Block', 'Body Slam', 'Boomburst', 'Camouflage', 'Captivate', 'Celebrate', 'Chip Away', 'Comet Punch', 'Confide', 'Constrict', 'Conversion', 'Conversion 2', 'Copycat', 'Covet', 'Crush Claw', 'Crush Grip', 'Cut', 'Defense Curl', 'Disable', 'Dizzy Punch', 'Double-Edge', 'Double Hit', 'Double Slap', 'Double Team', 'Echoed Voice', 'Egg Bomb', 'Encore', 'Endeavor', 'Endure', 'Entrainment', 'Explosion', 'Extreme Speed', 'Facade', 'Fake Out', 'False Swipe', 'Feint', 'Flail', 'Flash', 'Focus Energy', 'Follow Me', 'Foresight', 'Frustration', 'Fury Attack', 'Fury Swipes', 'Giga Impact', 'Glare', 'Growl', 'Growth', 'Guillotine', 'Happy Hour', 'Harden', 'Head Charge', 'Headbutt', 'Heal Bell', 'Helping Hand', 'Hidden Power', 'Hold Back', 'Hold Hands', 'Horn Attack', 'Horn Drill', 'Howl', 'Hyper Beam', 'Hyper Fang', 'Hyper Voice', 'Judgment', 'Laser Focus', 'Last Resort', 'Leer', 'Lock-On', 'Lovely Kiss', 'Lucky Chant', 'Me First', 'Mean Look', 'Mega Kick', 'Mega Punch', 'Metronome', 'Milk Drink', 'Mimic', 'Mind Reader', 'Minimize', 'Morning Sun', 'Multi-Attack', 'Natural Gift', 'Nature Power', 'Noble Roar', 'Odor Sleuth', 'Pain Split', 'Pay Day', 'Perish Song', 'Play Nice', 'Pound', 'Present', 'Protect', 'Psych Up', 'Quick Attack', 'Rage', 'Rapid Spin', 'Razor Wind', 'Recover', 'Recycle', 'Reflect Type', 'Refresh', 'Relic Song', 'Retaliate', 'Return', 'Revelation Dance', 'Roar', 'Rock Climb', 'Round', 'Safeguard', 'Scary Face', 'Scratch', 'Screech', 'Secret Power', 'Self-Destruct', 'Sharpen', 'Shell Smash', 'Simple Beam', 'Sing', 'Sketch', 'Skull Bash', 'Slack Off', 'Slam', 'Slash', 'Sleep Talk', 'Smelling Salts', 'Smokescreen', 'Snore', 'Soft-Boiled', 'Sonic Boom', 'Spike Cannon', 'Spit Up', 'Splash', 'Spotlight', 'Stockpile', 'Stomp', 'Strength', 'Struggle', 'Substitute', 'Super Fang', 'Supersonic', 'Swagger', 'Swallow', 'Sweet Scent', 'Swift', 'Swords Dance', 'Tackle', 'Tail Slap', 'Tail Whip', 'Take Down', 'Tearful Look', 'Techno Blast', 'Teeter Dance', 'Thrash', 'Tickle', 'Transform', 'Tri Attack', 'Trump Card', 'Uproar', 'Vice Grip', 'Weather Ball', 'Whirlwind', 'Wish', 'Work Up', 'Wrap', 'Wring Out', 'Yawn']
pois = ['Acid', 'Acid Armor', 'Acid Spray', 'Baneful Bunker', 'Belch', 'Clear Smog', 'Coil', 'Cross Poison', 'Gastro Acid', 'Gunk Shot', 'Hidden Power Poison', 'Poison Fang', 'Poison Gas', 'Poison Jab', 'Poison Powder', 'Poison Sting', 'Poison Tail', 'Purify', 'Sludge', 'Sludge Bomb', 'Sludge Wave', 'Smog', 'Toxic', 'Toxic Spikes', 'Toxic Thread', 'Venom Drench', 'Venoshock']
psy = ['Agility', 'Ally Switch', 'Amnesia', 'Barrier', 'Calm Mind', 'Confusion', 'Cosmic Power', 'Dream Eater', 'Extrasensory', 'Future Sight', 'Gravity', 'Guard Split', 'Guard Swap', 'Heal Block', 'Heal Pulse', 'Healing Wish', 'Heart Stamp', 'Heart Swap', 'Hidden Power Psychic', 'Hyperspace Hole', 'Hypnosis', 'Imprison', 'Instruct', 'Kinesis', 'Light Screen', 'Lunar Dance', 'Luster Purge', 'Magic Coat', 'Magic Room', 'Meditate', 'Miracle Eye', 'Mirror Coat', 'Mist Ball', 'Photon Geyser', 'Power Split', 'Power Swap', 'Power Trick', 'Prismatic Laser', 'Psybeam', 'Psychic', 'Psychic Fangs', 'Psychic Terrain', 'Psycho Boost', 'Psycho Cut', 'Psycho Shift', 'Psyshock', 'Psystrike', 'Psywave', 'Reflect', 'Rest', 'Role Play', 'Skill Swap', 'Speed Swap', 'Stored Power', 'Synchronoise', 'Telekinesis', 'Teleport', 'Trick', 'Trick Room', 'Wonder Room', 'Zen Headbutt']
rock = ['Accelerock', 'Ancient Power', 'Diamond Storm', 'Head Smash', 'Hidden Power Rock', 'Power Gem', 'Rock Blast', 'Rock Polish', 'Rock Slide', 'Rock Throw', 'Rock Tomb', 'Rock Wrecker', 'Rollout', 'Sandstorm', 'Smack Down', 'Stealth Rock', 'Stone Edge', 'Wide Guard']
stel = ['Anchor Shot', 'Autotomize', 'Bullet Punch', 'Doom Desire', 'Flash Cannon', 'Gear Grind', 'Gear Up', 'Gyro Ball', 'Heavy Slam', 'Hidden Power Steel', 'Iron Defense', 'Iron Head', 'Iron Tail', "King's Shield", 'Magnet Bomb', 'Metal Burst', 'Metal Claw', 'Metal Sound', 'Meteor Mash', 'Mirror Shot', 'Shift Gear', 'Smart Strike', 'Steel Wing']
wat = ['Aqua Jet', 'Aqua Ring', 'Aqua Tail', 'Brine', 'Bubble', 'Bubble Beam', 'Clamp', 'Crabhammer', 'Dive', 'Hidden Power Water', 'Hydro Cannon', 'Hydro Pump', 'Liquidation', 'Muddy Water', 'Octazooka', 'Origin Pulse', 'Rain Dance', 'Razor Shell', 'Scald', 'Soak', 'Sparkling Aria', 'Steam Eruption', 'Surf', 'Water Gun', 'Water Pledge', 'Water Pulse', 'Water Sport', 'Water Spout', 'Waterfall', 'Water Shuriken', 'Whirlpool', 'Withdraw']

#List of moves by tier
tier1m = ['Accelerock', 'Acid Spray', 'Acrobatics', 'Aeroblast', 'Agility', 'Air Slash', 'Anchor Shot', 'Aqua Jet', 'Aqua Tail', 'Aromatherapy', 'Attack Order', 'Aura Sphere', 'Aurora Veil', 'Autotomize', 'Avalanche', 'Baneful Bunker', 'Baton Pass', 'Beak Blast', 'Blaze Kick', 'Blue Flare', 'Body Slam', 'Bolt Strike', 'Bonemerang', 'Boomburst', 'Brave Bird', 'Brick Break', 'Bug Buzz', 'Bulk Up', 'Bullet Punch', 'Bullet Seed', 'Calm Mind', 'Chatter', 'Circle Throw', 'Clanging Scales', 'Clear Smog', 'Close Combat', 'Coil', 'Core Enforcer', 'Cotton Guard', 'Crabhammer', 'Cross Chop', 'Crunch', 'Darkest Lariat', 'Dark Pulse', 'Dark Void', 'Dazzling Gleam', 'Defend Order', 'Defog', 'Destiny Bond', 'Detect', 'Diamond Storm', 'Disable', 'Discharge', 'Double-Edge', 'Draco Meteor', 'Dragon Ascent', 'Dragon Claw', 'Dragon Dance', 'Dragon Hammer', 'Dragon Pulse', 'Dragon Tail', 'Drain Punch', 'Drill Peck', 'Drill Run', 'Earth Power', 'Earthquake', 'Encore', 'Endeavor', 'Energy Ball', 'Eruption', 'Explosion', 'Extrasensory', 'Extreme Speed', 'Facade', 'Fake Out', 'Fiery Dance', 'Final Gambit', 'Fire Blast', 'Fire Fang', 'Fire Lash', 'Fire Punch', 'First Impression', 'Flame Charge', 'Flamethrower', 'Flare Blitz', 'Flash Cannon', 'Fleur Cannon', 'Focus Blast', 'Focus Punch', 'Foul Play', 'Freeze-Dry', 'Frustration', 'Fusion Bolt', 'Fusion Flare', 'Gear Grind', 'Geomancy', 'Giga Drain', 'Glare', 'Grass Knot', 'Gunk Shot', 'Hammer Arm', 'Haze', 'Head Charge', 'Head Smash', 'Heal Bell', 'Healing Wish', 'Heal Order', 'Heat Wave', 'Heavy Slam', 'Hex', 'High Jump Kick', 'Hone Claws', 'Horn Leech', 'Hurricane', 'Hydro Pump', 'Hyperspace Fury', 'Hyper Voice', 'Ice Beam', 'Ice Fang', 'Ice Hammer', 'Ice Punch', 'Ice Shard', 'Icicle Crash', 'Icicle Spear', 'Iron Head', 'Judgment', "King's Shield", 'Knock Off', 'Lava Plume', 'Leaf Blade', 'Leaf Storm', 'Leech Life', 'Leech Seed', 'Light of Ruin', 'Light Screen', 'Liquidation', 'Lovely Kiss', 'Low Kick', 'Lunar Dance', 'Lunge', 'Mach Punch', 'Magic Coat', 'Magma Storm', 'Megahorn', 'Memento', 'Meteor Mash', 'Milk Drink', 'Mind Blown', 'Moonblast', 'Moongeist Beam', 'Moonlight', 'Morning Sun', 'Multi-Attack', 'Nasty Plot', 'Nature Power', "Nature's Madness", 'Night Shade', 'Night Slash', 'Nuzzle', 'Oblivion Wing', 'Origin Pulse', 'Outrage', 'Overheat', 'Pain Split', 'Parting Shot', 'Perish Song', 'Petal Blizzard', 'Photon Geyser', 'Plasma Fists', 'Play Rough', 'Poison Jab', 'Power Gem', 'Power-Up Punch', 'Power Whip', 'Precipice Blades', 'Protect', 'Psychic', 'Psychic Fangs', 'Psycho Boost', 'Psycho Cut', 'Psyshock', 'Psystrike', 'Pursuit', 'Quick Attack', 'Quiver Dance', 'Rapid Spin', 'Razor Shell', 'Recover', 'Reflect', 'Refresh', 'Relic Song', 'Rest', 'Return', 'Revelation Dance', 'Roar', 'Rock Blast', 'Rock Polish', 'Rock Slide', 'Roost', 'Sacred Fire', 'Sacred Sword', 'Scald', 'Searing Shot', 'Secret Sword', 'Seed Bomb', 'Seed Flare', 'Seismic Toss', 'Shadow Ball', 'Shadow Bone', 'Shadow Claw', 'Shadow Force', 'Shadow Punch', 'Shadow Sneak', 'Shell Smash', 'Shift Gear', 'Shore Up', 'Signal Beam', 'Slack Off', 'Sleep Powder', 'Sleep Talk', 'Sludge Bomb', 'Sludge Wave', 'Soft-Boiled', 'Spacial Rend', 'Spectral Thief', 'Spikes', 'Spiky Shield', 'Spirit Shackle', 'Spore', 'Stealth Rock', 'Steam Eruption', 'Sticky Web', 'Stone Edge', 'Storm Throw', 'Strength Sap', 'Substitute', 'Sucker Punch', 'Sunsteel Strike', 'Super Fang', 'Superpower', 'Surf', 'Switcheroo', 'Swords Dance', 'Synthesis', 'Tail Glow', 'Tail Slap', 'Tailwind', 'Taunt', 'Techno Blast', 'Thousand Arrows', 'Thunderbolt', 'Thunder Punch', 'Thunder Wave', 'Toxic', 'Toxic Spikes', 'Toxic Thread', 'Tri Attack', 'Trick', 'Trick Room', 'U-turn', 'V-create', 'Volt Switch', 'Volt Tackle', 'Waterfall', 'Water Shuriken', 'Water Spout', 'Whirlwind', 'Wild Charge', 'Will-O-Wisp', 'Wish', 'Wood Hammer', 'X-Scissor', 'Zen Headbutt', 'Zing Zap']
tier2m = ['Absorb', 'Acid', 'Acid Armor', 'Acupressure', 'Aerial Ace', 'After You', 'Air Cutter', 'Ally Switch', 'Amnesia', 'Ancient Power', 'Aqua Ring', 'Arm Thrust', 'Aromatic Mist', 'Assist', 'Assurance', 'Astonish', 'Attract', 'Aurora Beam', 'Baby-Doll Eyes', 'Barrage', 'Barrier', 'Beat Up', 'Belch', 'Belly Drum', 'Bestow', 'Bide', 'Bind', 'Bite', 'Blast Burn', 'Blizzard', 'Block', 'Bone Club', 'Bone Rush', 'Bounce', 'Brine', 'Brutal Swing', 'Bubble', 'Bubble Beam', 'Bug Bite', 'Bulldoze', 'Burn Up', 'Camouflage', 'Captivate', 'Celebrate', 'Charge', 'Charge Beam', 'Charm', 'Chip Away', 'Clamp', 'Comet Punch', 'Confide', 'Confuse Ray', 'Confusion', 'Constrict', 'Conversion', 'Conversion 2', 'Copycat', 'Cosmic Power', 'Cotton Spore', 'Counter', 'Covet', 'Crafty Shield', 'Cross Poison', 'Crush Claw', 'Crush Grip', 'Curse', 'Cut', 'Defense Curl', 'Dig', 'Disarming Voice', 'Dive', 'Dizzy Punch', 'Doom Desire', 'Double Hit', 'Double Kick', 'Double Slap', 'Double Team', 'Dragon Breath', 'Dragon Rage', 'Dragon Rush', 'Draining Kiss', 'Dream Eater', 'Dual Chop', 'Dynamic Punch', 'Echoed Voice', 'Eerie Impulse', 'Egg Bomb', 'Electric Terrain', 'Electrify', 'Electro Ball', 'Electroweb', 'Embargo', 'Ember', 'Endure', 'Entrainment', 'Fairy Lock', 'Fairy Wind', 'Fake Tears', 'False Swipe', 'Feather Dance', 'Feint', 'Feint Attack', 'Fell Stinger', 'Fire Pledge', 'Fire Spin', 'Fissure', 'Flail', 'Flame Burst', 'Flame Wheel', 'Flash', 'Flatter', 'Fling', 'Floral Healing', 'Flower Shield', 'Fly', 'Flying Press', 'Focus Energy', 'Follow Me', 'Force Palm', 'Foresight', "Forest's Curse", 'Freeze Shock', 'Frenzy Plant', 'Frost Breath', 'Fury Attack', 'Fury Cutter', 'Fury Swipes', 'Future Sight', 'Gastro Acid', 'Gear Up', 'Giga Impact', 'Glaciate', 'Grass Pledge', 'Grass Whistle', 'Grassy Terrain', 'Gravity', 'Growl', 'Growth', 'Grudge', 'Guard Split', 'Guard Swap', 'Guillotine', 'Gust', 'Gyro Ball', 'Hail', 'Happy Hour', 'Harden', 'Headbutt', 'Heal Block', 'Heal Pulse', 'Heart Stamp', 'Heart Swap', 'Heat Crash', 'Helping Hand', 'Hidden Power', 'Hidden Power Bug', 'Hidden Power Dark', 'Hidden Power Dragon', 'Hidden Power Electric', 'Hidden Power Fighting', 'Hidden Power Fire', 'Hidden Power Flying', 'Hidden Power Ghost', 'Hidden Power Grass', 'Hidden Power Ground', 'Hidden Power Ice', 'Hidden Power Poison', 'Hidden Power Psychic', 'Hidden Power Rock', 'Hidden Power Steel', 'Hidden Power Water', 'High Horsepower', 'Hold Back', 'Hold Hands', 'Horn Attack', 'Horn Drill', 'Howl', 'Hydro Cannon', 'Hyper Beam', 'Hyper Fang', 'Hyperspace Hole', 'Hypnosis', 'Ice Ball', 'Ice Burn', 'Icy Wind', 'Imprison', 'Incinerate', 'Inferno', 'Infestation', 'Ingrain', 'Instruct', 'Ion Deluge', 'Iron Defense', 'Iron Tail', 'Jump Kick', 'Karate Chop', 'Kinesis', "Land's Wrath", 'Laser Focus', 'Last Resort', 'Leafage', 'Leaf Tornado', 'Leer', 'Lick', 'Lock-On', 'Low Sweep', 'Lucky Chant', 'Luster Purge', 'Magical Leaf', 'Magic Room', 'Magnet Bomb', 'Magnetic Flux', 'Magnet Rise', 'Magnitude', 'Mat Block', 'Mean Look', 'Meditate', 'Me First', 'Mega Drain', 'Mega Kick', 'Mega Punch', 'Metal Burst', 'Metal Claw', 'Metal Sound', 'Metronome', 'Mimic', 'Mind Reader', 'Minimize', 'Miracle Eye', 'Mirror Coat', 'Mirror Move', 'Mirror Shot', 'Mist', 'Mist Ball', 'Misty Terrain', 'Mud Bomb', 'Muddy Water', 'Mud Shot', 'Mud-Slap', 'Mud Sport', 'Mystical Fire', 'Natural Gift', 'Needle Arm', 'Night Daze', 'Nightmare', 'Noble Roar', 'Octazooka', 'Odor Sleuth', 'Ominous Wind', 'Parabolic Charge', 'Payback', 'Pay Day', 'Peck', 'Petal Dance', 'Phantom Force', 'Pin Missile', 'Play Nice', 'Pluck', 'Poison Fang', 'Poison Gas', 'Poison Powder', 'Poison Sting', 'Poison Tail', 'Pollen Puff', 'Pound', 'Powder', 'Powder Snow', 'Power Split', 'Power Swap', 'Power Trick', 'Power Trip', 'Present', 'Prismatic Laser', 'Psybeam', 'Psychic Terrain', 'Psycho Shift', 'Psych Up', 'Psywave', 'Punishment', 'Purify', 'Quash', 'Quick Guard', 'Rage', 'Rage Powder', 'Rain Dance', 'Razor Leaf', 'Razor Wind', 'Recycle', 'Reflect Type', 'Retaliate', 'Revenge', 'Reversal', 'Roar of Time', 'Rock Climb', 'Rock Smash', 'Rock Throw', 'Rock Tomb', 'Rock Wrecker', 'Role Play', 'Rolling Kick', 'Rollout', 'Rototiller', 'Round', 'Safeguard', 'Sand Attack', 'Sandstorm', 'Sand Tomb', 'Scary Face', 'Scratch', 'Screech', 'Secret Power', 'Self-Destruct', 'Sharpen', 'Sheer Cold', 'Shell Trap', 'Shock Wave', 'Silver Wind', 'Simple Beam', 'Sing', 'Sketch', 'Skill Swap', 'Skull Bash', 'Sky Attack', 'Sky Drop', 'Sky Uppercut', 'Slam', 'Slash', 'Sludge', 'Smack Down', 'Smart Strike', 'Smelling Salts', 'Smog', 'Smokescreen', 'Snarl', 'Snatch', 'Snore', 'Soak', 'Solar Beam', 'Solar Blade', 'Sonic Boom', 'Spark', 'Sparkling Aria', 'Speed Swap', 'Spider Web', 'Spike Cannon', 'Spite', 'Spit Up', 'Splash', 'Spotlight', 'Steamroller', 'Steel Wing', 'Stockpile', 'Stomp', 'Stomping Tantrum', 'Stored Power', 'Strength', 'String Shot', 'Struggle', 'Struggle Bug', 'Stun Spore', 'Submission', 'Sunny Day', 'Supersonic', 'Swagger', 'Swallow', 'Sweet Kiss', 'Sweet Scent', 'Swift', 'Synchronoise', 'Tackle', 'Tail Whip', 'Take Down', 'Tearful Look', 'Teeter Dance', 'Telekinesis', 'Teleport', 'Thief', 'Thousand Waves', 'Thrash', 'Throat Chop', 'Thunder', 'Thunder Fang', 'Thunder Shock', 'Tickle', 'Topsy-Turvy', 'Torment', 'Transform', 'Trick-or-Treat', 'Triple Kick', 'Trop Kick', 'Trump Card', 'Twineedle', 'Twister', 'Uproar', 'Vacuum Wave', 'Venom Drench', 'Venoshock', 'Vice Grip', 'Vine Whip', 'Vital Throw', 'Wake-Up Slap', 'Water Gun', 'Water Pledge', 'Water Pulse', 'Water Sport', 'Weather Ball', 'Whirlpool', 'Wide Guard', 'Wing Attack', 'Withdraw', 'Wonder Room', 'Work Up', 'Worry Seed', 'Wrap', 'Wring Out', 'Yawn', 'Zap Cannon']

#List of useless items
useless = ["Armor Fossil", "Beast Ball", "Belue Berry", "Bluk Berry", "Cherish Ball", "Claw Fossil", "Cornn Berry", "Cover Fossil", "Dawn Stone", "Dive Ball", "Dome Fossil", "Dragon Scale", "Dream Ball", "Dubious Disc", "Durin Berry", "Dusk Ball", "Dusk Stone", "Electirizer", "Energy Powder", "Fast Ball", "Fire Stone", "Friend Ball", "Great Ball", "Heal Ball", "Heavy Ball", "Helix Fossil", "Hondew Berry", "Ice Stone", "Jaw Fossil", "Leaf Stone", "Level Ball", "Love Ball", "Lure Ball", "Luxury Ball", "Magmarizer", "Magost Berry", "Master Ball", "Moon Ball", "Moon Stone", "Nanab Berry", "Nest Ball", "Net Ball", "Nomel Berry", "Old Amber", "Oval Stone", "Pamtre Berry", "Park Ball", "Pinap Berry", "Plume Fossil", "Poke Ball", "Pomeg Berry", "Premier Ball", "Prism Scale", "Protector", "Qualot Berry", "Quick Ball", "Rabuta Berry", "Rare Bone", "Razz Berry", "Reaper Cloth", "Repeat Ball", "Root Fossil", "Sachet", "Safari Ball", "Sail Fossil", "Shiny Stone", "Skull Fossil", "Spelon Berry", "Sport Ball", "Sun Stone", "Tamato Berry", "Thunder Stone", "Timer Ball", "Ultra Ball", "Up-Grade", "Water Stone", "Watmel Berry", "Wepear Berry", "Whipped Dream"]

#List of Z-moves by type
sig_z = ["10,000,000 Volt Thunderbolt", "Catastropika", "Genesis Supernova", "Guardian of Alola", "Clangorous Soulblaze", "Malicious Moonsault", "Oceanic Operetta", "Pulverizing Pancake", "Sinister Arrow Raid", "Soul-Stealing 7-Star Strike", "Stoked Sparksurfer"]
bad_z = ["Acid Downpour", "All-Out Pummeling", "Black Hole Eclipse", "Bloom Doom", "Breakneck Blitz", "Continental Crush", "Corkscrew Crash", "Devastating Drake", "Extreme Evoboost", "Gigavolt Havoc", "Hydro Vortex", "Inferno Overdrive", "Never-Ending Nightmare", "Pulverizing Pancake", "Savage Spin-Out", "Shattered Psyche", "Subzero Slammer", "Supersonic Skystrike", "Tectonic Rage", "Twinkle Tackle"]
all_z = ['10,000,000 Volt Thunderbolt', 'Catastropika', 'Genesis Supernova', 'Guardian of Alola', 'Malicious Moonsault', 'Oceanic Operetta', 'Pulverizing Pancake', 'Sinister Arrow Raid', 'Soul-Stealing 7-Star Strike', 'Stoked Sparksurfer', 'Acid Downpour', 'All-Out Pummeling', 'Black Hole Eclipse', 'Bloom Doom', 'Breakneck Blitz', 'Continental Crush', 'Corkscrew Crash', 'Devastating Drake', 'Extreme Evoboost', 'Gigavolt Havoc', 'Hydro Vortex', 'Inferno Overdrive', 'Never-Ending Nightmare', 'Pulverizing Pancake', 'Savage Spin-Out', 'Shattered Psyche', 'Subzero Slammer', 'Supersonic Skystrike', 'Tectonic Rage', 'Twinkle Tackle']

#Moves which are status and not
statmov = ['Acid Armor', 'Acupressure', 'After You', 'Agility', 'Ally Switch', 'Amnesia', 'Aqua Ring', 'Aromatherapy', 'Aromatic Mist', 'Assist', 'Attract', 'Aurora Veil', 'Autotomize', 'Baby-Doll Eyes', 'Baneful Bunker', 'Barrier', 'Baton Pass', 'Belly Drum', 'Bestow', 'Block', 'Bulk Up', 'Calm Mind', 'Camouflage', 'Captivate', 'Celebrate', 'Charge', 'Charm', 'Coil', 'Confide', 'Confuse Ray', 'Conversion', 'Conversion 2', 'Copycat', 'Cosmic Power', 'Cotton Guard', 'Cotton Spore', 'Crafty Shield', 'Curse', 'Dark Void', 'Defend Order', 'Defense Curl', 'Defog', 'Destiny Bond', 'Detect', 'Disable', 'Double Team', 'Dragon Dance', 'Eerie Impulse', 'Electric Terrain', 'Electrify', 'Embargo', 'Encore', 'Endure', 'Entrainment', 'Fairy Lock', 'Fake Tears', 'Feather Dance', 'Flash', 'Flatter', 'Floral Healing', 'Flower Shield', 'Focus Energy', 'Follow Me', 'Foresight', "Forest's Curse", 'Gastro Acid', 'Gear Up', 'Geomancy', 'Glare', 'Grass Whistle', 'Grassy Terrain', 'Gravity', 'Growl', 'Growth', 'Grudge', 'Guard Split', 'Guard Swap', 'Hail', 'Happy Hour', 'Harden', 'Haze', 'Heal Bell', 'Heal Block', 'Heal Order', 'Heal Pulse', 'Healing Wish', 'Heart Swap', 'Helping Hand', 'Hold Hands', 'Hone Claws', 'Howl', 'Hypnosis', 'Imprison', 'Ingrain', 'Instruct', 'Ion Deluge', 'Iron Defense', 'Kinesis', "King's Shield", 'Laser Focus', 'Leech Seed', 'Leer', 'Light Screen', 'Lock-On', 'Lovely Kiss', 'Lucky Chant', 'Lunar Dance', 'Magic Coat', 'Magic Room', 'Magnetic Flux', 'Magnet Rise', 'Mat Block', 'Me First', 'Mean Look', 'Meditate', 'Memento', 'Metal Sound', 'Metronome', 'Milk Drink', 'Mimic', 'Mind Reader', 'Minimize', 'Miracle Eye', 'Mirror Move', 'Mist', 'Misty Terrain', 'Moonlight', 'Morning Sun', 'Mud Sport', 'Nasty Plot', 'Nature Power', 'Nightmare', 'Noble Roar', 'Odor Sleuth', 'Pain Split', 'Parting Shot', 'Perish Song', 'Play Nice', 'Poison Gas', 'Poison Powder', 'Powder', 'Power Split', 'Power Swap', 'Power Trick', 'Protect', 'Psych Up', 'Psychic Terrain', 'Psycho Shift', 'Purify', 'Quash', 'Quick Guard', 'Quiver Dance', 'Rage Powder', 'Rain Dance', 'Recover', 'Recycle', 'Reflect', 'Reflect Type', 'Refresh', 'Rest', 'Roar', 'Rock Polish', 'Role Play', 'Roost', 'Rototiller', 'Safeguard', 'Sand Attack', 'Sandstorm', 'Scary Face', 'Screech', 'Sharpen', 'Shell Smash', 'Shift Gear', 'Shore Up', 'Simple Beam', 'Sing', 'Sketch', 'Skill Swap', 'Slack Off', 'Sleep Powder', 'Sleep Talk', 'Smokescreen', 'Snatch', 'Speed Swap', 'Spiky Shield', 'Soak', 'Soft-Boiled', 'Spider Web', 'Spikes', 'Spite', 'Splash', 'Spore', 'Spotlight', 'Stealth Rock', 'Sticky Web', 'Stockpile', 'Strength Sap', 'String Shot', 'Stun Spore', 'Substitute', 'Sunny Day', 'Supersonic', 'Swagger', 'Swallow', 'Sweet Kiss', 'Sweet Scent', 'Switcheroo', 'Swords Dance', 'Synthesis', 'Tail Glow', 'Tail Whip', 'Tailwind', 'Taunt', 'Tearful Look', 'Teeter Dance', 'Telekinesis', 'Teleport', 'Thunder Wave', 'Tickle', 'Topsy-Turvy', 'Torment', 'Toxic', 'Toxic Spikes', 'Toxic Thread', 'Transform', 'Trick', 'Trick-or-Treat', 'Trick Room', 'Venom Drench', 'Water Sport', 'Whirlwind', 'Wide Guard', 'Will-O-Wisp', 'Wish', 'Withdraw', 'Wonder Room', 'Work Up', 'Worry Seed', 'Yawn', 'Extreme Evoboost']
notstatmov = ['Absorb', 'Accelerock', 'Acid', 'Acid Spray', 'Acrobatics', 'Aerial Ace', 'Aeroblast', 'Air Cutter', 'Air Slash', 'Anchor Shot', 'Ancient Power', 'Aqua Jet', 'Aqua Tail', 'Arm Thrust', 'Assurance', 'Astonish', 'Attack Order', 'Aura Sphere', 'Aurora Beam', 'Avalanche', 'Barrage', 'Beak Blast', 'Beat Up', 'Belch', 'Bide', 'Bind', 'Bite', 'Blast Burn', 'Blaze Kick', 'Blizzard', 'Blue Flare', 'Body Slam', 'Bolt Strike', 'Bone Club', 'Bone Rush', 'Bonemerang', 'Boomburst', 'Bounce', 'Brave Bird', 'Brick Break', 'Brine', 'Brutal Swing', 'Bubble', 'Bubble Beam', 'Bug Bite', 'Bug Buzz', 'Bulldoze', 'Bullet Punch', 'Bullet Seed', 'Burn Up', 'Charge Beam', 'Chatter', 'Chip Away', 'Circle Throw', 'Clamp', 'Clanging Scales', 'Clear Smog', 'Close Combat', 'Comet Punch', 'Confusion', 'Constrict', 'Core Enforcer', 'Counter', 'Covet', 'Crabhammer', 'Cross Chop', 'Cross Poison', 'Crunch', 'Crush Claw', 'Crush Grip', 'Cut', 'Dark Pulse', 'Darkest Lariat', 'Dazzling Gleam', 'Diamond Storm', 'Dig', 'Disarming Voice', 'Discharge', 'Dive', 'Dizzy Punch', 'Doom Desire', 'Double-Edge', 'Double Hit', 'Double Kick', 'Double Slap', 'Draco Meteor', 'Dragon Ascent', 'Dragon Breath', 'Dragon Claw', 'Dragon Hammer', 'Dragon Pulse', 'Dragon Rage', 'Dragon Rush', 'Dragon Tail', 'Draining Kiss', 'Drain Punch', 'Dream Eater', 'Drill Peck', 'Drill Run', 'Dual Chop', 'Dynamic Punch', 'Earth Power', 'Earthquake', 'Echoed Voice', 'Egg Bomb', 'Electro Ball', 'Electroweb', 'Ember', 'Endeavor', 'Energy Ball', 'Eruption', 'Explosion', 'Extrasensory', 'Extreme Speed', 'Facade', 'Feint Attack', 'Fairy Wind', 'Fake Out', 'False Swipe', 'Feint', 'Fell Stinger', 'Fiery Dance', 'Final Gambit', 'Fire Blast', 'Fire Fang', 'Fire Lash', 'Fire Pledge', 'Fire Punch', 'Fire Spin', 'First Impression', 'Fissure', 'Flail', 'Flame Burst', 'Flame Charge', 'Flame Wheel', 'Flamethrower', 'Flare Blitz', 'Flash Cannon', 'Fleur Cannon', 'Fling', 'Fly', 'Flying Press', 'Focus Blast', 'Focus Punch', 'Force Palm', 'Foul Play', 'Freeze-Dry', 'Freeze Shock', 'Frenzy Plant', 'Frost Breath', 'Frustration', 'Fury Attack', 'Fury Cutter', 'Fury Swipes', 'Fusion Bolt', 'Fusion Flare', 'Future Sight', 'Gear Grind', 'Giga Drain', 'Giga Impact', 'Glaciate', 'Grass Knot', 'Grass Pledge', 'Guillotine', 'Gunk Shot', 'Gust', 'Gyro Ball', 'Hammer Arm', 'Head Charge', 'Head Smash', 'Headbutt', 'Heart Stamp', 'Heat Crash', 'Heat Wave', 'Heavy Slam', 'Hex', 'Hidden Power', 'Hidden Power Bug', 'Hidden Power Dark', 'Hidden Power Dragon', 'Hidden Power Electric', 'Hidden Power Fighting', 'Hidden Power Fire', 'Hidden Power Flying', 'Hidden Power Ghost', 'Hidden Power Grass', 'Hidden Power Ground', 'Hidden Power Ice', 'Hidden Power Poison', 'Hidden Power Psychic', 'Hidden Power Rock', 'Hidden Power Steel', 'Hidden Power Water', 'High Horsepower', 'High Jump Kick', 'Hold Back', 'Horn Attack', 'Horn Drill', 'Horn Leech', 'Hurricane', 'Hydro Cannon', 'Hydro Pump', 'Hyper Beam', 'Hyper Fang', 'Hyperspace Fury', 'Hyperspace Hole', 'Hyper Voice', 'Ice Ball', 'Ice Beam', 'Ice Burn', 'Ice Fang', 'Ice Hammer', 'Ice Punch', 'Ice Shard', 'Icicle Crash', 'Icicle Spear', 'Icy Wind', 'Incinerate', 'Inferno', 'Infestation', 'Iron Head', 'Iron Tail', 'Judgment', 'Jump Kick', 'Karate Chop', 'Knock Off', "Land's Wrath", 'Last Resort', 'Lava Plume', 'Leaf Blade', 'Leaf Storm', 'Leaf Tornado', 'Leafage', 'Leech Life', 'Lick', 'Light of Ruin', 'Liquidation', 'Low Kick', 'Low Sweep', 'Lunge', 'Luster Purge', 'Mach Punch', 'Magical Leaf', 'Magma Storm', 'Magnet Bomb', 'Magnitude', 'Mega Drain', 'Mega Kick', 'Mega Punch', 'Megahorn', 'Metal Burst', 'Metal Claw', 'Meteor Mash', 'Mind Blown', 'Mirror Coat', 'Mirror Shot', 'Mist Ball', 'Moonblast', 'Moongeist Beam', 'Mud-Slap', 'Mud Bomb', 'Mud Shot', 'Muddy Water', 'Multi-Attack', 'Mystical Fire', 'Natural Gift', "Nature's Madness", 'Needle Arm', 'Night Daze', 'Night Shade', 'Night Slash', 'Nuzzle', 'Oblivion Wing', 'Octazooka', 'Ominous Wind', 'Origin Pulse', 'Outrage', 'Overheat', 'Parabolic Charge', 'Pay Day', 'Payback', 'Peck', 'Petal Blizzard', 'Petal Dance', 'Phantom Force', 'Photon Geyser', 'Pin Missile', 'Plasma Fists', 'Play Rough', 'Pluck', 'Poison Fang', 'Poison Jab', 'Poison Sting', 'Poison Tail', 'Pollen Puff', 'Pound', 'Powder Snow', 'Power Gem', 'Power Trip', 'Power-Up Punch', 'Power Whip', 'Precipice Blades', 'Present', 'Prismatic Laser', 'Psybeam', 'Psychic', 'Psychic Fangs', 'Psycho Boost', 'Psycho Cut', 'Psyshock', 'Psystrike', 'Psywave', 'Punishment', 'Pursuit', 'Quick Attack', 'Rage', 'Rapid Spin', 'Razor Leaf', 'Razor Shell', 'Razor Wind', 'Relic Song', 'Retaliate', 'Return', 'Revelation Dance', 'Revenge', 'Reversal', 'Roar of Time', 'Rock Blast', 'Rock Climb', 'Rock Slide', 'Rock Smash', 'Rock Throw', 'Rock Tomb', 'Rock Wrecker', 'Rolling Kick', 'Rollout', 'Round', 'Sacred Fire', 'Sacred Sword', 'Sand Tomb', 'Scald', 'Scratch', 'Searing Shot', 'Secret Power', 'Secret Sword', 'Seed Bomb', 'Seed Flare', 'Seismic Toss', 'Self-Destruct', 'Shadow Ball', 'Shadow Bone', 'Shadow Claw', 'Shadow Force', 'Shadow Punch', 'Shadow Sneak', 'Sheer Cold', 'Shell Trap', 'Shock Wave', 'Signal Beam', 'Silver Wind', 'Skull Bash', 'Sky Attack', 'Sky Drop', 'Sky Uppercut', 'Slam', 'Slash', 'Sludge', 'Sludge Bomb', 'Sludge Wave', 'Smack Down', 'Smart Strike', 'Smelling Salts', 'Smog', 'Snarl', 'Snore', 'Spectral Thief', 'Spirit Shackle', 'Solar Beam', 'Solar Blade', 'Sonic Boom', 'Spacial Rend', 'Spark', 'Sparkling Aria', 'Spike Cannon', 'Spit Up', 'Steam Eruption', 'Steel Wing', 'Stomp', 'Stomping Tantrum', 'Stone Edge', 'Stored Power', 'Storm Throw', 'Steamroller', 'Strength', 'Struggle', 'Struggle Bug', 'Submission', 'Sucker Punch', 'Sunsteel Strike', 'Super Fang', 'Superpower', 'Surf', 'Swift', 'Synchronoise', 'Tackle', 'Tail Slap', 'Take Down', 'Techno Blast', 'Thief', 'Thousand Arrows', 'Thousand Waves', 'Thrash', 'Throat Chop', 'Thunder', 'Thunder Fang', 'Thunder Punch', 'Thunder Shock', 'Thunderbolt', 'Tri Attack', 'Triple Kick', 'Trop Kick', 'Trump Card', 'Twineedle', 'Twister', 'U-turn', 'Uproar', 'V-create', 'Vacuum Wave', 'Venoshock', 'Vice Grip', 'Vine Whip', 'Vital Throw', 'Volt Switch', 'Volt Tackle', 'Wake-Up Slap', 'Water Gun', 'Water Pledge', 'Water Pulse', 'Water Spout', 'Waterfall', 'Water Shuriken', 'Weather Ball', 'Whirlpool', 'Wild Charge', 'Wing Attack', 'Wood Hammer', 'Wrap', 'Wring Out', 'X-Scissor', 'Zap Cannon', 'Zen Headbutt', 'Zing Zap']

#List of pokemon by smogon's tiers
uber = ['Rayquaza-Mega', 'Aegislash', 'Arceus', 'Arceus-Bug', 'Arceus-Dark', 'Arceus-Dragon', 'Arceus-Electric', 'Arceus-Fairy', 'Arceus-Fighting', 'Arceus-Fire', 'Arceus-Flying', 'Arceus-Ghost', 'Arceus-Grass', 'Arceus-Ground', 'Arceus-Ice', 'Arceus-Poison', 'Arceus-Psychic', 'Arceus-Rock', 'Arceus-Steel', 'Arceus-Water', 'Blaziken', 'Blaziken-Mega', 'Darkrai', 'Deoxys', 'Deoxys-Attack', 'Deoxys-Defense', 'Deoxys-Speed', 'Dialga', 'Genesect', 'Genesect-Burn', 'Genesect-Chill', 'Genesect-Douse', 'Genesect-Shock', 'Gengar-Mega', 'Giratina', 'Giratina-Origin', 'Groudon', 'Groudon-Primal', 'Ho-Oh', 'Kangaskhan-Mega', 'Kyogre', 'Kyogre-Primal', 'Kyurem-White', 'Landorus', 'Lucario-Mega', 'Lugia', 'Lunala', 'Marshadow', 'Metagross-Mega', 'Mewtwo', 'Mewtwo-Mega-X', 'Mewtwo-Mega-Y', 'Naganadel', 'Necrozma-Dawn-Wings', 'Necrozma-Dusk-Mane', 'Necrozma-Ultra', 'Palkia', 'Pheromosa', 'Rayquaza', 'Reshiram', 'Salamence-Mega', 'Shaymin-Sky', 'Solgaleo', 'Xerneas', 'Yveltal', 'Zekrom', 'Zygarde-Complete']
#Uber includes Mega-Rayquaza, for simplicity
ou = ['Zeraora', 'Alakazam-Mega', 'Amoonguss', 'Bisharp', 'Blacephalon', 'Celesteela', 'Chansey', 'Charizard-Mega-X', 'Clefable', 'Diancie-Mega', 'Excadrill', 'Ferrothorn', 'Garchomp', 'Greninja', 'Greninja-Ash', 'Gyarados-Mega', 'Hawlucha', 'Heatran', 'Hoopa-Unbound', 'Jirachi', 'Kartana', 'Keldeo', 'Keldeo-Resolute', 'Kyurem-Black', 'Landorus-Therian', 'Latias-Mega', 'Latios', 'Latios-Mega', 'Lopunny-Mega', 'Magearna', 'Magnezone', 'Mamoswine', 'Mawile-Mega', 'Medicham-Mega', 'Mew', 'Mimikyu', 'Pelipper', 'Pinsir-Mega', 'Rotom-Wash', 'Sableye-Mega', 'Scizor-Mega', 'Skarmory', 'Swampert-Mega', 'Tangrowth', 'Tapu Bulu', 'Tapu Fini', 'Tapu Koko', 'Tapu Lele', 'Tornadus-Therian', 'Toxapex', 'Tyranitar', 'Venusaur-Mega', 'Victini', 'Volcarona', 'Zapdos', 'Zygarde', 'Alakazam', 'Azumarill', 'Buzzwole', 'Charizard-Mega-Y', 'Conkeldurr', 'Diggersby', 'Dragonite', 'Gallade-Mega', 'Gardevoir-Mega', 'Gyarados', 'Heracross-Mega', 'Manaphy', 'Ninetales-Alola', 'Porygon-Z', 'Salamence', 'Scolipede', 'Staraptor', 'Thundurus', 'Thundurus-Therian', 'Weavile', 'Xurkitree', 'Garchomp-Mega', 'Tyranitar-Mega']
uu = ['Aerodactyl-Mega', 'Aggron-Mega', 'Alomomola', 'Altaria-Mega', 'Arcanine', 'Azelf', 'Beedrill-Mega', 'Blissey', 'Breloom', 'Celebi', 'Chandelure', 'Cobalion', 'Crawdaunt', 'Crobat', 'Darmanitan', 'Empoleon', 'Gengar', 'Gliscor', 'Haxorus', 'Heracross', 'Hippowdon', 'Hydreigon', 'Infernape', 'Klefki', 'Kommo-o', 'Krookodile', 'Latias', 'Magneton', 'Manectric-Mega', 'Mantine', 'Marowak-Alola', 'Metagross', 'Muk-Alola', 'Nidoking', 'Nihilego', 'Pidgeot-Mega', 'Primarina', 'Raikou', 'Sceptile-Mega', 'Scizor', 'Seismitoad', 'Serperior', 'Sharpedo-Mega', 'Slowbro-Mega', 'Stakataka', 'Starmie', 'Suicune', 'Swampert', 'Sylveon', 'Tentacruel', 'Terrakion', 'Togekiss', 'Volcanion', 'Absol-Mega', 'Durant', 'Houndoom-Mega', 'Kyurem', 'Lucario', 'Mienshao', 'Reuniclus', 'Sharpedo', 'Talonflame', 'Tornadus', 'Venomoth', 'Zoroark']
ru = ['Aerodactyl', 'Ampharos-Mega', 'Araquanid', 'Banette-Mega', 'Bewear', 'Blastoise-Mega', 'Bronzong', 'Chesnaught', 'Cloyster', 'Cresselia', 'Decidueye', 'Dhelmise', 'Donphan', 'Doublade', 'Dragalge', 'Drapion', 'Emboar', 'Entei', 'Escavalier', 'Espeon', 'Feraligatr', 'Florges', 'Flygon', 'Forretress', 'Galvantula', 'Gardevoir', 'Glalie-Mega', 'Gligar', 'Golisopod', 'Goodra', 'Honchkrow', 'Hoopa', 'Jolteon', 'Linoone', 'Lycanroc-Dusk', 'Machamp', 'Mandibuzz', 'Meloetta', 'Milotic', 'Moltres', 'Necrozma', 'Nidoqueen', 'Pangoro', 'Porygon2', 'Quagsire', 'Registeel', 'Rhyperior', 'Roserade', 'Rotom-Heat', 'Rotom-Mow', 'Salazzle', 'Shaymin', 'Snorlax', 'Steelix-Mega', 'Swellow', 'Tsareena', 'Tyrantrum', 'Umbreon', 'Virizion', 'Yanmega', 'Zygarde-10%', 'Abomasnow-Mega', 'Barbaracle', 'Bruxish', 'Camerupt-Mega', 'Cofagrigus', 'Exploud', 'Kingdra', 'Noivern', 'Ribombee', 'Slurpuff', 'Venusaur']
nu = ['Accelgor', 'Altaria', 'Ambipom', 'Aromatisse', 'Audino-Mega', 'Blastoise', 'Braviary', 'Cinccino', 'Clawitzer', 'Comfey', 'Cryogonal', 'Delphox', 'Diancie', 'Dodrio', 'Druddigon', 'Froslass', 'Garbodor', 'Gigalith', 'Golbat', 'Guzzlord', 'Hariyama', 'Heliolisk', 'Hitmonlee', 'Hitmontop', 'Houndoom', 'Incineroar', 'Jellicent', 'Klinklang', 'Malamar', 'Medicham', 'Miltank', 'Minior', 'Mismagius', 'Omastar', 'Palossand', 'Passimian', 'Piloswine', 'Qwilfish', 'Rhydon', 'Rotom', 'Sceptile', 'Scrafty', 'Scyther', 'Sigilyph', 'Silvally-Steel', 'Slowbro', 'Slowking', 'Sneasel', 'Steelix', 'Toxicroak', 'Uxie', 'Vanilluxe', 'Vaporeon', 'Vikavolt', 'Vileplume', 'Vivillon', 'Vivillon-Fancy', 'Vivillon-Pokeball', 'Whimsicott', 'Xatu', 'Archeops', 'Charizard', 'Gallade', 'Magmortar', 'Samurott', 'Sawk', 'Tauros', 'Typhlosion']
pu = ['Abomasnow', 'Absol', 'Aggron', 'Ampharos', 'Arbok', 'Ariados', 'Armaldo', 'Articuno', 'Audino', 'Aurorus', 'Avalugg', 'Banette', 'Basculin', 'Basculin-Blue-Striped', 'Bastiodon', 'Beartic', 'Beautifly', 'Beedrill', 'Beheeyem', 'Bellossom', 'Bibarel', 'Bouffalant', 'Butterfree', 'Cacturne', 'Camerupt', 'Carbink', 'Carnivine', 'Carracosta', 'Castform', 'Chatot', 'Cherrim', 'Chimecho', 'Claydol', 'Clefairy', 'Corsola', 'Crabominable', 'Cradily', 'Crustle', 'Dedenne', 'Delcatty', 'Delibird', 'Dewgong', 'Ditto', 'Drampa', 'Drifblim', 'Dugtrio', 'Dugtrio-Alola', 'Dunsparce', 'Dusknoir', 'Dustox', 'Eelektross', 'Electivire', 'Electrode', 'Emolga', 'Exeggutor', 'Exeggutor-Alola', "Farfetch'd", 'Fearow', 'Ferroseed', 'Flareon', 'Floatzel', 'Furfrou', 'Furret', 'Gastrodon', 'Girafarig', 'Glaceon', 'Glalie', 'Gogoat', 'Golduck', 'Golem', 'Golem-Alola', 'Golurk', 'Gorebyss', 'Gothitelle', 'Gourgeist', 'Gourgeist-Large', 'Gourgeist-Small', 'Gourgeist-Super', 'Granbull', 'Grumpig', 'Gumshoos', 'Gurdurr', 'Haunter', 'Heatmor', 'Hitmonchan', 'Huntail', 'Hypno', 'Illumise', 'Jumpluff', 'Jynx', 'Kabutops', 'Kangaskhan', 'Kecleon', 'Kingler', 'Komala', 'Kricketune', 'Lanturn', 'Lapras', 'Leafeon', 'Leavanny', 'Ledian', 'Lickilicky', 'Liepard', 'Lilligant', 'Lopunny', 'Ludicolo', 'Lumineon', 'Lunatone', 'Lurantis', 'Luvdisc', 'Luxray', 'Lycanroc', 'Lycanroc-Midnight', 'Magcargo', 'Manectric', 'Maractus', 'Marowak', 'Masquerain', 'Mawile', 'Meganium', 'Meowstic', 'Meowstic-F', 'Mesprit', 'Mightyena', 'Minun', 'Mothim', 'Mr. Mime', 'Mudsdale', 'Muk', 'Musharna', 'Ninetales', 'Ninjask', 'Noctowl', 'Octillery', 'Oranguru', 'Oricorio', "Oricorio-Pa'u", 'Oricorio-Pom-Pom', 'Oricorio-Sensu', 'Pachirisu', 'Parasect', 'Persian', 'Persian-Alola', 'Phione', 'Pidgeot', 'Pikachu-Alola', 'Pikachu-Hoenn', 'Pikachu-Kalos', 'Pikachu-Original', 'Pikachu-Partner', 'Pikachu-Sinnoh', 'Pikachu-Unova', 'Pinsir', 'Plusle', 'Politoed', 'Poliwrath', 'Primeape', 'Probopass', 'Purugly', 'Pyroar', 'Pyukumuku', 'Raichu', 'Raichu-Alola', 'Rampardos', 'Rapidash', 'Raticate', 'Raticate-Alola', 'Regice', 'Regigigas', 'Regirock', 'Relicanth', 'Rotom-Fan', 'Rotom-Frost', 'Sableye', 'Sandslash', 'Sandslash-Alola', 'Sawsbuck', 'Seaking', 'Seviper', 'Shedinja', 'Shiftry', 'Shiinotic', 'Shuckle', 'Silvally', 'Silvally-Bug', 'Silvally-Dark', 'Silvally-Dragon', 'Silvally-Electric', 'Silvally-Fairy', 'Silvally-Fighting', 'Silvally-Fire', 'Silvally-Flying', 'Silvally-Ghost', 'Silvally-Grass', 'Silvally-Ground', 'Silvally-Ice', 'Silvally-Poison', 'Silvally-Psychic', 'Silvally-Rock', 'Silvally-Water', 'Simipour', 'Simisage', 'Simisear', 'Skuntank', 'Slaking', 'Smeargle', 'Solrock', 'Spinda', 'Spiritomb', 'Stantler', 'Stoutland', 'Stunfisk', 'Sudowoodo', 'Sunflora', 'Swalot', 'Swanna', 'Swoobat', 'Throh', 'Togedemaru', 'Torkoal', 'Torterra', 'Toucannon', 'Trevenant', 'Tropius', 'Turtonator', 'Unfezant', 'Unown', 'Ursaring', 'Vespiquen', 'Victreebel', 'Volbeat', 'Wailord', 'Walrein', 'Watchog', 'Weezing', 'Whiscash', 'Wigglytuff', 'Wishiwashi', 'Wobbuffet', 'Wormadam', 'Wormadam-Sandy', 'Wormadam-Trash', 'Zangoose', 'Zebstrika', 'Floette-Eternal', 'Magearna-Original', 'Bayleef', 'Boldore', 'Braixen', 'Brionne', 'Cascoon', 'Charjabug', 'Charmeleon', 'Combusken', 'Cosmoem', 'Croconaw', 'Dartrix', 'Dewott', 'Dragonair', 'Duosion', 'Dusclops', 'Eelektrik', 'Electabuzz', 'Flaaffy', 'Fletchinder', 'Floette', 'Fraxure', 'Frogadier', 'Gabite', 'Gloom', 'Gothorita', 'Graveler', 'Graveler-Alola', 'Grotle', 'Grovyle', 'Hakamo-o', 'Herdier', 'Ivysaur', 'Jigglypuff', 'Kadabra', 'Kakuna', 'Kirlia', 'Klang', 'Krokorok', 'Lairon', 'Lampent', 'Lombre', 'Loudred', 'Luxio', 'Machoke', 'Magmar', 'Marill', 'Marshtomp', 'Metang', 'Metapod', 'Monferno', 'Nidorina', 'Nidorino', 'Nuzleaf', 'Palpitoad', 'Pidgeotto', 'Pignite', 'Pikachu', 'Poipole', 'Poliwhirl', 'Prinplup', 'Pupitar', 'Quilava', 'Quilladin', 'Roselia', 'Seadra', 'Sealeo', 'Servine', 'Shelgon', 'Silcoon', 'Skiploom', 'Sliggoo', 'Spewpa', 'Staravia', 'Steenee', 'Swadloon', 'Togetic', 'Torracat', 'Tranquill', 'Trumbeak', 'Type: Null', 'Vanillish', 'Vibrava', 'Vigoroth', 'Wartortle', 'Weepinbell', 'Whirlipede', 'Zweilous']
lc = ['Aipom', 'Cutiefly', 'Drifloon', 'Gothita', 'Meditite', 'Misdreavus', 'Murkrow', 'Porygon', 'Swirlix', 'Tangela', 'Torchic', 'Vulpix', 'Yanma', 'Abra', 'Amaura', 'Anorith', 'Archen', 'Aron', 'Axew', 'Azurill', 'Bagon', 'Baltoy', 'Barboach', 'Beldum', 'Bellsprout', 'Bergmite', 'Bidoof', 'Binacle', 'Blitzle', 'Bonsly', 'Bounsweet', 'Bronzor', 'Budew', 'Buizel', 'Bulbasaur', 'Buneary', 'Bunnelby', 'Burmy', 'Cacnea', 'Carvanha', 'Caterpie', 'Charmander', 'Cherubi', 'Chespin', 'Chikorita', 'Chimchar', 'Chinchou', 'Chingling', 'Clamperl', 'Clauncher', 'Cleffa', 'Combee', 'Corphish', 'Cosmog', 'Cottonee', 'Crabrawler', 'Cranidos', 'Croagunk', 'Cubchoo', 'Cubone', 'Cyndaquil', 'Darumaka', 'Deerling', 'Deino', 'Dewpider', 'Diglett', 'Diglett-Alola', 'Doduo', 'Dratini', 'Drilbur', 'Drowzee', 'Ducklett', 'Duskull', 'Dwebble', 'Eevee', 'Ekans', 'Electrike', 'Elekid', 'Elgyem', 'Espurr', 'Exeggcute', 'Feebas', 'Fennekin', 'Finneon', 'Flabébé', 'Fletchling', 'Fomantis', 'Foongus', 'Frillish', 'Froakie', 'Gastly', 'Geodude', 'Geodude-Alola', 'Gible', 'Glameow', 'Goldeen', 'Golett', 'Goomy', 'Grimer', 'Grimer-Alola', 'Growlithe', 'Grubbin', 'Gulpin', 'Happiny', 'Helioptile', 'Hippopotas', 'Honedge', 'Hoothoot', 'Hoppip', 'Horsea', 'Houndour', 'Igglybuff', 'Inkay', 'Jangmo-o', 'Joltik', 'Kabuto', 'Karrablast', 'Klink', 'Koffing', 'Krabby', 'Kricketot', 'Larvesta', 'Larvitar', 'Ledyba', 'Lickitung', 'Lileep', 'Lillipup', 'Litleo', 'Litten', 'Litwick', 'Lotad', 'Machop', 'Magby', 'Magikarp', 'Magnemite', 'Makuhita', 'Mankey', 'Mantyke', 'Mareanie', 'Mareep', 'Meowth', 'Meowth-Alola', 'Mienfoo', 'Mime Jr.', 'Minccino', 'Morelull', 'Mudbray', 'Mudkip', 'Munchlax', 'Munna', 'Natu', 'Nidoran-F', 'Nidoran-M', 'Nincada', 'Noibat', 'Nosepass', 'Numel', 'Oddish', 'Omanyte', 'Onix', 'Oshawott', 'Pancham', 'Panpour', 'Pansage', 'Pansear', 'Paras', 'Patrat', 'Pawniard', 'Petilil', 'Phanpy', 'Phantump', 'Pichu', 'Pidgey', 'Pidove', 'Pikipek', 'Pineco', 'Piplup', 'Poliwag', 'Ponyta', 'Poochyena', 'Popplio', 'Psyduck', 'Pumpkaboo', 'Pumpkaboo-Large', 'Pumpkaboo-Small', 'Pumpkaboo-Super', 'Purrloin', 'Ralts', 'Rattata', 'Rattata-Alola', 'Remoraid', 'Rhyhorn', 'Riolu', 'Rockruff', 'Roggenrola', 'Rowlet', 'Rufflet', 'Salandit', 'Sandile', 'Sandshrew', 'Sandshrew-Alola', 'Sandygast', 'Scatterbug', 'Scraggy', 'Seedot', 'Seel', 'Sentret', 'Sewaddle', 'Shellder', 'Shellos', 'Shelmet', 'Shieldon', 'Shinx', 'Shroomish', 'Shuppet', 'Skiddo', 'Skitty', 'Skorupi', 'Skrelp', 'Slakoth', 'Slowpoke', 'Slugma', 'Smoochum', 'Snivy', 'Snorunt', 'Snover', 'Snubbull', 'Solosis', 'Spearow', 'Spheal', 'Spinarak', 'Spoink', 'Spritzee', 'Squirtle', 'Starly', 'Staryu', 'Stufful', 'Stunky', 'Sunkern', 'Surskit', 'Swablu', 'Swinub', 'Taillow', 'Teddiursa', 'Tentacool', 'Tepig', 'Timburr', 'Tirtouga', 'Togepi', 'Totodile', 'Trapinch', 'Treecko', 'Trubbish', 'Turtwig', 'Tympole', 'Tynamo', 'Tyrogue', 'Tyrunt', 'Vanillite', 'Venipede', 'Venonat', 'Voltorb', 'Vullaby', 'Vulpix-Alola', 'Wailmer', 'Weedle', 'Whismur', 'Wimpod', 'Wingull', 'Woobat', 'Wooper', 'Wurmple', 'Wynaut', 'Yamask', 'Yungoos', 'Zigzagoon', 'Zorua', 'Zubat']   

#List of pokemon by generation for Mono-generation
Gen1m = ["Bulbasaur", "Ivysaur", "Venusaur", "Venusaur-Mega", "Charmander", "Charmeleon", "Charizard", "Charizard-Mega-X", "Charizard-Mega-Y", "Squirtle", "Wartortle", "Blastoise", "Blastoise-Mega", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Beedrill-Mega", "Pidgey", "Pidgeotto", "Pidgeot", "Pidgeot-Mega", "Rattata", "Rattata-Alola", "Raticate", "Raticate-Alola", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Raichu-Alola", "Sandshrew", "Sandshrew-Alola", "Sandslash", "Sandslash-Alola", "Nidoran-F", "Nidorina", "Nidoqueen", "Nidoran-M", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Vulpix-Alola", "Ninetales", "Ninetales-Alola", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Diglett-Alola", "Dugtrio", "Dugtrio-Alola", "Meowth", "Meowth-Alola", "Persian", "Persian-Alola", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Alakazam-Mega", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Geodude-Alola", "Graveler", "Graveler-Alola", "Golem", "Golem-Alola", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Slowbro-Mega", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Grimer-Alola", "Muk", "Muk-Alola", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Gengar-Mega", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Exeggutor-Alola", "Cubone", "Marowak", "Marowak-Alola", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Kangaskhan-Mega", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Pinsir-Mega", "Tauros", "Magikarp", "Gyarados", "Gyarados-Mega", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Aerodactyl-Mega", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mewtwo-Mega-X", "Mewtwo-Mega-Y", "Mew"]
Gen2m = ["Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava", "Typhlosion", "Totodile", "Croconaw", "Feraligatr", "Sentret", "Furret", "Hoothoot", "Noctowl", "Ledyba", "Ledian", "Spinarak", "Ariados", "Crobat", "Chinchou", "Lanturn", "Pichu", "Cleffa", "Igglybuff", "Togepi", "Togetic", "Natu", "Xatu", "Mareep", "Flaaffy", "Ampharos", "Ampharos-Mega", "Bellossom", "Marill", "Azumarill", "Sudowoodo", "Politoed", "Hoppip", "Skiploom", "Jumpluff", "Aipom", "Sunkern", "Sunflora", "Yanma", "Wooper", "Quagsire", "Espeon", "Umbreon", "Murkrow", "Slowking", "Misdreavus", "Unown", "Wobbuffet", "Girafarig", "Pineco", "Forretress", "Dunsparce", "Gligar", "Steelix", "Steelix-Mega", "Snubbull", "Granbull", "Qwilfish", "Scizor", "Scizor-Mega", "Shuckle", "Heracross", "Heracross-Mega", "Sneasel", "Teddiursa", "Ursaring", "Slugma", "Magcargo", "Swinub", "Piloswine", "Corsola", "Remoraid", "Octillery", "Delibird", "Mantine", "Skarmory", "Houndour", "Houndoom", "Houndoom-Mega", "Kingdra", "Phanpy", "Donphan", "Porygon2", "Stantler", "Smeargle", "Tyrogue", "Hitmontop", "Smoochum", "Elekid", "Magby", "Miltank", "Blissey", "Raikou", "Entei", "Suicune", "Larvitar", "Pupitar", "Tyranitar", "Tyranitar-Mega", "Lugia", "Ho-Oh", "Celebi"]
Gen3m = ["Treecko", "Grovyle", "Sceptile", "Sceptile-Mega", "Torchic", "Combusken", "Blaziken", "Blaziken-Mega", "Mudkip", "Marshtomp", "Swampert", "Swampert-Mega", "Poochyena", "Mightyena", "Zigzagoon", "Linoone", "Wurmple", "Silcoon", "Beautifly", "Cascoon", "Dustox", "Lotad", "Lombre", "Ludicolo", "Seedot", "Nuzleaf", "Shiftry", "Taillow", "Swellow", "Wingull", "Pelipper", "Ralts", "Kirlia", "Gardevoir", "Gardevoir-Mega", "Surskit", "Masquerain", "Shroomish", "Breloom", "Slakoth", "Vigoroth", "Slaking", "Nincada", "Ninjask", "Shedinja", "Whismur", "Loudred", "Exploud", "Makuhita", "Hariyama", "Azurill", "Nosepass", "Skitty", "Delcatty", "Sableye", "Sableye-Mega", "Mawile", "Mawile-Mega", "Aron", "Lairon", "Aggron", "Aggron-Mega", "Meditite", "Medicham", "Medicham-Mega", "Electrike", "Manectric", "Manectric-Mega", "Plusle", "Minun", "Volbeat", "Illumise", "Roselia", "Gulpin", "Swalot", "Carvanha", "Sharpedo", "Sharpedo-Mega", "Wailmer", "Wailord", "Numel", "Camerupt", "Camerupt-Mega", "Torkoal", "Spoink", "Grumpig", "Spinda", "Trapinch", "Vibrava", "Flygon", "Cacnea", "Cacturne", "Swablu", "Altaria", "Altaria-Mega", "Zangoose", "Seviper", "Lunatone", "Solrock", "Barboach", "Whiscash", "Corphish", "Crawdaunt", "Baltoy", "Claydol", "Lileep", "Cradily", "Anorith", "Armaldo", "Feebas", "Milotic", "Castform", "Kecleon", "Shuppet", "Banette", "Banette-Mega", "Duskull", "Dusclops", "Tropius", "Chimecho", "Absol", "Absol-Mega", "Wynaut", "Snorunt", "Glalie", "Glalie-Mega", "Spheal", "Sealeo", "Walrein", "Clamperl", "Huntail", "Gorebyss", "Relicanth", "Luvdisc", "Bagon", "Shelgon", "Salamence", "Salamence-Mega", "Beldum", "Metang", "Metagross", "Metagross-Mega", "Regirock", "Regice", "Registeel", "Latias", "Latias-Mega", "Latios", "Latios-Mega", "Kyogre", "Kyogre-Primal", "Groudon", "Groudon-Primal", "Rayquaza", "Rayquaza-Mega", "Jirachi", "Deoxys", "Deoxys-Attack", "Deoxys-Defense", "Deoxys-Speed"]
Gen4m = ["Turtwig", "Grotle", "Torterra", "Chimchar", "Monferno", "Infernape", "Piplup", "Prinplup", "Empoleon", "Starly", "Staravia", "Staraptor", "Bidoof", "Bibarel", "Kricketot", "Kricketune", "Shinx", "Luxio", "Luxray", "Budew", "Roserade", "Cranidos", "Rampardos", "Shieldon", "Bastiodon", "Burmy", "Wormadam", "Wormadam-Sandy", "Wormadam-Trash", "Mothim", "Combee", "Vespiquen", "Pachirisu", "Buizel", "Floatzel", "Cherubi", "Cherrim", "Shellos", "Gastrodon", "Ambipom", "Drifloon", "Drifblim", "Buneary", "Lopunny", "Lopunny-Mega", "Mismagius", "Honchkrow", "Glameow", "Purugly", "Chingling", "Stunky", "Skuntank", "Bronzor", "Bronzong", "Bonsly", "Mime Jr.", "Happiny", "Chatot", "Spiritomb", "Gible", "Gabite", "Garchomp", "Garchomp-Mega", "Munchlax", "Riolu", "Lucario", "Lucario-Mega", "Hippopotas", "Hippowdon", "Skorupi", "Drapion", "Croagunk", "Toxicroak", "Carnivine", "Finneon", "Lumineon", "Mantyke", "Snover", "Abomasnow", "Abomasnow-Mega", "Weavile", "Magnezone", "Lickilicky", "Rhyperior", "Tangrowth", "Electivire", "Magmortar", "Togekiss", "Yanmega", "Leafeon", "Glaceon", "Gliscor", "Mamoswine", "Porygon-Z", "Gallade", "Gallade-Mega", "Probopass", "Dusknoir", "Froslass", "Rotom", "Rotom-Heat", "Rotom-Wash", "Rotom-Frost", "Rotom-Fan", "Rotom-Mow", "Uxie", "Mesprit", "Azelf", "Dialga", "Palkia", "Heatran", "Regigigas", "Giratina", "Giratina-Origin", "Cresselia", "Phione", "Manaphy", "Darkrai", "Shaymin", "Shaymin-Sky", "Arceus", "Arceus-Bug", "Arceus-Dark", "Arceus-Dragon", "Arceus-Electric", "Arceus-Fairy", "Arceus-Fighting", "Arceus-Fire", "Arceus-Flying", "Arceus-Ghost", "Arceus-Grass", "Arceus-Ground", "Arceus-Ice", "Arceus-Poison", "Arceus-Psychic", "Arceus-Rock", "Arceus-Steel", "Arceus-Water"]
Gen5m = ["Victini", "Snivy", "Servine", "Serperior", "Tepig", "Pignite", "Emboar", "Oshawott", "Dewott", "Samurott", "Patrat", "Watchog", "Lillipup", "Herdier", "Stoutland", "Purrloin", "Liepard", "Pansage", "Simisage", "Pansear", "Simisear", "Panpour", "Simipour", "Munna", "Musharna", "Pidove", "Tranquill", "Unfezant", "Blitzle", "Zebstrika", "Roggenrola", "Boldore", "Gigalith", "Woobat", "Swoobat", "Drilbur", "Excadrill", "Audino", "Audino-Mega", "Timburr", "Gurdurr", "Conkeldurr", "Tympole", "Palpitoad", "Seismitoad", "Throh", "Sawk", "Sewaddle", "Swadloon", "Leavanny", "Venipede", "Whirlipede", "Scolipede", "Cottonee", "Whimsicott", "Petilil", "Lilligant", "Basculin", "Basculin-Blue-Striped", "Sandile", "Krokorok", "Krookodile", "Darumaka", "Darmanitan", "Maractus", "Dwebble", "Crustle", "Scraggy", "Scrafty", "Sigilyph", "Yamask", "Cofagrigus", "Tirtouga", "Carracosta", "Archen", "Archeops", "Trubbish", "Garbodor", "Zorua", "Zoroark", "Minccino", "Cinccino", "Gothita", "Gothorita", "Gothitelle", "Solosis", "Duosion", "Reuniclus", "Ducklett", "Swanna", "Vanillite", "Vanillish", "Vanilluxe", "Deerling", "Sawsbuck", "Emolga", "Karrablast", "Escavalier", "Foongus", "Amoonguss", "Frillish", "Jellicent", "Alomomola", "Joltik", "Galvantula", "Ferroseed", "Ferrothorn", "Klink", "Klang", "Klinklang", "Tynamo", "Eelektrik", "Eelektross", "Elgyem", "Beheeyem", "Litwick", "Lampent", "Chandelure", "Axew", "Fraxure", "Haxorus", "Cubchoo", "Beartic", "Cryogonal", "Shelmet", "Accelgor", "Stunfisk", "Mienfoo", "Mienshao", "Druddigon", "Golett", "Golurk", "Pawniard", "Bisharp", "Bouffalant", "Rufflet", "Braviary", "Vullaby", "Mandibuzz", "Heatmor", "Durant", "Deino", "Zweilous", "Hydreigon", "Larvesta", "Volcarona", "Cobalion", "Terrakion", "Virizion", "Tornadus", "Tornadus-Therian", "Thundurus", "Thundurus-Therian", "Reshiram", "Zekrom", "Landorus", "Landorus-Therian", "Kyurem", "Kyurem-Black", "Kyurem-White", "Keldeo", "Meloetta", "Genesect", "Genesect-Douse", "Genesect-Shock", "Genesect-Burn", "Genesect-Chill"]
Gen6m = ["Chespin", "Quilladin", "Chesnaught", "Fennekin", "Braixen", "Delphox", "Froakie", "Frogadier", "Greninja", "Greninja-Ash", "Bunnelby", "Diggersby", "Fletchling", "Fletchinder", "Talonflame", "Scatterbug", "Spewpa", "Vivillon", "Vivillon-Fancy", "Vivillon-Pokeball", "Litleo", "Pyroar", "Flabebe", "Flabebe-Blue", "Flabebe-Orange", "Flabebe-White", "Flabebe-Yellow", "Floette", "Floette-Blue", "Floette-Orange", "Floette-White", "Floette-Yellow", "Floette-Eternal", "Florges", "Florges-Blue", "Florges-Orange", "Florges-White", "Florges-Yellow", "Skiddo", "Gogoat", "Pancham", "Pangoro", "Furfrou", "Espurr", "Meowstic", "Meowstic-F", "Honedge", "Doublade", "Aegislash", "Spritzee", "Aromatisse", "Swirlix", "Slurpuff", "Inkay", "Malamar", "Binacle", "Barbaracle", "Skrelp", "Dragalge", "Clauncher", "Clawitzer", "Helioptile", "Heliolisk", "Tyrunt", "Tyrantrum", "Amaura", "Aurorus", "Sylveon", "Hawlucha", "Dedenne", "Carbink", "Goomy", "Sliggoo", "Goodra", "Klefki", "Phantump", "Trevenant", "Pumpkaboo", "Pumpkaboo-Small", "Pumpkaboo-Large", "Pumpkaboo-Super", "Gourgeist", "Gourgeist-Small", "Gourgeist-Large", "Gourgeist-Super", "Bergmite", "Avalugg", "Noibat", "Noivern", "Xerneas", "Yveltal", "Zygarde", "Zygarde-10%", "Zygarde-Complete", "Diancie", "Diancie-Mega", "Hoopa", "Hoopa-Unbound", "Volcanion"]
Gen7m = ["Rowlet", "Dartrix", "Decidueye", "Litten", "Torracat", "Incineroar", "Popplio", "Brionne", "Primarina", "Pikipek", "Trumbeak", "Toucannon", "Yungoos", "Gumshoos", "Grubbin", "Charjabug", "Vikavolt", "Crabrawler", "Crabominable", "Oricorio", "Oricorio-Pom-Pom", "Oricorio-Pa'u", "Oricorio-Sensu", "Cutiefly", "Ribombee", "Rockruff", "Lycanroc", "Lycanroc-Midnight", "Lycanroc-Dusk", "Wishiwashi", "Mareanie", "Toxapex", "Mudbray", "Mudsdale", "Dewpider", "Araquanid", "Fomantis", "Lurantis", "Morelull", "Shiinotic", "Salandit", "Salazzle", "Stufful", "Bewear", "Bounsweet", "Steenee", "Tsareena", "Comfey", "Oranguru", "Passimian", "Wimpod", "Golisopod", "Sandygast", "Palossand", "Pyukumuku", "Type: Null", "Silvally", "Silvally-Bug", "Silvally-Dark", "Silvally-Dragon", "Silvally-Electric", "Silvally-Fairy", "Silvally-Fighting", "Silvally-Fire", "Silvally-Flying", "Silvally-Ghost", "Silvally-Grass", "Silvally-Ground", "Silvally-Ice", "Silvally-Poison", "Silvally-Psychic", "Silvally-Rock", "Silvally-Steel", "Silvally-Water", "Minior", "Minior-Orange", "Minior-Yellow", "Minior-Green", "Minior-Blue", "Minior-Indigo", "Minior-Violet", "Minior-Meteor", "Komala", "Turtonator", "Togedemaru", "Mimikyu", "Bruxish", "Drampa", "Dhelmise", "Jangmo-o", "Hakamo-o", "Kommo-o", "Tapu Koko", "Tapu Lele", "Tapu Bulu", "Tapu Fini", "Cosmog", "Cosmoem", "Solgaleo", "Lunala", "Nihilego", "Buzzwole", "Pheromosa", "Xurkitree", "Celesteela", "Kartana", "Guzzlord", "Necrozma", "Necrozma-Dusk-Mane", "Necrozma-Dawn-Wings", "Necrozma-Ultra", "Magearna", "Marshadow", "Poipole", "Naganadel", "Stakataka", "Blacephalon", "Zeraora"]

#List of pokemon by egg group for Mono-egg group
Monster = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Venusaur-Mega', 'Charmander', 'Charmeleon', 'Charizard', 'Charizard-Mega-X', 'Charizard-Mega-Y', 'Squirtle', 'Wartortle', 'Blastoise', 'Blastoise-Mega', 'Nidoran-F', 'Nidoran-M', 'Nidorino', 'Nidoking', 'Slowpoke', 'Slowbro', 'Slowbro-Mega', 'Cubone', 'Marowak', 'Marowak-Alola', 'Lickitung', 'Rhyhorn', 'Rhydon', 'Kangaskhan', 'Kangaskhan-Mega', 'Lapras', 'Snorlax', 'Chikorita', 'Bayleef', 'Meganium', 'Totodile', 'Croconaw', 'Feraligatr', 'Mareep', 'Flaaffy', 'Ampharos', 'Ampharos-Mega', 'Slowking', 'Larvitar', 'Pupitar', 'Tyranitar', 'Tyranitar-Mega', 'Treecko', 'Grovyle', 'Sceptile', 'Sceptile-Mega', 'Mudkip', 'Marshtomp', 'Swampert', 'Swampert-Mega', 'Whismur', 'Loudred', 'Exploud', 'Aron', 'Lairon', 'Aggron', 'Aggron-Mega', 'Tropius', 'Turtwig', 'Grotle', 'Torterra', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon', 'Gible', 'Gabite', 'Garchomp', 'Garchomp-Mega', 'Snover', 'Abomasnow', 'Abomasnow-Mega', 'Lickilicky', 'Rhyperior', 'Axew', 'Fraxure', 'Haxorus', 'Druddigon', 'Helioptile', 'Heliolisk', 'Tyrunt', 'Tyrantrum', 'Amaura', 'Aurorus', 'Bergmite', 'Avalugg', 'Salandit', 'Salazzle', 'Turtonator', 'Drampa']
Grassz = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Venusaur-Mega', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Exeggcute', 'Exeggutor', 'Exeggutor-Alola', 'Tangela', 'Chikorita', 'Bayleef', 'Meganium', 'Bellossom', 'Hoppip', 'Skiploom', 'Jumpluff', 'Sunkern', 'Sunflora', 'Seedot', 'Nuzleaf', 'Shiftry', 'Shroomish', 'Breloom', 'Roselia', 'Cacnea', 'Cacturne', 'Tropius', 'Turtwig', 'Grotle', 'Torterra', 'Roserade', 'Cherubi', 'Cherrim', 'Carnivine', 'Snover', 'Abomasnow', 'Abomasnow-Mega', 'Tangrowth', 'Snivy', 'Servine', 'Serperior', 'Cottonee', 'Whimsicott', 'Petilil', 'Lilligant', 'Maractus', 'Foongus', 'Amoonguss', 'Ferroseed', 'Ferrothorn', 'Phantump', 'Trevenant', 'Fomantis', 'Lurantis', 'Morelull', 'Shiinotic', 'Bounsweet', 'Steenee', 'Tsareena', 'Comfey']
Dragonz = ['Charmander', 'Charmeleon', 'Charizard', 'Charizard-Mega-X', 'Charizard-Mega-Y', 'Ekans', 'Arbok', 'Treecko', 'Grovyle', 'Sceptile', 'Sceptile-Mega', 'Swablu', 'Altaria', 'Altaria-Mega', 'Seviper', 'Bagon', 'Shelgon', 'Salamence', 'Salamence-Mega', 'Gible', 'Gabite', 'Garchomp', 'Garchomp-Mega', 'Scraggy', 'Scrafty', 'Axew', 'Fraxure', 'Haxorus', 'Druddigon', 'Deino', 'Zweilous', 'Hydreigon', 'Helioptile', 'Heliolisk', 'Tyrunt', 'Tyrantrum', 'Goomy', 'Sliggoo', 'Goodra', 'Salandit', 'Salazzle', 'Turtonator', 'Drampa', 'Jangmo-o', 'Hakamo-o', 'Kommo-o']
Waterz = ['Squirtle', 'Wartortle', 'Blastoise', 'Blastoise-Mega', 'Slowpoke', 'Slowbro', 'Slowbro-Mega', 'Lapras', 'Totodile', 'Croconaw', 'Feraligatr', 'Slowking', 'Mudkip', 'Marshtomp', 'Swampert', 'Swampert-Mega', 'Wailmer', 'Wailord', 'Skorupi', 'Drapion', 'Archen', 'Archeops', 'Wimpod', 'Golisopod', 'Psyduck', 'Golduck', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Seel', 'Dewgong', 'Horsea', 'Seadra', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Dratini', 'Dragonair', 'Dragonite', 'Marill', 'Azumarill', 'Politoed', 'Wooper', 'Quagsire', 'Corsola', 'Remoraid', 'Octillery', 'Delibird', 'Mantine', 'Kingdra', 'Lotad', 'Lombre', 'Ludicolo', 'Wingull', 'Pelipper', 'Surskit', 'Masquerain', 'Corphish', 'Crawdaunt', 'Feebas', 'Milotic', 'Spheal', 'Sealeo', 'Walrein', 'Clamperl', 'Huntail', 'Gorebyss', 'Relicanth', 'Piplup', 'Prinplup', 'Empoleon', 'Bidoof', 'Bibarel', 'Buizel', 'Floatzel', 'Shellos', 'Gastrodon', 'Phione', 'Manaphy', 'Tympole', 'Palpitoad', 'Seismitoad', 'Tirtouga', 'Carracosta', 'Ducklett', 'Swanna', 'Alomomola', 'Stunfisk', 'Froakie', 'Frogadier', 'Greninja', 'Inkay', 'Malamar', 'Skrelp', 'Dragalge', 'Clauncher', 'Clawitzer', 'Popplio', 'Brionne', 'Primarina', 'Mareanie', 'Toxapex', 'Dewpider', 'Araquanid', 'Pyukumuku', 'Goldeen', 'Seaking', 'Magikarp', 'Gyarados', 'Gyarados-Mega', 'Chinchou', 'Lanturn', 'Qwilfish', 'Carvanha', 'Sharpedo', 'Sharpedo-Mega', 'Barboach', 'Whiscash', 'Luvdisc', 'Finneon', 'Lumineon', 'Basculin', 'Basculin-Blue-Striped', 'Wishiwashi', 'Bruxish', 'Tentacool', 'Tentacruel', 'Shellder', 'Cloyster', 'Krabby', 'Kingler', 'Staryu', 'Starmie', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Binacle', 'Barbaracle', 'Crabrawler', 'Crabominable']
Bugz = ['Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Beedrill-Mega', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Scyther', 'Pinsir', 'Pinsir-Mega', 'Ledyba', 'Ledian', 'Spinarak', 'Ariados', 'Yanma', 'Pineco', 'Forretress', 'Gligar', 'Scizor', 'Scizor-Mega', 'Shuckle', 'Heracross', 'Heracross-Mega', 'Wurmple', 'Silcoon', 'Beautifly', 'Cascoon', 'Dustox', 'Nincada', 'Ninjask', 'Volbeat', 'Illumise', 'Trapinch', 'Vibrava', 'Flygon', 'Kricketot', 'Kricketune', 'Burmy', 'Wormadam', 'Wormadam-Sandy', 'Wormadam-Trash', 'Mothim', 'Combee', 'Vespiquen', 'Skorupi', 'Drapion', 'Yanmega', 'Gliscor', 'Sewaddle', 'Swadloon', 'Leavanny', 'Venipede', 'Whirlipede', 'Scolipede', 'Dwebble', 'Crustle', 'Karrablast', 'Escavalier', 'Joltik', 'Galvantula', 'Shelmet', 'Accelgor', 'Durant', 'Larvesta', 'Volcarona', 'Scatterbug', 'Spewpa', 'Vivillon', 'Vivillon-Fancy', 'Vivillon-Pokeball', 'Grubbin', 'Charjabug', 'Vikavolt', 'Cutiefly', 'Ribombee', 'Wimpod', 'Golisopod']
Flyingz = ['Pidgey', 'Pidgeotto', 'Pidgeot', 'Pidgeot-Mega', 'Spearow', 'Fearow', 'Zubat', 'Golbat', 'Farfetchd', 'Doduo', 'Dodrio', 'Aerodactyl', 'Aerodactyl-Mega', 'Hoothoot', 'Noctowl', 'Crobat', 'Togetic', 'Natu', 'Xatu', 'Murkrow', 'Skarmory', 'Taillow', 'Swellow', 'Swablu', 'Altaria', 'Altaria-Mega', 'Starly', 'Staravia', 'Staraptor', 'Honchkrow', 'Chatot', 'Togekiss', 'Pidove', 'Tranquill', 'Unfezant', 'Woobat', 'Swoobat', 'Sigilyph', 'Archen', 'Archeops', 'Rufflet', 'Braviary', 'Vullaby', 'Mandibuzz', 'Fletchling', 'Fletchinder', 'Talonflame', 'Noibat', 'Noivern', 'Rowlet', 'Dartrix', 'Decidueye', 'Pikipek', 'Trumbeak', 'Toucannon', 'Oricorio', 'Oricorio-Pom-Pom', 'Oricorio-Pau', 'Oricorio-Sensu']
Field = ['Rattata', 'Rattata-Alola', 'Raticate', 'Raticate-Alola', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Raichu-Alola', 'Sandshrew', 'Sandshrew-Alola', 'Sandslash', 'Sandslash-Alola', 'Nidoran-F', 'Nidoran-M', 'Nidorino', 'Nidoking', 'Vulpix', 'Vulpix-Alola', 'Ninetales', 'Ninetales-Alola', 'Diglett', 'Diglett-Alola', 'Dugtrio', 'Dugtrio-Alola', 'Meowth', 'Meowth-Alola', 'Persian', 'Persian-Alola', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Ponyta', 'Rapidash', 'Farfetchd', 'Rhyhorn', 'Rhydon', 'Tauros', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Cyndaquil', 'Quilava', 'Typhlosion', 'Sentret', 'Furret', 'Mareep', 'Flaaffy', 'Ampharos', 'Ampharos-Mega', 'Aipom', 'Espeon', 'Umbreon', 'Girafarig', 'Dunsparce', 'Snubbull', 'Granbull', 'Sneasel', 'Teddiursa', 'Ursaring', 'Swinub', 'Piloswine', 'Houndour', 'Houndoom', 'Houndoom-Mega', 'Phanpy', 'Donphan', 'Stantler', 'Smeargle', 'Miltank', 'Torchic', 'Combusken', 'Blaziken', 'Blaziken-Mega', 'Poochyena', 'Mightyena', 'Zigzagoon', 'Linoone', 'Seedot', 'Nuzleaf', 'Shiftry', 'Slakoth', 'Vigoroth', 'Slaking', 'Whismur', 'Loudred', 'Exploud', 'Skitty', 'Delcatty', 'Mawile', 'Mawile-Mega', 'Electrike', 'Manectric', 'Manectric-Mega', 'Wailmer', 'Wailord', 'Numel', 'Camerupt', 'Camerupt-Mega', 'Torkoal', 'Spoink', 'Grumpig', 'Spinda', 'Zangoose', 'Seviper', 'Kecleon', 'Absol', 'Absol-Mega', 'Chimchar', 'Monferno', 'Infernape', 'Shinx', 'Luxio', 'Luxray', 'Pachirisu', 'Ambipom', 'Buneary', 'Lopunny', 'Lopunny-Mega', 'Glameow', 'Purugly', 'Stunky', 'Skuntank', 'Lucario', 'Lucario-Mega', 'Hippopotas', 'Hippowdon', 'Weavile', 'Rhyperior', 'Leafeon', 'Glaceon', 'Mamoswine', 'Snivy', 'Servine', 'Serperior', 'Tepig', 'Pignite', 'Emboar', 'Oshawott', 'Dewott', 'Samurott', 'Patrat', 'Watchog', 'Lillipup', 'Herdier', 'Stoutland', 'Purrloin', 'Liepard', 'Pansage', 'Simisage', 'Pansear', 'Simisear', 'Panpour', 'Simipour', 'Munna', 'Musharna', 'Blitzle', 'Zebstrika', 'Woobat', 'Swoobat', 'Drilbur', 'Excadrill', 'Sandile', 'Krokorok', 'Krookodile', 'Darumaka', 'Darmanitan', 'Scraggy', 'Scrafty', 'Zorua', 'Zoroark', 'Minccino', 'Cinccino', 'Deerling', 'Sawsbuck', 'Emolga', 'Cubchoo', 'Beartic', 'Mienfoo', 'Mienshao', 'Bouffalant', 'Heatmor', 'Chespin', 'Quilladin', 'Chesnaught', 'Fennekin', 'Braixen', 'Delphox', 'Bunnelby', 'Diggersby', 'Litleo', 'Pyroar', 'Skiddo', 'Gogoat', 'Pancham', 'Pangoro', 'Furfrou', 'Espurr', 'Meowstic', 'Meowstic-F', 'Sylveon', 'Dedenne', 'Litten', 'Torracat', 'Incineroar', 'Yungoos', 'Gumshoos', 'Rockruff', 'Lycanroc', 'Lycanroc-Midnight', 'Lycanroc-Dusk', 'Mudbray', 'Mudsdale', 'Stufful', 'Bewear', 'Oranguru', 'Passimian', 'Komala', 'Togedemaru']
Fairyz = ['Pikachu', 'Raichu', 'Raichu-Alola', 'Clefairy', 'Clefable', 'Jigglypuff', 'Wigglytuff', 'Chansey', 'Togetic', 'Hoppip', 'Skiploom', 'Jumpluff', 'Snubbull', 'Granbull', 'Blissey', 'Shroomish', 'Breloom', 'Skitty', 'Delcatty', 'Mawile', 'Mawile-Mega', 'Plusle', 'Minun', 'Roselia', 'Castform', 'Snorunt', 'Glalie', 'Glalie-Mega', 'Roserade', 'Pachirisu', 'Cherubi', 'Cherrim', 'Togekiss', 'Froslass', 'Audino', 'Audino-Mega', 'Cottonee', 'Whimsicott', 'Flabebe', 'Flabebe-Blue', 'Flabebe-Orange', 'Flabebe-White', 'Flabebe-Yellow', 'Floette', 'Floette-Blue', 'Floette-Orange', 'Floette-White', 'Floette-Yellow', 'Florges', 'Florges-Blue', 'Florges-Orange', 'Florges-White', 'Florges-Yellow', 'Spritzee', 'Aromatisse', 'Swirlix', 'Slurpuff', 'Dedenne', 'Carbink', 'Cutiefly', 'Ribombee', 'Togedemaru']
Undiscovered = ['Nidorina', 'Nidoqueen', 'Articuno', 'Zapdos', 'Moltres', 'Mewtwo', 'Mewtwo-Mega-X', 'Mewtwo-Mega-Y', 'Mew', 'Pichu', 'Cleffa', 'Igglybuff', 'Togepi', 'Unown', 'Tyrogue', 'Smoochum', 'Elekid', 'Magby', 'Raikou', 'Entei', 'Suicune', 'Lugia', 'Ho-Oh', 'Celebi', 'Azurill', 'Wynaut', 'Regirock', 'Regice', 'Registeel', 'Latias', 'Latias-Mega', 'Latios', 'Latios-Mega', 'Kyogre', 'Kyogre-Primal', 'Groudon', 'Groudon-Primal', 'Rayquaza', 'Rayquaza-Mega', 'Jirachi', 'Deoxys', 'Deoxys-Attack', 'Deoxys-Defense', 'Deoxys-Speed', 'Budew', 'Chingling', 'Bonsly', 'Mime Jr.', 'Happiny', 'Munchlax', 'Riolu', 'Mantyke', 'Uxie', 'Mesprit', 'Azelf', 'Dialga', 'Palkia', 'Heatran', 'Regigigas', 'Giratina', 'Giratina-Origin', 'Cresselia', 'Darkrai', 'Shaymin', 'Shaymin-Sky', 'Arceus', 'Arceus-Bug', 'Arceus-Dark', 'Arceus-Dragon', 'Arceus-Electric', 'Arceus-Fairy', 'Arceus-Fighting', 'Arceus-Fire', 'Arceus-Flying', 'Arceus-Ghost', 'Arceus-Grass', 'Arceus-Ground', 'Arceus-Ice', 'Arceus-Poison', 'Arceus-Psychic', 'Arceus-Rock', 'Arceus-Steel', 'Arceus-Water', 'Victini', 'Cobalion', 'Terrakion', 'Virizion', 'Tornadus', 'Tornadus-Therian', 'Thundurus', 'Thundurus-Therian', 'Reshiram', 'Zekrom', 'Landorus', 'Landorus-Therian', 'Kyurem', 'Kyurem-Black', 'Kyurem-White', 'Keldeo', 'Meloetta', 'Genesect', 'Genesect-Douse', 'Genesect-Shock', 'Genesect-Burn', 'Genesect-Chill', 'Greninja-Ash', 'Floette-Eternal', 'Xerneas', 'Yveltal', 'Zygarde', 'Zygarde-10%', 'Zygarde-Complete', 'Diancie', 'Diancie-Mega', 'Hoopa', 'Hoopa-Unbound', 'Volcanion', 'Type: Null', 'Silvally', 'Silvally-Bug', 'Silvally-Dark', 'Silvally-Dragon', 'Silvally-Electric', 'Silvally-Fairy', 'Silvally-Fighting', 'Silvally-Fire', 'Silvally-Flying', 'Silvally-Ghost', 'Silvally-Grass', 'Silvally-Ground', 'Silvally-Ice', 'Silvally-Poison', 'Silvally-Psychic', 'Silvally-Rock', 'Silvally-Steel', 'Silvally-Water', 'Tapu Koko', 'Tapu Lele', 'Tapu Bulu', 'Tapu Fini', 'Cosmog', 'Cosmoem', 'Solgaleo', 'Lunala', 'Nihilego', 'Buzzwole', 'Pheromosa', 'Xurkitree', 'Celesteela', 'Kartana', 'Guzzlord', 'Necrozma', 'Necrozma-Dusk-Mane', 'Necrozma-Dawn-Wings', 'Necrozma-Ultra', 'Magearna', 'Marshadow', 'Poipole', 'Naganadel', 'Stakataka', 'Blacephalon', 'Zeraora']
#Water1 = ['Psyduck', 'Golduck', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Seel', 'Dewgong', 'Horsea', 'Seadra', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Dratini', 'Dragonair', 'Dragonite', 'Marill', 'Azumarill', 'Politoed', 'Wooper', 'Quagsire', 'Corsola', 'Remoraid', 'Octillery', 'Delibird', 'Mantine', 'Kingdra', 'Lotad', 'Lombre', 'Ludicolo', 'Wingull', 'Pelipper', 'Surskit', 'Masquerain', 'Corphish', 'Crawdaunt', 'Feebas', 'Milotic', 'Spheal', 'Sealeo', 'Walrein', 'Clamperl', 'Huntail', 'Gorebyss', 'Relicanth', 'Piplup', 'Prinplup', 'Empoleon', 'Bidoof', 'Bibarel', 'Buizel', 'Floatzel', 'Shellos', 'Gastrodon', 'Phione', 'Manaphy', 'Tympole', 'Palpitoad', 'Seismitoad', 'Tirtouga', 'Carracosta', 'Ducklett', 'Swanna', 'Alomomola', 'Stunfisk', 'Froakie', 'Frogadier', 'Greninja', 'Inkay', 'Malamar', 'Skrelp', 'Dragalge', 'Clauncher', 'Clawitzer', 'Popplio', 'Brionne', 'Primarina', 'Mareanie', 'Toxapex', 'Dewpider', 'Araquanid', 'Pyukumuku']
Human_Like = ['Abra', 'Kadabra', 'Alakazam', 'Alakazam-Mega', 'Machop', 'Machoke', 'Machamp', 'Drowzee', 'Hypno', 'Hitmonlee', 'Hitmonchan', 'Mr. Mime', 'Jynx', 'Electabuzz', 'Magmar', 'Hitmontop', 'Makuhita', 'Hariyama', 'Sableye', 'Sableye-Mega', 'Meditite', 'Medicham', 'Medicham-Mega', 'Volbeat', 'Illumise', 'Spinda', 'Cacnea', 'Cacturne', 'Chimchar', 'Monferno', 'Infernape', 'Buneary', 'Lopunny', 'Lopunny-Mega', 'Lucario', 'Lucario-Mega', 'Croagunk', 'Toxicroak', 'Electivire', 'Magmortar', 'Timburr', 'Gurdurr', 'Conkeldurr', 'Throh', 'Sawk', 'Gothita', 'Gothorita', 'Gothitelle', 'Elgyem', 'Beheeyem', 'Mienfoo', 'Mienshao', 'Pawniard', 'Bisharp', 'Pancham', 'Pangoro', 'Hawlucha']
#Water3 = ['Tentacool', 'Tentacruel', 'Shellder', 'Cloyster', 'Krabby', 'Kingler', 'Staryu', 'Starmie', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Binacle', 'Barbaracle', 'Crabrawler', 'Crabominable']
Mineral = ['Geodude', 'Geodude-Alola', 'Graveler', 'Graveler-Alola', 'Golem', 'Golem-Alola', 'Magnemite', 'Magneton', 'Onix', 'Voltorb', 'Electrode', 'Porygon', 'Sudowoodo', 'Steelix', 'Steelix-Mega', 'Porygon2', 'Shedinja', 'Nosepass', 'Lunatone', 'Solrock', 'Baltoy', 'Claydol', 'Snorunt', 'Glalie', 'Glalie-Mega', 'Beldum', 'Metang', 'Metagross', 'Metagross-Mega', 'Bronzor', 'Bronzong', 'Magnezone', 'Porygon-Z', 'Probopass', 'Froslass', 'Roggenrola', 'Boldore', 'Gigalith', 'Dwebble', 'Crustle', 'Yamask', 'Cofagrigus', 'Trubbish', 'Garbodor', 'Vanillite', 'Vanillish', 'Vanilluxe', 'Ferroseed', 'Ferrothorn', 'Klink', 'Klang', 'Klinklang', 'Cryogonal', 'Golett', 'Golurk', 'Honedge', 'Doublade', 'Aegislash', 'Carbink', 'Klefki', 'Minior', 'Minior-Orange', 'Minior-Yellow', 'Minior-Green', 'Minior-Blue', 'Minior-Indigo', 'Minior-Violet', 'Minior-Meteor', 'Dhelmise']
Amorphous = ['Grimer', 'Grimer-Alola', 'Muk', 'Muk-Alola', 'Gastly', 'Haunter', 'Gengar', 'Gengar-Mega', 'Koffing', 'Weezing', 'Misdreavus', 'Wobbuffet', 'Slugma', 'Magcargo', 'Ralts', 'Kirlia', 'Gardevoir', 'Gardevoir-Mega', 'Gulpin', 'Swalot', 'Castform', 'Shuppet', 'Banette', 'Banette-Mega', 'Duskull', 'Dusclops', 'Chimecho', 'Drifloon', 'Drifblim', 'Mismagius', 'Spiritomb', 'Gallade', 'Gallade-Mega', 'Dusknoir', 'Rotom', 'Rotom-Heat', 'Rotom-Wash', 'Rotom-Frost', 'Rotom-Fan', 'Rotom-Mow', 'Yamask', 'Cofagrigus', 'Solosis', 'Duosion', 'Reuniclus', 'Frillish', 'Jellicent', 'Tynamo', 'Eelektrik', 'Eelektross', 'Litwick', 'Lampent', 'Chandelure', 'Phantump', 'Trevenant', 'Pumpkaboo', 'Pumpkaboo-Small', 'Pumpkaboo-Large', 'Pumpkaboo-Super', 'Gourgeist', 'Gourgeist-Small', 'Gourgeist-Large', 'Gourgeist-Super', 'Sandygast', 'Palossand', 'Mimikyu']
#Water2 = ['Goldeen', 'Seaking', 'Magikarp', 'Gyarados', 'Gyarados-Mega', 'Chinchou', 'Lanturn', 'Qwilfish', 'Carvanha', 'Sharpedo', 'Sharpedo-Mega', 'Barboach', 'Whiscash', 'Luvdisc', 'Finneon', 'Lumineon', 'Basculin', 'Basculin-Blue-Striped', 'Wishiwashi', 'Bruxish']
Ditto = ['Ditto']

#List of legendaries for Mono-Lengendary
legend = ['Articuno', 'Zapdos', 'Moltres', 'Mewtwo', 'Mewtwo-Mega-X', 'Mewtwo-Mega-Y', 'Mew', 'Raikou', 'Entei', 'Suicune', 'Lugia', 'Ho-Oh', 'Celebi', 'Regirock', 'Regice', 'Registeel', 'Latias', 'Latias-Mega', 'Latios', 'Latios-Mega', 'Kyogre', 'Kyogre-Primal', 'Groudon', 'Groudon-Primal', 'Rayquaza', 'Rayquaza-Mega', 'Jirachi', 'Deoxys', 'Deoxys-Attack', 'Deoxys-Defense', 'Deoxys-Speed', 'Dialga', 'Palkia', 'Heatran', 'Regigigas', 'Giratina', 'Giratina-Origin', 'Cresselia', 'Darkrai', 'Shaymin', 'Shaymin-Sky', 'Arceus', 'Arceus-Bug', 'Arceus-Dark', 'Arceus-Dragon', 'Arceus-Electric', 'Arceus-Fairy', 'Arceus-Fighting', 'Arceus-Flying', 'Arceus-Ghost', 'Arceus-Grass', 'Arceus-Ground', 'Arceus-Ice', 'Arceus-Poison', 'Arceus-Psychic', 'Arceus-Rock', 'Arceus-Steel', 'Arceus-Water', 'Victini', 'Cobalion', 'Terrakion', 'Virizion', 'Tornadus', 'Tornadus-Therian', 'Thundurus', 'Thundurus-Therian', 'Reshiram', 'Zekrom', 'Landorus', 'Landorus-Therian', 'Kyurem', 'Kyurem-Black', 'Kyurem-White', 'Keldeo', 'Meloetta', 'Genesect', 'Genesect-Douse', 'Genesect-Shock', 'Genesect-Burn', 'Genesect-Chill', 'Xerneas', 'Yveltal', 'Zygarde', 'Zygarde-10%', 'Zygarde-Complete', 'Diancie', 'Diancie-Mega', 'Hoopa', 'Hoopa-Unbound', 'Volcanion', 'Tapu Koko', 'Tapu Lele', 'Tapu Bulu', 'Tapu Fini', 'Cosmog', 'Cosmoem', 'Solgaleo', 'Lunala', 'Nihilego', 'Buzzwole', 'Pheromosa', 'Xurkitree', 'Celesteela', 'Kartana', 'Guzzlord', 'Necrozma', 'Necrozma-Dusk-Mane', 'Necrozma-Dawn-Wings', 'Necrozma-Ultra', 'Magearna', 'Marshadow', 'Poipole', 'Naganadel', 'Stakataka', 'Blacephalon', 'Zeraora', 'Mesprit', 'Azelf', 'Uxie']

#Function that runs when you click run program button
def generate_team():
    m = "" #Empty string for later use
    story_txt.delete(0.0, END) #Removes message saying it is complete
    va13g = va13.get() #Gets an item from a dropdown menu
    if va13g == "Random Monotype": # If it is "Random Monotype", it chooses a random mono- to use for later
        va13g = random.choice(monotype)
        print("Your random Mono- is " + va13g)
        
    if va13g == "Random Mono Generation": # If it is "Random Mono Generation", it chooses a random mono- to use for later
        va13g = random.choice(monogen)
        print("Your random Mono- is " + va13g)        

    if va13g == "Random Mono Egg Group": # If it is "Random Mono Egg Group", it chooses a random mono- to use for later
        va13g = random.choice(monoeg)
        print("Your random Mono- is " + va13g)     

    if va13g == "Random Mono Colour": # If it is "Random Mono Colour", it chooses a random mono- to use for later
        va13g = random.choice(monocolour)
        print("Your random Mono- is " + va13g)  

    if va13g == "Random Mono-": # If it is "Random Mono-", it chooses a random mono- to use for later
        va13g = random.choice(monoany)
        print("Your random Mono- is " + va13g) 
 
    for number_mon in range(6): #Runs this bit 6 times for 6 pokemon, change the 6 for more of less pokemon
        passingisgo = False #Lets a loop run in the future
        movess = [] #Empty list, used later
        
        #Gets some of the items from the dropdown menu, and formats them for use
        va4g = va4.get()
        rad1g = rado.get()
        eg = e1.get()
        eg = eg.title()
        eg2 = e11.get()
        eg2 = eg2.title()
        eg3 = e3.get()
        eg3 = eg3.title()
        va7g = va7.get()
        va8g = va8.get()
        etwog = etwo.get()
        ethreeg = ethree.get()
        va9g = va9.get()
        va10g = va10.get()
        mon = []
        va11g = va11.get()

        #Shows the value of each smogon tier
        Uber = 5
        OU = 4
        UU = 3
        RU = 2
        NU = 1
        PU = 0
        LC = -1

        #If you select one tier it will add that to the list of pokemon to use
        if va10g == "Thats it":
            if va9g == "Uber":
                mon.extend(uber)
        if va10g == "Thats it":
            if va9g == "OU":
                mon.extend(ou)
        if va10g == "Thats it":
            if va9g == "UU":
                mon.extend(uu)
                
        if va10g == "Thats it":
            if va9g == "RU":
                mon.extend(ru)

        if va10g == "Thats it":
            if va9g == "NU":
                mon.extend(nu)

        if va10g == "Thats it":
            if va9g == "PU":
                mon.extend(pu)

        if va10g == "Thats it":
            if va9g == "LC":
                mon.extend(lc)

        if mon == []:  # If you don't not pick "That's it", then it selects the relevant tiers to use
            if va9g == "Uber":
                x = 5
            elif va9g == "OU":
                x = 4
            elif va9g == "UU":
                x = 3
            elif va9g == "RU":
                x = 2
            elif va9g == "NU":
                x = 1
            elif va9g == "PU":
                x = 0
            elif va9g == "LC":
                x = -1
            else:
                print("error") #If something goes wrong it prints (Shows) "error"

            if va10g == "Lower":
                mon.extend(lc)
                if OU <= x:
                    mon.extend(ou)
                if Uber <= x:
                    mon.extend(uber)
                if UU <= x:
                    mon.extend(uu)
                if RU <= x:
                    mon.extend(ru)
                if NU <= x:
                    mon.extend(nu)
                if PU <= x:
                    mon.extend(pu)

            if va10g == "Higher":
                mon.extend(uber)
                if OU >= x:
                    mon.extend(ou)
                if UU >= x:
                    mon.extend(uu)
                if RU >= x:
                    mon.extend(ru)
                if NU >= x:
                    mon.extend(nu)
                if PU >= x:
                    mon.extend(pu)
                if LC >= x:
                    mon.extend(lc)

        #Gets what Mono- you would like, and adds that to the list of pokemon to use

        if va13g == "Grass":
            mon.extend(Grassm)
        if va13g == "Fire":
            mon.extend(Firem)
        if va13g == "Water":
            mon.extend(Waterm)
        if va13g == "Bug":
            mon.extend(Bugm)
        if va13g == "Normal":
            mon.extend(Normalm)
        if va13g == "Dark":
            mon.extend(Darkm)
        if va13g == "Poison":
            mon.extend(Poisonm)
        if va13g == "Electric":
            mon.extend(Electricm)
        if va13g == "Ground":
            mon.extend(Groundm)
        if va13g == "Ice":
            mon.extend(Icem)
        if va13g == "Fairy":
            mon.extend(Fairym)
        if va13g == "Fighting":
            mon.extend(Fightingm)
        if va13g == "Psychic":
            mon.extend(Psychicm)
        if va13g == "Rock":
            mon.extend(Rockm)
        if va13g == "Ghost":
            mon.extend(Ghostm)
        if va13g == "Dragon":
            mon.extend(Dragonm)
        if va13g == "Steel":
            mon.extend(Steelm)
        if va13g == "Flying":
            mon.extend(Flyingm)
        if va13g == "Gen 1":
            mon.extend(Gen1m)
        if va13g == "Gen 2":
            mon.extend(Gen2m)
        if va13g == "Gen 3":
            mon.extend(Gen3m)
        if va13g == "Gen 4":
            mon.extend(Gen4m)
        if va13g == "Gen 5":
            mon.extend(Gen5m)
        if va13g == "Gen 6":
            mon.extend(Gen6m)
        if va13g == "Gen 7":
            mon.extend(Gen7m)
        if va13g == "Monster (Egg Group)":
            mon.extend(Monster)
        if va13g == "Grass (Egg Group)":
            mon.extend(Grassz)
        if va13g == "Dragon (Egg Group)":
            mon.extend(Dragonz)
        if va13g == "All Water (Egg Groups)":
            mon.extend(Waterz)
        if va13g == "Bug (Egg Group)":
            mon.extend(Bugz)
        if va13g == "Flying (Egg Group)":
            mon.extend(Flyingz)
        if va13g == "Field (Egg Group)":
            mon.extend(Field)
        if va13g == "Fairy (Egg Group)":
            mon.extend(Fairyz)
        if va13g == "Undiscovered (Egg Group)":
            mon.extend(Undiscovered)
        if va13g == "Human-Like (Egg Group)":
            mon.extend(Human_Like)
        if va13g == "Mineral (Egg Group)":
            mon.extend(Mineral)
        if va13g == "Amorphous (Egg Group)":
            mon.extend(Amorphous)
        if va13g == "Ditto (Egg Group)":
            mon.extend(Ditto)
        if va13g == "Green":
            mon.extend(Green)
        if va13g == "Red":
            mon.extend(Red)
        if va13g == "Black":
            mon.extend(Black)
        if va13g == "Blue":
            mon.extend(Blue)
        if va13g == "White":
            mon.extend(White)
        if va13g == "Brown":
            mon.extend(Brown)
        if va13g == "Yellow":
            mon.extend(Yellow)
        if va13g == "Purple":
            mon.extend(Purple)
        if va13g == "Pink":
            mon.extend(Pink)
        if va13g == "Grey":
            mon.extend(Grey)
        if va13g == "Lengendary":
            mon.extend(legend)
        if va13g == "None":
            mon.extend(p)

        #I was bored when I made these variable names
        asdf = True
        meep = []
        if asdf == True: #This does not need to exist
            for i in mon: #for every pokemon in the list
                try:
                    t = mon.count(i) #Will check for copys in the list, and remove them
                    if t > 1:
                        if i not in meep:
                            meep.append(i)
                except:
                    pass
            if len(meep) > 0: #Uses this list if there are pokemon in it
                passingisgo = True
            else:
                 pass

        try:
            ethreeg = int(ethreeg) #Gets numbers to use for levels
            etwog = int(etwog)
            if etwog < 1 or ethreeg > 100: #Forces an error if your using invalid error
                q = 1 / 0
        except: #If there was an error it uses 1 to 100 and show an error in the box
            e44.delete(0.0, END)
            e44.insert(0.0, "Not valid Numbers, Using 1 and 100")
            ethreeg = 100
            etwog = 1

        if passingisgo == False: #If there are no pookemon it will select from all pokemon and show an error in the box
            poke = random.choice(p)
            e55.delete(0.0, END)
            e55.insert(END, "No Pokemon Found, using all Pokemon")            
        else:
            poke = random.choice(meep) #Otherwise it uses the wanted pokemon
        gender = random.choice(gend) #Picks a random gender
        item = random.choice(items) #Picks a random item, may be changed later

        #Variables for later
        t1 = False
        t2 = False
        t3 = False
        
        #Gets items from drop-down Menus
        va5g = va5.get()
        va6g = va6.get()
        pas = False
        rad1g3 = radit.get()

        if eg3 in items: #If the item to force on exists it checks whether you want it on all pokemon or just one, and gives it to them, them it lets it pass a later loop
            if rad1g3 == "One Pokemon":
                if number_mon == 5:
                    item = eg3
                    pas = True
            else:
                item = eg3
                pas = True
        else:
            e33.delete(0.0, END)
            e33.insert(END, "Item not found") #If the item is not found, it showss an error in the right box


                

        if va3.get() == "No":
            while item in useless: #If you don't want useless items then it keeps choosing another item until it is not
                item = random.choice(items)

        # CHooses a random ability, may be changed later
        abil = random.choice(abils)
        try: #Trys to randomize a level from giveen levels, gives an error if it can't
            level = random.randint(etwog, ethreeg)
        except:
            level = random.randint(1, 100)
            e44.delete(0.0, END)
            e44.insert(0.0, "Not valid Numbers, Using 1 and 100")
        shiny = random.choice(shinys) #Picks whether it should be shiny, may be changed later
        happy = random.randint(0, 255) #Chooses a random happiness value
        nature = random.choice(natures) #Chooses a random nature

        ##va4g = types of z move and va8 = move tiers

        #If you want status and attacking moves, then it picks moves from other options
        if va11g == "All":

            if va4g == "All" and va8g == "All Tiers":
                movess.extend(all_z)
                movess.extend(moves)

            if va4g == "Only Signature" and va8g == "All Tiers":
                movess.extend(sig_z)
                movess.extend(moves)            

            if va4g == "None" and va8g == "All Tiers":
                movess.extend(moves)
                
            if va4g == "All" and va8g == "Only 1":
                movess.extend(all_z)
                movess.extend(tier1m)
                

            if va4g == "Only Signature" and va8g == "Only 1":
                movess.extend(sig_z)
                movess.extend(tier1m)
                

            if va4g == "None" and va8g == "Only 1":
                movess.extend(tier1m)
                

            if va4g == "All" and va8g == "Only 2":
                movess.extend(all_z)
                movess.extend(tier2m)
                

            if va4g == "Only Signature" and va8g == "Only 2":
                movess.extend(sig_z)
                movess.extend(tier2m)            

            if va4g == "None" and va8g == "Only 2":
                movess.extend(tier2m)

        else: #Otherwise it adds moves which are status, or not status, depending on option
            if va11g == "Only Attacking (No Z-Moves)":
                movess.extend(notstatmov)
            else:
                movess.extend(statmov)


        # Picks random moves for each slot depending on critera
        
        move1 = random.choice(movess)
        move2 = random.choice(movess)
        move3 = random.choice(movess)
        move4 = random.choice(movess)

        #Does not let you pass a loop later
        pa = False

        
        if eg in moves: #Checks if you want a move on a pokemon, how many pokemon, and gives it if it is a valid move, then lets you pass a loop later
            if rad1g == "One Pokemon":
                if number_mon == 5:
                    move4 = eg
                    pa = True
            else:
                move4 = eg
                pa = True
                
        else: #Otherwise it gives an error in the right box
            e12.delete(0.0, END)
            e12.insert(END, "Move not found")



        #If you only want Signature or no Z-Moves it will keep randomizing until it is not, unless you forced a Z-Move on a pokemon
        if va4g == "Only Signature":
            while move1 in bad_z:
                move1 = random.choice(moves)
        if va4g == "Only Signature":
            while move2 in bad_z:
                move2 = random.choice(moves)
        if va4g == "Only Signature":
            while move3 in bad_z:
                move3 = random.choice(moves)
        if pa != True:                
            if va4g == "Only Signature":
                while move4 in bad_z:
                    move4 = random.choice(moves)
        if va4g == "None":
            while move1 in sig_z or move1 in bad_z:
                move1 = random.choice(moves)
        if va4g == "None":
            while move2 in sig_z or move2 in bad_z:
                move2 = random.choice(moves)
        if va4g == "None":
            while move3 in sig_z or move3 in bad_z:
                move3 = random.choice(moves)
        if pa != True:                
            if va4g == "None":
                while move4 in sig_z or move4 in bad_z:
                    move4 = random.choice(moves)

                    
        orp = False

        rad1g2 = radab.get() #Gets a value from a dropdwon menu

        
        if eg2 in abils: #If you give it a valid ability it checks if you want it on all or one pokemon and gives them it
            if rad1g2 == "One Pokemon":
                if number_mon == 5:
                   abil = eg2
                   orp = True
            else:
                abil = eg2
                orp = True

        else: #If there is an error then it shows an error message in the box
            e121.delete(0.0, END)
            e121.insert(END, "Ability not found")

        # Assigns variables according to given dropdown menu for later use

        if va5g == "All Tiers":
            t1 = True
            t2 = True
            t3 = True

        if va5g == "1 + 2":
            t1 = True
            t2 = True
            t3 = False

        if va5g == "2 + 3":
            t1 = False
            t2 = True
            t3 = True
            
        if va5g == "Only 1":
            t1 = True
            t2 = False
            t3 = False

        if va5g == "Only 2":
            t1 = False
            t2 = True
            t3 = False

        if va5g == "Only 3":
            t1 = False
            t2 = False
            t3 = True

        t11 = 0
        t22 = 0
        t33 = 0   

        # Assigns variables according to given dropdown menu for later use

        if va7g == "All Tiers":
            t11 = True
            t22 = True
            t33 = True

        if va7g == "1 + 2":
            t11 = True
            t22 = True
            t33 = False

        if va7g == "2 + 3":
            t11 = False
            t22 = True
            t33 = True
            
        if va7g == "Only 1":
            t11 = True
            t22 = False
            t33 = False

        if va7g == "Only 2":
            t11 = False
            t22 = True
            t33 = False

        if va7g == "Only 3":
            t11 = False
            t22 = False
            t33 = True

        while pas != True: #While your item is in an unwanted tier it will keep randomizing it.
            
            if item in tier1:
                if t1 == True:
                    pas = True
            
            if item in tier2:
                if t2 == True:
                    pas = True
            
            if item in tier3:
                if t3 == True:
                    pas = True
                    
            if item in pokespec:
                if va6g == "Yes":
                    pas = True
                    
            if item in useless:
                if va3.get() == "Yes":
                    pas = True
                
            if pas == False:
                item = random.choice(items)

        porg = False

        if orp != True:
        
            while porg != True: #While your ability is in an unwanted tier it will keep randomizing it.
                
                if abil in tieroneab:
                    if t11 == True:
                        porg = True

                if abil in tiertwoab:
                    if t22 == True:
                        porg = True

                if abil in tierthreeab:
                    if t33 == True:
                        porg = True

                if porg == False:
                    abil = random.choice(abils)
        
        va12g = va12.get() #Gets value from a Dropdown Menu
        
        if va12g == "Yes": #If you want to force Z-Move to be useful, and you have a Z-Crytal, then it picks a random move from the according type

            if item == "Buginium Z":
                move1 = random.choice(bug)

            if item == "Darkinium Z":
                move1 = random.choice(dark)

            if item == "Dragonium Z":
                move1 = random.choice(dragon)

            if item == "Electrium Z":
                move1 = random.choice(elec)

            if item == "Fairium Z":
                move1 = random.choice(fai)

            if item == "Fightinium Z":
                move1 = random.choice(fight)

            if item == "Firium Z":
                move1 = random.choice(fire)

            if item == "Flyinium Z":
                move1 = random.choice(fly)

            if item == "Ghostium Z":
                move1 = random.choice(ghost)

            if item == "Grassium Z":
                move1 = random.choice(grass)

            if item == "Groundium Z":
                move1 = random.choice(ground)

            if item == "Icium Z":
                move1 = random.choice(ic)

            if item == "Normalium Z":
                move1 = random.choice(norm)

            if item == "Poisonium Z":
                move1 = random.choice(pois)

            if item == "Psychium Z":
                move1 = random.choice(psy)
                
            if item == "Rockium Z":
                move1 = random.choice(rock)

            if item == "Steelium Z":
                move1 = random.choice(stel)

            if item == "Waterium Z":
                move1 = random.choice(wat)


        shinyny = va1.get() #Gets a value from the dropdown menu
        
        
        if shinyny == "No": #If you don't want to randomize shinys, then it checks if you want all pokemon be shiny or not, then it sets it
            shiny = va2.get()
                
        # Sets the variable "story" to the pokemon showdown format, and makes the pokemon in the team! 
        
        story = ("\n" + str(poke) + " (" + gender + ") @ " + item + "\nAbility: " + abil + "\nLevel: " + str(level) + "\nShiny: " + shiny + "\nHappiness: " + str(happy) + "\nEVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe\n" + nature + " Nature\n" + "- " + move1 + "\n" + "- " + move2 + "\n" + "- " + move3 + "\n" + "- " + move4 + "\n")


        m += story #Adds the pokemon to the total team.
    

    r = Tk() #Makes a non-existant window for tkinter, for copying to clipboard
    r.withdraw() #Does not show the window
    r.clipboard_clear() #Clears what is currently on the clipboard
    r.clipboard_append(m) #Adds your team to the clipboard
    r.update() #Lets you keep your clipboard when the window disappears
    r.destroy() #Gets rid of the non-existant window

    story_txt.insert(0.0, "Your team has been copied to the clipboard") #Gives a message saying it is done, and sets it to the right box

    story_txt.after(10000, deleteing) #Runs a command in 10000 somethings

    

def deleteing(): #See above to see when this is run
    # Deletes all the error messages from all the boxes, and the message saying it is done
    story_txt.delete(0.0, END)
    e12.delete(0.0, END)
    e121.delete(0.0, END)
    e33.delete(0.0, END)
    e44.delete(0.0, END)
    e55.delete(0.0, END)

master = Tk() #Creates a main window for all the GUI widgets
master.title("Hackmon Random Team Generator") #Sets the title for the window

tabs = ttk.Notebook() #Creates a list of tabs
tabs.grid(row = 17, column = 0, rowspan = 50, columnspan = 50, sticky = "NESW") #Puts it on the window
#Adds a bunch of tabs to the list of tabs
tab1 = ttk.Frame(tabs)
tabs.add(tab1, text = "Home/Run Program")
tabpoke = ttk.Frame(tabs)
tabs.add(tabpoke, text = "Pokemon Options")
tabitem = ttk.Frame(tabs)
tabs.add(tabitem, text = "Item Options")
tabab = ttk.Frame(tabs)
tabs.add(tabab, text = "Ability Options")
tabmove = ttk.Frame(tabs)
tabs.add(tabmove, text = "Move Options")
tabo = ttk.Frame(tabs)
tabs.add(tabo, text = "Other Options")

# Creates the main button which runs the main part of the program
b = Button(tab1, text = "Generate team, Ctrl + V to paste", command = generate_team).grid(row = 0, column = 0, sticky = W)

#Creates the boxes to send error messages, and message saying the team is done
story_txt = Text(tab1, wrap = WORD, height = 1, width = 42)
story_txt.grid(row = 0, column = 1, columnspan = 1)
e12 = Text(tabmove, wrap = WORD, height = 1, width = 30)
e12.grid(row = 7, column = 2, columnspan = 1)
e121 = Text(tabab, wrap = WORD, height = 1, width = 30)
e121.grid(row = 8, column = 2, columnspan = 1)
e33 = Text(tabitem, wrap = WORD, height = 1, width = 30)
e33.grid(row = 9, column = 2, columnspan = 1)
e44 = Text(tabo, wrap = WORD, height = 1, width = 34)
e44.grid(row = 12, column = 4, columnspan = 1, sticky = "W")
e55 = Text(tabpoke, wrap = WORD, height = 1, width = 35)
e55.grid(row = 18, column = 0, columnspan = 1, sticky = "W")

# Creates a list for every dropdown menu
yn = ["Yes", "No"]
z_opsl = ["All", "Only Signature", "None"]
tiers = ["All Tiers", "1 + 2", "2 + 3", "Only 1", "Only 2", "Only 3"]
tiers2 = ["All Tiers", "1 + 2", "2 + 3", "Only 1", "Only 2", "Only 3"]
tiers3 = ["All Tiers", "Only 1", "Only 2"]
smotiers = ["Uber", "OU", "UU", "RU", "NU", "PU", "LC"]
smoup = ["Higher", "Lower", "Thats it"]
typemove = ["All", "Only Attacking (No Z-Moves)", "Only Status (No Z-Moves)"]
tips = ['None', "Random Mono-", 'Lengendary', "Random Monotype", 'Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water', "Random Mono Generation", "Gen 1", "Gen 2", "Gen 3", "Gen 4", "Gen 5", "Gen 6", "Gen 7", "Random Mono Egg Group", 'All Water (Egg Groups)', 'Amorphous (Egg Group)', 'Bug (Egg Group)', 'Ditto (Egg Group)', 'Dragon (Egg Group)', 'Fairy (Egg Group)', 'Field (Egg Group)', 'Flying (Egg Group)', 'Grass (Egg Group)', 'Human-Like (Egg Group)', 'Mineral (Egg Group)', 'Monster (Egg Group)', 'Undiscovered (Egg Group)', "Random Mono Colour", 'Black', 'Blue', 'Brown', 'Green', 'Grey', 'Pink', 'Purple', 'Red', 'White', 'Yellow']
monotype = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']
monogen = ["Gen 1", "Gen 2", "Gen 3", "Gen 4", "Gen 5", "Gen 6", "Gen 7"]
monoeg = ['All Water (Egg Groups)', 'Amorphous (Egg Group)', 'Bug (Egg Group)', 'Ditto (Egg Group)', 'Dragon (Egg Group)', 'Fairy (Egg Group)', 'Field (Egg Group)', 'Flying (Egg Group)', 'Grass (Egg Group)', 'Human-Like (Egg Group)', 'Mineral (Egg Group)', 'Monster (Egg Group)', 'Undiscovered (Egg Group)']
monocolour = ['Black', 'Blue', 'Brown', 'Green', 'Grey', 'Pink', 'Purple', 'Red', 'White', 'Yellow']
monoany = ['Lengendary', 'Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water', "Gen 1", "Gen 2", "Gen 3", "Gen 4", "Gen 5", "Gen 6", "Gen 7", 'All Water (Egg Groups)', 'Amorphous (Egg Group)', 'Bug (Egg Group)', 'Ditto (Egg Group)', 'Dragon (Egg Group)', 'Fairy (Egg Group)', 'Field (Egg Group)', 'Flying (Egg Group)', 'Grass (Egg Group)', 'Human-Like (Egg Group)', 'Mineral (Egg Group)', 'Monster (Egg Group)', 'Undiscovered (Egg Group)', 'Black', 'Blue', 'Brown', 'Green', 'Grey', 'Pink', 'Purple', 'Red', 'White', 'Yellow']


#Creates Labels saying what every dropdown menu does
Label(tabo, text = "Do you want to randomize shinies?").grid(row = 1, column = 0, sticky = "W")
Label(tabo, text = "Do you want the default shiny option to be shiny? (Only applies if yes above)").grid(row = 2, column = 0, sticky = "W")
Label(tabitem, text = "Do you want to include smogon's list of useless items? (Such as Helix Fossil)").grid(row = 3, column = 0, sticky = "W")
Label(tabmove, text = "Do you want to include Z-moves?").grid(row = 4, column = 0, sticky = "W")
Label(tabitem, text = "What tiers of items would you like to use?").grid(row = 5, column = 0, sticky = "W")
Label(tabitem, text = "Do you want to include pokemon specific items?").grid(row = 6, column = 0, sticky = "W")
Label(tabmove, text = "Do you want to force a move on a pokemon? (And what move)").grid(row = 7, column = 0, sticky = "W")
Label(tabab, text = "Do you want to force an ability on a pokemon? (And what ability)").grid(row = 8, column = 0, sticky = "W")
Label(tabitem, text = "Do you want to force a item on a pokemon? (And what item)").grid(row = 9, column = 0, sticky = "W")
Label(tabab, text = "What tiers of abilities do you want to use?").grid(row = 10, column = 0, sticky = "W")
Label(tabmove, text = "What tiers of moves do you want to use?").grid(row = 11, column = 0, sticky = "W")
Label(tabo, text = "What range of levels would you like to randomize?").grid(row = 12, column = 0, sticky = "W")
Label(tabpoke, text = "What smogon tiers of pokemon would you like to use (Valid from May 2018) (PU includes NFE)?").grid(row = 13, column = 0, sticky = "W")
Label(tabmove, text = "What kind of moves would you like to include (Overrides all other move options)?").grid(row = 14, column = 0, sticky = "W")
Label(tabmove, text = "Do you want standard Z-Crystals to be forced to be useful (Overrides all other move options)?").grid(row = 15, column = 0, sticky = "W")
Label(tabpoke, text = "Do you want to do a mono-...?").grid(row = 16, column = 0, sticky = "W")

# Sets the default option for every dropdown menu
va1 = StringVar()
va1.set("Yes")

va2 = StringVar()
va2.set("No")

va3 = StringVar()
va3.set("Yes")

va4 = StringVar()
va4.set("All")

va5 = StringVar()
va5.set("All Tiers")

va6 = StringVar()
va6.set("Yes")

va7 = StringVar()
va7.set("All Tiers")

va8 = StringVar()
va8.set("All Tiers")

va9 = StringVar()
va9.set("Uber")

va10 = StringVar()
va10.set("Lower")

va11 = StringVar()
va11.set("All")

va12 = StringVar()
va12.set("No")

va13 = StringVar()
va13.set("None")


# Creates the dropdown menus, and puts then on the right tabs, using the right lists
mono = OptionMenu(tabpoke, va13, *tips)
mono.grid(row = 16, column = 1, sticky = "E")

mtier = OptionMenu(tabmove, va8, *tiers3)
mtier.grid(row = 11, column = 1, sticky = "E")

forz = OptionMenu(tabmove, va12, *yn)
forz.grid(row = 15, column = 1, sticky = "E")

movety = OptionMenu(tabmove, va11, *typemove)
movety.grid(row = 14, column = 1, sticky = "E")

rand_shiny_yn = OptionMenu(tabo, va1, *yn)
rand_shiny_yn.grid(row = 1, column = 1, sticky = "E")

shiny_defualt_yn = OptionMenu(tabo, va2, *yn)
shiny_defualt_yn.grid(row = 2, column = 1, sticky = "E")

inc_less = OptionMenu(tabitem, va3, *yn)
inc_less.grid(row = 3, column = 1, sticky = "E")

z_ops = OptionMenu(tabmove, va4, *z_opsl)
z_ops.grid(row = 4, column = 1, sticky = "E")

itier = OptionMenu(tabitem, va5, *tiers)
itier.grid(row = 5, column = 1, sticky = "E")

atier = OptionMenu(tabab, va7, *tiers2)
atier.grid(row = 10, column = 1, sticky = "E")

speci = OptionMenu(tabitem, va6, *yn)
speci.grid(row = 6, column = 1, sticky = "E")

setier = OptionMenu(tabpoke, va9, *smotiers)
setier.grid(row = 13, column = 1, sticky = "E")

Label(tabpoke, text = "and").grid(row = 13, column = 2, sticky = "W")

upd = OptionMenu(tabpoke, va10, *smoup)
upd.grid(row = 13, column = 3)

radop = ["All Pokemon", "One Pokemon"] #Another list for dropdown menu

# Sets default value for it
rado = StringVar()
rado.set("One Pokemon")
# Makes the dropdown menu
whichy = OptionMenu(tabmove, rado, *radop)
whichy.grid(row = 7, column = 4, sticky = "E")

# Creates places for you to force items, and tells you not to type in he wrong box
e1 = Entry(tabmove, width = 30)
e1.insert(END, 'Any Invalid move will count as No')
e1.grid(row = 7, column = 1, sticky = "E")
e12.insert(0.0, "Don't type in this box")
e44.insert(0.0, "Don't type in this box")

# Makes a box for typing levels into, and sets the default value to 1
etwo = Entry(tabo, width = 15)
etwo.insert(END, 1)
etwo.grid(row = 12, column = 1, sticky = "E")

# Creates label saying that it is picking a level between the 2 values given
Label(tabo, text = "to").grid(row = 12, column = 2, sticky = "W")

# Makes a box for typing levels into, and sets the default value to 100
ethree = Entry(tabo, width = 15)
ethree.insert(END, 100)
ethree.grid(row = 12, column = 3, sticky = "E")



radab = ["All Pokemon", "One Pokemon"] #Another list for dropdown menu
# Sets default value for it
radab = StringVar()
radab.set("One Pokemon")
# Makes the dropdown menu
whichy2 = OptionMenu(tabab, radab, *radop)
whichy2.grid(row = 8, column = 4, sticky = "E")

# Creates places for you to force an ability, and tells you not to type in he wrong box
e11 = Entry(tabab, width = 30)
e11.insert(END, 'Any Invalid ability will count as No')
e11.grid(row = 8, column = 1, sticky = "E")
e121.insert(0.0, "Don't type in this box")
e55.insert(0.0, "Don't type in this box")


radit = ["All Pokemon", "One Pokemon"] #Another list for dropdown menu
# Sets default value for it
radit = StringVar()
radit.set("One Pokemon")
# Makes the dropdown menu
whichy3 = OptionMenu(tabitem, radit, *radop)
whichy3.grid(row = 9, column = 4, sticky = "E")

# Creates places for you to force an ability, and tells you not to type in he wrong box
e3 = Entry(tabitem, width = 30)
e3.insert(END, 'Any Invalid item will count as No')
e3.grid(row = 9, column = 1, sticky = "E")
e33.insert(0.0, "Don't type in this box")
e44.insert(0.0, "Don't type in this box")


from tkinter import * #Import tkinter again in a format where I don't have to type "tkinter." before everything

def save(): #Creates a function for saving your options

    # Gets file location for saving file, first asking for .txt files in the documents file
    filename =  filedialog.asksaveasfilename(initialdir = "Documents",title = "Select Saving File", filetypes = (("Text files (.txt)","*.txt"),("All files","*.*")))
    the_file = filename
    temp = list(the_file) #Turns the filename you asks for into a list, snd if it does not have a "." in it then it adds ".txt" to the filename
    if "." not in temp:
        the_file += ".txt"
    


    try: #Tries to sent the data from all the options into the given file
        t = open(the_file, "w")
        t.write(va1.get() + "\n")
        t.write(va2.get() + "\n")
        t.write(va3.get() + "\n")
        t.write(va4.get() + "\n")
        t.write(va5.get() + "\n")
        t.write(va6.get() + "\n")
        t.write(va7.get() + "\n")
        t.write(va8.get() + "\n")
        t.write(va9.get() + "\n")
        t.write(va10.get() + "\n")
        t.write(va11.get() + "\n")
        t.write(va12.get() + "\n")
        t.write(va13.get() + "\n")
        t.write(e1.get() + "\n")
        t.write(e11.get() + "\n")
        t.write(e3.get() + "\n")
        t.write(etwo.get() + "\n")
        t.write(ethree.get() + "\n")
        t.write(radit.get() + "\n")
        t.write(radab.get() + "\n")
        t.write(rado.get() + "\n")
        t.close()

    except: #If it fails then it says on the shell
        print("File not found")

def opening(): #Creates a function for loading your options

    # Gets file location for opening file, first asking for .txt files in the documents file
    filename = filedialog.askopenfilename(initialdir = "Documents",title = "Select Saving File", filetypes = (("Text files (.txt)","*.txt"),("All files","*.*")))
    the_file = filename
    try: #Tries to get the data for all the options into the given file
        t = open(the_file, "r")
        t = t.read() #Reads the file
        t = t.splitlines() #Turns the file into a list, then sets each variable into the relevant value in the list
        va1.set(t[0])
        va2.set(t[1])
        va3.set(t[2])
        va4.set(t[3])
        va5.set(t[4])
        va6.set(t[5])
        va7.set(t[6])
        va8.set(t[7])
        va9.set(t[8])
        va10.set(t[9])
        va11.set(t[10])
        va12.set(t[11])
        va13.set(t[12])
        e1.delete(0, END)
        e1.insert(END, t[13])
        e11.delete(0, END)
        e11.insert(END, t[14])
        e3.delete(0, END)
        e3.insert(END, t[15])
        etwo.delete(0, END)
        etwo.insert(END, t[16])
        ethree.delete(0, END)
        ethree.insert(END, t[17])
        radit.set(t[18])
        radab.set(t[19])
        rado.set(t[20])
    except: #If something goes wrong it shows an error message in the shell window
        print("File not found / Something went wrong")

def auto_load(): #Function for changing default values for dropdown menus
    t = open("Auto_Load.txt", "w") #opens a file called "Auto_Load.txt", and gives it the values from the dropdown menu and text boxes
    t.write(va1.get() + "\n")
    t.write(va2.get() + "\n")
    t.write(va3.get() + "\n")
    t.write(va4.get() + "\n")
    t.write(va5.get() + "\n")
    t.write(va6.get() + "\n")
    t.write(va7.get() + "\n")
    t.write(va8.get() + "\n")
    t.write(va9.get() + "\n")
    t.write(va10.get() + "\n")
    t.write(va11.get() + "\n")
    t.write(va12.get() + "\n")
    t.write(va13.get() + "\n")
    t.write(e1.get() + "\n")
    t.write(e11.get() + "\n")
    t.write(e3.get() + "\n")
    t.write(etwo.get() + "\n")
    t.write(ethree.get() + "\n")
    t.write(radit.get() + "\n")
    t.write(radab.get() + "\n")
    t.write(rado.get() + "\n")
    t.close()

def get_auto_load(): #Function for automatically getting the changed default values 
    try:
        t = open("Auto_Load.txt", "r") #Opens the file
        t = t.read() #Reads the file
        t = t.splitlines() #Turns the file into a list, then sets each variable into the relevant value in the list
        va1.set(t[0])
        va2.set(t[1])
        va3.set(t[2])
        va4.set(t[3])
        va5.set(t[4])
        va6.set(t[5])
        va7.set(t[6])
        va8.set(t[7])
        va9.set(t[8])
        va10.set(t[9])
        va11.set(t[10])
        va12.set(t[11])
        va13.set(t[12])
        e1.delete(0, END)
        e1.insert(END, t[13])
        e11.delete(0, END)
        e11.insert(END, t[14])
        e3.delete(0, END)
        e3.insert(END, t[15])
        etwo.delete(0, END)
        etwo.insert(END, t[16])
        ethree.delete(0, END)
        ethree.insert(END, t[17])
        radit.set(t[18])
        radab.set(t[19])
        rado.set(t[20])
    except: #If there is a error it shows an error in the window shell
        print("Auto Load not found")

def help_doc(): #Function for opening the help file
    try:
        import webbrowser #Imports a program that lets this program open files
        # It sounds like it will always open web pages, but it can open ".html" files in your folder, but you can trick it into opening any type of file in the default program
        webbrowser.open("Help_for_program.txt") #Opens the help file
    except: #If there is an error it shows an error message
        print("There was an error, You may not have installed \"Help_for_program.txt\" in the same folder as the program.")

menubar = Menu(master) #Creates a menu bar for above functions

# Creates a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff = 0) #Creates the menu
filemenu.add_command(label="Open Options", command = opening) #Creates an option to open an options file, in the dropdown menu
filemenu.add_separator() #Adds a nice looking seperator between each option
filemenu.add_command(label="Save Options", command = save) #Creates an option to save an options file, in the dropdown menu
filemenu.add_separator() #Adds a nice looking seperator between each option
filemenu.add_command(label="Change Default Options to Current Options", command = auto_load) #Creates an option to change the default options by making a text file, in the dropdown menu
filemenu.add_separator() #Adds a nice looking seperator between each option
filemenu.add_command(label = "Open help file in defualt text editor", command = help_doc) #Creates an option to open the help file, if it can be found
menubar.add_cascade(label="File", menu = filemenu) # Adds all these options to the menu under the name "File"

# displays the menu
master.config(menu = menubar)

get_auto_load() #Automatically loads the changed defualt option file, by running an above function

mainloop() #Creates the windows and runs the program








