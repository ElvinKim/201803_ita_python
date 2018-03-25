# Problem1-1
print("*")
print("**")
print("***")
print("****")
print("*****")

# Problem1-2
for i in range(5):
    print("*" * (i + 1))

# Problem1-3
for x in range(5):
    for y in range(x + 1):
        print("*", end="")
    print("")

random_num = 20

while True:
    user_number = int(input("number : "))

    if user_number == random_num:
        break

sample_string = """
Best of Greece: Beautiful places and tastiest foods
John Malathronas, CNN • Updated 23rd March 2018
Facebook
Twitter
Email
(CNN) — Many destinations rely on a couple of well-worn beauty spots to carry their images as a vacation hotspot.
When it comes to Greece, those picture-postcard scenes of blue skies, bluer seas and whitewashed villages are everywhere.
The sun-kissed Mediterranean country has enough perfect locations to last anyone a lifetime of vacations. And there's seldom a better time to celebrate them on the week of Greece's national day, March 25.
Here are 36 beautiful -- and delicious -- reasons to travel to Greece:
Naxos Portara
Sun, sea and sand on Naxos Portara.
Sun, sea and sand on Naxos Portara.
Courtesy John Malathronas
The largest island of the Cyclades, Naxos, combines Caribbean-looking sugar-sand beaches for sun-worshippers and a 3,000-foot mountain for hikers.
Portara is the site of the worst of all mythical betrayals. It's there that Theseus dumped Ariadne, daughter of King Minos, despite his promises to marry her and her help in killing the Minotaur.
Not all was lost, however: the god Dionysus fell in love with her and composer Richard Strauss wrote a popular opera about her predicament.
Karpathos
Karpathos has ancient underground chambers and shrines.
Karpathos has ancient underground chambers and shrines.
Kalliopi Mallofti
One of the Aegean's most mysterious of islands, Karpathos is hardly ever mentioned in historical texts, leaving archaeologists struggling to decipher ancient underground chambers and oddly constructed shrines.
Its wild landscapes are only matched by its unique ethnic culture. The village of Olympos (NOT Olympus) is so cut off from the rest of the island that women still wear traditional embroidered dresses even in the beginning of the 21st century.
Ios
Don't miss the Greek island of Ios, known for its iconic windmills.
Don't miss the Greek island of Ios, known for its iconic windmills.
Courtesy Anna Evsyukova
No Greek island encapsulates better the carefree, sun-drenched summer vacation than Ios.
It has some of the finest beaches in the Mediterranean.
Its nightlife is notorious with open-air clubs that start after midnight and continue beyond sunrise.
Finally, its capital, Chora, is a white-washed zigzag of narrow lanes whose iconic windmills are a reminder that, despite the heat and the sun, the island also draws a seasonal summer wind, the meltemi, acting as a natural air conditioner.
Fresh seafood
Seafood in Greece is the best of the best.
Seafood in Greece is the best of the best.
Courtesy John Malathronas
Greeks fuss about freshness like no other people, especially where seafood is concerned.
Many fish tavernas in the smaller islands or coastal villages have their own fishing boats and serve today's catch.
"Frozen" is a dirty word and many a waiter will warn a customer that the calamari or the sea-bream is katepsigmeno, frozen.
Some restaurants will even go to the extent of letting you know where the fish was caught: nearby or in the deeper sea, signifying a longer journey and possible on-boat freezing.
Pidima tis Grias
Andros, is a green, lush island close to Athens the birthplace of 20-odd ship-owning families who have endowed it with museums and art collections; it's still easier to navigate around the island by boat than car even today.
Many of its spectacular beaches feel isolated even in the height of summer like Pidima Tis Grias (The Granny's Jump).
According to legend, an old woman who betrayed the nearby fortified village of Kochylos to Saracen pirates jumped from the cliff full of remorse and was turned into the vertical, isolated rock you can see in the sea.
Sarakiniko
Milos is an volcanic island with natural geothermal heat.
The local taverna on the beach of Paleochori is well-known for its stews that are buried in the sand just before midnight and are ready to eat in the morning after being slow-cooked at a constant heat for eight hours.
The various eruptions have resulted into more than 70 multi-colored beaches although none is more spectacular than the all-white limestone coast of Sarakíniko as shown below.
Related content
Greek islands: How to choose the right one for your holiday
Santorini volcano walk
Santorini features in everyone's bucket list: shaped like a crescent, on the west it faces a submerged crater while on the east side it sports boundless stretches of black sand seen nowhere else in the Aegean.
Hiking on the otherworldly slopes of two still actively volcanic Kammeni ("Burnt") islands inside the crater while facing the main island whose whitewashed houses cap the cliffs like icing sugar is a vacation highlight.
Skopelos
"""
word_dict = {}
for word in sample_string.split():
    print(word)
