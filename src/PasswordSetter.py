import os
import subprocess
from pathlib import Path
import re


class PasswordSetter:

    def __init__(self):
        pass

    def setPassword(self, excel_file_path, name, password):
        """Locks excel file with password. Modification allowed only when password is entered"""

        folder_path = Path(os.path.normpath(os.path.dirname(excel_file_path)))
        name_to_save = 'a' + name
        excel_file_path = Path(os.path.normpath(os.path.join(folder_path, name)))
        excel_file_path_to_save = Path(os.path.normpath(os.path.join(folder_path, name_to_save)))


        vbs_script = \
        f"""' Save with password required upon opening

        Set excel_object = CreateObject("Excel.Application")
        Set workbook = excel_object.Workbooks.Open("{excel_file_path}")

        excel_object.DisplayAlerts = False
        excel_object.Visible = False

        workbook.SaveAs "{excel_file_path_to_save}",,, "{password}"

        workbook.Close

        excel_object.Application.Quit
        """

        # write
        vbs_script_path = excel_file_path.parent.joinpath("set_password.vbs")
        with open(vbs_script_path, "w") as file:
            file.write(vbs_script)

        # execute
        result = subprocess.Popen(['cscript.exe', str(vbs_script_path)], creationflags=subprocess.CREATE_NO_WINDOW, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = result.communicate()
        res = {
            "result": output.decode(encoding='cp866'),
            "err": self._errMessage(err.decode(encoding='cp866'))
        }

        # Remove the old file and rename the new one
        self._rename(excel_file_path_to_save, excel_file_path)
        
        # remove
        vbs_script_path.unlink()

        return res

    def _errMessage(self, err):
        patern = r'Microsoft Excel\:.*'
        error = re.search(patern, err)
        if err:
            return error.group()
        return None

    def _rename(self, initial_path, renamed_path):
        os.unlink(renamed_path)
        os.rename(initial_path, renamed_path)
