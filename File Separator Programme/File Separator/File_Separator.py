from tkinter import Tk,Canvas,Entry,Button,filedialog,END,StringVar,messagebox,ttk
import os
import shutil


#region Code_



def list_file_extensions(folder_path):
    extension_list = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            _, extension = os.path.splitext(item)
            if extension not in extension_list:
                extension_list.append(extension)
    return extension_list

def create_dir(folder_path,output_path):
    ext_list=list_file_extensions(folder_path)

    for directory in ext_list:
        dir=os.path.join(output_path, directory)
        if not os.path.exists(dir):
            os.makedirs(dir)

def file_process(folder_path,output_path,mode):

    create_dir(folder_path,output_path)
    
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        
        if os.path.isfile(item_path):
            _, extension = os.path.splitext(item)

            out_path=os.path.join(output_path,extension+'\\'+item)

            process(item_path,out_path,mode)
            

def process(item_path,out_path,mode):

    match mode:
        case 'Copy':
            shutil.copy(item_path,out_path)
        case 'Move':
            shutil.move(item_path,out_path)
        case _:
            shutil.copy(item_path,out_path)
    

def path_exist_check(folder_path,output_path):

    if(folder_path!='' and output_path!=''):

        is_folder_path=os.path.exists(folder_path)
        is_outout_path=os.path.exists(output_path)

        if(is_folder_path or is_outout_path):
            if(is_folder_path==False):
                return 'IFNE'
            if(is_outout_path==False):
                return 'OFNE'
            
            if(is_folder_path and is_outout_path):
                return 'AllSet'
            
        else:
            return 'NoPathExist'


    else:

        return 'NoPathSet'


#endregion


#region Code

def select_input_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_input.delete(0, END)  # Clear any previous path
        entry_input.insert(END, folder_path)

def select_output_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_output.delete(0, END)  # Clear any previous path
        entry_output.insert(END, folder_path)

is_click=True

def start():
    global is_click

    if(is_click):

        is_click=False

        input_folder_path=input_folder.get()
        output_folder_path=output_folder.get()

        path_info=path_exist_check(input_folder_path,output_folder_path)


        if path_info=='AllSet':
            mode=dropdown_list.get()
            file_process(input_folder_path,output_folder_path,mode)
            messagebox.showinfo('Success','                 Done                   ')
            is_click=True
           
        else:

            if path_info=='NoPathSet':
                messagebox.showerror('error','                  No Path Set                 ')
                is_click=True
                return
            if path_info=='NoPathExist':
                messagebox.showerror('error','Input And Output Folder not Exist')
                is_click=True
                return
            if path_info=='IFNE':
                messagebox.showerror('error','Input Folder not exist')
                is_click=True
                return
            if path_info=='OFNE':
                messagebox.showerror('error','Output Folder not exist')
                is_click=True
                return
            
            messagebox.showerror('error','Path Properly Set')

#endregion
            
# Window

window = Tk()

window.geometry("455x384")
window.title('File Separator')
window.configure(bg = "#FFFFFF")



#region Design 

canvas = Canvas(
    window,
    bg = "#F6FEFE",
    height = 384,
    width = 455,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"

)

canvas.place(x = 0, y = 0)

canvas.create_rectangle(
    48.0,
    48.0,
    407.0,
    128.0,
    fill="#F6FEFE",
    width=2,
    outline="#3D5A80")

canvas.create_rectangle(
    48.0,
    152.0,
    407.0,
    232.0,
    fill="#F6FEFE",
    width=2,
    outline="#3D5A80")


button_input = Button(
    text='Select',
    background="#293241",
    foreground="#F6FEFE",
    borderwidth=0,
    font=("Consolas Bold", 8),
    command=select_input_folder,
)
button_input.place(
    x=339.0,
    y=88.0,
    width=60.0,
    height=28.0
)


button_output = Button(
    text='Select',
    background="#293241",
    foreground="#F6FEFE",
    borderwidth=0,
    font=("Consolas Bold", 8),
    command=select_output_folder,
)
button_output.place(
    x=339.0,
    y=192.0,
    width=60.0,
    height=28.0
)


button_start = Button(
    text='Start',
    background="#EE6C4D",
    foreground='#F6FEFE',
    font=("Consolas Bold", 14 ),
    borderwidth=0,
    command=start,
)
button_start.place(
    x=239.0,
    y=296.0,
    width=95.0,
    height=40.0
)


canvas.create_text(
    64.0,
    56.0,
    anchor="nw",
    text="INPUT FOLDER",
    fill="#3D5A80",
    font=("Consolas Bold", 18 * -1)
)

canvas.create_text(
    64.0,
    160.0,
    anchor="nw",
    text="OUTPUT FOLDER",
    fill="#3D5A80",
    font=("Consolas Bold", 18 * -1)
)

input_folder=StringVar()

entry_input = Entry(
    window,
    textvariable=input_folder,
    bd=0,
    bg="#E3F2F6",
    fg="#3D5A80",
)
entry_input.place(
    x=66.0,
    y=92.0,
    width=263.0,
    height=18.0
)

output_folder=StringVar()
entry_output = Entry(
    window,
    textvariable=output_folder,
    bd=0,
    bg="#E3F2F6",
    fg="#3D5A80",
)
entry_output.place(
    x=66.0,
    y=196.0,
    width=263.0,
    height=18.0
)

options=['Copy','Move']
dropdown_option=StringVar(value=options[0])
dropdown_list=ttk.Combobox(window,
                           textvariable=dropdown_option,
                           foreground="#293241",
                           justify='center',
                           font=("Consolas Bold", 14 ),
                           state="readonly")
dropdown_list['values']=options

dropdown_list.place(
    x=120.0,
    y=296.0,
    width=95.0,
    height=40.0
)

#endregion


window.resizable(False, False)
window.mainloop()



