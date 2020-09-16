import os
import subprocess
from pathlib import Path


class PasswordSetter:

    def __init__(self):
        pass

    def setPassword(self, excel_file_path, password):
        """Locks excel file with password. Modification allowed only when password is entered"""

        # excel_file_path = Path(os.path.abspath(excel_file_path))
        excel_file_path = Path(excel_file_path)

        vbs_script = \
        f"""' Save with password required upon opening

        Set excel_object = CreateObject("Excel.Application")
        Set workbook = excel_object.Workbooks.Open("{excel_file_path}")

        excel_object.DisplayAlerts = False
        excel_object.Visible = False

        workbook.SaveAs "{excel_file_path}",,, "{password}"

        excel_object.Application.Quit
        """

        # write
        vbs_script_path = excel_file_path.parent.joinpath("set_password.vbs")
        with open(vbs_script_path, "w") as file:
            file.write(vbs_script)

        # execute
        subprocess.call(['cscript.exe', str(vbs_script_path)], creationflags=subprocess.CREATE_NO_WINDOW)

        # remove
        vbs_script_path.unlink()

        return None
