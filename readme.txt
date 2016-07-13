Scripts pour automatiser la sauvegarde de dossiers (et de leur contenu) sur un support externe.

Avant de commencer: ces scripts sont sensibles à la casse, c'est-à-dire que les noms "Adrien" et "adrien" sont différents! De plus, les noms de fichiers contenant des caractères spéciaux peuvent poser problème.

Localisez chaque dossier à sauvegarder de votre ordinateur.
Trouvez dans l'arborescence de vos fichiers, un dossier qui contient tout ce que vous voulez sauvegarder.
Notez le chemin complet dans "srcdir.txt" (exemple: "C:/Users/Adrien").
Indiquez dans le fichier "dstdir.txt" l'emplacement où la sauvegarde doit être créée (exemple: "G:/save"). Choisissez bien votre destination, elle sera souvent utilisée.
Dans le fichier "list.txt", notez chaque dossier à sauvegarder, en chemin relatif à celui dans "srcdir.txt" (exemple: pour sauvegarder "C:/Users/Adrien/Documents", notez "Documents"). Il doit y avoir une ligne par dossier.
Si vous voulez exclure certains fichiers ou dossiers de la sauvegarde, indiquez-les de la même façon que ceux à sauvegarder, mais dans le fichier "ignore.txt" (exemple: pour ignorer "C:/Users/Adrien/Documents/Confidentiel", notez "Documents/Confidentiel").

Si toutes les opérations citées sont effectuées, ouvrez un terminal dans le dossier du script.
Lancez le script "searchdiffs.py". Cela peut prendre quelques minutes.
Normalement, vous devriez avoir une sortie semblable à la suivante, comprise entre les deux lignes de tirets (basée sur les exemples ci-dessus):
--------------------------------------------------
   --- C:/Users/Adrien
   --- G:/save
   --- ['Documents']
   --- ['Documents/Confidentiel']

  Fichiers modifies:
    
  Fichiers crees:
    Documents
  
  Fichiers supprimes:
  
  Fichiers erreur:
  
--------------------------------------------------
Quatre fichiers sont générés, reprenant les informations données par le premier script. Ces fichiers indiquent au prochain script ce qu'il faut sauvegarder.
- "out_new.txt": les fichiers ou dossiers qui ont été créés depuis la dernière sauvegarde. Ils seront copié, et le contenu de chaque dossier sera copié également (sauf ceux indiqués dans "ignore.txt")
- "out_modified.txt": les fichiers qui ont été modifiés depuis la dernière sauvegarde (basé sur la date de modification)
- "out_delete.txt": les fichiers ou dossiers qui ont été supprimés depuis la dernière sauvegarde. Il seront supprimés du support externe
- "out_err.txt": les fichiers ou dossiers qui ne peuvent pas être copié. Typiquement, cela arrive quand un nom indiqué dans "list.txt" désigne un fichier au lieu d'un dossier, ou quand un dossier (rest. fichier) à copier porterait le nom d'un fichier (resp. dossier) du support externe s'il était copié.
Lancez le script "update.txt". Cela peut prendre plusieurs heures, selon la quantité à transférer. Tout problème rencontré lors de la copie sera reporté sur la console, ainsi que dans le fichier "update_err.txt".
Si "update.txt" est interrompu avant la fin, exécutez "searchdiffs.txt" afin de réinitialiser les quatre fichiers dont "update.txt" a besoin, afin de continuer là où il a été interrompu. Sinon, il va tout recommencer depuis le début, même pour un fichier!

Remarque: vous pouvez tester ces scripts sur des données dédiées à cet effet, en exécutant "recreatetestenv.py", "searchdiffs.txt usetest" et "update.py usetest". Ceci peut aussi servir d'exemple en vue d'une utilisation sur vos données personnelles.


