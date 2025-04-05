#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

la_liste = ["Python",
    "Data Science",
    "veille technologique",
    "javascript veille technologique",
    "python web Scraping",
    "Machine Learning",
    "Introduction to AI",
    "Neural Networks",
    "Deep Learning Algorithms",
    "Programmation",
    "Langages de programmation",
    "Introduction à la programmation",
    "Algorithmes et structures de données",
    "Programmation orientée objet",
    "Programmation fonctionnelle",
    "Développement web",
    "Développement mobile",
    "Développement de jeux",
    "Bases de données",
    "Frameworks de développement",
    "Meilleures pratiques en programmation",
    "Débogage et tests",
    "Contrôle de version avec Git",
    "Programmation concurrente",
    "Performance et optimisation du code",
    "Sécurité du code",
    "Carrière en programmation",
    "Compétences en programmation avancées",
    "Thème Python",
    "Introduction à Python",
    "Programmation avancée en Python",
    "Bibliothèques Python populaires",
    "Projets Python pour débutants",
    "Python pour la science des données",
    "Automatisation avec Python",
    "Développement web avec Django/Flask",
    "Thème JavaScript",
    "Introduction à JavaScript",
    "Programmation avancée en JavaScript",
    "Frameworks JavaScript populaires",
    "Projets JavaScript pour débutants",
    "JavaScript côté serveur avec Node.js",
    "Applications web interactives avec JavaScript",
    "Thème PHP",
    "Introduction à PHP",
    "Programmation avancée en PHP",
    "Frameworks PHP populaires",
    "Projets PHP pour débutants",
    "Développement web avec PHP",
    "Sécurité en PHP",
    "Thème HTML",
    "Introduction à HTML",
    "Structuration des pages web avec HTML",
    "Balises HTML avancées",
    "Accessibilité et HTML",
    "HTML5 et ses nouveautés",
    "Thème CSS",
    "Introduction à CSS",
    "Mise en page avec CSS",
    "Animations et transitions en CSS",
    "Préprocesseurs CSS (Sass, LESS)",
    "Responsive design avec CSS",
    "les projets pour devenir développeur",
    "comment se former à la cybersécurité",
    "Introduction à la cybersécurité",
    "Types de menaces informatiques",
    "Sécurité des réseaux",
    "Protection des données",
    "Cryptographie",
    "Sécurité des applications web",
    "Sécurité mobile",
    "Prévention des cyberattaques",
    "Analyse des risques informatiques",
    "Sécurité dans le cloud",
    "Gestion des incidents de sécurité informatique",
    "Normes et réglementations en cybersécurité",
    "Meilleures pratiques en cybersécurité",
    "Formation en cybersécurité",
    "Carrière en cybersécurité",
    "Recettes cuisine facile",
    "Cuisine italienne",
    "Techniques de cuisson",
    "Recettes de desserts",
    "Cuisine asiatique",
    "Meilleures recettes de pâtes",
    "Comment faire du pain maison",
    "Recettes saines et faciles",
    "les lieux incontournables pour visiter paris",
    "les meilleurs restos à paris",
    "Destinations",
    "Voyage en Europe",
    "Meilleures plages",
    "Conseils de voyage",
    "Itinéraires de voyage",
    "Destinations de vacances d'été",
    "Comment planifier un road trip",
    "meilleurs destinations pour aller au japon",
    "lieux incontournables pour visiter le japon",
    "Santé et Bien-être",
    "Yoga",
    "Nutrition",
    "Méditation",
    "Exercices physiques",
    "Alimentation équilibrée",
    "Techniques de relaxation",
    "Comment améliorer sa santé mentale",
    "Guide complet sur la gestion du stress",
    "Culture et Arts",
    "Peinture",
    "Art moderne",
    "Histoire de l'art",
    "Expositions d'art",
    "Musées célèbres",
    "Techniques de peinture à l'huile",
    "Comment comprendre l'art abstrait",
    "Guide des plus grands artistes du 20ème siècle",
    "Sport",
    "Football",
    "Basketball",
    "Tennis",
    "Entraînement sportif",
    "Compétitions sportives",
    "Meilleurs exercices pour la musculation",
    "Conseils pour améliorer son endurance",
    "Comment débuter en course à pied",
    "Musique",
    "Jazz",
    "Rock",
    "musique metale",
    "Musique classique",
    "Instruments de musique",
    "Histoire de la musique",
    "Comment apprendre la guitare",
    "Compositeurs célèbres de musique classique",
    "Guide pour créer une playlist parfaite",
    "Technologie",
    "Smartphones",
    "Gadgets",
    "Réalité virtuelle",
    "Innovation technologique",
    "Meilleurs logiciels de 2024",
    "Tendances technologiques",
    "Comment choisir un ordinateur portable",
    "Guide des meilleures applications mobiles",
    "Photographie",
    "Comment prendre de belles photos",
    "Techniques de photographie",
    "Édition de photos",
    "Meilleurs appareils photo de 2024",
    "Voyage photographique",
    "Photographie de nature",
    "Photographie urbaine",
    "Cinéma",
    "Films classiques",
    "Nouveautés cinématographiques",
    "Réalisateurs célèbres",
    "Critiques de films",
    "Genres cinématographiques",
    "Comment réaliser un court-métrage",
    "Histoire du cinéma",
    "Acteurs et actrices célèbres",
    "Culture japonaise",
    "Mangas",
    "Anime",
    "Histoire du manga",
    "Meilleurs mangas de tous les temps",
    "Genres de manga",
    "Mangakas célèbres",
    "Comment dessiner des mangas",
    "Meilleurs anime de 2023",
    "meilleur anime de 2024",
    "Jeux vidéo",
    "Histoire des jeux vidéo",
    "Genres de jeux vidéo",
    "Consoles de jeux",
    "meilleurs rpg 2023",
    "meilleurs rpg 2024",
    "Jeux vidéo classiques",
    "Développement de jeux vidéo",
    "nintendo actu",
    "Meilleurs jeux vidéo de 2024",
    "Personnages célèbres de jeux vidéo",
    "Culture otaku"]

