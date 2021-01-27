
DictPAM = {}
Proteins = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'J', 'Z', 'X']

def BlosumMatrix():
    with open("Blosum.txt", 'r') as file:
        lines = file.read().splitlines()
        Blosum = []
        for line in lines:
            BlosumList = [int(i) for i in line.split()] 
            Blosum.append(BlosumList)
        return Blosum


def generateDic():
    Blosum_MATRIX = BlosumMatrix()

    for i in range(0, len(Proteins)):
        DictPAM[Proteins[i]] = {}
        Helper_Dict = {}
        for j in range(0, len(Proteins)):
            Helper_Dict[Proteins[j]] = Blosum_MATRIX[i][j]

        DictPAM[Proteins[i]] = Helper_Dict
    
    return DictPAM
