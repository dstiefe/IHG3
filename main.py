
from capone import CapOne
from barclays import Barclays
from citicDeposit import CiticDeposit
from citicVerify import CiticVerify

def toDo():

    lastCell = last_cell_in_col("A").row
    

    x = 1
    todo = {}
    while x < lastCell:
        x = x + 1
        todo.update({

                    Cell(x,1).value : Cell(x,2).value
        
                    })
        
    return todo

def kickOff(ls):

    for k,v in ls.iteritems():

        if k == 'Cap One' and v == 'Yes':
            Cell("D2").value = '=Now()'
            Cell("C2").value = Cell("D2").value
            Cell("D2").value = ""
            
            capone = CapOne()
            capone.go('C:\\IHG\\Cap One\\Src','C:\\IHG\\Cap One\\Processed' )

            Cell("e2").value = '=Now()'
            Cell("d2").value = Cell("e2").value
            Cell("e2").value = ""
            
        if k == 'Barclays' and v == 'Yes':
            Cell("D3").value = '=Now()'
            Cell("C3").value = Cell("D3").value
            Cell("D3").value = ""

            bc = Barclays()
            bc.go('C:\\IHG\\Barclay\\Src', 'C:\\IHG\\Barclay\\Processed')

            Cell("e3").value = '=Now()'
            Cell("d3").value = Cell("e3").value
            Cell("e3").value = ""


        if k == 'Citic' and v == 'Yes':
            Cell("D4").value = '=Now()'
            Cell("C4").value = Cell("D4").value
            Cell("D4").value = ""
            cd = CiticDeposit()
            cd.process('C:\\IHG\\CITIC\\DEPOSIT\\Src', 'C:\\IHG\\CITIC\\DEPOSIT\\Processed')
    
            cv = CiticVerify()
            cv.process('C:\\IHG\\CITIC\\VERIFY\\Src', 'C:\\IHG\\CITIC\\VERIFY\\Processed')

            Cell("e4").value = '=Now()'
            Cell("d4").value = Cell("e4").value
            Cell("e4").value = ""
    
    
if __name__ == '__main__':
#     
#     ls = toDo()
#     kickOff(ls)
#     

    
#       
#     capone = CapOne()
#     capone.go('C:\\IHG\\Cap One\\Src','C:\\IHG\\Cap One\\Processed' )
#          
#     bc = Barclays()
#     bc.go('C:\\IHG\\Barclay\\Src', 'C:\\IHG\\Barclay\\Processed')
         
#     cd = CiticDeposit()
#     cd.process('C:\\IHG\\CITIC\\DEPOSIT\\Src', 'C:\\IHG\\CITIC\\DEPOSIT\\Processed')
#         
    cv = CiticVerify()
    cv.process('C:\\IHG\\CITIC\\VERIFY\\Src', 'C:\\IHG\\CITIC\\VERIFY\\Processed')