# Sélectionner cinq éléments aléatoires de la liste
elements_aleatoires = random.sample(la_liste, 15)

print (len(la_liste))
# Imprimer les éléments sélectionnés
print(elements_aleatoires)


# In[12]:


import random

la_liste = [
    "Python",
    "Data Science",
    "veille technologique",
    "javascript veille technologique",
    "python web Scraping",
    "Machine Learning",
    "Introduction to AI",
    "Neural Networks",
    "Deep Learning Algorithms",
    "Programmation",
    "Langages de programmation",
    "Introduction à la programmation",
    "Algorithmes et structures de données",
    "Programmation orientée objet",
    "Programmation fonctionnelle",
    "Développement web",
    "Développement mobile",
    "Développement de jeux",
    "Bases de données",
    "Frameworks de développement",
    "Meilleures pratiques en programmation",
    "Débogage et tests",
    "Contrôle de version avec Git",
    "Programmation concurrente",
    "Performance et optimisation du code",
    "Sécurité du code",
    "Carrière en programmation",
    "Compétences en programmation avancées",
    "Thème Python",
    "Introduction à Python",
    "Programmation avancée en Python",
    "Bibliothèques Python populaires",
    "Projets Python pour débutants",
    "Python pour la science des données",
    "Automatisation avec Python",
    "Développement web avec Django/Flask",
    "Thème JavaScript",
    "Introduction à JavaScript",
    "Programmation avancée en JavaScript",
    "Frameworks JavaScript populaires",
    "Projets JavaScript pour débutants",
    "JavaScript côté serveur avec Node.js",
    "Applications web interactives avec JavaScript",
    "Thème PHP",
    "Introduction à PHP",
    "Programmation avancée en PHP",
    "Frameworks PHP populaires",
    "Projets PHP pour débutants",
    "Développement web avec PHP",
    "Sécurité en PHP",
    "Thème HTML",
    "Introduction à HTML",
    "Structuration des pages web avec HTML",
    "Balises HTML avancées",
    "Accessibilité et HTML",
    "HTML5 et ses nouveautés",
    "Thème CSS",
    "Introduction à CSS",
    "Mise en page avec CSS",
    "Animations et transitions en CSS",
    "Préprocesseurs CSS (Sass, LESS)",
    "Responsive design avec CSS",
    "les projets pour devenir développeur",
    "comment se former à la cybersécurité",
    "Introduction à la cybersécurité",
    "Types de menaces informatiques",
    "Sécurité des réseaux",
    "Protection des données",
    "Cryptographie",
    "Sécurité des applications web",
    "Sécurité mobile",
    "Prévention des cyberattaques",
    "Analyse des risques informatiques",
    "Sécurité dans le cloud",
    "Gestion des incidents de sécurité informatique",
    "Normes et réglementations en cybersécurité",
    "Meilleures pratiques en cybersécurité",
    "Formation en cybersécurité",
    "Carrière en cybersécurité",
    "Recettes cuisine facile : Idées simples et rapides pour préparer des repas savoureux à la maison.",
    "Cuisine italienne : Exploration des plats emblématiques de l'Italie, y compris les pâtes, les pizzas et les desserts italiens.",
    "Techniques de cuisson : Apprendre les bases des différentes techniques de cuisson, comme la cuisson à la vapeur, la friture, la grillade, etc.",
    "Recettes de desserts : Recettes pour réaliser des desserts délicieux, allant des gâteaux aux pâtisseries fines.",
    "Cuisine asiatique : Découverte des saveurs et des techniques de la cuisine asiatique, incluant les cuisines japonaise, chinoise, thaïlandaise, etc.",
    "Meilleures recettes de pâtes : Variété de recettes de pâtes pour tous les goûts, des classiques aux créations innovantes.",
    "Comment faire du pain maison : Guide pour préparer différents types de pain maison, y compris le pain au levain et les baguettes.",
    "Recettes saines et faciles : Recettes équilibrées et nutritives pour un mode de vie sain.",
    "les lieux incontournables pour visiter paris : Les attractions touristiques majeures à Paris, telles que la Tour Eiffel, le Louvre, et Montmartre.",
    "les meilleurs restos à paris : Sélection des meilleurs restaurants parisiens pour tous les budgets.",
    "Destinations : Listes des destinations populaires à travers le monde.",
    "Voyage en Europe : Guides de voyage pour découvrir les pays européens.",
    "Meilleures plages : Classement des plus belles plages du monde.",
    "Conseils de voyage : Astuces et recommandations pour un voyage sans soucis.",
    "Itinéraires de voyage : Propositions d'itinéraires pour des voyages courts ou longs.",
    "Destinations de vacances d'été : Suggestions pour des vacances estivales inoubliables.",
    "Comment planifier un road trip : Conseils pour organiser un road trip, de l'itinéraire aux préparatifs.",
    "meilleurs destinations pour aller au japon : Les meilleures villes et sites à visiter au Japon.",
    "lieux incontournables pour visiter le japon : Les sites historiques, naturels et culturels à ne pas manquer au Japon.",
    "Santé et Bien-être",
    "Yoga : Différents styles de yoga et leurs bienfaits.",
    "Nutrition : Conseils pour une alimentation équilibrée et saine.",
    "Méditation : Techniques de méditation pour améliorer le bien-être mental.",
    "Exercices physiques : Programmes d'exercice pour différents niveaux de forme physique.",
    "Alimentation équilibrée : Guide pour une alimentation saine et équilibrée.",
    "Techniques de relaxation : Méthodes pour réduire le stress et favoriser la relaxation.",
    "Comment améliorer sa santé mentale : Stratégies et conseils pour maintenir une bonne santé mentale.",
    "Guide complet sur la gestion du stress : Techniques et astuces pour gérer et réduire le stress.",
    "Culture et Arts",
    "Peinture : Techniques et styles de peinture.",
    "Art moderne : Exploration de l'art moderne et contemporain.",
    "Histoire de l'art : Voyage à travers les différentes périodes de l'histoire de l'art.",
    "Expositions d'art : Les meilleures expositions à voir.",
    "Musées célèbres : Les musées les plus réputés dans le monde.",
    "Techniques de peinture à l'huile : Apprentissage des bases et des techniques avancées de la peinture à l'huile.",
    "Comment comprendre l'art abstrait : Guide pour appréhender et apprécier l'art abstrait.",
    "Guide des plus grands artistes du 20ème siècle : Découverte des artistes influents du 20ème siècle et de leurs œuvres.",
    "Sport",
    "Football : Actualités, règles et techniques du football.",
    "Basketball : Informations sur les ligues, les équipes et les joueurs de basketball.",
    "Tennis : Suivi des tournois et conseils pour améliorer son jeu.",
    "Entraînement sportif : Programmes d'entraînement pour améliorer la performance sportive.",
    "Compétitions sportives : Calendrier des grandes compétitions sportives.",
    "Meilleurs exercices pour la musculation : Exercices efficaces pour développer les muscles.",
    "Conseils pour améliorer son endurance : Techniques pour augmenter l'endurance physique.",
    "Comment débuter en course à pied : Guide pour les débutants en course à pied.",
    "Musique",
    "Jazz : Histoire du jazz et ses artistes emblématiques.",
    "Rock : Exploration des genres et des groupes de rock.",
    "musique métal : Détails sur les sous-genres et les groupes de métal.",
    "Musique classique : Compositeurs célèbres et œuvres incontournables de la musique classique.",
    "Instruments de musique : Présentation des différents instruments et comment les apprendre.",
    "Histoire de la musique : Évolution de la musique à travers les âges.",
    "Comment apprendre la guitare : Guide pour débuter et progresser en guitare.",
    "Compositeurs célèbres de musique classique : Biographies et œuvres des grands compositeurs classiques.",
    "Guide pour créer une playlist parfaite : Conseils pour composer une playlist adaptée à toutes les occasions.",
    "Technologie",
    "Smartphones",
    "Gadgets",
    "Réalité virtuelle",
    "Innovation technologique",
    "Meilleurs logiciels de 2024",
    "Tendances technologiques",
    "Comment choisir un ordinateur portable",
    "Guide des meilleures applications mobiles",
    "Photographie",
    "Comment prendre de belles photos : Techniques de base pour améliorer ses photos.",
    "Techniques de photographie : Astuces avancées pour maîtriser l'art de la photographie.",
    "Édition de photos : Guide pour éditer et retoucher ses photos.",
    "Meilleurs appareils photo de 2024 : Sélection des meilleurs appareils photo disponibles en 2024.",
    "Voyage photographique : Conseils pour combiner voyage et photographie.",
    "Photographie de nature : Techniques pour capturer la beauté de la nature.",
    "Photographie urbaine : Astuces pour prendre des photos captivantes en milieu urbain.",
    "Cinéma",
    "Films classiques : Les films qui ont marqué l'histoire du cinéma.",
    "Nouveautés cinématographiques : Les dernières sorties au cinéma.",
    "Réalisateurs célèbres : Portraits des réalisateurs les plus influents.",
    "Critiques de films : Analyses et critiques des films récents.",
    "Genres cinématographiques : Exploration des différents genres de films.",
    "Comment réaliser un court-métrage : Guide pour écrire, tourner et monter un court-métrage.",
    "Histoire du cinéma : Évolution du cinéma à travers les décennies.",
    "Acteurs et actrices célèbres : Biographies des stars du cinéma.",
    "Culture japonaise",
    "Mangas : Histoire et évolution du manga.",
    "Anime : Les séries et films d'animation japonais.",
    "Histoire du manga : Origines et développement du manga au Japon.",
    "Meilleurs mangas de tous les temps : Les mangas les plus populaires et influents.",
    "Genres de manga : Différents genres de manga et leurs caractéristiques.",
    "Mangakas célèbres : Les auteurs de mangas les plus renommés.",
    "Comment dessiner des mangas : Techniques de base pour dessiner des mangas.",
    "Meilleurs anime de 2023 : Les anime les plus appréciés de 2023.",
    "meilleur anime de 2024 : Les anime les plus attendus de 2024.",
    "Jeux vidéo",
    "Histoire des jeux vidéo : De la naissance des premiers jeux à l'industrie actuelle.",
    "Genres de jeux vidéo : Exploration des différents genres de jeux.",
    "Consoles de jeux : Comparatif des différentes consoles de jeux vidéo.",
    "meilleurs rpg 2023 : Sélection des meilleurs jeux de rôle sortis en 2023.",
    "meilleurs rpg 2024 : Les RPG les plus attendus de 2024.",
    "Jeux vidéo classiques : Les jeux vidéo qui ont marqué l'histoire.",
    "Développement de jeux vidéo : Processus de création et de développement des jeux vidéo.",
    "nintendo actu : Actualités et nouveautés concernant Nintendo.",
    "Meilleurs jeux vidéo de 2024 : Les jeux vidéo les plus populaires de 2024.",
    "Personnages célèbres de jeux vidéo : Les personnages emblématiques des jeux vidéo.",
    "Culture otaku : Exploration de la culture otaku, ses origines et ses influences."
]

print(len(la_liste))

# Sélectionner quinze éléments aléatoires de la liste
elements_aleatoires = random.sample(la_liste, 15)

# Imprimer les éléments sélectionnés
print(elements_aleatoires)


# In[ ]:




