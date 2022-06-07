from tkinter import PhotoImage, filedialog
from tkinter import Button, Label, Tk, Entry
from PIL import Image, ImageFilter, ImageTk


def ChangeMainImageLabel(imagePath : str) -> None:
    global imageLabel
    currentImage = Image.open(imagePath)
    resizedCurrentImage = currentImage.resize((500, 480))
    newMainImageLabelPhoto = ImageTk.PhotoImage(resizedCurrentImage)
    imageLabel.configure(image=newMainImageLabelPhoto)
    imageLabel.image = newMainImageLabelPhoto


def ChangeSizeEntries(imagePath : str) -> None:
    global xSizeEnter, ySizeEnter
    currentImage = Image.open(imagePath)
    xSizeEnter.delete(0, len(xSizeEnter.get()))
    ySizeEnter.delete(0, len(ySizeEnter.get()))
    xSizeEnter.insert(0, str(currentImage.size[0]))
    ySizeEnter.insert(0, str(currentImage.size[1]))


def ChangeMainImageNameLabel(imagePath : str) -> None:
    global imageNameLabel
    imageNameLabel.configure(text=f"Назва: {imagePath.split('/')[-1]}")


def ChangeMainImage() -> None:
    """Changes current picture file and its label to show on the screen"""
    global mainImagePath
    mainImagePath = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                               filetypes=(("JPG", "*.jpg"), ("BMP", "*.bmp")))
    ChangeMainImageLabel(mainImagePath)
    ChangeMainImageNameLabel(mainImagePath)
    ChangeSizeEntries(mainImagePath)


def SaveImage():
    """Saves current selected image"""
    global mainImagePath
    global imageFormat, changeImageFilter, imageSize
    global xSizeEnter, ySizeEnter
    mainImage = Image.open(mainImagePath)
    mainImage = mainImage.convert("RGB")    # it doesn't allow working with JPG without RGB
    if changeImageFilter:
        mainImage.filter(ImageFilter.DETAIL)
    imageSize = (int(xSizeEnter.get()), int(ySizeEnter.get()))
    mainImage = mainImage.resize(imageSize)
    mainImage.save(f"NewImages/{mainImagePath.split('/')[-1][:-4]}_changed{imageFormat}")


def ChangeFormat(changeTO: str):
    """Changes current format
    and related buttons"""
    global imageFormat
    global jpgButton, bmpButton
    imageFormat = changeTO
    if imageFormat == ".jpg":
        jpgButton.configure(bg="cyan")
        bmpButton.configure(bg="white")
    else:
        jpgButton.configure(bg="white")
        bmpButton.configure(bg="cyan")


def SetFilter(isSetFilter: bool):
    """Changes the image's filter
    and related buttons"""
    global changeImageFilter
    global filterButton, nonFilterButton
    changeImageFilter = isSetFilter
    if changeImageFilter:
        filterButton.configure(bg="cyan")
        nonFilterButton.configure(bg="white")
    else:
        filterButton.configure(bg="white")
        nonFilterButton.configure(bg="cyan")


if __name__ == '__main__':
    # Creation of the main window
    mainWindow = Tk()
    mainWindow.geometry("1000x610")
    mainWindow.resizable(False, False)

    # Image set
    mainImagePath = "FactoryImages/cat.jpg"
    imageFormat = ".jpg"
    changeImageFilter = False
    imageSize = Image.open(mainImagePath).size

    # Background image
    background_image = PhotoImage(file="FactoryImages/BackPhoto.png")
    backgroundLabel = Label(mainWindow, image=background_image)

    # Main image label
    imageLabel_photo = ImageTk.PhotoImage(Image.open(mainImagePath))
    imageLabel = Label(mainWindow, image=imageLabel_photo)

    # Change and save buttons
    changeImageButton = Button(mainWindow, fg="black", bg="white", height=2, width=30,
                               text="Змінити зображення", command=ChangeMainImage)
    saveButton = Button(mainWindow, fg="black", bg="white", height=2, width=30,
                        text="Зберігти фото", command=SaveImage)

    # Image file name without its path
    imageNameLabel = Label(mainWindow, fg="lime", bg="black", height=2, width=35,
                     text=f"Назва: {mainImagePath.split('/')[-1]}", font=3)

    # Format change
    formatText = Label(mainWindow, fg="white", bg="black", height=2, width=35,
                     text=f"Оберіть формат", font=3)
    # Button, that changes format to jpg
    jpgButton = Button(mainWindow, bg="cyan", height=1, width=15, borderwidth=0,
                       text="JPG", font=13, command=lambda: ChangeFormat(".jpg"))
    # Button, that changes format to bmp
    bmpButton = Button(mainWindow, bg="white", height=1, width=15, borderwidth=0,
                       text="BMP", font=13, command=lambda: ChangeFormat(".bmp"))

    # Size change
    sizeText = Label(mainWindow, fg="white", bg="black", height=2, width=35,
                       text=f"Введіть розмір", font=3)

    xSizeEnter = Entry(fg="black", bg="white", font=10, justify="center")
    ySizeEnter = Entry(fg="black", bg="white", font=10, justify="center")
    xSizeEnter.insert(0, str(imageSize[0]))
    ySizeEnter.insert(0, str(imageSize[1]))

    # Filter change
    filterText = Label(mainWindow, fg="white", bg="black", height=2, width=35,
                       text=f"Оберіть фільтр", font=3)
    filterButton = Button(mainWindow, bg="white", height=1, width=15, borderwidth=0,
                          text="Detail", font=13, command=lambda: SetFilter(True))
    nonFilterButton = Button(mainWindow, bg="cyan", height=1, width=15, borderwidth=0,
                             text="Standart", font=13, command=lambda: SetFilter(False))

    # Buttons' placing
    saveButton.place(x=170, y=560)
    changeImageButton.place(x=170, y=12)
    jpgButton.place(x=570, y=160)
    bmpButton.place(x=780, y=160)
    filterButton.place(x=570, y=508)
    nonFilterButton.place(x=780, y=508)

    # Labels' placing
    backgroundLabel.place(x=0, y=0)
    imageLabel.place(x=40, y=60)
    imageNameLabel.place(x=570, y=12)
    formatText.place(x=570, y=100)
    sizeText.place(x=570, y=280)
    filterText.place(x=570, y=448)

    # Size enter
    xSizeEnter.place(x=570, y=340, height=35, width=170)  # there's no such a parameter "height" in entry
    ySizeEnter.place(x=780, y=340, height=35, width=170)  # that's why we change the size here

    mainWindow.mainloop()
