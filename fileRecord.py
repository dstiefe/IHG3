


class CapOneRecord:
    
    
    
    def determineRecordId(self, rec):
        
        
        
        recType = rec[:2]
        
        if recType == '10':
            ds = self._processRecordMain('10', rec)
            return ds
        if recType == '20':
            ds = self._processRecordMain('20', rec)
            return ds

    def _processRecordMain(self, recType, rec):
        
        if recType == '10': 
        
            procRecord =  self._processDetailRecord(rec)
        
        if recType == '20':
            procRecord =  self._processDetailRecord(rec)
            
        
        return procRecord
      
    def _processDetailRecord(self, rec):
        
        ds = []
        row = []
        cnt = 0
#         print(rec)
        while cnt < len(rec):
            
            if cnt == 0:
                row.append(rec[cnt])
                
            else:
                
                if rec[cnt] == ' ' and rec[cnt-1] == ' ':
                    if len(row) != 0:
                        x = ''.join(row)
                        ds.append(x)
                    row = [] 
                     
                else:
                    row.append(rec[cnt]) 
                  
                         
            
            cnt = cnt + 1    
        
        return ds 
    
    def processHeader(self, hd):
        newRec = []
#         print(hd)
        print(hd)
        header_id = '10'
        version = str(hd[0])[2:4]
        agent_id = str(hd[0][4:7])
        dateBase = str(hd[1])
      
        yr = dateBase[2:4]
        mth = dateBase[4:6]
        dy = dateBase[6:8]
        dateFinal = '20' + yr + '-' + mth + '-' + dy
        
        program_id = str(hd[2])[-3:]
        program_id.strip()
        description = 'Capital One'
        file_sequence = '0000000'
        
        newRec.append(header_id)
        newRec.append(version)
        newRec.append(agent_id)
        newRec.append(dateFinal)
        newRec.append(program_id)
        newRec.append(description)
        newRec.append(file_sequence)
        
        return newRec
        
#     def processDetail(self, dt):
  
    def processStringBasedRecord(self,rec):
        
        
        recType = rec[:2]
        if recType == '10':
            hd = self.processStringBasedHeader(rec)
            return hd
        
        
        if recType == '20':
            
            hd = self.processSTringBasedDetail(rec)
            return hd

    def processStringBasedHeader(self, rec):
        header = []
        record_id = rec[:2]
        version = 'V1'
        agent_id = 'CPO'
        file_create_date_base = rec[34:40]
       
        yr = '20' + file_create_date_base[:2]
       
        mnth = file_create_date_base[2:4]
        day = file_create_date_base[4:6]
        date_final = yr + '-' + mnth + '-' + day
        program_id = 'PC'
        description = 'Capital One'
        file_sequence_number = '0000000'
        
        header.append(record_id)
        header.append(version)
        header.append(agent_id)
        header.append(date_final)
        header.append(program_id)
        header.append(description)
        header.append(file_sequence_number)
        
        return header

    def processSTringBasedDetail(self, rec):
        detail = []
        record_id = rec[:2]
        
        tracking_number = rec[2:12].strip()
        account_number = rec[12:28].strip()
        
        pcr_member = rec[28:53].strip()
        source_agent = 'CPO'
        description = rec[142:147].strip()
        promotion_identifier = rec[147:153].strip()
        alliance_code = 'HPC'
        parter_transaction_date_base = rec[170:176].strip()
        yr = '20' + parter_transaction_date_base[:2]
        month = parter_transaction_date_base[2:4]
        day = parter_transaction_date_base[4:6]
        parter_transaction_date = yr + '-' + month + '-' + day
        
        prc_credits_earned = rec[184:193].strip()
        tran_status = rec[193:194].strip()
        status_code = rec[194:200].strip()
        if status_code == '000000':
            transaction_status = 'P'
        else:
            transaction_status = 'R'
        status_description = rec[215:279].strip()

        detail.append(record_id)
        detail.append(tracking_number)
        detail.append(account_number)
        detail.append(pcr_member)
        detail.append(source_agent)
        detail.append(description)
        detail.append(promotion_identifier)
        detail.append(alliance_code)
        detail.append(parter_transaction_date)
        detail.append(prc_credits_earned)
#         detail.append(tran_status)
        detail.append(status_code)
        detail.append(transaction_status)
        detail.append(status_description)
        
       
        return detail
       
    def processStringBasedRecordEnrolled(self,rec):
        
#         print(rec)
        recType = rec[:2]
        if recType == '10':
            hd = self.processStringBasedRecordEnrolledHeader(rec)
            return hd
        
        
        if recType == '02':
            
            hd = self.processStringBasedRecordEnrolledDetail(rec)
            return hd
 
    def processStringBasedRecordEnrolledHeader(self, rec):
        
        header = []

        record_id = '10'
        version = 'V1'
        agent_id = 'CPO'
        
        dateBase = rec[34:40]
        yr = '20' + dateBase[:2]
        month = dateBase[2:4]
        day = dateBase[4:6]
        dateFinal = yr + '-' + month + '-' + day
        
        program_id = 'PC'
        description = 'Capital One'
        file_sequence_number = '0000000'
        
        header.append(record_id)
        header.append(version)
        header.append(agent_id)
        header.append(dateFinal)
        header.append(program_id)
        header.append(description)
        header.append(file_sequence_number)
        
        return header
   
    def processStringBasedRecordEnrolledDetail(self,rec):
        detail = []
