# dbt-snowflake

L'objectif du projet est de tester DBT avec Snowflake afin de parfaire des transformations
Ce MVP permettra de démontrer aux parties tenantes la pertinence de DBT dans l'élaboration d'une Data Platform

Materiel necessaire : 
- Des fakes données représentants les données SAP et CICS de Roquette
- La creation d'un compte sur Snowflake
- L'installation de DBT et la configuration
- Un schéma expliquant les transformations souhaitées

Tâches necessaires pour la démonstration : 
- Creer une fonction permettant de générer les fakes data simulant BW
- Utiliser DBT pour faire ces transformation jusqu'au layer Datawarehouse
- Mettre une logique de tests sur les données (notamment le rejet dans une table de stagging)
- Tester avec un snowflake sur un datalake azure

image.png
