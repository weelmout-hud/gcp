import win32com.client as client
import pythoncom

from Fetchdatabase import Fetchingdata

class Send_it():

    def sender(self,dlx, new_asset, old_asset,name,surname,non_pol_name,non_pol_surname):
        pythoncom.CoInitialize()
        self.name = name
        self.surname = surname
        self.non_pol_name = non_pol_name
        self.non_pol_surname = non_pol_surname
        self.dlx = dlx
        self.new_asset = new_asset
        self.old_asset = old_asset
        
        if self.dlx == True:
            self.name = ""
            self.surname = ""
            self.non_pol_name = ""
            self.non_pol_surname = ""
        else:
            pass
        outlook= client.Dispatch("Outlook.Application")
        message = outlook.CreateItem(0)

        message.Display()
        message.To = "barnaber13@gmail.com"
        message.Subject = f"Dokument wymiany {self.new_asset} na {self.old_asset}"
        message.Attachments.Add(r'C:/Users/barna/OneDrive/Trocha/QP.png')
        html_body = f"""
            <div>
                <span>
                Cześć,<br>przesyłam dokument wymiany {self.new_asset} na {self.old_asset}<br>
                </span>
                
                <span style="font-size: 11;">
                    <br>Pozdrawiam / Kind regards / Mit freundlichen Grüßen<br> <b>{self.name} {self.surname}<br><br> H&D – An HCL Technologies Company<br> H&D International Sp. z o.o. Oddział w Polsce</b><br><br> Plac Andersa 7<br> 61-894 Poznań<br> Tel: +48 616642679<br> Mobile: +48 538445687<br><br> E-Mail: extern.{self.non_pol_name} {self.non_pol_surname}@vw-poznan.pl<br> Web: www.hud.de<br><br>
                </span>
                
                <span style="font-size: 8;">
                    Geschäftsführer:<br>  Bernhard Hönigsberg Anita Hönigsberg<br>  Claudia Raabe Andreas Lehmann<br>  Karl-Heinz Franke<br><br> Sitz der Gesellschaft:<br>  Wolfsburg Amtsgericht Braunschweig<br> HRB 201 129<br><br><br> Ta wiadomość została wysłana w ramach umowy pomiędzy Volkswagen Poznań Sp. z o.o. a H &D International Group, na zlecenie działu – IT Września – PF-3/4<br> Diese Nachricht wurde in Rahmen des Vertrages zwischen Volkswagen Poznań Sp. z o.o. und H &D International Group im Auftrag von  IT Września – PF-3/4<br><br>
                </span>
                
                <span style="font-size: 11;">
                    <br> INTERNAL
                </span>
            <div>
        """
        message.HTMLBody = html_body