#         print(rec)
        
        record_id = '02'
        account_reference = rec[12:28].strip()
        pcr_member_id = rec[28:53].strip()
        card_type = rec[74:77].strip()
        first_name = rec[85:110].strip()
        middle_name = rec[110:135].strip()
        last_name = rec[135:175].strip()
        address_type = rec[175:177].strip()
        en_address1 = rec[207:252].strip()
        en_address2 = rec[252:297].strip()
        en_city = rec[297:347].strip()
        country_code = rec[347:351].strip()
        en_state = rec[351:353].strip()
        en_zip = rec[353:366].strip()
        language_spoken = rec[366:370].strip()
        phone_1 = rec[370:395].strip()
        phone_1_usage = rec[395:396].strip()
        phone_2 = rec[396:421].strip()
        phone_2_usage = rec[421:422].strip()
        status_code = rec[422:428].strip()
        if status_code == '000000':
            transaction_status = 'P'
        else:
            transaction_status = 'R'
        status_description = rec[436:500].strip()
        
        detail.append(record_id)
        detail.append(account_reference)
        detail.append(pcr_member_id)
        detail.append(card_type)
        detail.append(first_name)
        detail.append(middle_name)
        detail.append(last_name)
        detail.append(address_type)
        detail.append(en_address1)
        detail.append(en_address2)
        detail.append(en_city)
        detail.append(country_code)
        detail.append(en_state)
        detail.append(en_zip)
        detail.append(language_spoken)
        detail.append(phone_1)
        detail.append(phone_1_usage)
        detail.append(phone_2)
        detail.append(phone_2_usage)
        detail.append(status_code)
        detail.append(transaction_status)
        detail.append(status_description)
        
        return detail

    def processStringBasedRecordACC(self,rec):
        
#         print(rec)
        recType = rec[:2]
        if recType == '10':
            hd = self.processStringBasedRecordACCHeader(rec)
           
            return hd
         
         
        if recType == '08':
              
            hd = self.processStringBasedRecordACCDetail(rec)
            return hd     

    def processStringBasedRecordACCHeader(self, rec):
        
        header = []

        record_id = '10'
        version = 'V1'
        agent_id = 'CPO'
        
        dateBase = rec[34:40]
        yr = '20' + dateBase[:2]
        month = dateBase[2:4]
        day = dateBase[4:6]
        dateFinal = yr + '-' + month + '-' + day
        
        program_id = 'PC'
        description = 'Capital One'
        file_sequence_number = '0000000'
        
        header.append(record_id)
        header.append(version)
        header.append(agent_id)
        header.append(dateFinal)
        header.append(program_id)
        header.append(description)
        header.append(file_sequence_number)
        
        return header   
   
    def processStringBasedRecordACCDetail(self,rec):
        detail = []
#         print(rec)
        
        record_id = '08'
        account_reference = rec[13:29].strip()
        pcr_member_id = rec[29:54].strip()
        enrollement_source_code = rec[72:75].strip()
        card_type = rec[75:78].strip()
        last_name = rec[86:126].strip()
        first_name = rec[126:151].strip()
#         middle_name = rec[110:135].strip()
        
#         address_type = rec[175:177].strip()
#         en_address1 = rec[207:252].strip()
#         en_address2 = rec[252:297].strip()
#         en_city = rec[297:347].strip()
#         country_code = rec[347:351].strip()
#         en_state = rec[351:353].strip()
#         en_zip = rec[353:366].strip()
        language_spoken = rec[151:155].strip()
#         phone_1 = rec[370:395].strip()
#         phone_1_usage = rec[395:396].strip()
#         phone_2 = rec[396:421].strip()
#         phone_2_usage = rec[421:422].strip()
        status_code = rec[155:161].strip()
        
        if status_code == '000000':
            transaction_status = 'P'
        else:
            transaction_status = 'R'
        status_description = rec[176:240].strip()
        
        detail.append(record_id)
        detail.append(account_reference)
        detail.append(pcr_member_id)
        detail.append(enrollement_source_code)
        detail.append(card_type)
        detail.append(last_name)
        detail.append(first_name)
#         detail.append(middle_name)
    
#         detail.append(address_type)
#         detail.append(en_address1)
#         detail.append(en_address2)
#         detail.append(en_city)
#         detail.append(country_code)
#         detail.append(en_state)
#         detail.append(en_zip)
        detail.append(language_spoken)
#         detail.append(phone_1)
#         detail.append(phone_1_usage)
#         detail.append(phone_2)
#         detail.append(phone_2_usage)
        detail.append(status_code)
        detail.append(status_description)
        detail.append(transaction_status)
        
        print(detail)
        return detail
