# dbt-snowflake

L'objectif du projet est de tester DBT avec Snowflake afin de parfaire des transformations
Ce MVP permettra de démontrer aux parties tenantes la pertinence de DBT dans l'élaboration d'une Data Platform

Materiel necessaire : 
- Des fakes données représentants les données SAP et CICS de Roquette -> ok
- La creation d'un compte sur Snowflake -> ok
- L'installation de DBT et la configuration -> ok
- Un schéma expliquant les transformations souhaitées

Tâches necessaires pour la démonstration : 
- Creer une fonction permettant de générer les fakes data simulant BW -> ok
- Utiliser DBT pour faire ces transformation jusqu'au layer Datawarehouse
- Mettre une logique de tests sur les données (notamment le rejet dans une table de stagging)
- Tester avec un snowflake sur un datalake azure

![Screenshot](img\archi.png)


Structure des fakes data : 


Tutorial : 
- Installer snowsql pour charger des données dans snowflake
- Installer dbt en local
- Creer un fichier sql dans src -> executer la query dans snowflake pour verifier
- Faire un dbt run -> la view devrait être créée

Steps dbt transform : 
![Screenshot](img\dataflow_raw_to_staging.png)
![Screenshot](img\dataflow_staging_to_corelayer.png)


TIPS : 
- Raw Layer : la data source
- Staging Layer : le 1er layer sert à selectionner les colonnes et d'appliquer un renommage simple