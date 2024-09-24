import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ControlLight
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Baskerville Old Face", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(162, 21)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(582, 379)
        self._label1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ControlLight
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._button1.Font = System.Drawing.Font("Baskerville Old Face", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(23, 21)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(84, 87)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ControlLight
        self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._button2.Font = System.Drawing.Font("Baskerville Old Face", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(23, 157)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(84, 87)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ControlLight
        self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._button3.Font = System.Drawing.Font("Baskerville Old Face", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(23, 313)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(84, 87)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(1017, 421)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Schedule"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "1. AP Physics\n2. Spanish III\n3. Civil Engineer and Architexture\n4. Teams Sports\n5. English 11 Honors\n6. AP Pre-calc\n7. AP European History\n8. Computer Programming I"

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()