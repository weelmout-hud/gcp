import requests
from bs4 import BeautifulSoup
import json
import sys
import urllib.request as ur
import urllib.request
import traceback


# local frameworks
from Docxsupp import Dokument_var_change
from Fetchdatabase import Fetchingdata
from Sending import Send_it


def main(requests):

    ERR_VAR_NAME = ""
    ADDI_JSON_NEW_NAME = ""
    NEW_JSON_OUTPUT = ""
    ADDI_JSON_OLD_NAME = ""
    char_x = ""
    char_z = ""
    char_u = ""
    char_y = ""
    OLD_JSON_OUTPUT = ""
    ADDI_JSON_ERROR = ""
    DLX_VAR_NAME = ""
    ADDI_JSON_DLX = ""
    
    
    try:
    # Calling variables
        char_x = "{"
        char_y = "}"
        char_z = ":"
        char_w = '"'
        char_u = ","
        dlx_v = "DLX"
        err_v = "Error Description"
        
        # requesting parameters from username
        requests_args = requests.args
        
        if requests_args and "new_assetname" in requests_args and "old_assetname" in requests_args and "error_description" in requests_args and "dlx_name" in requests_args and "dlx_name_for_call" in requests_args and "if_correct" in requests_args and "if_repair" in requests_args and "ticket" in requests_args:
            new_assetname = requests_args['new_assetname']
            old_assetname = requests_args['old_assetname']
            error_description = requests_args['error_description']
            dlx_name = requests_args['dlx_name']
            dlx_name_for_call = requests_args['dlx_name_for_call']
            if_correct = requests_args['if_correct']
            if_repair = requests_args['if_repair']
            ticket = requests_args['ticket']
            
        else:
            new_assetname = "error"
            old_assetname = "error"
            error_description = "error"
            dlx_name = "error"
            dlx_name_for_call = "error"
            if_correct = "error"
            if_repair = "error"
            ticket = "error"
            
        print(if_correct, if_repair, dlx_name_for_call)
            
        # Validating DLX input
        validate_it = validate_input(dlx_name)
        
        # Validating New AssetName input
        validate_assets_new = validate_assets(new_assetname)
        
        # Validating Old AssetName input
        validate_assets_old = validate_assets(old_assetname)


        # validating data
        if validate_it == False:
            return f'{char_x}\n\t"Warning"{char_z} "Wpisałeś {dlx_name}, wpisz proszę poprawny DLX",\n\t "Err_code"{char_z} "404" \n{char_y}'
            sys.exit()

        elif validate_assets_new == False:
            return f'{char_x}\n\t"Warning"{char_z} "Wpisałeś {new_assetname}, wpisz proszę poprawny nowy AssetName",\n\t "Err_code"{char_z} "404" \n{char_y}'
            sys.exit()

        elif validate_assets_old == False:
            return f'{char_x}\n\t"Warning"{char_z} "Wpisałeś {old_assetname}, wpisz proszę poprawny stary AssetName", \n\t "Err_code"{char_z} "404" \n{char_y}'
            sys.exit()

        else:
            # Instance of a class which Fetchs out all needed data from db which is dependent from "dlx_name"
            fetch_data = Fetchingdata()
            fetch_dlx = fetch_data.dataFetch(dlx_name)
            vars_fetch = vars(fetch_data)
            
            if vars_fetch["id"] == 99:
                return f'{char_x}\n\t"Insert proper input, current one isint stored in database" \n{char_y}'
                sys.exit()

            # Fetching exact cells from database
            fetch_name = vars_fetch["f_name"]
            fetch_surname = vars_fetch["f_surname"]
            fetch_non_pol_name = vars_fetch["f_non_pol_name"]
            fetch_non_pol_surname = vars_fetch["f_non_pol_surname"]

            # Instance of a class calling an Outllok app with parameters
            email_sender_class = Send_it()
            email_sender_def = email_sender_class.sender(dlx_name,new_assetname,old_assetname,fetch_name, fetch_surname, fetch_non_pol_name,fetch_non_pol_surname)

            # Instance of a class outputing json convertion of a new device
            NEW = Convert_asset()
            NEW_CONVERT = NEW.convert_new(new_assetname)
            NEW_VARS = vars(NEW)
            NEW_JSON_OUTPUT = NEW_VARS["convert_python_new"]

            # Instance of a class outputing json convertion of an old device
            OLD = Convert_asset()
            OLD_CONVERT = OLD.convert_old(old_assetname)
            OLD_VARS = vars(OLD)
            OLD_JSON_OUTPUT = OLD_VARS["convert_python_old"]
            # instance of a class changing data in .docx document
            DOCX_CLASS = Dokument_var_change()
            DOCX_DEVICE_CLASS = Devices()
            DOCX_CREATE_CLASS = DOCX_DEVICE_CLASS.create_device(old_assetname)
            VARS_DEVICE_DOCX_OLD = vars(DOCX_DEVICE_CLASS)
            # instance of a class calling needed variables for a .docx input
            DOCX_CLASS = Dokument_var_change()
            DOCX_DEVICE_CLASS = Devices()
            DOCX_CREATE_CLASS = DOCX_DEVICE_CLASS.create_device(new_assetname)
            VARS_DEVICE_DOCX_NEW = vars(DOCX_DEVICE_CLASS)
            
            # musisz callować na nowo instancje klasy, co za gówno eozu, musi się zamykac po wykonaniu zapytania w końcu jest destrukotr lol
            DN = dlx_name
            DevN = VARS_DEVICE_DOCX_OLD["Device"]
            ED =  error_description
            DNFC = dlx_name_for_call
            IF = if_repair
            IC = if_correct
            TC = ticket
            
            AN = VARS_DEVICE_DOCX_NEW["AssetName"]
            PN = VARS_DEVICE_DOCX_NEW["Process_name"]
            IPN = VARS_DEVICE_DOCX_NEW["IP_address1"]
            SNN = VARS_DEVICE_DOCX_NEW["Serial_no"]
            LN = VARS_DEVICE_DOCX_NEW["Location"]

            AO = VARS_DEVICE_DOCX_OLD["AssetName"]
            PO = VARS_DEVICE_DOCX_OLD["Process_name"]
            IPO = VARS_DEVICE_DOCX_OLD["IP_address1"]
            SNO = VARS_DEVICE_DOCX_OLD["Serial_no"]
            #LO =  VARS_DEVICE_DOCX_OLD["Location"] -- użyte później jako stała
            
            DOCX_VAR_CHANGE = DOCX_CLASS.var_change(DN,DevN,AN,AO,PN,PO,IPN,IPO,SNN,SNO,LN,ED,DNFC,IC,IF,TC)
            
            DOCX_FILE_OPERATIONS = DOCX_CLASS.file_operations(DevN,AO,AN,ticket)
            
            # Instance of a class outputing json convertion of a additional variables that are used in a "return"
            ADDI_VARIABLE = Input_side_variables()
            ADDI_CONVERT = ADDI_VARIABLE.input_them(error_description,dlx_name)
            ADDI_VARS = vars(ADDI_VARIABLE)
            ADDI_JSON_OUTPUT = json.dumps(ADDI_VARS)

            # Calls for variables that are going to be converted to JSOn
            CALL_NEW_NAME = ADDI_VARS["new_name"]
            CALL_OLD_NAME = ADDI_VARS["old_name"]
            CALL_ERROR = ADDI_VARS["error"]
            CALL_DLX = ADDI_VARS["dlx"]

            # Converting CALL's to JSON
            ADDI_JSON_NEW_NAME = json.dumps(CALL_NEW_NAME, default=lambda o: o.__dict__,sort_keys=True, indent=4)
            ADDI_JSON_OLD_NAME = json.dumps(CALL_OLD_NAME, default=lambda o: o.__dict__,sort_keys=True, indent=4)
            ADDI_JSON_ERROR = json.dumps(CALL_ERROR, default=lambda o: o.__dict__,sort_keys=True, indent=4)
            ADDI_JSON_DLX = json.dumps(CALL_DLX, default=lambda o: o.__dict__,sort_keys=True, indent=4)

            # Converting Descriptions of an object to JSON
            DLX_VAR_NAME = json.dumps(dlx_v, default=lambda o: o.__dict__,sort_keys=True, indent=4)
            ERR_VAR_NAME = json.dumps(err_v, default=lambda o: o.__dict__,sort_keys=True, indent=4)
            return f"{char_x}{ADDI_JSON_NEW_NAME}{char_z}{NEW_JSON_OUTPUT}{char_u}\n\t{ADDI_JSON_OLD_NAME}{char_z}{OLD_JSON_OUTPUT}{char_u}\n{ERR_VAR_NAME}{char_z}{ADDI_JSON_ERROR}{char_u}\n{DLX_VAR_NAME}{char_z}{ADDI_JSON_DLX}\n, \n {char_w}Err_code{char_w}{char_z} {char_w}200{char_w} {char_y}"

    # Validcja błędu ez
    except Exception:
        err_mess = traceback.print_exc()
        return f'Błąd {err_mess}'
    
        # Returns all to HTTP

