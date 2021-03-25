import os
import sys
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
from PySide2 import QtCore

from PySide2.QtWidgets import (QApplication, QDialog, QFileDialog, QMainWindow,
                               QMessageBox)

from main_window1 import UI_PDFMarginWindow


class PDFMarginWindow(UI_PDFMarginWindow):
    def __init__(self):
        self.file_check = False
        self.delete_orig = False
        self.input = None
        self.output = None
        self.multi = None
        self.x = 1.0
        self.y = 1.0
        super().__init__()

    def validate_all(self):
        permissions = []
        self.debug("Checking an input path has been set...")
        if not self.input and not self.multi:
            # fail if no input supplied
            self.debug("No input selected.")
            self.alert("Must select either a "
                       "directory or .pdf file in order to continue.")
            return False
        self.debug("Pass!")

        self.debug("Checking one input path selected...")
        if self.input and self.multi:
            # fail if input and multi selected
            self.debug("Input dir and multiple files selected.")
            self.alert("Cannot have both an "
                       "input directory and multiple files selected.")
            return False
        self.debug("Pass!")

        self.debug("Checking output dir set.")
        if not self.output:
            self.debug("No output dir.")
            self.alert("Must select an output "
                       "directory for new pdfs to be written to.")
            return False
        self.debug("Pass!")

        self.debug("Checking margin sizes...")
        if self.x > 10.0 or self.y > 10.0:
            # fail if margins greater than 10 inches
            self.debug("Margins greater than 10 inches.")
            self.alert("Sorry, this program does "
                       "not support margins greater than 10 inches.")
            return False
        self.debug("Pass!")

        self.debug("Checking input path existance...")
        if self.input and not self.multi:
            # verify only input and not multi fail if input path does not exist
            if not self.input.exists():
                self.debug(f"Input directory does not exist: {self.input}")
                self.alert("Your input directory does not exist.")
                return False
        if self.multi and not self.input:
            # verify only multi and not input and paths exist
            invalid = [x for x in self.multi if not x.exists()]
            if len(invalid) > 0:
                msg = '\n'.join(invalid)
                self.debug(f"The following files do not exist:\n{msg}")
                self.alert("File does not exist! See log.")
                return False
        self.debug("Pass!")

        self.debug("Checking if output dir needs to be made...")
        if self.output.exists():
            # try to make output dir or fail
            try:
                self.output.mkdir(parents=True, exist_ok=False)
            except FileExistsError:
                self.debug("Directory already exists, not making a new one.")
            else:
                self.debug(f"{self.output} made!")

        self.debug("Checking permissions...")
        perm_fail = []
        if self.input:
            permissions.append(self.input)
        if self.multi:
            permissions.extend([x for x in self.multi if x])
            perm_fail.extend([y for y in permissions if not os.access(y, os.R_OK)])
        if not os.access(self.output, os.W_OK):
            perm_fail.append(self.output)
        if len(perm_fail) > 0:
            msg = '\n'.join(perm_fail)
            self.debug(f"You do not have access to the following:\n{msg}")
            self.alert("Access error!")
            return False
        self.debug("All checks passed! Writing pdfs.")
        return True

    def debug(self, msg):
        self.debug_textBrowser.append(msg)
    def clear(self):
        self.debug_textBrowser.clear()
    def setupUI(self, MW):
        super().setupUI(MW)
    def settle_dialog(self, dialog):
        self.debug_textBrowser.clear()
        self.input = None
        self.multi = None
        if len(dialog) > 1:
            self.multi = [Path(x) for x in dialog]
            self.debug_textBrowser.append('\n'.join(dialog))
        else:
            self.input_lineEdit.setText(dialog[0])
            self.input = Path(dialog[0])

    def inputBrowseSlot(self):
        if self.file_check:
            dialog = FileDialog(directory=str(Path.home()), fmt='pdf', isFolder=False)
        else:
            dialog = FileDialog(directory=str(Path.home()), fmt='pdf', isFolder=True)
        if dialog:
            self.settle_dialog(dialog)


    def outputBrowseSlot(self):
        dialog = FileDialog(directory=str(Path.home()), isFolder=True)
        if dialog:
            self.output_lineEdit.setText(dialog[0])
            self.output = Path(dialog[0])

    def input_text_editFinishedSlot(self):
        self.settle_dialog([self.input_lineEdit.text()])

    def output_text_editFinishedSlot(self):
        self.output = Path(self.output_lineEdit.text())

    def x_editFinishedSlot(self):
        self.x = float(self.lr_lineEdit.text())

    def y_editFinishedSlot(self):
        self.y = float(self.tb_lineEdit.text())

    def files_checkSlot(self):
        self.file_check = self.files_checkBox.isChecked()
        print(self.file_check)

    def delete_checkSlot(self):
        self.delete_orig = self.delete_checkBox.isChecked()
        print(self.delete_orig)

    def alert(self, msg):
        msgBox = QMessageBox()
        msgBox.setText(msg)
        msgBox.exec_()

    def createSlot(self):
        self.clear()
        self.debug('Validating...')
        valid = self.validate_all()
        response = parse_pdfs(root=self,
                           input=self.input,
                           pdfs=self.multi,
                           out=self.output,
                           x=self.x,
                           y=self.y,
                           delete=self.delete_orig)
        self.progressBar.reset()
        self.debug(response)


