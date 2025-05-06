# 📊 Projet d’Investissement Automatisé en Machine Learning

Ce projet a pour objectif de développer un algorithme de **décision d’investissement** automatisée basé sur une combinaison de trois analyses complémentaires : **analyse technique**, **analyse sentimentale sur les réseaux sociaux**, et **analyse sentimentale issue de l’actualité économique**.  
Le tout est développé en **Python**, en s'appuyant sur des bibliothèques spécialisées en finance, traitement du langage naturel (NLP) et machine learning.

---

## 🔍 Objectifs

- Fournir une **note agrégée** de confiance sur une entreprise cotée en bourse.
- Prendre une **décision d’achat ou de vente** à partir de données financières et sentimentales.
- Intégrer plusieurs **sources de données hétérogènes** pour un jugement plus robuste.

---

## 🧠 Structure du projet

Le projet est divisé en **trois modules principaux**, chacun relié à un dataset spécifique :

### 1. `analyse_technique.py`

- Analyse les **cours historiques de l’action**.
- Calcule des **indicateurs techniques** (Moyennes mobiles, RSI, MACD, etc.).
- Fait des **prédictions de prix de clôture**.
- Génère une **note technique** entre **0 et 5**.

### 2. `analyse_reseaux.py`

- Analyse les **sentiments exprimés sur les réseaux sociaux** (X, LinkedIn...).
- Utilise des techniques de **scraping** et de **NLP**.
- Donne une **note sentimentale** en fonction de la tonalité générale des discussions.
- ⚠️ **Problème connu** : Certains sites mettent en place des protections anti-scraping, nécessitant une adaptation (via proxies, API officielles ou IA générative).

### 3. `analyse_actualite.py`

- Analyse les **sentiments dans les articles de presse économique** (Les Echos, Le Monde, etc.).
- Extraction du ton global des titres et contenus via NLP.
- Fournit une **note de confiance média**.
- ⚠️ **Problème connu** : Accès restreint aux contenus, des solutions alternatives sont à l’étude (API, RSS, agrégateurs, scraping contourné).

---

## ✅ Étape suivante

Un quatrième module `decision_investissement.py` combinera les trois notes pour :

- Évaluer le **niveau de confiance global**.
- Déterminer une **action recommandée** : acheter, conserver, ou vendre.

---

## 🔧 Technologies utilisées

- **Langage** : Python 3.10+
- **Librairies principales** : `pandas`, `numpy`, `scikit-learn`, `yfinance`, `BeautifulSoup`, `requests`, `transformers`, `nltk`, etc.
- **Approches ML/NLP** : vectorisation, modèles pré-entraînés, classification de sentiment, régression de prix.

---

## 📌 Remarques

Ce projet est en cours de développement. Certaines fonctionnalités (scraping avancé, API sociales et presse) peuvent nécessiter des contournements techniques ou un passage à des solutions payantes / semi-automatisées.

---

## 📫 Contact

Pour toute question ou suggestion :  
**Robin Levasseur** – codev
**Albane Oury**- codev
📧 *albane.oury@gmail.com*