class Devices():
    def create_device(self,zmienna_wejsciowa):
        #URL = f'http://assetlist.prodwr.vwpn.emea.vwg/details.php?id={zmienna_wejsciowa}&event=0'
        URL = f'http://localhost:8000/{zmienna_wejsciowa}.html'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        data_collection = soup.find_all('div', class_='limiter')
        assetName_collection = soup.find_all('div', class_='limiter')

        for my_asset in assetName_collection:
            assetName_search = my_asset.find_all ('th', class_='columndet2')

        for my_data in data_collection:
            data_name = my_data.find_all('td', class_='columndet1')
            data_content = my_data.find_all('td', class_='columndet2')


        #Asigning direct containers of a table to the variables
        walidate_fourth = 4
        walidate_fifth = 5
        walidate_six = 6

        test_mac_adr2 = data_name[3].text
        test_mac_adr3 = data_name[4].text

        if test_mac_adr2 == "MAC_address2" or test_mac_adr2 == "MAC_address3":
            walidate_fourth = walidate_fourth + 1
            walidate_fifth = walidate_fifth + 1
            walidate_six = walidate_six + 1

        elif test_mac_adr3 == "MAC_address3" or test_mac_adr3 == "MAC_address2":
            walidate_fourth = walidate_fourth + 1
            walidate_fifth = walidate_fifth + 1
            walidate_six = walidate_six + 1
        self.AssetName = assetName_search[0].text
        self.Process_name = data_content[0].text
        self.IP_address1 = data_content[1].text
        self.MAC_address1 = data_content[2].text
        self.Device = data_content[walidate_fourth].text
        self.Serial_no = data_content[walidate_fifth].text
        self.Location = data_content[walidate_six].text

        return self.__dict__ #returnes objects of a func. (all of them)

