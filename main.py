#### Imports et définition des variables globales
"""
Ce module permet de lire un fichier CSV contenant des listes d'entiers, 
de traiter ces listes et d'afficher des informations utiles telles que :
- le premier et le dernier élément d'une liste,
- les valeurs minimales, maximales et la somme des éléments,
- ainsi que l'affichage de toutes les lignes du fichier.

Les données sont lues à partir du fichier spécifié par la constante FILENAME.
"""

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        for line in f:
            l.append([int(x) for x in line.strip().split(';')])
    return l


def get_list_k(data, k):
    """Retourne la k-ième ligne de la liste de données.

    Args:
        data (list): La liste contenant toutes les lignes du fichier.
        k (int): L'indice de la ligne à retourner.
        
    Returns:
        list: La k-ième ligne de données.
    """
    return data[k]

def get_first(l):
    """Retourne le premier élément de la liste.

    Args:
        l (list): La liste d'entrée.
        
    Returns:
        Le premier élément de la liste.
    """
    return l[0]

def get_last(l):
    """Retourne le dernier élément de la liste.

    Args:
        l (list): La liste d'entrée.
        
    Returns:
        Le dernier élément de la liste.
    """
    return l[-1]

def get_max(l):
    """Retourne l'élément le plus grand de la liste.

    Args:
        l (list): La liste d'entiers.
        
    Returns:
        L'élément le plus grand de la liste.
    """
    return max(l)

def get_min(l):
    """Retourne l'élément le plus petit de la liste.

    Args:
        l (list): La liste d'entiers.
        
    Returns:
        L'élément le plus petit de la liste.
    """
    return min(l)

def get_sum(l):
    """Retourne la somme de tous les éléments de la liste.

    Args:
        l (list): La liste d'entiers.
        
    Returns:
        La somme des éléments de la liste.
    """
    return sum(l)

#### Fonction principale


def main():
    """lit les données et affiche des informations utiles.

    Cette fonction charge les données du fichier et affiche :
    - Le premier et dernier élément de la première ligne.
    - Le minimum, maximum et la somme de la première ligne.
    - Les données de chaque ligne du fichier.
    """
    data = read_data(FILENAME)
    liste = data[0]
    print(get_first(liste))
    print(get_last(liste))
    print(get_min(liste))
    print(get_max(liste))
    print(get_sum(liste))
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