def FileDialog(directory='', forOpen=True, fmt='', isFolder=False):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    options |= QFileDialog.DontUseCustomDirectoryIcons
    dialog = QFileDialog()
    dialog.setOptions(options)

    dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)

    # ARE WE TALKING ABOUT FILES OR FOLDERS
    if isFolder and fmt =='':
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOptions(QFileDialog.ShowDirsOnly)
    elif isFolder and fmt !='':
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setNameFilters([f'{fmt} (*.{fmt})'])
    else:
        dialog.setFileMode(QFileDialog.ExistingFiles)

    # OPENING OR SAVING
    dialog.setAcceptMode(QFileDialog.AcceptOpen) if forOpen else dialog.setAcceptMode(QFileDialog.AcceptSave)

    # SET FORMAT, IF SPECIFIED
    if fmt != '' and isFolder is False:
        dialog.setDefaultSuffix(fmt)
        dialog.setNameFilters([f'{fmt} (*.{fmt})'])

    # SET THE STARTING DIRECTORY
    if directory != '':
        dialog.setDirectory(str(directory))
    else:
        dialog.setDirectory(str(ROOT_DIR))

    if dialog.exec_() == QDialog.Accepted:
        path = dialog.selectedFiles()
        return path
    else:
        return ''





def get_info(path, name, out_path, x_mult, y_mult, delete, window):
    with open(path, 'rb') as f:
        p = PdfFileReader(f)
        info = p.getDocumentInfo()
        number_of_pages = p.getNumPages()
        writer = PdfFileWriter()
        marginx = int(72*x_mult)
        marginy = int(72*y_mult)
        window.debug(f'\nConverting {name}')
        window.progressBar.setTextVisible(True)
        window.progressBar.setRange(0, number_of_pages-1)
        for i in range(number_of_pages):
            window.progressBar.setValue(i)
            page = p.getPage(i)
            new_page = writer.addBlankPage(
                page.mediaBox.getWidth() + 2 * marginx,
                page.mediaBox.getHeight() + 2 * marginy
            )
            new_page.mergeScaledTranslatedPage(page, 1, marginx, marginy)
        '''
        for i in tqdm(range(number_of_pages)):
            page = p.getPage(i)
            new_page = writer.addBlankPage(
                page.mediaBox.getWidth() + 2 * marginx,
                page.mediaBox.getHeight() + 2 * marginy
            )
            new_page.mergeScaledTranslatedPage(page, 1, marginx, marginy)
            # writer.addPage(new_page)'''
        new_name = '_' + name
        outpath = out_path / new_name
        with open(outpath, 'wb') as f:
            writer.write(f)
    if delete:
        os.remove(path)
        window.debug(f"Deleted {path}.")


def parse_pdfs(**kwargs):
    pdfs = []
    window = kwargs["root"]
    if kwargs["input"]:
        pdfs = sorted(kwargs["input"].glob('*.pdf'))
    elif len(kwargs["pdfs"]) > 0:
        pdfs = kwargs["pdfs"]
    out_path = kwargs["out"]
    x_mult = float(kwargs["x"])
    y_mult = float(kwargs["y"])
    delete = kwargs["delete"]
    if len(pdfs) > 0:
        for pdf in pdfs:
            get_info(pdf, pdf.name, out_path, x_mult, y_mult, delete, window)
        return f"Wrote {len(pdfs)} new files in {out_path}."
    else:
        return "No input passed."


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = PDFMarginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
