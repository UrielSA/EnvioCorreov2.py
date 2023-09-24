import  tkinter as Tk 
import smtplib
from tkinter import messagebox

colorBoton= "#B5E5ED"
#ventana principal
ventana=Tk.Tk()
ventana.title("Ciber Bullis")
ventana.geometry("1200x720")
#Nombre de empresa
Nempresa=Tk.Label(ventana,text="Ciber Bullis", font=("arial",25) )
Nempresa.pack()

#Numero del cliente
NCliente=Tk.Label(ventana,text="Numero de Telefono:")
NCliente.place(x="633",y="100")

#Entrada Numero cliente
ENumeroCliente=Tk.Entry(ventana,width=30,bg="#C5FDFC")
ENumeroCliente.place(x="750",y="100")

#texto nombre cliente
preguntaNom=Tk.Label(ventana,text="Nombre del cliente: ")
preguntaNom.place(x="320",y="100")

#entrada de Nombre de cliente
ENombre=Tk.Entry(ventana,width=30,bg="#C5FDFC")
ENombre.place(x="430",y="100")

#texto Pregunta Marca
PMarcEquipo=Tk.Label(ventana,text="Marca del equipo:  ")
PMarcEquipo.place(x="650",y="150")

#entrada de marca equipo
EMarca=Tk.Entry(ventana,width=30,bg="#C5FDFC")
EMarca.place(x="750",y="150")

#texto Problema Equipo

txtProblema=Tk.Label(ventana,text="Describe el Problema del equipo detalladamente")
txtProblema.place(x="500",y="190")


#Descripcion Probelma del equipo
Problema=Tk.Text(ventana,height="20", bg="#C5FDFC")
Problema.place(x="313",y="220")

#Texto Pregunta si es Lap Top o Celular u otro

pregunta=Tk.Label(ventana,text="¿Que equipo es?\n lapTop,celular,CPU,ALL IN ONE :")
pregunta.place(x=310,y=130)

Equipo=Tk.Entry(ventana,bg="#C5FDFC")
Equipo.place(y=144,x=490)

correo_cliente=Tk.Label(ventana,text="Correo cliente(Opcional):", fg="red")
correo_cliente.place(x=310,y=550)

correo_cliente_en=Tk.Entry(ventana,bg=colorBoton)
correo_cliente_en.place(x=453,y=550)






#Funcion mandar correo

# Función para enviar el correo electrónico
def enviar_correo():
    # Configura la conexión SMTP
    smtp_server = 'smtp.office365.com'  # Reemplaza con el servidor SMTP adecuado
    smtp_port = 587  # Reemplaza con el puerto SMTP adecuado
    smtp_username = 'cookiesone1@hotmail.com'  # Reemplaza con tu dirección de correo electrónico
    smtp_password = 'GiioGalleta25Y1'  # Reemplaza con tu contraseña de correo electrónico

    # Crea una conexión SMTP
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Obtiene los datos del formulario
        destinatario = "sagcookies@gmail.com"
        dest2=correo_cliente_en.get()
        
        NumeroCliente = ENumeroCliente.get()
        NombreCliente = ENombre.get()
        MarcaEquipo = EMarca.get()
        equipo= Equipo.get()
        mensaje = Problema.get("1.0",Tk.END )

      
        # Crea el correo electrónico

        
        correo = f"Subject: {NombreCliente}\nTo: {destinatario} {dest2} \n\n Muchas gracias por confiar en nosotros! :D\n\n{NombreCliente}\n\n Su numero de contacto es: {NumeroCliente}\n\nSu equipo es: {equipo }\n\n La marca de su equipo es : {MarcaEquipo }\n\nEl problema de su equipo es el siguiente:  {mensaje}\n\nSi alguno de los datos es incorrecto comuniquese con nosotros\n\nQueremos informarle que una vez recibamos su equipo para su revision y diagnostico\n\n nuestro tecnico Uriel realizara una evaluacion exhaustiva para identificar y diagnosticar cualquier problema que pueda estar afectando su dispositivo."

        destinatarios=[destinatario , dest2]
        # Envía el correo electrónico
        server.sendmail(smtp_username, destinatarios,correo)
        server.quit()
        

        messagebox.showinfo("Éxito", "Correo electrónico enviado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"Error al enviar el correo electrónico: {str(e)}")
        
        

def limpiar ():
    ENumeroCliente.delete(0,"end")
    ENombre.delete(0,"end")
    EMarca.delete(0,"end")
    Equipo.delete(0,"end")
    Problema.delete("1.0","end")
    correo_cliente_en.delete(0,"end")


    

enviar_button = Tk.Button(ventana, text="Enviar", command=enviar_correo,bg=colorBoton)
enviar_button.place(x=870,y=590)

limpiar_l=Tk.Label(ventana,text="Limpia datos en pantalla")
limpiar_l.place(x=710,y=560)

limpiarText=Tk.Button(text="limpiar", command=limpiar, bg=colorBoton)
limpiarText.place(x=750,y=590)

ventana.resizable(False, False)

ventana.mainloop()