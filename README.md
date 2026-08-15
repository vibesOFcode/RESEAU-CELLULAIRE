# API CELLULAIRE

## Description

Cette API de réseau cellulaire a été conçue pour modéliser et visualiser un cluster hexagonal, couramment utilisé dans les réseaux cellulaires tels que ceux des télécommunications.

La logique principale repose sur plusieurs concepts clés :

- Structure hexagonale :
  Chaque cellule est représentée par un hexagone, ce qui correspond à une approximation réaliste des zones de couverture des antennes dans un réseau cellulaire.
  Les coordonnées des hexagones sont calculées à l’aide d’un système de coordonnées axiales $(x, y, z)$ adapté aux grilles hexagonales.

- Calcul du nombre de cellules :
  Le nombre total de cellules dans un cluster hexagonal est calculé à partir de la formule :
  $N = i^2 + i \times j + j^2$
  où $i$ et $j$ représentent les dimensions du cluster.

- Représentation graphique :
  La bibliothèque `matplotlib` est utilisée pour tracer les hexagones.
  Les cellules sont dessinées avec des couleurs aléatoires afin de simuler une vue réaliste et visuellement attractive du cluster.

- Architecture de l’API :
  L’API est implémentée avec le framework `FastAPI` afin de permettre une interaction simple et rapide.
  Elle expose deux endpoints principaux :
  - `/calculate` : pour calculer le nombre total de cellules dans le cluster.
  - `/draw` : pour générer une représentation visuelle du cluster sous forme d’image.

En combinant des principes mathématiques, une logique de programmation structurée et des outils modernes, cette API offre une solution simple mais efficace pour modéliser les réseaux cellulaires hexagonaux.

---

## Objectif du projet

Le projet a pour but de :

- calculer le nombre de cellules dans un cluster hexagonal ;
- estimer la distance de réutilisation selon le facteur de réutilisation $N$ ;
- générer une visualisation graphique du cluster pour mieux comprendre son organisation.

---

## Fonctionnalités

- calcul du facteur de réutilisation : $N = i^2 + i \times j + j^2$
- calcul de la distance de réutilisation :
  $D = R \times \sqrt{3N}$
- génération d’une image PNG représentant le cluster hexagonal
- API REST via FastAPI

### Exemple de résultat

Pour un cluster de dimensions $i = 2$ et $j = 1$, la formule donne :

$N = 2^2 + 2 \times 1 + 1^2 = 4 + 2 + 1 = 7$

Ainsi, le nombre total de cellules dans le cluster est :

- Nombre de cellules : 7
- Distance de réutilisation : 4.58

Ce résultat correspond à une configuration typique utilisée pour illustrer le calcul d’un cluster hexagonal dans ce projet.

---

## Prérequis

Avant de lancer le projet, assurez-vous d’avoir installé :

- Python 3.9+
- FastAPI
- Uvicorn
- Matplotlib

---

## Installation

```bash
pip install fastapi uvicorn matplotlib
```

---

## Lancement du serveur

Depuis le dossier du projet :

```bash
python code.py
```

Le serveur sera accessible sur :

```text
http://127.0.0.1:8000
```

---

## Endpoints

### 1. GET /calculate

Calcule le nombre de cellules et la distance de réutilisation pour un cluster donné.

#### Paramètres

- `i` : entier
- `j` : entier

#### Exemple

```bash
http://127.0.0.1:8000/calculate?i=2&j=1
```

#### Réponse exemple

```json
{
  "parametres": {
    "i": 2,
    "j": 1
  },
  "facteur_reutilisation_N": 7,
  "distance_reutilisation_D": 4.58
}
```

### 2. GET /draw

Génère une image du cluster hexagonal.

#### Paramètres

- `i` : entier
- `j` : entier

#### Exemple

```bash
http://127.0.0.1:8000/draw?i=2&j=1
```

La réponse est une image PNG.

---

## Exemple d’utilisation

Voici un exemple simple d’appel dans un navigateur ou via `curl` :

```bash
curl "http://127.0.0.1:8000/calculate?i=3&j=2"
```

---

## Structure du projet

```text
API CELLULAIRE/
├── code.py
├── README.md
└── .dist/
```

---

## Conclusion

Le nom du projet, `API CELLULAIRE`, est parfaitement cohérent avec son objectif : modéliser visuellement un réseau cellulaire hexagonal et calculer ses éléments clés à partir de formules mathématiques. Il est clair, direct et adapté au domaine des télécommunications.

Si vous souhaitez, vous pouvez aussi le renommer en version plus standard :

- `API Cellulaire`
- `api-cellulaire`
- `Cellular Network API`

Selon votre style de projet, le nom `API CELLULAIRE` est entièrement correct et compréhensible.
