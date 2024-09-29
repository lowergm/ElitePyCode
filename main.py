# Inicio do código

# Imports
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.codeinput import CodeInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooser
import io
import sys

# Classe principal
class ElitePyCode(App):
    # Função para criar o layout
    def build(self):
        # Criar o layout na horientação vertical |
        self.layout = BoxLayout(orientation='vertical')
        
        # Barra de ferramentas
        self.layout_button = BoxLayout(orientation='horizontal', size_hint_y=None)
        
        # Área para escrever o código
        self.code = CodeInput()
        
        # Botão para executar o código
        self.execute_button = Button(text='Execute', size_hint=(None, None), size=(200, 100))
        
        self.execute_button.bind(on_press=self.execute_code)
        
        # Botão para salvar o arquivo
        self.save_button = Button(text='Save', size_hint=(None, None), size=(200, 100))
        
        self.save_button.bind(on_press=self.save_file)
        
        # Adicionar o tab no código
        self.tab_button = Button(text='Tab', size_hint=(None, None), size=(200, 100))
        
        # Função de clique no tab para adiconar um \t ou tab, no código
        self.tab_button.bind(on_press=self.tab)
        
        # Adicionar o botão do tab no menu de ferramentas
        self.layout_button.add_widget(self.tab_button)
        
        # Adicionar a área para escrever códigos no layout
        self.layout.add_widget(self.code)
        
        # Adicionar o botão para executar códigos no menu de ferramentas
        self.layout_button.add_widget(self.execute_button)
        
        # Adicionar o botão para salvar no menu de ferramentas
        self.layout_button.add_widget(self.save_button)
        
        # Adicionar o menu de ferramentas ao layout
        self.layout.add_widget(self.layout_button)
        
        # Saida do terminal
        self.saida = Label(text='No code executed', size_hint_y=1.)
        self.saidaAuxilio = Label(text="")
        # Criar o terminal
        self.terminal = BoxLayout(orientation='horizontal')
		
        # Adicionar um texto ao terminal
        self.terminal.add_widget(self.saida)
        self.terminal.add_widget(self.saidaAuxilio)
        
        self.layout.add_widget(self.terminal)
        
        # Mostrar o layout
        return self.layout
    
    # Função do tab
    def tab(self, instance):
    	# Adicionar o tab ao texto atual da área de codificação
    	self.code.text= self.code.text + "\t"
    
    def execute_code(self, instance):
    	old_stdout = sys.stdout
    	new_stdout = io.StringIO()
    	sys.stdout = new_stdout
    	
    	# Executar o código
    	try:
    		exec(self.code.text)
    	except Exception as e:
    		print(f"Erro: {e}")
    	
    	sys.stdout = old_stdout
    	
    	# Obter a saida do código
    	output = new_stdout.getvalue()
    	
    	self.saida.text=output
    
    
    def save_file(self, instance):
    	self.popup = Popup(title="Salvar Arquivo", content=TextInput(hint_text="Insira o nome do arquivo"), size_hint=(None, None), size=(400, 200))
    	self.file_chooser = FileChooser()
    	self.file_chooser.dirselect = True
    	
    def onPopupConfirm(self, instance):
     file_name = self.popup.content.text
     selected_dir = self.file_chooser.selection[0]
     file_path = os.path.join(selected_dir, file_name + ".py")
     
     with open(file_path, 'w') as file:
     	file.write(self.code.text)
     	print(f"Arquivo salvo em {file_path}")
     
     self.popup.content.bind(on_text_validate=onPopupConfirm)
     self.popup.open()
     self.file_chooser.open()
     
# Rodar o app
if __name__ == '__main__':
	ElitePyCode().run()

# Fim do código
