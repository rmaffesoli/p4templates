import os
from PyQt6.QtWidgets import QApplication

from p4_templates.ui.p4_template_loader_gui import P4TemplateLoaderDialog

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    os.chdir(script_dir)

    app = QApplication([])
    P4TemplateLoaderDialog()