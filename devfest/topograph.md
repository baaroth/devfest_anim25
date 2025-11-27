ça fonctionne, mais ça manque de généricité, même après lui avoir demandé explicitement
genre il y a deux fois la même structure de code, une pour chaque partie
(il gère les deux parties du 2024 J10)

ligne.73 : il fait un call à `strip()` pour faire un test dessus, sans enregistrer le résultat
et la réinvoquer dans `parse_grid` (ligne.5)  plutôt que simplement lui passer le résultat
