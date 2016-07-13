Scripts pour automatiser la sauvegarde de dossiers (et de leur contenu) sur un support externe.

Avant de commencer: ces scripts sont sensibles � la casse, c'est-�-dire que les noms "Adrien" et "adrien" sont diff�rents! De plus, les noms de fichiers contenant des caract�res sp�ciaux peuvent poser probl�me.

Localisez chaque dossier � sauvegarder de votre ordinateur.
Trouvez dans l'arborescence de vos fichiers, un dossier qui contient tout ce que vous voulez sauvegarder.
Notez le chemin complet dans "srcdir.txt" (exemple: "C:/Users/Adrien").
Indiquez dans le fichier "dstdir.txt" l'emplacement o� la sauvegarde doit �tre cr��e (exemple: "G:/save"). Choisissez bien votre destination, elle sera souvent utilis�e.
Dans le fichier "list.txt", notez chaque dossier � sauvegarder, en chemin relatif � celui dans "srcdir.txt" (exemple: pour sauvegarder "C:/Users/Adrien/Documents", notez "Documents"). Il doit y avoir une ligne par dossier.
Si vous voulez exclure certains fichiers ou dossiers de la sauvegarde, indiquez-les de la m�me fa�on que ceux � sauvegarder, mais dans le fichier "ignore.txt" (exemple: pour ignorer "C:/Users/Adrien/Documents/Confidentiel", notez "Documents/Confidentiel").

Si toutes les op�rations cit�es sont effectu�es, ouvrez un terminal dans le dossier du script.
Lancez le script "searchdiffs.py". Cela peut prendre quelques minutes.
Normalement, vous devriez avoir une sortie semblable � la suivante, comprise entre les deux lignes de tirets (bas�e sur les exemples ci-dessus):
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
Quatre fichiers sont g�n�r�s, reprenant les informations donn�es par le premier script. Ces fichiers indiquent au prochain script ce qu'il faut sauvegarder.
- "out_new.txt": les fichiers ou dossiers qui ont �t� cr��s depuis la derni�re sauvegarde. Ils seront copi�, et le contenu de chaque dossier sera copi� �galement (sauf ceux indiqu�s dans "ignore.txt")
- "out_modified.txt": les fichiers qui ont �t� modifi�s depuis la derni�re sauvegarde (bas� sur la date de modification)
- "out_delete.txt": les fichiers ou dossiers qui ont �t� supprim�s depuis la derni�re sauvegarde. Il seront supprim�s du support externe
- "out_err.txt": les fichiers ou dossiers qui ne peuvent pas �tre copi�. Typiquement, cela arrive quand un nom indiqu� dans "list.txt" d�signe un fichier au lieu d'un dossier, ou quand un dossier (rest. fichier) � copier porterait le nom d'un fichier (resp. dossier) du support externe s'il �tait copi�.
Lancez le script "update.txt". Cela peut prendre plusieurs heures, selon la quantit� � transf�rer. Tout probl�me rencontr� lors de la copie sera report� sur la console, ainsi que dans le fichier "update_err.txt".
Si "update.txt" est interrompu avant la fin, ex�cutez "searchdiffs.txt" afin de r�initialiser les quatre fichiers dont "update.txt" a besoin, afin de continuer l� o� il a �t� interrompu. Sinon, il va tout recommencer depuis le d�but, m�me pour un fichier!

Remarque: vous pouvez tester ces scripts sur des donn�es d�di�es � cet effet, en ex�cutant "recreatetestenv.py", "searchdiffs.txt usetest" et "update.py usetest". Ceci peut aussi servir d'exemple en vue d'une utilisation sur vos donn�es personnelles.


