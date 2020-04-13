from selenium import webdriver
import time

class whatsappbot:
    def __init__(self):
        self.mensagem = "Bom dia pessoal!!! Que a paz do Senhor esteja convosco."
        self.grupos = ["Manu","Família Braga Lira"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        # <span dir="auto" title="Manu" class="_1wjpf _3NFp9 _3FXB1">Manu</span>
        # <div tabindex="-1" class="_3F6QL _2WovP">
        # <div class="weEq5">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(10)
        for grupo in self.grupos:
            grupo = self.driver.find_elements_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3F6QL _2WovP')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

bot = whatsappbot()
bot.EnviarMensagens()