import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

teams = np.array([
"Belgium",
"Italy",
"Russia",
"Poland",
"Ukraine",
"Spain",
"France",
"Turkey",
"England",
"Czech Republic",
"Finland",
"Sweden",
"Croatia",
"Austria",
"Netherlands",
"Germany",
"Portugal",
"Switzerland",
"Denmark",
"Wales",
"North",
"Hungary",
"Slovakia",
"Scotland"])

participants = np.array([
"Mindy Beaudoin",
"Rida Hollin",
"Nakisha Bahena",
"Lera Mcnealy",
"Iesha Sorber",
"Molly Nesmith",
"Rico Blackburn",
"Lorenzo Skiles",
"Yvone Musser",
"Tatyana Vaillancourt",
"Ludie Hotz",
"Enniffer Mcginn",
"Lasonya Emmert",
"Nickole Egner",
"Charisse Schwenk",
"Joycelyn Lingo",
"Victorina Knotts",
"Casey Heatwole",
"Willia Cantu",
"Priscilla Benbow",
"Jack Hewson",
"Jonathon Gloveman",
"Pete Peterson",
"The Sidekick"])

shuffler = np.random.permutation(len(teams))
teams_shuffled = teams[shuffler]
sweepstake = np.stack((participants,teams_shuffled),axis=1)

print(sweepstake)

np.savetxt(dir_path + "\sweepstake.csv", sweepstake, fmt='%s', delimiter = ',')