class Convert_asset(Devices):
    def convert_new(self,new_asset):
        self.new_asset = new_asset
        self.new_device = Devices()
        self.new_creation = self.new_device.create_device(self.new_asset)
        self.return_vars_new = vars(self.new_device)
        self.convert_python_new = json.dumps((self.return_vars_new), default=lambda o: o.__dict__,sort_keys=True, indent=4)

    def convert_old(self,old_asset):
        self.old_asset = old_asset
        self.old_device = Devices()
        self.old_creation = self.old_device.create_device(old_asset)
        self.return_vars_old = vars(self.old_device)
        self.convert_python_old = json.dumps((self.return_vars_old), default=lambda o: o.__dict__,sort_keys=True, indent=4)

class Input_side_variables():
    def input_them(self, error, dlx):
        self.error = error
        self.dlx = dlx
        self.new_name = "New Device "
        self.old_name = "Old Device "

def validate_input(var_input):
    input_lenght = len(var_input)
    if input_lenght > 7 or input_lenght < 6:
        return False
    else:
        return True

def validate_assets(enter_value):
    check_error = ur.Request(f'http://localhost:8000/{enter_value}.html')     

    try:
        urllib.request.urlopen(check_error)

    except urllib.error.HTTPError as error_asset:
        exception = str((error_asset.code))
        
        print(error_asset.code)
        if exception == "404":
            return False
        else:
            return True

