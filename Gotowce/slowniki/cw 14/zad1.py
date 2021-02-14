#przedstawiam jeden z najbrzydszych kodów, jakie można było do tego zadania wymyślić.
#Zasada DRY niezachowana, nazwy zmiennych mocno nieintuicyjne, cały algorytm jakiś chory i
# niełatwy do zrozumienia... ale przynajmniej fajnie jest zaimplementowane budowanie drzewa od dołu :)

from math import ceil

class auxNode:
    def __init__(self):
        self.max = 0
        self.left = 0
        self.right = 0
        self.leftson = None
        self.rightson = None
        self.parent = None

class leaf:
    def __init__(self, val):
        self.val = val          #1 zapalona, 0 nie zapalona
        self.parent = None


def darknessTreeInit(data):
    n = len(data)
    prepData = [leaf(val) for val in data]      #dane muszą być spreparowane, aby posiadały wskaźnik na rodzica

    tmp = [0]*ceil(n/2)
    for i in range(ceil(n/2)):      #budowanie pierwszego poziomu od dołu
        tmp[i] = auxNode()
        if 2*i + 1 < n and prepData[2*i+1].val == 0 and prepData[2*i].val == 0:
            tmp[i].right = 2
            tmp[i].left = 2
            tmp[i].max = 2
        elif prepData[2*i].val == 0:
            tmp[i].left = 1
            tmp[i].max = 1
            if 2*i+1 == n:
                tmp[i].right = 1
        elif 2*i+1 < n and prepData[2*i+1].val == 0:
            tmp[i].right = 1
            tmp[i].max = 1
        tmp[i].leftson = prepData[2*i]
        prepData[2*i].parent = tmp[i]
        if 2*i+1 < n:
            tmp[i].rightson = prepData[2*i+1]
            prepData[2*i+1].parent = tmp[i]

    while len(tmp)//2 > 0:      #budowanie pozostałych poziomów
        aux = [0]*ceil(len(tmp) / 2)        #aux obecnie budowany poziom, tmp - poprzedni
        for i in range(len(aux)):
            aux[i] = auxNode()
            if 2*i+1 == len(tmp):       #jeżeli budujemy ostatni węzeł dla len(tmp) nieparzystego
                aux[i].max = tmp[2*i].max
                aux[i].left = tmp[2*i].left
                aux[i].right = tmp[2*i].right
                aux[i].leftson = tmp[2*i]
            else:                           #w innym przypadku
                aux[i].left = tmp[2*i].left
                if tmp[2*i].left != 0 and tmp[2*i].left == tmp[2*i].max and tmp[2*i].left == tmp[2*i].right:
                    aux[i].left += tmp[2*i+1].left          #jezeli zera wypełniają cały lewy przedział, dodajemy lewą wartość prawego przedziału

                aux[i].right = tmp[2 * i+1].right
                if tmp[2*i+1] != 0 and tmp[2*i+1].right == tmp[2*i+1].left and tmp[2*i+1].right == tmp[2*i+1].max:
                    aux[i].right += tmp[2*i].right          #jezeli zera wypałniają cały prawy przedział, dodajemy prawą wartość lewego przedziału

                aux[i].max = max(tmp[2*i].max, tmp[2*i+1].max,
                                 tmp[2*i].right+tmp[2*i+1].left)        #max budowanego węzła to max poniższych lub suma "wewnętrznych" zer

                aux[i].leftson = tmp[2*i]
                aux[i].rightson = tmp[2*i+1]
            tmp[2*i].parent = aux[i]
            if 2*i+1 < len(tmp):   tmp[2*i+1].parent = aux[i]

        tmp = aux
    return aux[0], prepData

def heapify(prepData, i):           #analogiczna do heapify procedura naprawy drzewa
    parent = prepData[i].parent
    if i%2 == 1:        #sprawdzenie, czy zmieniliśmy prawe czy lewe dziecko
        leftson = parent.leftson
        rightson = prepData[i]
    else:
        leftson = prepData[i]
        rightson = parent.rightson

    if rightson is None:
        parent.max = parent.left = parent.right = 1 - leftson.val
    elif leftson.val == 0 and rightson.val == 0:
        parent.max = 2
        parent.left = 2
        parent.right = 2
    elif leftson.val != rightson.val:       #można na to patrzeć jak na XOR logiczny - jeśli jedna się świeci
        parent.max = 1
        parent.left = 1 - leftson.val
        parent.right = 1 - rightson.val

    parent = parent.parent      #za takie nazwy zmiennych diabeł już ostrzy na mnie widły
    while True:
        if parent.rightson is None:
            leftson = parent.leftson
            parent.max = leftson.max
            parent.left = leftson.left
            parent.right = leftson.right
        else:
            leftson = parent.leftson
            rightson = parent.rightson

            parent.left = leftson.left
            if leftson.left != 0 and leftson.left == leftson.right and leftson.left == leftson.max:
                parent.left += rightson.left

            parent.right = rightson.right
            if rightson.right != 0 and rightson.right == rightson.left and rightson.right == rightson.max:
                parent.right += leftson.right

            parent.max = max(rightson.max, leftson.max, leftson.right + rightson.left)

        if parent.parent is None:
            return parent
        else:
            parent = parent.parent


def makelight(prepData, i):     #przynajmniej to jest w miarę zrozumiałe XD
    prepData[i].val = 1
    root = heapify(prepData, i)
    return root

def dimlight(prepData, i):
    prepData[i].val = 0
    root = heapify(prepData, i)
    return root


def maxdarkness(T):
    return T.max


data = [1,0,1,0,1,0,0,0,1,0,0]
T, prepData = darknessTreeInit(data)
print(maxdarkness(T))
T = makelight(prepData, 1)
T = dimlight(prepData, 8)
print(maxdarkness(T))