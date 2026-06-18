<div align="center">
<h1>COVID-19 & Bonheur</h1>
<p><em>Analyse de données — Impact du COVID-19 sur le bonheur mondial</em></p>
<a href="#"><img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white&style=flat-square"></a>
<a href="#"><img src="https://img.shields.io/badge/Data-Analysis-orange?style=flat-square"></a>
<a href="#"><img src="https://img.shields.io/badge/COVID--19-World%20Happiness-blueviolet?style=flat-square"></a>
<a href="#"><img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square"></a>
<a href="https://hoangviet1810.github.io/covid/">
  <img src="https://img.shields.io/badge/Demo-Live_Website-red?style=flat-square">
</a>
<a href="#"><img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square"></a>
</div>
<br>

# Projet-Covid-19-Data-Analyst

# Présentation du projet

Dans ce projet, on analyse les données de la COVID-19 concernant le nombre cumulé de cas confirmés par pays. On les combine avec des données sur différents indicateurs de qualité de vie afin d'étudier l'existence d'un lien entre la propagation du virus et le niveau de bonheur des populations.

Pour cela, on utilise l'ensemble de données COVID-19 publié par l'université Johns Hopkins ainsi que l'ensemble de données World Happiness Report 2021. Ces données sont disponibles sur Kaggle aux adresses suivantes :

- <https://www.kaggle.com/datasets/antgoldbloom/covid19-data-from-john-hopkins-university>
- <https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2021>

## 📊 Données utilisées
 
| Source | Description |
|--------|-------------|
| Johns Hopkins University | Données COVID-19 (cas, décès, guérisons) |
| Gallup World Poll / ONU | World Happiness Report |
| Kaggle | Dataset public disponible en ligne |
 
---
 
## 🔍 Indicateurs analysés
 
- **GDP per capita** — Richesse économique par habitant
- **Social support** — Réseau de soutien social perçu
- **Life expectancy** — Espérance de vie en bonne santé
- **Freedom** — Liberté de faire des choix de vie
- **Generosity** — Générosité
- **Corruption perception** — Perception de la corruption


# Organisation des codes

Le projet est divisé en plusieurs parties :

```
├── Part1  — Préparation et nettoyage des données
├── Part2  — Analyse exploratoire (EDA)
├── Part3  — Corrélations et régressions
└── Part4  — Conclusion
```

## Partie 1 : Préparation et nettoyage des données

Cette partie est consacrée à l'importation des jeux de données, au traitement des valeurs manquantes, à l'agrégation des données par pays ainsi qu'à la fusion des différentes sources de données.

## Partie 2 : Analyse exploratoire des données (EDA)

Cette étape vise à explorer les caractéristiques principales des données à l'aide de statistiques descriptives et de visualisations afin de mieux comprendre l'évolution de la pandémie dans différents pays.

## Partie 3 : Analyse de la relation COVID-19 – Bonheur

Dans cette partie, on étudie les corrélations entre le taux maximal d'infection et plusieurs indicateurs issus du World Happiness Report, tels que :

- le PIB par habitant ;
- le soutien social ;
- l'espérance de vie en bonne santé ;
- la liberté de faire des choix de vie.

## Partie 4 : Conclusion

On résume les principaux résultats obtenus, discute de leurs limites et propose des pistes d'amélioration pour des analyses futures.

## 🚀 Démo
 
👉 [Voir le site en ligne](https://hoangviet1810.github.io/covid/)
 
---

**Consulter le dashboard**

[![Dashboard du projet](images/dashboard_covid.png)](https://hoangviet1810.github.io/Projet-Covid-19-Data-Analyst/images/dashboard_covid_happiness.html)

➡️ Cliquez sur l'image pour ouvrir le dashboard interactif.

