class Spreadsheet:

    def __init__(self, rows: int):
        self.cols = {}
        for i in range(26):
            self.cols[chr(ord("A") + i)] = [0] * rows



    def setCell(self, cell: str, value: int) -> None:
        print(cell, value)
        col = cell[0]
        row = int(cell[1:]) - 1

        self.cols[col][row] = value
        

    def resetCell(self, cell: str) -> None:
        col = cell[0]
        row = int(cell[1:]) - 1

        self.cols[col][row] = 0
        

    def getValue(self, formula: str) -> int:
        if formula[1].isdigit():
            num1 = int(formula[1:formula.index('+')])
        else:
            ref = formula[1:formula.index('+')]
            col = ref[0]
            row = int(ref[1:]) - 1
            num1 = self.cols[col][row]
        
        formula = formula[formula.index('+') + 1:]
        if formula[0].isdigit():
            num2 = int(formula) 
        else:
            col = formula[0]
            row = int(formula[1:]) - 1
            num2 = self.cols[col][row]

        return num1 + num2
            

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)