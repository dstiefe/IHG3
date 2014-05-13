
import shutil
import os

from barclaysRecord import BarclaysRecord
from databaseuploader import BarclaysDB

class Barclays:
    
    
    
        
    
    def getFiles(self,pth ):
#         PTH = self.Path + '\\Src'
     
        l = os.listdir(pth)
        return l
    
    def readFile(self, fl, cnt):
   
        f = open(self.pth + '\\' + str(fl), 'r')
        header = []
        ds = []
        if cnt == 1:
           
            fieldNames = self.fieldNames()
            
            ds.append(fieldNames)
        for rw in f:
            newRw = rw.split(' ')

                                
            
            # get header info
            newRecord = []
            detail = []
            if str(newRw[0])[:2] == '10':
#                 print('record ==10')
                header = BarclaysRecord().process(newRw, str(newRw[0])[:2])
          
            if len(header) != 0:  
                if str(newRw[0])[:2] == '20':
                    detail = BarclaysRecord().process(newRw, str(newRw[0])[:2])
                    
                    newRecord = detail + header
#                     print('this is appended' + str(newRecord))
                 
                    ds.append(newRecord)
        
        return ds
    
    def writeFile(self, ds, PTH):
        flName = self.pthDest + '\\' + 'Barclays_processed_file.txt'
        f = open(PTH + '\\' + 'Barclays_processed_file.txt' , 'a')
        
        for rw in ds:
            rw.append('\n')
            newRwPrint = '|'.join(rw)
            
            f.write(newRwPrint)
            
        coDB = BarclaysDB(flName).go()
        
    def fieldNames(self):
        
        fieldNames = ['Record_id', 'PCR_Member_#', 'Alliance_Code', 'Partner_Transaction_Date', 'Promotion_Identifier', 'Total_PCR_Credits_Earned', 'Source_Agent',  'Transaction_Status', 'Status_Code', 'Status_Description', 'Header_Record_Id', 'Header_File_Creation_Date', 'Header_Description', 'Header_ProgramId', 'Header_Agent_Id', 'Header_File_Sequence_number']
        
        return fieldNames

    def setPath(self, pth):
        self.pth = pth
        
    def setDestPath(self, pthDest):
        self.pthDest = pthDest
    
    def setDestPathUploaded(self, pthDestUploaded):
        
        self.pthDestUploaded = pthDestUploaded
        
    
    def moveFilesUploaded(self, pthDest):
        
        l = os.listdir(self.pthDest)
        pthdesUploaded = 'C:\\IHG\\Barclay\\Uploaded'
        
        for f in l:

            src = self.pthDest + '\\' + str(f)
            de = pthdesUploaded + '\\' + str(f)
            shutil.move(src, de)

    def go(self, pth , pthDest):
        
        self.setDestPath(pthDest)
        self.setPath(pth)
       
        pth = self.pth
        
        fl = self.getFiles(pth)
        x = 0
        
        for rw in fl:
#             x = x + 1
            ds = self.readFile(rw, x)
            self.writeFile(ds, self.pthDest)

        self.moveFilesUploaded(self.pthDest)
        
if __name__ == '__main__':
    
    print('hello')
    pth = 'C:\\IHG\\Barclay\\Src'
    pthDest = 'C:\\IHG\\Barclay\\Processed'

    bc = Barclays()
    bc.go(pth, pthDest)
#     fl = bc.getFiles()
#     x = 0
#     for rw in fl:
#         x = x + 1
#         ds = bc.readFile(rw, x)
#         bc.writeFile(ds, PTH)
    
   