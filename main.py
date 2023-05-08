#BIBLIOTECAS UTILIZADAS
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen 
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import sys

# JANELAS ARQUIVO KIVYMD LAYOUT
KV = """
#####################################################JANELA DE INICIO##################################################
<Tela1>
    
    name:"t1"

    Image:
        canvas:
            Rectangle:
                source: 'Nf.png'
                size:self.size
                pos:self.pos  
                 

    Image:
        source: 'Nlogo.png'
        allow_stretch: True
        size_hint: 0.45, 0.55
        pos_hint: {'center_x': 0.555,'center_y': 0.60}
    
        
    MDFloatLayout:

        MDIconButton:
            icon: "close"
            theme_icon_color: "Custom"
            icon_color: "gray"
            pos_hint: {'center_x': 0.95,'center_y': 0.955}
            on_press:
                root.fechar() 
       

        MDFillRoundFlatIconButton:
            text: " INICIAR     " 
            icon: 'arrow-right'
            size_hint_x: .30
            theme_text_color: "Custom"
            text_color: "white"
            theme_icon_color: "Custom"
            icon_color: "white"
            pos_hint: {'center_x': 0.495,'center_y': 0.25} 
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current ='t2'
        
        MDLabel: 
            text: "PH.Development©"
            color: 'grey'
            font_size: 17
            halign: 'center'
            pos_hint: {'center_x': 0.90,'center_y': 0.03}                

############################################JANELA-PRINCIPAL########################################################
<Saida>
    
    name:"t2"

    Image:
        canvas:
            Rectangle:
                source: 'Nfundo.jpg'
                size:self.size
                pos:self.pos 

    Image:
        source: 'Nlogo.png'
        allow_stretch: True
        size_hint: 0.525, 0.18
        pos_hint: {'center_x': 0.525,'center_y': 0.84}

    MDFloatLayout:

        MDIconButton:
            icon: "arrow-left"
            theme_icon_color: "Custom"
            icon_color: "gray"
            pos_hint: {'center_x': 0.05,'center_y': 0.95}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current ='t1'
                root.limpar()

        MDIconButton:
            icon: "close"
            theme_icon_color: "Custom"
            icon_color: "gray"
            pos_hint: {'center_x': 0.95,'center_y': 0.95}
            on_press:
                root.fechar() 
        
        MDLabel: 
            text: "Média de Consumo "
            color: 'gray'
            font_size: 15
            halign: 'center'
            pos_hint: {'center_x': 0.15,'center_y': 0.72}

        MDTextField:
            id: ra
            size_hint_x: .43
            hint_text: " Km/L Alcool"
            max_height: "200dp"
            mode: "rectangle"
            fill_color: 0, 0, 0, 0
            pos_hint: {"center_x": .27, "center_y": .65}

        
        MDTextField:
            id: rg
            size_hint_x: .43
            hint_text: " Km/L Gasolina"
            max_height: "200dp"
            mode: "rectangle"
            fill_color: 0, 0, 0, 0
            pos_hint: {"center_x": .73, "center_y": .65}

        MDLabel: 
            text: "Valor do Combustivel"
            color: 'gray'
            font_size: 15
            halign: 'center'
            pos_hint: {'center_x': 0.15,'center_y': 0.55}

        MDTextField:
            id: vmx
            size_hint_x: .43
            hint_text: "R$-Max Gasolina"
            max_height: "200dp"
            mode: "rectangle"
            fill_color: 0, 0, 0, 0
            pos_hint: {"center_x": .27, "center_y": .48}

        MDTextField:
            id: vmn
            size_hint_x: .43
            hint_text: "R$-Min Gasolina"
            max_height: "200dp"
            mode: "rectangle"
            fill_color: 0, 0, 0, 0
            pos_hint: {"center_x": .73, "center_y": .48}

        MDFillRoundFlatIconButton:
            text: "  ANALISAR     " 
            icon: 'check'
            size_hint_x: .29
            theme_text_color: "Custom"
            text_color: "white"
            theme_icon_color: "Custom"
            icon_color: "white"
            pos_hint: {'center_x': 0.5,'center_y': 0.365} 
            on_press:
                root.analisar()
                

        MDLabel:
            id: resp 
            text: " "
            color: 'gray'
            font_size: 65
            halign: 'center'
            pos_hint: {'center_x': 0.5,'center_y': 0.26}

        MDLabel: 
            text: "PH.Development©"
            color: 'grey'
            font_size: 17
            halign: 'center'
            pos_hint: {'center_x': 0.90,'center_y': 0.03}

"""


#JANELA APRESENTAÇÃO
class Tela1(MDScreen):
    
    #Fechar a janela 
    def fechar(self):
        sys.exit()


#JANELA PRINCIPAL        
class Saida(MDScreen):

    #Limpar os campos anteriormente preenchidos
    def limpar(self):
        self.ids.ra.text = ''
        self.ids.rg.text = ''
        self.ids.vmx.text = ''
        self.ids.vmn.text = ''
        self.ids.resp.text = ''

    #Fechar a janela 
    def fechar(self):
        sys.exit()

    #Programa Principal   
    def analisar(self):
        #ENTRADAS 
        
        #Popup de Erro
        self.dialog = MDDialog(title = 'ERRO*', text = 'Por favor!\nInsira um valor válido',
                                buttons = [MDFlatButton(text= 'OK',
                                on_release = self.liberar)])

        try:
            #Coleta valores de entra e converte para float "gambirra"
            r1= str(self.ids.ra.text)
            rend_alc= float(r1.replace(',','.'))
            #Coleta valores de entra e converte para float "gambirra"
            r2= str(self.ids.rg.text)
            rend_gas= float(r2.replace(',','.'))
            #Coleta valores de entra e converte para float "gambirra"
            r3= str(self.ids.vmx.text)
            max_gas= float(r3.replace(',','.'))
            #Coleta valores de entra e converte para float "gambirra"
            r4= str(self.ids.vmn.text)
            min_gas= float(r4.replace(',','.'))

            #PROCESAMENTO
            
            #Calculo do valor medio da gasolina
            media_gas= float((max_gas + min_gas)/2)
            #Calculo do rendimento alcool x gasolina
            rend_ag= float(rend_alc / rend_gas)
            #Calculo da viabilidade da utilização do alcool
            max_alcool= rend_ag * media_gas

            #exporta os valores obtidos durante o calculo para o label resp
            self.ids.resp.text = ('O valor máximo P/ uso do ALCOOL\nNão devera passar de: R$ {:0.2f}'.format(max_alcool))
        except:
            self.dialog.open()
    
    #Função leração de erros
    def liberar(self, obj):
        self.dialog.dismiss()


#CLASSE DE ATIVAÇÃO
class FuelGaugeApp(MDApp):
    
    def build(self):
        Builder.load_string(KV)
        sm = MDScreenManager()
        sm.add_widget(Tela1())
        sm.add_widget(Saida())
       
        return sm


#INICIALIZAÇÃO DO PROGRAMA
FuelGaugeApp().run()

#OH DEUS MAGNIFICO COMO TU NÃO HÁ, DONO DO CONHECIMENTO SOU GRATO POR VÓS TER COMPARTILHADO UM POUCO COM ESTE HUMILDE FILHO QUE TE AMA E TE ADORA, GLORIAS A TI MEU CRIADOR OBRIGADO!!! 