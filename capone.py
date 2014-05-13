import os
from caponeFile import CapOneFileObj
import shutil
class CapOne:
    
    
    
    def setPath(self, pth):
        
        self.pth = pth
    
    def setPathDest(self, pthdest):
        self.pthDest = pthdest
        
    def getFiles(self, pth):
        
        
        l = os.listdir(pth)
        return l

    def processFile(self, flName):
        
        
        f = open(self.pth + '\\' + flName, 'r')
        
        coF = CapOneFileObj()
        cleanedFile = coF.normalizeFile(f)
   
        coF.createNewFile(f, cleanedFile)

    def processFileTextBased(self, flName, actCount):
        f = open(self.pth + '\\' + flName, 'r')
        coF = CapOneFileObj()
        
        combined = coF.processFileStringBased(f, actCount)
        coF.writeFile(self.pthDest, combined, 'Activity')
        
    def moveFilesUploaded(self, pthDest):
        
        l = os.listdir(self.pthDest)
        pthdesUploaded = 'C:\\IHG\\Cap One\\Uploaded'
        
        for f in l:

            src = self.pthDest + '\\' + str(f)
            de = pthdesUploaded + '\\' + str(f)
            shutil.move(src, de)
    
    
    def processFileTextBasedEnroll(self, flName, enrolCount):
        f = open(self.pth + '\\' + flName, 'r')
    
        coF = CapOneFileObj()
        combined = coF.processFileStringBasedEnrolled(f, enrolCount)
        coF.writeFile(self.pthDest, combined, 'Enrolled')
        
    def processFileTextBasedACC(self, flName, accCount):
        f = open(self.pth + '\\' + flName, 'r')
    
        coF = CapOneFileObj()
        combined = coF.processFileStringBasedACC(f, accCount)
        coF.writeFile(self.pthDest, combined, 'ACC')
    
    def go(self,pth, pthdest):
        
        self.setPath(pth)
        self.setPathDest(pthdest)
        l = self.getFiles(pth)
        actCount = 0
        enrolCount = 0
        accCount = 0
        for f in l:
            
            
            activityFlag = f.find('ACTIVITY')
            enrollFlag = f.find('ENROLL')
            accFlag = f.find('ACCMEMBER')
           
            if activityFlag != -1:
#                 actCount = actCount + 1
                self.processFileTextBased(f, actCount)
                 
              
            if enrollFlag != -1:
#                 enrolCount = enrolCount + 1
                self.processFileTextBasedEnroll(f, enrolCount)
# #             
            if accFlag != -1:
#                 print('acc_Flag')
#                 accCount = accCount + 1
                self.processFileTextBasedACC(f,accCount)
#                 
        self.moveFilesUploaded(self.pthDest)
            