#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import time
import sys

def verificar_nprogress_o_toast(driver, tiempo_total=2, intervalo=0.2):

    inicio = time.time()
    nprogress_detectado = False
    toast_mensaje = None

    while time.time() - inicio < tiempo_total:
        try:
            nprogress = driver.find_element(By.ID, "nprogress")
            if nprogress.is_displayed():
                nprogress_detectado = True
        except NoSuchElementException:
            pass

        try:
            toast = driver.find_element(By.XPATH, "//div[contains(@class, 'toast-container')]//div[1]")
            if toast.is_displayed():
                toast_mensaje = toast.text
                break  
        except NoSuchElementException:
            pass

        sleep(intervalo)

    if nprogress_detectado:
        print("Se ha recolectado la ganancia diaria.")
    elif toast_mensaje:
        print(toast_mensaje)
    else:
        print("No se detectó ninguna acción después de presionar el botón.")

def recolectar_ganancia(driver):

    try:
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/nav/a[4]').click(); sleep(5)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/button'))).click(); sleep(0.5)
        verificar_nprogress_o_toast(driver)
    except Exception as e:
        print(e)
    finally:
        driver.quit()

def login(driver, num_celular, num_password):

    try:
        celular = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/form/div[1]/div/input'))); celular.send_keys(num_celular)
        contrasena = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/form/div[2]/input'))); contrasena.send_keys(num_password)
        ingresar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/form/button[1]')))
        ingresar.click(); sleep(10)

    except Exception as e:
        print(e)

    recolectar_ganancia(driver)

def iniciar_proceso():

    try:
        if len(sys.argv) == 3:
            args = Options()
<<<<<<< HEAD
            args.add_argument("--headless=new")
=======
            args.add_argument("--headless")
            args.add_argument("--no-sandbox")
            args.add_argument("--disable-dev-shm-usage")
>>>>>>> 29b9901c7ee07627758803329546827b674b12b4
            driver = webdriver.Chrome(options=args)
            #driver = webdriver.Chrome()
            driver.get('https://sg-wind.com/#/login'); sleep(5)
            
            if len(sys.argv[1]) == 10:
                login(driver, num_celular=sys.argv[1], num_password=sys.argv[2])
            else:
                print("Suministre un numero valido de celular")
        else:
            print("Se requiere que se pasen como argumentos el numero de celular y la contrasena de acceso.")

    except Exception as e:
        print(e)

if __name__ == '__main__':
    iniciar_proceso()
