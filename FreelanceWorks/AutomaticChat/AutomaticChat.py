import time
import sys
import pyautogui
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):

        """1. Katman!"""  
        self.hello1 = QtWidgets.QPushButton("Hello!")
        self.hello_lobby1 = QtWidgets.QPushButton("Lobby!")
        self.Good_day1 = QtWidgets.QPushButton("Bb!")
        self.hello2 = QtWidgets.QPushButton("Hello!2")
        self.Good_day2 = QtWidgets.QPushButton("Bb!2")
        self.hello_lobby2 = QtWidgets.QPushButton("Lobby!2")

        """2. Katman!"""  
        self.firm_price = QtWidgets.QPushButton("F.Price!") 
        self.how_mduw = QtWidgets.QPushButton("HMDYW?") 
        self.how_mduh = QtWidgets.QPushButton("HMDYH?") 
        self.sure_letsgo = QtWidgets.QPushButton("Sure.L!")
        self.sorry_ichy = QtWidgets.QPushButton("Sorry!")
        self.what_color = QtWidgets.QPushButton("W.Color?")

        """3. Katman!"""  
        self.pls_wait = QtWidgets.QPushButton("Pls.Wait!")
        self.just_write = QtWidgets.QPushButton("PlsWritewdyw!")
        self.pls_quickly = QtWidgets.QPushButton("P.Quickly!")
        self.yes_ = QtWidgets.QPushButton("Yes!")
        self.no_ = QtWidgets.QPushButton("No!")
        self.w_invite= QtWidgets.QPushButton("IwillInte!")

        """4. Katman!"""  
        self.np_myf = QtWidgets.QPushButton("Np.MyFr.")
        self.m_seller = QtWidgets.QPushButton("Iseller")
        self.okay = QtWidgets.QPushButton("Okay.")
        self.Isold = QtWidgets.QPushButton("Isold")
        self.not_inter = QtWidgets.QPushButton("N.Inter")
        self.wdyw = QtWidgets.QPushButton("Wdyw?")

        """5. Katman!""" 
        self.m_buyer = QtWidgets.QPushButton("Ibuyer")
        self.have_or_want = QtWidgets.QPushButton("OrWant?")
        self.thanks = QtWidgets.QPushButton("Thanks.")
        self.mixedhas = QtWidgets.QPushButton("MixHas!")
        self.gameflip = QtWidgets.QPushButton("Gameflip!")
        self.noncrate = QtWidgets.QPushButton("NotNC!")
  
        
        h_box =QtWidgets.QHBoxLayout()
        h2_box =QtWidgets.QHBoxLayout()
        h3_box =QtWidgets.QHBoxLayout()
        h4_box =QtWidgets.QHBoxLayout()
        h5_box =QtWidgets.QHBoxLayout() 

        v_box = QtWidgets.QVBoxLayout()

        """5"""   
        h5_box.addWidget(self.noncrate)
        h5_box.addWidget(self.m_buyer)
        h5_box.addWidget(self.have_or_want)
        h5_box.addWidget(self.thanks)
        h5_box.addWidget(self.mixedhas)
        h5_box.addWidget(self.gameflip)
        """4"""   
        h4_box.addWidget(self.m_seller)
        h4_box.addWidget(self.np_myf)
        h4_box.addWidget(self.okay)
        h4_box.addWidget(self.Isold)
        h4_box.addWidget(self.not_inter)
        h4_box.addWidget(self.wdyw)
        """3"""     
        h3_box.addWidget(self.yes_)
        h3_box.addWidget(self.no_)
        h3_box.addWidget(self.pls_wait)
        h3_box.addWidget(self.just_write)
        h3_box.addWidget(self.pls_quickly)
        h3_box.addWidget(self.w_invite)
        """2"""
        h2_box.addWidget(self.how_mduw)
        h2_box.addWidget(self.how_mduh)
        h2_box.addWidget(self.firm_price)
        h2_box.addWidget(self.sure_letsgo)
        h2_box.addWidget(self.sorry_ichy)
        h2_box.addWidget(self.what_color)
        """1"""
        h_box.addWidget(self.hello1)
        h_box.addWidget(self.hello2)
        h_box.addWidget(self.hello_lobby1)        
        h_box.addWidget(self.hello_lobby2)
        h_box.addWidget(self.Good_day1)        
        h_box.addWidget(self.Good_day2)

        """Main"""
        v_box.addLayout(h5_box) 
        v_box.addLayout(h4_box) 
        v_box.addLayout(h3_box)
        v_box.addLayout(h2_box)
        v_box.addLayout(h_box)

        self.setWindowTitle("Rocket Bot")
        self.setLayout(v_box)

        """5. Katman!"""  
        self.m_buyer.clicked.connect(self.m_buyer_clicked)
        self.have_or_want.clicked.connect(self.have_or_want_clicked)
        self.thanks.clicked.connect(self.thanks_clicked)
        self.mixedhas.clicked.connect(self.mixedhas_clicked)
        self.gameflip.clicked.connect(self.gameflip_clicked)
        self.noncrate.clicked.connect(self.noncrate_clikced)
        """4. Katman!"""  
        self.np_myf.clicked.connect(self.np_myf_clicked)
        self.m_seller.clicked.connect(self.m_seller_clicked)
        self.okay.clicked.connect(self.okay_clicked)
        self.Isold.clicked.connect(self.Isold_clicked)
        self.not_inter.clicked.connect(self.not_inter_clicked)
        self.wdyw.clicked.connect(self.wdyw_clicked)
        
        """3. Katman!"""  
        self.pls_wait.clicked.connect(self.pls_wait_clicked)
        self.just_write.clicked.connect(self.just_write_clicked)
        self.pls_quickly.clicked.connect(self.pls_quickly_clicked)
        self.no_.clicked.connect(self.no_clicked)
        self.yes_.clicked.connect(self.yes_clicked)
        self.w_invite.clicked.connect(self.w_invite_clicked)

        """2. Katman!"""  
        self.firm_price.clicked.connect(self.firm_price_clicked)
        self.how_mduw.clicked.connect(self.how_mduw_clicked)
        self.how_mduh.clicked.connect(self.how_mduh_clicked)
        self.what_color.clicked.connect(self.what_color_clicked)
        self.sorry_ichy.clicked.connect(self.sorry_ichy_clicked)
        self.sure_letsgo.clicked.connect(self.sure_letsgo_clicked)
        
        """1. Katman!"""  
        self.hello2.clicked.connect(self.hello2_clicked)        
        self.hello1.clicked.connect(self.hello1_clicked)
        self.hello_lobby1.clicked.connect(self.hello_lobby1_clicked)
        self.hello_lobby2.clicked.connect(self.hello_lobby2_clicked)
        self.Good_day1.clicked.connect(self.Good_day1_clicked)
        self.Good_day2.clicked.connect(self.Good_day2_clicked)
        
        self.show()

        """5. Katman!"""  
    def noncrate_clikced(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Dont put your Sun Ray")
        self.enter=pyautogui.press("enter") 
        time.sleep(0.6)
        self.yazma=pyautogui.write("Or hot rocks not noncrate!")
        self.enter=pyautogui.press("enter") 
    def gameflip_clicked(self):
        self.tiklama=pyautogui.click(1854,760)
        time.sleep(0.1)
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Ty for your purchase!")
        self.enter=pyautogui.press("enter")
        time.sleep(0.6)
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Pls confirm the trade <3")
        self.enter=pyautogui.press("enter")
        time.sleep(0.6)
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Ty for choosing me!")
        self.enter=pyautogui.press("enter")
    def mixedhas_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("U mixed 'has'-'my wants'!")
        self.enter=pyautogui.press("enter")    
    def thanks_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Thanks!")
        self.enter=pyautogui.press("enter")            
    def have_or_want_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Do u have or want?")
        self.enter=pyautogui.press("enter")     
    def m_buyer_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("I'm buyer not seller!")
        self.enter=pyautogui.press("enter")     
        
        """4. Katman!"""  
    def wdyw_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("What do u want?")
        self.enter=pyautogui.press("enter") 
    def not_inter_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("I'm not interested.")
        self.enter=pyautogui.press("enter") 
    def Isold_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("I sold all sorry :(")
        self.enter=pyautogui.press("enter")  
    def okay_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Okay.")
        self.enter=pyautogui.press("enter")             
    def m_seller_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("I'm seller not buyer!")
        self.enter=pyautogui.press("enter")         
    def np_myf_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Np mate!")
        self.enter=pyautogui.press("enter") 

        """3. Katman!"""  
    def w_invite_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("I will interested everyone!")
        self.enter=pyautogui.press("enter") 
    def no_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("No!")
        self.enter=pyautogui.press("enter") 
    def yes_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Yes.")
        self.enter=pyautogui.press("enter") 
    def pls_quickly_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Pls quickly!")
        self.enter=pyautogui.press("enter") 
    def pls_wait_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Pls just wait your turn!")
        self.enter=pyautogui.press("enter") 
    def just_write_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Pls write wdyw H:xx W:xx")
        self.enter=pyautogui.press("enter") 

        """2. Katman!"""  
    def sure_letsgo_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Sure lets go!")
        self.enter=pyautogui.press("enter")          
    def sorry_ichy_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Sorry I can't help u :(")
        self.enter=pyautogui.press("enter")        
    def what_color_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("What color do u want?")
        self.enter=pyautogui.press("enter")       
    def how_mduh_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("How many do u have?")
        self.enter=pyautogui.press("enter")
    def how_mduw_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("How many do u want?")
        self.enter=pyautogui.press("enter")
    def firm_price_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Firm price sorry :(")
        self.enter=pyautogui.press("enter")

        """1. Katman!"""  
    def hello2_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Hey, How can I help u?")
        self.enter=pyautogui.press("enter")
    def hello1_clicked(self):
        self.tiklama=pyautogui.click(1854,760)
        time.sleep(0.1)
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Hey, How can I help u?")
        self.enter=pyautogui.press("enter")
    def hello_lobby2_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Hey guys trader is me Wdyw?")
        self.enter=pyautogui.press("enter")
    def hello_lobby1_clicked(self):
        self.tiklama = pyautogui.click(1854, 760)
        time.sleep(0.1)
        self.tiklama=pyautogui.click(1637,728)
        self.yazma=pyautogui.write("Hey guys trader is me Wdyw?")
        self.enter=pyautogui.press("enter")
    def Good_day2_clicked(self):
        self.tiklama=pyautogui.click(1637,728)
        self.yazma = pyautogui.write("Have a great day!")
        self.enter = pyautogui.press("enter")
    def Good_day1_clicked(self):
        self.tiklama=pyautogui.click(1854,760)
        time.sleep(0.1)
        self.tiklama=pyautogui.click(1637,728)
        self.yazma = pyautogui.write("Have a great day!")
        self.enter = pyautogui.press("enter")

app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())


